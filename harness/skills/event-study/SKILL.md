---
name: event-study
description: Panel event studies of dynamic treatment responses with explicit event time, reference period, comparison units and cohort aggregation. Use did for identification; use return-event-study for abnormal asset returns.
kind: method
---

# Panel event studies

## When to use

Use to estimate/plot responses before and after an event in panel outcomes. This skill focuses on event-time construction and dynamic coefficients; use did for adoption-based identification and estimator choice. Recurrent events or continuous shocks need a separate design rather than automatically applying adoption estimators.

## Inputs

Unit-calendar keys, event/adoption date, never-treated definition, outcome and predetermined controls, comparison group, event window, reference period, anticipation allowance and dependence units.

## Procedure

1. Define event time from the actual calendar and assignment date. Keep never-treated units in the estimator's supported coding; setting their outcome/event observations missing can silently remove controls.
2. State the dynamic estimand and comparison group. Adoption designs need parallel trends and no anticipation for the relevant untreated comparisons; common calendar shocks require time controls.
3. Choose an estimator compatible with staggered timing and heterogeneous effects. Generic TWFE lead/lag coefficients may combine contaminated comparisons; use cohort-aware estimation where appropriate.
4. Define the omitted period, supported event window and tail handling. Binning tails imposes restrictions; dropping unsupported periods changes the comparison/sample. Plot cohort/calendar support alongside dynamics when composition changes.
5. Use design-appropriate clustering and choose pointwise intervals versus a simultaneous band. Joint lead tests are diagnostics, not proof of parallel trends; selecting a sample after a successful pretest can distort inference.
6. Explain aggregation over cohorts and time, including changing weights. A long-lag coefficient based only on early cohorts is not automatically comparable with a short-lag coefficient using all cohorts.
7. Check anticipation dates, alternative comparison groups/windows and sensitivity to departures from parallel trends. For repeatable events, address overlapping event windows, prior exposure and the target episode population explicitly.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives Sun–Abraham in R and cohort-aware Stata eventstudyinteract. The did command collection includes imputation, group-time ATT and HonestDiD alternatives.

Return event-time coefficients/intervals, reference/comparison definitions, support and aggregation/inference assumptions.
