---
name: diff-in-disc
description: Difference-in-discontinuities at a fixed running-variable cutoff across periods or groups. Estimate changes in local jumps, state stability of other cutoff effects, and jointly infer sharp or fuzzy contrasts.
kind: method
---

# Difference-in-discontinuities

## When to use

Use when a policy changes the outcome discontinuity at a fixed cutoff between periods or groups, and an existing cutoff effect can be removed by a credible second contrast. A simple time before/after design is not sufficient.

## Inputs

Outcome, running variable and cutoff, before/after or group indicator, policy eligibility/receipt, independent assignment units, local support in every cutoff-by-period cell and other rules sharing the cutoff.

## Procedure

1. Define the four local cells and estimand: post-period jump minus pre-period jump. Explain why other cutoff effects would remain stable absent the policy and why treatment effects/interactions do not invalidate that subtraction.
2. Inspect running-variable measurement, sorting, support and composition in every period. Treatment may induce movement across the cutoff; using post-treatment running values can alter identification.
3. Estimate pre/post jumps and their difference using side- and period-specific local slopes. Use a justified common window or a selector for the actual contrast; ordinary sharp-RD bandwidth optimization does not automatically optimize the difference.
4. Infer the contrast jointly. Repeated units induce covariance across periods; do not subtract two SE or assume their estimates independent. A local weighted regression gives model-based local inference and is not automatically RD robust bias correction.
5. For fuzzy designs, require a nonzero change in the treatment jump and explicit exclusion/monotonicity assumptions for the ratio of outcome-jump change to treatment-jump change. A ratio is not automatically a familiar LATE when an old treatment also changes. Use joint or weak-first-stage-aware inference.
6. Check bandwidths, side-specific slopes, covariate continuity, placebo periods/cutoffs and changes in other cutoff policies. Interpret results locally for the contrast's population.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives joint local linear estimates in R/Stata and reports both jumps and the difference. Use rdd for the underlying support and density checks.

Return the four-cell sample sizes, individual jumps, contrast, uncertainty and the stability assumptions.
