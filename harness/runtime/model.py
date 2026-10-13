"""Manifest validation and paths, using the standard library DAG implementation."""
import hashlib
import json
import re
from graphlib import TopologicalSorter
from pathlib import Path


STATES = {"pending", "running", "succeeded", "failed", "needs_attention"}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def local_path(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError("Artifact paths must be nonempty paths relative to the workspace.")
    path = (root / value).resolve()
    if path == root or root not in path.parents:
        raise ValueError("Artifact path escapes the workspace: " + value)
    return path


def fingerprints(root, names):
    result = {}
    for name in names:
        path = local_path(root, name)
        if not path.is_file():
            raise ValueError("Missing input or output: " + name)
        result[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def command_ok(value):
    return isinstance(value, list) and bool(value) and all(isinstance(s, str) and s and "\x00" not in s for s in value)


def load_manifest(path, root):
    path = Path(path)
    manifest = json.loads((path if path.is_absolute() else root / path).read_text())
    if manifest.get("version") != 1 or not manifest.get("goal") or not manifest.get("tasks"):
        raise ValueError("A version-1 manifest needs a goal and nonempty tasks.")
    tasks = manifest["tasks"]
    if not isinstance(tasks,list) or any(not isinstance(t,dict) or not isinstance(t.get("id"),str) for t in tasks):
        raise ValueError("Tasks must be a list of objects with string IDs.")
    ids = [t["id"] for t in tasks]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r"[a-zA-Z0-9_-]+", i) for i in ids):
        raise ValueError("Task IDs must be unique simple identifiers.")
    owners = []
    for task in tasks:
        task.setdefault("needs", [])
        task.setdefault("inputs", [])
        task.setdefault("outputs", [])
        task.setdefault("checks", [])
        task.setdefault("skills", [])
        task.setdefault("references", [])
        task.setdefault("effect", "local")
        task.setdefault("replay_safe", False)
        task.setdefault("timeout_seconds", 300)
        task.setdefault("retry", {})
        for field in ("needs","inputs","outputs","skills","references","checks"):
            if not isinstance(task[field],list):
                raise ValueError("Task field must be a list: "+field)
        if type(task["replay_safe"]) is not bool:
            raise ValueError("replay_safe must be a boolean.")
        if not isinstance(task["retry"],dict):
            raise ValueError("Retry policy must be an object.")
        retry = task["retry"]
        retry.setdefault("max_attempts", 1)
        retry.setdefault("exit_codes", [])
        retry.setdefault("delay_seconds", 0)
        retry.setdefault("timeout", False)
        if type(retry["timeout"]) is not bool:
            raise ValueError("Retry timeout must be a boolean.")
        if not set(task["needs"]) <= set(ids) or task["id"] in task["needs"]:
            raise ValueError("Unknown or self dependency: " + task["id"])
        if task.get("kind") not in ("command", "agent"):
            raise ValueError("Task kind must be command or agent.")
        if task["effect"] not in ("read", "local", "external"):
            raise ValueError("Unknown effect class.")
        if task["kind"] == "command" and (not command_ok(task.get("command")) or task["effect"] == "external"):
            raise ValueError("Commands require an argv list and read/local effects; external actions use host tools.")
        if task["kind"] == "agent" and not task.get("instruction"):
            raise ValueError("Agent tasks need a scoped instruction.")
        if not task["outputs"]:
            raise ValueError("Every task needs a declared completion artifact.")
        if any(not command_ok(c) for c in task["checks"]):
            raise ValueError("Checks must be argv lists.")
        if type(retry["max_attempts"]) is not int or not 1 <= retry["max_attempts"] <= 5:
            raise ValueError("Retry max_attempts must be an integer from 1 to 5.")
        if not isinstance(retry["exit_codes"],list) or any(type(c) is not int or c == 0 for c in retry["exit_codes"]):
            raise ValueError("Retry exit codes must be nonzero integers.")
        if not 0 <= retry["delay_seconds"] <= 30 or not 0 < task["timeout_seconds"] <= 86400:
            raise ValueError("Delay or timeout is outside the supported bounds.")
        if retry["max_attempts"] > 1 and (not task["replay_safe"] or task["effect"] == "external"):
            raise ValueError("Automatic retry requires explicitly replay-safe local/read work.")
        for name in task["inputs"] + task["outputs"] + task["references"]:
            local_path(root, name)
        for name in task["outputs"]:
            path = local_path(root, name)
            for prior in owners:
                if path == prior or path in prior.parents or prior in path.parents:
                    raise ValueError("Overlapping output ownership: " + name)
            owners.append(path)
        if set(task["inputs"]) & set(task["outputs"]):
            raise ValueError("Inputs and outputs must be distinct; use a new revision path.")
        if len(task["skills"]) > 3 or len(task.get("context", "")) > 12000 or len(task.get("instruction", "")) > 12000:
            raise ValueError("Split the task: at most three initial skills and 12,000 context characters.")
    order = list(TopologicalSorter({t["id"]: t["needs"] for t in tasks}).static_order())
    by_id = {t["id"]: t for t in tasks}
    output_owners = {local_path(root, name): t["id"] for t in tasks for name in t["outputs"]}
    ancestors = {}
    for i in order:
        ancestors[i] = set(by_id[i]["needs"])
        for dependency in by_id[i]["needs"]:
            ancestors[i].update(ancestors[dependency])
        for name in by_id[i]["inputs"]:
            owner = output_owners.get(local_path(root, name))
            if owner and owner not in ancestors[i]:
                raise ValueError("Input artifact requires a dependency on its producing task: " + name)
    return manifest, {i: by_id[i] for i in order}
