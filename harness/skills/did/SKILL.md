---
name: did
description: Difference-in-differences and event-study designs (two-period, staggered adoption, triple difference, synthetic DID) for design, implementation, audit and explanation. Use when treatment turns on for some units at known times and untreated or not-yet-treated units serve as comparison. Do not use for designs without a pre-period or when treatment timing is chosen in response to outcomes.
version: 0.1.0
kind: method
status: draft
---

# did

Method skill for difference-in-differences (DID) and event studies. It covers the two-period case, staggered adoption with heterogeneity-robust estimators, triple differences, synthetic DID as a related branch, and the inference and pre-trend diagnostics that go with them. Observed corpus practice (`harness/paradigms/did/observed.md`, 24 cards; `harness/paradigms/event_study/observed.md`, 10 cards) is kept separate from recommendations (`harness/paradigms/did/recommendations.md`, draft).

## When to use

- Some units become treated at known dates; others are never treated or treated later; outcomes are observed before and after.
- Event-study versions: effects by time relative to treatment, with leads as pre-trend evidence.
- Staggered adoption: treatment dates differ across cohorts; the choice of estimator (two-way fixed effects versus heterogeneity-robust estimators) is a design decision to record.
- Roles: empirical-analyst (estimand, comparison group, estimator choice, inference plan), code-engineer (implementation), reviewer (audit), explainer.

## When not to use

- No pre-treatment periods, or treatment timing responds to the outcome path (anticipation or endogenous timing without a design argument).
- The comparison group is defined by a discontinuity (use `rdd` or difference-in-discontinuities) or by an instrument (use `iv`).
- Single treated unit with many controls and long pre-periods: synthetic control is the closer branch; synthetic DID is covered here only as a related estimator.

## Inputs required

- Panel or repeated cross-section description: unit, time, treatment timing per unit, never-treated and not-yet-treated groups, balance of the panel.
- Target estimand: ATT overall, by cohort, by relative time; the comparison group used to identify it.
- Cluster structure (assignment level), weights, covariates and their timing.
- For audit: relevant code, available environment details, analysis choices and outputs.

## Procedure

1. Write the estimand and comparison group. Overall ATT, cohort-time ATTs, or dynamic effects by relative time; comparison from never-treated, not-yet-treated, or both. Record whether the design has one adoption date (two-way fixed effects is a natural estimator) or staggered adoption with possibly heterogeneous effects (two-way fixed effects can weight some comparisons negatively; choose a heterogeneity-robust estimator or justify TWFE).
2. Build the treatment variables explicitly: cohort (first treatment period), relative time, post indicator; define the never-treated cohort code the estimator expects. Check that units switch on once (no reversals) or document reversals and choose an estimator that handles them.
3. Run the panel checks (`panel-data-checks`): unit-time uniqueness, balance, singleton units, treatment timing consistency across periods, the number of treated cohorts and the sample size per relative time.
4. Choose the estimator and record the choice: TWFE with leads and lags (binned endpoints, a stated reference period); Callaway-Sant'Anna group-time ATTs; Sun-Abraham interaction-weighted event study; de Chaisemartin-D'Haultfoeuille; Borusyak-Jaravel-Spiess imputation; stacked regression; synthetic DID. State the reference period and how endpoints are binned. Use a Goodman-Bacon decomposition as a diagnostic when TWFE is reported for staggered designs.
5. Inference: cluster at the level of treatment assignment (state, firm, district) and pass the cluster variable into the estimation call; report the number of clusters; with few clusters plan a wild cluster bootstrap or randomization inference. For multi-way dependence, state the rationale.
6. Diagnostics with decision rules written before estimation: pre-trend plot and test on leads (report both, with the caution that pre-testing changes inference), balance of covariates between treated and comparison units, heterogeneous treatment effect diagnostics for staggered designs (Bacon weights, comparison of TWFE with a robust estimator), sensitivity to parallel-trend violations (HonestDiD-style bounds) where the plan calls for it.
7. Robustness: alternative comparison group (never-treated only), alternative estimator, sample restrictions (drop always-treated, trim relative-time window), alternative fixed effects (unit and time versus unit-specific trends), alternative clustering.
8. Outputs from code: event-study plot with the reference period marked and confidence bands; tables with N, clusters, fixed effects, SE type, weights and the estimator; every column mapped to a plan specification id; JSON with the estimator options.

### Software commands

Use [code-examples.md](code-examples.md) for complete calls and the required variables. Choose the sample, comparison group, weights and inference settings for the current research design.

- R: `fe3 = felm(allunits~Before+After+Chain|as.factor(BUYER_ZIP)+as.factor(Date)|0|BUYER_ZIP, data=d)` after loading `lfe`. The examples also cover `feols` TWFE and `sunab` event studies, `att_gt` and `aggte`, `synthdid_estimate`, and `bacondecomp::bacon`.
- Stata: `did_imputation trade bvd_id year Ei, fe(bvd_id year year#country_num) autosample cluster(BankID_num) tol(0.1)`. The examples also cover `reghdfe`, `eventstudyinteract`, `csdid` and `csdid_estat event`, dynamic imputation with `pretrends(18)`, legacy `did_multiplegt`, nonlinear `jwdid`, `bacondecomp`, and `honestdid`.
- Python: `model = PanelOLS(y, X, entity_effects=True, time_effects=True, drop_absorbed=True)` followed by `result = model.fit(cov_type='clustered', cluster_entity=True)`. The example includes imports, the panel index and the treatment-by-post regressor.

The option is `pretrends()`. Legacy `did_multiplegt` options require the matching interface; `did_multiplegt_dyn` uses different arguments.

## Missing information

- Treatment timing missing for some units: exclude them and record it as a sample restriction with the count, or treat as never-treated only with a stated reason.
- Unclear assignment level: report the clustering choice as unresolved and give two alternatives in the plan.
- No never-treated units: use not-yet-treated comparisons and say that long-run effects are not identified for the last cohort.
- Corpus card fields null: unknown, never "not done".

## Checklist

See `checklist.md`.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Evidence

Observed practice is generated into `harness/paradigms/did/observed.md` (distillation set: 17 cards, ReStud 6, AER 4, QJE 3, RFS 2, Econometrica 1, JFE 1; Stata code in 15, R in 9) and `harness/paradigms/event_study/observed.md`. Seven papers are held out (`examples/exclusions/did.json`: aer_110_9_10, aer_113_3_7, aer_114_6_6, aer_115_3_8, restud_90_5_11, restud_92_2_14, rfs_2025_rfs_hhaf065) and are not used here. Headline observations with pointers in `observed.md`:

- Two-way fixed-effects OLS (`hdfe_ols`, mostly `reghdfe`) is the recorded estimator in 12 of 17 cards; heterogeneity-robust estimators appear as `did_group_time_att` (3: `csdid`, `att_gt`, `jwdid`), `did_imputation` (3), `did_multiplegt` (1), synthetic DID (2, one of them the method paper's own code).
- Standard errors are clustered in 14 of 17 cards (one dimension in all 14); bootstrap in 1 and randomization inference in 1; unknown in 2.
- Fixed-effect dimensions: two in 6 cards, three or more in 2, one in 1; unknown in 8.
- Pre-trend tests are observed as calls in 4 cards, not found in the read scope in 1, unknown in 1; pre-trend plots observed in 2; heterogeneous-treatment-effect diagnostics observed in 2, unknown in 1. Diagnostics are recorded for 9 of the 17 cards only.
- Design variants are unknown in 15 of 17 (`staggered` 1, `synthetic_did` 1); design roles are unknown in 16 of 17, so main versus robustness status cannot be aggregated. Table export packages are known in 3 cards (esttab/estout).

These counts describe what the cards recorded; unknowns are not absence.

<!-- reported-practice:begin -->
### Reported practice (paper texts; generated by `fhb papers skill-evidence`, 2026-09-09)

From 32 paper-practice notes (method did; `harness/paradigms/did/reported.md`, note hashes there). Counts are papers whose note carries the tag; an absent tag means the reader did not record it. Pointers are artid p.pages locator.

- **data_access** (papers with the category: 27/32): `administrative` 25 (e.g. aer_111_12_2 p.1 Acknowledgments and Section IB); `data_restricted` 19 (e.g. aer_111_12_2 p.1 Acknowledgments and Section IB); `commercial` 10 (e.g. aer_113_1_1 p.26 Section V.B); `linked_records` 9 (e.g. jpe_2026_740222 p.14 Section III.A, Ownership and acquisition)

- **design_statement** (papers with the category: 32/32): `design_variant_named` 30 (e.g. aer_111_12_2 p.1 Abstract and Introduction); `threats_discussed` 25 (e.g. aer_111_12_2 p.18 Section IIIA, Empirical Strategy); `parallel_trends_argued` 22 (e.g. aer_114_11_7 p.17 Section II.B and Section III.D); `identifying_assumption_explicit` 21 (e.g. aer_111_12_2 p.18 Section IIIA, Empirical Strategy)

- **diagnostic_reported** (papers with the category: 28/32): `in_main_text` 24 (e.g. aer_111_12_2 p.20 Section IIIA and Figure 3); `pre_trends_plot` 20 (e.g. aer_111_12_2 p.21 Figure 3 and Figure 4, panel B); `in_appendix` 19 (e.g. aer_111_12_2 p.23 Section IIIB, footnote referencing appen); `balance_table` 12 (e.g. aer_111_12_8 p.7 Figure 1, bottom panel)

- **external_validity** (papers with the category: 24/32): `site_specific` 17 (e.g. aer_111_12_2 p.31 Section IIIC); `scaling_discussed` 13 (e.g. aer_111_12_2 p.31 Section IIIC); `time_period_specific` 7 (e.g. aer_113_1_1 p.17 Section IV.B); `compliers_vs_population` 3 (e.g. jpe_132_9_2 p.7 Section II-III)

- **heterogeneity_reported** (papers with the category: 23/32): `split_sample` 19 (e.g. aer_111_12_2 p.24 Section IIIB, footnote referencing appen); `mechanism_motivated` 17 (e.g. aer_114_11_7 p.38 Tables 11-12); `interaction` 9 (e.g. aer_114_11_7 p.38 Tables 11-12); `in_appendix` 7 (e.g. aer_111_12_2 p.24 Section IIIB, footnote referencing appen)

- **inference_justification** (papers with the category: 27/32): `cluster_at_unit_level` 18 (e.g. aer_111_12_2 p.19 Section IIIA, footnote); `no_justification_found` 17 (e.g. aer_111_12_2 p.19 Section IIIA, footnote); `cluster_at_assignment_level` 9 (e.g. aer_114_11_7 p.19 Table 3, Table 4, and Table 9 notes); `in_footnote` 4 (e.g. restud_2025_restud_rdae091 p.15 Footnote 9)

- **limitation_stated** (papers with the category: 25/32): `identification_caveat` 17 (e.g. aer_111_12_2 p.18 Section IIIA, footnote); `interpretation_caveat` 16 (e.g. aer_113_1_1 p.17 Section IV.B); `data_coverage` 14 (e.g. aer_111_12_2 p.10 Section IB, footnote); `measurement` 14 (e.g. aer_113_1_1 p.26 Section V.B, footnote 21)

- **magnitude_interpretation** (papers with the category: 27/32): `relative_to_mean` 23 (e.g. aer_111_12_2 p.23 Table 1, column 7; Section IIIB); `compared_to_literature` 15 (e.g. aer_111_12_2 p.23 Table 1, column 7; Section IIIB); `back_of_envelope` 13 (e.g. aer_111_12_2 p.40 Section IVC, Table 7); `precision_discussed` 11 (e.g. jfe_2026_j_jfineco_2025_104223 p.9 throughout Section 4)

- **mechanism_evidence** (papers with the category: 20/32): `intermediate_outcomes` 16 (e.g. aer_111_12_2 p.25 Section IIIB, Mechanisms subsection and ); `suggestive_labelled` 15 (e.g. aer_111_12_2 p.8 Section IA, footnote); `ruled_out_alternatives` 11 (e.g. aer_111_12_2 p.25 Section IIIB, Mechanisms subsection and ); `model_guided` 10 (e.g. aer_111_12_2 p.29 Section IIIC, Figure 7 and Tables 4 and )

- **other** (papers with the category: 5/32): `in_footnote` 1 (e.g. restud_90_5_13 p.25 Section 5.1; footnote 29); `in_main_text` 1 (e.g. restud_90_5_13 p.25 Section 5.1; footnote 29); `other:descriptive_regression_of_loan_terms` 1 (e.g. rfs_2026_rfs_hhaf080 p.14 Table 2, Section 2.2.2 and 2.2.3); `other:full_control_list_in_every_note` 1 (e.g. restud_2026_restud_rdaf071 p.12 Table 2, Figure 2, Figure 3, Table 5, Fi)

- **preregistration_or_ethics** (papers with the category: 3/32): `irb_stated` 2 (e.g. jpe_2026_740226 p.1 Acknowledgments footnote); `other:funding_and_disclaimer_stated` 1 (e.g. restud_2026_restud_rdaf027 p.37 Acknowledgments)

- **presentation_convention** (papers with the category: 30/32): `notes_state_se` 20 (e.g. aer_111_12_2 p.20 Figures 3, 4, and 6); `coefficient_plot` 19 (e.g. aer_114_11_7 p.27 Figures 1-2); `event_study_figure` 18 (e.g. aer_111_12_2 p.20 Figures 3, 4, and 6); `notes_state_sample` 18 (e.g. aer_111_12_2 p.20 Figures 3, 4, and 6)

- **replication_statement** (papers with the category: 26/32): `replication_package_cited` 26 (e.g. aer_111_12_2 p.43 References); `code_public` 17 (e.g. ecta_2024_ecta19872 p.1 Author note (page 1) and editorial state); `data_public` 13 (e.g. aer_114_11_7 p.43 References list); `data_access_procedure_described` 7 (e.g. jpe_132_9_2 p.33 Data Availability statement)

- **robustness_reported** (papers with the category: 28/32): `in_appendix` 26 (e.g. aer_111_12_2 p.27 Section IIIB, Robustness paragraph); `alt_sample` 21 (e.g. aer_111_12_2 p.28 Section IIIB, Robustness paragraph); `alt_specification` 20 (e.g. aer_111_12_2 p.27 Section IIIB, Robustness paragraph); `alt_estimator` 18 (e.g. aer_111_12_2 p.27 Section IIIB, Robustness paragraph)

- **sample_construction** (papers with the category: 28/32): `data_source_named` 26 (e.g. aer_111_12_2 p.10 Section IB, Data); `exclusions_justified` 25 (e.g. aer_111_12_2 p.18 Section IIIA, discussion of office waves); `sample_period_stated` 25 (e.g. aer_111_12_2 p.10 Section IB, Data); `unit_of_observation_stated` 23 (e.g. aer_111_12_8 p.9 Section II.A, Data Generating Process)

- **specification_reporting** (papers with the category: 25/32): `cluster_level_in_notes` 21 (e.g. aer_111_12_2 p.30 Tables 4 and 5); `fe_listed_in_table` 21 (e.g. aer_111_12_2 p.30 Tables 4 and 5); `se_type_in_notes` 21 (e.g. aer_111_12_8 p.6 Table 1 and notes); `n_reported` 18 (e.g. aer_111_12_2 p.22 Table 1)

- **variable_construction** (papers with the category: 27/32): `outcome_definition` 23 (e.g. aer_111_12_2 p.22 Table 1 notes); `treatment_definition` 20 (e.g. aer_113_1_1 p.10 Section III, equation (2)); `measurement_error_discussed` 14 (e.g. aer_114_11_7 p.23 Table 4 discussion, footnote 44); `logs_or_ihs` 10 (e.g. aer_114_11_7 p.16 Section II.B, control variable discussio)

- **writing_structure** (papers with the category: 28/32): `results_previewed_in_intro` 27 (e.g. aer_111_12_2 p.2 Introduction); `contribution_paragraph` 25 (e.g. aer_111_12_2 p.2 Introduction); `appendix_heavy` 22 (e.g. aer_111_12_2 p.27 Sections IIIB and IVB); `roadmap_paragraph` 20 (e.g. aer_111_12_2 p.2 Introduction)

- **paper versus code** (concordance with recipe cards): bandwidth agree 3; bandwidth paper_only 2; bandwidth code_only 1; cluster_level agree 24; cluster_level paper_only 10; cluster_level unknown 3; cluster_level code_only 1; cluster_level disagree 1; comparison_group paper_only 16; comparison_group agree 2; controls agree 12; controls paper_only 11
<!-- reported-practice:end -->

## Templates

- None tested yet. The RD template shows the intended structure (prepare, estimate with explicit options, diagnostics, report); a DID template with synthetic staggered data and a planted negative-weight case is the next milestone item.
