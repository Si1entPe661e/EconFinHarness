"""Prepare and capture a real repository project workflow; native agents author deliverables."""
import argparse
import hashlib
import html
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from harness.runtime.engine import Engine
from harness.runtime.native import NativeDispatcher

HERE = "harness/examples/native-project"
AGENTS = ("project_status", "technical_review", "project_plan", "report", "brief", "claim_review")
GIT_PATHS = ["AGENTS.md", "README.md", "harness/runtime", "harness/checks", "harness/maintenance",
             "harness/agents", "harness/skills", "harness/orchestration", HERE, ".codex/config.toml"]


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return path.resolve().relative_to(ROOT).as_posix()


def save(path, value, immutable=False):
    data = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    if immutable:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(data)
    else:
        path.write_text(data, encoding="utf-8")


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def inventory():
    groups = {"skill_entrypoints": sorted((ROOT / "harness/skills").glob("*/SKILL.md")),
              "markdown_roles": sorted((ROOT / "harness/agents").glob("*.md")),
              "codex_roles": sorted((ROOT / "harness/agents/codex").glob("*.toml")),
              "runtime_modules": sorted((ROOT / "harness/runtime").glob("*.py")),
              "check_modules": sorted((ROOT / "harness/checks").glob("*.py"))}
    result = {}
    for name, paths in groups.items():
        result[name] = {"count": len(paths), "utf8_bytes": sum(p.stat().st_size for p in paths),
                        "files": [{"path": relative(p), "bytes": p.stat().st_size,
                                   "words": len(p.read_text(encoding="utf-8").split())} for p in paths]}
    routes = json.loads((ROOT / "harness/orchestration/routes.json").read_text())
    result["capability_routes"] = {"count": len(routes), "utf8_bytes": (ROOT / "harness/orchestration/routes.json").stat().st_size,
                                  "names": sorted(routes)}
    return result, groups


def captured_sources():
    _, groups = inventory()
    paths = {ROOT / "AGENTS.md", ROOT / "README.md", ROOT / ".codex/config.toml"}
    for values in groups.values():
        paths.update(values)
    for pattern in ("harness/maintenance/*.py", "harness/orchestration/*.md", "harness/orchestration/*.json",
                    "harness/checks/fixtures/*.json", "harness/skills/*/references/*.md", HERE + "/*.py", HERE + "/*.md"):
        paths.update(ROOT.glob(pattern))
    # These maintained guides are exercised by the paper-first check. No author code or data is opened.
    paths.update(ROOT / p for p in ("harness/workflows/replicate-paper.md", "harness/workflows/paper-first-replication.md"))
    return sorted(relative(p) for p in paths)


def output_path(value):
    path = (ROOT / value).resolve()
    if ROOT not in path.parents or any(part in {"Paper", "sample_repository", "war-discourse"} for part in path.relative_to(ROOT).parts):
        raise ValueError("Output must be inside the project and outside research/source boundaries.")
    return path


def prepare(output):
    if (output / ".harness/state.sqlite3").exists():
        raise ValueError("This output already has durable state; resume it or prepare a new output directory.")
    prefix = relative(output)
    path = lambda name: prefix + "/" + name
    requirements = {"as_of": now(), "scope": "Current FinEconHarness maintained project guides, runtime and checks",
                    "audience": "Project owner", "outcome": "Evidence-based current project status, delivery plan, report and decision brief",
                    "dispatch": "Actual native host collaboration tools with fresh scoped agents, durable receipts and independent review",
                    "context": "Route-selected initial skill and role; declared sources read on demand with measured character/byte limits",
                    "constraints": ["No network, external messages or external systems", "No author code, corpus, datasets or paper collection",
                                    "Do not invent budget, deadline or staffing commitments", "Native agents author their own disjoint deliverables",
                                    "Distinguish checked completion from substantive claim support"]}
    save(output / "requirements.json", requirements)
    command = lambda stage: ["python3", "-B", HERE + "/project_run.py", stage, "--output", prefix]
    check = lambda stage: [["python3", "-B", HERE + "/validate.py", "--stage", stage, "--output", prefix]]
    helper = [HERE + "/validate.py"]
    common = ("You are not alone in this workspace. Own only your declared outputs, preserve all other edits, and do not spawn agents. "
              "Use only the scoped maintained sources. No corpus, author code, network or external messages. "
              "Read sources through the supplied native read command so observed context metrics remain attributable. "
              "Helper-mediated reads are actual audited accesses; their audit does not prove no direct reads occurred. "
              "Do not claim provider token counts or filesystem isolation. Write sources as workspace-relative path plus precise field/line locator. "
              "Every JSON object and HTML artifact-data needs as_of, scope and sources. HTML must be readable standalone with a title, headings, "
              "local source links and a script type=application/json id=artifact-data containing its structured claims. "
              "Acceptance checks validate structure/numbers, not writing quality. Run the declared check and repair your own artifacts if needed. ")
    tasks = [{"id": "capture", "kind": "command", "command": command("capture"), "inputs": captured_sources() + [path("requirements.json")],
              "outputs": [path("snapshot.json"), path("validation.json")], "checks": check("capture"), "replay_safe": True}]

    def agent(task_id, capability, needs, inputs, outputs, instruction, references=()):
        tasks.append({"id": task_id, "kind": "agent", "capability": capability, "needs": needs,
                      "inputs": [path(p) for p in inputs] + helper, "outputs": [path(p) for p in outputs],
                      "checks": check(task_id), "instruction": common + instruction,
                      "context": "Real current repository project work. Read the schema and acceptance contract in " + HERE + "/README.md on demand. "
                                 "Sources are bounded by this contract; missing evidence stays open.",
                      "references": [HERE + "/README.md", *references]})

    agent("project_status", "project-status", ["capture"], ["requirements.json", "snapshot.json", "validation.json"], ["status.json", "status.html"],
          "Inspect actual capture evidence. Produce current milestones with deliverable/state/sources, risks, and next_actions with responsible roles. "
          "Use only supported milestone states from validate.py. Distinguish current implementation checks from still pending live workflow/report delivery. "
          "status.html artifact-data must equal status.json exactly; include readable status narrative.",
          ["README.md", "harness/orchestration/README.md", "harness/orchestration/runtime.md"])
    agent("technical_review", "evidence-review", ["capture"], ["requirements.json", "snapshot.json", "validation.json"], ["technical-review.json"],
          "Independently inspect what current checks actually establish and any implementation/context-control limitations. Produce verdict approved or changes_required, "
          "findings list (severity blocking/nonblocking, finding, action, sources), and exact source locators. Empty findings are allowed only with an explained review scope. "
          "Do not change implementation; give actionable delivery risks. Review code selectively rather than reloading whole modules.",
          ["harness/runtime/native.py", "harness/runtime/dispatch.py", "harness/runtime/engine.py", "harness/checks/README.md"])
    agent("project_plan", "project-plan", ["project_status", "technical_review"], ["requirements.json", "status.json", "technical-review.json"], ["delivery-plan.json"],
          "Build prioritized deliverables (deliverable, positive integer priority, dependencies list, owner role, observable acceptance, sources), risks and next actions. "
          "Resolve status/review implications; preserve unresolved decisions. No invented dates, budgets, effort or staffed capacity. "
          "Plan delivery against the existing task graph and evidence, distinguishing this run's remaining outputs from future maintenance.")
    tasks.append({"id": "checkpoint", "kind": "command", "needs": ["project_plan"], "command": command("checkpoint"),
                  "inputs": [path(p) for p in ("status.json", "technical-review.json", "delivery-plan.json")] + helper + [HERE + "/project_run.py"],
                  "outputs": [path("before-report.json")], "checks": check("checkpoint"), "replay_safe": False})
    agent("report", "report", ["checkpoint"], ["requirements.json", "snapshot.json", "validation.json", "status.json", "technical-review.json", "delivery-plan.json", "before-report.json"], ["report.html"],
          "Write a project-owner report: lead finding/recommendation, delivered vs in-progress work, measured inventory/check outcomes, review implications, "
          "native/context evidence limits and next priorities. Cite source fields close to claims. The report phase checkpoint precedes report/brief/claim review; "
          "do not call it final workflow completion. Metadata requires audience, lead_finding, recommendation and facts with inventory_counts matching snapshot inventory "
          "counts, check_exit_codes matching validation, checkpoint_native_accepted counting only requests with state accepted and current_attempt true, "
          "checkpoint_execution and provider_token_count:null. Historical accepted attempts remain in the audit and are excluded from this current count. "
          "Preserve observations, interpretations and recommendations distinctly; do not edit this report after native acceptance.")
    agent("brief", "briefing", ["report"], ["requirements.json", "report.html", "delivery-plan.json"], ["brief.html"],
          "Write a concise project-owner decision brief grounded in the accepted report and plan. Include decisions, viable tradeoffs, and concrete actions with roles. "
          "Metadata requires decision, tradeoffs and actions plus as_of/scope/sources. Distinguish authorized actions from decisions needed; do not invent deadlines.")
    agent("claim_review", "evidence-review", ["report"], ["report.html", "snapshot.json", "validation.json", "before-report.json", "technical-review.json", "delivery-plan.json"], ["claim-review.json"],
          "Independently compare material report claims to actual source fields and observed native phase evidence. Produce explicit verdict approved or changes_required, "
          "findings with severity/finding/action/sources and judgments list of at least three material claims, each claim/support/basis/sources. Support is verified, "
          "reported, inferred, conflicting or open. Check numbers, completed vs pending, phase timing, context measurement limits and recommendations. "
          "Unsupported material assertions require blocking findings; good prose/file existence does not establish support. Do not edit the report.",
          ["harness/runtime/native.py", "harness/runtime/engine.py"])
    tasks.append({"id": "publish", "kind": "command", "needs": ["brief", "claim_review"], "command": command("publish"),
                  "inputs": [path(p) for p in ("requirements.json", "snapshot.json", "validation.json", "status.json", "status.html", "technical-review.json", "delivery-plan.json", "before-report.json", "report.html", "brief.html", "claim-review.json")]
                            + helper + [HERE + "/project_run.py"],
                  "outputs": [path("run-summary.json"), path("index.html")], "checks": check("publish"), "replay_safe": True})
    manifest = {"version": 1, "goal": requirements["outcome"], "root": str(ROOT), "state_dir": path(".harness"), "tasks": tasks}
    save(output / "task.json", manifest)
    print(json.dumps({"manifest": path("task.json"), "root": str(ROOT), "state_dir": path(".harness"), "tasks": [t["id"] for t in tasks]}))


def capture(output):
    logs = output / "checks"
    logs.mkdir(parents=True, exist_ok=True)
    commands = [("unit_tests", ["python3", "-B", "-m", "unittest", "discover", "-s", "harness/checks", "-p", "test_*.py"]),
                ("paper_first", ["python3", "-B", "harness/checks/check_paper_first.py"]),
                ("role_sync", ["python3", "-B", "harness/maintenance/sync_roles.py", "--config"]),
                ("diff_check", ["git", "diff", "--check", "--", *GIT_PATHS]),
                ("example_checks", ["python3", "-B", HERE + "/check_helpers.py"])]
    outcomes = []
    for name, argv in commands:
        outcomes.append(run_check(name, argv, logs))
    groups, _ = inventory()
    snapshot = {"as_of": now(), "scope": "Maintained project sources only; no corpus or author materials inspected",
                "git": {"head": git("rev-parse", "HEAD"), "status": git("status", "--short", "--untracked-files=all", "--", *GIT_PATHS),
                        "status_paths": GIT_PATHS}, "python": sys.version, "inventory": groups,
                "source_hashes": {p: sha(ROOT / p) for p in captured_sources()},
                "capture_limits": ["Static inventory and executed implementation checks do not establish native-host execution or report claim support.",
                                   "Inventory is enumerated during prepare/capture; rerun prepare in a new output directory after adding source entrypoints."]}
    save(output / "snapshot.json", snapshot)
    save(output / "validation.json", {"as_of": now(), "scope": snapshot["scope"], "checks": outcomes,
                                      "all_passed": all(item["exit_code"] == 0 for item in outcomes)})
    if not all(item["exit_code"] == 0 for item in outcomes):
        raise ValueError("Actual capture checks failed; inspect validation.json and its logs.")


def run_check(name, argv, logs):
    start = now()
    error = None
    try:
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False, timeout=300)
        code, stdout, stderr = result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as failure:
        code, error = None, "Command timed out after 300 seconds."
        stdout, stderr = failure.stdout or "", failure.stderr or ""
        stdout = stdout.decode("utf-8", errors="replace") if isinstance(stdout, bytes) else stdout
        stderr = stderr.decode("utf-8", errors="replace") if isinstance(stderr, bytes) else stderr
    except OSError as failure:
        code, stdout, stderr, error = None, "", "", str(failure)
    log = logs / (name + ".log")
    log.write_text(stdout + stderr + (("\n" + error) if error else ""), encoding="utf-8")
    return {"id": name, "argv": argv, "exit_code": code, "started_at": start, "finished_at": now(),
            "stdout": stdout, "stderr": stderr, "error": error, "log": relative(log), "log_sha256": sha(log)}


def native_snapshot(output):
    manifest = json.loads((output / "task.json").read_text())
    engine = Engine(ROOT, relative(output / "task.json"), manifest["state_dir"])
    try:
        dispatcher = NativeDispatcher(engine, max_workers=2, available_agent_types=("default",),
                                      max_initial_chars=16000, max_read_chars=40000, max_chunk_chars=8000)
        return {"workflow": engine.status(), "native": dispatcher.status()}
    finally:
        engine.close()


def checkpoint(output):
    value = {"as_of": now(), "phase": "before_report", **native_snapshot(output)}
    value["note"] = "Immutable observed phase checkpoint: the report and downstream deliveries are still pending. No native task state is settled here."
    save(output / "before-report.json", value, immutable=True)


def publish(output):
    import importlib.util
    spec = importlib.util.spec_from_file_location("native_project_validate", ROOT / HERE / "validate.py")
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    validator.validate("claim_review", output)
    review = json.loads((output / "claim-review.json").read_text())
    if review["verdict"] != "approved" or any(item["severity"] == "blocking" for item in review["findings"]):
        raise ValueError("Independent claim review blocks publication.")
    observed = native_snapshot(output)
    accepted = [r for r in observed["native"]["requests"] if r["state"] == "accepted" and r["current_attempt"]]
    if ({r["task"] for r in accepted} != set(AGENTS) or len(accepted) != len(AGENTS) or
            any(not r["native_id"] or not r["context"]["loaded"] for r in accepted) or observed["native"]["unresolved_dispatches"]):
        raise ValueError("Publication requires six current accepted, bound native agents with loaded context and no unresolved dispatches.")
    artifacts = ["requirements.json", "snapshot.json", "validation.json", "status.json", "status.html", "technical-review.json",
                 "delivery-plan.json", "before-report.json", "report.html", "brief.html", "claim-review.json"]
    summary = {"as_of": now(), "phase": "publish_acceptance", "native_accepted_tasks": sorted(r["task"] for r in accepted),
               **observed, "provider_token_count": None,
               "artifact_hashes": {relative(output / name): sha(output / name) for name in artifacts},
               "input_hashes": json.loads((output / "snapshot.json").read_text())["source_hashes"],
               "context_limits": "Measured initial characters/UTF-8 bytes and audited helper-read characters; this audit does not prove absence of direct reads. No provider token count or filesystem sandbox measurement.",
               "completion_scope": "All six native deliveries and independent claim review accepted. This cover is generated during publish acceptance; the runtime records publish success only after its checks pass."}
    save(output / "run-summary.json", summary)
    rows = "".join("<tr><td>" + "</td><td>".join(html.escape(str(v)) for v in
                    (r["task"], r["role"], r["host_agent_type"], r["native_id"], r["context"]["initial_chars"], r["context"]["read_chars"])) + "</td></tr>" for r in accepted)
    links = "".join('<li><a href="' + name + '">' + name + "</a></li>" for name in artifacts + ["run-summary.json"])
    content = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Native project delivery</title><style>body{max-width:1100px;margin:3rem auto;font:17px/1.6 system-ui;padding:0 1rem;color:#172638}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border:1px solid #ccd5dd;padding:.5rem;text-align:left}</style><body><h1>Native project delivery</h1>'
    content += '<p>Six project status, review, planning, report and briefing deliveries were accepted from actual bound native agents. The independent claim review approved the report without blocking findings. The report retains its immutable before-report phase evidence; this cover adds the observed final delivery evidence.</p>'
    content += '<p>Publish acceptance is recorded here before the runtime settles the publish command. Read runtime status after the command for final workflow completion. Character and byte counts describe the supplied context and audited helper reads; the audit does not prove no direct reads occurred. Provider tokens, additional host context and filesystem isolation were not measured.</p>'
    content += '<h2>Observed native delivery</h2><table><thead><tr><th>Task</th><th>Semantic role</th><th>Host type</th><th>Observed native ID</th><th>Initial characters</th><th>Source-read characters</th></tr></thead><tbody>' + rows + '</tbody></table><h2>Artifacts and evidence</h2><ul>' + links + '</ul></body></html>'
    (output / "index.html").write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("prepare", "capture", "checkpoint", "publish"))
    parser.add_argument("--output", default="outputs/native-project-run")
    args = parser.parse_args()
    globals()[args.stage](output_path(args.output))


if __name__ == "__main__":
    main()
