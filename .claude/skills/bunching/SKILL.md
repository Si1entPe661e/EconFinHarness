---
name: bunching
description: Bunching at kinks or notches using binned densities, counterfactual fitting, excess/missing mass and assumption-dependent elasticity interpretation. Use for distributional responses, not an RD outcome jump.
kind: method
---

# Bunching

## When to use

Use for excess mass near a kink/notch or salient threshold in a distribution. Bunching as manipulation or reporting behavior differs from a structural elasticity estimate.

## Inputs

Running quantity, policy threshold and budget schedule, observation/cluster units, bin width, fit range, excluded response region, rounding/heaping information, possible comparison distributions and target mass/elasticity.

## Procedure

1. Distinguish a kink from a notch and describe the behavior the schedule can induce. State smoothness or comparison-distribution assumptions for the counterfactual.
2. Plot counts/density at useful bin widths, inspect rounding at other thresholds and distinguish data heaping from policy-induced excess mass.
3. Fit the counterfactual outside the response region, with an explicit polynomial order and round-number controls when justified. Explain normalization or mass-conservation adjustments; never fit away the response region.
4. Report excess mass and its normalization. For notches inspect the missing mass/dominated region and how the upper exclusion boundary is chosen. Negative counterfactual counts or unstable fits need attention.
5. Refit the entire construction in resampling, including fitted density and any selected boundary. Resample independent observation or dependence units as appropriate; a residual-bin bootstrap and a cluster bootstrap target different uncertainty.
6. Vary bin widths, fit order, fit range and excluded region, and examine placebo thresholds/comparison groups. Do not select the window by the largest excess mass.
7. Map mass to an elasticity only under an explicit model of the schedule, heterogeneity and optimization frictions. The histogram alone does not identify a structural elasticity.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives an actual bunchit call and parameter sensitivity. Return the histogram/counterfactual, excluded region, excess/missing mass and any conditional elasticity interpretation.
