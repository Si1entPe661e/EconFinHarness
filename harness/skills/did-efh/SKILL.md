---
name: did-efh
description: Difference-in-differences and event-study designs (two-period, staggered adoption, triple difference, synthetic DID) for design, implementation, audit and explanation. Use when treatment turns on for some units at known times and untreated or not-yet-treated units serve as comparison. Do not use for designs without a pre-period or when treatment timing is chosen in response to outcomes.
metadata:
  version: 0.1.0
  kind: method
  status: draft
---

# did

Method skill for difference-in-differences (DID) and event studies. It covers the two-period case, staggered adoption with heterogeneity-robust estimators, triple differences, synthetic DID as a related branch, and the inference and pre-trend diagnostics that go with them. Observed corpus practice (`harness/paradigms/did/observed.md`, 24 cards; `harness/paradigms/event_study/observed.md`, 10 cards) is kept separate from recommendations (`harness/paradigms/did/recommendations.md`, draft).

## When to use

- Some units become treated at known dates; others are never treated or treated later; outcomes are observed before and after.
- Event-study versions: effects by time relative to treatment, with leads as pre-trend evidence.
- Staggered adoption: treatment dates differ across cohorts; the choice of estimator (two-way fixed effects versus heterogeneity-robust estimators) is a design decision to record.
- Roles: empirical-analyst (estimand, comparison group, estimator choice, inference plan), code-engineer (implementation), reviewer (audit), explainer.

## When not to use

- No pre-treatment periods, or treatment timing responds to the outcome path (anticipation or endogenous timing without a design argument).
- The comparison group is defined by a discontinuity (use `rdd-efh` or difference-in-discontinuities) or by an instrument (use `iv-efh`).
- Single treated unit with many controls and long pre-periods: synthetic control is the closer branch; synthetic DID is covered here only as a related estimator.

## Inputs required

- Panel or repeated cross-section description: unit, time, treatment timing per unit, never-treated and not-yet-treated groups, balance of the panel.
- Target estimand: ATT overall, by cohort, by relative time; the comparison group used to identify it.
- Cluster structure (assignment level), weights, covariates and their timing.
- For audit: relevant code, available environment details, analysis choices and outputs.

## Procedure

1. Define the target ATT, treatment timing, reference period and untreated comparison. Check panel keys, reversals, anticipation and support at each event time.
2. Distinguish one-date treatment from staggered adoption. With heterogeneous staggered effects, choose a compatible estimator or justify TWFE; do not infer a design from a regression command.
3. Keep estimator-specific cohorts, weights, aggregation and sample restrictions explicit. Choose clustering from assignment/dependence separately from fixed effects.
4. Inspect pre-trends and sensitivity with their limits; an insignificant lead test does not establish parallel trends. Keep actual N, clusters and identifying comparisons with the estimates.
5. Export the same estimand, sample and uncertainty in tables, dynamic figures and prose. Revisit only affected steps after changes.

Read [design and estimation details](references/design-and-estimation.md) for the applicable estimator branch, diagnostics and missing-information rules. Use [code-examples.md](code-examples.md) only for the selected language and command; avoid loading every estimator's examples.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks-efh, inference-clustering-efh and tables-figures-efh steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Research records

Recorded practice is in `harness/paradigms/did/` and `harness/paradigms/event_study/`: code observations in `observed.md` and paper statements in `reported.md`, kept apart from the recommendations in `recommendations.md`.
