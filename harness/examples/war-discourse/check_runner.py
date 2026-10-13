"""Regression checks for stale success markers after interrupted or failed runs."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run_all


class RunnerStatusChecks(unittest.TestCase):
    def test_failure_replaces_prior_success(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            status = out / "task_status.json"
            status.write_text('{"status":"succeeded"}')

            def fail():
                self.assertEqual(json.loads(status.read_text())["status"], "running")
                raise RuntimeError("deliberate diagnostic failure")

            with patch.object(run_all, "OUT", out), patch.object(run_all, "main", fail):
                with self.assertRaisesRegex(RuntimeError, "deliberate"):
                    run_all.run()
            self.assertEqual(json.loads(status.read_text())["status"], "failed")

    def test_success_is_written_only_after_all_steps(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)

            def finish():
                self.assertEqual(json.loads((out / "task_status.json").read_text())["status"], "running")

            with patch.object(run_all, "OUT", out), patch.object(run_all, "main", finish):
                run_all.run()
            self.assertEqual(json.loads((out / "task_status.json").read_text())["status"], "succeeded")

    def test_interruption_is_also_failed(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            with patch.object(run_all, "OUT", out), patch.object(run_all, "main", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    run_all.run()
            self.assertEqual(json.loads((out / "task_status.json").read_text())["status"], "failed")


if __name__ == "__main__":
    unittest.main()
