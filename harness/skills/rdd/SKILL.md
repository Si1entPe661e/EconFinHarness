---
name: rdd
description: "Regression discontinuity designs (sharp, fuzzy; sharp kink slope change as a narrow branch) for design, implementation, audit and explanation. Use when treatment changes at a threshold of an observed running variable. Do not use for difference-in-discontinuities or bunching estimands without the extra design assumptions, or when the running variable is chosen after treatment."
version: 0.2.1
kind: method
status: validated
---

# Regression discontinuity

## When to use

Use when treatment or eligibility changes at a predetermined cutoff of a running variable. Sharp RD targets the outcome jump at the cutoff; fuzzy RD targets the local Wald effect for compliers under continuity, exclusion and monotonicity. A policy kink needs a slope-based estimand. Use diff-in-disc for changes in discontinuities across periods and bunching for excess mass in a distribution.

## Inputs

Outcome, running variable, cutoff and assignment direction; treatment received for fuzzy RD; predetermined covariates, cluster identifier, weights if needed, and whether the running variable has discrete support or several cutoffs.

## Procedure

1. Define eligibility from the actual rule, including equality at the cutoff. Centre the running variable. Examine support, observations, distinct values and treatment rates on both sides.
2. Discuss continuity of untreated potential outcomes, sorting and other policies changing at the cutoff. A density rejection is a warning, not proof of manipulation; non-rejection is not proof of continuity.
3. Plot binned outcomes and treatment rates, and inspect heaping, gaps and cutoff mass. Test density and predetermined covariate continuity where the running-variable support makes those procedures appropriate.
4. Estimate a local linear RD with triangular kernel and a stated bandwidth rule. Report the conventional estimate together with bias-corrected robust inference, selected estimation/bias bandwidths and effective sample sizes. A global high-order polynomial is not a replacement.
5. For fuzzy RD, estimate the treatment jump on the same observations and bandwidth. The sign follows the coding of assignment and treatment; negative compliance orientation is not automatically invalid. Weak local first stages need weak-identification-aware inference.
6. Choose heteroskedastic or clustered inference from dependence and assignment. Count clusters inside the bandwidth. Discrete support needs support-aware inference; clustering by running-variable values alone does not solve approximation bias.
7. Vary bandwidths, polynomial order, predetermined covariate adjustment and justified donut exclusions. A donut changes the local sample and may require extrapolation to the cutoff. Explain sample or estimand changes.
8. Keep the conclusion local to the cutoff. Pool multiple cutoffs only with an explicit weighting and comparability argument; do not interpret a pooled jump as an unrestricted population ATE.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Software commands

[code-examples.md](code-examples.md) contains sharp/fuzzy rdrobust, rddensity, plotting and bandwidth sensitivity in R, plus Stata calls.

The existing [R template](templates/rd_analysis.R) is available when useful. Its support-count gates are local conventions, not universal thresholds; its positive-first-stage check requires treatment coding to match that orientation. Its kink branch estimates an outcome slope change only. A kink effect additionally requires the policy or treatment slope change and corresponding inference.

## Outputs and missing information

Return the estimate and interval, bandwidths, kernel/order, cutoff, effective observations on each side, first-stage jump if fuzzy, and RD plots. If support or compliance is insufficient, explain the limitation without treating a software output as a credible causal estimate.

Use [checklist.md](checklist.md) as needed.

## Evidence

Observed practice is generated into `harness/paradigms/rdd/observed.md`. The distillation set excludes the four held-out papers listed in `harness_build/evals/holdout/rdd.json` (aer_107_1_5, ecta_92_3_6, jpe_132_9_2, qje_140_1_11); they are reserved for evaluating this skill. At the time of writing the distillation set has 10 validated cards (ReStud 4, AER 3, JPE 1, QJE 1, RFS 1; all 10 with Stata code, 3 with R; coverage partial 9, minimal 1). Headline observations, each with artid and source-line pointers in `observed.md`:

- `rdrobust` is the estimation command in all 10 papers (estimators `local_polynomial_rd` 5, `local_linear_rd` 4); fuzzy designs through 2SLS commands appear once (`ivreghdfe`).
- Fuzzy designs are recorded in 4 papers, a kink design in 1, normalised multiple cutoffs in 1; the variant is unknown in 4.
- Standard errors are clustered in 5 papers and robust in 2; unknown in 3. Clustering dimensions are unknown in 7 of 10.
- Density tests: observed as calls in 2 papers, not found in the read scope in 2, unknown in 4. Bandwidth selection observed as calls in 3; alternative bandwidths recorded as robustness in 2 (one confirmed, one unresolved).
- Package attribution is known in 5 papers (all `rdrobust`); no card links RD specifications to table or figure outputs, so output conventions cannot be aggregated for RD yet.

These counts describe what the cards recorded, not what is correct; unknowns are not absence. The held-out cards (which include the only full-coverage RD card and the R-based RD inference paper) are available for the evaluation step, not for writing this skill.

<!-- reported-practice:begin -->
### Reported practice (paper texts; generated by `fhb papers skill-evidence`, 2026-09-09)

From 11 paper-practice notes (method rdd; `harness/paradigms/rdd/reported.md`, note hashes there). Counts are papers whose note carries the tag; an absent tag means the reader did not record it. Pointers are artid p.pages locator.

- **data_access** (papers with the category: 9/11): `administrative` 7 (e.g. aer_114_11_1 p.9 Section II); `data_restricted` 6 (e.g. aer_110_2_5 p.8 Section I.C); `linked_records` 5 (e.g. restud_2025_restud_rdae108 p.6 Sections 2.1-2.2; Data Appendices A-I); `public_use` 4 (e.g. aer_114_11_1 p.9 Section II)

- **design_statement** (papers with the category: 9/11): `design_variant_named` 9 (e.g. aer_110_2_5 p.10 Section II.A); `threats_discussed` 9 (e.g. aer_110_2_5 p.11 Section II.A); `continuity_at_cutoff_argued` 8 (e.g. aer_110_2_5 p.10 Section II.A); `estimand_named` 8 (e.g. aer_110_2_5 p.10 Section II.A)

- **diagnostic_reported** (papers with the category: 11/11): `in_appendix` 10 (e.g. aer_110_2_5 p.16 Section III.A, referencing Appendix Figu); `balance_table` 9 (e.g. aer_110_2_5 p.13 Table 1); `density_test` 9 (e.g. aer_110_2_5 p.16 Section III.A, referencing Appendix Figu); `in_main_text` 9 (e.g. aer_110_2_5 p.13 Table 1)

- **external_validity** (papers with the category: 8/11): `site_specific` 7 (e.g. aer_110_2_5 p.3 Introduction); `compliers_vs_population` 5 (e.g. aer_114_11_1 p.3 Introduction); `scaling_discussed` 3 (e.g. aer_114_11_1 p.38 Section VI, Conclusion); `in_appendix` 1 (e.g. restud_2025_restud_rdae108 p.26 Sections 4.4.1-4.4.3; Appendix Tables E.)

- **heterogeneity_reported** (papers with the category: 5/11): `split_sample` 5 (e.g. aer_114_11_1 p.35 Table 6); `exploratory_labelled` 3 (e.g. aer_114_11_1 p.27 Section IV.D); `interaction` 3 (e.g. aer_114_11_1 p.26 Table 4); `mechanism_motivated` 3 (e.g. qje_2026_qje_qjaf045 p.47 Table VII)

- **inference_justification** (papers with the category: 8/11): `multiple_testing_adjustment` 4 (e.g. aer_114_11_1 p.31 footnote 36); `no_justification_found` 4 (e.g. jpe_2026_740226 p.17 Table 1 note); `cluster_at_unit_level` 3 (e.g. qje_2026_qje_qjaf045 p.19 Section III.B.1); `randomization_inference` 2 (e.g. restud_2025_restud_rdae108 p.2 Introduction; Section 4.3.3; Appendix F)

- **limitation_stated** (papers with the category: 7/11): `interpretation_caveat` 6 (e.g. aer_114_11_1 p.37 Section V.B); `identification_caveat` 5 (e.g. aer_110_2_5 p.27 Section III.G, Stigma of Disease); `measurement` 5 (e.g. aer_110_2_5 p.19 Section III.C, footnote 32); `data_coverage` 4 (e.g. aer_110_2_5 p.23 Section III.E)

- **magnitude_interpretation** (papers with the category: 8/11): `compared_to_literature` 5 (e.g. aer_114_11_1 p.31 Section V.A); `relative_to_mean` 5 (e.g. aer_114_11_1 p.20 Section IV.B); `back_of_envelope` 4 (e.g. aer_110_2_5 p.39 Appendix A); `cost_benefit` 3 (e.g. aer_110_2_5 p.39 Appendix A)

- **mechanism_evidence** (papers with the category: 7/11): `intermediate_outcomes` 6 (e.g. aer_110_2_5 p.20 Sections III.C-D); `model_guided` 5 (e.g. aer_110_2_5 p.39 Appendix A, back-of-the-envelope calcula); `ruled_out_alternatives` 5 (e.g. aer_114_11_1 p.33 Sections V.B, V.D); `suggestive_labelled` 4 (e.g. jpe_2026_740226 p.33 Table 5)

- **other** (papers with the category: 2/11): `in_footnote` 1 (e.g. restud_2025_restud_rdae108 p.8 footnotes 9, 14, 15, 16, 20, 23, 24); `other:evidence available upon request` 1 (e.g. restud_2025_restud_rdaf004 p.25 Section 6.2 fn. 56); `other:reviewer_facing_footnotes` 1 (e.g. restud_2025_restud_rdae108 p.8 footnotes 9, 14, 15, 16, 20, 23, 24)

- **preregistration_or_ethics** (papers with the category: 2/11): `irb_stated` 2 (e.g. jpe_2026_740226 p.1 Acknowledgments footnote)

- **presentation_convention** (papers with the category: 10/11): `coefficient_plot` 9 (e.g. aer_114_11_1 p.25 Figures 3-4); `rd_plot` 8 (e.g. aer_110_2_5 p.11 Figure 2 notes); `notes_state_se` 7 (e.g. aer_114_11_1 p.13 Table 1 notes); `appendix_tables_numbered_a` 6 (e.g. aer_114_11_1 p.16 footnote 14, throughout)

- **replication_statement** (papers with the category: 9/11): `replication_package_cited` 8 (e.g. aer_114_11_1 p.42 References); `code_public` 6 (e.g. jpe_2026_740226 p.44 Data Availability statement); `software_named` 5 (e.g. aer_110_2_5 p.10 Section II.A footnote; Section III.F); `data_access_procedure_described` 4 (e.g. jpe_2026_740226 p.44 Data Availability statement)

- **robustness_reported** (papers with the category: 9/11): `in_appendix` 9 (e.g. aer_110_2_5 p.24 Section III.F, BSP Boundary Definition; ); `alt_specification` 7 (e.g. aer_114_11_1 p.29 Section IV.E, Financing); `alt_sample` 6 (e.g. aer_114_11_1 p.22 footnote 24); `alt_bandwidth` 5 (e.g. aer_110_2_5 p.18 Section III.B; Tables 3, 4, 6, 7, 8)

- **sample_construction** (papers with the category: 9/11): `data_source_named` 9 (e.g. aer_110_2_5 p.8 Section I.C); `sample_period_stated` 9 (e.g. aer_110_2_5 p.7 Section I.C); `sample_size_reported_per_table` 9 (e.g. aer_110_2_5 p.16 Tables 2-8); `exclusions_justified` 8 (e.g. aer_110_2_5 p.23 Section III.E, discussion of Table 3 pan)

- **specification_reporting** (papers with the category: 8/11): `n_reported` 7 (e.g. aer_110_2_5 p.16 Tables 2-8); `baseline_then_variants` 6 (e.g. aer_110_2_5 p.17 Table 3 layout); `mean_of_dependent_reported` 6 (e.g. aer_110_2_5 p.16 Tables 2-8); `se_type_in_notes` 6 (e.g. aer_110_2_5 p.16 Notes to Tables 2-8)

- **variable_construction** (papers with the category: 9/11): `running_variable_definition` 9 (e.g. aer_110_2_5 p.12 Section II.B, equation (1)); `treatment_definition` 9 (e.g. aer_110_2_5 p.10 Section II.A); `outcome_definition` 7 (e.g. aer_110_2_5 p.12 Section II.B and Tables 3, 8); `standardized_index` 6 (e.g. aer_110_2_5 p.10 Section I.C, footnote)

- **writing_structure** (papers with the category: 9/11): `results_previewed_in_intro` 9 (e.g. aer_110_2_5 p.2 Introduction); `appendix_heavy` 8 (e.g. aer_110_2_5 p.24 Section III.F); `contribution_paragraph` 8 (e.g. aer_110_2_5 p.3 Introduction); `mechanisms_after_main` 8 (e.g. aer_110_2_5 p.4 Sections I-IV)

- **paper versus code** (concordance with recipe cards): bandwidth agree 7; bandwidth paper_only 2; bandwidth unknown 1; cluster_level agree 5; cluster_level paper_only 3; cluster_level unknown 1; comparison_group paper_only 4; comparison_group agree 1; controls paper_only 4; controls agree 3; controls unknown 1; controls disagree 1
<!-- reported-practice:end -->
