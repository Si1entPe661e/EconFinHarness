"""CLI integration checks; native handles here are explicit test doubles, not live runs."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from harness.runtime.engine import Engine
from harness.runtime.native import NativeDispatcher


ROOT = Path(__file__).resolve().parents[2]


class NativeCliChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manifest = self.root / "task.json"
        self.manifest.write_text(json.dumps({"version": 1, "goal": "CLI integration", "tasks": [
            {"id": "report", "kind": "agent", "capability": "report", "instruction": "Write a scoped report.",
             "inputs": ["source.txt"], "outputs": ["report.txt"]}]}))
        (self.root / "source.txt").write_text("Actual test source\nSecond line\n")

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args):
        return subprocess.run([sys.executable, "-B", "-m", "harness.runtime", "--root", str(self.root),
                               "--manifest", "task.json", "native", *args],
                              cwd=ROOT, capture_output=True, text=True)

    def test_native_cli_load_read_bind_and_settle(self):
        result = self.cli("next", "--authorized")
        self.assertEqual(result.returncode, 0, result.stderr)
        request = json.loads(result.stdout)["dispatches"][0]
        token = request["token"]
        self.assertEqual(request["tool_args"]["fork_turns"], "none")
        self.assertNotIn("prompt", request)
        self.assertEqual(self.cli("begin", "--token", token).returncode, 0)
        native_id = "/root/" + request["tool_args"]["task_name"]
        self.assertEqual(self.cli("bind", "--token", token, "--native-id", native_id).returncode, 0)
        context = self.cli("context", "--token", token)
        self.assertEqual(context.returncode, 0, context.stderr)
        self.assertIn("Semantic role: report-writer", context.stdout)
        self.assertFalse(context.stdout.startswith('{"prompt"'))
        read = self.cli("read", "--token", token, "--path", "source.txt", "--start", "1", "--end", "1")
        self.assertEqual(read.returncode, 0, read.stderr)
        self.assertEqual(read.stdout, "1: Actual test source\n")
        with_engine = Engine(self.root, self.manifest)
        try:
            signature = with_engine.store.rows()["report"]["signature"]
        finally:
            with_engine.close()
        (self.root / "report.txt").write_text("Delivered test report")
        (self.root / "return.json").write_text(json.dumps({
            "task": "report", "attempt_token": token, "input_signature": signature,
            "status": "completed", "artifacts": ["report.txt"], "summary": "Produced the test report.",
            "unresolved": []}))
        settled = self.cli("settle", "--token", token, "--native-id", native_id,
                           "--terminal-state", "completed", "--result-file", "return.json")
        self.assertEqual(settled.returncode, 0, settled.stderr)
        self.assertEqual(json.loads(settled.stdout)["state"], "accepted")

    def test_unauthorized_next_does_not_execute_ready_commands(self):
        self.manifest.write_text(json.dumps({"version": 1, "goal": "No unauthorized execution", "tasks": [
            {"id": "capture", "kind": "command", "command": [sys.executable, "-c",
             "from pathlib import Path;Path('capture.txt').write_text('ran')"], "outputs": ["capture.txt"]}]}))
        result = self.cli("next")
        self.assertEqual(result.returncode, 1)
        self.assertIn("authorization", result.stderr)
        self.assertFalse((self.root / "capture.txt").exists())

    def test_resolve_cli_records_known_not_started_outcome(self):
        request = json.loads(self.cli("next", "--authorized").stdout)["dispatches"][0]
        token = request["token"]
        self.assertEqual(self.cli("begin", "--token", token).returncode, 0)
        result = self.cli("resolve", "--token", token, "--outcome", "not_started",
                          "--reason", "Test host confirms the simulated call was never made.")
        self.assertEqual(result.returncode, 0, result.stderr)
        status = json.loads(self.cli("status").stdout)
        self.assertEqual(status["running"], 0)


if __name__ == "__main__":
    unittest.main()
