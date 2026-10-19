---
name: inference-clustering-efh
description: "Choose, implement, document, and check standard errors: robust vs clustered, cluster level from design, two-way and multi-way, few clusters and wild bootstrap, HAC, Driscoll-Kraay, Conley, randomization inference. Use when an inference plan is written, implemented, or reviewed. Not for choosing an estimator or building tables."
metadata:
  version: 0.1.0
  kind: task
  status: draft
---

# Standard errors and inference

## When to use

Use to choose or check covariance estimates, confidence intervals, p-values or resampling for an existing estimator. Sample construction belongs to panel-data-checks-efh; identification and point estimation belong to the relevant method skill.

## Inputs

Estimating equation, fitted sample, assignment/sampling mechanism, repeated observations, FE and weights, candidate dependence groups, cluster and treated-cluster counts, time frequency or spatial coordinates where relevant.

## Procedure

1. State the source of uncertainty: assignment, sampling or model errors. Derive dependence from the design; do not choose the cluster variable because it produces a preferred p-value.
2. For clustered assignment, account for assignment-group dependence; for repeated observations, account for serial dependence. Survey strata/PSUs and sampling weights may require a survey estimator rather than ordinary weighted regression.
3. Use heteroskedastic robust covariance when observations are appropriately independent. Use one-way clustering for within-group dependence and multi-way clustering for distinct non-nested dependence dimensions. Nested clusters generally call for the coarser relevant group.
4. Count groups, treated groups, sizes and leverage on the fitted sample. Few clusters, severe imbalance or few treated clusters need special treatment; no universal count threshold guarantees reliable inference.
5. Consider a null-imposed wild cluster bootstrap, CR2 with Satterthwaite degrees of freedom, or assignment-based inference when their assumptions fit. None automatically repairs a design with almost no independent treatment variation.
6. Use HAC for ordered time series and state the lag/kernel choice, prewhitening, finite-sample adjustment and reference distribution. Package defaults may implement a different estimator: `sandwich::NeweyWest` defaults to prewhitening, which must be disabled for the unprewhitened Newey-West (1987) calculation. Overlapping h-period outcomes usually require at least h-1 lags, with more if dependence persists. Ordinary HAC on stacked unrelated panel rows is inappropriate. Check calendar gaps before using a package's row-based lag; never fill missing return or slope estimates with zero. When needed, pad centered estimating scores on the calendar grid and retain the actual observation denominator, with an independent pair-distance check.
7. Use Driscoll–Kraay for suitable panels with sufficiently long time dimension and broad cross-sectional dependence; specify time ordering and lag. Use Conley for spatial dependence with justified coordinates, distance units, cutoff and kernel. Sensitivity choices should have a substantive rationale.
8. Randomization inference must reproduce the actual mechanism, including blocks, clusters, treatment counts and unequal assignment probabilities. Permuting an arbitrary regressor is not an experiment. State the sharp null and statistic.
9. Make finite-sample corrections and degrees of freedom consistent with the estimator, FE and singleton handling. When comparing software, distinguish covariance changes from sample changes.
10. Ensure reported SE, intervals, p-values and stars use the intended fitted model and inference. A bootstrap p-value can accompany analytic SE if clearly distinguished; do not silently combine them as though they share one formula.

## Software commands

[code-examples.md](code-examples.md) gives R robust/clustered/CR2/HAC/DK/Conley calls, Stata cluster and wild-bootstrap calls, Python panel covariance, and a blocked cluster randomization test.

## Outputs and missing information

Return the covariance choice and rationale, cluster counts or time/spatial tuning parameters, interval/test details and any material limitation. If assignment or dependence is unknown, explain the candidate choices instead of silently selecting one.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Work with the selected method and actual fitted sample. Preserve specialized RD, matching, weak-IV, randomization or forecast inference where required. Return selected covariance/test results and reference-distribution choices to implementation and tables-figures-efh; changing inference requires updating affected intervals, p-values, stars and claims.

## Research records

Recorded practice is in `harness/paradigms/`: each method's folder and `_all/reported.md` across methods. It describes what papers did, not what is correct.

## Corpus examples

Related commands as written in published replication packages, with paper shares: [Stata](examples/stata.md), [R](examples/r.md), [Python](examples/python.md), [MATLAB](examples/matlab.md), [Julia](examples/julia.md). Open only the file for the language in use.
