# Reported practice: `matching` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 11 paper notes (10 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | AER: 3, ReStud: 3, JFE: 2, JPE: 1, QJE: 1, RFS: 1 |
| year | 2021: 1, 2023: 1, 2024: 2, 2025: 3, 2026: 4 |
| papers with at least one observation in category | diagnostic_reported: 9, robustness_reported: 8, design_statement: 6, sample_construction: 6, writing_structure: 4, limitation_stated: 3, specification_reporting: 3, external_validity: 3, replication_statement: 3, data_access: 3, mechanism_evidence: 2, presentation_convention: 2, variable_construction: 1, inference_justification: 1, heterogeneity_reported: 1, magnitude_interpretation: 1, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_111_12_2 | AER | 2021 | full | yes | 1e6a579f8a8a |
| aer_113_6_2 | AER | 2023 | main_text | no | a9a4f1c0f4ad |
| aer_114_7_10 | AER | 2024 | full | yes | a2ce2c0a92fe |
| jfe_2024_j_jfineco_2024_103809 | JFE | 2024 | full | yes | 3776fdfeb8c7 |
| jfe_2025_j_jfineco_2025_104150 | JFE | 2025 | full | yes | d509ecfbe6d0 |
| jpe_2026_740222 | JPE | 2026 | full | yes | 98c23fe93722 |
| qje_140_1_4 | QJE | 2025 | partial | yes | 793bd3a24ebb |
| restud_2025_restud_rdaf004 | ReStud | 2025 | full | yes | adc4b78e8b08 |
| restud_2026_restud_rdaf027 | ReStud | 2026 | full | yes | e5e02c526e90 |
| restud_2026_restud_rdag080 | ReStud | 2026 | full | yes | feb48766a8b7 |
| rfs_2026_rfs_hhaf080 | RFS | 2026 | full | yes | bef15266e552 |

## Practices by category and tag


### data_access (papers with this category: 3/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 3 | 27% | aer_113_6_2 p.9-12 Section II: Draws underlying data from a mix of publicly available digitized newspaper archives, publicly compiled histori; qje_140_1_4 p.31-32 Section III.A: The empirical analysis is built from two named external academic data products rather than data collected by t |
| `commercial` | 1 | 9% | rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |
| `data_public` | 1 | 9% | aer_113_6_2 p.9-12 Section II: Draws underlying data from a mix of publicly available digitized newspaper archives, publicly compiled histori |
| `data_restricted` | 1 | 9% | rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |
| `linked_records` | 1 | 9% | rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |
| `public_use` | 1 | 9% | aer_113_6_2 p.9-12 Section II: Draws underlying data from a mix of publicly available digitized newspaper archives, publicly compiled histori |
| `web_scraped` | 1 | 9% | rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |

### design_statement (papers with this category: 6/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 4 | 36% | aer_111_12_2 p.1-4 Abstract and Introduction: Names the tax administration analysis a matched difference-in-differences design and states the estimand as th; jfe_2024_j_jfineco_2024_103809 p.2-7 Section 1 (introduction) and Section 4.2: The paper names three complementary designs for the main analysis: a firm and day fixed-effects difference-in- |
| `threats_discussed` | 4 | 36% | aer_111_12_2 p.18-19 Section IIIA, Empirical Strategy: States that the original assignment formula and worksheets used to place taxpayers into the medium taxpayer of; jpe_2026_740222 p.21-21 Section IV.A, footnote 34: A stable-unit-treatment-value threat is named explicitly: never-treated units competing in the same markets as |
| `estimand_named` | 3 | 27% | aer_111_12_2 p.1-4 Abstract and Introduction: Names the tax administration analysis a matched difference-in-differences design and states the estimand as th; jfe_2024_j_jfineco_2024_103809 p.7-10 Section 4.2 and Table 5: Coarsened Exact Matching is introduced as a strategy to select a comparison sample that minimizes covariate im |
| `identifying_assumption_explicit` | 2 | 18% | aer_111_12_2 p.18-19 Section IIIA, Empirical Strategy: States that the original assignment formula and worksheets used to place taxpayers into the medium taxpayer of; rfs_2026_rfs_hhaf080 p.3-4 Introduction, paragraphs on benchmark borrowers: The identifying assumption for the matched comparison is stated in the introduction: observably similar FinTec |
| `in_main_text` | 2 | 18% | jfe_2024_j_jfineco_2024_103809 p.2-7 Section 1 (introduction) and Section 4.2: The paper names three complementary designs for the main analysis: a firm and day fixed-effects difference-in-; rfs_2026_rfs_hhaf080 p.3-4 Introduction, paragraphs on benchmark borrowers: The identifying assumption for the matched comparison is stated in the introduction: observably similar FinTec |
| `other:control_group_selection_justified` | 1 | 9% | restud_2026_restud_rdaf027 p.12-13 Section 4.1: Nearest-neighbour matching of control schools is justified as reducing differential trend concerns; schools in |
| `other:regression_discontinuity_ruled_out` | 1 | 9% | aer_111_12_2 p.18-18 Section IIIA, footnote: Explicitly explains why a regression discontinuity design is not used for the administration reform: the exact |
| `parallel_trends_argued` | 1 | 9% | rfs_2026_rfs_hhaf080 p.20-24 Section 3.1 end and Section 3.3: Each benchmark group is introduced with an explicit strength and limitation: bank borrowers share credit deman |

### diagnostic_reported (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `balance_table` | 7 | 64% | aer_111_12_2 p.22-23 Table 1, columns 1 and 2: Presents preperiod weighted means for treated and comparison taxpayers not only on the variables explicitly ta; aer_113_6_2 p.28-28 Section IV.D, Other Robustness, footnote: Reports a formal coefficient-stability statistic for selection on unobservables computed from the unmatched an |
| `in_appendix` | 5 | 46% | aer_111_12_2 p.28-29 Section IIIB, footnote: Constructs a placebo assignment among comparison taxpayers that mimics the increasing relationship between ass; aer_113_6_2 p.28-28 Section IV.D, Other Robustness, footnote: Reports a formal coefficient-stability statistic for selection on unobservables computed from the unmatched an |
| `in_main_text` | 5 | 46% | aer_111_12_2 p.22-23 Table 1, columns 1 and 2: Presents preperiod weighted means for treated and comparison taxpayers not only on the variables explicitly ta; jfe_2025_j_jfineco_2025_104150 p.11-12 Table 5: A dedicated balance table reports mean differences and t-statistics on the matching covariates for each of the |
| `online_appendix_not_available` | 2 | 18% | aer_111_12_2 p.28-29 Section IIIB, footnote: Constructs a placebo assignment among comparison taxpayers that mimics the increasing relationship between ass; qje_140_1_4 p.36-37 Section III.B.2: Balance between migrants and their matched placebo controls is asserted qualitatively in the main text through |
| `density_test` | 1 | 9% | aer_113_6_2 p.28-28 Section IV.D, Other Robustness, footnote: Reports a formal coefficient-stability statistic for selection on unobservables computed from the unmatched an |
| `other:placebo_treatment_assignment` | 1 | 9% | aer_114_7_10 p.32-33 Section VI: Separately from randomization inference, the paper runs a placebo check that assigns fake treatment to non-Car |
| `other:spillover_check` | 1 | 9% | jpe_2026_740222 p.21-21 Section IV.A, footnote 34: Possible spillovers onto comparison units are addressed diagnostically in two ways: an appendix matching desig |
| `placebo_outcomes` | 1 | 9% | aer_111_12_2 p.28-29 Section IIIB, footnote: Constructs a placebo assignment among comparison taxpayers that mimics the increasing relationship between ass |
| `sensitivity_bounds` | 1 | 9% | aer_113_6_2 p.28-28 Section IV.D, Other Robustness, footnote: Reports a formal coefficient-stability statistic for selection on unobservables computed from the unmatched an |

### external_validity (papers with this category: 3/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 2 | 18% | qje_140_1_4 p.6-7 Section I, end: The paper explicitly generalizes its inventor-specific findings to other categories of high-skilled workers, n; rfs_2026_rfs_hhaf080 p.47-48 Section 6, footnotes 47 and 48: The conclusion has a dedicated generalisation paragraph arguing portability beyond France (collateral constrai |
| `site_specific` | 1 | 9% | rfs_2026_rfs_hhaf080 p.47-48 Section 6, footnotes 47 and 48: The conclusion has a dedicated generalisation paragraph arguing portability beyond France (collateral constrai |
| `time_period_specific` | 1 | 9% | aer_113_6_2 p.3-4 Introduction: Discusses the historical specificity of the setting, an early-twentieth-century road-show distribution system  |

### heterogeneity_reported (papers with this category: 1/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `mechanism_motivated` | 1 | 9% | rfs_2026_rfs_hhaf080 p.30-46 Section 4.1.2, 4.2.1, 5.2, footnote 33: Heterogeneity is always run as split samples (loan purpose, rated versus unrated, high versus low interest rat |
| `other:rematching_within_subsample` | 1 | 9% | rfs_2026_rfs_hhaf080 p.30-46 Section 4.1.2, 4.2.1, 5.2, footnote 33: Heterogeneity is always run as split samples (loan purpose, rated versus unrated, high versus low interest rat |
| `split_sample` | 1 | 9% | rfs_2026_rfs_hhaf080 p.30-46 Section 4.1.2, 4.2.1, 5.2, footnote 33: Heterogeneity is always run as split samples (loan purpose, rated versus unrated, high versus low interest rat |

### inference_justification (papers with this category: 1/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_justification_found` | 1 | 9% | aer_113_6_2 p.1-37 throughout: Does not discuss a multiple-testing adjustment anywhere in the text despite reporting many outcome variables a |

### limitation_stated (papers with this category: 3/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `measurement` | 2 | 18% | aer_113_6_2 p.30-30 Section V: States explicitly that mechanism evidence on persuasion is only suggestive because the available historical me; rfs_2026_rfs_hhaf080 p.4-30 footnotes 7, 29, 31: Limits of the collateral data are stated in footnotes: only pledges of specific assets are observed, not perso |
| `data_coverage` | 1 | 9% | rfs_2026_rfs_hhaf080 p.4-30 footnotes 7, 29, 31: Limits of the collateral data are stated in footnotes: only pledges of specific assets are observed, not perso |
| `identification_caveat` | 1 | 9% | aer_111_12_2 p.18-18 Section IIIA, footnote: States as a limitation that the precise taxpayer-assignment formula and files were not retained, which rules o |
| `interpretation_caveat` | 1 | 9% | aer_113_6_2 p.30-30 Section V: States explicitly that mechanism evidence on persuasion is only suggestive because the available historical me |

### magnitude_interpretation (papers with this category: 1/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `back_of_envelope` | 1 | 9% | rfs_2026_rfs_hhaf080 p.45-47 Section 5.2, footnote 46, Internet Appendix Sections J and K: Interest-expense and investor-return calculations combine regression estimates with summary statistics and ext |
| `cost_benefit` | 1 | 9% | rfs_2026_rfs_hhaf080 p.45-47 Section 5.2, footnote 46, Internet Appendix Sections J and K: Interest-expense and investor-return calculations combine regression estimates with summary statistics and ext |
| `other:binscatter_slope_comparison` | 1 | 9% | rfs_2026_rfs_hhaf080 p.33-34 Figure 6, Section 4.1.4: A binned scatter of new loan size against subsequent bank credit growth for the two groups is used to compare  |

### mechanism_evidence (papers with this category: 2/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `suggestive_labelled` | 2 | 18% | aer_113_6_2 p.29-29 Section V, opening paragraph: States at the outset of the mechanisms section that data constraints prevent a comprehensive test of channels,; rfs_2026_rfs_hhaf080 p.27-27 footnote 28: A footnote uses loan-to-value reasoning to distinguish sequential from simultaneous financing and compares imp |
| `in_footnote` | 1 | 9% | rfs_2026_rfs_hhaf080 p.27-27 footnote 28: A footnote uses loan-to-value reasoning to distinguish sequential from simultaneous financing and compares imp |
| `survey_evidence` | 1 | 9% | aer_113_6_2 p.30-30 Section V: Uses survey-based attitude data from later decades as an indirect proxy for contemporaneous persuasion effects |

### other (papers with this category: 1/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:descriptive_regression_of_loan_terms` | 1 | 9% | rfs_2026_rfs_hhaf080 p.14-16 Table 2, Section 2.2.2 and 2.2.3: Before the main analysis, FinTech and bank loans are compared by regressing loan size, maturity and rate on a  |

### presentation_convention (papers with this category: 2/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `notes_state_sample` | 2 | 18% | aer_113_6_2 p.21-21 Table 3, and generally: Reports standard errors in parentheses beneath every coefficient directly in the regression tables, with notes; rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `notes_state_se` | 2 | 18% | aer_113_6_2 p.21-21 Table 3, and generally: Reports standard errors in parentheses beneath every coefficient directly in the regression tables, with notes; rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `appendix_tables_numbered_a` | 1 | 9% | rfs_2026_rfs_hhaf080 p.1-47 Title page note, references throughout: Internet Appendix material is referenced by lettered sections and tables or figures (A.1 to K), covering varia |
| `binscatter` | 1 | 9% | rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `coefficient_plot` | 1 | 9% | rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `event_study_figure` | 1 | 9% | rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `map` | 1 | 9% | aer_113_6_2 p.9-10 Figure 2: Uses paired choropleth maps to visualize the geographic footprint of both the film's road show and the second  |
| `online_appendix_not_available` | 1 | 9% | rfs_2026_rfs_hhaf080 p.1-47 Title page note, references throughout: Internet Appendix material is referenced by lettered sections and tables or figures (A.1 to K), covering varia |
| `stars_used` | 1 | 9% | rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `summary_stats_table` | 1 | 9% | rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |

### replication_statement (papers with this category: 3/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 3 | 27% | aer_113_6_2 p.35-35 References: Cites a formal archived replication-data deposit for the paper in the reference list rather than including a d; qje_140_1_4 p.69-69 Data Availability statement: A dedicated data-availability statement at the end of the article names the public repository and identifier w |
| `code_public` | 1 | 9% | rfs_2026_rfs_hhaf080 p.48-48 Code Availability paragraph: A one-sentence Code Availability statement at the end of the conclusion points to a Harvard Dataverse DOI for  |
| `data_public` | 1 | 9% | qje_140_1_4 p.69-69 Data Availability statement: A dedicated data-availability statement at the end of the article names the public repository and identifier w |
| `online_appendix_not_available` | 1 | 9% | qje_140_1_4 p.69-69 Supplementary Material statement: The article repeatedly refers throughout the main text to an Online Appendix published separately at the journ |
| `software_named` | 1 | 9% | qje_140_1_4 p.33-33 Section III.A.1: A commercial third-party software product is named and described for one specific analysis step, inferring an  |

### robustness_reported (papers with this category: 8/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 6 | 55% | aer_111_12_2 p.27-28 Section IIIB, Robustness paragraph: Summarizes robustness of the administration treatment effect to alternative weighting strategies, including no; aer_113_6_2 p.28-28 Section IV.D, Other Robustness: Reports propensity-score-matching estimates as an alternative-estimator robustness check for the long-run desi |
| `alt_estimator` | 5 | 46% | aer_111_12_2 p.27-28 Section IIIB, Robustness paragraph: Summarizes robustness of the administration treatment effect to alternative weighting strategies, including no; aer_113_6_2 p.28-28 Section IV.D, Other Robustness: Reports propensity-score-matching estimates as an alternative-estimator robustness check for the long-run desi |
| `alt_control_group` | 4 | 36% | aer_113_6_2 p.28-28 Section IV.D, Other Robustness: Reports propensity-score-matching estimates as an alternative-estimator robustness check for the long-run desi; aer_114_7_10 p.30-33 Section VI: Paper reports several alternative control-group constructions as robustness checks: adding non-Carolina Southe |
| `in_main_text` | 2 | 18% | jfe_2024_j_jfineco_2024_103809 p.9-11 Tables 3-5 and Figures 1-2: The three-estimator strategy (difference-in-differences, synthetic difference-in-differences, matching) functi; jfe_2025_j_jfineco_2025_104150 p.11-16 Section 5.1: Robustness to confounding between treated and control firms is pursued through a sequence of distinct named es |
| `summarized_in_one_table` | 2 | 18% | aer_111_12_2 p.27-28 Section IIIB, Robustness paragraph: Summarizes robustness of the administration treatment effect to alternative weighting strategies, including no; jfe_2024_j_jfineco_2024_103809 p.9-11 Tables 3-5 and Figures 1-2: The three-estimator strategy (difference-in-differences, synthetic difference-in-differences, matching) functi |
| `alt_sample` | 1 | 9% | rfs_2026_rfs_hhaf080 p.26-26 Section 3.3 last paragraph, Internet Appendix Section D: Robustness of the matched DiD is delegated to an appendix section: alternative matching procedures (one neares |
| `alt_specification` | 1 | 9% | aer_111_12_2 p.27-28 Section IIIB, Robustness paragraph: Summarizes robustness of the administration treatment effect to alternative weighting strategies, including no |
| `measurement_error_discussed` | 1 | 9% | aer_113_6_2 p.5-5 footnote 1: Discloses that the two independently constructed treatment datasets were developed by separate research teams  |
| `online_appendix_not_available` | 1 | 9% | jpe_2026_740222 p.44-44 Section VII, Matching difference-in-differences: A matched difference-in-differences check pairs each treated generator with several comparison units drawn fro |
| `summarized_in_figure` | 1 | 9% | restud_2026_restud_rdaf027 p.30-31 Section 5.3; Appendix Figures A12 to A14: Eight alternative matching strategies (extra match variables, exact region match, more controls, reverse order |

### sample_construction (papers with this category: 6/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `exclusions_justified` | 4 | 36% | aer_111_12_2 p.18-18 Section IIIA, discussion of office waves: Restricts the main administration analysis to regions where offices opened in a single later wave rather than ; aer_113_6_2 p.11-12 Section II.C, KKK Chapters: Notes that the klavern data record only the date a chapter was first mentioned, not its founding or dissolutio |
| `matching_or_linkage_described` | 4 | 36% | aer_113_6_2 p.9-10 Section II.A, Movie Screenings: Describes construction of the treatment-timing variable from newspaper advertisements gathered across three di; jfe_2025_j_jfineco_2025_104150 p.11-12 Section 5.1; Table 5 and Table 6 notes: The stacked-DID sample is built by matching each SLL borrower to a single never-issuer control firm on country |
| `sample_size_reported_per_table` | 3 | 27% | jfe_2025_j_jfineco_2025_104150 p.11-12 Section 5.1; Table 5 and Table 6 notes: The stacked-DID sample is built by matching each SLL borrower to a single never-issuer control firm on country; qje_140_1_4 p.36-37 Section III.B.2: The paper reports how many migrants find an exact match under the matching procedure separately for EU-origin  |
| `data_source_named` | 2 | 18% | aer_113_6_2 p.9-10 Section II.A, Movie Screenings: Describes construction of the treatment-timing variable from newspaper advertisements gathered across three di; rfs_2026_rfs_hhaf080 p.10-12 Section 2.1.1 to 2.1.6, Table A.1: Data sources are listed one by one in numbered subsections (scraped aggregator website, central bank FinTech r |
| `sample_period_stated` | 2 | 18% | restud_2025_restud_rdaf004 p.12-13 Section 5.2: The DiD uses a perfectly balanced worker-year panel from several years before to several years after layoff, w; rfs_2026_rfs_hhaf080 p.10-11 Section 2.1.1, footnote 19, Internet Appendix B.1: Platform exclusions (equity or bond platforms, an agriculture-only platform) are justified by comparability wi |
| `unit_of_observation_stated` | 2 | 18% | restud_2025_restud_rdaf004 p.12-13 Section 5.2: The DiD uses a perfectly balanced worker-year panel from several years before to several years after layoff, w; rfs_2026_rfs_hhaf080 p.12-13 Section 2.1.7, footnote 22: The unmatched sample is built as an ordered list: industry exclusions, minimum presence in the credit registry |
| `in_appendix` | 1 | 9% | rfs_2026_rfs_hhaf080 p.13-13 Section 2.1.8, Tables A.3 and A.4: Two Internet Appendix tables document, for every table and figure, the sample restrictions, frequency, time pe |
| `in_footnote` | 1 | 9% | rfs_2026_rfs_hhaf080 p.10-11 Section 2.1.1, footnote 19, Internet Appendix B.1: Platform exclusions (equity or bond platforms, an agriculture-only platform) are justified by comparability wi |
| `in_main_text` | 1 | 9% | rfs_2026_rfs_hhaf080 p.10-12 Section 2.1.1 to 2.1.6, Table A.1: Data sources are listed one by one in numbered subsections (scraped aggregator website, central bank FinTech r |
| `other:common_support_trimming` | 1 | 9% | aer_111_12_2 p.18-19 Section IIIA: Imposes a common support restriction that drops taxpayers in the extreme tails of the matching-variable distri |
| `restricted_data_used` | 1 | 9% | rfs_2026_rfs_hhaf080 p.10-12 Section 2.1.1 to 2.1.6, Table A.1: Data sources are listed one by one in numbered subsections (scraped aggregator website, central bank FinTech r |

### specification_reporting (papers with this category: 3/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `weights_stated` | 2 | 18% | jfe_2024_j_jfineco_2024_103809 p.10-10 Section 5.2, discussion around Table 5: The matching table states explicitly that observations are equally weighted in the reported specification, wit; rfs_2026_rfs_hhaf080 p.21-26 Section 3.2.1, Table 4 notes: Matching is described as five nearest neighbours with replacement, and the text notes that a benchmark firm ca |
| `baseline_then_variants` | 1 | 9% | jfe_2024_j_jfineco_2024_103809 p.10-10 Section 5.2, discussion around Table 5: The matching table states explicitly that observations are equally weighted in the reported specification, wit |
| `mean_of_dependent_reported` | 1 | 9% | aer_113_6_2 p.12-13 Table 1: Presents a summary-statistics table comparing treatment and control counties, with a separate comparison restr |
| `notes_state_sample` | 1 | 9% | aer_113_6_2 p.12-13 Table 1: Presents a summary-statistics table comparing treatment and control counties, with a separate comparison restr |
| `other:weights_not_stated_in_text` | 1 | 9% | rfs_2026_rfs_hhaf080 p.21-26 Section 3.2.1, Table 4 notes: Matching is described as five nearest neighbours with replacement, and the text notes that a benchmark firm ca |

### variable_construction (papers with this category: 1/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:balancing_weight_construction` | 1 | 9% | aer_111_12_2 p.18-19 Section IIIA: Constructs taxpayer-level balancing weights through an entropy-balancing procedure that matches treated and co |

### writing_structure (papers with this category: 4/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_heavy` | 3 | 27% | aer_113_6_2 p.6-6 Introduction, end: Relies heavily on the online appendix for supporting figures and tables referenced repeatedly throughout the m; qje_140_1_4 p.10-10 Section I, end: A short roadmap paragraph at the end of the introduction states the section order for the rest of the article, |
| `contribution_paragraph` | 3 | 27% | aer_113_6_2 p.5-6 Introduction: Places a stand-alone contribution paragraph enumerating three separate literatures the paper claims to contrib; qje_140_1_4 p.8-10 Section I.A: A dedicated related-literature subsection immediately follows the introduction and organizes prior work into s |
| `results_previewed_in_intro` | 2 | 18% | aer_113_6_2 p.3-4 Introduction: Previews the paper's main qualitative findings (short-run violence spike, long-run Klan formation, and persist; rfs_2026_rfs_hhaf080 p.2-8 Introduction: The introduction previews every result in the order of the paper (credit dynamics, mechanism, IV, overborrowin |
| `roadmap_paragraph` | 2 | 18% | aer_113_6_2 p.5-6 Introduction: Places a stand-alone contribution paragraph enumerating three separate literatures the paper claims to contrib; qje_140_1_4 p.10-10 Section I, end: A short roadmap paragraph at the end of the introduction states the section order for the rest of the article, |
| `data_before_design` | 1 | 9% | rfs_2026_rfs_hhaf080 p.2-8 Introduction: The introduction previews every result in the order of the paper (credit dynamics, mechanism, IV, overborrowin |
| `main_result_first` | 1 | 9% | rfs_2026_rfs_hhaf080 p.2-8 Introduction: The introduction previews every result in the order of the paper (credit dynamics, mechanism, IV, overborrowin |
| `mechanisms_after_main` | 1 | 9% | rfs_2026_rfs_hhaf080 p.2-8 Introduction: The introduction previews every result in the order of the paper (credit dynamics, mechanism, IV, overborrowin |
| `online_appendix_not_available` | 1 | 9% | aer_113_6_2 p.6-6 Introduction, end: Relies heavily on the online appendix for supporting figures and tables referenced repeatedly throughout the m |
| `other:no_roadmap_paragraph` | 1 | 9% | rfs_2026_rfs_hhaf080 p.26-42 Sections 3.3, 4.1, 4.3.3: There is no roadmap paragraph and no separate robustness section; robustness is folded into the end of each re |
| `other:no_separate_robustness_section` | 1 | 9% | rfs_2026_rfs_hhaf080 p.26-42 Sections 3.3, 4.1, 4.3.3: There is no roadmap paragraph and no separate robustness section; robustness is folded into the end of each re |
| `other:robustness_integrated_in_main_results` | 1 | 9% | jfe_2025_j_jfineco_2025_104150 p.11-16 Section 5.1: Robustness to alternative econometric approaches (matching, overlap-weighting, synthetic control) is integrate |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | paper_only | 1 | restud_2025_restud_rdaf004 s10.sample (paper: 45 days, symmetric / card: abs(t)<=${band} with band unspecified) |
| cluster_level | agree | 8 | aer_111_12_2 s3.se.cluster_level (paper: States that standard errors in the elasticity regression are clustered / card: spec s3 records se.type 'cluster' and se.cluster_level ['npwp'], where); aer_114_7_10 s1.se.cluster_level (paper: Standard errors clustered by county throughout the paper / card: s1 se.type=cluster, se.cluster_level=[fips]) |
| cluster_level | paper_only | 2 | aer_111_12_2 s1.se.cluster_level (paper: States that standard errors in the administration regressions are clus / card: spec s1's se.cluster_level is null; the underlying call uses cluster(`); qje_140_1_4 specifications (paper: For the co-inventor spillover regression (Table III) the text separate / card: No specification extracted in the card corresponds to the co-inventor ) |
| cluster_level | unknown | 2 | restud_2025_restud_rdaf004 s1.se.cluster_level (paper: DiD standard errors clustered at the firm level / card: s1 to s5: cl(identificad)); restud_2026_restud_rdaf027 s1.se.cluster_level (paper: Short-run standard errors clustered by school (shooting plus control s / card: cluster(unique_id); design note interprets unique_id as school match-g) |
| cluster_level | code_only | 1 | qje_140_1_4 s3.se.cluster_level (paper: The main text does not state a cluster level for the shift-share IV re / card: The card records two-way clustering at the region and decade level for) |
| comparison_group | paper_only | 6 | aer_111_12_2 s1.comparison_group (paper: Describes the comparison group as taxpayers not assigned to the medium / card: spec s1's comparison_group field is null.); aer_114_7_10 s1.comparison_group (paper: Comparison group is counties without a Duke funding commitment (never/ / card: s1 comparison_group=null) |
| comparison_group | agree | 1 | restud_2026_restud_rdaf027 d1.implementation_features / packages.teffects (paper: Two nearest-neighbour matched control schools per shooting school, dif / card: teffects nnmatch with fuzzy_vars enrollment, share_female, share_white) |
| controls | paper_only | 5 | aer_114_7_10 s1.controls_summary (paper: Preferred specifications add a control vector (percent illiterate, per / card: s1 controls_summary=null (not resolved from code trace)); jfe_2024_j_jfineco_2024_103809 s2.controls_summary (paper: Even-numbered columns of the main tables add a stated set of firm-leve / card: s2.controls_summary is null.) |
| controls | agree | 2 | qje_140_1_4 s2.controls_summary (paper: The migrant event-study and interaction specifications are described a / card: The card's controls_summary field is unset (null) for the extracted sp); rfs_2026_rfs_hhaf080 d2.evidence (paper: IV stages include the matching covariates as controls plus a shift-sha / card: ivreghdfe call includes $control_0 and volloanv; controls_summary null) |
| controls | disagree | 1 | restud_2025_restud_rdaf004 s10.controls (paper: RD baseline has only eligibility dummy, running variable and interacti / card: s10 adds worker and firm covariates (tempempr, lnrem, school, age, sec) |
| data_source | paper_only | 7 | aer_111_12_2 data (paper: Names several distinct anonymized administrative data extracts obtaine / card: The card's top-level data array is empty.); aer_114_7_10 data[0].source_hint (paper: Data section names specific sources for each processed dataset (Duke E / card: data entries (nc_deaths_event_study_input, gompertz_event_study_input_) |
| data_source | agree | 2 | restud_2026_restud_rdag080 d1 (paper: CDDA designated-area database, Landsat NDVI, Li et al. nightlights, HI / card: Variable names greenness, foundationCS, cddaid consistent with CDDA an); rfs_2026_rfs_hhaf080 data[0] (paper: Credit registry, M-Contran survey, Banque de France FinTech data, scra / card: Three intermediate admin files with unknown access; one is a scraped I) |
| diagnostic | paper_only | 5 | aer_111_12_2 x1 (paper: Reports first-stage F-statistics for both instrumented regressions dir / card: diagnostic x1 records kind 'first_stage' for design d1 with status 'un); jfe_2024_j_jfineco_2024_103809 diagnostics (paper: The paper reports a pre-trends figure, a covariate-balance table, and  / card: diagnostics is an empty list in the card.) |
| diagnostic | agree | 5 | aer_114_7_10 x1 (paper: Paper reports and interprets a formal test of whether Black and White  / card: x1 diagnostic kind=heterogeneous_treatment_effects, status=observed, o); jfe_2025_j_jfineco_2025_104150 diagnostics.x2 (paper: Table 5 reports covariate balance (assets, leverage, ROA, Q, ESG score / card: diagnostics x2 (balance) status=observed, describing a clttest of size) |
| estimator | agree | 14 | aer_111_12_2 s3.estimator (paper: Describes a two-equation instrumental-variables procedure: a first-sta / card: spec s3 records estimator '2sls', command 'ivreghdfe', with the endoge); aer_114_7_10 s1.estimator (paper: First-stage hospital and physician outcomes estimated by a linear two- / card: s1 estimator=hdfe_ols via reghdfe, formula reghdfe depvar b0.treated, ) |
| estimator | paper_only | 2 | jfe_2024_j_jfineco_2024_103809 designs (paper: Coarsened Exact Matching (Iacus et al., 2012) is described as a fourth / card: The card's designs and specifications list only d1/d2/d3 (return_event); jfe_2025_j_jfineco_2025_104150 designs.d1.method (paper: Identification combines a panel OLS quasi-DID, a propensity-score matc / card: d1 records only method=event_study with role, variant, treatment and c) |
| estimator | disagree | 1 | aer_111_12_2 d1/d2 (paper: Frames the administration analysis primarily as a matched difference-i / card: Designs d1 and d2 are both recorded with method 'iv' only, extracted f) |
| estimator | code_only | 1 | qje_140_1_4 s3.formula_or_call (paper: The text names a shift-share instrumental-variables strategy based on  / card: The card's IV specification (s3) is a two-stage-least-squares regressi) |
| fixed_effects | agree | 10 | aer_111_12_2 s1.fixed_effects (paper: States that the administration regressions include taxpayer fixed effe / card: spec s1 records fixed_effects as the Stata absorb() variables 'npwp' a); aer_111_12_2 s3.fixed_effects (paper: States that the elasticity regression includes taxpayer and year fixed / card: spec s3 records fixed_effects as 'year' and 'npwp' (taxpayer identific) |
| fixed_effects | paper_only | 2 | jfe_2024_j_jfineco_2024_103809 s2.fixed_effects (paper: The difference-in-differences specification includes firm fixed effect / card: s2.fixed_effects is null in the card's structured fields, even though ); jpe_2026_740222 s1.fixed_effects (paper: Table 2 lists a progression of fixed effects for the preferred column: / card: Specification s1.fixed_effects is null; the card's evidence trace only) |
| fixed_effects | disagree | 2 | qje_140_1_4 s1.fixed_effects (paper: The main text describes the leads-and-lags event-study specification ( / card: The card's leads-and-lags specification (s1) additionally absorbs a te); restud_2025_restud_rdaf004 s10.fe (paper: RD: no fixed effects in the baseline local linear model / card: s10 absorb(mun)) |
| other | paper_only | 1 | aer_114_7_10 d1.variant (paper: Design is named specifically as a staggered-adoption difference-in-dif / card: d1 method=did, variant=null) |
| outputs | paper_only | 6 | aer_114_7_10 outputs.tables (paper: Six numbered main tables and five numbered main figures reported in th / card: outputs.tables=[] and outputs.figures=[] in the card); jfe_2025_j_jfineco_2025_104150 outputs.tables (paper: Paper presents eleven main numbered tables and six main numbered figur / card: outputs.tables and outputs.figures are both empty arrays) |
| outputs | agree | 1 | restud_2026_restud_rdaf027 outputs.tables.t2 (paper: Tables 2 and 3 report long-run educational and labor market outcomes f / card: t2 and t3 produced by esttab from B3_Long_run_analysis_baseline.do; st) |
| outputs | disagree | 1 | restud_2026_restud_rdag080 outputs (paper: Four main tables, eight main figures and appendix tables A.3 to A.16. / card: tables 0, figures 2 with partial coverage.) |
| robustness | paper_only | 8 | aer_111_12_2 robustness (paper: Describes extensive robustness checks for both empirical exercises (al / card: The card's top-level robustness array is empty.); aer_114_7_10 robustness (paper: Extensive robustness section covering alternative estimators, alternat / card: robustness array is empty in the card) |
| robustness | agree | 1 | restud_2026_restud_rdag080 robustness[0] (paper: TWFE and matched TWFE reported as alternatives to the preferred estima / card: Robustness record alt_estimator base s2 variant s3 confirmed; s1 alt u) |
| sample | paper_only | 5 | aer_111_12_2 s3.sample (paper: States the elasticity sample uses CIT filings for the tax years immedi / card: spec s3's sample field is null, though the raw formula_or_call include); jfe_2024_j_jfineco_2024_103809 pipeline.sample_restrictions (paper: The difference-in-differences analysis is run on a balanced panel of f / card: pipeline.sample_restrictions is an empty list and s1/s2/s3 sample fiel) |
| sample | agree | 3 | aer_114_7_10 pipeline.sample_restrictions[0] (paper: Main analysis restricted to North Carolina counties and birth years 19 / card: pipeline sample_restrictions: statefip==37 (North Carolina) births, 19); restud_2025_restud_rdaf004 s1.sample (paper: DiD main sample restricted to mass layoffs; ITT and plant closure vari / card: s1 if mass==1; s3 if empcont==1 & t<=103) |
| sample | unknown | 1 | restud_2026_restud_rdag080 s2.sample (paper: Some estimations use a stratified 1 percent random sample of never-tre / card: Script named 4_CS_small.R uses object strat_sample; sample restriction) |
| se_type | agree | 4 | jfe_2024_j_jfineco_2024_103809 s2.se.cluster_level (paper: Baseline panel regressions (returns, volatility, risk-adjusted returns / card: s2.se.type is cluster with cluster_level firm.); jfe_2024_j_jfineco_2024_103809 s1.se (paper: The event-study table (Table 2) note states only that standard errors  / card: s1.se.type is cluster with cluster_level firm, taken from the clus(fir) |
| se_type | paper_only | 3 | jfe_2024_j_jfineco_2024_103809 specifications (paper: The firm-year dividend regressions and the media-coverage regression a / card: No specification in the card corresponds to the dividend regression or); restud_2026_restud_rdaf027 s1.se.type (paper: Wild cluster bootstrap for few-cluster subgroup analyses; permutation  / card: Only cluster-robust SE recorded for s1.) |
| se_type | unknown | 1 | aer_114_7_10 s2.se.type (paper: Text does not separately describe the standard-error method used speci / card: s2 se.type=null, se.cluster_level=null (unresolved in code trace)) |
| weights | paper_only | 6 | aer_111_12_2 s1.weights (paper: States that the administration regressions are weighted by taxpayer-sp / card: spec s1's structured weights field is null, though the raw formula_or_); aer_114_7_10 s1.weights (paper: Preferred specifications weight observations by county-by-year (or wav / card: s1 weights=null; s2 formula references an unresolved iw=weightvar) |
| weights | agree | 2 | qje_140_1_4 s2.weights (paper: No specification in the empirical section is described as weighted. / card: The card's weights field is unset (null) for every extracted specifica); restud_2025_restud_rdaf004 s5.weights (paper: Entropy balancing reweighting for robustness (job loss and RD samples) / card: s5 [w=wei] in balancing do-file) |
| weights | code_only | 1 | rfs_2026_rfs_hhaf080 s1.weights (paper: No regression weights are mentioned; matching is five nearest neighbou / card: pweight=weight in both s1 and s2.) |

## Gaps the readers reported

- (1) No pre-analysis plan, IRB approval, or participant consent statement appears anywhere in the article text.
- (1) No explicit software name (e.g., Stata) appears anywhere in the article text, even though this is a code-based empirical
- (1) No dedicated data-and-code availability statement appears in the article body describing what the cited replication pack
- (1) No explicit multiple-testing adjustment is discussed despite many outcomes and subgroups being tested across the adminis
- (1) No R-squared or adjusted R-squared is reported on any main regression table.
- (1) No explicit justification is given in the main text for choosing the taxpayer level for standard-error clustering, beyon
- (1) No statistical software (e.g., Stata, R) is named anywhere in the main text, even though the paper is a code-based empir
- (1) No dedicated data-and-code availability statement appears in the article body describing what the replication package co
- (1) No pre-analysis plan, IRB approval, or participant-consent statement appears anywhere in the text; the study uses archiv
- (1) No explicit justification for choosing the state as the standard-error clustering level appears in the main text beyond 
- (1) No explicit multiple-testing adjustment is discussed despite many outcome variables (lynchings, riots, homicides, klaver
- (1) The extracted text contains only the published article; the online Appendix referenced dozens of times (additional figur
- (1) No preregistration, pre-analysis plan, or IRB/ethics statement found anywhere in the main text.
- (1) No explicit multiple-testing adjustment stated despite reporting many outcome subgroups (race splits) and robustness var
- (1) No dedicated summary-statistics table appears in the main text itself; it is referenced as being in the online appendix 
- (1) No explicit statement of statistical software beyond what can be inferred from the recipe card's Stata commands (reghdfe
- (1) No formal density or manipulation test is reported, consistent with the design not relying on a running-variable cutoff.
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
- (1) No preregistration, pre-analysis plan, IRB approval, or research-ethics/consent statement appears anywhere in the read m
- (1) No explicit statement of the statistical software, package, or version used for estimation appears in the main text; thi
- (1) No formal joint-significance test (for example an F-test or Wald test) for the pre-acquisition event-study coefficients 

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
