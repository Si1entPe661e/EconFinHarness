# rdd checklist (answer yes / no / unknown; "unknown" is a legitimate answer and must be reported as such)

Design

1. Is the cutoff fixed by a rule that predates the outcomes, and is it stated in the plan?
2. Is the design classified (sharp / fuzzy / kink) and is the estimand written out (effect at the cutoff; for compliers if fuzzy)?
3. Is the running variable observed for every unit in the estimation sample, and was it not affected by treatment?
4. Does the sign of the treatment jump match the assignment rule and treatment coding?

Running variable and sample

5. Are the number of observations on each side of the cutoff and within the bandwidth reported?
6. Was the running variable checked for mass points, heaping and the share of distinct values, and was the discrete branch used when appropriate?
7. Was a density test at the cutoff run on the estimation sample, with statistic and p-value reported?
8. Was covariate balance at the cutoff estimated for predetermined covariates with the same bandwidth rule?

Estimation options (each one visible in the call, not assumed from defaults)

9. Polynomial order stated (and not a global high-order polynomial)?
10. Kernel stated?
11. Bandwidth selector stated (MSE-optimal / manual), and are the left and right bandwidths reported?
12. Bias-corrected robust confidence intervals reported alongside the conventional point estimate?
13. Covariates, if used, entered as adjustment in the RD call rather than changing the estimand?
14. For fuzzy designs, is the first stage inside the bandwidth reported and strong enough to interpret the Wald ratio?

Inference

15. Is the SE type (heteroskedasticity-robust vs cluster) stated, and does the cluster variable reach the RD call?
16. Is the number of clusters within the bandwidth reported, and is a small-cluster plan in place when it is small?

Robustness and outputs

17. Bandwidth sensitivity grid reported (estimates and CIs across bandwidths)?
18. Alternative polynomial order and, when heaping exists, a donut specification reported?
19. Placebo cutoffs reported with treatment held fixed?
20. RD plot produced from code with binned means and the local fit?
21. Do table notes state bandwidth, order, kernel, effective N and SE type?
22. Are the interpretations local to the cutoff and, for fuzzy designs, restricted to compliers?

Corpus and card use

23. When citing corpus practice, were nulls and not_found_in_scope treated as unknown rather than as "not done"?
24. Are any restrictions on redistributing substantial reused code respected?
