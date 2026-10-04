---
name: synthetic-control
description: Classical synthetic control for a treated aggregate unit with a credible donor pool and pretreatment fit. Choose donor weights, inspect fit and placebo comparisons; distinguish SCM from synthetic DID.
kind: method
---

# Synthetic control

## When to use

Use for a treated unit or a small set of treated aggregates with a sufficiently long pretreatment panel and untreated donors. Classical SCM, augmented SCM and synthetic DID are different estimators; choose deliberately.

## Inputs

Unit-time outcomes, intervention date, treated unit(s), candidate donors, pretreatment predictors, outcome scale, fit/validation periods and plausible contamination or anticipation dates.

## Procedure

1. Define the treated unit and intervention window. Exclude donors affected by the intervention, spillovers or overlapping policies using substantive information.
2. Build a aligned panel with comparable outcomes, consistent units and documented missingness. Interpolation or outcome rescaling changes the fit and must be justified.
3. Fit donor weights from pretreatment data only. For classical SCM inspect nonnegative weights summing to one, concentration and whether the treated trajectory lies within a useful donor span.
4. Inspect pre-fit trajectories, gaps and RMSPE; reserve a pretreatment validation segment when choosing predictors or tuning parameters. Good in-sample fit is not itself identification.
5. Plot the post-treatment gap and report the intended period average/cumulative effect. Separate announcement, implementation and anticipation periods.
6. Use donor-placebo or time-placebo comparisons under stated comparability assumptions; show how poor-fit placebos are handled and the attainable p-value resolution. Donor placebos are not automatically an exact randomized test.
7. Examine leave-one-donor-out results, donor-pool and predictor sensitivity. With multiple treated units, state aggregation weights and appropriate inference rather than treating them as independent replications.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives classical SCM with sc_estimate, donor weights, pre-fit and leave-one-out sensitivity. Use did for synthetic DID.

Return treated/synthetic paths, gaps, donor weights, pre-fit, sensitivity and a cautious interpretation conditional on donor comparability.
