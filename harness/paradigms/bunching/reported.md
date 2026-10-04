# Reported practice: `bunching` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 5 paper notes (5 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | AER: 2, ReStud: 2, Econometrica: 1 |
| year | 2021: 1, 2022: 1, 2025: 1, 2026: 2 |
| papers with at least one observation in category | design_statement: 5, presentation_convention: 5, sample_construction: 4, variable_construction: 4, diagnostic_reported: 4, robustness_reported: 4, mechanism_evidence: 4, writing_structure: 4, replication_statement: 4, inference_justification: 3, heterogeneity_reported: 3, magnitude_interpretation: 3, limitation_stated: 3, data_access: 3, specification_reporting: 2, external_validity: 2 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_111_4_3 | AER | 2021 | full | yes | 500f457d1b91 |
| aer_112_10_8 | AER | 2022 | full | yes | df1a1baa7d3d |
| ecta_2025_ecta22303 | Econometrica | 2025 | full | yes | e8342e263d9f |
| restud_2026_restud_rdag037 | ReStud | 2026 | full | yes | 23b104741be7 |
| restud_2026_restud_rdag071 | ReStud | 2026 | full | yes | 99224bf0681d |

## Practices by category and tag


### data_access (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 3 | 60% | aer_111_4_3 p.11-11 Section I.D: Survey data are merged onto the administrative pension records at an aggregated occupation level to add worker; ecta_2025_ecta22303 p.7-8 Section 2.2: The underlying data are described as administrative program records assembled during loan underwriting, includ |
| `data_restricted` | 2 | 40% | aer_111_4_3 p.1-1 Title footnote: A title-page footnote directs readers to the journal's article page for additional materials and an author dis; ecta_2025_ecta22303 p.7-8 Section 2.2: The underlying data are described as administrative program records assembled during loan underwriting, includ |
| `linked_records` | 2 | 40% | aer_111_4_3 p.11-11 Section I.D: Survey data are merged onto the administrative pension records at an aggregated occupation level to add worker; restud_2026_restud_rdag037 p.7-9 Section 3: Data are public administrative releases (USSC, EOUSA case files, state inmate records, seizure systems) and na |
| `data_access_procedure_described` | 1 | 20% | aer_111_4_3 p.1-1 Title footnote: A title-page footnote directs readers to the journal's article page for additional materials and an author dis |
| `public_use` | 1 | 20% | restud_2026_restud_rdag037 p.7-9 Section 3: Data are public administrative releases (USSC, EOUSA case files, state inmate records, seizure systems) and na |
| `survey_collected` | 1 | 20% | restud_2026_restud_rdag037 p.7-9 Section 3: Data are public administrative releases (USSC, EOUSA case files, state inmate records, seizure systems) and na |

### design_statement (papers with this category: 5/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 4 | 80% | aer_111_4_3 p.13-20 Section II.B and Section III.B, equations (3) and (5): The paper frames its central estimand as the direct behavioral effect of statutory retirement ages on bunching; ecta_2025_ecta22303 p.14-15 Section 3.2: The paper names its preferred design a difference-in-bunching estimator and explicitly frames it as similar to |
| `identifying_assumption_explicit` | 4 | 80% | aer_111_4_3 p.13-14 Section II.B: Two explicit, numbered identifying assumptions (labeled Assumption A and Assumption B) are stated, requiring t; aer_112_10_8 p.9-23 Section I.B footnote; Section III.C Fact 3: The reference point for loss aversion is assumed to equal the nominal original purchase price throughout, an a |
| `threats_discussed` | 4 | 80% | aer_111_4_3 p.13-22 Sections II.B and III.C: The authors discuss as a threat to identification that observed differences in bunching across discontinuity t; ecta_2025_ecta22303 p.17-18 Section 3.3: Authors state the identifying assumption that, within the bunching region, disaster loss size is plausibly ind |
| `estimand_named` | 3 | 60% | aer_111_4_3 p.13-20 Section II.B and Section III.B, equations (3) and (5): The paper frames its central estimand as the direct behavioral effect of statutory retirement ages on bunching; ecta_2025_ecta22303 p.14-15 Section 3.2: The paper names its preferred design a difference-in-bunching estimator and explicitly frames it as similar to |
| `other:multi_discontinuity_bunching` | 1 | 20% | aer_111_4_3 p.13-13 Section II.B: The approach is named as a multi-discontinuity extension of the standard bunching estimator, distinguishing th |
| `other:smooth_counterfactual_density_argued` | 1 | 20% | aer_111_4_3 p.13-13 Section II.A, footnote: Identification of bunching itself rests on an explicitly stated assumption that the retirement-age density wou |
| `parallel_trends_argued` | 1 | 20% | ecta_2025_ecta22303 p.15-16 Section 3.2, Figure 6: The event-study-style bunching plot is used as an internal placebo check: loan amounts for borrowers whose pre |

### diagnostic_reported (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 3 | 60% | aer_111_4_3 p.24-26 Section IV.A-B: Two policy reforms are used as quasi-diagnostic checks on the proposed mechanism, examining whether bunching s; ecta_2025_ecta22303 p.9-9 Section 2.2, Figure 3: A figure showing that loan approval and offered interest rates are smooth through the collateral threshold is  |
| `density_test` | 2 | 40% | aer_112_10_8 p.22-23 Figure 6; Section III.C: Excess bunching mass at the reference point is quantified against an explicit counterfactual distribution buil; restud_2026_restud_rdag037 p.22-23 Section 5.3, Figure A11: The paper checks that the pre-reform share of cases in the future bunching bin is stable near zero across year |
| `in_appendix` | 2 | 40% | aer_111_4_3 p.22-34 text references to online Appendix Figures A5 and A12: Additional diagnostic exercises, including density comparisons split by statutory-age type and sensitivity of ; restud_2026_restud_rdag037 p.22-23 Section 5.3, Figure A11: The paper checks that the pre-reform share of cases in the future bunching bin is stable near zero across year |
| `other:bunching_counterfactual` | 1 | 20% | aer_112_10_8 p.22-23 Figure 6; Section III.C: Excess bunching mass at the reference point is quantified against an explicit counterfactual distribution buil |
| `other:reform_based_placebo_check` | 1 | 20% | aer_111_4_3 p.24-26 Section IV.A-B: Two policy reforms are used as quasi-diagnostic checks on the proposed mechanism, examining whether bunching s |
| `other:smoothness_check` | 1 | 20% | ecta_2025_ecta22303 p.9-9 Section 2.2, Figure 3: A figure showing that loan approval and offered interest rates are smooth through the collateral threshold is  |
| `placebo_outcomes` | 1 | 20% | restud_2026_restud_rdag037 p.16-17 Figure 2a and notes: Distributional equality by race in the pre-reform window is tested with a Kolmogorov-Smirnov test, shown as ov |
| `pre_trends_plot` | 1 | 20% | ecta_2025_ecta22303 p.15-16 Section 3.2, Figure 6: The difference-in-bunching coefficient plot with confidence intervals is used to display a precisely estimated |

### external_validity (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 2 | 40% | ecta_2025_ecta22303 p.37-37 Section 6, footnote 36: The conclusion explicitly cautions that the specific magnitudes of collateral aversion may not generalize acro; restud_2026_restud_rdag037 p.12-31 footnote 9, Table A2, Section 5.5.3: The author argues the setting is chosen for identification but notes bunching disparities appear for other dru |
| `site_specific` | 2 | 40% | ecta_2025_ecta22303 p.5-6 Section 1: The authors explicitly discuss that their sample of households who recently experienced a disaster is a distin; restud_2026_restud_rdag037 p.12-31 footnote 9, Table A2, Section 5.5.3: The author argues the setting is chosen for identification but notes bunching disparities appear for other dru |

### heterogeneity_reported (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `mechanism_motivated` | 3 | 60% | aer_111_4_3 p.22-28 Sections III.C and IV.C: The heterogeneity analysis is framed as a check on the identifying assumption and on alternative behavioral me; ecta_2025_ecta22303 p.28-30 Section 5.1.2: Bunching behavior is examined across bins of an existing-mortgage leverage ratio to argue for a role of nonfin |
| `exploratory_labelled` | 2 | 40% | aer_111_4_3 p.27-27 Section IV.C, footnote: Results from heterogeneity by financial-sophistication proxies are explicitly described as sensitive to the ch; ecta_2025_ecta22303 p.26-28 Section 5.1.1: Subgroup comparisons around the bunching threshold by ex ante creditworthiness and income are presented as des |
| `interaction` | 2 | 40% | aer_111_4_3 p.22-23 Section III.C, Figure 5: Heterogeneity in observed bunching elasticities is reported by sorting discontinuities into quintiles of resid; restud_2026_restud_rdag037 p.24-26 Table 7, Figure 4: Heterogeneity is estimated by fully interacting the race model with binary offender or district characteristic |
| `split_sample` | 2 | 40% | ecta_2025_ecta22303 p.26-28 Section 5.1.1: Subgroup comparisons around the bunching threshold by ex ante creditworthiness and income are presented as des; restud_2026_restud_rdag037 p.24-26 Table 7, Figure 4: Heterogeneity is estimated by fully interacting the race model with binary offender or district characteristic |
| `quantile` | 1 | 20% | aer_111_4_3 p.22-23 Section III.C, Figure 5: Heterogeneity in observed bunching elasticities is reported by sorting discontinuities into quintiles of resid |

### inference_justification (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_justification_found` | 2 | 40% | aer_111_4_3 p.15-17 Figure 3 notes: For the specific-discontinuity comparison figures earlier in the results section, standard errors shown in par; restud_2026_restud_rdag037 p.12-13 Table 2 notes, Section 5.1.1: Robust standard errors are used for the main specification without an explicit rationale in the text; alternat |
| `cluster_at_assignment_level` | 1 | 20% | ecta_2025_ecta22303 p.15-16 Section 3.2: Standard errors for the bunching-based estimates are block-bootstrapped at the disaster level, justified expli |
| `cluster_at_unit_level` | 1 | 20% | restud_2026_restud_rdag037 p.19-20 Section 5.2.3, Table 5 notes: For prosecutor-level regressions, standard errors are clustered at the prosecutor level (the unit whose classi |
| `few_clusters_addressed` | 1 | 20% | restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Figure A4a: Because the post-reform white subsample is small, the author runs a placebo exercise reassigning white offende |
| `other:bootstrap_for_generated_regressor` | 1 | 20% | restud_2026_restud_rdag037 p.19-20 Section 5.2.3, Table 5 notes: For prosecutor-level regressions, standard errors are clustered at the prosecutor level (the unit whose classi |
| `other:joint_test_over_bins` | 1 | 20% | restud_2026_restud_rdag037 p.16-17 Section 5.1.3, Figure 2b notes: When many narrow-bin coefficients are individually noisy, the author reports a joint test over the contiguous  |
| `randomization_inference` | 1 | 20% | restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Figure A4a: Because the post-reform white subsample is small, the author runs a placebo exercise reassigning white offende |

### limitation_stated (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identification_caveat` | 3 | 60% | aer_111_4_3 p.38-38 Section VII: The conclusion explicitly states that the paper remains agnostic about the welfare consequences of policies th; ecta_2025_ecta22303 p.15-15 Section 3.2: The authors state that the difference-in-bunching approach is limited to households whose losses fall below th |
| `data_coverage` | 2 | 40% | aer_111_4_3 p.28-28 Section IV.C: The authors state that the role of liquidity constraints at the early retirement age cannot be fully verified ; restud_2026_restud_rdag037 p.18-19 Section 5.2.2 and 5.2.3, Figure 3 notes: Limitations of the prosecutor files are stated: no race field, many missing quantities, and small caseloads pe |
| `interpretation_caveat` | 2 | 40% | aer_111_4_3 p.38-38 Section VII: The conclusion explicitly states that the paper remains agnostic about the welfare consequences of policies th; restud_2026_restud_rdag037 p.2-24 Section 1, Section 5.4: The paper clarifies it is not an evaluation of the reform, that the results do not imply discretion began afte |
| `measurement` | 2 | 40% | ecta_2025_ecta22303 p.18-19 Section 3.4.2: The original-request proxy for a household's ideal loan amount is flagged as requiring imputation for early bu; restud_2026_restud_rdag037 p.18-19 Section 5.2.2 and 5.2.3, Figure 3 notes: Limitations of the prosecutor files are stated: no race field, many missing quantities, and small caseloads pe |
| `power` | 1 | 20% | ecta_2025_ecta22303 p.29-30 Section 5.1.2: Null results for two proxies intended to capture school-aged-children considerations are explicitly labeled in |
| `selection` | 1 | 20% | ecta_2025_ecta22303 p.18-19 Section 3.4.2: The original-request proxy for a household's ideal loan amount is flagged as requiring imputation for early bu |

### magnitude_interpretation (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `back_of_envelope` | 2 | 40% | ecta_2025_ecta22303 p.3-3 Section 1, footnote 1: The back-of-envelope net-present-value translation of collateral aversion is benchmarked against an independen; restud_2026_restud_rdag037 p.31-32 Section 5.5.3, Table A21: A back-of-envelope exercise converts sentencing effects into sentence-years and dollar costs using a per-year  |
| `compared_to_literature` | 2 | 40% | aer_111_4_3 p.23-23 Section III.A: The estimated retirement-age elasticity with respect to financial incentives is explicitly benchmarked against; ecta_2025_ecta22303 p.3-3 Section 1, footnote 1: The back-of-envelope net-present-value translation of collateral aversion is benchmarked against an independen |
| `cost_benefit` | 1 | 20% | restud_2026_restud_rdag037 p.31-32 Section 5.5.3, Table A21: A back-of-envelope exercise converts sentencing effects into sentence-years and dollar costs using a per-year  |
| `monetary_terms` | 1 | 20% | restud_2026_restud_rdag037 p.31-32 Section 5.5.3, Table A21: A back-of-envelope exercise converts sentencing effects into sentence-years and dollar costs using a per-year  |
| `precision_discussed` | 1 | 20% | restud_2026_restud_rdag037 p.12-13 Section 5.1.1 and 5.1.2: Effect sizes are interpreted as ratios of the race-specific coefficients and as the share of the excess mass a |
| `relative_to_mean` | 1 | 20% | restud_2026_restud_rdag037 p.12-13 Section 5.1.1 and 5.1.2: Effect sizes are interpreted as ratios of the race-specific coefficients and as the share of the excess mass a |

### mechanism_evidence (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `ruled_out_alternatives` | 4 | 80% | aer_111_4_3 p.26-27 Section IV.C: The authors examine whether employer-driven layoff incentives can explain the statutory-age effect by comparin; ecta_2025_ecta22303 p.28-29 Section 5.1.2, Figure 10: Borrowers with no remaining financial stake in their home (already underwater on an existing mortgage) are exa |
| `model_guided` | 3 | 60% | aer_111_4_3 p.24-25 Section IV.A, Figure 6: A gradual, cohort-by-cohort phase-in of a statutory-age reform is used as a natural experiment, showing that t; restud_2026_restud_rdag037 p.27-29 Section 5.4.3: Statistical versus taste-based discrimination is discussed through a simple model whose implications are check |
| `intermediate_outcomes` | 2 | 40% | aer_111_4_3 p.24-25 Section IV.A, Figure 6: A gradual, cohort-by-cohort phase-in of a statutory-age reform is used as a natural experiment, showing that t; restud_2026_restud_rdag037 p.17-18 Section 5.2.1, Tables A7 and A8: Alternative channels (offender behaviour, state-to-federal case shifting, law enforcement tactics) are each ru |
| `suggestive_labelled` | 2 | 40% | aer_111_4_3 p.26-26 Section IV.B: Evidence on the effect of increased information-letter frequency on bunching at the associated statutory age i; restud_2026_restud_rdag037 p.21-21 Section 5.2.5, Tables A11 and A12, Figure A10: Persistence of prosecutor bunching across districts, thresholds and time, and spillovers to colleagues after a |
| `heterogeneity_as_mechanism` | 1 | 20% | ecta_2025_ecta22303 p.26-28 Section 5.1.1.1, Figure 9: Both ex ante credit-quality comparisons and ex post realized-default comparisons around the bunching threshold |

### presentation_convention (papers with this category: 5/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `notes_state_sample` | 4 | 80% | aer_111_4_3 p.12-20 Table 2 and Table 4 notes: Table and figure notes consistently spell out the estimation sample, the weighting scheme, and the type of sta; ecta_2025_ecta22303 p.8-8 Table I: A detailed summary-statistics table reporting the mean, standard deviation, and several percentiles for key bo |
| `notes_state_se` | 4 | 80% | aer_111_4_3 p.12-20 Table 2 and Table 4 notes: Table and figure notes consistently spell out the estimation sample, the weighting scheme, and the type of sta; aer_112_10_8 p.18-26 Figures 2, 4, 6, 7: Figures throughout use binned-average plots with polynomial or nonparametric smoothers overlaid, and several e |
| `coefficient_plot` | 3 | 60% | ecta_2025_ecta22303 p.15-16 Section 3.2, Figure 6: Coefficient-style plots with confidence intervals, rather than a coefficient table, are the primary device use; restud_2026_restud_rdag037 p.17-30 Figure 2b, Figure 5: Later figures include a coefficient plot of bin-by-bin race differences scaled by bin share, RD-style binned p |
| `raw_data_plot` | 3 | 60% | aer_111_4_3 p.1-1 Figure 1, Panel A: The paper's opening figure presents a raw, unsmoothed count of job exits by monthly age bin for the full sampl; restud_2026_restud_rdag037 p.8-12 Table 1, Table 2, Figure 1: Figures begin with raw density histograms of drug amounts pre and post reform and a yearly share plot by race; |
| `summary_stats_table` | 3 | 60% | aer_111_4_3 p.12-12 Table 2: A dedicated summary statistics table reports means and standard deviations of key variables across the three s; ecta_2025_ecta22303 p.8-8 Table I: A detailed summary-statistics table reporting the mean, standard deviation, and several percentiles for key bo |
| `appendix_tables_numbered_a` | 2 | 40% | restud_2026_restud_rdag037 p.13-14 Table 3, Tables A1 to A21: Appendix tables and figures are numbered with an A prefix and referenced heavily; a table row labelled 'Predic; restud_2026_restud_rdag071 p.7-37 throughout; Supplementary Data note: Appendix figures are labelled A.x, appendix tables B.x, and theory appendices C.x; the appendix itself is only |
| `binscatter` | 2 | 40% | aer_111_4_3 p.19-19 Figure 4: A binned-scatterplot format is used to summarize the relationship between excess mass and kink size separately; aer_112_10_8 p.18-26 Figures 2, 4, 6, 7: Figures throughout use binned-average plots with polynomial or nonparametric smoothers overlaid, and several e |
| `rd_plot` | 2 | 40% | restud_2026_restud_rdag037 p.17-30 Figure 2b, Figure 5: Later figures include a coefficient plot of bin-by-bin race differences scaled by bin share, RD-style binned p; restud_2026_restud_rdag071 p.13-23 Figures 3-9: Figures include raw density plots by speed zone and normalized pooled versions, binned outcome-by-running-vari |
| `event_study_figure` | 1 | 20% | restud_2026_restud_rdag037 p.17-30 Figure 2b, Figure 5: Later figures include a coefficient plot of bin-by-bin race differences scaled by bin share, RD-style binned p |
| `map` | 1 | 20% | ecta_2025_ecta22303 p.7-7 Section 2.1, Figure 2: A choropleth-style map of participating ZIP codes is used to describe the geographic coverage of the sample ra |
| `other:cdf_plot` | 1 | 20% | ecta_2025_ecta22303 p.20-21 Section 3.5, Figure 7: Cumulative-distribution-function plots are used to compare the three bunching methods' implied distributions o |
| `stars_used` | 1 | 20% | restud_2026_restud_rdag037 p.8-12 Table 1, Table 2, Figure 1: Figures begin with raw density histograms of drug amounts pre and post reform and a yearly share plot by race; |

### replication_statement (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 4 | 80% | aer_111_4_3 p.40-40 References: The reference list includes a formal citation to a deposited replication data package for this paper, hosted t; ecta_2025_ecta22303 p.41-41 Back matter, replication statement: A replication-package DOI is given in the back matter, and the article states that the authors were granted an |
| `code_public` | 2 | 40% | restud_2026_restud_rdag037 p.33-33 Data Availability: A data availability statement gives a Zenodo DOI for the data and code; supplementary material is said to be a; restud_2026_restud_rdag071 p.37-37 Data Availability: A data availability statement says public data and all programs are in a Zenodo repository, confidential data  |
| `data_access_procedure_described` | 2 | 40% | ecta_2025_ecta22303 p.41-41 Back matter, replication statement: A replication-package DOI is given in the back matter, and the article states that the authors were granted an; restud_2026_restud_rdag071 p.37-37 Data Availability: A data availability statement says public data and all programs are in a Zenodo repository, confidential data  |
| `data_restricted` | 2 | 40% | ecta_2025_ecta22303 p.41-41 Back matter, replication statement: A replication-package DOI is given in the back matter, and the article states that the authors were granted an; restud_2026_restud_rdag071 p.37-37 Data Availability: A data availability statement says public data and all programs are in a Zenodo repository, confidential data  |
| `data_public` | 1 | 20% | restud_2026_restud_rdag037 p.33-33 Data Availability: A data availability statement gives a Zenodo DOI for the data and code; supplementary material is said to be a |
| `other:journal_verified_reproducibility` | 1 | 20% | ecta_2025_ecta22303 p.41-41 Back matter, replication statement: The journal states it checked the submitted code and data for the ability to generate the paper's tables and f |
| `other:software_not_named` | 1 | 20% | restud_2026_restud_rdag071 p.1-39 whole paper: No statistical software is named in the main text. |

### robustness_reported (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 3 | 60% | aer_111_4_3 p.24-24 Section III.C footnote, online Appendix Table A1: A decomposition exercise is used as an additional robustness check to gauge how much of the difference in bunc; aer_112_10_8 p.24-24 Section III.E, Bunching robustness paragraph: Robustness of the bunching evidence to round-number effects, to subsamples split by property holding period, a |
| `alt_estimator` | 2 | 40% | ecta_2025_ecta22303 p.18-20 Sections 3.4-3.5: Three independently constructed estimators of households' ideal loan amounts and collateral aversion are compa; restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Tables A3 to A5: Main-result robustness is summarised in one paragraph listing sample restrictions, state fixed effects and tre |
| `alt_sample` | 2 | 40% | aer_112_10_8 p.24-24 Section III.E, Bunching robustness paragraph: Robustness of the bunching evidence to round-number effects, to subsamples split by property holding period, a; restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Tables A3 to A5: Main-result robustness is summarised in one paragraph listing sample restrictions, state fixed effects and tre |
| `in_main_text` | 2 | 40% | aer_112_10_8 p.24-24 Section III.E, Bunching robustness paragraph: Robustness of the bunching evidence to round-number effects, to subsamples split by property holding period, a; restud_2026_restud_rdag037 p.14-16 Table 4 columns 4 to 6, Section 5.1.2: The missing-mass analysis is repeated with a later start year to address secular trends around a prior Supreme |
| `alt_fixed_effects` | 1 | 20% | restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Tables A3 to A5: Main-result robustness is summarised in one paragraph listing sample restrictions, state fixed effects and tre |
| `alt_se` | 1 | 20% | restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Tables A3 to A5: Main-result robustness is summarised in one paragraph listing sample restrictions, state fixed effects and tre |
| `alt_specification` | 1 | 20% | restud_2026_restud_rdag037 p.29-29 Section 5.4.3, Table A20: The animus result is probed in an appendix table by adding individual and district controls interacted with po |
| `online_appendix_not_available` | 1 | 20% | ecta_2025_ecta22303 p.18-20 Sections 3.4-3.5: Three independently constructed estimators of households' ideal loan amounts and collateral aversion are compa |
| `other:decomposition_robustness` | 1 | 20% | aer_111_4_3 p.24-24 Section III.C footnote, online Appendix Table A1: A decomposition exercise is used as an additional robustness check to gauge how much of the difference in bunc |
| `summarized_in_one_table` | 1 | 20% | restud_2026_restud_rdag037 p.13-13 Section 5.1.1, Tables A3 to A5: Main-result robustness is summarised in one paragraph listing sample restrictions, state fixed effects and tre |

### sample_construction (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 4 | 80% | aer_111_4_3 p.11-11 Section I.D: The main data source is named as administrative records from the German State Pension Fund covering the popula; ecta_2025_ecta22303 p.7-7 Section 2.2: The analysis sample is defined as household applications to the federal disaster loan program over a fixed mul |
| `exclusions_justified` | 4 | 80% | aer_111_4_3 p.11-11 Section I.D: The birth-cohort window used for the main analysis is stated explicitly, with the justification that only coho; ecta_2025_ecta22303 p.7-7 Section 2.2: The analysis sample is defined as household applications to the federal disaster loan program over a fixed mul |
| `sample_period_stated` | 4 | 80% | aer_111_4_3 p.11-11 Section I.D: The birth-cohort window used for the main analysis is stated explicitly, with the justification that only coho; ecta_2025_ecta22303 p.7-7 Section 2.2: The analysis sample is defined as household applications to the federal disaster loan program over a fixed mul |
| `unit_of_observation_stated` | 3 | 60% | aer_111_4_3 p.11-12 Section I.D, Table 2: The paper distinguishes three units of observation used across different parts of the analysis: an individual-; ecta_2025_ecta22303 p.7-7 Section 2.2: The analysis sample is defined as household applications to the federal disaster loan program over a fixed mul |
| `matching_or_linkage_described` | 2 | 40% | restud_2026_restud_rdag037 p.7-9 Section 3.2, Figure A1: Several auxiliary datasets from different stages of the criminal process are introduced with their purpose: st; restud_2026_restud_rdag071 p.8-9 Section 2.3.1: Primary data are police speeding tickets over a stated two-year window, linked via personal identifiers to the |
| `restricted_data_used` | 2 | 40% | aer_111_4_3 p.11-11 Section I.D: The underlying administrative data are described as accessed through a research data center rather than distri; restud_2026_restud_rdag071 p.8-9 Section 2.3.1: Primary data are police speeding tickets over a stated two-year window, linked via personal identifiers to the |
| `sample_size_reported_per_table` | 2 | 40% | aer_111_4_3 p.12-12 Table 2: The summary statistics table reports the number of observations separately for each of the three samples used,; restud_2026_restud_rdag037 p.8-25 Tables 1 to 7: Observation counts are reported in every regression table, including by column when the sample changes, and su |
| `data_restricted` | 1 | 20% | aer_111_4_3 p.11-11 Section I.D: The underlying administrative data are described as accessed through a research data center rather than distri |

### specification_reporting (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `baseline_then_variants` | 2 | 40% | ecta_2025_ecta22303 p.19-19 Table II: The table comparing collateral-aversion estimates across estimation approaches reports each method's summary s; restud_2026_restud_rdag037 p.12-12 Table 2 and notes: The main table has two columns, the pooled effect and the race-interacted version, with robust standard errors |
| `se_type_in_notes` | 2 | 40% | ecta_2025_ecta22303 p.19-19 Table II: The table comparing collateral-aversion estimates across estimation approaches reports each method's summary s; restud_2026_restud_rdag037 p.12-12 Table 2 and notes: The main table has two columns, the pooled effect and the race-interacted version, with robust standard errors |
| `cluster_level_in_notes` | 1 | 20% | restud_2026_restud_rdag037 p.25-25 Table 7 notes: The heterogeneity table mixes standard error types by column: robust for offender-level splits and clustered a |
| `fe_listed_in_table` | 1 | 20% | restud_2026_restud_rdag037 p.14-15 Table 3 and Table 4 notes: Missing-mass tables note that standard errors are estimated jointly across ranges by seemingly unrelated regre |
| `n_reported` | 1 | 20% | restud_2026_restud_rdag037 p.12-12 Table 2 and notes: The main table has two columns, the pooled effect and the race-interacted version, with robust standard errors |

### variable_construction (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `running_variable_definition` | 3 | 60% | aer_111_4_3 p.9-9 Section I.B: The key regressors are indicator variables for the presence of each type of statutory retirement age at a disc; ecta_2025_ecta22303 p.15-15 Section 3.2, Equation 6: The running/damage variable underlying the bunching analysis is binned into fixed-width increments and used bo |
| `measurement_error_discussed` | 2 | 40% | aer_111_4_3 p.11-11 Section I.D, footnote: The outcome analyzed throughout is the monthly job-exit (retirement) age, which the authors note is imputed fr; ecta_2025_ecta22303 p.18-19 Section 3.4.2: An alternative measure of a household's ideal loan amount is constructed from the loan amount originally reque |
| `outcome_definition` | 2 | 40% | aer_111_4_3 p.11-11 Section I.D, footnote: The outcome analyzed throughout is the monthly job-exit (retirement) age, which the authors note is imputed fr; restud_2026_restud_rdag037 p.10-10 Section 4.1, equations (1) and (2), footnote 7: The outcome is a binary indicator that the recorded drug amount falls in a narrow ten-gram bin at and above th |
| `treatment_definition` | 2 | 40% | aer_111_4_3 p.9-9 Section I.B: The key regressors are indicator variables for the presence of each type of statutory retirement age at a disc; restud_2026_restud_rdag037 p.10-10 Section 4.1, equations (1) and (2), footnote 7: The outcome is a binary indicator that the recorded drug amount falls in a narrow ten-gram bin at and above th |
| `other:counterfactual_proxy_construction` | 1 | 20% | ecta_2025_ecta22303 p.18-19 Section 3.4.2: An alternative measure of a household's ideal loan amount is constructed from the loan amount originally reque |
| `other:excess_mass_normalization` | 1 | 20% | aer_111_4_3 p.20-20 Section III.B, equation (5): The dependent variable in the discontinuity-level regressions is excess bunching mass normalized by the thresh |
| `other:key_construct_definition` | 1 | 20% | ecta_2025_ecta22303 p.13-14 Section 3.1: The paper's central outcome construct, collateral aversion, is formally defined within the stylized household  |
| `other:nominal_vs_real_discussion` | 1 | 20% | ecta_2025_ecta22303 p.9-9 Section 2.2, footnote 5: The paper explicitly discusses using nominal rather than inflation-adjusted dollar values throughout, arguing  |
| `standardized_index` | 1 | 20% | restud_2026_restud_rdag037 p.24-28 Figure 4b notes, footnote 24: A predicted sentence is built by regressing sentence on offender characteristics in pre-reform data and applyi |
| `winsorization` | 1 | 20% | ecta_2025_ecta22303 p.8-8 Table I note: Several monetary variables in the main summary-statistics table are winsorized at the extreme tails, with the  |

### writing_structure (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `results_previewed_in_intro` | 4 | 80% | aer_111_4_3 p.2-3 Introduction: The introduction previews the paper's main qualitative results, that financial incentives alone cannot explain; ecta_2025_ecta22303 p.2-5 Section 1: The introduction previews the paper's findings separately for each of the three motivating questions it poses, |
| `contribution_paragraph` | 3 | 60% | aer_111_4_3 p.1-2 Introduction: The introduction contains an explicit, numbered statement of the paper's main contributions before turning to ; restud_2026_restud_rdag037 p.2-13 Sections 1 to 6: The introduction previews all main findings and the sequence of supporting results, followed by a related-lite |
| `roadmap_paragraph` | 3 | 60% | aer_111_4_3 p.6-6 Introduction, penultimate paragraph: The introduction closes with an explicit roadmap paragraph naming each numbered section of the paper and descr; ecta_2025_ecta22303 p.2-5 Section 1: The introduction previews the paper's findings separately for each of the three motivating questions it poses, |
| `mechanisms_after_main` | 2 | 40% | aer_111_4_3 p.24-28 Section IV: Mechanism evidence is presented in a dedicated section placed after the main reduced-form results and before t; restud_2026_restud_rdag037 p.9-29 Section 4 opening, Section 5: Results open with the headline bunching estimate and its robustness, then progress through missing mass, condi |
| `appendix_heavy` | 1 | 20% | restud_2026_restud_rdag037 p.2-13 Sections 1 to 6: The introduction previews all main findings and the sequence of supporting results, followed by a related-lite |
| `data_before_design` | 1 | 20% | aer_111_4_3 p.7-14 Sections I and II: The institutional background and data section is presented before the empirical methodology section, rather th |
| `design_before_data` | 1 | 20% | restud_2026_restud_rdag037 p.2-13 Sections 1 to 6: The introduction previews all main findings and the sequence of supporting results, followed by a related-lite |
| `main_result_first` | 1 | 20% | restud_2026_restud_rdag037 p.9-29 Section 4 opening, Section 5: Results open with the headline bunching estimate and its robustness, then progress through missing mass, condi |
| `online_appendix_not_available` | 1 | 20% | ecta_2025_ecta22303 p.17-17 Section 3.4, and throughout: Substantial technical and robustness detail (full bunching derivations, additional heterogeneity results, and  |
| `other:companion_paper_appendix` | 1 | 20% | ecta_2025_ecta22303 p.17-17 Section 3.4, and throughout: Substantial technical and robustness detail (full bunching derivations, additional heterogeneity results, and  |
| `other:model_after_empirics` | 1 | 20% | restud_2026_restud_rdag071 p.28-31 Section 5: The theoretical model is presented after the empirical results and is explicitly positioned as rationalizing t |
| `other:robustness_embedded_in_results` | 1 | 20% | ecta_2025_ecta22303 p.18-25 Sections 3.4-3.5 and 4.2: Robustness checks for both the default model and the bunching estimates are embedded within the results subsec |
| `robustness_separate_section` | 1 | 20% | restud_2026_restud_rdag037 p.2-13 Sections 1 to 6: The introduction previews all main findings and the sequence of supporting results, followed by a related-lite |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | paper_only | 1 | aer_111_4_3 d1.implementation_features (paper: The bunching estimation excludes a region around each threshold when f / card: No bandwidth or exclusion-window field is populated for design d1 or a) |
| bandwidth | unknown | 1 | aer_112_10_8 s2.sample (paper: The appendix regression-kink implementation of the listing-premium hoc / card: Card specification s2 shows a formula with a local-polynomial order an) |
| bandwidth | code_only | 1 | ecta_2025_ecta22303 s1.notes / x2 (paper: The traditional bunching estimator's counterfactual is described in th / card: Spec s1's notes record a specific polynomial degree and three cutpoint) |
| bandwidth | agree | 1 | restud_2026_restud_rdag071 s2.sample_restrictions (paper: CCT optimal bandwidth, reported per horizon in Table 3 / card: s2 restricts to |normalized| <= bw; bandwidth value not recorded) |
| cluster_level | paper_only | 2 | ecta_2025_ecta22303 s2.se.cluster_level (paper: Standard errors in the default model are stated as clustered at the di / card: Spec s2's se.type and se.cluster_level fields are both null (unknown),); restud_2026_restud_rdag037 s1.se.cluster_level (paper: No clustering for the main table; state-level clustering for state spl / card: cluster_level null for s1 and s2; no prosecutor-level spec recorded.) |
| cluster_level | unknown | 1 | aer_111_4_3 s1.se.cluster_level (paper: The paper does not mention clustering of standard errors at any level. / card: s1.se.cluster_level=null for every specification.) |
| cluster_level | agree | 1 | restud_2026_restud_rdag071 s1.se.cluster_level; s2.se.cluster_level (paper: Clustered at the individual level / card: s1 cluster on cluster_id; s2 cluster on shnro) |
| comparison_group | paper_only | 2 | aer_111_4_3 d1.comparison_group (paper: The design's comparison is explicit throughout: statutory-age disconti / card: d1.comparison_group=null.); ecta_2025_ecta22303 d2.comparison_group (paper: The paper explicitly names the control/comparison group for the differ / card: Design d2's comparison_group field is null (unknown).) |
| comparison_group | agree | 1 | aer_112_10_8 s2.comparison_group (paper: The appendix regression-kink check is a single-threshold kink design a / card: Card specification s2.comparison_group is null, consistent with a kink) |
| controls | paper_only | 3 | aer_112_10_8 s1.controls_summary (paper: The hedonic model's control set is spelled out in the text: time-varyi / card: Card specification s1.controls_summary is null; only the outcome varia); ecta_2025_ecta22303 s2.controls_summary (paper: The paper lists the specific borrower and home covariates added across / card: Spec s2's controls_summary field is null.) |
| controls | agree | 1 | aer_111_4_3 s3.bindings[0] (paper: Column 3 adds worker controls including income, education, gender, mar / card: s3 binds global controls_ind to a variable list (schooly2 lifeearn lli) |
| data_source | paper_only | 4 | aer_112_10_8 data (paper: The paper names four core administrative data sources plus one commerc / card: The card's top-level data array is empty; no data sources are recorded); ecta_2025_ecta22303 data[0].source_hint (paper: The paper describes the underlying data as administrative federal disa / card: The card's data records show access as 'unknown' and source_hint as nu) |
| data_source | agree | 1 | aer_111_4_3 data[0].name (paper: The main administrative data are named as coming from the German State / card: data[0].name=RTZN, type=admin, source_hint=null; evidence line 'use $d) |
| diagnostic | paper_only | 3 | aer_111_4_3 diagnostics (paper: The paper reports a density-shape comparison test (Figure 8) used to d / card: diagnostics=[] (empty array) at the card level.); aer_112_10_8 diagnostics (paper: The paper reports an extensive set of diagnostics: hedonic fit-statist / card: The card's diagnostics array is empty.) |
| diagnostic | unknown | 2 | ecta_2025_ecta22303 x1 (paper: The main text does not report a formal bandwidth-sensitivity check for / card: Diagnostic x1 (bandwidth_selection) is recorded with status 'unknown' ); restud_2026_restud_rdag037 x1 (paper: KS test of pre-2010 distributions by race, placebo reassignment exerci / card: x1 density_test with unknown details.) |
| estimator | agree | 5 | aer_111_4_3 s1.estimator (paper: Reduced-form effects are estimated by OLS on discontinuity-level bunch / card: s1-s5 all record estimator=ols, command=reg.); aer_112_10_8 s1.formula_or_call (paper: The hedonic fair-value model is estimated as an OLS regression of log  / card: Card specification s1 records the same command and formula, an OLS reg) |
| estimator | paper_only | 2 | aer_111_4_3 specifications (paper: Section VI.A states that reference-dependence parameters are recovered / card: The specifications array contains only the OLS reduced-form regression); aer_112_10_8 designs (paper: The paper's primary estimator for its main claims is a structural mode / card: The card records only two designs, an OLS hedonic regression (d1/s1) a) |
| fixed_effects | agree | 3 | aer_112_10_8 s1.fixed_effects (paper: The hedonic model's fixed effects are described as year-cross-municipa / card: Card specification s1 lists fixed_effects as year and komstr, matching); ecta_2025_ecta22303 s2.fixed_effects (paper: The default equations include disaster fixed effects, years-since-orig / card: Spec s2's fixed_effects field lists Disaster_Id, timeInt, and loss_cut) |
| fixed_effects | paper_only | 2 | aer_111_4_3 s3.fixed_effects (paper: Table 4 lists pathway fixed effects and year-of-birth fixed effects as / card: s3.fixed_effects=null and s4.fixed_effects=null; the underlying formul); restud_2026_restud_rdag037 s1.fe (paper: No fixed effects in the main specification; district FE and race-speci / card: fe None for s1 and s2; no other specs recorded.) |
| other | paper_only | 2 | ecta_2025_ecta22303 structural (paper: The paper documents a fully specified structural model in the main tex / card: The card's dedicated 'structural' field is null; the structural design); restud_2026_restud_rdag071 methods (paper: IV via 2SLS with crossing the cutoff as instrument for fine amount / card: only rdd recorded as method) |
| other | unknown | 1 | restud_2026_restud_rdag037 packages.rdplot (paper: RD-style plots of sentence around 280 g and time discontinuity around  / card: Package rdplot listed under Stata with unknown use.) |
| outputs | paper_only | 4 | aer_111_4_3 s1.output_ids (paper: The reduced-form regressions are explicitly reported in Table 4 of the / card: s1-s5.output_ids are all empty arrays; no table is linked to any speci); aer_112_10_8 outputs (paper: The paper contains four numbered main tables and ten main figures repo / card: The card's outputs.tables and outputs.figures arrays are both empty.) |
| outputs | disagree | 1 | restud_2026_restud_rdag071 outputs (paper: Three main tables and twelve figures plus appendix A/B figures and tab / card: tables=1 figures=0) |
| robustness | paper_only | 5 | aer_111_4_3 robustness (paper: The paper references robustness checks for the structural parameters a / card: robustness=[] (empty array) at the card level.); aer_112_10_8 robustness (paper: The paper reports a dedicated robustness table re-estimating the full  / card: The card's robustness array is empty.) |
| sample | paper_only | 3 | aer_111_4_3 s1.sample (paper: Section I.D describes the discontinuity-level bunching sample and its  / card: s1-s5.sample is null; the formula shows an unexplained 'if incl==1' fi); ecta_2025_ecta22303 s2.sample (paper: The paper states explicit sample restrictions: the default analysis is / card: Spec s2's sample field is null (unknown); the card's data records for ) |
| sample | agree | 1 | restud_2026_restud_rdag071 s1.source (paper: 80 km/h and 120 km/h limit zones omitted from main RD / card: script name step5_estimates_dayFine_no80.do) |
| se_type | agree | 2 | aer_112_10_8 s1.se (paper: The main text does not discuss standard errors or clustering for the h / card: Card specification s1 records se.type and se.cluster_level as null.); restud_2026_restud_rdag037 s1.se, s2.se (paper: Robust standard errors in parentheses for Table 2. / card: se robust in s1 and s2.) |
| se_type | unknown | 1 | aer_111_4_3 s1.se.type (paper: Table 4 notes state standard errors are obtained by bootstrap, resampl / card: s1.se.type=robust (vce(r)); s2.se.type=iid (no vce option) at the trac) |
| weights | agree | 3 | aer_111_4_3 s1.weights (paper: Table 4 notes state that all regressions are weighted by group size. / card: s1-s5 all record weights=aweight=weight.); aer_112_10_8 s1.weights (paper: No mention of regression weights appears in the discussion of the hedo / card: Card specifications s1.weights and s2.weights are both null.) |

## Gaps the readers reported

- (1) No explicit McCrary-style density manipulation test is reported for the running variable used in the bunching estimation
- (1) No formal pre-analysis plan, IRB approval, or consent statement is mentioned anywhere in the main text; the setting uses
- (1) No explicit clustering of standard errors by pathway, cohort, or any other group is discussed; only a bootstrap over bun
- (1) The main text does not name the statistical software used to produce the estimates or figures.
- (1) No formal weak-instrument, first-stage, or overidentification diagnostic appears, consistent with the paper not using an
- (1) No explicit justification found in the main text for choosing the shire level (rather than municipality or another unit)
- (1) No preregistration, IRB approval, or ethics/consent statement found anywhere in the read pages.
- (1) No explicit statement in the main text of the software or optimization package used to solve and estimate the structural
- (1) No formal first-stage or weak-instrument statistic reported in the main text for the demand-concavity instrumental varia
- (1) No description in the main text of the procedure for obtaining access to the restricted Danish administrative registers;
- (1) The online appendix (referenced dozens of times, spanning lettered sections A through K) was not included in the supplie
- (1) No explicit statement of a stars/significance-level convention was found in the main-text tables; coefficients are repor
- (1) The specific polynomial degree and bandwidth used for the traditional bunching counterfactual are not given numeric valu
- (1) No preregistration, IRB approval, or participant-consent statement is present anywhere in the article; this is an admini
- (1) The statistical/programming software used for estimation is not named in the main article text itself (it is only infera
- (1) The companion supplement 'Collier, Ellis, and Keys (2025), Supplement to The Cost of Consumer Collateral' that the artic
- (1) No explicit justification for using robust (unclustered) standard errors in the main specification.
- (1) No software or package named in the text; only a Zenodo DOI for data and code.
- (1) No preregistration, IRB or ethics statement.
- (1) Online appendix (Tables A1 to A21, Figures A1 to A12) is not included in the text file; appendix content is known only t
- (1) No multiple testing adjustment discussed for the many heterogeneity columns.
- (1) No explicit justification for clustering at the individual level
- (1) No formal density (McCrary or rddensity) test statistic; manipulation assessed graphically only
- (1) No weak-instrument statistic reported for the IV first stage
- (1) No software named in the main text
- (1) Online appendix (Figures A.x, Tables B.x, Section C) is not in the text file, so appendix practices are recorded only as
- (1) No preregistration or ethics statement

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
