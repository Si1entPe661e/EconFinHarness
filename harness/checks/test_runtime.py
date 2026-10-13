"""Behavior checks for general coordination; no LLM credentials or third-party data."""
import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from harness.runtime.dispatch import make_packet
from harness.runtime.engine import Engine
from harness.runtime.model import digest, fingerprints


def write_command(path, text="done"):
    return [sys.executable, "-c", f"from pathlib import Path;Path({path!r}).write_text({text!r})"]


def task(name="build", **kw):
    value = {"id": name, "kind": "command", "command": write_command(name + ".txt"),
             "outputs": [name + ".txt"], "replay_safe": True}
    value.update(kw)
    return value


class RuntimeChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manifest = self.root / "task.json"
        self.engines = []

    def tearDown(self):
        for e in self.engines: e.close()
        self.temp.cleanup()

    def engine(self, tasks, state_dir=".harness"):
        self.manifest.write_text(json.dumps({"version": 1, "goal": "General coordination test", "tasks": tasks}))
        e = Engine(self.root, self.manifest, state_dir)
        self.engines.append(e)
        return e

    def state(self, e, name="build"):
        return e.store.rows()[name]

    def test_dependency_order_and_resume_skip_completed_work(self):
        e = self.engine([task("second", needs=["first"]), task("first")])
        self.assertEqual(e.ready(), ["first"])
        self.assertEqual(e.run()["execution"], "succeeded")
        count = e.store.db.execute("SELECT COUNT(*) FROM events WHERE action='started'").fetchone()[0]
        e.run()
        self.assertEqual(count, e.store.db.execute("SELECT COUNT(*) FROM events WHERE action='started'").fetchone()[0])

    def test_input_change_invalidates_only_descendants(self):
        (self.root / "source.txt").write_text("v1")
        tasks = [task("first", inputs=["source.txt"]), task("second", needs=["first"]), task("independent")]
        e = self.engine(tasks); e.run()
        (self.root / "source.txt").write_text("v2")
        rows = e.refresh()
        self.assertEqual(rows["first"]["state"], "pending")
        self.assertEqual(rows["second"]["state"], "pending")
        self.assertEqual(rows["independent"]["state"], "succeeded")

    def test_output_tampering_invalidates_completion(self):
        e = self.engine([task()]); e.run()
        (self.root / "build.txt").write_text("altered")
        self.assertEqual(e.refresh()["build"]["state"], "pending")

    def test_known_transient_failure_retries_with_limit(self):
        argv = [sys.executable, "-c", "from pathlib import Path;import sys;p=Path('count');n=int(p.read_text())+1 if p.exists() else 1;p.write_text(str(n));Path('build.txt').write_text('ok');sys.exit(75 if n==1 else 0)"]
        e = self.engine([task(command=argv, retry={"max_attempts": 2, "exit_codes": [75]})])
        self.assertEqual(e.run()["execution"], "succeeded")
        self.assertEqual(self.state(e)["attempts"], 2)

    def test_unclassified_failure_does_not_retry_or_block_independent_task(self):
        e = self.engine([task(command=[sys.executable, "-c", "raise SystemExit(66)"],
                              retry={"max_attempts": 3, "exit_codes": [75]}), task("independent")])
        e.run()
        self.assertEqual(self.state(e)["attempts"], 1)
        self.assertEqual(self.state(e)["state"], "failed")
        self.assertEqual(self.state(e,"independent")["state"], "succeeded")

    def test_retry_budget_exhaustion_survives_resume(self):
        e = self.engine([task(command=[sys.executable, "-c", "raise SystemExit(75)"],
                              retry={"max_attempts": 2, "exit_codes": [75]})])
        e.run(); e.run()
        self.assertEqual(self.state(e)["attempts"], 2)
        self.assertEqual(self.state(e)["state"], "failed")

    def test_retry_requires_replay_safety(self):
        with self.assertRaisesRegex(ValueError, "replay-safe"):
            self.engine([task(replay_safe=False, retry={"max_attempts": 2})])

    def test_external_mutations_are_host_managed(self):
        with self.assertRaisesRegex(ValueError, "external"):
            self.engine([task(effect="external")])

    def test_missing_output_is_not_success(self):
        e = self.engine([task(command=[sys.executable, "-c", "pass"])])
        self.assertEqual(e.run()["execution"], "incomplete")
        self.assertEqual(self.state(e)["state"], "needs_attention")

    def test_failing_completion_check_is_not_retried_as_transient(self):
        e = self.engine([task(checks=[[sys.executable, "-c", "raise SystemExit(75)"]],
                              retry={"max_attempts": 3, "exit_codes": [75]})])
        e.run()
        self.assertEqual(self.state(e)["state"], "needs_attention")
        self.assertEqual(self.state(e)["attempts"], 1)

    def test_paths_and_symlinks_cannot_escape_workspace(self):
        with self.assertRaisesRegex(ValueError, "escapes"):
            self.engine([task(outputs=["../outside.txt"])])
        (self.root / "escape").symlink_to(self.root.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "escapes"):
            self.engine([task(outputs=["escape/outside.txt"])])

    def test_ownership_overlap_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "ownership"):
            self.engine([task("a", outputs=["shared.txt"]), task("b", outputs=["shared.txt"])])

    def test_missing_dependency_and_cycles_are_rejected(self):
        with self.assertRaises(ValueError): self.engine([task(needs=["absent"])])
        from graphlib import CycleError
        with self.assertRaises(CycleError):
            self.engine([task("a", needs=["b"]),task("b", needs=["a"])])

    def test_packet_is_scoped_and_does_not_embed_source_content(self):
        (self.root / "notes.txt").write_text("A long private source must remain on demand.")
        t = task(kind="agent", capability="report", instruction="Write a source-grounded report.", inputs=["notes.txt"])
        t.pop("command")
        e = self.engine([t]); packet = e.packet("build")
        self.assertEqual(packet["role"], "report-writer")
        self.assertNotIn("long private", json.dumps(packet))
        self.assertEqual(packet["owns_outputs"], ["build.txt"])
        self.assertTrue(Path(packet["skill_paths"][0]).is_file())

    def test_context_overflow_requires_task_split(self):
        with self.assertRaisesRegex(ValueError, "Split"):
            self.engine([task(context="x"*12001)])

    def test_agent_completion_rejects_changed_input(self):
        (self.root / "source.txt").write_text("before")
        t = task(kind="agent", capability="report", instruction="Draft.", inputs=["source.txt"])
        e = self.engine([t]); packet = e.packet("build")
        (self.root / "build.txt").write_text("draft")
        (self.root / "source.txt").write_text("after")
        with self.assertRaisesRegex(ValueError, "stale"): e.complete("build",packet["attempt_token"])
        self.assertEqual(self.state(e)["state"], "needs_attention")

    def test_recovery_invalidates_prior_completion_token(self):
        e = self.engine([task(kind="agent", instruction="Draft.")]); old = e.packet("build")
        e.recover("build", "Confirmed old worker stopped; no external effects.")
        new = e.packet("build"); (self.root / "build.txt").write_text("new")
        with self.assertRaisesRegex(ValueError, "token"): e.complete("build", old["attempt_token"])
        e.complete("build",new["attempt_token"])

    def test_two_dispatchers_cannot_claim_the_same_task(self):
        tasks = [task(kind="agent",instruction="Draft.")]
        e = self.engine(tasks); e.packet("build")
        other = self.engine(tasks)
        with self.assertRaisesRegex(ValueError, "not ready"): other.packet("build")
        self.assertEqual(self.state(e)["state"], "running")

    def test_verified_evidence_requires_verification_scope(self):
        e = self.engine([task()])
        with self.assertRaisesRegex(ValueError, "verification"):
            e.record_evidence({"id":"c1","claim":"Ready","status":"verified","sources":[]})

    def test_evidence_changes_become_stale_not_silently_reverified(self):
        e = self.engine([task()]); e.run()
        e.record_evidence({"id":"c1","claim":"The output says done","status":"reported",
                           "sources":[{"path":"build.txt","locator":"entire file"}]})
        (self.root / "build.txt").write_text("changed")
        r = e.status()["evidence"][0]
        self.assertEqual(r["status"], "reported")
        self.assertEqual(r["freshness"], "stale")

    def test_input_mutation_by_a_check_cannot_be_accepted(self):
        (self.root / "source.txt").write_text("before")
        e = self.engine([task(inputs=["source.txt"], checks=[write_command("source.txt","after")])])
        e.run()
        self.assertNotEqual(self.state(e)["state"], "succeeded")

    def test_second_runner_cannot_change_a_claimed_task_state(self):
        e = self.engine([task()]); e.claim("build")
        e.run_task("build")
        self.assertEqual(self.state(e)["state"], "running")

    def test_evidence_retains_the_producing_task_revision(self):
        (self.root / "source.txt").write_text("v1")
        e = self.engine([task(inputs=["source.txt"])]);e.run()
        e.record_evidence({"id":"c1","claim":"Ready at revision 1","status":"verified","verification":"Inspected output for revision 1",
                           "task":"build","sources":[{"path":"build.txt","locator":"entire file"}]})
        (self.root / "source.txt").write_text("v2");e.run()
        self.assertEqual(e.status()["evidence"][0]["freshness"], "stale")

    def test_outputs_cannot_overwrite_coordinator_state(self):
        with self.assertRaisesRegex(ValueError, "state"):
            self.engine([task(outputs=[".harness/state.sqlite3"])])

    def test_manifest_is_relative_to_selected_workspace(self):
        e = self.engine([task()])
        other = Engine(self.root, "task.json");self.engines.append(other)
        self.assertEqual(other.ready(),["build"])

    def test_existing_stale_artifact_is_not_a_new_success(self):
        (self.root / "build.txt").write_text("old output")
        e = self.engine([task(command=[sys.executable,"-c","pass"])])
        self.assertEqual(e.run()["execution"],"incomplete")
        self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_explicit_check_can_revalidate_unchanged_artifact(self):
        (self.root / "build.txt").write_text("valid")
        e = self.engine([task(command=[sys.executable,"-c","pass"], checks=[
            [sys.executable,"-c","from pathlib import Path;assert Path('build.txt').read_text()=='valid'"]])])
        self.assertEqual(e.run()["execution"],"succeeded")

    def test_check_cannot_rewrite_the_completion_artifact(self):
        e = self.engine([task(checks=[write_command("build.txt","different")])])
        e.run();self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_reading_another_tasks_output_needs_a_dependency(self):
        with self.assertRaisesRegex(ValueError,"dependency"):
            self.engine([task("a"),task("b",inputs=["a.txt"])])

    def test_retry_after_timeout_is_explicit_and_bounded(self):
        e = self.engine([task(command=[sys.executable,"-c","import time;time.sleep(1)"], timeout_seconds=.05,
                              retry={"max_attempts":2,"timeout":True})])
        e.run();self.assertEqual(self.state(e)["attempts"],2)
        self.assertEqual(self.state(e)["state"],"failed")

    def test_missing_executable_needs_repair_not_automatic_retry(self):
        e = self.engine([task(command=["definitely-not-a-real-harness-command"],
                              retry={"max_attempts":2,"exit_codes":[75]})])
        e.run();self.assertEqual(self.state(e)["attempts"],1)
        self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_independent_agents_have_distinct_claims_and_context(self):
        e = self.engine([task("plan",kind="agent",capability="project-plan",instruction="Plan."),
                         task("brief",kind="agent",capability="briefing",instruction="Brief.")])
        self.assertEqual(set(e.ready()),{"plan","brief"})
        a=e.packet("plan");b=e.packet("brief")
        self.assertNotEqual(a["attempt_token"],b["attempt_token"])
        self.assertNotEqual(a["role"],b["role"])
        self.assertFalse(set(a["owns_outputs"])&set(b["owns_outputs"]))

    def test_instruction_overflow_also_requires_task_split(self):
        with self.assertRaisesRegex(ValueError,"Split"):
            self.engine([task(kind="agent",instruction="x"*12001)])

    def test_replay_safety_is_a_boolean_not_a_truthy_string(self):
        with self.assertRaisesRegex(ValueError,"boolean"):
            self.engine([task(replay_safe="false",retry={"max_attempts":2})])

    def test_missing_agent_acceptance_checker_records_failure(self):
        e=self.engine([task(kind="agent",instruction="Draft.",checks=[["missing-harness-checker-command"]])])
        packet=e.packet("build");(self.root/"build.txt").write_text("draft")
        with self.assertRaises(OSError):e.complete("build",packet["attempt_token"])
        self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_automatic_retry_cannot_silently_switch_input_revision(self):
        (self.root/"source.txt").write_text("original")
        argv=[sys.executable,"-c","from pathlib import Path;Path('source.txt').write_text('changed');raise SystemExit(75)"]
        e=self.engine([task(command=argv,inputs=["source.txt"],retry={"max_attempts":2,"exit_codes":[75]})])
        e.run()
        self.assertEqual(self.state(e)["attempts"],1)
        self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_attempt_retains_input_fingerprints_for_inspection(self):
        (self.root/"source.txt").write_text("source")
        e=self.engine([task(inputs=["source.txt"])]);e.run()
        event=json.loads(e.store.db.execute("SELECT detail FROM events WHERE action='started'").fetchone()[0])
        self.assertIn("source.txt",event.get("inputs",{}))

    def test_input_change_during_retry_delay_stops_the_retry(self):
        source=self.root/"source.txt";source.write_text("original")
        e=self.engine([task(inputs=["source.txt"],command=[sys.executable,"-c","raise SystemExit(75)"],
                            retry={"max_attempts":2,"exit_codes":[75],"delay_seconds":1})])
        with patch.object(e,"execute",return_value=75), patch(
                "harness.runtime.engine.time.sleep",side_effect=lambda _:source.write_text("changed")):
            e.run()
        self.assertEqual(self.state(e)["attempts"],1)
        self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_packet_size_rejection_does_not_reserve_an_attempt(self):
        e=self.engine([task(kind="agent",instruction="i"*12000,context="c"*11000,
                            references=[f"ref{n}.md" for n in range(550)])])
        current=len(json.dumps(make_packet(e.tasks["build"],"","",self.root),ensure_ascii=False))
        e.tasks["build"]["context"]+="c"*(31950-current)
        self.assertLessEqual(len(e.tasks["build"]["context"]),12000)
        e.sync()
        with self.assertRaisesRegex(ValueError,"32,000"):
            e.packet("build")
        self.assertEqual(self.state(e)["state"],"pending")
        self.assertEqual(self.state(e)["attempts"],0)

    def test_evidence_cli_record_is_relative_to_selected_workspace(self):
        self.engine([task()])
        (self.root/"evidence.json").write_text(json.dumps({"id":"open","claim":"Awaiting review", "status":"open","sources":[]}))
        result=subprocess.run([sys.executable,"-B","-m","harness.runtime","--root",str(self.root),
                               "--manifest","task.json","evidence","evidence.json"],
                              cwd=Path(__file__).resolve().parents[2],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)["evidence"][0]["id"],"open")

    def test_execution_validation_error_is_recorded_as_attention(self):
        e=self.engine([task()])
        with patch.object(e,"execute",side_effect=ValueError("Invalid execution argument")):
            e.run()
        self.assertEqual(self.state(e)["state"],"needs_attention")

    def test_completion_and_recovery_cannot_interleave_their_state_writes(self):
        tasks=[task(kind="agent",instruction="Draft.")]
        e=self.engine(tasks);packet=e.packet("build")
        other=self.engine(tasks);other.store.db.execute("PRAGMA busy_timeout=0")
        (self.root/"build.txt").write_text("draft")
        original_update=e.store.update;recovery_blocked=[]

        def racing_update(i,**fields):
            if fields.get("state")=="succeeded":
                try:
                    other.recover(i,"Concurrent recovery must not supersede a committing completion.")
                except sqlite3.OperationalError as error:
                    self.assertIn("locked",str(error));recovery_blocked.append(True)
                else:
                    other.packet(i)
            return original_update(i,**fields)

        with patch.object(e.store,"update",side_effect=racing_update):
            e.complete("build",packet["attempt_token"])
        self.assertEqual(recovery_blocked,[True])
        self.assertEqual(self.state(e)["attempts"],1)
        self.assertEqual(self.state(e)["token"],packet["attempt_token"])

    def test_old_retry_runner_cannot_overwrite_a_recovered_attempt(self):
        tasks=[task(retry={"max_attempts":2,"exit_codes":[75],"delay_seconds":1})]
        e=self.engine(tasks);other=self.engine(tasks);new_tokens=[]

        def recover_during_backoff(_):
            other.recover("build","A new host takes responsibility for this attempt.")
            new_tokens.append(other.claim("build")[0])

        with patch.object(e,"execute",return_value=75), patch(
                "harness.runtime.engine.time.sleep",side_effect=recover_during_backoff):
            e.run_task("build")
        self.assertEqual(self.state(e)["state"],"running")
        self.assertEqual(self.state(e)["token"],new_tokens[0])
        self.assertEqual(self.state(e)["attempts"],1)

    def test_claim_can_join_a_durable_host_dispatch_transaction(self):
        e=self.engine([task(kind="agent",instruction="Draft.")])
        with self.assertRaisesRegex(RuntimeError,"Abort host request"):
            with e.store.transaction():
                e.packet("build")
                raise RuntimeError("Abort host request before it is persisted")
        self.assertEqual(self.state(e)["state"],"pending")
        self.assertEqual(self.state(e)["attempts"],0)
        self.assertEqual(e.store.db.execute("SELECT COUNT(*) FROM events").fetchone()[0],0)

    def test_role_revision_invalidates_a_completed_agent_result(self):
        catalog=self.root/"capabilities";roles=catalog/"agents";routes=catalog/"orchestration"
        roles.mkdir(parents=True);routes.mkdir()
        (routes/"routes.json").write_text(json.dumps({"implementation":{"role":"code-engineer","skills":[]}}))
        role=roles/"code-engineer.md";role.write_text("Original task responsibility")
        with patch("harness.runtime.dispatch.HARNESS",catalog):
            e=self.engine([task(kind="agent",instruction="Draft.")]);packet=e.packet("build")
            (self.root/"build.txt").write_text("draft")
            e.complete("build",packet["attempt_token"])
            role.write_text("Revised acceptance responsibility")
            self.assertEqual(e.refresh()["build"]["state"],"pending")

    def test_nested_transaction_rollback_keeps_outer_work(self):
        e=self.engine([task()])
        with e.store.transaction():
            e.store.event("build","outer",{})
            with self.assertRaisesRegex(RuntimeError,"Inner"):
                with e.store.transaction():
                    e.store.event("build","inner",{})
                    raise RuntimeError("Inner attempt failed")
        actions=[r[0] for r in e.store.db.execute("SELECT action FROM events")]
        self.assertEqual(actions,["outer"])

    def test_native_context_tracking_preserves_existing_command_checkpoints(self):
        e=self.engine([task()]);e.run()
        legacy=digest({"task":e.tasks["build"],"inputs":fingerprints(self.root,[]),"dependencies":{}})
        with e.store.transaction():
            e.store.update("build",signature=legacy)
        self.assertEqual(e.refresh()["build"]["state"],"succeeded")


if __name__ == "__main__":
    unittest.main()
