---
name: inference-clustering
description: "Choose, implement, document, and check standard errors: robust vs clustered, cluster level from design, two-way and multi-way, few clusters and wild bootstrap, HAC, Driscoll-Kraay, Conley, randomization inference. Use when an inference plan is written, implemented, or reviewed. Not for choosing an estimator or building tables."
version: 0.1.0
kind: task
status: draft
---

# Standard errors and inference

## When to use

Use to choose or check covariance estimates, confidence intervals, p-values or resampling for an existing estimator. Sample construction belongs to panel-data-checks; identification and point estimation belong to the relevant method skill.

## Inputs

Estimating equation, fitted sample, assignment/sampling mechanism, repeated observations, FE and weights, candidate dependence groups, cluster and treated-cluster counts, time frequency or spatial coordinates where relevant.

## Procedure

1. State the source of uncertainty: assignment, sampling or model errors. Derive dependence from the design; do not choose the cluster variable because it produces a preferred p-value.
2. For clustered assignment, account for assignment-group dependence; for repeated observations, account for serial dependence. Survey strata/PSUs and sampling weights may require a survey estimator rather than ordinary weighted regression.
3. Use heteroskedastic robust covariance when observations are appropriately independent. Use one-way clustering for within-group dependence and multi-way clustering for distinct non-nested dependence dimensions. Nested clusters generally call for the coarser relevant group.
4. Count groups, treated groups, sizes and leverage on the fitted sample. Few clusters, severe imbalance or few treated clusters need special treatment; no universal count threshold guarantees reliable inference.
5. Consider a null-imposed wild cluster bootstrap, CR2 with Satterthwaite degrees of freedom, or assignment-based inference when their assumptions fit. None automatically repairs a design with almost no independent treatment variation.
6. Use HAC for ordered time series and state the lag/kernel choice. Overlapping h-period outcomes usually require at least h-1 lags, with more if dependence persists. Ordinary HAC on stacked unrelated panel rows is inappropriate.
7. Use Driscoll–Kraay for suitable panels with sufficiently long time dimension and broad cross-sectional dependence; specify time ordering and lag. Use Conley for spatial dependence with justified coordinates, distance units, cutoff and kernel. Sensitivity choices should have a substantive rationale.
8. Randomization inference must reproduce the actual mechanism, including blocks, clusters, treatment counts and unequal assignment probabilities. Permuting an arbitrary regressor is not an experiment. State the sharp null and statistic.
9. Make finite-sample corrections and degrees of freedom consistent with the estimator, FE and singleton handling. When comparing software, distinguish covariance changes from sample changes.
10. Ensure reported SE, intervals, p-values and stars use the intended fitted model and inference. A bootstrap p-value can accompany analytic SE if clearly distinguished; do not silently combine them as though they share one formula.

## Software commands

[code-examples.md](code-examples.md) gives R robust/clustered/CR2/HAC/DK/Conley calls, Stata cluster and wild-bootstrap calls, Python panel covariance, and a blocked cluster randomization test.

## Outputs and missing information

Return the covariance choice and rationale, cluster counts or time/spatial tuning parameters, interval/test details and any material limitation. If assignment or dependence is unknown, explain the candidate choices instead of silently selecting one.

Use [checklist.md](checklist.md) or the existing trace note when useful; no additional plan file is required.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Work with the selected method and actual fitted sample. Preserve specialized RD, matching, weak-IV, randomization or forecast inference where required. Return selected covariance/test results and reference-distribution choices to implementation and tables-figures; changing inference requires updating affected intervals, p-values, stars and claims.

## Evidence

This is a task skill. It carries no corpus counts. It makes no claim about how often any inference choice appears in published replication code, and it must not be cited as evidence that a practice is standard.

Method-specific observed practice, with denominators and explicit unknown counts, lives in `harness/paradigms/<method>/observed.md` (for example `harness/paradigms/rdd/observed.md`). Recommendations, where they exist, are separate and live in `harness/paradigms/<method>/recommendations.md`.

Existing method observations and paper-practice notes remain available for consultation.

<!-- reported-practice:begin -->
### Reported practice (paper texts; generated by `fhb papers skill-evidence`, 2026-09-09)

From 91 paper-practice notes (all methods; `harness/paradigms/_all/reported.md`, note hashes there). Counts are papers whose note carries the tag; an absent tag means the reader did not record it. Pointers are artid p.pages locator.

- **inference_justification** (papers with the category: 91/91): `no_justification_found` 57 (e.g. aer_107_1_5 p.14 Section II.B; Section III.A); `cluster_at_unit_level` 36 (e.g. aer_107_5_108 p.5 Table 1 notes); `cluster_at_assignment_level` 35 (e.g. aer_107_1_5 p.18 Section III.A); `randomization_inference` 24 (e.g. aer_107_1_5 p.22 Section III.A; Figure 7)
<!-- reported-practice:end -->
