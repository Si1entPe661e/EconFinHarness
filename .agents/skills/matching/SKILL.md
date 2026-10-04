---
name: matching
description: Matching and propensity-score designs for ATT/ATE under conditional exchangeability and overlap. Build matches using pretreatment variables, inspect balance and retained populations, and choose estimator-appropriate inference.
kind: method
---

# Matching

## When to use

Use to construct comparable treated/control samples under conditional exchangeability, consistency and overlap. Matching alone does not remove unobserved confounding. Matching combined with DID still needs parallel trends for the matched population.

## Inputs

Binary treatment, outcomes and measurement dates, pretreatment covariates, eligible control pool, target ATT/ATE, exact-match strata if any, repeated observations/assignment groups and matching distance.

## Procedure

1. Define the target population and treatment timing. Select covariates using substantive confounding knowledge; avoid outcomes, mediators, colliders and variables observed only after treatment.
2. Inspect overlap and decide what populations can be compared. Fit the propensity score or a covariate distance on the eligible sample; a well-predicted treatment indicator is not the goal.
3. Choose nearest-neighbor/full/exact matching, replacement, ratio and caliper before examining effects. Distinguish calipers on probabilities from those on logit scores and specify whether they are standardized.
4. Compare standardized mean differences, distributional balance and overlap before/after matching using the actual matching weights. Do not use balance p-values as the sole criterion.
5. Report unmatched treated units, reused controls and effective sample size. Trimming changes the target; name the retained population instead of claiming the original ATT/ATE automatically.
6. Estimate the outcome contrast with matching weights and justified adjustment. Account for reuse, subclasses and assignment dependence. Ordinary regression SE after matching are not automatically valid.
7. For fixed-neighbor matching, the ordinary nonparametric bootstrap can be inconsistent. Use estimator-specific analytical variance or a justified alternative. For DID/event studies, carry matched weights and the additional identifying assumptions into that estimator.
8. Check sensitivity to distance, caliper, overlap and unmeasured confounding without selecting the specification by outcome significance.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) includes MatchIt sample construction and Stata matching estimation. Return balance, overlap, retained counts/weights and the treatment contrast with its inference assumptions.
