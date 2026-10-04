# Empirical research methods

Start with the [composition guide](skill-composition.md) to select a method and connect sample checks, inference, presentation and writing. Use the [analysis workflow](workflows/empirical-analysis.md) for implementation and the [presentation workflow](workflows/present-results.md) for tables and figures.

| Directory | Contents |
|---|---|
| `paradigms/` | Recommendations, code observations and paper practices for 20 methods |
| `skills/` | 31 operational guides: 20 methods, nine shared research skills and two reading skills |
| `agents/` | Nine Markdown roles, including paper and code reading; Codex TOML configurations in `agents/codex/` |
| `workflows/` | 11 optional task workflows |
| `presets/` | 12 reusable task prompts |

Each method skill has a `SKILL.md` entry point and a `code-examples.md` file with commands, input variables and interpretation guidance.

| Area | Skills |
|---|---|
| Causal designs | [DID](skills/did/SKILL.md), [RDD](skills/rdd/SKILL.md), [IV](skills/iv/SKILL.md), [RCT](skills/rct/SKILL.md), [matching](skills/matching/SKILL.md), [synthetic control](skills/synthetic-control/SKILL.md), [difference-in-discontinuities](skills/diff-in-disc/SKILL.md), [bunching](skills/bunching/SKILL.md), [shift-share](skills/shift-share/SKILL.md) |
| Regression and estimation | [Regression](skills/regression/SKILL.md), [panel fixed effects](skills/panel-fe/SKILL.md), [GMM](skills/gmm/SKILL.md), [structural estimation](skills/structural-estimation/SKILL.md), [ML nuisance estimation](skills/ml-nuisance/SKILL.md) |
| Empirical finance | [Fama–MacBeth](skills/fama-macbeth/SKILL.md), [portfolio sorts](skills/portfolio-sorts/SKILL.md), [return event studies](skills/return-event-study/SKILL.md), [predictive regression](skills/predictive-regression/SKILL.md) |
| Other methods | [Panel event studies](skills/event-study/SKILL.md), [ML prediction](skills/ml-prediction/SKILL.md) |
| Shared research tasks | [Sample checks](skills/panel-data-checks/SKILL.md), [inference and clustering](skills/inference-clustering/SKILL.md), [tables and figures](skills/tables-figures/SKILL.md), [academic writing](skills/academic-writing/SKILL.md), [literature verification](skills/literature-verification/SKILL.md), [code audit](skills/code-audit/SKILL.md), [code annotation](skills/code-annotation/SKILL.md), [research explanation](skills/research-explanation/SKILL.md), [project bookkeeping](skills/project-bookkeeping/SKILL.md) |

Panel event studies describe dynamic treatment responses. Return event studies describe abnormal asset returns and CAR/BHAR. ML nuisance estimation supports a causal estimand, whereas ML prediction evaluates forecasts on held-out observations.

For methodological advice, read `paradigms/<method>/recommendations.md`. For recorded practice, read the corresponding `observed.md` and `reported.md`. These layers have different evidentiary roles. Existing draft labels and historical evaluation references do not make a review or rebuilding step a prerequisite for use.

Use checklists and templates when they help. An [R template for RD](skills/rdd/templates/rd_analysis.R) is available. [Paper-practice notes](skills/paper-practice-notes/SKILL.md) and [code-card extraction](skills/recipe-card-extraction/SKILL.md) support a requested new reading of a paper or its code.

Maintain skills and Markdown roles here. The root skill directories and Claude Code role directory link to these files. Codex project settings refer to `agents/codex/`; keep each TOML configuration consistent with its Markdown role. Shared repository guidance is in [AGENTS.md](../AGENTS.md).
