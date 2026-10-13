"""Regression checks for resuming the general demo across task revisions."""
import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "harness/examples/general/run_demo.py"


class GeneralDemoChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def run_demo(self, executable=None):
        result = subprocess.run(
            [executable or sys.executable, "-B", str(SCRIPT), "--output", str(self.root)],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        summary = json.loads((self.root / "summary.json").read_text())
        for name in ("project-management", "operations-report", "document-editing"):
            self.assertEqual(summary[name]["execution"], "succeeded")
        self.assertTrue((self.root / "index.html").is_file())
        return summary

    def measure_history(self):
        path = self.root / "operations-report/.harness/state.sqlite3"
        with closing(sqlite3.connect(path)) as db:
            return db.execute(
                "SELECT seq, action, detail FROM events WHERE task='measure' ORDER BY seq"
            ).fetchall()

    def check_resumed_measure(self, summary, prior_history):
        measure = next(t for t in summary["operations-report"]["tasks"] if t["id"] == "measure")
        self.assertEqual(measure["attempts"], 1)
        self.assertEqual((self.root / "operations-report/attempts.txt").read_text(), "3")
        history = self.measure_history()
        self.assertEqual(history[:len(prior_history)], prior_history)
        new_events = history[len(prior_history):]
        self.assertEqual(sum(action == "started" for _, action, _ in new_events), 1)
        self.assertEqual(sum(action == "completed" for _, action, _ in new_events), 1)
        self.assertFalse(any(action == "failed" for _, action, _ in new_events))
        self.assertTrue((self.root / "operations-report/report.html").is_file())
        self.assertTrue((self.root / "operations-report/brief.html").is_file())

    def test_demo_resumes_after_python_executable_changes(self):
        self.run_demo()
        prior_history = self.measure_history()
        alias = self.root / "python-alias"
        alias.symlink_to(sys.executable)
        summary = self.run_demo(str(alias))
        manifest = json.loads((self.root / "operations-report/task.json").read_text())
        self.assertEqual(manifest["tasks"][0]["command"][0], str(alias))
        self.check_resumed_measure(summary, prior_history)
        # Another unchanged run must reuse the accepted result.
        history = self.measure_history()
        self.check_resumed_measure(self.run_demo(str(alias)), prior_history)
        self.assertEqual(sum(action == "started" for _, action, _ in self.measure_history()),
                         sum(action == "started" for _, action, _ in history))

    def test_demo_rebuilds_missing_output_and_retains_attempt_history(self):
        self.run_demo()
        prior_history = self.measure_history()
        (self.root / "operations-report/result.json").unlink()
        self.check_resumed_measure(self.run_demo(), prior_history)

    def test_demo_requires_observed_transient_failure_and_retry(self):
        # A preexisting counter alone must not stand in for observed retry events.
        report = self.root / "operations-report"
        report.mkdir()
        (report / "attempts.txt").write_text("2")
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--output", str(self.root)],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Observed transient failure, retry and completion are required.", result.stderr)
        self.assertFalse((self.root / "summary.json").exists())


if __name__ == "__main__":
    unittest.main()
