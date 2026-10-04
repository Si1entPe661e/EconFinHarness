# Reported practice: `panel_fe` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 19 paper notes (19 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | ReStud: 7, AER: 3, RFS: 3, JFE: 2, QJE: 2, Econometrica: 1, JPE: 1 |
| year | 2020: 1, 2023: 1, 2024: 2, 2025: 8, 2026: 7 |
| papers with at least one observation in category | presentation_convention: 13, writing_structure: 13, variable_construction: 12, mechanism_evidence: 12, data_access: 12, inference_justification: 11, replication_statement: 11, sample_construction: 10, specification_reporting: 10, design_statement: 9, magnitude_interpretation: 9, limitation_stated: 8, robustness_reported: 7, heterogeneity_reported: 5, diagnostic_reported: 4, external_validity: 4, preregistration_or_ethics: 2, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_110_5_5 | AER | 2020 | full | yes | ba894e9a73c0 |
| aer_113_1_1 | AER | 2023 | full | yes | 9605da76b424 |
| aer_115_1_8 | AER | 2025 | full | yes | 8a6595f30461 |
| ecta_92_2_2 | Econometrica | 2024 | full | yes | 97ec8a0d772e |
| jfe_2025_j_jfineco_2025_104150 | JFE | 2025 | full | yes | d509ecfbe6d0 |
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | full | yes | e0a76ce6a2d4 |
| jpe_2026_740226 | JPE | 2026 | full | yes | 3af7c18d2956 |
| qje_140_1_11 | QJE | 2025 | full | yes | d071a02501be |
| qje_140_1_4 | QJE | 2025 | partial | yes | 793bd3a24ebb |
| restud_2025_restud_rdae072 | ReStud | 2025 | full | yes | b59e78835737 |
| restud_2025_restud_rdae091 | ReStud | 2025 | full | yes | e71c807b7f7a |
| restud_2025_restud_rdaf104 | ReStud | 2025 | full | yes | 6bb0c12a5f7d |
| restud_2026_restud_rdaf027 | ReStud | 2026 | full | yes | e5e02c526e90 |
| restud_2026_restud_rdaf044 | ReStud | 2026 | full | yes | 0021518efed4 |
| restud_2026_restud_rdag013 | ReStud | 2026 | full | yes | b781b6e5a7dc |
| restud_2026_restud_rdag056 | ReStud | 2026 | full | yes | ae6242059491 |
| rfs_2024_rfs_hhae045 | RFS | 2024 | full | yes | 5e68c13b1e2d |
| rfs_2025_rfs_hhaf065 | RFS | 2025 | full | yes | 81ac783c5036 |
| rfs_2026_rfs_hhag042 | RFS | 2026 | full | yes | d63dc3bb1fac |

Excluded (paper-level hold-out `harness/paradigms/panel_fe/reported.md`, not used for this method's skill evidence): aer_113_3_2, rfs_2026_rfs_hhaf081. Their notes still count in `_all`.

## Practices by category and tag


### data_access (papers with this category: 12/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 8 | 42% | aer_113_1_1 p.1-7 Acknowledgment footnote; Section II: Describes its primary dataset as administrative regulatory data collected by a federal drug-enforcement agency; jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold |
| `public_use` | 6 | 32% | aer_110_5_5 p.8-14 Section II: The analysis panel combines an original primary survey of radio-station characteristics and messaging content ; aer_113_1_1 p.1-7 Acknowledgment footnote; Section II: Describes its primary dataset as administrative regulatory data collected by a federal drug-enforcement agency |
| `commercial` | 5 | 26% | aer_113_1_1 p.26-26 Section V.B: Identifies the corporate-ownership database used to locate pharmacy headquarters as a commercial private-compa; jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold |
| `data_restricted` | 5 | 26% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Beyond the deposited replication data, several auxiliary series used in the analysis are described as shared d; jpe_2026_740226 p.10-10 Section III, Data: Characterizes all six underlying data sources as government administrative records rather than survey-collecte |
| `linked_records` | 4 | 21% | aer_110_5_5 p.8-14 Section II: The analysis panel combines an original primary survey of radio-station characteristics and messaging content ; qje_140_1_11 p.15-15 Section III.B: The paper describes its individual-level data as coming from linked Swedish government administrative register |
| `in_main_text` | 1 | 5% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `other:archival_transcription` | 1 | 5% | rfs_2025_rfs_hhaf065 p.1-9 Acknowledgements, Section 1.2: Data are hand-transcribed from historical archival records (registers, passbooks, resolution ledgers); a trans |
| `other:regulator_administrative_data` | 1 | 5% | restud_2026_restud_rdag013 p.8-9 Section 2.3: Data come from the state environmental regulator's administrative records (identifiers, scores, inspections, v |
| `other:satellite_imagery` | 1 | 5% | restud_2025_restud_rdaf104 p.9-29 Section 3; footnotes 18, 47; Section 4.1: Data are public-use administrative and census sources, hand-verified bridge records with satellite imagery, th |
| `survey_collected` | 1 | 5% | aer_110_5_5 p.8-14 Section II: The analysis panel combines an original primary survey of radio-station characteristics and messaging content  |

### design_statement (papers with this category: 9/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `threats_discussed` | 7 | 37% | aer_110_5_5 p.14-15 Section III: The paper argues against endogenous antenna placement as a threat to identification by controlling for distanc; aer_113_1_1 p.23-23 Section V.A, equation (4) discussion: Acknowledges that its competition regressions cannot be given a causal interpretation because the count of nea |
| `estimand_named` | 5 | 26% | aer_110_5_5 p.16-17 Section III, closing paragraph: Because individual reception of radio messages cannot be observed, the authors state that their coefficient sh; ecta_92_2_2 p.13-13 Section 4.1, ex post specification: Defines a second estimand adding a realized-flood indicator and its interaction with treatment, described as s |
| `design_variant_named` | 4 | 21% | aer_110_5_5 p.14-15 Section III, opening paragraphs: The identification strategy is stated as resting on three sources of plausibly exogenous variation: topography; aer_113_1_1 p.23-23 Section V.A: Distinguishes a within-pharmacy competition specification, which combines a mechanical division-of-prescriptio |
| `identifying_assumption_explicit` | 4 | 21% | aer_110_5_5 p.14-15 Section III, opening paragraphs: The identification strategy is stated as resting on three sources of plausibly exogenous variation: topography; restud_2025_restud_rdae072 p.9-10 Section 3.1, equations (1)-(2): The firm-level empirical framework writes relative demand as a function of relative capacity and relative pric |
| `in_main_text` | 4 | 21% | restud_2025_restud_rdae072 p.9-10 Section 3.1, equations (1)-(2): The firm-level empirical framework writes relative demand as a function of relative capacity and relative pric; restud_2025_restud_rdaf104 p.2-3 Section 1: The paper states two complementary quasi-experimental strategies for the same geography: variation in where br |
| `identification_caveat` | 1 | 5% | restud_2026_restud_rdag013 p.12-12 Section 3.3: After the descriptive deterrence regressions the authors state that a causal relationship cannot be ascertaine |
| `in_footnote` | 1 | 5% | aer_110_5_5 p.16-16 footnote 19: Exogeneity of the messaging-intensity measure is checked directly using household survey data, testing whether |
| `other:hypotheses_formalized` | 1 | 5% | rfs_2024_rfs_hhae045 p.9-13 Sections 1.3, 1.4: Hypotheses are numbered (H1 to H4b) and derived from institutional theory before any data are shown; one hypot |
| `other:institutional_narrative_supports_exogeneity` | 1 | 5% | restud_2025_restud_rdaf104 p.20-21 Section 5.1: Exogeneity of bridge opening timing is argued with historical narrative: named examples of decades-long lags b |

### diagnostic_reported (papers with this category: 4/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 4 | 21% | aer_110_5_5 p.31-31 Section IV.D: A placebo diagnostic randomly reassigns antenna locations across many simulated draws and re-estimates the ben; jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5, Appendix Fig. A.1 referenced: A time-series plot of the intermediary shock variables is placed in an appendix figure and referenced from the |
| `in_main_text` | 2 | 10% | aer_110_5_5 p.30-31 Section IV.D: A circular-coverage falsification control (predicted signal reach absent topographic obstruction) is added to ; restud_2025_restud_rdaf104 p.22-26 Section 5.1; Table 4 columns 2 and 4; Figure 10: Lead coefficients on future changes in bridge distance are shown in separate table columns with a joint p-valu |
| `balance_table` | 1 | 5% | aer_110_5_5 p.16-16 footnote 19: An indirect exogeneity check tests whether pre-existing household characteristics from a household survey pred |
| `in_footnote` | 1 | 5% | aer_110_5_5 p.16-16 footnote 19: An indirect exogeneity check tests whether pre-existing household characteristics from a household survey pred |
| `other:falsification_control` | 1 | 5% | aer_110_5_5 p.30-31 Section IV.D: A circular-coverage falsification control (predicted signal reach absent topographic obstruction) is added to  |
| `other:heterogeneous_responsiveness_check` | 1 | 5% | restud_2026_restud_rdag013 p.11-18 Sections 3.3 and 5.1.1: An appendix table is cited to support a modelling assumption (increasing differences) by showing that high-vio |
| `other:placebo_antenna_relocation` | 1 | 5% | aer_110_5_5 p.31-31 Section IV.D: A placebo diagnostic randomly reassigns antenna locations across many simulated draws and re-estimates the ben |
| `other:weighting_scheme_diagnostic` | 1 | 5% | restud_2025_restud_rdaf104 p.23-23 Section 5.1; Appendix Figure C20: The paper notes that the panel estimate is a variance-weighted average of heterogeneous effects and shows in a |
| `placebo_outcomes` | 1 | 5% | aer_110_5_5 p.29-30 Section IV.D: Spillover diagnostics using two additional conflict datasets test whether messaging affects violence unrelated |
| `pre_trends_plot` | 1 | 5% | restud_2025_restud_rdaf104 p.22-26 Section 5.1; Table 4 columns 2 and 4; Figure 10: Lead coefficients on future changes in bridge distance are shown in separate table columns with a joint p-valu |
| `pre_trends_test` | 1 | 5% | restud_2025_restud_rdaf104 p.22-26 Section 5.1; Table 4 columns 2 and 4; Figure 10: Lead coefficients on future changes in bridge distance are shown in separate table columns with a joint p-valu |

### external_validity (papers with this category: 4/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 4 | 21% | aer_110_5_5 p.1-32 Introduction footnote 1; Section V: The conclusion frames the intervention as a generalizable low-cost counterinsurgency tool for remote, low-stat; jfe_2026_j_jfineco_2025_104223 p.22-22 Section 6, Conclusion: In the conclusion, the author frames the equity-market estimates as a likely lower bound on the quantitative i |
| `site_specific` | 2 | 10% | aer_110_5_5 p.1-32 Introduction footnote 1; Section V: The conclusion frames the intervention as a generalizable low-cost counterinsurgency tool for remote, low-stat; jpe_2026_740226 p.43-44 Section VII, Conclusions: Discusses generalizability by contrasting the program's mandatory, near-universal exit exam and existing means |
| `in_appendix` | 1 | 5% | aer_110_5_5 p.1-32 Introduction footnote 1; Section V: The conclusion frames the intervention as a generalizable low-cost counterinsurgency tool for remote, low-stat |

### heterogeneity_reported (papers with this category: 5/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `split_sample` | 5 | 26% | aer_110_5_5 p.25-26 Section IV.C, "Further Heterogeneity": A battery of cross-sectional heterogeneity splits, by country, distance to border, terrain ruggedness, climate; aer_113_1_1 p.24-25 Table 6, panels B and C: Splits the competition analysis by the source of nearby competition, separately estimating effects of competit |
| `mechanism_motivated` | 4 | 21% | aer_110_5_5 p.24-25 Table 4; Section IV.C: Heterogeneity by economic shocks is estimated through interaction terms added directly to the benchmark specif; aer_113_1_1 p.24-25 Table 6, panels B and C: Splits the competition analysis by the source of nearby competition, separately estimating effects of competit |
| `in_appendix` | 2 | 10% | aer_110_5_5 p.25-26 Section IV.C, "Further Heterogeneity": A battery of cross-sectional heterogeneity splits, by country, distance to border, terrain ruggedness, climate; restud_2025_restud_rdaf104 p.19-27 Section 4.2; Section 5.2; Appendix Tables C3, C10 to C12; Appendix Figure C23: Heterogeneity is reported by river segment and river bank, by rail versus road bridges, by halves of the study |
| `exploratory_labelled` | 1 | 5% | aer_110_5_5 p.25-26 Section IV.C, "Further Heterogeneity": A battery of cross-sectional heterogeneity splits, by country, distance to border, terrain ruggedness, climate |
| `in_main_text` | 1 | 5% | rfs_2025_rfs_hhaf065 p.21-32 Tables 4 and 6: Structural breaks and closure regressions are estimated separately by race, local status, organization status  |
| `interaction` | 1 | 5% | aer_110_5_5 p.24-25 Table 4; Section IV.C: Heterogeneity by economic shocks is estimated through interaction terms added directly to the benchmark specif |
| `other:intensity_bin_dose_response` | 1 | 5% | aer_110_5_5 p.22-23 Figure 6; Section IV.A: The continuous treatment variable is discretized into several intensity-interval dummy variables to visualize  |

### inference_justification (papers with this category: 11/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_justification_found` | 7 | 37% | aer_113_1_1 p.10-10 Table 2 notes; Sections II-V: Reports zip-code-level clustering of standard errors in every table's notes but does not give an explicit text; aer_115_1_8 p.12-24 Tables 2, 3, 6 notes: Beyond naming the clustering level in each table's notes, the text gives no explicit discussion of why zip cod |
| `cluster_at_unit_level` | 4 | 21% | qje_140_1_11 p.35-35 Table V notes: For the survey-panel regressions relating search to job finding, standard errors are instead clustered at the ; restud_2025_restud_rdae072 p.9-12 Table 4 notes, Table 5 notes, Table 6 notes: Standard errors are clustered at the firm level in the fixed-effects and IV tables and left as default OLS err |
| `in_appendix` | 3 | 16% | aer_110_5_5 p.16-16 Section III: The text states that results are robust to alternative spatial cutoffs for the HAC correction and to conventio; restud_2025_restud_rdaf104 p.19-28 Section 4.3; Section 5.3 Non-random exposure; Appendix Figures C17, C25; footnote 28: Two shock-based inference exercises are reported: random flipping of confluence orientation for half the confl |
| `in_footnote` | 3 | 16% | aer_110_5_5 p.15-16 footnote 20: The spatial-HAC correction is implemented using code adapted from a named prior study, credited explicitly in ; restud_2025_restud_rdae072 p.7-9 Table 1 notes, Table 3 notes, footnote 11: Uncertainty for the cyclical correlation coefficients in the descriptive tables is reported as estimated stand |
| `in_main_text` | 3 | 16% | restud_2025_restud_rdae072 p.9-12 Table 4 notes, Table 5 notes, Table 6 notes: Standard errors are clustered at the firm level in the fixed-effects and IV tables and left as default OLS err; restud_2025_restud_rdaf104 p.23-23 Section 5.1: Panel standard errors are clustered by county to allow arbitrary serial correlation, cited to Bertrand et al.  |
| `cluster_at_assignment_level` | 2 | 10% | aer_115_1_8 p.24-24 Table 6 notes: The cap regression clusters standard errors at the hospice firm level, matching the level of the cap-pressure ; ecta_92_2_2 p.13-13 Section 4.1, baseline specification paragraph: States as a general rule for the household-level analysis that standard errors are always clustered at the bra |
| `randomization_inference` | 2 | 10% | ecta_92_2_2 p.14-14 Table I and subsequent result tables: Reports randomization-inference p-values alongside cluster-robust standard errors throughout the results table; restud_2025_restud_rdaf104 p.19-28 Section 4.3; Section 5.3 Non-random exposure; Appendix Figures C17, C25; footnote 28: Two shock-based inference exercises are reported: random flipping of confluence orientation for half the confl |
| `spatial_hac` | 2 | 10% | aer_110_5_5 p.15-16 Section III: Standard errors are computed using a spatial-HAC correction attributed to Conley and Hsiang, explicitly justif; restud_2025_restud_rdaf104 p.23-23 Section 5.1: Panel standard errors are clustered by county to allow arbitrary serial correlation, cited to Bertrand et al.  |
| `twoway_cluster` | 2 | 10% | jfe_2026_j_jfineco_2025_104223 p.14-14 Table 7, footnote 23: The stock-level panel regressions state that standard errors are clustered by both firm and time, explaining t; rfs_2026_rfs_hhag042 p.33-39 Section 5.5; Section 6.1; Table 14 notes: Panel regressions for volume and volatility double-cluster by month and firm, and the earnings-announcement da |
| `alt_se` | 1 | 5% | rfs_2025_rfs_hhaf065 p.16-16 Footnote 15: Standard errors are clustered by branch; a footnote acknowledges the small number of clusters, cites Abadie et |
| `few_clusters_addressed` | 1 | 5% | rfs_2025_rfs_hhaf065 p.16-16 Footnote 15: Standard errors are clustered by branch; a footnote acknowledges the small number of clusters, cites Abadie et |
| `other:varhac_se_for_correlations` | 1 | 5% | restud_2025_restud_rdae072 p.7-9 Table 1 notes, Table 3 notes, footnote 11: Uncertainty for the cyclical correlation coefficients in the descriptive tables is reported as estimated stand |

### limitation_stated (papers with this category: 8/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `interpretation_caveat` | 6 | 32% | aer_110_5_5 p.16-17 Section III: Because individual reception of messages cannot be observed, the authors explicitly limit their causal claim t; jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and  |
| `data_coverage` | 5 | 26% | aer_110_5_5 p.16-16 Section III: The authors acknowledge that conflict-event reporting may correlate with local media coverage, but argue that ; aer_113_1_1 p.26-26 Section V.B: Notes that the corporate-ownership database used to locate headquarters reflects only a recent snapshot in tim |
| `measurement` | 5 | 26% | aer_110_5_5 p.16-16 Section III: The authors acknowledge that conflict-event reporting may correlate with local media coverage, but argue that ; aer_113_1_1 p.26-26 Section V.B, footnote 21: Acknowledges that its name-and-state matching rule for grouping stores into multistore firms is an imperfect p |
| `identification_caveat` | 4 | 21% | aer_110_5_5 p.26-27 footnote 34: The authors state directly that their economic-channel narrative for the commodity-shock heterogeneity results; aer_113_1_1 p.23-23 Section V.A: States plainly that neither the pooled nor the source-decomposed competition regressions should be read as ide |
| `in_main_text` | 2 | 10% | restud_2025_restud_rdaf104 p.23-25 Section 5.1; Section 5.2; footnote 43: Three reasons the land value proxy likely understates effects are enumerated (measurement error, urban land un; rfs_2025_rfs_hhaf065 p.3-3 Introduction: The introduction has a dedicated paragraph on data limitations: closure timing is unobserved, passbooks and ba |
| `external_validity` | 1 | 5% | qje_140_1_11 p.45-45 Section VII: The authors flag that their cost-side production-efficiency estimate applies to a specific high-age, long-tenu |
| `in_footnote` | 1 | 5% | restud_2025_restud_rdae072 p.1-1 footnote 1, Figure 1: The downward trend in the aggregate utilization series is acknowledged in the first footnote; the author state |
| `selection` | 1 | 5% | rfs_2025_rfs_hhaf065 p.3-3 Introduction: The introduction has a dedicated paragraph on data limitations: closure timing is unobserved, passbooks and ba |

### magnitude_interpretation (papers with this category: 9/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `relative_to_mean` | 5 | 26% | aer_113_1_1 p.10-10 Table 2 notes: Interprets every reported coefficient in percentage terms relative to the mean of the dependent variable, pres; restud_2025_restud_rdaf104 p.17-24 Section 4.2; Section 5.2: Log-point coefficients are converted to percentage differences in the text, effects on income are scaled by ef |
| `sd_units` | 4 | 21% | aer_110_5_5 p.18-21 Section IV.A; footnote 25: Effect sizes are consistently interpreted in terms of a one-standard-deviation change in the standardized trea; jfe_2026_j_jfineco_2025_104223 p.9-16 throughout Section 4: Coefficients are consistently interpreted relative to a one-standard-deviation change in the standardized shoc |
| `compared_to_literature` | 3 | 16% | qje_140_1_11 p.37-37 Section V, end: Estimates of the relative return to job search obtained from three distinct designs are compared to each other; restud_2025_restud_rdaf104 p.17-24 Section 4.2; Section 5.2: Log-point coefficients are converted to percentage differences in the text, effects on income are scaled by ef |
| `back_of_envelope` | 2 | 10% | aer_110_5_5 p.21-22 Section IV.B: Aggregate impact is interpreted through counterfactual predicted outcomes constructed from a more flexible fun; qje_140_1_11 p.44-46 Section VII, equations (11)-(12): The paper's headline net-production-efficiency figure is expressed in units of a monthly wage and then transla |
| `in_main_text` | 2 | 10% | rfs_2025_rfs_hhaf065 p.16-31 Sections 2.2 and 4.1: Closure effects are interpreted relative to the baseline closure probability given by the constant, and Poisso; rfs_2026_rfs_hhag042 p.16-33 Section 3.1; Section 3.4; Section 5.5: Economic magnitude of the regression slope is translated by multiplying the average slope by the decile spread |
| `precision_discussed` | 2 | 10% | jfe_2026_j_jfineco_2025_104223 p.9-18 throughout Section 4: Alongside point estimates, the paper repeatedly reports the associated t-statistics and describes estimates as; qje_140_1_11 p.37-37 Section V, end: Estimates of the relative return to job search obtained from three distinct designs are compared to each other |
| `cost_benefit` | 1 | 5% | qje_140_1_11 p.44-46 Section VII, equations (11)-(12): The paper's headline net-production-efficiency figure is expressed in units of a monthly wage and then transla |
| `elasticity` | 1 | 5% | restud_2025_restud_rdaf104 p.17-24 Section 4.2; Section 5.2: Log-point coefficients are converted to percentage differences in the text, effects on income are scaled by ef |
| `in_appendix` | 1 | 5% | aer_110_5_5 p.21-22 Section IV.B: Aggregate impact is interpreted through counterfactual predicted outcomes constructed from a more flexible fun |
| `monetary_terms` | 1 | 5% | qje_140_1_11 p.44-46 Section VII, equations (11)-(12): The paper's headline net-production-efficiency figure is expressed in units of a monthly wage and then transla |
| `other:decomposition_of_effects` | 1 | 5% | restud_2025_restud_rdaf104 p.25-25 Section 5.2; footnote 44; Appendix Figure C22, Table C7: Effects on total activity are decomposed into population and per capita components by comparing land value and |
| `other:implied_effects_from_combined_regressions` | 1 | 5% | restud_2026_restud_rdag013 p.10-12 Sections 3.2, 3.3 and Figure 2: Descriptive coefficients are translated into implied inspection probabilities and deterrence effects for a 'cl |

### mechanism_evidence (papers with this category: 12/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `intermediate_outcomes` | 7 | 37% | aer_110_5_5 p.18-19 Section IV.A: A reduction in events characterized as violence against civilians and clashes, alongside the reduction in fata; jfe_2026_j_jfineco_2025_104223 p.19-20 Section 5.2, Table 10: A separate liquidity-based test uses stock-level illiquidity growth, rather than returns, as the dependent var |
| `suggestive_labelled` | 5 | 26% | aer_110_5_5 p.18-19 Section IV.A: A reduction in events characterized as violence against civilians and clashes, alongside the reduction in fata; aer_113_1_1 p.23-23 Section V.A: Explicitly labels its competition results as offering insight into incentives rather than as identifying a cau |
| `in_appendix` | 4 | 21% | aer_110_5_5 p.19-19 Section IV.A: An increase in looting under more intense messaging is interpreted as a survival-oriented response by remainin; aer_113_1_1 p.26-26 Section V.B, closing paragraph: States that it examined several other candidate explanations for the independent-chain gap, including differen |
| `ruled_out_alternatives` | 4 | 21% | aer_113_1_1 p.26-26 Section V.B, closing paragraph: States that it examined several other candidate explanations for the independent-chain gap, including differen; jfe_2026_j_jfineco_2025_104223 p.21-21 Section 5.3, Appendix Table A.7 referenced: A dedicated subsection adds fund-flow-based price-pressure controls from two specific prior papers to the base |
| `heterogeneity_as_mechanism` | 3 | 16% | aer_113_1_1 p.21-26 Section V, introduction to parts A and B: Presents the competition analysis and the headquarters-versus-branch comparison as two separate tests of two c; ecta_92_2_2 p.16-16 Section 5.1, Ex Post Outcomes discussion: Uses the split between the treatment coefficient and the treatment-flood interaction coefficient as the main d |
| `model_guided` | 3 | 16% | jfe_2026_j_jfineco_2025_104223 p.19-20 Section 5.2, Table 10: A separate liquidity-based test uses stock-level illiquidity growth, rather than returns, as the dependent var; jpe_2026_740226 p.30-33 Section IV.G: Frames the improvement in college value-added as the mechanism connecting the financial-aid shock to later ski |
| `in_main_text` | 1 | 5% | rfs_2026_rfs_hhag042 p.35-39 Section 6.1; Tables 13, 14: Mispricing versus risk is adjudicated by three steps: alphas across factor models, correlation with an existin |
| `other:companion_paper_design` | 1 | 5% | restud_2026_restud_rdaf044 p.28-29 Section 6.4; Tables D8 to D10: Peer effects are estimated with a different design from a companion paper (facility-by-year fixed effects, wit |
| `other:descriptive_evidence_sequence` | 1 | 5% | restud_2026_restud_rdag013 p.9-12 Section 3: Before the model, three descriptive facts are presented in sequence (within-firm correlation of violations, ta |

### other (papers with this category: 1/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 5% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |
| `other:conflict_disclosure` | 1 | 5% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |

### preregistration_or_ethics (papers with this category: 2/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `irb_stated` | 2 | 10% | aer_110_5_5 p.1-1 title-page acknowledgments: The acknowledgments state that ethics approval for the study, including the ex-combatant survey component, was; jpe_2026_740226 p.1-2 Acknowledgments footnote: States that the study received approval from a named university's institutional review board, citing a specifi |

### presentation_convention (papers with this category: 13/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `notes_state_se` | 8 | 42% | aer_115_1_8 p.12-24 Table notes throughout: Every regression table's notes state which fixed effects, controls, sample, endogenous or treatment variable, ; jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s |
| `stars_used` | 7 | 37% | jfe_2026_j_jfineco_2025_104223 p.9-16 Tables 4-11: Regression tables use a conventional multi-tier significance-star convention alongside t-statistics reported i; jpe_2026_740226 p.17-42 Tables 1-6 and notes: Places a standard-error-in-parentheses convention beneath each coefficient throughout every results table, and |
| `summary_stats_table` | 7 | 37% | aer_110_5_5 p.11-11 Table 1: The empirical presentation opens with a descriptive-statistics table reporting the mean, standard deviation, m; aer_113_1_1 p.9-9 Table 1: Opens the empirical analysis with a multi-panel summary statistics table that separately covers market concent |
| `notes_state_sample` | 6 | 32% | aer_115_1_8 p.12-24 Table notes throughout: Every regression table's notes state which fixed effects, controls, sample, endogenous or treatment variable, ; jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s |
| `appendix_tables_numbered_a` | 4 | 21% | jpe_2026_740226 p.8-8 Figure 1 caption: Labels every appendix table and figure with an A prefix and states, the first time an appendix item is cited, ; restud_2025_restud_rdaf104 p.5-30 Footnote 9; Section 5.3; Section 6: Appendix material is lettered (Appendix A data details, Appendix B measurement error derivation, Appendix C fi |
| `map` | 3 | 16% | aer_110_5_5 p.8-16 Figures 1, 2, 4 and 5: Spatial patterns in conflict incidence, radio coverage, and messaging intensity are visualized as choropleth m; aer_113_1_1 p.20-22 Figure 4; Figure 5: Uses choropleth-style maps to display the geographic distribution of both the top-diverting pharmacies and cou |
| `no_stars` | 3 | 16% | aer_110_5_5 p.17-18 Table 2: Coefficient estimates throughout the main tables are reported without significance stars; precision is conveye; aer_113_1_1 p.10-10 Table 2: Reports coefficients and standard errors in its regression tables without asterisks marking conventional signi |
| `coefficient_plot` | 2 | 10% | aer_110_5_5 p.22-26 Figures 6 and 7: Nonlinear treatment-response and interaction effects are presented as coefficient plots with stated confidence; restud_2025_restud_rdaf104 p.8-26 Figures 2, 9, 10; Table 1; Table 2 notes: Presentation combines maps of rivers, bridges and counties, an event-style coefficient plot with reversed axis |
| `in_appendix` | 2 | 10% | restud_2025_restud_rdaf104 p.5-30 Footnote 9; Section 5.3; Section 6: Appendix material is lettered (Appendix A data details, Appendix B measurement error derivation, Appendix C fi; rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `binscatter` | 1 | 5% | restud_2026_restud_rdag013 p.10-11 Figure 1, Tables 2 and 3: Binscatters with confidence bands are used for raw correlations; regression tables show standard errors in par |
| `event_study_figure` | 1 | 5% | restud_2025_restud_rdaf104 p.8-26 Figures 2, 9, 10; Table 1; Table 2 notes: Presentation combines maps of rivers, bridges and counties, an event-style coefficient plot with reversed axis |
| `in_main_text` | 1 | 5% | restud_2025_restud_rdae072 p.9-12 Tables 4, 5, 6 notes: Regression tables use three-level significance stars with thresholds defined in the notes; notes also state th |
| `online_appendix_not_available` | 1 | 5% | jpe_2026_740226 p.8-8 Figure 1 caption: Labels every appendix table and figure with an A prefix and states, the first time an appendix item is cited,  |
| `other:descriptive_table_of_policy_terms` | 1 | 5% | rfs_2025_rfs_hhaf065 p.13-13 Table 2: A descriptive table documents implied interest rates and minimum balances per dividend payment reconstructed f |
| `other:disclosure_examples_appendix` | 1 | 5% | rfs_2024_rfs_hhae045 p.48-50 Appendix A, Appendix B: Appendices provide a timeline of treatment and measurement windows and reproduced examples of actual disclosur |
| `other:setting_table` | 1 | 5% | restud_2026_restud_rdag056 p.5-6 Table 1; Figure 1: The setting is documented with a table listing each reform's date, duration rule and benefit change, and a fig |
| `other:timeline_appendix` | 1 | 5% | rfs_2024_rfs_hhae045 p.48-50 Appendix A, Appendix B: Appendices provide a timeline of treatment and measurement windows and reproduced examples of actual disclosur |
| `raw_data_plot` | 1 | 5% | rfs_2025_rfs_hhaf065 p.10-33 Figures 1 to 8, Tables 3 to 7: Figures are mainly raw time series (monthly averages, rolling seven-day averages, cumulative counts) with erro |

### replication_statement (papers with this category: 11/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 11 | 58% | aer_110_5_5 p.33-33 References: The reference list cites a replication data package deposited with a data archive under its own DOI, but the m; aer_113_1_1 p.32-32 References, Janssen and Zhang 2023 replication-data entry: Lists a formal replication-data citation with a persistent identifier in the reference list, following the jou |
| `data_public` | 6 | 32% | aer_110_5_5 p.33-33 References: The reference list cites a replication data package deposited with a data archive under its own DOI, but the m; jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title |
| `code_public` | 5 | 26% | jpe_2026_740226 p.44-44 Data Availability statement: Points readers to a named external replication package hosted on a data repository for the code that reproduce; restud_2025_restud_rdaf104 p.31-31 Data Availability: A data availability statement points to a Zenodo replication package with a DOI cited in the references, expla |
| `software_named` | 4 | 21% | qje_140_1_4 p.33-33 Section III.A.1: A commercial third-party software product is named and described for one specific analysis step, inferring an ; restud_2025_restud_rdaf104 p.23-23 Section 5.1: No statistical software is named; only the source of adapted spatial standard error code is credited. |
| `data_access_procedure_described` | 3 | 16% | jpe_2026_740226 p.44-44 Data Availability statement: States that the underlying administrative microdata are proprietary and names the specific government agencies; restud_2025_restud_rdaf104 p.31-31 Data Availability: A data availability statement points to a Zenodo replication package with a DOI cited in the references, expla |
| `data_restricted` | 3 | 16% | jpe_2026_740226 p.44-44 Data Availability statement: States that the underlying administrative microdata are proprietary and names the specific government agencies; restud_2025_restud_rdaf104 p.31-31 Data Availability: A data availability statement points to a Zenodo replication package with a DOI cited in the references, expla |
| `in_main_text` | 2 | 10% | restud_2025_restud_rdaf104 p.23-23 Section 5.1: No statistical software is named; only the source of adapted spatial standard error code is credited.; rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `online_appendix_not_available` | 1 | 5% | qje_140_1_4 p.69-69 Supplementary Material statement: The article repeatedly refers throughout the main text to an Online Appendix published separately at the journ |
| `other:software_not_named` | 1 | 5% | restud_2026_restud_rdag013 p.1-29 whole paper: No software or package is named in the main text for estimation or regressions. |
| `other:software_not_named_in_text` | 1 | 5% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: The manuscript text itself does not name the statistical software used to produce the reported estimates; the  |

### robustness_reported (papers with this category: 7/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 6 | 32% | aer_110_5_5 p.18-18 footnote 23: Nonlinear count-data estimators are mentioned in the main text as an additional robustness check on functional; ecta_92_2_2 p.18-18 Section 5.1, footnote 23, referencing Appendix Table A.17: Examines whether experiencing flood shocks in both experimental years erodes the value of guaranteed credit th |
| `alt_specification` | 5 | 26% | aer_110_5_5 p.17-18 Table 2, panel A1: A set of alternative control-set specifications, ranging from a minimal fixed-effects model through the benchm; ecta_92_2_2 p.18-18 Section 5.1, footnote 23, referencing Appendix Table A.17: Examines whether experiencing flood shocks in both experimental years erodes the value of guaranteed credit th |
| `alt_sample` | 4 | 21% | aer_110_5_5 p.12-12 Section II.C: The paper states that replacing grid cells with administrative district boundaries as the unit of analysis lea; restud_2025_restud_rdaf104 p.27-28 Section 5.3; Appendix Tables C8, C13, C14; Appendix Figure C26: Panel robustness paragraphs cover counties never building a bridge (spillover only), progressively more flexib |
| `alt_fixed_effects` | 2 | 10% | aer_110_5_5 p.31-31 footnote 38: Robustness is also assessed across a range of area fixed-effects structures, from no area fixed effects up to ; restud_2025_restud_rdaf104 p.27-28 Section 5.3; Appendix Tables C8, C13, C14; Appendix Figure C26: Panel robustness paragraphs cover counties never building a bridge (spillover only), progressively more flexib |
| `in_footnote` | 2 | 10% | qje_140_1_11 p.34-34 Section V, footnote 27: A footnote reports that adding individual fixed effects that vary by employment status to the search-hazard re; rfs_2025_rfs_hhaf065 p.28-28 Footnote 17: A footnote states that closure estimates from earlier periods are similar but less reliable because of record  |
| `in_main_text` | 2 | 10% | aer_110_5_5 p.17-18 Table 2, panel A1: A set of alternative control-set specifications, ranging from a minimal fixed-effects model through the benchm; restud_2025_restud_rdaf104 p.27-28 Section 5.3; Appendix Tables C8, C13, C14; Appendix Figure C26: Panel robustness paragraphs cover counties never building a bridge (spillover only), progressively more flexib |
| `alt_estimator` | 1 | 5% | aer_110_5_5 p.18-18 footnote 23: Nonlinear count-data estimators are mentioned in the main text as an additional robustness check on functional |
| `alt_se` | 1 | 5% | rfs_2025_rfs_hhaf065 p.17-32 Table 3 and Table 6 notes: Alternative clustering for the main tables is relegated to the Internet Appendix and flagged in table notes. |
| `other:measurement_error_attenuation_calculation` | 1 | 5% | restud_2025_restud_rdaf104 p.27-28 Section 5.3 More flexible time trends; footnote 45; Appendix B; Appendix Table C13: To interpret attenuation when adding regional trends, the author computes the share of measurement error in th |
| `summarized_in_one_table` | 1 | 5% | aer_110_5_5 p.17-18 Table 2, panel A1: A set of alternative control-set specifications, ranging from a minimal fixed-effects model through the benchm |

### sample_construction (papers with this category: 10/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 8 | 42% | aer_110_5_5 p.8-9 Section II.A, footnote 13: The radio-station survey covers the full set of stations broadcasting defection content during the study windo; aer_113_1_1 p.7-7 Section II: Uses pharmacy-level opioid order data from the DEA's Automation of Reports and Consolidated Orders System cove |
| `exclusions_justified` | 8 | 42% | aer_110_5_5 p.12-13 Section II.C: The unit of observation is a fixed grid of equally sized cells overlaid on the conflict-affected territory rat; aer_113_1_1 p.7-7 Section II, footnote 10: Restricts the sample to retail pharmacies and excludes pharmacies integrated into hospitals, clinics, or other |
| `sample_period_stated` | 8 | 42% | aer_110_5_5 p.2-8 Introduction; Section II.A: The analysis period is restricted to the years following the described military dispersal of the insurgent gro; aer_113_1_1 p.7-7 Section II: Uses pharmacy-level opioid order data from the DEA's Automation of Reports and Consolidated Orders System cove |
| `unit_of_observation_stated` | 7 | 37% | aer_110_5_5 p.12-13 Section II.C: The unit of observation is a fixed grid of equally sized cells overlaid on the conflict-affected territory rat; aer_113_1_1 p.7-7 Section II: States that the unit of observation is a retail pharmacy by calendar month, with quantities of each controlled |
| `sample_size_reported_per_table` | 6 | 32% | aer_110_5_5 p.17-18 Table 2 notes: Every main results table reports the number of observations and the number of cells beneath the coefficient bl; aer_113_1_1 p.10-17 Table 2; Table 4: Reports the number of observations in every regression table, and these counts vary across specifications and  |
| `in_footnote` | 5 | 26% | aer_110_5_5 p.8-9 Section II.A, footnote 13: The radio-station survey covers the full set of stations broadcasting defection content during the study windo; restud_2025_restud_rdae072 p.3-33 footnote 2 (Section 1), footnote 12 (Section 3), Acknowledgments: The firm-level KOF survey microdata are restricted and were obtained through the KOF micro data centre; the da |
| `in_main_text` | 4 | 21% | restud_2025_restud_rdae072 p.6-8 Section 2.1-2.2, Tables 1-3 and notes: Sources for the stylized facts are named in text and table notes: the Federal Reserve Board and BEA for the U.; restud_2025_restud_rdaf104 p.4-9 Section 3 Bridge data; footnotes 3, 9, 16, 41, 46: Bridge data are hand-assembled from the National Bridge Inventory, cross-checked with satellite imagery and co |
| `matching_or_linkage_described` | 3 | 16% | aer_113_1_1 p.7-26 Section II; Section V.B: Describes linking the opioid order dataset to pharmacy geographic identifiers from the same public source, to ; restud_2025_restud_rdaf104 p.21-28 Footnotes 33 and 46: County boundary changes are handled by remapping all data to baseline-year boundaries: separated counties are  |
| `restricted_data_used` | 3 | 16% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Several inputs are described as obtained directly from other researchers rather than a public repository (a he; jpe_2026_740226 p.10-10 Section III, Data: Lists six linked administrative sources spanning exam records, a household means-testing registry, financial-a |
| `in_appendix` | 1 | 5% | restud_2026_restud_rdag013 p.9-9 Section 2.3: The small share of inspections conducted by the federal EPA rather than the state regulator is retained in the |
| `other:multiple_sampling_criteria_rows` | 1 | 5% | restud_2025_restud_rdae072 p.6-7 Section 2.1, Table 2: The firm-level long-term underutilization table presents rows under successively stricter sampling criteria (a |

### specification_reporting (papers with this category: 10/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `fe_listed_in_table` | 8 | 42% | aer_110_5_5 p.17-18 Table 2 notes: The benchmark specification is explicitly defined in the table notes as cell and year fixed effects, propagati; ecta_92_2_2 p.13-13 Section 4.1, baseline specification equation: Reports a baseline linear specification of outcome on a treatment indicator with district and year fixed effec |
| `cluster_level_in_notes` | 7 | 37% | aer_113_1_1 p.10-24 Table notes throughout: States in every table's notes that standard errors are clustered at the zip code level and adjusted for within; aer_115_1_8 p.12-24 Table notes throughout: Each outcome table across the three separate empirical analyses (for-profit entry, the cap, and litigation) re |
| `se_type_in_notes` | 7 | 37% | aer_110_5_5 p.17-18 Table 2 notes: The type of standard error used (a correction allowing correlation over time and space) is stated once in the ; aer_113_1_1 p.10-24 Table notes throughout: States in every table's notes that standard errors are clustered at the zip code level and adjusted for within |
| `baseline_then_variants` | 5 | 26% | aer_110_5_5 p.17-18 Table 2 notes: The benchmark specification is explicitly defined in the table notes as cell and year fixed effects, propagati; ecta_92_2_2 p.13-13 Section 4.1, baseline specification equation: Reports a baseline linear specification of outcome on a treatment indicator with district and year fixed effec |
| `n_reported` | 5 | 26% | restud_2025_restud_rdae072 p.12-12 Table 6 and notes: The IV table pairs a baseline column with a column adding an interaction, for each of two outcome measures; ea; restud_2025_restud_rdaf104 p.25-25 Table 4 notes: The county panel table notes list year and county fixed effects and county-specific quadratic trends, state th |
| `controls_progressive_columns` | 3 | 16% | aer_110_5_5 p.17-18 Table 2, panel A1: Within a single table, numbered rows progress from a minimal fixed-effects-only model to the benchmark and the; jfe_2026_j_jfineco_2025_104223 p.15-16 Table 7: The main stock-level panel table progresses from single-shock specifications to versions adding risk-factor in |
| `in_main_text` | 2 | 10% | restud_2025_restud_rdae072 p.12-12 Table 6 and notes: The IV table pairs a baseline column with a column adding an interaction, for each of two outcome measures; ea; rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |
| `other:r2_not_reported` | 2 | 10% | restud_2025_restud_rdae072 p.9-9 Table 4: The limiting-factor table regresses binary indicators on the capacity utilization rate with firm and sector-by; restud_2025_restud_rdaf104 p.11-25 Table 1; Tables 2 to 4: Regression tables report neither R-squared nor the dependent variable mean; sample means of key outcomes appea |
| `r2_reported` | 2 | 10% | rfs_2025_rfs_hhaf065 p.32-32 Table 6: The closure table reports a pooled column followed by one column per regime, with adjusted R-squared, observat; rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |
| `weights_stated` | 2 | 10% | aer_113_1_1 p.10-24 Table notes throughout: Does not describe using sampling or regression weights anywhere in the main-text tables, so all reported regre; restud_2025_restud_rdaf104 p.25-25 Table 4 notes: The county panel table notes list year and county fixed effects and county-specific quadratic trends, state th |
| `mean_of_dependent_reported` | 1 | 5% | aer_113_1_1 p.10-10 Table 2 notes: Adopts a consistent table convention of reporting the mean of the outcome variable and the estimated effect ex |
| `other:dep_mean_in_summary_table` | 1 | 5% | restud_2025_restud_rdaf104 p.11-25 Table 1; Tables 2 to 4: Regression tables report neither R-squared nor the dependent variable mean; sample means of key outcomes appea |
| `other:log_likelihood_reported` | 1 | 5% | restud_2026_restud_rdag013 p.10-11 Table 2 and Section 3.2: The inspection-probability table reports three logit columns with fixed effects listed as Yes/No rows, N and l |

### variable_construction (papers with this category: 12/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `outcome_definition` | 7 | 37% | aer_110_5_5 p.17-18 Table 2 notes: The main conflict-count outcomes are log-transformed after adding a small constant to accommodate zero-valued ; aer_113_1_1 p.7-9 Section II: Defines the main outcome as monthly pharmacy-level dispensing measured in morphine equivalent doses, reported  |
| `treatment_definition` | 6 | 32% | aer_110_5_5 p.14-15 Section III, equation (1): The treatment variable, intensity of messaging, is defined by an explicit equation as the coverage-weighted su; aer_113_1_1 p.22-22 Section V.A, equation (4): Constructs a competition variable as a count of other pharmacies within a chosen radius of each pharmacy, and  |
| `logs_or_ihs` | 4 | 21% | aer_110_5_5 p.17-18 Table 2 notes: The main conflict-count outcomes are log-transformed after adding a small constant to accommodate zero-valued ; qje_140_1_11 p.32-33 Section V, Figure V notes: Job search intensity is constructed with an inverse hyperbolic sine transformation of counts, either the numbe |
| `measurement_error_discussed` | 4 | 21% | aer_110_5_5 p.9-10 Section II.A: Radio signal coverage is corrected for topography using an established terrain-propagation model applied to ea; restud_2025_restud_rdaf104 p.10-12 Section 3 Bridges and land transport infrastructure; Figure 4; footnote 18: Distance to a bridge is explicitly framed as a proxy for distance to a land transport route, validated in mode |
| `in_main_text` | 3 | 16% | restud_2025_restud_rdaf104 p.21-24 Section 5.1 equation (5.1); footnote 34: The panel treatment is the change in log distance from county centroid to the nearest bridge, entered as conte; rfs_2025_rfs_hhaf065 p.16-31 Sections 2.2 and 4.1: The main outcome for arrival analyses is the daily count of new accounts per branch, sometimes restricted to w |
| `standardized_index` | 3 | 16% | aer_110_5_5 p.14-15 Section III, equation (1): The treatment variable, intensity of messaging, is defined by an explicit equation as the coverage-weighted su; jfe_2026_j_jfineco_2025_104223 p.1-9 Introduction footnote 3; Section 4.2: The composite intermediary-shock proxy is built by standardizing two previously published shock series separat |
| `winsorization` | 2 | 10% | ecta_92_2_2 p.13-13 Section 4.1, baseline specification paragraph: States that all outcome variables are winsorized at fixed upper and lower percentiles before estimation to lim; rfs_2026_rfs_hhag042 p.13-45 Table 1 notes; Table 6 notes; Table 11 notes; Table B1 notes: Winsorization thresholds differ by use: summary statistics winsorize both tails at one level, regression contr |
| `in_footnote` | 1 | 5% | restud_2025_restud_rdaf104 p.24-25 Section 5.1; footnotes 40, 41, 44: Average agricultural land value is used as the proxy for total economic activity; a footnote derives the link  |
| `other:hand_collection` | 1 | 5% | rfs_2024_rfs_hhae045 p.14-16 Section 2.2, footnote 11: Because some disclosures are in images the script cannot read, the RD subsample is hand-checked; script-only r |
| `other:lasso_variable_selection` | 1 | 5% | aer_110_5_5 p.15-15 Section III, footnote 18; Section IV.C: The set of time-varying controls entering the benchmark specification, and the two commodities used for the he |
| `other:missing_coding_rule` | 1 | 5% | rfs_2024_rfs_hhae045 p.16-16 Section 2.2.2: Coding of missing breadth measures is made explicit: set to zero when no engagement is disclosed, treated as m |
| `other:price_shock_construction` | 1 | 5% | aer_110_5_5 p.13-14 Section II.D: Commodity price-shock variables combine each cell's historical share of land farmed with a given crop and the  |
| `other:proxy_justified_with_model` | 1 | 5% | restud_2025_restud_rdaf104 p.24-25 Section 5.1; footnotes 40, 41, 44: Average agricultural land value is used as the proxy for total economic activity; a footnote derives the link  |
| `other:scaling_by_account_mean` | 1 | 5% | rfs_2025_rfs_hhaf065 p.26-26 Section 3.3: Month-end passbook balances are scaled by the mean balance over the account's life so that accounts of differe |
| `other:text_keyword_measure` | 1 | 5% | rfs_2024_rfs_hhae045 p.14-15 Section 2.2.1, Table 1 notes: Outcomes are built by a Python script that flags engagement keywords within a fixed character distance of shar |
| `other:value_added_construction` | 1 | 5% | jpe_2026_740226 p.30-31 Section IV.G, equation (1): Builds college value-added measures for learning and earnings separately by regressing pre-policy outcomes on  |
| `other:variable_appendix` | 1 | 5% | rfs_2024_rfs_hhae045 p.50-52 Appendix C, Table C1: All variables are defined in a dedicated appendix table, and every table note points to it. |

### writing_structure (papers with this category: 13/19)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 11 | 58% | aer_110_5_5 p.4-5 Introduction: The introduction closes with an explicit contribution structure, separately positioning the paper against thre; aer_113_1_1 p.4-5 Introduction: Organizes its literature positioning into three consecutive contribution paragraphs late in the introduction,  |
| `results_previewed_in_intro` | 11 | 58% | aer_110_5_5 p.2-3 Introduction: The introduction previews the paper's main pattern of quantitative findings, across fatalities, returnees and ; aer_113_1_1 p.2-4 Introduction: Previews the paper's central quantitative findings from each empirical section in narrative form within the in |
| `appendix_heavy` | 10 | 53% | aer_110_5_5 p.1-35 throughout: The paper is heavily appendix-reliant: nearly every robustness check, heterogeneity split, and diagnostic ment; aer_113_1_1 p.8-26 Footnotes throughout Sections II-V: Defers many robustness checks, an event-study specification, quantile analyses, and several alternative-defini |
| `mechanisms_after_main` | 8 | 42% | aer_113_1_1 p.20-20 Section V, opening: Reserves the mechanism section, covering competitive pressure and pharmacist ownership, for after both main em; jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p |
| `data_before_design` | 7 | 37% | aer_110_5_5 p.8-14 Section II vs. Section III: The data section is placed before the empirical-strategy section, so that all data sources are described befor; jpe_2026_740226 p.6-15 Sections II-IV.A: Orders the empirical narrative as institutional background, then data, then design and validity, before turnin |
| `roadmap_paragraph` | 6 | 32% | jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul; jpe_2026_740226 p.3-5 Introduction: Previews the paper's main qualitative findings on enrollment, attainment, skill development, and earnings with |
| `robustness_separate_section` | 5 | 26% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection; restud_2025_restud_rdaf104 p.5-30 Sections 2 to 6: A descriptive correlations section motivates the problem, a history and data section precedes the designs, eac |
| `main_result_first` | 3 | 16% | restud_2026_restud_rdag056 p.12-29 Sections 4 to 7: Each outcome section presents the main figure and table first, then a robustness subsection, then alternative ; rfs_2025_rfs_hhaf065 p.9-34 Sections 2 to 4: No separate robustness section exists; robustness is handled in footnotes, table notes and the appendix, and e |
| `online_appendix_not_available` | 3 | 16% | aer_110_5_5 p.1-35 throughout: The paper is heavily appendix-reliant: nearly every robustness check, heterogeneity split, and diagnostic ment; qje_140_1_11 p.18-20 Section IV.A.1: Many robustness and diagnostic results are summarized narratively in the main text with the full tables and fi |
| `design_before_data` | 2 | 10% | jfe_2026_j_jfineco_2025_104223 p.4-8 Sections 2-4: The paper places its theoretical model and numbered propositions (Section 2) before the data description (Sect; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `in_footnote` | 1 | 5% | rfs_2026_rfs_hhag042 p.16-41 footnotes 11, 16, 17: Footnotes carry substantive supplementary analyses (an earnings-announcement test for the long leg, definition |
| `in_main_text` | 1 | 5% | rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `other:context_section_with_definitional_subsections` | 1 | 5% | restud_2026_restud_rdag013 p.6-8 Section 2: Institutional context precedes data, and the context section is organised as short definitional subsections (w |
| `other:robustness_as_subsection` | 1 | 5% | aer_110_5_5 p.17-31 Section IV, subsection D: Robustness checks are placed as the final lettered subsection within the single numbered Results section rathe |
| `roadmap_absent` | 1 | 5% | restud_2026_restud_rdag013 p.2-6 Sections 1, 1.1, 1.2: The introduction previews the counterfactual findings, the mechanism decomposition and additional counterfactu |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | agree | 3 | jpe_2026_740226 x3.description (paper: States that bandwidths are selected by a data-driven optimal-bandwidth / card: Records a bandwidth-selection diagnostic describing the same data-driv); restud_2025_restud_rdaf104 x1 (paper: Exclusion threshold of 31.4 km chosen as the minimum of rdbwselect opt / card: x1 bandwidth_selection call present (rdbwselect, IK and CCD); sample c) |
| cluster_level | agree | 12 | aer_110_5_5 s2.se.cluster_level (paper: No discrete cluster level is reported; inference relies on a continuou / card: se.cluster_level is null for both s1 and s2.); aer_113_1_1 s1.se.cluster_level; s4.se.cluster_level (paper: States in every table's notes, including both the ownership-change and / card: s1 and s2 (design d1) cluster on BUYER_ZIP; s4 and s5 (design d2) clus) |
| cluster_level | unknown | 3 | aer_115_1_8 s4.se.cluster_level (paper: Standard errors for the cap regression are stated to be clustered at t / card: s4, traced from a distributed-lags script, records cluster as a generi); ecta_92_2_2 s1.se.cluster_level (paper: States standard errors are clustered at the branch level, the unit of  / card: Card records se.cluster_level as hchyid (the ritest cluster variable) ) |
| cluster_level | paper_only | 3 | qje_140_1_4 specifications (paper: For the co-inventor spillover regression (Table III) the text separate / card: No specification extracted in the card corresponds to the co-inventor ); restud_2025_restud_rdae072 s3.se.cluster_level (paper: Firm-level clustered standard errors in Tables 4 and 6; default OLS st / card: s3.se cluster level and type are null.) |
| cluster_level | code_only | 1 | qje_140_1_4 s3.se.cluster_level (paper: The main text does not state a cluster level for the shift-share IV re / card: The card records two-way clustering at the region and decade level for) |
| comparison_group | paper_only | 7 | aer_113_1_1 none (not present among d1/d2) (paper: Defines a distinct headquarters-versus-branch comparison group among m / card: No design or spec record in the recipe card corresponds to a headquart); ecta_92_2_2 s1.comparison_group (paper: States explicitly that the comparison group is eligible clients in con / card: Card leaves comparison_group null for spec s1.) |
| comparison_group | agree | 1 | restud_2026_restud_rdaf027 d1.implementation_features / packages.teffects (paper: Two nearest-neighbour matched control schools per shooting school, dif / card: teffects nnmatch with fuzzy_vars enrollment, share_female, share_white) |
| controls | agree | 11 | aer_115_1_8 s1.formula (paper: The text states that regressions control for age, sex, race, and chron / card: The traced formula for s1 includes demographic and chronic-condition v); ecta_92_2_2 s1.controls_summary (paper: Baseline specification described as treatment plus district and year f / card: Card records controls_summary as null for spec s1.) |
| controls | paper_only | 5 | aer_110_5_5 s1.controls_summary (paper: The control set is described as Lasso-selected commodity-price and wea / card: controls_summary is null for both s1 and s2; only the unresolved $tren); jpe_2026_740226 s5.controls_summary (paper: Lists the specific baseline demographic, household, and high-school co / card: Leaves the controls-summary field unrecorded for the value-added speci) |
| controls | unknown | 1 | restud_2025_restud_rdae072 s3.controls (paper: Table 6 controls for the lagged information set, firm size, age and ag / card: s3 shows a single regressor and no control list.) |
| data_source | paper_only | 9 | aer_115_1_8 d1 (paper: The text names full-population Medicare claims, a government records r / card: The card's specification summary does not include a data_source field ); jfe_2025_j_jfineco_2025_104150 data.panel_firmyear.source_hint (paper: Appendix Table A.1 attributes variables to named commercial sources: D / card: data record panel_firmyear has type=null, access=unknown, source_hint=) |
| data_source | agree | 5 | ecta_92_2_2 data (paper: Names BRAC administrative loan and repayment records and a purpose-bui / card: Card's data array lists baseline.csv, endline_1.csv, and endline_2.csv); restud_2025_restud_rdae072 s1,s2,s3 file paths (paper: KOF business tendency survey microdata (restricted) for firm regressio / card: KOF_Code folder for the Stata regressions; Dynare datafile for estimat) |
| data_source | unknown | 2 | restud_2025_restud_rdaf104 data_source (paper: NBI bridge records, NHGIS, ICPSR county files, IPUMS full count, USGS  / card: Card data source fields not shown in the spec listing; packages rdrobu); rfs_2025_rfs_hhaf065 data_source (paper: Hand-transcribed archival registers, passbooks and dividend ledgers / card: dataverse_VX7HYE package; data source not recorded in specs output) |
| data_source | disagree | 1 | aer_110_5_5 data.0.type (paper: The core conflict data are described as coming from an NGO-run event-t / card: The merged dataset file (Radio_LRA_DB125.dta) is labeled with type=adm) |
| diagnostic | agree | 14 | aer_115_1_8 x1 (paper: A first-stage Wald statistic is reported in the main tables as the dia / card: Diagnostic x1 is recorded as first_stage with status unknown, meaning ); aer_115_1_8 x2 (paper: An event-study or distributed-lag analysis is described as the pre-tre / card: Diagnostic x2 is recorded as pretrend_test with status unknown.) |
| diagnostic | paper_only | 11 | aer_110_5_5 x1 (paper: The paper's design diagnostics are a randomized antenna-placement plac / card: The card's only diagnostic record (x1) reports a pre-trends plot as no); jfe_2025_j_jfineco_2025_104150 diagnostics.x1.status (paper: Text states that the event-study plot shows parallel pre-issuance tren / card: diagnostics x1 (pretrend_test) has status=unknown, only noting that pr) |
| diagnostic | unknown | 1 | aer_113_1_1 d1.s3; diag x1; diag x2 (paper: Refers by footnote to an event-study version of the ownership-change a / card: A separate spec s3 (design d1, FigureE1E2E3E4.do) implements an event-) |
| estimator | agree | 24 | aer_110_5_5 s1.estimator (paper: The benchmark model is described as a fixed-effects panel regression w / card: Both extracted specifications record estimator=hdfe_ols: s1 via Stata ); aer_113_1_1 d1 (s1, s2) (paper: Reports the ownership-change difference-in-differences model (equation / card: Design d1, specs s1 and s2 (Table3.R) run an OLS model of dispensing o) |
| estimator | paper_only | 3 | aer_115_1_8 s4 (paper: The litigation analysis is described as a difference-in-differences de / card: No card specification is labeled as the litigation difference-in-diffe); jfe_2025_j_jfineco_2025_104150 designs.d1.method (paper: Identification combines a panel OLS quasi-DID, a propensity-score matc / card: d1 records only method=event_study with role, variant, treatment and c) |
| estimator | code_only | 2 | qje_140_1_4 s3.formula_or_call (paper: The text names a shift-share instrumental-variables strategy based on  / card: The card's IV specification (s3) is a two-stage-least-squares regressi); restud_2026_restud_rdag013 s1.estimator (paper: Table 3 deterrence regressions are described only as regressions of vi / card: s1 to s3 use ppmlhdfe (Poisson PPML) for n_violations.) |
| estimator | disagree | 1 | jfe_2026_j_jfineco_2025_104223 d3 / s18 (paper: Section 4.3 explicitly names the S&P 500 inclusion test a difference-i / card: Card classifies the same test under design d3 with method return_event) |
| fixed_effects | agree | 15 | ecta_92_2_2 s1.fixed_effects (paper: States the baseline specification includes a district fixed effect (th / card: Card records fixed_effects district, year for spec s1.); jfe_2025_j_jfineco_2025_104150 specifications.s1.fixed_effects (paper: Table 4 col. 1/4/7 lists Country x Year FE and Industry x Year FE as t / card: s1.fixed_effects = [id_cyear, id_indyear] from tab4.do line 39) |
| fixed_effects | paper_only | 7 | aer_110_5_5 s1.fixed_effects (paper: The paper explicitly states cell and year fixed effects plus macro-reg / card: The fixed_effects field is null for both s1 and s2; the code-engineer ); aer_113_1_1 d1.s1; d1.s2 (paper: States that its preferred ownership-change specification (Table 3 colu / card: Both captured specs for design d1 (s1, s2) use zip-code fixed effects ) |
| fixed_effects | disagree | 2 | qje_140_1_4 s1.fixed_effects (paper: The main text describes the leads-and-lags event-study specification ( / card: The card's leads-and-lags specification (s1) additionally absorbs a te); restud_2026_restud_rdag013 s1.fixed_effects (paper: Table 3 column (1) lists year FE and unit FE 'Category, Firm'. / card: s1 absorbs year, naics_2, c_fe, region_fe.) |
| other | agree | 5 | qje_140_1_11 d1.variant (paper: Primary design is a sharp RD at the age-55 mandatory-notice eligibilit / card: Design d1 is classified as rdd with treatment defined as age >= 55 int); restud_2025_restud_rdae072 s2 (paper: Standard deviations of cyclical correlations computed with the VARHAC  / card: s2: varhac_est call in CU_Facts.m.) |
| other | paper_only | 3 | jfe_2026_j_jfineco_2025_104223 heterogeneity (paper: Section 5 describes heterogeneity splits by hedge-fund holdings and by / card: Card's structured heterogeneity array is empty, so these splits are no); rfs_2025_rfs_hhaf065 methods (paper: Structural break estimation with Bai-Perron via Ditzen et al. Stata co / card: methods list only did and event_study; no break spec recorded) |
| outputs | paper_only | 9 | aer_115_1_8 outputs (paper: The main text reports six numbered tables and three numbered figures,  / card: The card records no table or figure output artifacts (tables and figur); ecta_92_2_2 outputs.tables (paper: Names nine main numbered tables (Table I-IX) and a multi-panel figure  / card: Card's outputs.tables and outputs.figures arrays are both empty.) |
| outputs | unknown | 5 | jpe_2026_740226 outputs.tables (paper: Presents six main numbered tables and eleven main numbered figures in  / card: Records one table and two figures as observed outputs, reflecting a pa); restud_2025_restud_rdae091 outputs (paper: Five main-text tables and three multi-panel figures, plus appendix tab / card: tables=4 figures=2 from four files read; card coverage is partial.) |
| outputs | agree | 3 | aer_110_5_5 outputs.tables.t1 (paper: Table 2, titled "Effect of Defection Messaging on Fatalities," is the  / card: outputs.tables record t1 is labeled "Table 2 (main)" with matching evi); restud_2026_restud_rdaf027 outputs.tables.t2 (paper: Tables 2 and 3 report long-run educational and labor market outcomes f / card: t2 and t3 produced by esttab from B3_Long_run_analysis_baseline.do; st) |
| outputs | disagree | 1 | aer_113_1_1 summary: tables=2 figures=1 (paper: Presents eight numbered regression or descriptive tables and seven num / card: The card's summary line reports only two tables and one figure among i) |
| robustness | paper_only | 10 | ecta_92_2_2 robustness (paper: Describes several robustness checks in footnotes: an alternative gauge / card: Card's robustness array is empty.); jfe_2025_j_jfineco_2025_104150 robustness (paper: Paper reports multiple named robustness checks: log-transformed ESG sc / card: card robustness array is empty) |
| robustness | agree | 4 | aer_110_5_5 robustness.alt_functional_form (paper: Table 2 panel B reports the benchmark specification under alternative  / card: The robustness array records an alt_functional_form check (log(y+0.5),); restud_2025_restud_rdae091 robustness.alt_sample (s6) (paper: Table 2 column (6) omits Ukraine. / card: s6 with id != 26, recorded as alt_sample confirmed against base s2.) |
| robustness | disagree | 3 | aer_113_1_1 robustness alt_fixed_effects (base=[s1], var=[s2]) (paper: Presents its ownership-change results separately for all opioids and f / card: The card's automated robustness rule labels s1 (all-opioids outcome) a); aer_113_1_1 robustness alt_estimator (base=[s5], var=[s4]) (paper: Presents the no-fixed-effects and pharmacy-fixed-effects reformulation / card: The card's automated robustness rule labels s5 (no fixed effects, Stat) |
| robustness | unknown | 1 | qje_140_1_11 robustness (paper: The main text does not describe an alternative-specification robustnes / card: The card's top-level robustness array is empty, consistent with no rob) |
| sample | paper_only | 9 | aer_110_5_5 s1.sample (paper: The estimation sample is described as a cell-year panel covering the f / card: The sample field is null for both s1 and s2.); aer_113_1_1 robustness alt_sample (base=[s4,s5]) (paper: Reports the reformulation regression twice, once on the full study per / card: Specs s4 and s5 are recorded without a distinguishing sample-restricti) |
| sample | agree | 9 | ecta_92_2_2 d1.treatment (paper: States the main analysis compares eligible BRAC members across treatme / card: Card design d1 records the treatment as access to the Emergency Loan f); qje_140_1_11 pipeline.sample_restrictions[1] (paper: The paper states the RKD-based unemployed search analysis covers all U / card: The card's sample_restrictions entry for the RKD sample records a noti) |
| sample | code_only | 2 | qje_140_1_11 pipeline.sample_restrictions[1] (paper: The main text does not state a specific numeric bandwidth for the wage / card: The card's RKD sample restriction records a daily-wage variable normal); restud_2025_restud_rdae072 s1 (paper: Macro estimation uses four detrended U.S. series; the sample period is / card: s1 estimation command names datafile data_estimate_v8 with nobs=277.) |
| se_type | agree | 9 | aer_110_5_5 s2.se.type (paper: Main-table standard errors are described as allowing for correlation o / card: se.type=conley_spatial is recorded for s2 (CONLEY.do), matching the ma); ecta_92_2_2 s1.se.type (paper: States that standard errors are always clustered at the branch level a / card: Card records se.type randomization_inference for spec s1, built from t) |
| se_type | paper_only | 4 | restud_2025_restud_rdae091 s2.se (paper: Standard errors adjusted for spatial correlation within 1,500 km (prov / card: se=None/None on all specs; acreg is the estimator, spatial options unr); restud_2026_restud_rdaf027 s1.se.type (paper: Wild cluster bootstrap for few-cluster subgroup analyses; permutation  / card: Only cluster-robust SE recorded for s1.) |
| se_type | disagree | 1 | restud_2025_restud_rdaf104 s1.se (paper: Standard errors cluster-bootstrapped by nearest tributary confluence w / card: s1 records cluster(tempid2) analytic clustering; no bootstrap wrapper ) |
| se_type | unknown | 1 | restud_2026_restud_rdag013 s1.se (paper: No SE type or cluster level stated for Tables 2 and 3. / card: se null for all specs.) |
| weights | unknown | 6 | aer_110_5_5 s1.weights (paper: No observation-weighting scheme for the panel regressions is mentioned / card: The weights field is also null for both specifications.); jpe_2026_740226 s1.weights (paper: Does not describe any weighting scheme for the main RD or value-added  / card: Leaves the weights field unrecorded (null) for every extracted specifi) |
| weights | agree | 6 | aer_115_1_8 s1.weights (paper: The main text and table notes do not describe any sample weighting sch / card: Weights are recorded as null for s1 through s5.); ecta_92_2_2 s1.weights (paper: No sample weights are mentioned for the baseline household-level speci / card: Card records weights as null for spec s1.) |
| weights | paper_only | 3 | jfe_2025_j_jfineco_2025_104150 specifications.s1.weights (paper: Section 5.1 and Table 7 describe overlap-weighted regressions using pr / card: Neither s1 nor s2 records a weighting specification, and no specificat); jfe_2026_j_jfineco_2025_104223 s1.weights (paper: Text states portfolios are equal-weighted at baseline and separately r / card: Card records weights=None (null) for all listed specs, not distinguish) |
| weights | code_only | 1 | restud_2026_restud_rdag056 s4 (paper: No weighting mentioned for CPS regressions. / card: weight(wtfinl) used in CPS employment and duration specs s4 and s5.) |

## Gaps the readers reported

- (1) Main results tables report observation and cell counts for every specification but do not report R-squared or the depend
- (1) No pre-analysis plan or preregistration is mentioned; only IRB/ethics approval for the survey component is stated (prere
- (1) No explicit statement of estimation software appears in the main text; software use is only inferable from the replicati
- (1) No discussion of observation weighting for the panel regressions appears in either the main text or the table notes.
- (1) No explicit description of a discrete comparison group is given, consistent with the continuous-treatment design; the pa
- (1) No preregistration, IRB approval, or human-subjects consent statement appears anywhere in the main text; the study uses 
- (1) No explicit textual justification is given in the main text for the choice of zip-code-level clustering over some other 
- (1) No formal joint statistical test of pre-trends (for example an F-test on a set of leads) is reported in the main text; t
- (1) The event-study specification for the ownership-change design is referenced only by a single footnote pointing to an onl
- (1) The lettered online appendix (Appendices A through H, containing most robustness checks, the event study, quantile analy
- (1) No discussion of sampling or regression weights appears anywhere in the main text; all reported regressions appear to be
- (1) No explicit pre-analysis plan or preregistration is mentioned anywhere in the main text; only an IRB exemption is stated
- (1) No explicit multiple-testing adjustment is discussed despite many outcome categories being tested within the same tables
- (1) No weak-instrument-robust inference procedure is reported alongside the first-stage Wald statistics in the main text.
- (1) The main text does not name a statistical software package or version used for estimation.
- (1) No table or passage explicitly states whether sample weights are or are not used; the tables' notes are silent on weight
- (1) The content behind the online appendix tables and figures (balance table, first-stage table, complier table, event-study
- (1) No explicit justification in the main text for why randomization-inference p-values are reported alongside cluster-robus
- (1) No explicit statistical power or minimum-detectable-effect calculation for the branch-level randomization was found in t
- (1) No discussion of a multiple-testing adjustment across the many outcomes and subgroup checks was found.
- (1) The paper's own online appendix (Lane 2023) is hosted as a separate document and is not part of the extracted text, so a
- (1) No pre-analysis plan document is cited beyond the AEA RCT registry identification, and no discussion distinguishing regi
- (1) No passage in the main text justifies clustering standard errors at the firm level specifically (versus country, industr
- (1) No preregistration, pre-analysis plan, or IRB/ethics statement is present anywhere in the text; the study uses secondary
- (1) Main regression tables (e.g., Tables 4, 6, 8) report N and adjusted R2 but do not include a row for the mean of the depe
- (1) No passage discusses a multiple-testing or multiple-comparisons adjustment despite many subgroup and successive robustne
- (1) The paper's main text and appendix never name the statistical software or estimation package used; this is only recovera
- (1) The recipe card's coverage is partial (9 of 26 pipeline scripts read), so several paper-stated robustness and diagnostic
- (1) No pre-registration, IRB, or ethics statement is present; not applicable to this secondary-market asset-pricing study us
- (1) The paper's own text does not name the statistical software used for estimation; Stata/SAS are only identifiable from th

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
