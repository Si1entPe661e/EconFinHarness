---
name: fama-macbeth
description: Fama-MacBeth repeated cross-sectional regressions and time-series inference on average slopes. Distinguish characteristic regressions from estimated-beta risk-premium tests and account for timing, generated regressors and serial dependence.
kind: method
---

# Fama–MacBeth regressions

## When to use

Use to average coefficients from repeated cross-sectional regressions, often of future asset returns on known characteristics or estimated exposures. Pooled panel OLS with clustered SE is a different estimator.

## Inputs

Asset/date keys, forward or contemporaneous return definition, observable-at-formation characteristics or estimated betas, cross-sectional controls, weighting/normalization rules, sample filters and time-series covariance plan.

## Procedure

1. Define the cross-sectional relationship and timing. Characteristics measured at t must be known when predicting t+1; accounting publication delays and delisting returns matter.
2. For characteristic regressions, interpret slopes as average conditional associations/predictive relations. For risk-premium tests, estimate betas in a stated first stage and discuss their error, exposure stability and pricing-model assumptions.
3. Run each date's cross-section with identical definitions, an intercept where appropriate and enough independent observations/rank. Report skipped dates and changing coverage rather than silently averaging a selected set.
4. Average date-level slopes using the intended time weights. Ordinary equal-date averaging differs from weighting dates by cross-sectional N.
5. Infer from the coefficient time series. Use HAC for persistent or overlapping coefficients and state bandwidth/kernel. The number of periods, not the stacked asset N, drives this inference.
6. Generated betas may require a Shanken-style correction under its specific assumptions or a suitable full-procedure bootstrap; it is not universally appropriate for characteristic regressions.
7. Examine scaling, within-date winsorization, industry controls, sample composition, alternative horizons and weighting. Multiple signals/models require a multiple-testing or exploratory interpretation.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives Python FamaMacBeth, Stata xtfmb and an R implementation retaining date-level slopes. Return average slopes, intervals/t-statistics, dates used, sample coverage and timing/normalization rules.
