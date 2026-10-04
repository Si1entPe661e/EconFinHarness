---
name: ml-nuisance
description: Machine learning for nuisance functions in causal estimation, including orthogonal scores, cross-fitting and partially linear or AIPW estimands. Distinguish causal identification and valid inference from predictive fit.
kind: method
---

# Machine learning for nuisance functions

## When to use

Use when flexible outcome, propensity or treatment models support an identified causal parameter through an orthogonal score. Use ml-prediction for forecasting alone. Double selection, cross-fitted DML and causal forests are distinct procedures.

## Inputs

Outcome, treatment, pretreatment confounders, target PLR coefficient/ATE/ATT, identification assumptions, independent groups, fold rules, nuisance learners and overlap information.

## Procedure

1. Establish identification first: conditional exchangeability/overlap for selection-on-observables, valid instruments for IV-DML, or the chosen design's assumptions. Flexible fitting does not solve hidden confounding.
2. Choose the score for the estimand. PLR residual-on-residual estimates a partial-linear coefficient; with heterogeneous effects it is not generally the ATE. Binary-treatment AIPW uses separate arm outcome regressions and a propensity score.
3. Split independent units into folds; keep repeated observations or dependence groups together. Time dependence may need a different splitting/inference theory. Fit preprocessing, tuning and nuisances using training folds only.
4. Generate out-of-fold predictions for every evaluation observation. Never residualize with a full-sample model and call it cross-fitting. Nested tuning must stay inside training folds.
5. Compute the orthogonal score and solve the target moment. Inspect residual treatment variation, propensity tails, arm-specific fit and extreme score values. Trimming/clipping affects the estimator and potentially its target.
6. Infer using the influence/score structure and design-appropriate dependence. Orthogonality and cross-fitting still require nuisance-rate and regularity conditions; predictive validation alone does not prove valid causal inference.
7. Examine reasonable learners and repeated splits, and report coefficient stability without selecting seeds by significance. Causal-forest heterogeneity needs honest estimation and its own uncertainty treatment.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) implements grouped cross-fitting with random forests and a PLR estimate. Return the estimand, fold unit, nuisance diagnostics, estimate/interval and identification assumptions.
