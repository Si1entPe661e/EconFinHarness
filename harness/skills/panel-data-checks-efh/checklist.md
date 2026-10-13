# Checklist: panel and sample checks

Each item is answered `yes`, `no`, or `unknown`. `unknown` means the inputs available did not settle the question. `unknown` is never recorded as `yes`. `no` means the check ran and the answer is negative.

Use relevant items and note the observed values or unresolved questions.

| # | Item | yes / no / unknown |
|---|---|---|
| 1 | Is the claimed unit of observation stated in writing before the checks were run? | |
| 2 | Is the key unique on the estimation sample (row count equals distinct key count)? | |
| 3 | If duplicates exist, is their mechanism identified (finer unit, merge fan-out, repeated append)? | |
| 4 | Is the rule for resolving duplicate keys stated in the analysis plan rather than only in code? | |
| 5 | Are the number of groups and the group size distribution reported for every fixed effect and cluster dimension? | |
| 6 | Is the number of singleton groups reported, and is it known whether the estimator drops them? | |
| 7 | Is the panel balance reported (units, periods, balanced or not, units observed once)? | |
| 8 | Are within-unit time gaps identified before lags, leads, or differences are computed? | |
| 9 | Do lags, leads, and differences use a declared time index rather than row order? | |
| 10 | Is the time variable a single consistent frequency with no mixed formats? | |
| 11 | Does the treatment indicator agree with the treatment timing variable for every unit? | |
| 12 | Is treatment reversal either absent or explicitly documented as allowed by the estimator? | |
| 13 | Is the treatment timing measured at the level of assignment rather than a finer level? | |
| 14 | Is the number of units per treatment cohort reported? | |
| 15 | Does every merge declare its expected cardinality before it runs? | |
| 16 | Does every merge report matched rows, unmatched left rows, and unmatched right rows? | |
| 17 | Were unmatched merge rows inspected for a pattern in treatment, period, or outcome? | |
| 18 | Are join key types and formats compatible across sources (case, whitespace, leading zeros, identifier changes over time)? | |
| 19 | Does an ordered restriction list reproduce the reported N exactly? | |
| 20 | Is per-variable missingness reported, including how many rows each variable drops? | |
| 21 | Was differential missingness across treatment arms or periods checked? | |
| 22 | Are sentinel missing codes identified and excluded from being treated as data? | |
| 23 | Are weights non-negative, non-missing on the estimation sample, and matched to the estimand? | |
| 24 | Are winsorization or trimming rules recorded with variables, cutoffs, sides, grouping, and position in the pipeline? | |
| 25 | Were variable ranges and units checked against the data dictionary or the stated definition? | |
