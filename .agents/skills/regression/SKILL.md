---
name: regression
description: Regression modeling for OLS, weighted least squares, binary outcomes and count outcomes. Define the conditional relationship, functional form, sample and inference; causal interpretation requires a separate design.
kind: method
---

# Regression

## When to use

Use for conditional associations, baseline outcome models and a regression implementing an already specified design. The estimator alone does not identify a causal effect. Use panel-fe, iv, did or rdd for their additional assumptions.

## Inputs

Outcome scale and support, regressors and measurement dates, controls, interactions, sample, weights, FE if any, dependence groups and the target conditional quantity.

## Procedure

1. Define the outcome and parameter. Distinguish linear mean effects, log effects, odds ratios and nonlinear marginal effects; a binary indicator in logit is not a percentage-point coefficient.
2. Specify transformations and controls using the research question. Handle zeros/missing values explicitly; avoid post-treatment controls for total causal effects.
3. Inspect sample losses, collinearity, leverage and overlap. Compare models on a common sample where that is the intended comparison.
4. Estimate OLS/WLS for a linear mean, or a justified nonlinear model for binary/count outcomes. Poisson pseudo-ML can model nonnegative outcomes with zeros; it does not require Poisson variance for consistent mean estimation under the appropriate mean specification.
5. Interpret interactions through contrasts/marginal effects and uncertainty. Centre continuous covariates when useful; do not infer heterogeneous effects from separate significance tests.
6. Match covariance to dependence. Weights have a stated purpose; precision weighting is not automatically survey inference. Examine heteroskedasticity, functional form and influential observations.
7. Report coefficients or relevant predicted contrasts, intervals, N, units and model assumptions. Robust SE do not cure omitted confounding or incorrect functional form.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands

[code-examples.md](code-examples.md) contains OLS, WLS, PPML, logit and marginal effects in R/Stata/Python.
