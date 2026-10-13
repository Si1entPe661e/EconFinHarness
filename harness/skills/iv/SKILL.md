---
name: iv
description: "Instrumental-variables designs (2SLS with fixed effects, shift-share, examiner/judge leniency, weak-instrument-robust inference) for design, implementation, audit and explanation. Use when an excluded instrument shifts an endogenous treatment. Do not use when the exclusion restriction has no design argument or when the instrument is a function of the outcome."
version: 0.1.0
kind: method
status: draft
---

# Instrumental variables

## When to use

Use when excluded instruments shift endogenous regressors and the design supports independence and exclusion. Cover 2SLS, absorbed fixed effects, multiple endogenous regressors and leniency instruments. Use shift-share for the additional exposure/shock decisions, and rdd for local fuzzy RD.

## Inputs

Outcome, endogenous regressors, excluded instruments, predetermined controls, fixed effects, weights, assignment or sampling units, and the intended population. Explain why the instrument is relevant and excluded. A first-stage association alone cannot establish validity.

## Procedure

1. State the estimand. Binary treatment/instrument designs can identify a complier LATE under independence, exclusion, relevance and monotonicity. Continuous or multiple instruments need their own interpretation; do not label every IV coefficient a LATE.
2. Construct the instrument before estimation. For leniency, respect assignment cells and remove the observation's own contribution; examine decision-maker caseloads and assignment balance. Leave-one-out construction does not establish random assignment or exclusion.
3. Build one complete-case sample covering every stage, instrument, FE, weight and cluster variable. Run first stages, reduced form, OLS and 2SLS on that same sample. Keep controls and weights consistent.
4. Report excluded-instrument coefficients and joint tests in each first stage. Inspect partial relevance after absorbing FE. With several endogenous regressors, assess conditional strength, not only an overall F.
5. Use strength diagnostics appropriate to heteroskedasticity or clustering. An ordinary first-stage F is not an effective F by definition; a statistic exceeding 10 is not a universal guarantee. With weak instruments, use AR/CLR or another procedure valid for the design and covariance; confidence sets can be unbounded or disconnected. tF applies only in its supported single-instrument setting.
6. Match inference to assignment, sampling and dependence. Count clusters on the fitted sample. Instrument identifiers alone do not automatically determine the correct cluster level. Use shock-level or exposure-aware inference for shock-based shift-share designs.
7. When overidentified, explain what the overidentification test assumes; non-rejection cannot establish exclusion. Consider LIML with many instruments and appropriate inference, rather than treating it as a validity repair.
8. Check predetermined balance, placebo outcomes, alternative instrument definitions and sample restrictions. Interpret results using the actual instrument-induced variation and discuss external validity.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Software commands

[code-examples.md](code-examples.md) contains R fixest 2SLS with first-stage and reduced-form calls, Stata ivreg2/ivreghdfe, Python IV2SLS, and a clustered AR test for a specified coefficient. Use the IV estimator directly; regressions on manually generated fitted treatment generally have incorrect second-stage standard errors.

## Outputs and missing information

Return the estimate and interval, first-stage results, reduced form, sample size, FE, weights, covariance choice and cluster count. Explain the instrument and estimand in plain language. Missing exclusion or assignment information remains an unresolved design question; a successful estimation call does not resolve it.

The existing [checklist.md](checklist.md) is optional.

## Research records

Read [research records](references/research-records.md) only when recorded practice or corpus evidence is relevant. These records are distinct from methodological recommendations.
