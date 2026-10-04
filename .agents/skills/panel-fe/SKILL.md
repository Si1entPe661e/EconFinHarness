---
name: panel-fe
description: Panel fixed-effects estimation using within-unit variation with one-way or multiple absorbed effects. Check timing, identifying variation, strict exogeneity, dynamic bias, singleton losses and clustered inference.
kind: method
---

# Panel fixed effects

## When to use

Use for repeated-unit models removing additive time-invariant heterogeneity and other specified FE. Treatment staggered across cohorts needs did, rather than treating generic TWFE as an automatically valid treatment estimator.

## Inputs

Unit-time key, outcome and regressors, measurement/timing definitions, FE dimensions, weights, dependence groups, intended within-unit parameter and time length.

## Procedure

1. Verify keys, dates, gaps and sample using panel-data-checks. Define the actual unit; changing identifiers over time can destroy the panel.
2. State the within-unit identifying variation and exogeneity assumptions. Unit FE remove additive fixed confounding, not time-varying confounding, reverse causality or feedback automatically.
3. Inspect variation after the planned FE. Unit-invariant regressors are absorbed; time-common variables are absorbed by full time FE. Redundant FE and highly sparse cells can change usable N.
4. Estimate the specified one-/two-/multi-way model. Inspect collinear terms and recursively dropped singleton groups; compare alternative models on consistent samples when appropriate.
5. Cluster for serial dependence and any additional assignment/common-shock dimensions. State group counts; time FE do not automatically eliminate within-period residual dependence.
6. With lagged dependent variables and short T, discuss dynamic FE bias and choose a justified alternative. A generic FE call or extra lags do not solve it; use gmm only with defensible moment assumptions.
7. Interpret the coefficient for units/periods providing within variation. Check heterogeneous slopes, unbalanced-panel selection and trends where relevant.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives fixest, reghdfe/xtreg and PanelOLS calls, including unit-by-time FE. Return within-effect estimates/intervals, FE, fitted N and covariance; avoid interpreting overall R-squared as within fit.
