# Capabilities and coordination

Start with [general orchestration](orchestration/README.md) for task routing, project management, writing, evidence and recovery. Focused entrypoints load only the current capability. The [research composition guide](skill-composition.md) selects empirical methods and connects samples, inference and presentation when the task needs them.

| Directory | Contents |
|---|---|
| `paradigms/` | Recommendations, code observations and paper practices for 20 methods |
| `orchestration/` | General contracts, routing, context dispatch, recovery and inspected reuse patterns |
| `runtime/` | Optional provider-neutral local DAG/checkpoint/evidence adapter; Python standard library |
| `skills/` | Focused general-task and research guides; conditional detail and recorded practice in references |
| `agents/` | Bounded responsibility roles; Codex TOML configurations generated in `agents/codex/` |
| `workflows/` | General execution, project management, writing and specialized research workflows |
| `examples/general/` | Runnable project-management, operational-reporting and document-editing demonstrations |
| `examples/native-project/` | Real repository status, delivery plan, report and briefing through native host dispatch; actual agent returns are required |
| `examples/war-discourse/` | Independently written real-data replication runner, numeric checks and publication comparisons; local third-party inputs are not bundled |
| `presets/` | Reusable task prompts for general work and empirical analysis |
| `checks/` | Fault-injection coordination checks, progressive-loading and shared-role consistency checks |
| `maintenance/` | Shared role/configuration synchronization |

Each method skill has a `SKILL.md` entry point and a `code-examples.md` file with commands, input variables and interpretation guidance.

| Area | Skills |
|---|---|
| General coordination | [Orchestration](skills/task-orchestration/SKILL.md), [evidence tracking](skills/evidence-tracking/SKILL.md), [failure recovery](skills/failure-recovery/SKILL.md) |
| Project management | [Planning](skills/project-planning/SKILL.md), [status and handoff](skills/project-status/SKILL.md) |
| General writing | [Reports](skills/report-writing/SKILL.md), [briefings](skills/briefing-writing/SKILL.md), [editing](skills/document-editing/SKILL.md) |
| Causal designs | [DID](skills/did/SKILL.md), [RDD](skills/rdd/SKILL.md), [IV](skills/iv/SKILL.md), [RCT](skills/rct/SKILL.md), [matching](skills/matching/SKILL.md), [synthetic control](skills/synthetic-control/SKILL.md), [difference-in-discontinuities](skills/diff-in-disc/SKILL.md), [bunching](skills/bunching/SKILL.md), [shift-share](skills/shift-share/SKILL.md) |
| Regression and estimation | [Regression](skills/regression/SKILL.md), [panel fixed effects](skills/panel-fe/SKILL.md), [GMM](skills/gmm/SKILL.md), [structural estimation](skills/structural-estimation/SKILL.md), [ML nuisance estimation](skills/ml-nuisance/SKILL.md) |
| Empirical finance | [Fama–MacBeth](skills/fama-macbeth/SKILL.md), [portfolio sorts](skills/portfolio-sorts/SKILL.md), [return event studies](skills/return-event-study/SKILL.md), [predictive regression](skills/predictive-regression/SKILL.md) |
| Other methods | [Panel event studies](skills/event-study/SKILL.md), [ML prediction](skills/ml-prediction/SKILL.md) |
| Shared research tasks | [Sample checks](skills/panel-data-checks/SKILL.md), [inference and clustering](skills/inference-clustering/SKILL.md), [tables and figures](skills/tables-figures/SKILL.md), [academic writing](skills/academic-writing/SKILL.md), [literature verification](skills/literature-verification/SKILL.md), [code audit](skills/code-audit/SKILL.md), [code annotation](skills/code-annotation/SKILL.md), [research explanation](skills/research-explanation/SKILL.md), [project bookkeeping](skills/project-bookkeeping/SKILL.md) |

Panel event studies describe dynamic treatment responses. Return event studies describe abnormal asset returns and CAR/BHAR. ML nuisance estimation supports a causal estimand, whereas ML prediction evaluates forecasts on held-out observations.

For methodological advice, read `paradigms/<method>/recommendations.md`. For recorded practice, read the corresponding `observed.md` and `reported.md`. These layers have different evidentiary roles. Existing draft labels and historical evaluation references do not make a review or rebuilding step a prerequisite for use.

Use checklists and templates when they help. An [R template for RD](skills/rdd/templates/rd_analysis.R) is available. [Paper-practice notes](skills/paper-practice-notes/SKILL.md) and [code-card extraction](skills/recipe-card-extraction/SKILL.md) support a requested new reading of a paper or its code.

Maintain skills and Markdown roles here. The root skill directories and Claude Code role directory link to these files. Codex project settings refer to `agents/codex/`; keep each TOML configuration consistent with its Markdown role. Shared repository guidance is in [AGENTS.md](../AGENTS.md).
