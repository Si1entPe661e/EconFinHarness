---
name: panel-data-checks-efh
description: "Sample and panel structure checks to run before any estimation: key uniqueness, duplicates, singleton groups, balance, treatment timing, merge quality, missingness, weights, variable ranges and date handling. Use when an analysis sample is built or changed. Do not use for choosing standard errors or for building output tables."
metadata:
  version: 0.1.0
  kind: task
  status: draft
---

# Panel and sample checks

## When to use

Use before estimation or when changing a sample, key, merge, date variable, treatment timing, weight or transformation. Apply only checks relevant to the data; do not require a balanced panel when the estimator permits an unbalanced one.

## Inputs

Unit of observation, intended key, time frequency, outcome and regressors, treatment/assignment information, merge keys and expected cardinality, weights, FE and cluster dimensions, and sample restrictions.

## Procedure

1. Check missing keys and key uniqueness. Distinguish exact duplicate rows from conflicting records and from a genuinely finer observation unit. Inspect duplicate groups; never resolve conflicts by keeping an arbitrary first row.
2. Parse dates and identifiers consistently, preserving leading zeros. Confirm frequency, sorting and time gaps. A previous row is a calendar lag only when the time index is consecutive.
3. Count units, periods, observations per unit, singleton FE groups and cluster sizes. Inspect entry/exit and balanced-panel restrictions for selection; compare estimator N with the intended sample after singleton/collinearity removal.
4. Check every merge's cardinality and matched/unmatched keys. Inspect fan-out and differential unmatched rates across treatment or time. A successful join is not evidence of a correct match.
5. Apply restrictions sequentially and explain major losses. Check missingness for outcomes, every model term, instruments, weights, FE and clusters. Do not change the sample unintentionally when comparing models. A derived indicator keeps a missing source missing until a declared fill rule; count missing sources per derived variable before filling. Comparisons such as `x != 1` or `x > 0` are true for a missing value in Stata, and conditional helpers in R and pandas can turn a missing source into 0.
6. Check treatment cohorts, treatment before recorded adoption, reversals and event-time coding. The never-treated sentinel must match the estimator. Eligibility, assignment and treatment received are distinct variables.
7. Inspect ranges, units, special missing codes, transformations and outliers. For a declared discrete scale, list values off its support: non-integers, out-of-range values and stored nonresponse codes such as 7, 77, 98 or 99, negative codes and decimal placeholders; record a rule and its alternative. A regressor that is constant on all but one or two fitted rows acts as an observation dummy. Before totalling to a higher level, confirm the component is not already copied to every member row. When a concept has several measurements or informants, follow [variable construction](references/variable-construction.md). Map columns to source definitions using documented meaning and independent diagnostics; names such as `main`, `base` or `original` do not establish provenance, excess-return treatment or the upstream estimation procedure. Distinguish supplied intermediate data from transformations independently reproduced. Logs exclude nonpositive values; zero and missing are different. Winsorization needs a substantive rule and must not use future observations when constructing predictions or portfolio signals.
8. Check weights for missingness, sign and extreme concentration; distinguish sampling, analytic, frequency and portfolio weights. Decide how zero weights are treated by the estimator.
9. Inspect the final fitted sample and cluster counts. Return the important issues and their effect on sample construction, with small summaries when useful.

## Software commands

[code-examples.md](code-examples.md) provides duplicate inspection, validated merges, calendar-aware lags, treatment reversal checks and weight/missingness checks in Python, R and Stata, plus fitted-sample boundary counts and missing-value behavior in four runtimes.

## Missing information and outputs

When data are unavailable, explain which properties cannot be checked. Return the intended/fitted N, units/periods, merge losses and unresolved variable issues that matter to the analysis. A short note or sample-flow table is enough; use existing templates only when useful.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Pass the actual usable sample, time/treatment definitions and weight information to the selected method and inference-clustering-efh. Recheck the fitted sample after FE/singleton, bandwidth, matching or support restrictions; tables-figures-efh must use the resulting counts, not raw-data counts.

## Research records

Recorded practice is in `harness/paradigms/`: each method's folder and `_all/reported.md` across methods. It describes what papers did, not what is correct.

## Corpus examples

Related commands as written in published replication packages, with paper shares: [Stata](examples/stata.md), [R](examples/r.md), [Python](examples/python.md), [MATLAB](examples/matlab.md), [Julia](examples/julia.md).
