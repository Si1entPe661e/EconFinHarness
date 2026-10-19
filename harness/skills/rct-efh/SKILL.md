---
name: rct-efh
description: Randomized experiments for assignment-aware ITT, ANCOVA, noncompliance, attrition, multiple outcomes and randomization inference. Use when treatment assignment is randomized; distinguish assignment from receipt.
metadata:
  kind: method
---

# Randomized experiments

## When to use

Use for individually or cluster-randomized experiments, blocked or paired assignment, encouragement designs and multi-arm trials. Quasi-random observational assignment needs a separate identification argument.

## Inputs

Assignment mechanism, randomization unit and blocks, treatment probabilities, assigned arm, actual receipt, outcomes and baseline measurements, follow-up/attrition information, weights and intended estimand.

## Procedure

1. Reconstruct eligible units and assigned arms from randomization information. Distinguish assignment, receipt and exposure; preserve the assigned arm for the ITT sample.
2. State ITT as the primary assignment effect. For treatment-on-the-treated/LATE, use assignment as an instrument only with exclusion, monotonicity and relevance; do not compare treatment receivers directly with nonreceivers.
3. Inspect baseline balance and differential attrition. Chance imbalance does not justify outcome-driven covariate selection. Do not condition on post-assignment survival, compliance or mediators without a separate estimand and assumptions.
4. Estimate arm contrasts, including randomization blocks and prespecified baseline outcome adjustment when appropriate. With unequal assignment probabilities, choose a design-consistent weighting/estimator and state its target population. Rebuild strata controls from the randomization description, one indicator per stratum level, and never pool a level with missing or don't-know. A missing baseline covariate should not remove a unit: unless the plan says otherwise, fill a constant and add an indicator for that covariate, and report an indicator that is nonzero on only one or two fitted rows. See [covariates](covariates.md) and [recommendations](../../paradigms/rct/recommendations.md) r1-r2.
5. Match inference to the randomization unit, stratification and sampling. Cluster at the assignment group when appropriate; few groups require a suitable procedure. Randomization inference must reproduce blocks, pairs, counts and any allocation restrictions.
6. Define primary outcomes and families; adjust or clearly distinguish exploratory multiple comparisons. For heterogeneous effects, test interactions rather than comparing significance across subgroups. For heterogeneity by a baseline group, extend the main equation minimally: group main effects and group-by-assignment terms with the main controls unchanged. Further interactions are labelled variants; state how units without a group value are handled and the resulting N.
7. Address attrition with sensitivity, bounds or weighting under stated assumptions. Repeated outcomes need the intended time contrast and within-unit dependence; interference or spillovers require explicit exposure definitions.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks-efh, inference-clustering-efh and tables-figures-efh steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives blocked ANCOVA, compliance IV and arm contrasts in R/Stata. Use inference-clustering-efh for blocked cluster permutations.

Return arm counts, receipt/attrition rates, ITT contrasts with intervals, any first-stage/complier result, and the randomization/inference assumptions.

## Corpus examples

Related commands as written in published replication packages, with paper shares: [Stata](examples/stata.md), [R](examples/r.md).
