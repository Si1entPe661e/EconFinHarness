# did checklist (answer yes / no / unknown; "unknown" is a legitimate answer and must be reported as such)

Design

1. Is the estimand written (overall ATT, cohort-time ATT, dynamic effects) together with the comparison group (never-treated, not-yet-treated, both)?
2. Are treatment dates known for every treated unit and fixed before outcomes are observed (no anticipation argument, or one that is stated)?
3. Is the design classified: single adoption date, staggered adoption, triple difference, synthetic DID?
4. For staggered adoption, is the estimator choice justified (heterogeneity-robust estimator, or TWFE with a decomposition diagnostic)?

Data construction

5. Are cohort, relative time and post indicators built explicitly and checked (no reversals, or reversals handled)?
6. Is the panel checked for unit-time uniqueness, balance, singleton units and sample size per relative-time bin?
7. Is the reference period stated and are endpoints binned or trimmed as stated in the plan?

Estimation

8. Does the estimation call show the fixed effects actually absorbed (not inferred from `xtset` or panel identifiers)?
9. Are covariates time-invariant or pre-treatment, and is their role stated?
10. Are weights (if any) visible in the call and justified?
11. For heterogeneity-robust estimators, is the never-treated code, the comparison option and the aggregation stated?

Inference

12. Is the cluster level the treatment assignment level, stated with a rationale, and does the cluster variable reach the call?
13. Is the number of clusters reported and, when small, is a wild cluster bootstrap or randomization inference used?

Diagnostics and robustness

14. Pre-trend plot with confidence bands produced from code?
15. Pre-trend test on leads reported, with the pre-testing caveat stated?
16. Covariate balance between treated and comparison units reported?
17. For staggered TWFE, a Bacon decomposition or comparison with a robust estimator reported?
18. Sensitivity to parallel-trend violations reported when the plan calls for it?
19. Robustness: alternative comparison group, alternative estimator, alternative fixed effects, alternative clustering reported as planned?

Outputs and interpretation

20. Event-study plot marks the reference period and uses the same sample as the table?
21. Every table column maps to a plan specification id, with N, clusters, fixed effects, SE type and weights in the notes?
22. Are effects interpreted relative to the comparison group and the sample of cohorts actually identified?

Corpus and card use

23. Were nulls and not_found_in_scope in cards treated as unknown rather than as "not done"?
24. Were any corpus code fragments reused only after a licence check?
