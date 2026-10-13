"""Exercise the same runtime across project management, reporting and editing."""
import argparse
import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from harness.runtime.engine import Engine


def document(title, body):
    return '<!doctype html><html lang="en"><meta charset="utf-8"><title>' + html.escape(title) + \
        '</title><style>body{max-width:900px;margin:50px auto;padding:20px;font:17px/1.65 system-ui;color:#173641}table{border-collapse:collapse}td,th{padding:10px;border-bottom:1px solid #ccd8dc;text-align:left}a{color:#12647b}.note{background:#eef5f5;padding:18px}</style><h1>' + \
        html.escape(title) + '</h1>' + body + '</html>'


def setup(path, goal, tasks, inputs):
    path.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(Path(__file__).with_name("worker.py"), path / "worker.py")
    for name, value in inputs.items():
        (path / name).write_text(value if isinstance(value,str) else json.dumps(value,indent=2))
    (path / "task.json").write_text(json.dumps({"version":1,"goal":goal,"tasks":tasks},indent=2))
    return Engine(path,"task.json")


def accept(e, task, content):
    packet = e.packet(task)
    packet_dir = e.state_dir / "packets"; packet_dir.mkdir(exist_ok=True)
    (packet_dir / (task+"-"+packet["attempt_token"]+".json")).write_text(json.dumps(packet,indent=2))
    output = e.tasks[task]["outputs"][0]
    (e.root / output).write_text(content)
    e.complete(task,packet["attempt_token"])


def agent(task_id, capability, output, inputs, check, needs=()):
    return {"id":task_id,"kind":"agent","capability":capability,"instruction":"Produce the scoped demonstration artifact from the supplied facts; retain qualifications.",
            "needs":list(needs),"inputs":inputs+["worker.py"],"outputs":[output],
            "checks":[[sys.executable,"worker.py",check]]}


def run(out):
    plan = setup(out / "project-management","Plan a small operations project",[
        {"id":"inventory","kind":"command","command":[sys.executable,"worker.py","inventory"],
         "inputs":["project.json","worker.py"],"outputs":["inventory.json"],"replay_safe":True},
        agent("plan","project-plan","plan.html",["inventory.json"],"check-plan",["inventory"])
    ],{"project.json":{"deliverables":[
        {"title":"Service review","status":"planned","owner":"Operations lead","acceptance":"Current metrics and source notes included"},
        {"title":"Release checklist","status":"blocked","owner":"Delivery lead","acceptance":"Acceptance checks executed; access is currently missing"}]}})
    try:
        plan.run()
        facts=json.loads((plan.root / "inventory.json").read_text())
        body='<p>A demonstration plan, with no invented dates or commitments.</p><table><tr><th>Deliverable</th><th>Status</th><th>Owner</th><th>Acceptance</th></tr>'
        for d in facts["deliverables"]:
            body+='<tr>'+''.join('<td>'+html.escape(d[k])+'</td>' for k in ("title","status","owner","acceptance"))+'</tr>'
        if "plan" in plan.ready():
            accept(plan,"plan",document("Project delivery plan",body+'</table><p>Next action: resolve access for the blocked checklist. Planned work remains incomplete.</p>'))
        plan_status=plan.status()
    finally: plan.close()

    report=setup(out / "operations-report","Report current operations and prepare a briefing",[
        {"id":"measure","kind":"command","command":[sys.executable,"worker.py","measure"],
         "inputs":["metrics.json","worker.py"],"outputs":["result.json","attempts.txt"],"replay_safe":True,
         "retry":{"max_attempts":2,"exit_codes":[75]}},
        agent("report","report","report.html",["result.json"],"check-report",["measure"]),
        agent("brief","briefing","brief.html",["result.json","report.html"],"check-brief",["report"])
    ],{"metrics.json":{"closed":12,"open":3,"period":"Week 1"}})
    try:
        report.run();facts=json.loads((report.root / "result.json").read_text())
        message=f'{facts["period"]}: {facts["closed"]} of {facts["total"]} tickets closed ({facts["closed_percent"]:.0f}%).'
        if "report" in report.ready():
            accept(report,"report",document("Operations report",'<p>'+message+'</p><p>Scope: the supplied ticket snapshot. This is observed workload, not a forecast of service capacity.</p><p>Recommendation: inspect the three open tickets before committing to a delivery date. Severity and effort are unavailable.</p>'))
        if "brief" in report.ready():
            accept(report,"brief",document("Operations briefing",'<p>'+message+'</p><p>Three tickets remain open. Inspect severity and effort before agreeing a date; these counts do not establish a capacity forecast.</p>'))
        report.record_evidence({"id":"closure-rate","claim":message,"status":"verified","task":"measure",
                                "verification":"Recomputed 12/(12+3)=80%; scope is arithmetic on authored fixture data.",
                                "sources":[{"path":"result.json","locator":"closed, open, total, closed_percent and period"}]})
        report_status=report.status()
        # Attempt counts reset for a new revision, while the fixture fails only once
        # per workspace. Verify the original retry in the retained event history.
        history=[(row["action"],json.loads(row["detail"])) for row in report.store.db.execute(
            "SELECT action, detail FROM events WHERE task='measure' "
            "AND action IN ('failed','retry_scheduled','completed') ORDER BY seq")]
        assert (len(history)>=3 and history[0][0]=="failed" and
                history[0][1].get("error")=="Command exited with 75." and
                history[1][0]=="retry_scheduled" and history[1][1].get("next_attempt")==2 and
                history[2][0]=="completed"), "Observed transient failure, retry and completion are required."
    finally:report.close()

    editing=setup(out / "document-editing","Revise prose while preserving completion qualifications",[
        agent("edit","editing","edited.html",["draft.txt"],"check-edit")
    ],{"draft.txt":"Delivery is planned. Acceptance checks have not yet run."})
    try:
        if "edit" in editing.ready():
            accept(editing,"edit",document("Delivery update",'<p>Delivery is planned; acceptance checks have not yet run.</p>'))
        editing.record_evidence({"id":"draft-v1","claim":"Acceptance checks are not yet run.","status":"reported","task":"edit",
                                 "sources":[{"path":"draft.txt","locator":"sentence 2"}]})
        (editing.root / "draft.txt").write_text("Delivery is planned. Acceptance checks passed.")
        editing.refresh()
        assert editing.status()["evidence"][0]["freshness"]=="stale"
        accept(editing,"edit",document("Delivery update",'<p>Acceptance checks passed; delivery remains planned.</p>'))
        editing_status=editing.status()
    finally:editing.close()

    results={"execution_mode":"Authored fixtures and serial role execution; no live subagents or LLM evaluation",
             "project-management":plan_status,"operations-report":report_status,"document-editing":editing_status}
    assert all(results[k]["execution"]=="succeeded" for k in ("project-management","operations-report","document-editing"))
    (out / "summary.json").write_text(json.dumps(results,indent=2))
    body='<p class="note">The same task, evidence and recovery contracts support three non-paper workflows. These are small authored demonstrations with serial role execution; they do not benchmark an LLM or live multi-agent transport.</p><ul>'
    for path,title in [("project-management/plan.html","Project plan: dependencies, ownership and acceptance"),
                       ("operations-report/report.html","Operations report: classified transient retry and evidence"),
                       ("operations-report/brief.html","Briefing: concise audience-specific interpretation"),
                       ("document-editing/edited.html","Editing: source revision invalidates the old draft and evidence"),
                       ("summary.json","Machine-readable state and evidence summary")]:
        body+='<li><a href="'+path+'">'+title+'</a></li>'
    (out / "index.html").write_text(document("General Harness demonstrations",body+'</ul><p>Each project contains task.json, source fixtures, actual outputs and .harness checkpoints/logs/dispatch packets.</p>'))
    return results


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=ROOT/"outputs/general-harness-demo")
    args=parser.parse_args()
    run(args.output.resolve())
    print("Demonstrations passed:",args.output.resolve()/"index.html")
