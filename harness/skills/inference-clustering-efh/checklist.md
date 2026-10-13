# Checklist: standard errors and inference

Each item is answered `yes`, `no`, or `unknown`. `unknown` means the available inputs did not settle the question and is never recorded as `yes`. `no` means the check ran and the answer is negative.

Use relevant items and note the inference choice, observed counts and unresolved questions.

| # | Item | yes / no / unknown |
|---|---|---|
| 1 | Is the source of uncertainty stated in one sentence (design, sampling, or model)? | |
| 2 | Is the level of treatment assignment documented independently of the code? | |
| 3 | Is the cluster level at least as coarse as the level of treatment assignment? | |
| 4 | If the data comes from a survey, does the inference account for the sampling design? | |
| 5 | For panel data, is within-unit serial correlation addressed by the chosen method? | |
| 6 | If two-way or multi-way clustering is used, is the number of groups reported for every dimension? | |
| 7 | Is the number of clusters reported next to the estimate? | |
| 8 | Is the number of treated clusters reported, not only the number of clusters? | |
| 9 | If clusters are few, is a few-cluster method used or is the limitation stated explicitly? | |
| 10 | If a wild cluster bootstrap is used, are replications, seed, bootstrap cluster variable, and whether the null is imposed all recorded? | |
| 11 | If HAC is used, is the lag truncation rule stated before estimation rather than chosen from results? | |
| 12 | If Driscoll-Kraay is used, are the number of periods and the lag reported? | |
| 13 | If Conley spatial standard errors are used, are the distance cutoff and kernel stated and varied in robustness? | |
| 14 | If randomization inference is used, does the permutation reproduce the actual assignment mechanism including blocking? | |
| 15 | Is the small-sample correction recorded (name and package default versus explicit setting)? | |
| 16 | Is the degrees of freedom rule recorded, including the treatment of absorbed fixed effects and dropped singletons? | |
| 17 | Does the cluster variable used in the call resolve to the variable the design implies, after following all macros and wrappers? | |
| 18 | Does the exported table use the intended fitted model? | |
| 19 | Do the standard errors, p-values, confidence intervals, and stars in the same table all come from the same variance estimator? | |
| 20 | Is the software function and version recorded for every inference method used? | |
| 21 | Were alternative inference choices run and reported, rather than only the one with the smallest p-value? | |
| 22 | Is the order of decisions recorded, so that the main choice can be seen not to depend on the results? | |
| 23 | Is the inference choice clear for every reported model? | |
| 24 | Are all unresolved inference questions recorded as `unknown` or `unverified` rather than silently defaulted? | |
