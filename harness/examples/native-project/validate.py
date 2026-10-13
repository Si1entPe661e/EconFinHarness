"""Read-only structural and numerical acceptance checks for real native work."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATES = {"completed_and_checked", "produced_unchecked", "in_progress", "blocked", "stale", "planned"}
SUPPORT = {"verified", "reported", "inferred", "conflicting", "open"}
AGENT_TASKS = {"project_status", "technical_review", "project_plan", "report", "brief", "claim_review"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), str(path) + " must contain a JSON object.")
    return value


def text_field(value, name):
    require(isinstance(value.get(name), str) and bool(value[name].strip()), "Missing text field: " + name)


def sources(value, root=ROOT):
    items = value.get("sources")
    require(isinstance(items, list) and bool(items), "At least one source is required.")
    for source in items:
        require(isinstance(source, dict), "Source must be an object.")
        text_field(source, "path")
        text_field(source, "locator")
        path = Path(source["path"])
        require(not path.is_absolute() and ".." not in path.parts, "Source must be workspace-relative.")
        resolved = (root / path).resolve()
        require(root.resolve() in resolved.parents and resolved.is_file(), "Missing source: " + str(path))
        require(not any(part in {"Paper", "sample_repository", "war-discourse"} for part in path.parts),
                "Source is outside this workflow's maintained-project scope.")


def base(value):
    for name in ("as_of", "scope"):
        text_field(value, name)
    sources(value)


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.visible = []
        self.script = False
        self.data = []
        self.capture = False
        self.links = []
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script":
            self.script = True
            self.capture = attrs.get("id") == "artifact-data" and attrs.get("type") == "application/json"
        if tag in {"h1", "h2"}:
            self.headings += 1
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "script":
            self.script = self.capture = False

    def handle_data(self, data):
        if self.capture:
            self.data.append(data)
        elif not self.script:
            self.visible.append(data)


def html(path, metadata=True):
    raw = path.read_text(encoding="utf-8")
    parsed = Document()
    parsed.feed(raw)
    require("<html" in raw.lower() and "<title" in raw.lower() and parsed.headings > 0,
            "HTML needs a document, title and readable heading.")
    require(len(" ".join(parsed.visible).split()) >= 40, "HTML has too little readable content.")
    for href in parsed.links:
        if not re.match(r"^[a-zA-Z]+:", href) and not href.startswith("#"):
            target = href.split("#", 1)[0].split("?", 1)[0]
            require((path.parent / target).resolve().is_file(), "Missing HTML link target: " + href)
    if metadata:
        value = json.loads("".join(parsed.data))
        require(isinstance(value, dict), "HTML artifact-data must be a JSON object.")
        base(value)
        return value
    return parsed


def findings(value):
    require(isinstance(value.get("findings"), list), "Findings must be a list, including when empty.")
    for finding in value["findings"]:
        require(finding.get("severity") in {"blocking", "nonblocking"}, "Unknown finding severity.")
        for name in ("finding", "action"):
            text_field(finding, name)
        sources(finding)


def status(value):
    base(value)
    require(isinstance(value.get("milestones"), list) and value["milestones"], "Milestones are required.")
    for item in value["milestones"]:
        text_field(item, "deliverable")
        require(item.get("state") in STATES, "Unknown milestone state.")
        sources(item)
    for field in ("risks", "next_actions"):
        require(isinstance(value.get(field), list), field + " must be a list.")
    require(value["next_actions"], "Current next actions are required.")


def review(value, claim=False):
    base(value)
    require(value.get("verdict") in {"approved", "changes_required"}, "Review needs an explicit verdict.")
    findings(value)
    blocked = any(f["severity"] == "blocking" for f in value["findings"])
    require(not blocked or value["verdict"] == "changes_required", "Blocking finding contradicts approval.")
    if claim:
        judgments = value.get("judgments")
        require(isinstance(judgments, list) and len(judgments) >= 3, "Review at least three material claims.")
        for judgment in judgments:
            text_field(judgment, "claim")
            text_field(judgment, "basis")
            require(judgment.get("support") in SUPPORT, "Unknown support judgment.")
            sources(judgment)


def plan(value):
    base(value)
    items = value.get("deliverables")
    require(isinstance(items, list) and bool(items), "Prioritized deliverables are required.")
    for item in items:
        for field in ("deliverable", "owner", "acceptance"):
            text_field(item, field)
        require(type(item.get("priority")) is int and item["priority"] >= 1, "Priority must be a positive integer.")
        require(isinstance(item.get("dependencies"), list), "Dependencies must be a list.")
        sources(item)
    require(isinstance(value.get("risks"), list), "Plan risks must be a list.")


def report_facts(value, output):
    base(value)
    for field in ("audience", "lead_finding", "recommendation"):
        text_field(value, field)
    facts = value.get("facts")
    require(isinstance(facts, dict), "Report facts are required.")
    snapshot = read_json(output / "snapshot.json")
    validation = read_json(output / "validation.json")
    checkpoint = read_json(output / "before-report.json")
    expected = {key: item["count"] for key, item in snapshot["inventory"].items()}
    require(facts.get("inventory_counts") == expected, "Report inventory counts differ from snapshot.")
    results = {item["id"]: item["exit_code"] for item in validation["checks"]}
    require(facts.get("check_exit_codes") == results, "Report check outcomes differ from executed validation.")
    require(facts.get("checkpoint_native_accepted") == sum(r["state"] == "accepted" and r["current_attempt"]
                                                          for r in checkpoint["native"]["requests"]),
            "Report current accepted native count differs from its phase checkpoint.")
    require(facts.get("checkpoint_execution") == checkpoint["workflow"]["execution"], "Report checkpoint execution differs.")
    require(facts.get("provider_token_count") is None, "Provider token count was not measured.")


def validate(stage, output):
    if stage == "capture":
        snapshot = read_json(output / "snapshot.json")
        value = read_json(output / "validation.json")
        require(snapshot.get("git", {}).get("head"), "Capture needs an actual git revision.")
        require(snapshot.get("source_hashes"), "Capture needs source revisions.")
        required = {"unit_tests", "paper_first", "role_sync", "diff_check", "example_checks"}
        require({c["id"] for c in value.get("checks", [])} == required, "Missing required executed check.")
        for item in value["checks"]:
            require(item.get("exit_code") == 0, "An executed check failed: " + item["id"])
            require(item.get("argv") and item.get("started_at") and item.get("finished_at"), "Missing execution provenance.")
            require((ROOT / item["log"]).is_file(), "Missing actual check log.")
    elif stage == "project_status":
        value = read_json(output / "status.json")
        status(value)
        require(html(output / "status.html") == value, "Status HTML metadata and JSON disagree.")
    elif stage == "technical_review":
        review(read_json(output / "technical-review.json"))
    elif stage == "project_plan":
        plan(read_json(output / "delivery-plan.json"))
    elif stage == "checkpoint":
        value = read_json(output / "before-report.json")
        require(value.get("phase") == "before_report", "Wrong checkpoint phase.")
        accepted = {r["task"] for r in value["native"]["requests"] if r["state"] == "accepted" and r["current_attempt"]}
        require({"project_status", "technical_review", "project_plan"} <= accepted, "Prereport native tasks are not accepted.")
        require(value["workflow"]["execution"] == "incomplete", "Prereport snapshot cannot claim workflow completion.")
    elif stage == "report":
        report_facts(html(output / "report.html"), output)
    elif stage == "brief":
        value = html(output / "brief.html")
        for name in ("decision", "tradeoffs", "actions"):
            require(value.get(name), "Brief needs " + name)
    elif stage == "claim_review":
        review(read_json(output / "claim-review.json"), claim=True)
    elif stage == "publish":
        value = read_json(output / "run-summary.json")
        require(value.get("phase") == "publish_acceptance", "Wrong final summary phase.")
        require(value.get("native_accepted_tasks") == sorted(AGENT_TASKS), "Final summary requires six accepted native tasks.")
        require(value.get("provider_token_count") is None, "Provider tokens were not measured.")
        review_value = read_json(output / "claim-review.json")
        review(review_value, claim=True)
        require(review_value["verdict"] == "approved" and not any(f["severity"] == "blocking" for f in review_value["findings"]),
                "Independent claim review blocks publication.")
        html(output / "index.html", metadata=False)
    else:
        raise ValueError("Unknown acceptance stage: " + stage)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    validate(args.stage, (ROOT / args.output).resolve())
    print(json.dumps({"stage": args.stage, "structural_and_numeric_acceptance": "passed",
                      "semantic_limit": "Independent native review assesses support; these checks do not score writing quality."}))


if __name__ == "__main__":
    main()
