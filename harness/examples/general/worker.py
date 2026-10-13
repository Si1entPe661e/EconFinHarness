"""Small authored fixtures for coordination demonstrations, not domain software."""
import json
import sys
from pathlib import Path


def main(mode):
    if mode == "inventory":
        project = json.loads(Path("project.json").read_text())
        Path("inventory.json").write_text(json.dumps({"deliverables": project["deliverables"],
                                                      "blocked": sum(d["status"] == "blocked" for d in project["deliverables"])}))
    elif mode == "measure":
        count = Path("attempts.txt")
        n = int(count.read_text()) + 1 if count.exists() else 1
        count.write_text(str(n))
        if n == 1: raise SystemExit(75)  # Declared transient fault injection.
        values = json.loads(Path("metrics.json").read_text())
        total = values["closed"] + values["open"]
        Path("result.json").write_text(json.dumps({**values, "total": total, "closed_percent": 100*values["closed"]/total}))
    elif mode == "check-plan":
        facts = json.loads(Path("inventory.json").read_text())
        text = Path("plan.html").read_text()
        assert all(d["title"] in text for d in facts["deliverables"])
        assert "blocked" in text and "Acceptance" in text
    elif mode in ("check-report", "check-brief"):
        facts = json.loads(Path("result.json").read_text())
        text = Path("report.html" if mode == "check-report" else "brief.html").read_text()
        assert f'{facts["closed"]} of {facts["total"]}' in text
        assert f'{facts["closed_percent"]:.0f}%' in text
        assert facts["period"] in text and "forecast" in text
    elif mode == "check-edit":
        before = Path("draft.txt").read_text()
        after = Path("edited.html").read_text()
        if "not yet run" in before: assert "not yet run" in after
        else: assert "checks passed" in after
        assert "planned" in after
    else:
        raise ValueError("Unknown fixture mode.")


if __name__ == "__main__":
    main(sys.argv[1])
