---
name: gmm
description: Generalized method of moments for explicit orthogonality conditions, IV-GMM, nonlinear moments and dynamic panels. Check identification, weighting, covariance, optimization and instrument proliferation.
kind: method
---

# Generalized method of moments

## When to use

Use when a parameter is identified by explicit population moment restrictions. Cover linear IV-GMM and nonlinear moment estimation; dynamic-panel GMM additionally needs valid lag restrictions and stationarity/initial-condition assumptions for system moments.

## Inputs

Parameter vector, observation-level moments, instruments, independent/time/cluster ordering, parameter bounds and starting values, moment scaling, weighting-matrix plan and intended inference.

## Procedure

1. Write each moment and explain why its expectation is zero at the target parameter. Count moments/parameters and assess rank; having more moments than parameters is not enough for identification.
2. Build moments on a consistent sample with instruments measured at admissible times. Separate exogenous, predetermined and endogenous regressors.
3. State one-step/two-step/iterated estimation and the covariance underlying the weighting matrix. Scale disparate moments sensibly and inspect conditioning rather than silently inverting a nearly singular matrix.
4. Optimize with feasible parameter transformations, several starts and sensible tolerances. Check objective, gradient, boundaries and Jacobian rank; optimizer success alone does not establish an identified optimum.
5. Match moment covariance to iid, serial or cluster dependence. Two-step finite-sample correction may matter, particularly dynamic panels; robust covariance and efficient weighting are related but distinct choices.
6. Report J/overidentification tests with their assumptions; non-rejection does not establish all instruments valid. For dynamic panels report serial-correlation diagnostics, lag ranges and instrument count; restrict/collapse instruments to avoid proliferation.
7. Examine sensitivity to moments, instruments, weighting and starts, and show whether identification is weak or concentrated.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) contains a complete R moment function and Stata clustered IV-GMM. Return parameter estimates, intervals, moments/instruments, objective/convergence and material diagnostics. Do not fabricate structural moments when the economic model is missing.
