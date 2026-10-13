# Real native project delivery

This workflow inspects the current maintained FinEconHarness repository and delivers a project status, technical evidence review, delivery plan, project-owner report, decision brief and independent claim review. These artifacts must be authored by actual native host agents. The scripts prepare contracts, execute real implementation checks, capture observed durable state and assemble the final cover. They never manufacture agent outputs or simulate a successful host receipt.

The source boundary excludes `Paper/`, `sample_repository/`, author implementation material, research data and the war-discourse example. The checks inspect maintained instruction boundaries and project implementation. No network, external messages, installation, budget or deadline is involved. The existing standard-library runtime and route catalog provide coordination; the example adds a task-specific inventory and acceptance checks.

## Prepare and execute

From the repository root:

```bash
python3 -B harness/examples/native-project/check_helpers.py
python3 -B harness/examples/native-project/project_run.py prepare --output outputs/native-project-run
python3 -B -m harness.runtime --root "$PWD" --manifest outputs/native-project-run/task.json --state-dir outputs/native-project-run/.harness run
```

`prepare` writes the real task manifest and a small `requirements.json`. It refuses to overwrite a run with durable state. The manifest records the absolute repository root and workspace-relative state directory; pass both CLI options explicitly. `run` executes capture and stops with incomplete status when native agents are required. The capture includes unittest discovery, paper-first boundary checks, shared-role synchronization, the example helper checks and `git diff --check` for the maintained scope. Actual argument vectors, timestamps, exit codes, stdout/stderr and log hashes are saved. A failing check rejects capture. Snapshot inventory reports actual route, role, skill, runtime and check counts/sizes, git HEAD/status, Python version and source hashes. Prepare enumerates source entrypoints as invalidation inputs; start a new prepared run after adding source files.

The authorized host orchestrator then uses `NativeDispatcher.prepare(authorized=True)` or the matching native CLI. For each returned request, call `begin(token)` before the real `collaboration.spawn_agent(**request["tool_args"])`, then `bind(token, actual_canonical_agent_name)`. The fresh agent loads its saved context and uses the supplied `native read` command for scoped sources. Once the host observes its real terminal return, call `settle(token, actual_canonical_agent_name, "completed", final_json_text)`. Run local commands again and dispatch newly ready agents until the DAG finishes. Never replace these host calls with authored receipt fixtures. A spawn with unknown outcome must be reconciled rather than resent.

```python
from harness.runtime.engine import Engine
from harness.runtime.native import NativeDispatcher

engine = Engine(root, "outputs/native-project-run/task.json", "outputs/native-project-run/.harness")
dispatcher = NativeDispatcher(engine, max_workers=2, available_agent_types=("default",),
                              max_initial_chars=16000, max_read_chars=40000, max_chunk_chars=8000)
engine.run()
requests = dispatcher.prepare(authorized=True)
# The host performs begin -> actual native spawn -> bind -> observed terminal result -> settle.
print(dispatcher.status())
engine.close()
```

The limits measure supplied initial characters/UTF-8 bytes and cooperative audited source reads. Helper-mediated reads are actual audited accesses; this audit does not prove no direct reads occurred. It does not measure provider token counts, hidden host context or filesystem isolation. Each request embeds the route-selected semantic role and initial skill even when the native host uses its available `default` agent type. Agent outputs have disjoint ownership.

## Dependency and artifact contract

```text
capture -> project_status ----+
        -> technical_review --+-> project_plan -> checkpoint -> report -> brief --------+
                                                                     -> claim_review -+-> publish
```

| Task | Capability / initial skill | Owned outputs |
|---|---|---|
| capture | Local command | `snapshot.json`, `validation.json` |
| project_status | project-status / project-status-efh | `status.json`, `status.html` |
| technical_review | evidence-review / evidence-tracking-efh | `technical-review.json` |
| project_plan | project-plan / project-planning-efh | `delivery-plan.json` |
| checkpoint | Local read/capture command | `before-report.json` |
| report | report / report-writing-efh | `report.html` |
| brief | briefing / briefing-writing-efh | `brief.html` |
| claim_review | evidence-review / evidence-tracking-efh | `claim-review.json` |
| publish | Local command | `run-summary.json`, `index.html` |

Agent JSON and HTML metadata always include nonempty `as_of`, `scope` and `sources`. Each source is `{"path": "outputs/native-project-run/snapshot.json", "locator": "inventory.skill_entrypoints.count"}` or an equally precise existing maintained source and field/line locator. Paths in metadata are workspace-relative; HTML hyperlinks are relative to the HTML file. Source pointers are provenance, not proof of the associated claim.

- `status.json`: `milestones` is a nonempty list of `{deliverable, state, sources}`. Allowed states are `completed_and_checked`, `produced_unchecked`, `in_progress`, `blocked`, `stale`, `planned`. Include `risks` and nonempty `next_actions`, naming responsible roles where useful. `status.html` contains the same JSON object in its artifact-data and an owner-readable narrative.
- `technical-review.json`: `verdict` is `approved` or `changes_required`; `findings` is a list of `{severity, finding, action, sources}`, with severity `blocking` or `nonblocking`. Preserve a clearly described review scope even when findings are empty. A blocking finding requires `changes_required`.
- `delivery-plan.json`: `deliverables` is a nonempty list of `{deliverable, priority, dependencies, owner, acceptance, sources}`. Priority is a positive integer; dependencies is a list; acceptance is an observable outcome. Include `risks`. Do not invent deadlines, effort, budget or staffed capacity.
- HTML artifacts contain `<script type="application/json" id="artifact-data">{...}</script>` with machine-checkable claims, alongside readable prose, a title and headings. The JSON is not a substitute for the report or brief.
- `report.html` metadata adds `audience`, `lead_finding`, `recommendation`, and `facts`. Facts include `inventory_counts` (every snapshot inventory group's actual count), `check_exit_codes` (every validation check's actual exit code), `checkpoint_native_accepted` (only requests with `state: accepted` and `current_attempt: true`), `checkpoint_execution`, and `provider_token_count: null`. Historical accepted attempts remain in the audit and are excluded from the current count. Explain delivered/in-progress work, source/check evidence, recommendations, uncertainty and the native/context measurement limits in visible prose.
- `brief.html` metadata adds `decision`, `tradeoffs`, and `actions`. Its visible prose is a concise owner-facing decision memo based on the accepted report and plan, with evidence pointers and roles for actions.
- `claim-review.json` has the review verdict/findings fields plus at least three material `judgments`, each `{claim, support, basis, sources}`. Support is `verified`, `reported`, `inferred`, `conflicting` or `open`. The independent reviewer compares the actual report wording with sources, including numeric facts, phase timing and context limits. Unsupported material claims block publication.

`before-report.json` is an immutable observation made after the plan is accepted and before report delivery. It captures the runtime's real task state and native public status, including actual IDs and context metrics. It must show the first three native tasks accepted while the workflow remains incomplete. It neither settles native tasks nor establishes final completion. If this checkpoint exists after an interrupted attempt, preserve it and reconcile/recover explicitly; the script refuses to overwrite it.

Publication requires all six current native tasks accepted with actual bound IDs and loaded context, no unresolved dispatches, and independent claim review approval without blocking findings. `run-summary.json` exports actual native roles/host types, input and artifact hashes, context metrics and phase distinction. `index.html` links the accepted deliveries and this final evidence; it does not alter the accepted report. The summary is captured during publish acceptance. Query runtime `status` after publish to confirm the runtime subsequently accepted that command and the whole graph succeeded.

## Acceptance and limits

```bash
python3 -B harness/examples/native-project/validate.py --stage report --output outputs/native-project-run
python3 -B -m harness.runtime --root "$PWD" --manifest outputs/native-project-run/task.json --state-dir outputs/native-project-run/.harness status
```

Each task declares its appropriate read-only stage check. Structural checks reject missing fields, unsupported states, broken source paths/links, inconsistent report counts/check outcomes and contradictory blocking approvals. They do not grade LLM quality or treat text shape as substantive verification. Independent actual native reviews provide the separate support assessment, whose own limits remain visible.

`check_helpers.py` uses bounded helper-only fixtures to test negative cases: escaping/corpus sources, missing locators, invalid completion vocabulary, blocking approval, missing claim judgments, mismatched report counts, historical accepted attempts included in current counts, invented provider tokens, missing HTML links, immutable checkpoint overwrite and preserved check timeout output. Those fixtures are never delivered as real workflow evidence. Real workflow outputs come solely from the current repository, executed commands, actual host dispatch state and the six native agents.
