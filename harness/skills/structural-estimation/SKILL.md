---
name: structural-estimation
description: Structural economic estimation through likelihood or simulated moments. Specify the model, identifying variation, solution and simulation before optimization; check fit and counterfactual assumptions.
kind: method
---

# Structural estimation

## When to use

Use when parameters belong to an explicit behavioral/equilibrium model and estimates support model-based counterfactuals. A numerical optimizer without a specified model and data mapping is not a structural estimator.

## Inputs

Economic primitives, parameter normalization/bounds, observables and measurement process, likelihood or moment function, identifying variation, numerical solution/simulator, random draws, initial values, weights and dependence units.

## Procedure

1. State the model, target parameters and variation identifying each parameter. Separate calibrated and estimated quantities; utility scale and location normalizations affect interpretation.
2. Map data to choices, states, prices and moments. Explain missingness, selection and measurement error; endogenous prices or choices need valid instruments, control functions or a correctly specified joint likelihood.
3. Solve the model and test economic feasibility before optimization. For simulation, use common random numbers across parameter evaluations and enough draws to control simulation noise.
4. Build the likelihood/SMM objective and specify weights. Rescale parameters/moments, use multiple starts and inspect local solutions, constraints and convergence; confirm tighter numerical tolerances do not materially change estimates.
5. Compute uncertainty appropriate to likelihood correctness, dependence, simulation, calibration and preliminary stages. An inverse optimizer Hessian alone does not handle arbitrary clustering or uncertainty in generated inputs.
6. Show in-sample and held-out moment/choice fit, parameter sensitivity and identification profiles where useful. A precise parameter can reflect restrictive assumptions rather than rich variation.
7. For counterfactuals, restate which primitives remain invariant, solve equilibrium again and distinguish parameter uncertainty from model uncertainty. Explain extrapolation beyond observed support.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) supplies a fully defined static-choice likelihood in R and an actual MATLAB simulated-likelihood optimizer call. For another model, first provide its solver/likelihood rather than inventing a universal command.

Return parameter estimates and uncertainty, fit diagnostics, identification/normalization and counterfactual assumptions.
