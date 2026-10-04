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

## Evidence

Observed practice is generated into `harness/paradigms/iv/observed.md` (distillation set: 10 cards, AER 4, ReStud 4, JPE 1, RFS 1; Stata code in 9, R in 5) with pointers. Three papers are held out (`harness/paradigms/iv/reported.md`: aer_112_5_9, jpe_132_9_2, qje_139_1_2). Headline observations:

- 2SLS is the recorded estimator in all 10 cards; commands are `ivreg2` (6), `ivreghdfe` (3), `reghdfe` for reduced forms (2), `feols` (1), `ivreg` (1), `twostepweakiv` (1).
- Standard errors are clustered in 7 of 10 cards, robust in 1, unknown in 2; clustering dimensions are unknown in 4.
- First-stage diagnostics are `unknown` in all 8 cards that record a diagnostic entry; weak-IV tests are observed in 1 card (`twostepweakiv`), not found in scope in 1, unknown in 2; a monotonicity/exclusion test is observed in 1 (leniency design).
- Design variants are unknown in 8 of 10 (`shift_share` 1, `distance_instrument` 1); roles unknown in 9. Package attribution known in 2; no table packages recorded.

The gap between IV practice in the literature and what the cards could ground (first stage unknown everywhere) is itself the main finding: extraction needs a targeted first-stage read.

<!-- reported-practice:begin -->
### Reported practice (paper texts; generated by `fhb papers skill-evidence`, 2026-09-09)

From 32 paper-practice notes (method iv; `harness/paradigms/iv/reported.md`, note hashes there). Counts are papers whose note carries the tag; an absent tag means the reader did not record it. Pointers are artid p.pages locator.

- **data_access** (papers with the category: 22/32): `administrative` 17 (e.g. aer_109_7_8 p.1 Title-page footnote); `data_restricted` 11 (e.g. aer_109_7_8 p.1 Title-page footnote); `linked_records` 8 (e.g. aer_109_7_8 p.1 Title-page footnote); `public_use` 6 (e.g. aer_112_2_1 p.6 Section II)

- **design_statement** (papers with the category: 26/32): `instrument_exclusion_argued` 21 (e.g. aer_109_7_8 p.8 Section I, equations (1)-(2)); `design_variant_named` 19 (e.g. aer_109_7_8 p.4 Introduction, literature paragraph); `threats_discussed` 17 (e.g. aer_109_7_8 p.17 Section IIIB); `estimand_named` 16 (e.g. aer_109_7_8 p.17 Section IV, discussion after Table 4)

- **diagnostic_reported** (papers with the category: 28/32): `in_main_text` 20 (e.g. aer_109_7_8 p.8 Table 1); `first_stage_table` 19 (e.g. aer_109_7_8 p.15 Figure 3 and Table 3); `weak_iv_statistic` 18 (e.g. aer_110_2_5 p.19 Appendix Table B2); `in_appendix` 15 (e.g. aer_109_7_8 p.17 Section IIIB, online Appendix Table A3)

- **external_validity** (papers with the category: 19/32): `scaling_discussed` 9 (e.g. aer_109_7_8 p.40 Conclusion, second caveat); `site_specific` 9 (e.g. aer_109_7_8 p.40 Conclusion, second caveat); `compliers_vs_population` 7 (e.g. aer_109_7_8 p.40 Conclusion); `in_main_text` 2 (e.g. restud_2026_restud_rdag027 p.31 Section 5.2; Section 8)

- **heterogeneity_reported** (papers with the category: 12/32): `mechanism_motivated` 11 (e.g. aer_109_7_8 p.22 Section VI, Tables 6 and 7); `split_sample` 11 (e.g. aer_109_7_8 p.22 Section VI, Tables 6 and 7); `interaction` 5 (e.g. aer_112_2_1 p.25 Figure 8; Tables 5-6); `exploratory_labelled` 3 (e.g. aer_109_7_8 p.27 Section VIA, closing paragraph)

- **inference_justification** (papers with the category: 24/32): `no_justification_found` 13 (e.g. aer_109_7_8 p.16 Table 3 notes and surrounding text); `cluster_at_assignment_level` 11 (e.g. aer_109_7_8 p.16 Table 3 notes and surrounding text); `cluster_at_unit_level` 5 (e.g. aer_111_12_2 p.19 Section IIIA, footnote); `in_footnote` 3 (e.g. restud_2025_restud_rdae072 p.7 Table 1 notes, Table 3 notes, footnote 1)

- **limitation_stated** (papers with the category: 16/32): `interpretation_caveat` 9 (e.g. aer_112_2_1 p.4 Introduction); `data_coverage` 8 (e.g. aer_112_2_1 p.7 Section II.A); `identification_caveat` 8 (e.g. aer_109_7_8 p.40 Conclusion, third caveat); `measurement` 8 (e.g. aer_112_2_1 p.7 Section II.A)

- **magnitude_interpretation** (papers with the category: 20/32): `back_of_envelope` 13 (e.g. aer_110_2_5 p.39 Appendix A); `relative_to_mean` 11 (e.g. aer_109_7_8 p.22 Section V, closing paragraph); `compared_to_literature` 10 (e.g. aer_111_12_2 p.37 Section IVB, footnote); `precision_discussed` 10 (e.g. aer_112_2_1 p.24 Table 4 and surrounding discussion)

- **mechanism_evidence** (papers with the category: 18/32): `suggestive_labelled` 10 (e.g. aer_109_7_8 p.27 Section VIB); `intermediate_outcomes` 6 (e.g. aer_109_7_8 p.26 Section VIB, Table 8); `model_guided` 6 (e.g. aer_110_2_5 p.39 Appendix A, back-of-the-envelope calcula); `heterogeneity_as_mechanism` 5 (e.g. aer_109_7_8 p.26 Section VIB, Table 8)

- **other** (papers with the category: 4/32): `online_appendix_not_available` 1 (e.g. restud_2026_restud_rdaf044 p.33 Supplementary Data); `other:descriptive_regression_of_loan_terms` 1 (e.g. rfs_2026_rfs_hhaf080 p.14 Table 2, Section 2.2.2 and 2.2.3); `other:editor_named` 1 (e.g. restud_2026_restud_rdag029 p.1 Title page footer; Funding); `other:funding_disclosed` 1 (e.g. restud_2026_restud_rdag029 p.1 Title page footer; Funding)

- **preregistration_or_ethics** (papers with the category: 3/32): `irb_stated` 3 (e.g. aer_115_1_8 p.1 Footnote, title page)

- **presentation_convention** (papers with the category: 23/32): `notes_state_sample` 17 (e.g. aer_109_7_8 p.16 Tables 3-11 generally); `notes_state_se` 17 (e.g. aer_109_7_8 p.16 Tables 3-11 generally); `summary_stats_table` 13 (e.g. aer_109_7_8 p.10 Table 2); `appendix_tables_numbered_a` 11 (e.g. aer_113_3_7 p.9 Section I.C, footnote citing Online Appe)

- **replication_statement** (papers with the category: 24/32): `replication_package_cited` 23 (e.g. aer_109_7_8 p.1 Title-page footnote and reference list); `code_public` 13 (e.g. aer_115_1_8 p.31 References); `data_restricted` 8 (e.g. ecta_2024_ecta20579 p.30 End matter, replication statement); `data_access_procedure_described` 7 (e.g. aer_109_7_8 p.1 Title-page footnote and reference list)

- **robustness_reported** (papers with the category: 18/32): `alt_specification` 13 (e.g. aer_111_12_2 p.38 Section IVB, Robustness paragraph); `in_appendix` 13 (e.g. aer_111_12_2 p.38 Section IVB, Robustness paragraph); `alt_sample` 10 (e.g. aer_109_7_8 p.7 Footnote 9); `in_main_text` 8 (e.g. aer_113_1_8 p.15 Table 4)

- **sample_construction** (papers with the category: 21/32): `data_source_named` 19 (e.g. aer_109_7_8 p.9 Section IIA, Data and Sample Restriction); `exclusions_justified` 16 (e.g. aer_109_7_8 p.10 Section IIA); `sample_period_stated` 15 (e.g. aer_109_7_8 p.10 Section IIA); `sample_size_reported_per_table` 14 (e.g. aer_112_2_1 p.16 Tables 1-9)

- **specification_reporting** (papers with the category: 23/32): `baseline_then_variants` 16 (e.g. aer_109_7_8 p.16 Table 3, panels A-C); `fe_listed_in_table` 16 (e.g. aer_109_7_8 p.16 Table 3 notes); `n_reported` 15 (e.g. aer_109_7_8 p.16 Tables 3 and 4); `mean_of_dependent_reported` 11 (e.g. aer_109_7_8 p.16 Tables 3 and 4)

- **variable_construction** (papers with the category: 27/32): `instrument_construction` 21 (e.g. aer_109_7_8 p.7 Section I, Verifying Random Assignment); `treatment_definition` 16 (e.g. aer_109_7_8 p.8 Section I, equations (1)-(2)); `outcome_definition` 14 (e.g. aer_109_7_8 p.10 Section IIA); `standardized_index` 8 (e.g. aer_110_2_5 p.10 Section I.C, footnote)

- **writing_structure** (papers with the category: 24/32): `results_previewed_in_intro` 22 (e.g. aer_109_7_8 p.3 Introduction); `contribution_paragraph` 20 (e.g. aer_109_7_8 p.3 Introduction); `roadmap_paragraph` 20 (e.g. aer_109_7_8 p.5 End of introduction and Section I); `appendix_heavy` 15 (e.g. aer_109_7_8 p.22 Section VI and surrounding online-append)

- **paper versus code** (concordance with recipe cards): bandwidth agree 3; bandwidth unknown 1; bandwidth code_only 1; bandwidth paper_only 1; cluster_level agree 20; cluster_level paper_only 7; cluster_level unknown 4; cluster_level code_only 1; comparison_group paper_only 14; comparison_group agree 1; controls paper_only 17; controls agree 9
<!-- reported-practice:end -->
