# Inspected patterns and local validation

The local repository-review workbook under `outputs/01a11ed4-7329-7260-b0dd-9ba13b18d446/repository-review/` guided this selection. Local snapshots are reference material, not runtime prerequisites. No third-party implementation was copied or vendored.

| Source | Inspected material | Adapted idea | Local validation |
|---|---|---|---|
| [LongTable](https://github.com/HosungYou/Diverga) | README; longtable-memory/core READMEs | Provider-neutral durable state, decision/evidence records and concise recovery context | SQLite restart, source-revision and producing-task-revision checks |
| [Pedro workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | README; `.claude/rules/orchestrator-protocol.md` | Bounded responsibilities, structured fan-out/join and explicit missing results; proportional process | Exclusive claims, old-token rejection, context/ownership checks and native-agent packets |
| [MixtapeTools](https://github.com/scunning1975/MixtapeTools) | `gtd/README.md`; raw-data integrity documentation | Work performed is separate from warrant for a claim; freshness is visible | Execution/claim separation, hash invalidation and stale-evidence tests |
| [AERS](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | `eval-harness/README.md`; `agents/README.md` | Distinguish machine checks from unresolved judgment; route narrowly rather than load a catalog | Fault-injection checks with observable outcomes; focused initial skills and progressive references |

The source collections' mandatory interviews, repeated approval stages, numerical quality scores, provider-specific hooks and full review fleets are not imported. These would change ordinary tasks without a demonstrated need. Their self-reported capabilities were not independently benchmarked here.

The local AERS evaluator was actually run with Python 3.12 using `--selftest --no-write`: its nine fixture pairs passed the discrimination test; all 42 scenarios validated (196 automatic rubric items, 21 manual). This validates that snapshot's fixture discrimination, not our agents' behavior. Our coordination checks instead inject missing artifacts, stale revisions, duplicate dispatch, permanent/transient failures and conflicting completion conditions.

No full workflow engine is installed in this environment. The adapter reuses available standard-library DAG, persistence, process and hashing primitives, adding only task/evidence/handoff semantics. Projects already using a mature workflow engine retain it. The adapter's small retry policy is classified and bounded; it does not implement distributed orchestration, backfills, remote queues or provider transport.

## Native host integration

Further source inspection covered LongTable's implemented `PanelPlan`/`PanelMemberResult` types (`packages/longtable-core/src/types.ts:151`), native-subagent plan and planned-member state (`packages/longtable/src/panel.ts:517,618`), and generated provider handoff (`packages/longtable-provider-codex/src/skills.ts:379`). These establish reusable plan/return contracts; they do not call this host's `collaboration.spawn_agent`. Its `native_workers` launcher uses tmux and separate `codex exec` processes (`panel-runtime.ts:169,457`) and is not used here. Its default aggregate completion (`project-session.ts:1798`) and missing-member handling are strengthened: every required task needs its own actual host handle, strict terminal return and artifact/check validation.

[Paper-WorkFlow](https://github.com/brycewang-stanford/Paper-WorkFlow) contributed targeted source reads, disk artifacts and short return guidance (`references/subagent-templates.md:3,355`), plus handoffs that are pointers rather than proof (`references/orchestration-and-handoff.md:57`). Pedro's fresh-context dispatch and explicit missing-return handling remain applicable. The local [Data-Wise workflow](https://github.com/Data-Wise/claude-plugins) selector was inspected but not adopted as transport: `workflow/workflow/agent_delegation.py` chooses keyword-based agent names; it does not launch or join agents, and its capped set ordering is unstable.

The native bridge adapts these contracts to the host's advertised tools without copying third-party code or introducing another model provider. SQLite durable requests and SAVEPOINT transactions reuse mature primitives. An active host orchestrator forwards generated calls; a Python CLI does not independently possess native tool authority. Context measurements cover emitted handoffs and helper-mediated reads, not hidden provider context or actual model token usage. Deterministic checks and the real repository/report run are separate evidence layers.
