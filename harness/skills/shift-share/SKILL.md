---
name: shift-share
description: Shift-share exposure and IV designs with a clear shares-based or shocks-based identification argument. Construct predetermined exposures, handle incomplete shares and leave-out shocks, and implement shock-aware inference.
kind: method
---

# Shift-share designs

## When to use

Use for exposure regressors or instruments built as sums of baseline shares times common shocks. Use iv for general 2SLS and weak-instrument issues. Shares-based and shocks-based identification imply different requirements and inference.

## Inputs

Exposure unit, shock unit and time, baseline shares, shocks and their construction samples, outcomes/endogenous treatment, controls, weights, dependence groups and the identification argument.

## Procedure

1. Write z_i = sum_n s_in g_n and choose the identification branch. Exogenous shares require an exposure-design argument; exogenous shocks require appropriately conditioned shock assignment and enough independent shock variation.
2. Fix shares before treatment and inspect totals, missing sectors, dominant exposures and effective shock concentration. If shares do not sum to a constant, account for total exposure and its interactions with shock-period means as the design requires.
3. Inspect shock contamination by the observation's own outcomes/endogenous treatment. Construct leave-out shocks when necessary using actual aggregation weights; leaving out only an observation can be inadequate for a correlated assignment group.
4. Estimate the exposure reduced form and, for IV, first stage/2SLS on common samples and controls. Explain what endogenous treatment differs from the instrument.
5. Under shock identification, residualize outcomes and treatment using the same unit-level controls/weights, aggregate with baseline-share exposure weights, and use compatible shock-level weighting/inference. Controls imposed at unit level cannot simply be omitted without residualization.
6. Account for shock dependence across industries, origins or periods. Unit-level clustered 2SLS alone need not capture common-shock uncertainty. Treat concentrated shocks and few shock clusters as substantive inference limitations.
7. Examine dominant shocks, leave-one-shock-out results, pretrends/balance and alternative base years. Shares-based decomposition and shock-level diagnostics answer different questions; avoid presenting a decomposition as proof of exogeneity.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives construction, common-control residualization, shock aggregation and clustered shock-level IV, plus Stata ivreg2 calls.

Return instrument components, identification branch, concentration, first-stage/IV results and the chosen shock/exposure inference.
