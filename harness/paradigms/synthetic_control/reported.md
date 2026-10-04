# Reported practice: `synthetic_control` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 6 paper notes (6 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | JFE: 2, ReStud: 2, AER: 1, JPE: 1 |
| year | 2021: 1, 2024: 1, 2025: 1, 2026: 3 |
| papers with at least one observation in category | inference_justification: 5, presentation_convention: 5, design_statement: 4, robustness_reported: 4, specification_reporting: 3, diagnostic_reported: 3, writing_structure: 3, sample_construction: 2, magnitude_interpretation: 2, external_validity: 2, variable_construction: 2, replication_statement: 2, data_access: 2, heterogeneity_reported: 1, limitation_stated: 1, mechanism_evidence: 1, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_111_12_8 | AER | 2021 | full | yes | 2dad5774a7af |
| jfe_2024_j_jfineco_2024_103809 | JFE | 2024 | full | yes | 3776fdfeb8c7 |
| jfe_2025_j_jfineco_2025_104150 | JFE | 2025 | full | yes | d509ecfbe6d0 |
| jpe_2026_742424 | JPE | 2026 | full | yes | 4c49976efe5e |
| restud_2026_restud_rdaf071 | ReStud | 2026 | full | yes | 66bf5dfc1113 |
| restud_2026_restud_rdag011 | ReStud | 2026 | full | yes | 6ac6bc1756be |

## Practices by category and tag


### data_access (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 2 | 33% | jpe_2026_742424 p.30-30 Section VII, footnote: The country-panel emissions data reanalyzed in the empirical application are described as originating from an ; restud_2026_restud_rdaf071 p.5-18 Section 2; Appendix C; footnote 21: Data are administrative registries, national surveys, census microdata, and historical election records; the a |
| `linked_records` | 1 | 17% | restud_2026_restud_rdaf071 p.5-18 Section 2; Appendix C; footnote 21: Data are administrative registries, national surveys, census microdata, and historical election records; the a |
| `other:oral_histories` | 1 | 17% | restud_2026_restud_rdaf071 p.5-18 Section 2; Appendix C; footnote 21: Data are administrative registries, national surveys, census microdata, and historical election records; the a |
| `public_use` | 1 | 17% | jpe_2026_742424 p.30-30 Section VII, footnote: The country-panel emissions data reanalyzed in the empirical application are described as originating from an  |
| `survey_collected` | 1 | 17% | restud_2026_restud_rdaf071 p.5-18 Section 2; Appendix C; footnote 21: Data are administrative registries, national surveys, census microdata, and historical election records; the a |

### design_statement (papers with this category: 4/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 4 | 67% | aer_111_12_8 p.1-3 Introduction, equations (1)-(3): The paper proposes synthetic difference-in-differences as a new estimator combining DID's parallel-trends logi; jfe_2024_j_jfineco_2024_103809 p.2-7 Section 1 (introduction) and Section 4.2: The paper names three complementary designs for the main analysis: a firm and day fixed-effects difference-in- |
| `identifying_assumption_explicit` | 3 | 50% | aer_111_12_8 p.4-5 Section I.A: Unit weights are chosen so unexposed units' pre-period trend is only approximately, not exactly, parallel to t; jpe_2026_742424 p.2-3 Introduction: The introduction states two inferential threats motivating the method: the synthetic control estimator is bias |
| `parallel_trends_argued` | 3 | 50% | aer_111_12_8 p.4-5 Section I.A: Unit weights are chosen so unexposed units' pre-period trend is only approximately, not exactly, parallel to t; jpe_2026_742424 p.3-24 Section III.C; Section IV.B Remark: The paper formally argues that the debiased synthetic control estimator is asymptotically at least as efficien |
| `estimand_named` | 2 | 33% | aer_111_12_8 p.1-3 Introduction, equations (1)-(3): The paper proposes synthetic difference-in-differences as a new estimator combining DID's parallel-trends logi; jpe_2026_742424 p.1-2 Abstract / Introduction: The paper names its target parameter precisely as the average treatment effect on the treated over the post-tr |
| `in_main_text` | 1 | 17% | jfe_2024_j_jfineco_2024_103809 p.2-7 Section 1 (introduction) and Section 4.2: The paper names three complementary designs for the main analysis: a firm and day fixed-effects difference-in- |
| `threats_discussed` | 1 | 17% | jpe_2026_742424 p.2-3 Introduction: The introduction states two inferential threats motivating the method: the synthetic control estimator is bias |

### diagnostic_reported (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 3 | 50% | aer_111_12_8 p.7-7 Figure 1, top panel: No formal statistical pre-trends test is reported anywhere; pre-treatment fit is instead conveyed only visuall; jpe_2026_742424 p.26-33 Section V.A; Section VII, Table 4: A placebo-in-time procedure is proposed and applied: the pre-treatment period is split into a placebo pre- and |
| `pre_trends_plot` | 2 | 33% | aer_111_12_8 p.7-7 Figure 1, top panel: No formal statistical pre-trends test is reported anywhere; pre-treatment fit is instead conveyed only visuall; restud_2026_restud_rdaf071 p.14-28 Figures 2, 3, 4, 7: Pre-trends are shown graphically in three event-study figures (semi-decade district estimates, SDID trend plot |
| `balance_table` | 1 | 17% | aer_111_12_8 p.7-7 Figure 1, bottom panel: The bottom panel of the same comparison figure functions as an implicit influence diagnostic, plotting each co |
| `event_study_figure` | 1 | 17% | restud_2026_restud_rdaf071 p.14-28 Figures 2, 3, 4, 7: Pre-trends are shown graphically in three event-study figures (semi-decade district estimates, SDID trend plot |
| `in_appendix` | 1 | 17% | jpe_2026_742424 p.27-29 Section VI, appendix reference: An extended simulation exercise with a much longer pre-treatment period is described as reported in the online |
| `online_appendix_not_available` | 1 | 17% | jpe_2026_742424 p.27-29 Section VI, appendix reference: An extended simulation exercise with a much longer pre-treatment period is described as reported in the online |
| `other:ar1_residual_persistence_check` | 1 | 17% | jpe_2026_742424 p.19-27 Section III.B; Section VI: Persistence in the pre-treatment prediction errors is diagnosed by fitting an autoregressive model to the synt |
| `other:coverage_simulation` | 1 | 17% | aer_111_12_8 p.24-24 Table 4: Coverage of nominal confidence intervals is reported as the paper's primary diagnostic of inference quality, c |
| `other:influence_diagnostic` | 1 | 17% | aer_111_12_8 p.7-7 Figure 1, bottom panel: The bottom panel of the same comparison figure functions as an implicit influence diagnostic, plotting each co |
| `other:placebo_in_time_test` | 1 | 17% | jpe_2026_742424 p.26-33 Section V.A; Section VII, Table 4: A placebo-in-time procedure is proposed and applied: the pre-treatment period is split into a placebo pre- and |

### external_validity (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 2 | 33% | aer_111_12_8 p.1-2 Introduction: The introduction explicitly frames DID and SC as historically suited to different empirical regimes, many trea; jpe_2026_742424 p.33-34 Section VIII.A: The practical-recommendations section discusses how the method should be adapted when there are multiple treat |

### heterogeneity_reported (papers with this category: 1/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `mechanism_motivated` | 1 | 17% | jpe_2026_742424 p.27-28 Section VI, Table 2: Heterogeneity across data-generating processes rather than across observational units is the paper's main lens |

### inference_justification (papers with this category: 5/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_se` | 1 | 17% | restud_2026_restud_rdaf071 p.12-18 Table 2 notes; footnote 19: SDID standard errors use the cluster bootstrap algorithm from the SDID paper; a footnote adds that the imputat |
| `other:accuracy_length_tradeoff` | 1 | 17% | jpe_2026_742424 p.18-20 Section III.B: Choosing the number of cross-fitting blocks is explicitly justified as a trade-off between the accuracy of the |
| `other:bootstrap_se` | 1 | 17% | jfe_2025_j_jfineco_2025_104150 p.15-15 Section 5.1, Fig. 6 notes: The synthetic-control confidence intervals are constructed from a nonparametric bootstrap procedure specific t |
| `other:cluster_bootstrap` | 1 | 17% | restud_2026_restud_rdaf071 p.12-18 Table 2 notes; footnote 19: SDID standard errors use the cluster bootstrap algorithm from the SDID paper; a footnote adds that the imputat |
| `other:cross_fitting_blocks` | 1 | 17% | jpe_2026_742424 p.11-18 Section II.B; Section III.B: The degrees of freedom of the inferential t-distribution are tied directly to the number of cross-fitting bloc |
| `other:jackknife_bias_caveat` | 1 | 17% | aer_111_12_8 p.22-23 Section IV, Theorem 2: The jackknife variance estimator is proven conservative in general and exact only under an additional stated c |
| `other:newey_west_critiqued` | 1 | 17% | jpe_2026_742424 p.3-3 Introduction, Figure 2: The authors justify avoiding classical long-run-variance estimators by pointing to simulation evidence, cited  |
| `other:persistence_diagnostic_for_block_choice` | 1 | 17% | jpe_2026_742424 p.19-20 Section III.B: The paper recommends that researchers gauge the persistence of prediction errors by fitting a simple autoregre |
| `other:self_normalized_pivotal_statistic` | 1 | 17% | jpe_2026_742424 p.11-16 Section II.B; Theorem 2: Inference is justified by constructing a scale-free, self-normalized statistic whose asymptotic distribution i |
| `randomization_inference` | 1 | 17% | jfe_2024_j_jfineco_2024_103809 p.11-11 Table 4 notes: Synthetic difference-in-differences standard errors are computed with the placebo-based inference method assoc |

### limitation_stated (papers with this category: 1/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identification_caveat` | 1 | 17% | jpe_2026_742424 p.2-34 Introduction; Section VIII.A: The recommendations section states explicitly that the method should not be used when there are too few post-t |

### magnitude_interpretation (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 2 | 33% | aer_111_12_8 p.6-6 Section I.B: Differences between estimators in the California application are interpreted qualitatively as well as numerica; jpe_2026_742424 p.6-32 Introduction; Section VII: The empirical illustration's inferential conclusion is explicitly framed as corroborating a specific published |
| `precision_discussed` | 2 | 33% | aer_111_12_8 p.6-6 Section I.B: Differences between estimators in the California application are interpreted qualitatively as well as numerica; jpe_2026_742424 p.32-33 Section VII: Differences in the width of confidence intervals across the four compared methods in the empirical application |
| `sd_units` | 1 | 17% | aer_111_12_8 p.10-10 Table 2 notes: Outcomes in the simulation studies are standardized before reporting bias and RMSE, and the resulting figures  |

### mechanism_evidence (papers with this category: 1/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `model_guided` | 1 | 17% | restud_2026_restud_rdaf071 p.10-32 Section 2.3; Appendix B: A Hotelling-style model of school entry and curriculum choice is placed in an appendix and referenced as the o |

### other (papers with this category: 1/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:funding_disclosed` | 1 | 17% | restud_2026_restud_rdag011 p.30-30 Acknowledgments: Funding source and host institutions are disclosed, along with a disclaimer that views are not those of the na |

### presentation_convention (papers with this category: 5/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `coefficient_plot` | 3 | 50% | jfe_2024_j_jfineco_2024_103809 p.9-11 Figures 1 and 2: Both the standard and synthetic difference-in-differences results are visualized as coefficient-over-time figu; jfe_2025_j_jfineco_2025_104150 p.13-15 Fig. 4 and Fig. 6: Dynamic treatment-effect estimates around issuance are presented as coefficient/event-study figures, with each |
| `event_study_figure` | 3 | 50% | jfe_2024_j_jfineco_2024_103809 p.9-11 Figures 1 and 2: Both the standard and synthetic difference-in-differences results are visualized as coefficient-over-time figu; jfe_2025_j_jfineco_2025_104150 p.13-15 Fig. 4 and Fig. 6: Dynamic treatment-effect estimates around issuance are presented as coefficient/event-study figures, with each |
| `raw_data_plot` | 3 | 50% | aer_111_12_8 p.7-7 Figure 1: The main comparison figure is a two-row diagram: raw trend lines with weighted control averages on top, paired; jpe_2026_742424 p.29-32 Section VII, Figure 4: The empirical application opens with a raw time-series plot of the outcome for the treated unit before any mod |
| `no_stars` | 2 | 33% | aer_111_12_8 p.6-6 Table 1: Every main table reports point estimates and standard errors without significance stars, consistent with the p; jpe_2026_742424 p.30-33 Table 3; Table 5: Result tables in both the simulation study and the empirical application report point estimates together with  |
| `notes_state_se` | 2 | 33% | jfe_2025_j_jfineco_2025_104150 p.13-15 Fig. 4 and Fig. 6: Dynamic treatment-effect estimates around issuance are presented as coefficient/event-study figures, with each; jpe_2026_742424 p.30-33 Table 3; Table 5: Result tables in both the simulation study and the empirical application report point estimates together with  |
| `appendix_tables_numbered_a` | 1 | 17% | restud_2026_restud_rdaf071 p.5-38 Section 2 and appendix references throughout: Appendix material is numbered with an A prefix and lettered appendices (B model, C oral histories, D data); no |
| `binscatter` | 1 | 17% | restud_2026_restud_rdaf071 p.8-28 Figures 1 to 7: Figures include district binscatters for targeting, semi-decade coefficient plots with confidence bars, SDID t |
| `other:error_density_plot` | 1 | 17% | aer_111_12_8 p.11-12 Figure 2: A second figure reports the simulated sampling distribution of estimator errors as overlaid density curves for |
| `other:no_summary_stats_table_in_main_text` | 1 | 17% | restud_2026_restud_rdaf071 p.5-38 Section 2 and appendix references throughout: Appendix material is numbered with an A prefix and lettered appendices (B model, C oral histories, D data); no |
| `other:simulation_distribution_figure` | 1 | 17% | jpe_2026_742424 p.2-3 Introduction, Figures 1-2: Simulation results are also conveyed graphically rather than only in tables: one figure overlays the sampling  |
| `other:weight_influence_diagram` | 1 | 17% | aer_111_12_8 p.7-7 Figure 1: The main comparison figure is a two-row diagram: raw trend lines with weighted control averages on top, paired |
| `summary_stats_table` | 1 | 17% | jpe_2026_742424 p.28-28 Table 2: A dedicated table enumerates each Monte Carlo data-generating process by name, its parameter settings, and the |

### replication_statement (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `code_public` | 2 | 33% | jpe_2026_742424 p.35-35 Data Availability statement: A dedicated data-availability statement cites a deposited replication package containing both the code and dat; restud_2026_restud_rdaf071 p.39-39 Data Availability; Supplementary Data: A Data Availability paragraph gives a Zenodo DOI for the data and code; a Supplementary Data line points to th |
| `data_public` | 2 | 33% | jpe_2026_742424 p.35-35 Data Availability statement: A dedicated data-availability statement cites a deposited replication package containing both the code and dat; restud_2026_restud_rdaf071 p.39-39 Data Availability; Supplementary Data: A Data Availability paragraph gives a Zenodo DOI for the data and code; a Supplementary Data line points to th |
| `replication_package_cited` | 2 | 33% | jpe_2026_742424 p.35-35 Data Availability statement: A dedicated data-availability statement cites a deposited replication package containing both the code and dat; restud_2026_restud_rdaf071 p.39-39 Data Availability; Supplementary Data: A Data Availability paragraph gives a Zenodo DOI for the data and code; a Supplementary Data line points to th |
| `software_named` | 1 | 17% | jpe_2026_742424 p.2-32 Introduction footnote; Section VII: The main inferential method is stated to be implemented in a named, publicly hosted R package, and the paper r |

### robustness_reported (papers with this category: 4/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 4 | 67% | aer_111_12_8 p.10-11 Table 2: The Monte Carlo comparison table is itself structured as a large set of robustness variants around one baselin; jfe_2024_j_jfineco_2024_103809 p.9-11 Tables 3-5 and Figures 1-2: The three-estimator strategy (difference-in-differences, synthetic difference-in-differences, matching) functi |
| `alt_estimator` | 3 | 50% | jfe_2024_j_jfineco_2024_103809 p.9-11 Tables 3-5 and Figures 1-2: The three-estimator strategy (difference-in-differences, synthetic difference-in-differences, matching) functi; jfe_2025_j_jfineco_2025_104150 p.11-16 Section 5.1: Robustness to confounding between treated and control firms is pursued through a sequence of distinct named es |
| `summarized_in_one_table` | 3 | 50% | aer_111_12_8 p.10-11 Table 2: The Monte Carlo comparison table is itself structured as a large set of robustness variants around one baselin; jfe_2024_j_jfineco_2024_103809 p.9-11 Tables 3-5 and Figures 1-2: The three-estimator strategy (difference-in-differences, synthetic difference-in-differences, matching) functi |
| `alt_specification` | 2 | 33% | aer_111_12_8 p.10-11 Table 2: The Monte Carlo comparison table is itself structured as a large set of robustness variants around one baselin; jpe_2026_742424 p.19-19 Section III.B, Figure 3 and Table 1: Sensitivity of the method to its own tuning parameter is reported through a figure showing the coverage-versus |
| `online_appendix_not_available` | 2 | 33% | aer_111_12_8 p.4-4 footnote 5: A footnote references a further comparison table contrasting more strongly regularized weights against the pap; jpe_2026_742424 p.25-25 Section V.A, appendix reference: Robustness of the method to a different kind of instability, namely time-varying synthetic control weights tha |
| `in_appendix` | 1 | 17% | jpe_2026_742424 p.25-25 Section V.A, appendix reference: Robustness of the method to a different kind of instability, namely time-varying synthetic control weights tha |

### sample_construction (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 2 | 33% | aer_111_12_8 p.12-12 Section II.B: The Penn World Table placebo sample's ending year is deliberately chosen so the treatment period does not coin; jpe_2026_742424 p.29-30 Section VII: The empirical illustration reuses a previously published country-panel dataset on transport carbon emissions w |
| `exclusions_justified` | 2 | 33% | aer_111_12_8 p.12-12 Section II.B: The Penn World Table placebo sample's ending year is deliberately chosen so the treatment period does not coin; jpe_2026_742424 p.29-29 Section VII: The sample period is justified by an external institutional cutoff: the post-treatment window ends at the year |
| `sample_period_stated` | 2 | 33% | aer_111_12_8 p.12-12 Section II.B: The Penn World Table placebo sample's ending year is deliberately chosen so the treatment period does not coin; jpe_2026_742424 p.29-29 Section VII: The sample period is justified by an external institutional cutoff: the post-treatment window ends at the year |
| `sample_size_reported_per_table` | 1 | 17% | aer_111_12_8 p.10-13 Table 2 and Table 3 notes: Panel dimensions and the number of treated units and periods for every simulation design variant are stated di |
| `unit_of_observation_stated` | 1 | 17% | jpe_2026_742424 p.29-30 Section VII: The empirical illustration reuses a previously published country-panel dataset on transport carbon emissions w |

### specification_reporting (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `baseline_then_variants` | 3 | 50% | aer_111_12_8 p.6-6 Table 1 and notes: The California results table reports point estimates and standard errors for five estimators side by side in o; jpe_2026_742424 p.33-33 Table 5: The main application table reports the proposed estimator as the primary panel and then presents three alterna |
| `fe_listed_in_table` | 2 | 33% | jpe_2026_742424 p.30-30 Table 3: The Monte Carlo results table organizes rows by data-generating process and by the number of cross-fitting fol; restud_2026_restud_rdaf071 p.9-9 Table 1: The targeting table progresses columns across alternative measures of Islamic education presence and then adds |
| `se_type_in_notes` | 2 | 33% | aer_111_12_8 p.6-6 Table 1 and notes: The California results table reports point estimates and standard errors for five estimators side by side in o; jpe_2026_742424 p.33-33 Table 5 notes: Table notes describe how each panel's interval was constructed (e.g., that one panel's interval is asymmetric  |
| `alt_estimator` | 1 | 17% | restud_2026_restud_rdaf071 p.12-12 Table 2 panels (a) to (d): The main entry table stacks four panels for the same outcomes: standard DID, synthetic DID, village DID, and t |
| `controls_progressive_columns` | 1 | 17% | restud_2026_restud_rdaf071 p.9-9 Table 1: The targeting table progresses columns across alternative measures of Islamic education presence and then adds |
| `other:no_r2_reported` | 1 | 17% | aer_111_12_8 p.6-13 Tables 1-4: Neither the California table nor the simulation tables report an R-squared or a dependent-variable mean; the t |

### variable_construction (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `treatment_definition` | 2 | 33% | jpe_2026_742424 p.31-31 Section VII, footnote: The predictor set used to construct synthetic control weights in the reanalysis is stated to differ from the o; restud_2026_restud_rdaf071 p.11-12 Section 3.1; Table 2 notes: Treatment intensity is defined as programme schools built in the 1973 to 1978 window per thousand children in  |
| `measurement_error_discussed` | 1 | 17% | jpe_2026_742424 p.13-14 Section III.A: The paper interprets its underlying prediction model as a statistical approximation rather than a structural m |
| `outcome_definition` | 1 | 17% | jpe_2026_742424 p.29-30 Section VII: The outcome variable is defined as the treated country's per-capita emissions from a specific sector, matching |

### writing_structure (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 2 | 33% | jpe_2026_742424 p.3-6 Introduction; Section I.A: The introduction closes with an explicit roadmap sentence pointing readers to the practical-recommendations se; restud_2026_restud_rdaf071 p.2-10 Section 1; Section 2.3: The introduction previews results for each of three outcome families in order, followed by three contribution  |
| `mechanisms_after_main` | 2 | 33% | jpe_2026_742424 p.27-29 Section VI precedes Section VII: Simulation evidence assessing when the method works well or poorly is placed in its own section immediately be; restud_2026_restud_rdaf071 p.10-38 Sections 3, 4, 5: Each results section opens with a short data paragraph, then the equation, then the main table, then a titled  |
| `results_previewed_in_intro` | 2 | 33% | jpe_2026_742424 p.6-6 Introduction: The direction and significance of the empirical application's main finding is previewed in the introduction, w; restud_2026_restud_rdaf071 p.2-10 Section 1; Section 2.3: The introduction previews results for each of three outcome families in order, followed by three contribution  |
| `roadmap_paragraph` | 2 | 33% | jpe_2026_742424 p.3-6 Introduction; Section I.A: The introduction closes with an explicit roadmap sentence pointing readers to the practical-recommendations se; restud_2026_restud_rdaf071 p.2-10 Section 1; Section 2.3: The introduction previews results for each of three outcome families in order, followed by three contribution  |
| `appendix_heavy` | 1 | 17% | restud_2026_restud_rdaf071 p.13-37 Footnotes 15, 19, 28, 30, 41: Many secondary results live in footnotes that cite appendix tables (robust clustering, transitions, years of s |
| `data_before_design` | 1 | 17% | restud_2026_restud_rdaf071 p.10-38 Sections 3, 4, 5: Each results section opens with a short data paragraph, then the equation, then the main table, then a titled  |
| `design_before_data` | 1 | 17% | jpe_2026_742424 p.9-27 Sections II-IV precede Sections VI-VII: The paper's overall structure develops the estimator and its theoretical guarantees under stationary and then  |
| `in_footnote` | 1 | 17% | restud_2026_restud_rdaf071 p.13-37 Footnotes 15, 19, 28, 30, 41: Many secondary results live in footnotes that cite appendix tables (robust clustering, transitions, years of s |
| `main_result_first` | 1 | 17% | restud_2026_restud_rdaf071 p.10-38 Sections 3, 4, 5: Each results section opens with a short data paragraph, then the equation, then the main table, then a titled  |
| `other:robustness_integrated_in_main_results` | 1 | 17% | jfe_2025_j_jfineco_2025_104150 p.11-16 Section 5.1: Robustness to alternative econometric approaches (matching, overlap-weighting, synthetic control) is integrate |
| `robustness_separate_section` | 1 | 17% | jpe_2026_742424 p.27-29 Section VI precedes Section VII: Simulation evidence assessing when the method works well or poorly is placed in its own section immediately be |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 4 | aer_111_12_8 s1.se.cluster_level (paper: The paper's variance estimators (bootstrap, jackknife, placebo) resamp / card: s1.se.cluster_level is null across all specifications, consistent with); jfe_2025_j_jfineco_2025_104150 specifications.s1.se.cluster_level (paper: Table 4 notes state standard errors clustered at the firm level / card: s1.se.cluster_level = [id_firm]) |
| cluster_level | unknown | 1 | jpe_2026_742424 s1.se.cluster_level (paper: The paper does not cluster standard errors at any group level; the rel / card: s1.se.cluster_level is null.) |
| cluster_level | disagree | 1 | restud_2026_restud_rdaf071 s2.se.cluster_level (paper: Village level for village-level DID and imputation estimates (Table 2  / card: s2 records cluster by kab (district); s4 shows no cluster option.) |
| comparison_group | paper_only | 2 | jfe_2025_j_jfineco_2025_104150 specifications.s1.comparison_group (paper: Comparison group is explicitly defined as never-SLL-issuer control fir / card: s1.comparison_group and s2.comparison_group are both null); jpe_2026_742424 specifications[0,0].comparison_group (paper: The set of comparison units is explicitly named in a footnote as a spe / card: No comparison_group field is populated in any specification (compariso) |
| comparison_group | agree | 1 | restud_2026_restud_rdaf071 s3 (paper: Event-study leads and lags from minus five to plus ten with the period / card: s3 includes inpresXdec1 to dec3 and dec5 to dec10 with dec4 omitted (s) |
| controls | paper_only | 3 | aer_111_12_8 specifications[].controls_summary (paper: A footnote describes an optional covariate-adjustment procedure (resid / card: controls_summary is null on every specification, and no specification'); jfe_2024_j_jfineco_2024_103809 s2.controls_summary (paper: Even-numbered columns of the main tables add a stated set of firm-leve / card: s2.controls_summary is null.) |
| controls | agree | 1 | restud_2026_restud_rdag011 s2.controls; s4.controls (paper: Three blocks: trade, policy, neighbour use; log controls added for log / card: $Tradecontrols $PolicyControls $NeighbourControls clearingbanks; $LogC) |
| data_source | agree | 4 | aer_111_12_8 data[0] (california_prop99) (paper: The California application is sourced from a well-known cigarette-tax  / card: The data entry for california_prop99 records type=admin, access=public); aer_111_12_8 data[1] (CPS) (paper: The CPS placebo study is built from average log wages in the Current P / card: The CPS data entry records type=survey, access=public, unit_of_observa) |
| data_source | paper_only | 3 | jfe_2024_j_jfineco_2024_103809 data[0].source_hint (paper: Financial and board data are described as hand-collected from named ar / card: data[0].source_hint and data[1].source_hint are null; the card records); jfe_2025_j_jfineco_2025_104150 data.panel_firmyear.source_hint (paper: Appendix Table A.1 attributes variables to named commercial sources: D / card: data record panel_firmyear has type=null, access=unknown, source_hint=) |
| diagnostic | agree | 4 | aer_111_12_8 x1 (paper: No formal pre-trend statistical test is reported; pre-treatment fit is / card: x1 records kind=pretrend_plot with status=not_found_in_scope, noting t); jfe_2025_j_jfineco_2025_104150 diagnostics.x2 (paper: Table 5 reports covariate balance (assets, leverage, ROA, Q, ESG score / card: diagnostics x2 (balance) status=observed, describing a clttest of size) |
| diagnostic | paper_only | 3 | jfe_2024_j_jfineco_2024_103809 diagnostics (paper: The paper reports a pre-trends figure, a covariate-balance table, and  / card: diagnostics is an empty list in the card.); jfe_2025_j_jfineco_2025_104150 diagnostics.x1.status (paper: Text states that the event-study plot shows parallel pre-issuance tren / card: diagnostics x1 (pretrend_test) has status=unknown, only noting that pr) |
| estimator | agree | 10 | aer_111_12_8 s1 (paper: SDID is defined by equations (1) and (4)-(6) and summarized as Algorit / card: s1 records estimator=synthetic_did, command=synthdid_estimate, called ); aer_111_12_8 s4 (paper: The matrix-completion (MC) estimator is described as imputing missing  / card: s4 records estimator=other:matrix_completion, command=mc_estimate, mat) |
| estimator | paper_only | 3 | jfe_2024_j_jfineco_2024_103809 designs (paper: Coarsened Exact Matching (Iacus et al., 2012) is described as a fourth / card: The card's designs and specifications list only d1/d2/d3 (return_event); jfe_2025_j_jfineco_2025_104150 designs.d1.method (paper: Identification combines a panel OLS quasi-DID, a propensity-score matc / card: d1 records only method=event_study with role, variant, treatment and c) |
| fixed_effects | agree | 4 | jfe_2025_j_jfineco_2025_104150 specifications.s1.fixed_effects (paper: Table 4 col. 1/4/7 lists Country x Year FE and Industry x Year FE as t / card: s1.fixed_effects = [id_cyear, id_indyear] from tab4.do line 39); jfe_2025_j_jfineco_2025_104150 specifications.s2.fixed_effects (paper: Table 6 notes list Firm x Cohort FE and Year x Cohort FE for the stack / card: s2.fixed_effects = [id_firmpair, id_yearpair] from fig4.do line 15) |
| fixed_effects | paper_only | 2 | aer_111_12_8 s1.fixed_effects (paper: The SDID objective (equation 1) explicitly includes a unit fixed effec / card: s1.fixed_effects is null; the card does not record which fixed effects); jfe_2024_j_jfineco_2024_103809 s2.fixed_effects (paper: The difference-in-differences specification includes firm fixed effect / card: s2.fixed_effects is null in the card's structured fields, even though ) |
| outputs | paper_only | 2 | jfe_2025_j_jfineco_2025_104150 outputs.tables (paper: Paper presents eleven main numbered tables and six main numbered figur / card: outputs.tables and outputs.figures are both empty arrays); jpe_2026_742424 outputs.tables; outputs.figures (paper: The paper contains a small number of numbered tables and figures prese / card: outputs.tables and outputs.figures are both empty arrays.) |
| outputs | agree | 1 | aer_111_12_8 outputs.tables, outputs.figures (paper: The paper presents four main numbered tables (California estimates; CP / card: outputs.tables lists t1-t4 matching the same four tables in the same o) |
| outputs | code_only | 1 | restud_2026_restud_rdaf071 outputs (paper: Nine main tables and eight main figures plus appendix tables A.1 to A. / card: Two tables (table1, table2 via estout) and one figure (figure2 twoway)) |
| outputs | unknown | 1 | restud_2026_restud_rdag011 outputs (paper: Seven main tables and seven main figures plus appendix tables A1 to A5 / card: tables=8 figures=3) |
| robustness | paper_only | 4 | jfe_2024_j_jfineco_2024_103809 robustness (paper: The paper describes an extensive robustness program spanning alternati / card: robustness is an empty list in the card.); jfe_2025_j_jfineco_2025_104150 robustness (paper: Paper reports multiple named robustness checks: log-transformed ESG sc / card: card robustness array is empty) |
| robustness | disagree | 1 | aer_111_12_8 robustness (paper: Table 2 reports an extensive set of robustness-style simulation varian / card: The card's robustness array is empty, recording no robustness checks f) |
| robustness | agree | 1 | jpe_2026_742424 specifications[1,1].notes; specifications[2,2].notes; specifications[3,3].notes (paper: The paper frames its comparison to difference-in-differences, subsampl / card: The card's top-level robustness array is empty, but the same three com) |
| sample | paper_only | 2 | jfe_2024_j_jfineco_2024_103809 pipeline.sample_restrictions (paper: The difference-in-differences analysis is run on a balanced panel of f / card: pipeline.sample_restrictions is an empty list and s1/s2/s3 sample fiel); jpe_2026_742424 data[0,0].period; data[0,0].unit_of_observation (paper: The paper states the pre-treatment period is a specific multiple of th / card: The data record gives only the overall panel period and leaves unit_of) |
| sample | agree | 2 | restud_2026_restud_rdaf071 s1.sample, s4.sample (paper: Balanced panels from 1960 to 1999. / card: s1 and s4 restrict est_year or year to 1960 through 1999.); restud_2026_restud_rdag011 s1.sample; s4.sample (paper: Developing economies below an income threshold; Iran dropped; Mongolia / card: if em_tag==1 filter; s4 excludes MNG) |
| se_type | agree | 5 | aer_111_12_8 s1.se.type (paper: The California results table's notes state directly that the 'placebo  / card: s1.se.type is recorded as randomization_inference with details describ); jfe_2024_j_jfineco_2024_103809 s2.se.cluster_level (paper: Baseline panel regressions (returns, volatility, risk-adjusted returns / card: s2.se.type is cluster with cluster_level firm.) |
| se_type | paper_only | 1 | jfe_2024_j_jfineco_2024_103809 specifications (paper: The firm-year dividend regressions and the media-coverage regression a / card: No specification in the card corresponds to the dividend regression or) |
| se_type | disagree | 1 | jpe_2026_742424 s1.se.type (paper: Inference for the main estimator is described as a self-normalized t-s / card: Specification s1's se.type field is recorded as 'cluster' with cluster) |
| weights | unknown | 2 | restud_2026_restud_rdaf071 s1.weights (paper: No weights mentioned in main text or notes. / card: No weights recorded (null).); restud_2026_restud_rdag011 s1.weights (paper: No regression weights mentioned / card: w=None for all specs) |
| weights | agree | 1 | aer_111_12_8 s2.weights, s3.weights, s5.weights (paper: SC is defined as the same weighted objective with the time weights fix / card: s2.weights, s3.weights, and s5.weights record exactly these constraine) |
| weights | paper_only | 1 | jfe_2025_j_jfineco_2025_104150 specifications.s1.weights (paper: Section 5.1 and Table 7 describe overlap-weighted regressions using pr / card: Neither s1 nor s2 records a weighting specification, and no specificat) |

## Gaps the readers reported

- (1) A footnote (page 4) references a further comparison table ('Table 6') of regularization choices for SC/DIFP; that table 
- (1) No empirical subgroup or heterogeneity analysis of treatment effects is reported; the general model in Section III permi
- (1) No preregistration, IRB approval, or research-ethics statement appears anywhere in the text; all analyses use secondary 
- (1) No analytic cluster-robust standard error at a named grouping level is used or discussed anywhere; all variance estimato
- (1) There is no separate concluding section; the paper moves directly from the related-work discussion into a technical appe
- (1) The paper does not name the statistical software or packages used for estimation anywhere in the main text (the CRediT s
- (1) No explicit justification is given for choosing firm-level clustering as opposed to, for example, addressing serial corr
- (1) No preregistration, pre-analysis plan, IRB approval, or consent statement is present or expected, consistent with this b
- (1) The recipe card (coverage: minimal) does not record a design or specification for the Coarsened Exact Matching strategy,
- (1) No passage in the main text justifies clustering standard errors at the firm level specifically (versus country, industr
- (1) No preregistration, pre-analysis plan, or IRB/ethics statement is present anywhere in the text; the study uses secondary
- (1) Main regression tables (e.g., Tables 4, 6, 8) report N and adjusted R2 but do not include a row for the mean of the depe
- (1) No passage discusses a multiple-testing or multiple-comparisons adjustment despite many subgroup and successive robustne
- (1) The paper's main text and appendix never name the statistical software or estimation package used; this is only recovera
- (1) The recipe card's coverage is partial (9 of 26 pipeline scripts read), so several paper-stated robustness and diagnostic
- (1) No heterogeneous-treatment-effect analysis across sub-populations or interaction terms is reported; the only heterogenei
- (1) No mechanism evidence (intermediate outcomes, survey evidence, or model-guided channel tests) is reported; the paper is 
- (1) No preregistration, institutional review board statement, or consent statement is present or expected, consistent with a
- (1) No multiple-testing adjustment or randomization-inference procedure is discussed as an alternative inferential safeguard
- (1) The online appendix sections (labeled A through H in the text) that contain the full random-treatment-status proofs, add
- (1) No formal balance table, density test, or attrition analysis is reported, consistent with a single-treated-unit aggregat
- (1) No explicit justification for the cluster level beyond stating it; no discussion of the number of clusters for district-
- (1) No multiple testing adjustment mentioned despite many outcomes and an index only for piety.
- (1) No software or package names in the main text (reghdfe, did_imputation, sdid appear only in code).
- (1) No summary statistics table in the main text; appendix D data description not in the PDF.
- (1) Online appendix (tables A.1 to A.27, Appendices B, C, D) is not included in the text file, so appendix practices are rec
- (1) No preregistration, IRB, or ethics statement for the oral histories.
- (1) No explicit justification for clustering at the country level beyond stating it.
- (1) No balance table or covariate comparison between treated and control countries in the main text.
- (1) No software or package named for the estimators.

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
