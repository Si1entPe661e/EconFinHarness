"""Targeted helper regression checks; these fixtures are never workflow outputs."""
import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

HERE = Path(__file__).resolve().parent


def module(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


v = module("validate")
p = module("project_run")
SOURCE = {"path": "harness/examples/native-project/validate.py", "locator": "sources()"}


class HelperChecks(unittest.TestCase):
    def base(self):
        return {"as_of": "helper-test-only", "scope": "structural fixture, not a real task", "sources": [SOURCE]}

    def test_source_scope_rejects_escape_and_corpus(self):
        for path in ("../AGENTS.md", "/etc/passwd", "Paper/example.pdf", "sample_repository/example.py", "harness/examples/war-discourse/run.R"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                v.sources({"sources": [{"path": path, "locator": "line 1"}]})
        v.sources({"sources": [SOURCE]})

    def test_source_needs_locator(self):
        with self.assertRaises(ValueError):
            v.sources({"sources": [{"path": SOURCE["path"]}]})

    def test_status_rejects_unsupported_completion_state(self):
        value = {**self.base(), "milestones": [{"deliverable": "Observed test", "state": "done", "sources": [SOURCE]}],
                 "risks": [], "next_actions": ["Inspect real data"]}
        with self.assertRaises(ValueError):
            v.status(value)
        value["milestones"][0]["state"] = "planned"
        v.status(value)

    def test_blocking_review_cannot_approve(self):
        value = {**self.base(), "verdict": "approved", "findings": [
            {"severity": "blocking", "finding": "Unsupported completion", "action": "Correct claim", "sources": [SOURCE]}]}
        with self.assertRaises(ValueError):
            v.review(value)
        value["verdict"] = "changes_required"
        v.review(value)

    def test_claim_review_needs_actual_judgment_fields(self):
        value = {**self.base(), "verdict": "approved", "findings": [], "judgments": []}
        with self.assertRaises(ValueError):
            v.review(value, claim=True)
        value["judgments"] = [{"claim": "A test claim", "support": "verified", "basis": "Named scoped inspection", "sources": [SOURCE]}] * 3
        v.review(value, claim=True)

    def test_report_counts_and_unmeasured_tokens_are_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            (output / "snapshot.json").write_text(json.dumps({"inventory": {"skills": {"count": 2}}}))
            (output / "validation.json").write_text(json.dumps({"checks": [{"id": "one", "exit_code": 0}]}))
            (output / "before-report.json").write_text(json.dumps({"native": {"requests": [{"state": "accepted", "current_attempt": True}]}, "workflow": {"execution": "incomplete"}}))
            value = {**self.base(), "audience": "Owner", "lead_finding": "Helper fixture", "recommendation": "Inspect actual evidence",
                     "facts": {"inventory_counts": {"skills": 2}, "check_exit_codes": {"one": 0},
                               "checkpoint_native_accepted": 1, "checkpoint_execution": "incomplete", "provider_token_count": None}}
            v.report_facts(value, output)
            value["facts"]["inventory_counts"]["skills"] = 3
            with self.assertRaises(ValueError):
                v.report_facts(value, output)
            value["facts"]["inventory_counts"]["skills"] = 2
            value["facts"]["provider_token_count"] = 123
            with self.assertRaises(ValueError):
                v.report_facts(value, output)

    def test_report_native_count_excludes_historical_accepted_attempts(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            (output / "snapshot.json").write_text(json.dumps({"inventory": {"skills": {"count": 2}}}))
            (output / "validation.json").write_text(json.dumps({"checks": [{"id": "one", "exit_code": 0}]}))
            requests = ([{"state": "accepted", "current_attempt": False}] * 3 +
                        [{"state": "accepted", "current_attempt": True}] * 3)
            (output / "before-report.json").write_text(json.dumps({"native": {"requests": requests}, "workflow": {"execution": "incomplete"}}))
            value = {**self.base(), "audience": "Owner", "lead_finding": "Helper fixture", "recommendation": "Inspect actual evidence",
                     "facts": {"inventory_counts": {"skills": 2}, "check_exit_codes": {"one": 0},
                               "checkpoint_native_accepted": 3, "checkpoint_execution": "incomplete", "provider_token_count": None}}
            v.report_facts(value, output)
            value["facts"]["checkpoint_native_accepted"] = 6
            with self.assertRaises(ValueError):
                v.report_facts(value, output)

    def test_missing_html_link_is_not_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.html"
            text = "<html><title>Helper test</title><h1>Fixture</h1><p>" + "readable helper fixture " * 20 + "</p>"
            path.write_text(text + '<a href="missing.json">Missing source</a></html>')
            with self.assertRaises(ValueError):
                v.html(path, metadata=False)

    def test_immutable_checkpoint_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "before-report.json"
            p.save(path, {"phase": "before_report"}, immutable=True)
            with self.assertRaises(FileExistsError):
                p.save(path, {"phase": "rewritten"}, immutable=True)

    def test_check_timeout_is_preserved_as_failure_with_actual_output(self):
        # Use a temporary directory under the checkout because recorded logs are workspace-relative.
        with tempfile.TemporaryDirectory(dir=HERE) as directory:
            with patch.object(p.subprocess, "run", side_effect=p.subprocess.TimeoutExpired(["check"], 300, output=b"partial output")):
                result = p.run_check("timeout", ["check"], Path(directory))
            self.assertIsNone(result["exit_code"])
            self.assertIn("timed out", result["error"])
            self.assertEqual(result["stdout"], "partial output")
            self.assertIn("partial output", (p.ROOT / result["log"]).read_text())


if __name__ == "__main__":
    unittest.main()
