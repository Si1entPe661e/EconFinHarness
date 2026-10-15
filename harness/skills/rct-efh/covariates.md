# Baseline covariates in randomized experiments

Covariates in an experiment improve precision; they do not identify the effect. Fix the set before outcomes are seen and keep it the same across outcomes unless the plan says otherwise.

## Strata and blocks

Include the randomization strata or blocks in every specification (Bruhn and McKenzie 2009, DOI 10.1257/app.1.4.200). Rebuild them from the description of the randomization: one indicator per stratum level, including levels that a later summary in the paper lists together. A level must not be pooled with missing or don't-know in the reference category, because that changes the comparison within strata. When a paper's list of stratification controls differs from its randomization description, record both readings.

## Missing baseline values

Under randomization a missing-indicator adjustment keeps the estimate unbiased for the assignment effect, and it keeps every randomized unit in the sample (White and Thompson 2005, DOI 10.1002/sim.1981; Groenwold et al. 2012, DOI 10.1503/cmaj.110977). The default is a constant fill plus one indicator per covariate with missing values. Two cautions:

- An indicator that is nonzero on one or two fitted rows acts as a dummy for those observations and removes their influence on the other coefficients. Report it and keep it only if the plan requires it.
- Fill from another measurement of the same concept before filling a constant (see [variable construction](../panel-data-checks-efh/references/variable-construction.md)).

## Level and timing

In stacked designs with several respondents per unit (spouses, parents and children), distinguish household-level covariates from respondent-specific ones, and state whether covariates are interacted with the respondent type. A time-invariant fact measured after assignment, such as birth year or completed schooling, is admissible. A time-varying covariate must be measured before assignment.

## Heterogeneity

For heterogeneity by a baseline group, add the group main effects and the group-by-assignment terms to the main equation and keep its controls. Interactions of the group with other regressors are variants. The group must be defined from baseline information, and units without a group value need a stated rule.
