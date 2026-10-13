---
name: rdd
description: "Regression discontinuity designs (sharp, fuzzy; sharp kink slope change as a narrow branch) for design, implementation, audit and explanation. Use when treatment changes at a threshold of an observed running variable. Do not use for difference-in-discontinuities or bunching estimands without the extra design assumptions, or when the running variable is chosen after treatment."
version: 0.2.1
kind: method
status: validated
---

# Regression discontinuity

## When to use

Use when treatment or eligibility changes at a predetermined cutoff of a running variable. Sharp RD targets the outcome jump at the cutoff; fuzzy RD targets the local Wald effect for compliers under continuity, exclusion and monotonicity. A policy kink needs a slope-based estimand. Use diff-in-disc for changes in discontinuities across periods and bunching for excess mass in a distribution.

## Inputs

Outcome, running variable, cutoff and assignment direction; treatment received for fuzzy RD; predetermined covariates, cluster identifier, weights if needed, and whether the running variable has discrete support or several cutoffs.

## Procedure

1. Define eligibility from the actual rule, including equality at the cutoff. Centre the running variable. Examine support, observations, distinct values and treatment rates on both sides.
2. Discuss continuity of untreated potential outcomes, sorting and other policies changing at the cutoff. A density rejection is a warning, not proof of manipulation; non-rejection is not proof of continuity.
3. Plot binned outcomes and treatment rates, and inspect heaping, gaps and cutoff mass. Test density and predetermined covariate continuity where the running-variable support makes those procedures appropriate.
4. Estimate a local linear RD with triangular kernel and a stated bandwidth rule. Report the conventional estimate together with bias-corrected robust inference, selected estimation/bias bandwidths and effective sample sizes. A global high-order polynomial is not a replacement.
5. For fuzzy RD, estimate the treatment jump on the same observations and bandwidth. The sign follows the coding of assignment and treatment; negative compliance orientation is not automatically invalid. Weak local first stages need weak-identification-aware inference.
6. Choose heteroskedastic or clustered inference from dependence and assignment. Count clusters inside the bandwidth. Discrete support needs support-aware inference; clustering by running-variable values alone does not solve approximation bias.
7. Vary bandwidths, polynomial order, predetermined covariate adjustment and justified donut exclusions. A donut changes the local sample and may require extrapolation to the cutoff. Explain sample or estimand changes.
8. Keep the conclusion local to the cutoff. Pool multiple cutoffs only with an explicit weighting and comparability argument; do not interpret a pooled jump as an unrestricted population ATE.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Software commands

[code-examples.md](code-examples.md) contains sharp/fuzzy rdrobust, rddensity, plotting and bandwidth sensitivity in R, plus Stata calls.

The existing [R template](templates/rd_analysis.R) is available when useful. Its support-count gates are local conventions, not universal thresholds; its positive-first-stage check requires treatment coding to match that orientation. Its kink branch estimates an outcome slope change only. A kink effect additionally requires the policy or treatment slope change and corresponding inference.

## Outputs and missing information

Return the estimate and interval, bandwidths, kernel/order, cutoff, effective observations on each side, first-stage jump if fuzzy, and RD plots. If support or compliance is insufficient, explain the limitation without treating a software output as a credible causal estimate.

Use [checklist.md](checklist.md) as needed.

## Research records

Read [research records](references/research-records.md) only when recorded practice or corpus evidence is relevant. These records are distinct from methodological recommendations.
