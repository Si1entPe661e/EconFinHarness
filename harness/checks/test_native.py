"""Native adapter checks use observed-handle fixtures, never fake real tool execution."""
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from harness.runtime.engine import Engine
from harness.runtime.native import NativeDispatcher


def agent(name="build", **fields):
    value = {"id": name, "kind": "agent", "instruction": "Produce the scoped output.",
             "capability": "implementation", "outputs": [name + ".txt"]}
    value.update(fields)
    return value


class NativeChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="native harness ")
        self.root = Path(self.temp.name)
        self.engines = []

    def tearDown(self):
        for engine in self.engines:
            engine.close()
        self.temp.cleanup()

    def dispatcher(self, tasks=None, state_dir=".state dir", **options):
        manifest = self.root / "task.json"
        manifest.write_text(json.dumps({"version": 1, "goal": "Native adapter checks", "tasks": tasks or [agent()]}))
        engine = Engine(self.root, manifest, state_dir)
        self.engines.append(engine)
        return NativeDispatcher(engine, **options)

    def prepared(self, dispatcher):
        return dispatcher.prepare(authorized=True)[0]

    def bound(self, dispatcher):
        request = self.prepared(dispatcher)
        dispatcher.begin(request["token"])
        native_id = "/root/" + request["tool_args"]["task_name"]
        dispatcher.bind(request["token"], native_id)
        dispatcher.context(request["token"])
        return request, native_id

    def final(self, request, **fields):
        value = {"task": request["task"], "attempt_token": request["token"],
                 "input_signature": request["input_signature"], "status": "completed",
                 "artifacts": request["packet"]["owns_outputs"], "summary": "Created output; acceptance checks passed.",
                 "unresolved": []}
        value.update(fields)
        return json.dumps(value)

    def output(self, request):
        for path in request["packet"]["owns_outputs"]:
            (self.root / path).write_text("actual output for " + request["token"])

    def settle(self, dispatcher, request, native_id, **fields):
        self.output(request)
        return dispatcher.settle(request["token"], native_id, "completed", self.final(request, **fields))

    def test_authorization_precedes_any_claim(self):
        dispatcher = self.dispatcher()
        for authorization in (False, None, "true", 1):
            with self.assertRaisesRegex(ValueError, "authorization"):
                dispatcher.prepare(authorization)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "pending")
        self.assertEqual(dispatcher.status()["requests"], [])

    def test_fresh_context_exact_tool_args_and_persisted_prompt(self):
        dispatcher = self.dispatcher(available_agent_types=("default", "code_engineer"))
        request = self.prepared(dispatcher)
        args = request["tool_args"]
        self.assertEqual(set(args), {"task_name", "agent_type", "fork_turns", "message"})
        self.assertEqual(args["agent_type"], "code_engineer")
        self.assertEqual(args["fork_turns"], "none")
        self.assertRegex(args["task_name"], r"^native_[a-f0-9]{32}$")
        self.assertIn("native context --token " + request["token"], args["message"])
        self.assertIn("--state-dir '.state dir'", args["message"])
        self.assertNotIn("model:", request["prompt"])
        self.assertEqual(request["context"]["initial_chars"], len(request["prompt"]) + len(args["message"]))
        self.assertEqual(request["context"]["initial_utf8_bytes"], len((request["prompt"] + args["message"]).encode()))
        self.assertEqual(dispatcher.prepare(True), [request])

    def test_unadvertised_semantic_role_uses_explicit_default_handoff(self):
        dispatcher = self.dispatcher([agent(capability="report")])
        request = self.prepared(dispatcher)
        self.assertEqual(request["role"], "report-writer")
        self.assertEqual(request["host_agent_type"], "default")
        self.assertIn("Semantic role: report-writer. Native host agent type: default.", request["prompt"])
        self.assertIn("Initial skill report-writing-efh:", request["prompt"])
        self.assertEqual(request["tool_args"]["agent_type"], "default")

    def test_unknown_capability_or_missing_role_skill_never_claims(self):
        dispatcher = self.dispatcher([agent(capability="unknown")])
        with self.assertRaisesRegex(ValueError, "Unknown capability"):
            dispatcher.prepare(True)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["attempts"], 0)
        with patch("harness.runtime.dispatch.route", return_value={"role": "absent", "skills": []}):
            with self.assertRaises(OSError):
                dispatcher.prepare(True)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["attempts"], 0)
        with patch("harness.runtime.dispatch.route", return_value={"role": "code-engineer", "skills": ["absent"]}):
            with self.assertRaisesRegex(ValueError, "Unknown skill"):
                dispatcher.prepare(True)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "pending")

    def test_initial_budget_rejected_before_claim(self):
        dispatcher = self.dispatcher(max_initial_chars=100)
        with self.assertRaisesRegex(ValueError, "initial character budget"):
            dispatcher.prepare(True)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["attempts"], 0)
        self.assertEqual(dispatcher.status()["requests"], [])

    def test_packet_only_points_to_input_contents(self):
        secret = "private input content is read only on demand"
        (self.root / "source.txt").write_text(secret)
        dispatcher = self.dispatcher([agent(inputs=["source.txt"])])
        request = self.prepared(dispatcher)
        self.assertNotIn(secret, request["prompt"])
        self.assertNotIn(secret, json.dumps(request["packet"]))

    def test_fanout_capacity_and_all_branch_join(self):
        dispatcher = self.dispatcher([agent("join", needs=["left", "right"]), agent("left"), agent("right"), agent("extra")])
        requests = dispatcher.prepare(True)
        self.assertEqual({request["task"] for request in requests}, {"left", "right"})
        self.assertEqual(dispatcher.status()["running"], 2)
        left, right = requests
        for request in (left, right):
            dispatcher.begin(request["token"])
            native_id = "/root/" + request["tool_args"]["task_name"]
            dispatcher.bind(request["token"], native_id)
            dispatcher.context(request["token"])
            self.settle(dispatcher, request, native_id)
            if request == left:
                self.assertNotIn("join", dispatcher.engine.ready())
        self.assertIn("join", dispatcher.engine.ready())
        next_requests = dispatcher.prepare(True)
        self.assertEqual({request["task"] for request in next_requests}, {"join", "extra"})

    def test_sending_outcome_is_unknown_and_never_resent_after_reopen(self):
        dispatcher = self.dispatcher([agent("one"), agent("two")], max_workers=1)
        request = self.prepared(dispatcher)
        dispatcher.begin(request["token"])
        with self.assertRaisesRegex(ValueError, "already begun"):
            dispatcher.begin(request["token"])
        self.assertEqual(dispatcher.prepare(True), [])
        other_engine = Engine(self.root, "task.json", ".state dir")
        self.engines.append(other_engine)
        other = NativeDispatcher(other_engine, max_workers=1)
        self.assertEqual(other.prepare(True), [])
        status = other.status()
        self.assertEqual((status["running"], status["available"]), (1, 0))
        self.assertIn("unknown", status["unresolved_dispatches"][0]["reason"])
        self.assertEqual(other_engine.store.rows()["two"]["state"], "pending")
        handle = "/root/" + request["tool_args"]["task_name"]
        other.bind(request["token"], handle)
        other.context(request["token"])
        self.settle(other, request, handle)
        self.assertEqual(other.prepare(True)[0]["task"], "two")

    def test_bind_requires_begin_and_observed_canonical_handle(self):
        dispatcher = self.dispatcher()
        request = self.prepared(dispatcher)
        handle = "/root/" + request["tool_args"]["task_name"]
        with self.assertRaisesRegex(ValueError, "begun"):
            dispatcher.bind(request["token"], handle)
        dispatcher.begin(request["token"])
        for invalid in (None, False, "", "fake", "/root/wrong_task"):
            with self.assertRaisesRegex(ValueError, "actual canonical"):
                dispatcher.bind(request["token"], invalid)
        dispatcher.bind(request["token"], handle)
        self.assertEqual(dispatcher.bind(request["token"], handle)["native_id"], handle)

    def test_a_native_handle_cannot_bind_two_attempts(self):
        dispatcher = self.dispatcher([agent("one"), agent("two")])
        one, two = dispatcher.prepare(True)
        for request in (one, two):
            dispatcher.begin(request["token"])
        handle = "/root/" + one["tool_args"]["task_name"]
        dispatcher.bind(one["token"], handle)
        with self.assertRaises(ValueError):
            dispatcher.bind(two["token"], handle)
        # The durable uniqueness constraint also protects against bypassing validation.
        with self.assertRaises(sqlite3.IntegrityError), dispatcher.store.transaction():
            dispatcher.store.db.execute("UPDATE native_requests SET native_id=? WHERE token=?", (handle, two["token"]))

    def test_settlement_requires_actual_bound_handle(self):
        dispatcher = self.dispatcher()
        request = self.prepared(dispatcher)
        for handle in (None, False, "invented", "/root/not_bound"):
            with self.assertRaisesRegex(ValueError, "actual bound"):
                dispatcher.settle(request["token"], handle, "completed", self.final(request))
        dispatcher.begin(request["token"])
        handle = "/root/" + request["tool_args"]["task_name"]
        with self.assertRaisesRegex(ValueError, "actual bound"):
            dispatcher.settle(request["token"], handle, "completed", self.final(request))
        dispatcher.bind(request["token"], handle)
        with self.assertRaisesRegex(ValueError, "terminal state"):
            dispatcher.settle(request["token"], handle, "running", self.final(request))
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "running")

    def test_context_must_be_loaded_before_success(self):
        dispatcher = self.dispatcher()
        request = self.prepared(dispatcher)
        dispatcher.begin(request["token"])
        handle = "/root/" + request["tool_args"]["task_name"]
        dispatcher.bind(request["token"], handle)
        self.output(request)
        with self.assertRaisesRegex(ValueError, "never loaded"):
            dispatcher.settle(request["token"], handle, "completed", self.final(request))
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
        self.assertEqual(dispatcher.status()["requests"][0]["state"], "rejected")

    def test_strict_status_and_return_shape_are_required(self):
        invalids = [lambda value: value.pop("status"), lambda value: value.update(status=None),
                    lambda value: value.update(status=True), lambda value: value.update(status="succeeded"),
                    lambda value: value.update(artifacts=[]),
                    lambda value: value.update(summary="x" * 2001), lambda value: value.update(extra="undeclared")]
        for change in invalids:
            with self.subTest(change=change):
                # Explicit recovery is required; each subtest uses a new state directory.
                dispatcher = self.dispatcher()
                request, handle = self.bound(dispatcher)
                value = json.loads(self.final(request))
                change(value)
                with self.assertRaises(ValueError):
                    dispatcher.settle(request["token"], handle, "completed", json.dumps(value))
                self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
                dispatcher.engine.recover("build", "Prior fixture host stopped; malformed return was inspected.")

    def test_missing_malformed_oversized_and_duplicate_json_returns_rejected(self):
        invalids = [None, "", "```json\n{}\n```", "x" * 6001, "[]", '{"status":"completed","status":"failed"}']
        dispatcher = self.dispatcher()
        for text in invalids:
            with self.subTest(text=str(text)[:30]):
                request, handle = self.bound(dispatcher)
                with self.assertRaises(ValueError):
                    dispatcher.settle(request["token"], handle, "completed", text)
                self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
                dispatcher.engine.recover("build", "Prior fixture host stopped; invalid return reconciled.")

    def test_wrong_task_token_and_signature_cannot_complete(self):
        dispatcher = self.dispatcher()
        for fields in ({"task": "other"}, {"attempt_token": "old"}, {"input_signature": "stale"}):
            request, handle = self.bound(dispatcher)
            with self.assertRaisesRegex(ValueError, "does not match"):
                self.settle(dispatcher, request, handle, **fields)
            dispatcher.engine.recover("build", "Host outcome inspected; rejected attempt is stopped.")

    def test_missing_outputs_and_failing_real_checks_are_rejected(self):
        dispatcher = self.dispatcher()
        request, handle = self.bound(dispatcher)
        with self.assertRaisesRegex(ValueError, "Missing input or output"):
            dispatcher.settle(request["token"], handle, "completed", self.final(request))
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
        dispatcher.engine.recover("build", "Missing output was inspected; old worker stopped.")
        # A new specification gets a distinct signature and real failing subprocess check.
        dispatcher = self.dispatcher([agent(checks=[[sys.executable, "-c", "raise SystemExit(7)"]])])
        request, handle = self.bound(dispatcher)
        with self.assertRaisesRegex(ValueError, "failed with exit 7"):
            self.settle(dispatcher, request, handle)
        self.assertTrue(list(dispatcher.engine.state_dir.glob("logs/*check0.log")))
        self.assertEqual(dispatcher.status()["requests"][-1]["state"], "rejected")

    def test_success_and_exact_duplicate_receipt_are_idempotent(self):
        dispatcher = self.dispatcher()
        request, handle = self.bound(dispatcher)
        result = self.settle(dispatcher, request, handle)
        self.assertEqual(result["state"], "accepted")
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "succeeded")
        same = dispatcher.settle(request["token"], handle, "completed", self.final(request))
        self.assertEqual(same, result)
        with self.assertRaisesRegex(ValueError, "same handle and content"):
            dispatcher.settle(request["token"], handle, "completed", self.final(request, summary="different"))
        self.assertEqual(dispatcher.prepare(True), [])

    def test_failed_and_interrupted_observed_workers_need_explicit_recovery(self):
        dispatcher = self.dispatcher()
        for terminal, task_state in (("failed", "failed"), ("interrupted", "needs_attention")):
            request, handle = self.bound(dispatcher)
            result = dispatcher.settle(request["token"], handle, terminal, "Observed native terminal event.")
            self.assertEqual(result["state"], terminal)
            self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], task_state)
            self.assertEqual(dispatcher.prepare(True), [])
            dispatcher.engine.recover("build", "Observed terminal host outcome; retry authorized explicitly.")

    def test_reported_attention_or_failure_is_not_completed(self):
        dispatcher = self.dispatcher()
        for status in ("needs_attention", "failed"):
            request, handle = self.bound(dispatcher)
            with self.assertRaisesRegex(ValueError, "reported " + status):
                self.settle(dispatcher, request, handle, status=status)
            self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
            dispatcher.engine.recover("build", "Host terminal return inspected; old worker stopped.")

    def test_numbered_utf8_ranges_and_actual_context_metrics(self):
        (self.root / "source.txt").write_text("alpha\n中文\nomega\n", encoding="utf-8")
        dispatcher = self.dispatcher([agent(inputs=["source.txt"])])
        request, handle = self.bound(dispatcher)
        read = dispatcher.source_read(request["token"], "source.txt", 2, 2)
        self.assertEqual(read["text"], "2: 中文")
        self.assertEqual(read["chars"], 5)
        self.assertEqual(read["utf8_bytes"], 9)
        metrics = dispatcher.status()["requests"][0]["context"]
        self.assertTrue(metrics["loaded"])
        self.assertEqual(metrics["read_chars"], 5)
        self.settle(dispatcher, request, handle)

    def test_read_rejects_undeclared_escape_and_invalid_ranges(self):
        (self.root / "source.txt").write_text("one\ntwo\nthree\n")
        (self.root / "other.txt").write_text("not declared")
        dispatcher = self.dispatcher([agent(references=["source.txt"])])
        request, _ = self.bound(dispatcher)
        for path in ("other.txt", "../outside.txt", str(self.root / "source.txt")):
            with self.assertRaises(ValueError):
                dispatcher.source_read(request["token"], path)
        for start, end in ((0, None), (True, None), (2, 1), (4, None), (1, 4), (1, False)):
            with self.assertRaises(ValueError):
                dispatcher.source_read(request["token"], "source.txt", start, end)
        self.assertEqual(dispatcher.status()["requests"][0]["context"]["read_chars"], 0)

    def test_read_budget_is_per_call_and_cumulative_without_charging_rejections(self):
        (self.root / "source.txt").write_text("abc\ndef\nghi\n")
        dispatcher = self.dispatcher([agent(references=["source.txt"])], max_read_chars=12, max_chunk_chars=6)
        request, _ = self.bound(dispatcher)
        with self.assertRaisesRegex(ValueError, "per-call"):
            dispatcher.source_read(request["token"], "source.txt", 1, 2)
        self.assertEqual(dispatcher.source_read(request["token"], "source.txt", 1, 1)["remaining_chars"], 6)
        self.assertEqual(dispatcher.source_read(request["token"], "source.txt", 2, 2)["remaining_chars"], 0)
        with self.assertRaisesRegex(ValueError, "cumulative"):
            dispatcher.source_read(request["token"], "source.txt", 3, 3)
        self.assertEqual(dispatcher.status()["requests"][0]["context"]["read_chars"], 12)

    def test_read_requires_loaded_current_context(self):
        (self.root / "source.txt").write_text("source")
        dispatcher = self.dispatcher([agent(inputs=["source.txt"])])
        request = self.prepared(dispatcher)
        dispatcher.begin(request["token"])
        with self.assertRaisesRegex(ValueError, "Load native context"):
            dispatcher.source_read(request["token"], "source.txt")
        dispatcher.context(request["token"])
        dispatcher.engine.recover("build", "Old worker interrupted and stopped by fixture host.")
        with self.assertRaisesRegex(ValueError, "Stale"):
            dispatcher.source_read(request["token"], "source.txt")
        with self.assertRaisesRegex(ValueError, "Stale"):
            dispatcher.context(request["token"])

    def test_changed_read_reference_rejects_completion(self):
        path = self.root / "reference.txt"
        path.write_text("original")
        dispatcher = self.dispatcher([agent(references=["reference.txt"])])
        request, handle = self.bound(dispatcher)
        dispatcher.source_read(request["token"], "reference.txt")
        path.write_text("changed")
        with self.assertRaisesRegex(ValueError, "Read source changed"):
            self.settle(dispatcher, request, handle)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")

    def test_changed_role_resources_reject_completion(self):
        dispatcher = self.dispatcher()
        request, handle = self.bound(dispatcher)
        original = __import__("harness.runtime.native", fromlist=["_hash"])._hash
        role = request["packet"]["role_path"]
        with patch("harness.runtime.native._hash", side_effect=lambda path: "changed" if str(path) == role else original(path)):
            with self.assertRaisesRegex(ValueError, "role or skill changed"):
                self.settle(dispatcher, request, handle)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")

    def test_check_changing_read_reference_is_rejected_after_real_completion(self):
        path = self.root / "reference.txt"
        path.write_text("original")
        check = [sys.executable, "-c", "from pathlib import Path;Path('reference.txt').write_text('changed')"]
        dispatcher = self.dispatcher([agent(references=["reference.txt"], checks=[check])])
        request, handle = self.bound(dispatcher)
        dispatcher.source_read(request["token"], "reference.txt")
        with self.assertRaisesRegex(ValueError, "Read source changed"):
            self.settle(dispatcher, request, handle)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")

    def test_recovery_never_makes_old_return_current(self):
        dispatcher = self.dispatcher(max_workers=2)
        old, old_handle = self.bound(dispatcher)
        dispatcher.engine.recover("build", "Fixture host stopped old worker; a new attempt takes ownership.")
        new, new_handle = self.bound(dispatcher)
        self.assertNotEqual(old["token"], new["token"])
        with self.assertRaisesRegex(ValueError, "Stale native attempt"):
            self.settle(dispatcher, old, old_handle)
        row = dispatcher.engine.store.rows()["build"]
        self.assertEqual(row["token"], new["token"])
        self.assertEqual(row["state"], "running")
        self.settle(dispatcher, new, new_handle)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "succeeded")

    def test_two_dispatchers_share_atomic_capacity_and_claim(self):
        dispatcher = self.dispatcher([agent("one"), agent("two")], max_workers=1)
        request = self.prepared(dispatcher)
        engine = Engine(self.root, "task.json", ".state dir")
        self.engines.append(engine)
        other = NativeDispatcher(engine, max_workers=1)
        self.assertEqual(other.prepare(True)[0]["token"], request["token"])
        dispatcher.begin(request["token"])
        self.assertEqual(other.prepare(True), [])
        self.assertEqual(engine.store.rows()["two"]["attempts"], 0)

    def test_completed_deliverable_may_record_unresolved_findings(self):
        dispatcher = self.dispatcher()
        request, handle = self.bound(dispatcher)
        result = self.settle(dispatcher, request, handle,
                             unresolved=["Report documents a finding whose evidence remains uncertain."])
        self.assertEqual(result["state"], "accepted")
        self.assertEqual(len(result["result"]["unresolved"]), 1)

    def test_initial_context_is_loaded_only_once(self):
        dispatcher = self.dispatcher()
        request, _ = self.bound(dispatcher)
        with self.assertRaisesRegex(ValueError, "already loaded"):
            dispatcher.context(request["token"])
        events = dispatcher.store.db.execute("SELECT COUNT(*) FROM events WHERE action='native_context_loaded'").fetchone()[0]
        self.assertEqual(events, 1)

    def test_leaf_contract_and_read_helper_are_explicit(self):
        dispatcher = self.dispatcher()
        request = self.prepared(dispatcher)
        self.assertIn("Do not spawn other agents", request["prompt"])
        self.assertIn("native read --token", request["prompt"])
        self.assertIn("Substantive source reads must use this helper", request["prompt"])

    def test_independent_source_reads_work_during_acceptance_checks(self):
        (self.root / "reference.txt").write_text("independent source")
        dispatcher = self.dispatcher([agent("one"), agent("two", references=["reference.txt"])])
        one, two = dispatcher.prepare(True)
        for request in (one, two):
            dispatcher.begin(request["token"])
            dispatcher.bind(request["token"], "/root/" + request["tool_args"]["task_name"])
            dispatcher.context(request["token"])
        engine = Engine(self.root, "task.json", ".state dir")
        self.engines.append(engine)
        engine.store.db.execute("PRAGMA busy_timeout=0")
        other = NativeDispatcher(engine)
        original = dispatcher.engine.check_outputs
        readings = []

        def check_without_global_lock(task, token):
            readings.append(other.source_read(two["token"], "reference.txt")["text"])
            self.assertEqual(other._get(one["token"])["state"], "checking")
            return original(task, token)

        with patch.object(dispatcher.engine, "check_outputs", side_effect=check_without_global_lock):
            self.settle(dispatcher, one, "/root/" + one["tool_args"]["task_name"])
        self.assertEqual(readings, ["1: independent source"])

    def test_superseded_unknown_spawn_can_bind_for_explicit_reconciliation(self):
        dispatcher = self.dispatcher(max_workers=1)
        old = self.prepared(dispatcher)
        dispatcher.begin(old["token"])
        dispatcher.engine.recover("build", "Host is inspecting an uncertain old spawn outcome.")
        handle = "/root/" + old["tool_args"]["task_name"]
        observed = dispatcher.bind(old["token"], handle)
        self.assertTrue(observed["superseded"])
        self.assertEqual(dispatcher.status()["running"], 1)
        with self.assertRaisesRegex(ValueError, "Stale"):
            dispatcher.context(old["token"])
        dispatcher.resolve(old["token"], "stopped", "Host listed and stopped the old canonical native agent.")
        new = self.prepared(dispatcher)
        self.assertNotEqual(old["token"], new["token"])

    def test_unknown_outcome_resolution_requires_explicit_host_attestation(self):
        dispatcher = self.dispatcher(max_workers=1)
        request = self.prepared(dispatcher)
        dispatcher.begin(request["token"])
        for outcome, reason in (("not_started", ""), ("timeout", "Waited a while"), ("stopped", "No handle observed")):
            with self.assertRaises(ValueError):
                dispatcher.resolve(request["token"], outcome, reason)
        self.assertEqual(dispatcher.status()["running"], 1)
        result = dispatcher.resolve(request["token"], "not_started", "Host tool returned a definitive no-agent-created error.")
        self.assertEqual(result["state"], "resolved")
        self.assertEqual(dispatcher.status()["running"], 0)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
        self.assertEqual(dispatcher.prepare(True), [])
        dispatcher.engine.recover("build", "No native agent exists; host confirmed retry is safe.")
        self.assertNotEqual(self.prepared(dispatcher)["token"], request["token"])

    def test_resolving_old_bound_worker_cannot_change_newer_attempt(self):
        dispatcher = self.dispatcher(max_workers=2)
        old, _ = self.bound(dispatcher)
        dispatcher.engine.recover("build", "Old host worker was stopped; new attempt can own the task.")
        new, _ = self.bound(dispatcher)
        dispatcher.resolve(old["token"], "stopped", "Host observed the old native worker stopped.")
        row = dispatcher.engine.store.rows()["build"]
        self.assertEqual((row["token"], row["state"]), (new["token"], "running"))

    def test_resolution_during_acceptance_cannot_accept_a_stopped_request(self):
        dispatcher = self.dispatcher()
        request, handle = self.bound(dispatcher)
        original = dispatcher.engine.complete

        def stop_after_check(task, token):
            original(task, token)
            dispatcher.resolve(token, "stopped", "Host stopped the attempt while its acceptance phase was running.")

        with patch.object(dispatcher.engine, "complete", side_effect=stop_after_check):
            with self.assertRaisesRegex(ValueError, "superseded|resolved|checking"):
                self.settle(dispatcher, request, handle)
        self.assertNotEqual(dispatcher.engine.store.rows()["build"]["state"], "succeeded")
        self.assertEqual(dispatcher._get(request["token"])["state"], "resolved")

    def test_recovered_prepared_request_cannot_trap_capacity_or_be_returned(self):
        dispatcher = self.dispatcher(max_workers=1)
        old = self.prepared(dispatcher)
        dispatcher.engine.recover("build", "Prepared request has not crossed begin; host cancelled it before spawning.")
        new = self.prepared(dispatcher)
        self.assertNotEqual(old["token"], new["token"])
        self.assertEqual(dispatcher._get(old["token"])["state"], "superseded")
        self.assertEqual(dispatcher.status()["running"], 1)

    def test_resource_change_before_begin_releases_unstarted_request(self):
        dispatcher = self.dispatcher()
        request = self.prepared(dispatcher)
        with patch("harness.runtime.native._hash", return_value="changed"):
            with self.assertRaisesRegex(ValueError, "role or skill changed"):
                dispatcher.begin(request["token"])
        self.assertEqual(dispatcher._get(request["token"])["state"], "rejected")
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")
        self.assertEqual(dispatcher.status()["running"], 0)

    def test_input_change_after_engine_completion_cannot_accept_native_result(self):
        source = self.root / "source.txt"
        source.write_text("original")
        dispatcher = self.dispatcher([agent(inputs=["source.txt"])])
        request, handle = self.bound(dispatcher)
        original = dispatcher.engine.complete

        def change_after_complete(task, token):
            original(task, token)
            source.write_text("changed after checks")

        with patch.object(dispatcher.engine, "complete", side_effect=change_after_complete):
            with self.assertRaisesRegex(ValueError, "Inputs changed"):
                self.settle(dispatcher, request, handle)
        self.assertEqual(dispatcher.engine.store.rows()["build"]["state"], "needs_attention")

    def test_compact_status_exposes_audited_reads_and_final_return_length(self):
        (self.root / "source.txt").write_text("中文\n", encoding="utf-8")
        dispatcher = self.dispatcher([agent(inputs=["source.txt"])])
        request, handle = self.bound(dispatcher)
        dispatcher.source_read(request["token"], "source.txt")
        metrics = dispatcher.status()["requests"][0]["context"]
        self.assertEqual(metrics["source_read_count"], 1)
        self.assertEqual(metrics["read_utf8_bytes"], 9)
        self.assertNotIn("final_return_chars", metrics)
        self.settle(dispatcher, request, handle)
        metrics = dispatcher.status()["requests"][0]["context"]
        self.assertEqual(metrics["final_return_chars"], len(self.final(request)))

    def test_known_terminal_history_does_not_block_a_successfully_recovered_attempt(self):
        for terminal in ("failed", "interrupted", "rejected"):
            with self.subTest(terminal=terminal):
                dispatcher = self.dispatcher([agent(terminal)], state_dir=".state-" + terminal)
                old, handle = self.bound(dispatcher)
                final_text = "Observed host terminal capacity error." if terminal != "rejected" else "malformed return"
                if terminal == "rejected":
                    with self.assertRaises(ValueError):
                        dispatcher.settle(old["token"], handle, "completed", final_text)
                else:
                    dispatcher.settle(old["token"], handle, terminal, final_text)
                self.assertIn(old["token"], {value["token"] for value in dispatcher.status()["unresolved_dispatches"]})
                dispatcher.engine.recover(terminal, "Host terminal outcome observed; old worker stopped and recovery is safe.")
                new, new_handle = self.bound(dispatcher)
                self.settle(dispatcher, new, new_handle)
                status = dispatcher.status()
                self.assertEqual(status["unresolved_dispatches"], [])
                self.assertEqual(dispatcher.engine.store.rows()[terminal]["state"], "succeeded")
                retained = dispatcher._get(old["token"])
                self.assertEqual(retained["state"], terminal)
                self.assertEqual(retained["receipt"]["final_text"], final_text)
                self.assertEqual({value["token"] for value in status["requests"]} & {old["token"], new["token"]},
                                 {old["token"], new["token"]})

    def test_recovery_cannot_hide_an_unknown_or_stale_live_dispatch(self):
        for native_state in ("sending", "bound", "checking"):
            with self.subTest(native_state=native_state):
                dispatcher = self.dispatcher([agent(native_state)], state_dir=".state-" + native_state, max_workers=2)
                old = self.prepared(dispatcher)
                dispatcher.begin(old["token"])
                if native_state in ("bound", "checking"):
                    dispatcher.bind(old["token"], "/root/" + old["tool_args"]["task_name"])
                if native_state == "checking":
                    dispatcher.context(old["token"])
                    with patch.object(dispatcher.engine, "complete", side_effect=KeyboardInterrupt):
                        with self.assertRaises(KeyboardInterrupt):
                            self.settle(dispatcher, old, "/root/" + old["tool_args"]["task_name"])
                dispatcher.engine.recover(native_state, "Host is investigating the old worker; do not assume its outcome.")
                new, handle = self.bound(dispatcher)
                self.settle(dispatcher, new, handle)
                self.assertIn(old["token"], {value["token"] for value in dispatcher.status()["unresolved_dispatches"]})


if __name__ == "__main__":
    unittest.main()
