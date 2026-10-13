"""Resume local commands and validate native-agent completions on the same task DAG."""
import json
import subprocess
import time
import uuid
from pathlib import Path

from .dispatch import context_fingerprints, make_packet
from .model import digest, fingerprints, load_manifest, local_path
from .store import Store, now


class Engine:
    def __init__(self, root, manifest, state_dir=".harness"):
        self.root = Path(root).resolve()
        if not self.root.is_dir():
            raise ValueError("Workspace root must be an existing directory.")
        manifest = Path(manifest)
        self.manifest_path = manifest.resolve() if manifest.is_absolute() else (self.root / manifest).resolve()
        self.manifest, self.tasks = load_manifest(self.manifest_path, self.root)
        self.state_dir = local_path(self.root, state_dir)
        for task in self.tasks.values():
            for name in task["inputs"] + task["outputs"]:
                path = local_path(self.root, name)
                if path == self.state_dir or self.state_dir in path.parents:
                    raise ValueError("Task artifacts must not overwrite or depend on coordinator state.")
        self.store = Store(self.state_dir / "state.sqlite3")
        self.sync()

    def sync(self):
        db = self.store.db
        with self.store.transaction():
            existing = self.store.rows()
            removed = set(existing) - set(self.tasks)
            if any(existing[i]["state"] == "running" for i in removed):
                raise ValueError("Recover running tasks before removing them from the manifest.")
            for i in removed:
                self.store.event(i, "removed", {"prior": existing[i]})
                db.execute("DELETE FROM tasks WHERE id=?", (i,))
            for i, task in self.tasks.items():
                spec = json.dumps(task, sort_keys=True)
                if i not in existing:
                    db.execute("INSERT INTO tasks(id,spec,state) VALUES (?,?,?)", (i, spec, "pending"))
                elif existing[i]["spec"] != spec:
                    if existing[i]["state"] == "running":
                        raise ValueError("Recover a running task before changing its specification.")
                    self.store.update(i, spec=spec, state="pending", attempts=0, signature=None, outputs=None, error=None)
                    self.store.event(i, "spec_changed", {})
        self.refresh()

    def signature(self, task, rows):
        revision = {"task": task, "inputs": fingerprints(self.root, task["inputs"]),
                    "dependencies": {i: [rows[i]["signature"], rows[i]["outputs"]] for i in task["needs"]}}
        if task["kind"] == "agent":
            revision["dispatch_resources"] = context_fingerprints(task)
        return digest(revision)

    def output_stamps(self, task):
        return {name: {"sha256": fingerprints(self.root,[name])[name],
                       "mtime_ns": local_path(self.root,name).stat().st_mtime_ns}
                for name in task["outputs"] if local_path(self.root,name).is_file()}

    def refresh(self):
        with self.store.transaction():
            rows = self.store.rows()
            for i, task in self.tasks.items():
                r = rows[i]
                if r["state"] != "succeeded":
                    continue
                reason = None
                try:
                    if any(rows[d]["state"] != "succeeded" for d in task["needs"]):
                        reason = "Upstream task is unfinished or stale."
                    elif self.signature(task, rows) != r["signature"]:
                        reason = "Input or upstream revision changed."
                    elif fingerprints(self.root, task["outputs"]) != json.loads(r["outputs"]):
                        reason = "Completion artifacts changed."
                except ValueError as error:
                    reason = str(error)
                if reason:
                    self.store.update(i, state="pending", attempts=0, token=None, error=reason)
                    self.store.event(i, "invalidated", {"reason": reason})
                    rows[i]["state"] = "pending"
        return self.store.rows()

    def ready(self):
        rows = self.refresh()
        return [i for i, t in self.tasks.items() if rows[i]["state"] == "pending" and
                all(rows[d]["state"] == "succeeded" for d in t["needs"])]

    def claim(self, i, expected_signature=None):
        if i not in self.tasks:
            raise ValueError("Unknown task: " + i)
        self.refresh()
        # A single transaction prevents two host dispatchers claiming the same task.
        with self.store.transaction():
            rows = self.store.rows(); task = self.tasks[i]; r = rows[i]
            if r["state"] != "pending" or any(rows[d]["state"] != "succeeded" for d in task["needs"]):
                raise ValueError("Task is not ready: " + i)
            if r["attempts"] >= task["retry"]["max_attempts"]:
                raise ValueError("Attempt budget exhausted; explicit recovery with a reason is required.")
            signature = self.signature(task, rows)
            if expected_signature is not None and signature != expected_signature:
                raise ValueError("Inputs changed before retry; explicit recovery is required.")
            token = uuid.uuid4().hex
            self.store.update(i, state="running", attempts=r["attempts"]+1, token=token,
                              signature=signature, error=None, prior_outputs=json.dumps(self.output_stamps(task)))
            self.store.event(i, "started", {"token": token, "signature": signature,
                                            "inputs":fingerprints(self.root,task["inputs"]),
                                            "dispatch_resources":context_fingerprints(task) if task["kind"] == "agent" else None,
                                            "upstream":{d:rows[d]["signature"] for d in task["needs"]}})
            return token, signature

    def packet(self, i):
        if self.tasks[i]["kind"] != "agent":
            raise ValueError("Only agent tasks have dispatch packets.")
        # Validate context before reserving an attempt.
        make_packet(self.tasks[i], "0" * 64, "0" * 32, self.root)
        token, signature = self.claim(i)
        return make_packet(self.tasks[i], signature, token, self.root)

    def check_outputs(self, i, token):
        task = self.tasks[i]
        outputs = fingerprints(self.root, task["outputs"])
        prior = json.loads(self.store.rows()[i]["prior_outputs"] or "{}")
        stamps = self.output_stamps(task)
        if not task["checks"] and any(stamps.get(name) == prior.get(name) for name in task["outputs"]):
            raise ValueError("An unchanged existing artifact needs an explicit acceptance check; existence is not completion.")
        for j, argv in enumerate(task["checks"]):
            code = self.execute(argv, task["timeout_seconds"], f"{i}-{token}-check{j}")
            if code != 0:
                raise ValueError(f"Completion check {j} failed with exit {code}.")
        if fingerprints(self.root, task["outputs"]) != outputs:
            raise ValueError("Acceptance checks changed output artifacts; checks must be read-only.")
        return outputs

    def complete(self, i, token):
        rows = self.store.rows(); r = rows[i]; task = self.tasks[i]
        if r["state"] != "running" or r["token"] != token:
            raise ValueError("Stale or unmatched completion token.")
        try:
            self.refresh(); rows = self.store.rows()
            if any(rows[d]["state"] != "succeeded" for d in task["needs"]) or self.signature(task, rows) != r["signature"]:
                raise ValueError("Inputs changed during execution; completion is stale.")
            outputs = self.check_outputs(i, token)
            rows = self.refresh()
            if any(rows[d]["state"] != "succeeded" for d in task["needs"]) or self.signature(task, rows) != r["signature"]:
                raise ValueError("Inputs changed during acceptance checks; completion is stale.")
        except (ValueError, OSError, subprocess.TimeoutExpired) as error:
            self.fail(i, token, str(error), "needs_attention")
            raise
        with self.store.transaction():
            current = self.store.rows()[i]
            if current["state"] != "running" or current["token"] != token:
                raise ValueError("Completion was superseded during acceptance checks.")
            self.store.update(i, state="succeeded", outputs=json.dumps(outputs), error=None)
            self.store.event(i, "completed", {"token": token, "outputs": outputs})

    def fail(self, i, token, error, state="failed"):
        with self.store.transaction():
            r = self.store.rows()[i]
            if r["state"] != "running" or r["token"] != token:
                raise ValueError("Stale or unmatched failure token.")
            self.store.update(i, state=state, error=error)
            self.store.event(i, state, {"error": error, "token": token})

    def execute(self, argv, timeout, label):
        logs = self.state_dir / "logs"; logs.mkdir(exist_ok=True)
        with (logs / (label + ".log")).open("wb") as log:
            return subprocess.run(argv, cwd=self.root, stdout=log, stderr=subprocess.STDOUT,
                                  timeout=timeout, check=False).returncode

    def run_task(self, i):
        task = self.tasks[i]
        if task["kind"] != "command":
            raise ValueError("Native-agent tasks require a packet and explicit completion.")
        expected_signature = None
        while True:
            try:
                token, _ = self.claim(i, expected_signature)
            except ValueError as error:
                with self.store.transaction():
                    if self.store.rows()[i]["state"] == "pending":
                        self.store.update(i, state="needs_attention", error=str(error))
                        self.store.event(i, "needs_attention", {"error": str(error)})
                return
            retryable = False
            try:
                code = self.execute(task["command"], task["timeout_seconds"], f"{i}-{token}")
                if code == 0:
                    try:
                        self.complete(i, token)
                    except (ValueError,OSError,subprocess.TimeoutExpired):
                        return  # Failed acceptance is never a transient command failure.
                    return
                retryable = code in task["retry"]["exit_codes"]
                self.fail(i, token, f"Command exited with {code}.")
            except subprocess.TimeoutExpired:
                retryable = task["retry"]["timeout"]
                self.fail(i, token, "Command timed out.")
            except (OSError, ValueError) as error:
                self.fail(i, token, str(error), "needs_attention")
            except BaseException as error:
                self.fail(i, token, type(error).__name__, "needs_attention")
                raise
            r = self.store.rows()[i]
            if not retryable or r["attempts"] >= task["retry"]["max_attempts"]:
                return
            time.sleep(task["retry"]["delay_seconds"])
            with self.store.transaction():
                rows = self.store.rows()
                if rows[i]["state"] != "failed" or rows[i]["token"] != token:
                    return  # Recovery or another host has already taken responsibility.
                try:
                    if self.signature(task,rows)!=r["signature"]:
                        raise ValueError("Inputs changed after failure; automatic retry is stale.")
                except ValueError as error:
                    self.store.update(i,state="needs_attention",error=str(error))
                    self.store.event(i,"needs_attention",{"error":str(error)})
                    return
                expected_signature = r["signature"]
                self.store.update(i, state="pending")
                self.store.event(i, "retry_scheduled", {"next_attempt": r["attempts"]+1})

    def run(self):
        while True:
            commands = [i for i in self.ready() if self.tasks[i]["kind"] == "command"]
            if not commands:
                return self.status()
            for i in commands:
                self.run_task(i)

    def recover(self, i, reason):
        if not reason.strip():
            raise ValueError("Recovery requires a reason and resolution/outcome check.")
        with self.store.transaction():
            r = self.store.rows()[i]
            if r["state"] not in ("failed", "needs_attention", "running"):
                raise ValueError("Only failed, interrupted or attention tasks can be recovered.")
            self.store.update(i, state="pending", attempts=0, token=None, error=None)
            self.store.event(i, "recovered", {"reason": reason, "prior_state": r["state"]})
        self.refresh()

    def record_evidence(self, record):
        required = {"id", "claim", "status", "sources"}
        if not required <= record.keys() or record["status"] not in ("reported", "verified", "inferred", "conflicting", "open"):
            raise ValueError("Evidence needs id, claim, status and sources.")
        if record["status"] == "verified" and not record.get("verification"):
            raise ValueError("Verified evidence requires an explicit verification description.")
        if record["status"] != "open" and not record["sources"]:
            raise ValueError("Supported claims need source pointers.")
        record = dict(record)
        record["fingerprints"] = fingerprints(self.root, [s["path"] for s in record["sources"]])
        if any(not s.get("locator") for s in record["sources"]):
            raise ValueError("Each evidence source needs a page, line, field, or other locator.")
        record["recorded_at"] = now()
        if record.get("task"):
            rows = self.refresh()
            if record["task"] not in rows:
                raise ValueError("Evidence names an unknown producing task.")
            record["task_signature"] = rows[record["task"]]["signature"]
        with self.store.transaction():
            self.store.db.execute("INSERT OR REPLACE INTO evidence(id,record) VALUES (?,?)",
                                  (record["id"], json.dumps(record)))
            self.store.event(record.get("task"), "evidence_recorded", record)

    def status(self):
        rows = self.refresh()
        tasks = [{"id": i, "state": rows[i]["state"], "attempts": rows[i]["attempts"],
                  "waiting_for": [d for d in self.tasks[i]["needs"] if rows[d]["state"]!="succeeded"],
                  "error": rows[i]["error"]} for i in self.tasks]
        evidence = []
        for row in self.store.db.execute("SELECT record FROM evidence ORDER BY id"):
            r = json.loads(row[0]); stale = False
            try:
                stale = fingerprints(self.root, list(r["fingerprints"])) != r["fingerprints"]
            except ValueError:
                stale = True
            if r.get("task") and (r["task"] not in rows or rows[r["task"]]["state"] != "succeeded" or
                                  rows[r["task"]]["signature"] != r.get("task_signature")):
                stale = True
            r["freshness"] = "stale" if stale else "current"
            evidence.append(r)
        return {"goal": self.manifest["goal"], "execution": "succeeded" if all(r["state"] == "succeeded" for r in tasks) else "incomplete",
                "tasks": tasks, "evidence": evidence,
                "note": "Execution success and file freshness do not establish semantic claim validity."}

    def close(self):
        self.store.close()
