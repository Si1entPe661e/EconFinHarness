# Reported practice: `shift_share` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 8 paper notes (8 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | AER: 3, QJE: 2, ReStud: 2, RFS: 1 |
| year | 2022: 2, 2023: 1, 2024: 1, 2025: 2, 2026: 2 |
| papers with at least one observation in category | writing_structure: 8, design_statement: 7, variable_construction: 7, replication_statement: 7, data_access: 7, sample_construction: 6, specification_reporting: 6, diagnostic_reported: 6, mechanism_evidence: 6, limitation_stated: 6, presentation_convention: 6, inference_justification: 5, robustness_reported: 5, external_validity: 5, heterogeneity_reported: 4, magnitude_interpretation: 4, other: 2 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_112_2_1 | AER | 2022 | full | yes | 2058c8346285 |
| aer_113_3_7 | AER | 2023 | full | yes | 65ba0a218650 |
| aer_114_7_10 | AER | 2024 | full | yes | a2ce2c0a92fe |
| qje_140_1_10 | QJE | 2025 | main_text | yes | e8ba74c8ad78 |
| qje_140_1_4 | QJE | 2025 | partial | yes | 793bd3a24ebb |
| restud_2026_restud_rdag027 | ReStud | 2026 | full | yes | 9ee63c03e3b3 |
| restud_89_1_6 | ReStud | 2022 | full | yes | 2aa31e3b1004 |
| rfs_2026_rfs_hhaf080 | RFS | 2026 | full | yes | bef15266e552 |

## Practices by category and tag


### data_access (papers with this category: 7/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 4 | 50% | aer_112_2_1 p.6-8 Section II: Historical data are drawn from complete-count decennial censuses and a historical government statistical compe; qje_140_1_4 p.31-32 Section III.A: The empirical analysis is built from two named external academic data products rather than data collected by t |
| `linked_records` | 3 | 38% | aer_112_2_1 p.2-2 Introduction, data paragraph: A newly digitized and harmonized database on local-government finance, private schooling, and crime is describ; restud_2026_restud_rdag027 p.14-34 Section 4.1; footnote 23: Data combine public complete-count censuses and Census Tree links, public digital collections (SPLC, GNIS, TIG |
| `public_use` | 3 | 38% | aer_112_2_1 p.6-8 Section II: Historical data are drawn from complete-count decennial censuses and a historical government statistical compe; restud_2026_restud_rdag027 p.14-34 Section 4.1; footnote 23: Data combine public complete-count censuses and Census Tree links, public digital collections (SPLC, GNIS, TIG |
| `commercial` | 2 | 25% | aer_113_3_7 p.8-22 Sections I.B, II.A, III.A: The analysis draws on commercial and subscription data sources (a newswire archive, two news-content archives,; rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |
| `data_access_procedure_described` | 2 | 25% | aer_112_2_1 p.2-2 Introduction, data paragraph: A newly digitized and harmonized database on local-government finance, private schooling, and crime is describ; aer_113_3_7 p.8-22 Sections I.B, II.A, III.A: The analysis draws on commercial and subscription data sources (a newswire archive, two news-content archives, |
| `data_public` | 1 | 12% | restud_89_1_6 p.32-32 Acknowledgments, Data Availability Statement: The application relies on replication data and code shared by the authors of the original studies, acknowledge |
| `data_restricted` | 1 | 12% | rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |
| `in_footnote` | 1 | 12% | qje_140_1_10 p.18-18 Section III.C, footnote 20: Credits a named collaborator for jointly digitizing the municipal manufacturing survey data in a footnote, doc |
| `other:provenance_credited` | 1 | 12% | qje_140_1_10 p.18-18 Section III.C, footnote 20: Credits a named collaborator for jointly digitizing the municipal manufacturing survey data in a footnote, doc |
| `survey_collected` | 1 | 12% | aer_113_3_7 p.8-22 Sections I.B, II.A, III.A: The analysis draws on commercial and subscription data sources (a newswire archive, two news-content archives, |
| `web_scraped` | 1 | 12% | rfs_2026_rfs_hhaf080 p.1-12 Acknowledgements, Section 2.1: Data combine central bank administrative and confidential registry files, a web-scraped aggregator, a commerci |

### design_statement (papers with this category: 7/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 7 | 88% | aer_112_2_1 p.11-17 Section III, Empirical Strategy: The paper names its design as a shift-share instrumental-variables strategy and states the estimand as the eff; aer_113_3_7 p.24-24 Section III.B: The county-level instrumental-variables step is explicitly named as akin to a shift-share strategy, with the p |
| `instrument_exclusion_argued` | 6 | 75% | aer_112_2_1 p.12-17 Section III: Exclusion is argued through a push-versus-pull distinction: southern out-migration shocks are argued to be ort; aer_113_3_7 p.24-24 Section III.B: The county-level instrumental-variables step is explicitly named as akin to a shift-share strategy, with the p |
| `estimand_named` | 5 | 62% | aer_112_2_1 p.11-17 Section III, Empirical Strategy: The paper names its design as a shift-share instrumental-variables strategy and states the estimand as the eff; qje_140_1_10 p.20-31 Section IV, equation (2); Section V.A, equation (5): States three linked designs: an industry-level difference-in-differences comparing manufacturing industries by |
| `identifying_assumption_explicit` | 5 | 62% | aer_112_2_1 p.15-15 Section III, Identifying Assumption and Validity Checks, equation 7: The identifying assumption is written out as a formal orthogonality condition between the predicted-migration ; qje_140_1_10 p.32-33 Section V.A.1: Argues that measuring local exposure from preexposure 1939 industry labor shares, rather than actual reparatio |
| `threats_discussed` | 5 | 62% | aer_112_2_1 p.12-17 Section III: Exclusion is argued through a push-versus-pull distinction: southern out-migration shocks are argued to be ort; qje_140_1_10 p.32-33 Section V.A.1: Argues that measuring local exposure from preexposure 1939 industry labor shares, rather than actual reparatio |
| `in_main_text` | 3 | 38% | restud_2026_restud_rdag027 p.3-3 Section 1, paragraph on identification; Section 4.2: The core design is named a shift-share instrumental variable (SSIV) framework: 1870 cross-county migrant netwo; restud_89_1_6 p.5-6 Section 2.1, equations (1)-(3): The paper states the target parameter as the coefficient in a linear causal or structural model with a control |
| `compliers_described` | 2 | 25% | restud_2026_restud_rdag027 p.19-19 Section 4.3, Discussion: interpreting magnitudes: The IV estimate is explicitly interpreted as a LATE for counties with the strongest chain migration; the autho; rfs_2026_rfs_hhaf080 p.41-42 Section 4.3.2, footnote 44, Internet Appendix Section I: The IV coefficient is explicitly interpreted as a LATE for compliers responding to bank collateral requirement |
| `in_footnote` | 1 | 12% | rfs_2026_rfs_hhaf080 p.37-39 Section 4.3.1, footnote 39: The shift-share IV section spells out relevance and exclusion conditions, names the main threat (collateral re |

### diagnostic_reported (papers with this category: 6/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 5 | 62% | aer_112_2_1 p.16-16 Section III, footnote 13: A footnote states that the instrument also does not predict several other baseline socioeconomic characteristi; qje_140_1_4 p.46-46 Section III.B.4: The main text names the shift-share IV strategy for the local spillover result but does not present a first-st |
| `in_main_text` | 5 | 62% | aer_112_2_1 p.17-21 Figure 5; Table 2, Panel A: A first-stage coefficient and an F-statistic for the excluded instrument are reported at the top of every main; qje_140_1_10 p.34-34 Table V: Reports an analogous municipality-level balance table with preperiod levels and changes in observable characte |
| `weak_iv_statistic` | 5 | 62% | aer_112_2_1 p.17-21 Figure 5; Table 2, Panel A: A first-stage coefficient and an F-statistic for the excluded instrument are reported at the top of every main; qje_140_1_4 p.46-46 Section III.B.4: The main text names the shift-share IV strategy for the local spillover result but does not present a first-st |
| `first_stage_table` | 4 | 50% | aer_112_2_1 p.17-21 Figure 5; Table 2, Panel A: A first-stage coefficient and an F-statistic for the excluded instrument are reported at the top of every main; restud_2026_restud_rdag027 p.17-17 Section 4.3, first paragraph; Appendix Table B.1: The first-stage estimates for the main table are relegated to an appendix table and described in the text as s |
| `overid_test` | 3 | 38% | aer_112_2_1 p.16-17 Section III; online Appendix Figure D16: Two additional instrument constructions are built from alternative sources of origin-county variation, and a f; restud_2026_restud_rdag027 p.18-18 Table 2 panel (b) and notes: IV tables report a first-stage F-statistic, Anderson-Rubin p-value, Kleibergen-Paap underidentification p-valu |
| `placebo_outcomes` | 3 | 38% | aer_112_2_1 p.33-34 Figure 9, panel A: The mechanism analysis separately plots the instrument's association with pre-1940 values of the same mechanis; restud_2026_restud_rdag027 p.19-19 Section 4.3; Appendix Table B.4: A placebo-type outcome check compares effects on lynchings of Black people with lynchings of non-Black minorit |
| `balance_table` | 2 | 25% | qje_140_1_10 p.34-34 Table V: Reports an analogous municipality-level balance table with preperiod levels and changes in observable characte; restud_89_1_6 p.26-27 Section 6.2.3, Table 3 Panels A and B: Two kinds of balance tests are reported in one table: shock-level regressions of predetermined industry covari |
| `online_appendix_not_available` | 2 | 25% | aer_112_2_1 p.16-16 Section III, footnote 13: A footnote states that the instrument also does not predict several other baseline socioeconomic characteristi; qje_140_1_4 p.46-46 Section III.B.4: The main text names the shift-share IV strategy for the local spillover result but does not present a first-st |
| `pre_trends_test` | 2 | 25% | aer_112_2_1 p.16-16 Table 1: A dedicated placebo table regresses the instrument on pre-treatment-period school-attendance and education out; restud_89_1_6 p.27-27 Section 6.2.3, Table 3 Panel B last rows: A pre-trend test regresses lagged outcome growth from two earlier decades on the instrument using the same spe |
| `attrition_analysis` | 1 | 12% | aer_112_2_1 p.25-25 Section IV.B: The text discusses possible sample attrition from reverse migration out of destination commuting zones and arg |
| `binscatter` | 1 | 12% | restud_89_1_6 p.28-28 footnote 48, Supplementary Appendix Figure C1: Binned scatter plots of the industry-level first-stage and reduced-form relationships for the preferred specif |
| `other:instrument_correlation_reported` | 1 | 12% | restud_2026_restud_rdag027 p.25-25 Section 5.1, Former slaveholder migrants: For the slaveholder versus non-slaveholder SSIVs the paper reports the correlation between the two instruments |
| `other:monte_carlo` | 1 | 12% | restud_89_1_6 p.19-19 Section 5.3, Supplementary Appendix A.11: Monte Carlo simulations of finite-sample coverage and weak-instrument behaviour are summarized in a short main |
| `other:random_shifts_placebo` | 1 | 12% | restud_2026_restud_rdag027 p.17-17 Section 4.2, final paragraph: The Adao, Kolesar and Morales random-shifts placebo exercise is implemented to validate the shift-based identi |
| `other:shares_lag_sensitivity` | 1 | 12% | rfs_2026_rfs_hhaf080 p.42-42 Section 4.3.3, Internet Appendix Table I.1: The stability of the shares is checked in an appendix table by rebuilding the instrument with shares lagged th |
| `other:shock_distribution_summary` | 1 | 12% | restud_89_1_6 p.23-25 Section 6.2.2, Table 1: Before estimation, the distribution of shocks (mean, SD, interquartile range) is summarized with and without t |
| `pre_trends_plot` | 1 | 12% | aer_112_2_1 p.33-34 Figure 9, panel A: The mechanism analysis separately plots the instrument's association with pre-1940 values of the same mechanis |

### external_validity (papers with this category: 5/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 3 | 38% | aer_112_2_1 p.37-37 Section VI, Conclusion: The conclusion explicitly discusses implications for the scalability of moving-to-opportunity style policies a; qje_140_1_4 p.6-7 Section I, end: The paper explicitly generalizes its inventor-specific findings to other categories of high-skilled workers, n |
| `in_main_text` | 2 | 25% | restud_2026_restud_rdag027 p.31-44 Section 5.2; Section 8: The authors contrast the 1870 to 1900 wave with the later 20th-century Southern White migration, showing in ap; restud_89_1_6 p.19-21 Section 6.1: Applicability of the framework is described as depending on details of each application; examples across trade |
| `site_specific` | 2 | 25% | restud_89_1_6 p.19-21 Section 6.1: Applicability of the framework is described as depending on details of each application; examples across trade; rfs_2026_rfs_hhaf080 p.47-48 Section 6, footnotes 47 and 48: The conclusion has a dedicated generalisation paragraph arguing portability beyond France (collateral constrai |
| `time_period_specific` | 1 | 12% | restud_2026_restud_rdag027 p.31-44 Section 5.2; Section 8: The authors contrast the 1870 to 1900 wave with the later 20th-century Southern White migration, showing in ap |

### heterogeneity_reported (papers with this category: 4/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `split_sample` | 4 | 50% | aer_112_2_1 p.25-28 Figure 8; Tables 5-6: Effects are estimated separately by race, gender, and parent-income group, first summarized in a single coeffi; aer_113_3_7 p.30-30 Table 7, test-for-equality row: Differences between heterogeneity subgroups are accompanied by an explicit formal test for equality of coeffic |
| `mechanism_motivated` | 2 | 25% | aer_112_2_1 p.28-29 Section IV.B: The gender split in the heterogeneity analysis is explicitly framed as motivated by prior findings that boys' ; qje_140_1_10 p.24-53 Table III, columns 5-8; Table XI: Splits treatment intensity by industry skill level throughout the industry, local, and individual analyses to  |
| `in_main_text` | 1 | 12% | restud_2026_restud_rdag027 p.20-22 Table 3 and notes: Separate SSIVs are built for migrant subgroups (border, upper South, deep South; Union North by slavery histor |
| `interaction` | 1 | 12% | aer_112_2_1 p.25-28 Figure 8; Tables 5-6: Effects are estimated separately by race, gender, and parent-income group, first summarized in a single coeffi |

### inference_justification (papers with this category: 5/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_se` | 2 | 25% | restud_2026_restud_rdag027 p.15-19 Section 4.2; Section 4.3 Identification and robustness checks: Clustering by square grid cells is justified by citing Bester et al., and robustness to other spatial structur; restud_89_1_6 p.28-28 footnote 47, Supplementary Appendix Table C2: Three alternative inference methods (conventional state-clustered SEs as in ADH, Adao et al. SEs, and null-imp |
| `cluster_at_assignment_level` | 2 | 25% | qje_140_1_10 p.20-35 Section IV, equation (2); Section V.B.1, equation (8): Clusters standard errors at the level treatment varies for each analysis: industry for the industry-level desi; restud_89_1_6 p.25-26 Section 6.2.2, equation (11), Table 2: The clustering level for shocks (SIC3) is chosen empirically by estimating intra-class correlations of shock r |
| `in_appendix` | 2 | 25% | qje_140_1_10 p.55-55 Section VII.A: States that it follows recent methodological literature on shift-share inference and provides the associated r; restud_89_1_6 p.28-28 footnote 47, Supplementary Appendix Table C2: Three alternative inference methods (conventional state-clustered SEs as in ADH, Adao et al. SEs, and null-imp |
| `in_main_text` | 2 | 25% | restud_2026_restud_rdag027 p.15-19 Section 4.2; Section 4.3 Identification and robustness checks: Clustering by square grid cells is justified by citing Bester et al., and robustness to other spatial structur; restud_89_1_6 p.17-18 Section 5.1, Proposition 5: Standard errors are justified by a formal result: estimating the numerically equivalent shock-level IV regress |
| `in_footnote` | 1 | 12% | restud_89_1_6 p.28-28 footnote 47, Supplementary Appendix Table C2: Three alternative inference methods (conventional state-clustered SEs as in ADH, Adao et al. SEs, and null-imp |
| `no_justification_found` | 1 | 12% | aer_112_2_1 p.15-31 Section III; table notes throughout: No sentence in the main text states why a particular clustering level, or the absence of clustering, was chose |
| `other:effective_sample_size_reported` | 1 | 12% | restud_89_1_6 p.24-24 Section 6.2.2, Table 1: The authors recommend and report the inverse Herfindahl index of shock-level exposure weights as the effective |
| `other:exposure_robust_shock_level_se` | 1 | 12% | restud_89_1_6 p.17-18 Section 5.1, Proposition 5: Standard errors are justified by a formal result: estimating the numerically equivalent shock-level IV regress |
| `other:icc_based_cluster_choice` | 1 | 12% | restud_89_1_6 p.25-26 Section 6.2.2, equation (11), Table 2: The clustering level for shocks (SIC3) is chosen empirically by estimating intra-class correlations of shock r |
| `other:no_multiple_testing_adjustment_stated` | 1 | 12% | aer_112_2_1 p.25-36 Section IV.B; Section V: No adjustment for testing across the many mechanism outcomes or subgroup splits is stated when the mechanism a |
| `other:shift_share_inference` | 1 | 12% | qje_140_1_10 p.55-55 Section VII.A: States that it follows recent methodological literature on shift-share inference and provides the associated r |
| `other:weak_iv_robust_ci` | 1 | 12% | rfs_2026_rfs_hhaf080 p.40-41 Table 8 Panel A bottom rows, Section 4.3.2: Following a cited guide on IV in corporate finance, the paper reports the Kleibergen-Paap robust F statistic a |
| `other:weak_iv_statistic_reported` | 1 | 12% | rfs_2026_rfs_hhaf080 p.40-41 Table 8 Panel A bottom rows, Section 4.3.2: Following a cited guide on IV in corporate finance, the paper reports the Kleibergen-Paap robust F statistic a |
| `randomization_inference` | 1 | 12% | aer_112_2_1 p.16-17 Section III, discussion following equation 7: Instead of a clustering argument, the authors address a shift-share-specific inference concern by re-running t |
| `spatial_hac` | 1 | 12% | restud_2026_restud_rdag027 p.15-19 Section 4.2; Section 4.3 Identification and robustness checks: Clustering by square grid cells is justified by citing Bester et al., and robustness to other spatial structur |

### limitation_stated (papers with this category: 6/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identification_caveat` | 4 | 50% | aer_112_2_1 p.15-15 Section III, Identifying Assumption: The authors state that the core orthogonality assumption cannot be directly tested and can only be supported i; qje_140_1_10 p.40-40 Section V.C.1: Notes that the local difference-in-differences and the Norway-based triple-difference local estimates are not  |
| `interpretation_caveat` | 4 | 50% | aer_112_2_1 p.4-4 Introduction: The introduction explicitly states that the paper does not speak to the causal effect of the Migration on the ; qje_140_1_10 p.58-58 Section VIII: States explicitly that the analysis does not claim local industrialization could not have occurred absent the  |
| `measurement` | 4 | 50% | aer_112_2_1 p.7-7 Section II.A: The authors note several data constraints, including that earlier cohorts cannot be studied because neither a ; aer_113_3_7 p.31-31 Section III.D, Magnitudes: The authors note that coverage in their commercial content databases is not universal, so article-count-based  |
| `data_coverage` | 3 | 38% | aer_112_2_1 p.7-7 Section II.A: The authors note several data constraints, including that earlier cohorts cannot be studied because neither a ; aer_113_3_7 p.31-31 Section III.D, Magnitudes: The authors note that coverage in their commercial content databases is not universal, so article-count-based  |
| `external_validity` | 2 | 25% | aer_112_2_1 p.4-4 Introduction: The introduction explicitly states that the paper does not speak to the causal effect of the Migration on the ; aer_113_3_7 p.32-32 Section IV, Conclusion: External validity is explicitly flagged as limited to the specific setting of unauthorized-immigration languag |
| `in_main_text` | 2 | 25% | restud_2026_restud_rdag027 p.19-25 Section 4.3; Section 5.1: Authors state that county-level models cannot separate the relative roles of spill-overs, organisations and in; restud_89_1_6 p.21-21 Section 6.2 opening: The authors state the application is meant to illustrate the framework, not to reassess the substantive findin |

### magnitude_interpretation (papers with this category: 4/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `back_of_envelope` | 3 | 38% | aer_112_2_1 p.24-25 Table 4 and surrounding discussion: A scaling exercise converts the per-year childhood-exposure estimate into a full-childhood magnitude under two; restud_2026_restud_rdag027 p.19-37 Section 4.3 Discussion; footnote 28: A more-than-compositional argument compares the IV coefficient with what a purely mechanical composition effec |
| `compared_to_literature` | 3 | 38% | aer_112_2_1 p.2-2 Introduction: The main coefficient is rescaled to a one-standard-deviation shock and set alongside a comparable estimate fro; restud_89_1_6 p.28-30 Section 6.2.4, footnotes 47 and 49: Estimates are interpreted by comparison across columns and against the original ADH and Acemoglu et al. number |
| `precision_discussed` | 3 | 38% | aer_112_2_1 p.24-25 Table 4 and surrounding discussion: A scaling exercise converts the per-year childhood-exposure estimate into a full-childhood magnitude under two; restud_2026_restud_rdag027 p.19-26 Section 4.3 Discussion; Section 5.1; Appendix B.5: The OLS versus IV gap is discussed at length, attributing it to measurement error in historical data, economic |
| `sd_units` | 3 | 38% | aer_112_2_1 p.2-2 Introduction: The main coefficient is rescaled to a one-standard-deviation shock and set alongside a comparable estimate fro; restud_2026_restud_rdag027 p.17-19 Section 4.3: Effects are interpreted per percentage point of migrant share relative to the outcome mean, and as the move fr |
| `in_main_text` | 2 | 25% | restud_2026_restud_rdag027 p.17-19 Section 4.3: Effects are interpreted per percentage point of migrant share relative to the outcome mean, and as the move fr; restud_89_1_6 p.28-30 Section 6.2.4, footnotes 47 and 49: Estimates are interpreted by comparison across columns and against the original ADH and Acemoglu et al. number |
| `cost_benefit` | 1 | 12% | rfs_2026_rfs_hhaf080 p.45-47 Section 5.2, footnote 46, Internet Appendix Sections J and K: Interest-expense and investor-return calculations combine regression estimates with summary statistics and ext |
| `other:binscatter_slope_comparison` | 1 | 12% | rfs_2026_rfs_hhaf080 p.33-34 Figure 6, Section 4.1.4: A binned scatter of new loan size against subsequent bank credit growth for the two groups is used to compare  |
| `relative_to_mean` | 1 | 12% | restud_2026_restud_rdag027 p.17-19 Section 4.3: Effects are interpreted per percentage point of migrant share relative to the outcome mean, and as the move fr |

### mechanism_evidence (papers with this category: 6/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `suggestive_labelled` | 4 | 50% | aer_112_2_1 p.35-35 Section V.A, Discussion of Local Mechanisms: The authors state that separating the causal contribution of each individual candidate mechanism is beyond wha; aer_113_3_7 p.31-32 Section III.E, Persuasion versus Social Signaling: The authors rule out a social-signaling alternative to persuasion by pointing to the anonymity of the online s |
| `intermediate_outcomes` | 2 | 25% | aer_112_2_1 p.32-35 Section V: A newly assembled panel of local-government spending, private schooling, crime, and incarceration measures is ; qje_140_1_10 p.37-37 Section V.B.4: Uses local manufacturing power usage as a proxy for capital accumulation to provide intermediate-outcome evide |
| `model_guided` | 2 | 25% | aer_113_3_7 p.31-33 Section III.E, Equivalence versus Emphasis Framing: The paper distinguishes two conceptually different treatments bundled in the natural experiment, an equivalenc; aer_114_7_10 p.25-28 Section IV.D: Interaction between Duke support and the arrival of sulfa drugs is tested with a shift-share-style specificati |
| `ruled_out_alternatives` | 2 | 25% | aer_113_3_7 p.31-32 Section III.E, Persuasion versus Social Signaling: The authors rule out a social-signaling alternative to persuasion by pointing to the anonymity of the online s; restud_89_1_6 p.29-30 Section 6.2.4, footnote 49: Differences between specifications are attributed to a specific confound (a sector-wide manufacturing decline  |
| `heterogeneity_as_mechanism` | 1 | 12% | aer_112_2_1 p.18-20 Section IV.A: The contrast between the location-only causal exposure measure and the raw average-outcome measure is used as  |
| `in_footnote` | 1 | 12% | rfs_2026_rfs_hhaf080 p.27-27 footnote 28: A footnote uses loan-to-value reasoning to distinguish sequential from simultaneous financing and compares imp |
| `in_main_text` | 1 | 12% | restud_89_1_6 p.29-30 Section 6.2.4, footnote 49: Differences between specifications are attributed to a specific confound (a sector-wide manufacturing decline  |
| `other:industrial_linkages` | 1 | 12% | qje_140_1_10 p.55-55 Section VII.B: Follows an established methodology for measuring upstream and downstream industrial linkages to test whether m |

### other (papers with this category: 2/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 12% | restud_2026_restud_rdag027 p.11-16 Section 3; Section 4.2: The descriptive push and pull regressions in Section 3 are explicitly framed as setting the stage for the inst |
| `other:descriptive_regression_of_loan_terms` | 1 | 12% | rfs_2026_rfs_hhaf080 p.14-16 Table 2, Section 2.2.2 and 2.2.3: Before the main analysis, FinTech and bank loans are compared by regressing loan size, maturity and rate on a  |
| `other:descriptive_stage_motivates_instrument` | 1 | 12% | restud_2026_restud_rdag027 p.11-16 Section 3; Section 4.2: The descriptive push and pull regressions in Section 3 are explicitly framed as setting the stage for the inst |

### presentation_convention (papers with this category: 6/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `notes_state_se` | 6 | 75% | aer_112_2_1 p.21-31 Table notes throughout: Every table note restates the unit of observation, the outcome definition, the instrument definition, and that; aer_113_3_7 p.16-19 Figures 5-7 notes: Figures pair time-series or coefficient plots with confidence bands, and every figure note states the fixed ef |
| `coefficient_plot` | 5 | 62% | aer_112_2_1 p.26-26 Figure 8: Subgroup heterogeneity results are summarized visually as a single horizontal coefficient plot with confidence; aer_113_3_7 p.16-19 Figures 5-7 notes: Figures pair time-series or coefficient plots with confidence bands, and every figure note states the fixed ef |
| `notes_state_sample` | 4 | 50% | aer_112_2_1 p.21-31 Table notes throughout: Every table note restates the unit of observation, the outcome definition, the instrument definition, and that; restud_2026_restud_rdag027 p.18-29 Notes to Tables 2, 4, 6: Table notes restate the sample, the instrument construction, control groups by reference to the main table's n |
| `summary_stats_table` | 4 | 50% | qje_140_1_10 p.22-34 Table II; Table V: Provides descriptive summary statistics, including means, minima, and maxima of key variables, jointly with ba; restud_2026_restud_rdag027 p.3-39 Figures 1 to 6; Appendix Tables A.1, C.3 to C.5: Figures are county maps of the regressor and composite outcome, a moving-average time series of naming frequen |
| `appendix_tables_numbered_a` | 3 | 38% | aer_113_3_7 p.9-9 Section I.C, footnote citing Online Appendix Figure A3: Appendix tables and figures are numbered with a letter prefix tied to the section they support (A for the AP-t; restud_2026_restud_rdag027 p.18-29 Notes to Tables 2, 4, 6: Table notes restate the sample, the instrument construction, control groups by reference to the main table's n |
| `no_stars` | 3 | 38% | aer_112_2_1 p.21-31 Tables 2-9: As extracted, the regression tables show coefficients and parenthetical standard errors without significance-s; aer_113_3_7 p.15-15 Table 2: Regression tables report point estimates with standard errors in parentheses beneath, without significance sta |
| `binscatter` | 2 | 25% | aer_112_2_1 p.9-34 Figures 3, 5, 6, 7, 9: The paper's main bivariate relationships, including the first stage, reduced form, exposure effects, and mecha; rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `event_study_figure` | 2 | 25% | qje_140_1_10 p.28-49 Figure III; Figure V; Online Appendix Figure A.III: Uses year- or cohort-interacted coefficient plots with shaded confidence bands as the standard way of presenti; rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `map` | 2 | 25% | qje_140_1_10 p.32-32 Figure IV: Includes a choropleth map of the municipal-level exposure measure by quartile to visually convey the geographi; restud_2026_restud_rdag027 p.3-39 Figures 1 to 6; Appendix Tables A.1, C.3 to C.5: Figures are county maps of the regressor and composite outcome, a moving-average time series of naming frequen |
| `raw_data_plot` | 2 | 25% | aer_112_2_1 p.9-34 Figures 3, 5, 6, 7, 9: The paper's main bivariate relationships, including the first stage, reduced form, exposure effects, and mecha; restud_2026_restud_rdag027 p.3-39 Figures 1 to 6; Appendix Tables A.1, C.3 to C.5: Figures are county maps of the regressor and composite outcome, a moving-average time series of naming frequen |
| `stars_used` | 2 | 25% | qje_140_1_10 p.24-53 Table III notes; Table XI notes: Uses a conventional three-tier significance-star convention and states the corresponding significance threshol; rfs_2026_rfs_hhaf080 p.14-46 Figures 1 to 6, Tables 1 to 10: Figures are event-study coefficient plots with confidence intervals (base period minus one), a standardized-di |
| `in_appendix` | 1 | 12% | restud_89_1_6 p.1-33 whole paper; footnote 48: The main text contains four tables and no figures; the only figure (binned scatters) is in the supplementary a |
| `in_main_text` | 1 | 12% | restud_89_1_6 p.24-29 Tables 1-4 notes: Tables use no significance stars; notes describe the estimation procedure, the SE construction and cluster lev |
| `online_appendix_not_available` | 1 | 12% | rfs_2026_rfs_hhaf080 p.1-47 Title page note, references throughout: Internet Appendix material is referenced by lettered sections and tables or figures (A.1 to K), covering varia |
| `other:checkmark_control_grid` | 1 | 12% | restud_89_1_6 p.29-29 Table 4: The main results table uses a checkmark grid of control groups under the coefficient row rather than listing c |
| `other:no_main_text_figures` | 1 | 12% | restud_89_1_6 p.1-33 whole paper; footnote 48: The main text contains four tables and no figures; the only figure (binned scatters) is in the supplementary a |

### replication_statement (papers with this category: 7/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 7 | 88% | aer_112_2_1 p.1-39 Title footnote; References: The reference list cites a formal AEA and ICPSR replication-data deposit for the paper, and the title page lin; aer_113_3_7 p.1-1 Title page footnote: A starred footnote on the title page directs readers to the article's online page for additional materials and |
| `data_public` | 5 | 62% | aer_112_2_1 p.1-39 Title footnote; References: The reference list cites a formal AEA and ICPSR replication-data deposit for the paper, and the title page lin; qje_140_1_10 p.60-60 Data Availability statement: States a formal data availability statement citing a public Harvard Dataverse replication package with its own |
| `code_public` | 3 | 38% | restud_2026_restud_rdag027 p.44-44 Data Availability: A Data Availability statement cites a Zenodo replication package DOI providing code and publicly available dat; restud_89_1_6 p.3-32 footnote 3, footnote 44, Data Availability Statement: A Data Availability Statement gives a Zenodo DOI for data and replication package; a GitHub repository and a S |
| `online_appendix_not_available` | 2 | 25% | qje_140_1_4 p.69-69 Supplementary Material statement: The article repeatedly refers throughout the main text to an Online Appendix published separately at the journ; restud_2026_restud_rdag027 p.44-44 Supplementary Data: All appendices are referenced as Supplementary Material available online; none are included in the PDF, and no |
| `software_named` | 2 | 25% | qje_140_1_4 p.33-33 Section III.A.1: A commercial third-party software product is named and described for one specific analysis step, inferring an ; restud_89_1_6 p.3-32 footnote 3, footnote 44, Data Availability Statement: A Data Availability Statement gives a Zenodo DOI for data and replication package; a GitHub repository and a S |
| `data_restricted` | 1 | 12% | restud_2026_restud_rdag027 p.44-44 Data Availability: A Data Availability statement cites a Zenodo replication package DOI providing code and publicly available dat |
| `in_main_text` | 1 | 12% | restud_2026_restud_rdag027 p.44-44 Supplementary Data: All appendices are referenced as Supplementary Material available online; none are included in the PDF, and no |

### robustness_reported (papers with this category: 5/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_specification` | 5 | 62% | aer_112_2_1 p.30-31 Tables 8-9: Two robustness tables each add one alternative control, fixed effect, or comparison instrument at a time relat; qje_140_1_10 p.55-55 Section VII.A: Summarizes robustness of the industry- and local-level baseline estimates to alternative control sets and spec |
| `in_appendix` | 5 | 62% | aer_112_2_1 p.32-32 Section IV.C; online Appendix Figure D15: A first-differenced version of the main specification is reported as an alternative to the levels specificatio; qje_140_1_10 p.55-55 Section VII.A: Summarizes robustness of the industry- and local-level baseline estimates to alternative control sets and spec |
| `summarized_in_one_table` | 4 | 50% | aer_112_2_1 p.30-31 Tables 8-9: Two robustness tables each add one alternative control, fixed effect, or comparison instrument at a time relat; qje_140_1_10 p.55-55 Section VII.A: Summarizes robustness of the industry- and local-level baseline estimates to alternative control sets and spec |
| `leave_one_out` | 3 | 38% | aer_112_2_1 p.9-9 Figure 2 notes: A figure note reports the same estimation with a specific merged commuting zone dropped from the sample.; restud_2026_restud_rdag027 p.19-19 Section 4.3; Appendix Figure B.3: Sending and receiving states are dropped one at a time, summarised as an appendix figure, motivated by the neg |
| `alt_estimator` | 2 | 25% | aer_112_2_1 p.32-32 Section IV.C; online Appendix Figure D15: A first-differenced version of the main specification is reported as an alternative to the levels specificatio; restud_89_1_6 p.28-30 footnotes 46 and 48, Supplementary Appendix Tables C1, C3, C4, C5: Additional control sets, other outcomes, period-specific coefficients and over-identified SSIV variants are re |
| `in_main_text` | 2 | 25% | restud_89_1_6 p.28-30 Section 6.2.4, Table 4 columns 4-7: Sensitivity to controls is presented within the main table itself: one column drops the original regional cont; rfs_2026_rfs_hhaf080 p.38-42 Section 4.3.3, Table 8 Panel B, Internet Appendix Table I.1: IV robustness adds quarter fixed effects interacted with industry, region, rating or size (appendix table), an |
| `alt_control_group` | 1 | 12% | aer_112_2_1 p.30-31 Tables 8-9: Two robustness tables each add one alternative control, fixed effect, or comparison instrument at a time relat |
| `alt_fixed_effects` | 1 | 12% | rfs_2026_rfs_hhaf080 p.38-42 Section 4.3.3, Table 8 Panel B, Internet Appendix Table I.1: IV robustness adds quarter fixed effects interacted with industry, region, rating or size (appendix table), an |
| `alt_sample` | 1 | 12% | restud_2026_restud_rdag027 p.19-19 Section 4.3, Identification and robustness checks; Appendix B.3: Robustness is summarised in one short paragraph listing four families (alternative SEs, control sets, sorting  |
| `alt_se` | 1 | 12% | restud_2026_restud_rdag027 p.19-19 Section 4.3, Identification and robustness checks; Appendix B.3: Robustness is summarised in one short paragraph listing four families (alternative SEs, control sets, sorting  |
| `other:shift_share_diagnostics` | 1 | 12% | qje_140_1_10 p.55-55 Section VII.A: Points to a dedicated set of online appendix tables implementing recently proposed shift-share-specific robust |
| `summarized_in_figure` | 1 | 12% | restud_2026_restud_rdag027 p.19-19 Section 4.3; Appendix Figure B.3: Sending and receiving states are dropped one at a time, summarised as an appendix figure, motivated by the neg |

### sample_construction (papers with this category: 6/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 6 | 75% | aer_112_2_1 p.6-9 Section II: Data sources named include complete-count historical censuses, a historical statistical compendium of city and; aer_113_3_7 p.8-8 Section I.B, Data: The AP-text sample is built from a keyword search of a commercial newswire database restricted to Associated P |
| `sample_period_stated` | 5 | 62% | aer_112_2_1 p.8-8 Section II.B: The analysis sample is restricted to non-southern commuting zones for which Black population figures are avail; aer_113_3_7 p.8-8 Section I.B, Data: The AP-text sample is built from a keyword search of a commercial newswire database restricted to Associated P |
| `sample_size_reported_per_table` | 5 | 62% | aer_112_2_1 p.16-31 Tables 1-9: The observation count is reported as a labeled row in every regression table and stays essentially fixed acros; aer_113_3_7 p.15-25 Tables 2 and 4-7: Observation counts, outlet or county counts are reported at the bottom of every regression table and vary by c |
| `unit_of_observation_stated` | 5 | 62% | aer_112_2_1 p.8-21 Section II.B; table notes: The commuting zone is stated as the unit of observation in the main text and repeated in the notes of every re; aer_113_3_7 p.20-20 Section III.A, Aggregation to the County Level: For the county-level stage, counties are retained only when newspapers matched to the content database account |
| `exclusions_justified` | 4 | 50% | aer_112_2_1 p.8-8 Section II.B: The analysis sample is restricted to non-southern commuting zones for which Black population figures are avail; aer_113_3_7 p.20-20 Section III.A, Aggregation to the County Level: For the county-level stage, counties are retained only when newspapers matched to the content database account |
| `in_footnote` | 3 | 38% | restud_2026_restud_rdag027 p.25-25 Footnote 15: Slaveholders are linked from the 1860 Slave Schedule to the population census by name and county using the ABE; restud_89_1_6 p.26-26 footnote 45: Missing industry-level balance covariates for a handful of industries are imputed with SIC3 group medians, fal |
| `in_main_text` | 3 | 38% | restud_2026_restud_rdag027 p.11-12 Section 3; footnote 7: Individuals are tracked with complete-count censuses 1870 to 1900 and Census Tree linked records; the paper de; restud_89_1_6 p.21-22 Section 6.2.1: The application reuses the Autor, Dorn and Hanson (2013) replication data: a repeated cross section of commuti |
| `matching_or_linkage_described` | 3 | 38% | restud_2026_restud_rdag027 p.11-12 Section 3; footnote 7: Individuals are tracked with complete-count censuses 1870 to 1900 and Census Tree linked records; the paper de; restud_89_1_6 p.26-26 footnote 45: Missing industry-level balance covariates for a handful of industries are imputed with SIC3 group medians, fal |
| `attrition_reported` | 1 | 12% | aer_112_2_1 p.25-25 Section IV.B, footnote: A data-privacy suppression rule removes one commuting zone from the race-specific tables, and the authors sepa |
| `in_appendix` | 1 | 12% | rfs_2026_rfs_hhaf080 p.13-13 Section 2.1.8, Tables A.3 and A.4: Two Internet Appendix tables document, for every table and figure, the sample restrictions, frequency, time pe |
| `restricted_data_used` | 1 | 12% | rfs_2026_rfs_hhaf080 p.10-12 Section 2.1.1 to 2.1.6, Table A.1: Data sources are listed one by one in numbered subsections (scraped aggregator website, central bank FinTech r |

### specification_reporting (papers with this category: 6/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `fe_listed_in_table` | 5 | 62% | aer_112_2_1 p.30-31 Tables 8-9: The robustness tables list included fixed effects and control sets as indicator rows beneath the coefficients,; qje_140_1_10 p.24-36 Table III; Table VI: Main regression tables list included fixed effects as indicator rows and report the number of observations and |
| `n_reported` | 5 | 62% | aer_112_2_1 p.21-31 Tables 2-9: Each results table reports the observation count, either an R-squared or a first-stage F-statistic, and the de; qje_140_1_10 p.24-36 Table III; Table VI: Main regression tables list included fixed effects as indicator rows and report the number of observations and |
| `se_type_in_notes` | 5 | 62% | aer_112_2_1 p.21-21 Table 2 notes: Table notes state that standard errors are shown in parentheses but do not name a clustering level or a robust; aer_113_3_7 p.15-15 Table 2 notes: Table notes for the main results state the unit of observation, the estimator, the weighting scheme, and the c |
| `weights_stated` | 5 | 62% | aer_112_2_1 p.23-24 Table 3; footnote on precision weights: A subset of specifications is flagged with a labeled 'Precision wt' indicator row denoting that those regressi; aer_113_3_7 p.15-15 Table 2 notes: Table notes for the main results state the unit of observation, the estimator, the weighting scheme, and the c |
| `baseline_then_variants` | 4 | 50% | aer_112_2_1 p.30-31 Tables 8-9: The robustness tables list included fixed effects and control sets as indicator rows beneath the coefficients,; restud_2026_restud_rdag027 p.18-18 Table 2: The main table stacks OLS in panel (a) and SSIV in panel (b) for the same five outcomes, alternates columns wi |
| `cluster_level_in_notes` | 4 | 50% | aer_113_3_7 p.15-15 Table 2 notes: Table notes for the main results state the unit of observation, the estimator, the weighting scheme, and the c; qje_140_1_10 p.24-45 Table III notes; Table VIII notes: States the standard error type and the exact clustering level in the notes beneath every main results table ra |
| `mean_of_dependent_reported` | 3 | 38% | aer_112_2_1 p.21-31 Tables 2-9: Each results table reports the observation count, either an R-squared or a first-stage F-statistic, and the de; qje_140_1_10 p.43-53 Table VIII; Table X; Table XI: Reports the sample mean of the dependent variable at the bottom of the individual-level and municipal-institut |
| `r2_reported` | 3 | 38% | aer_112_2_1 p.21-31 Tables 2-9: Each results table reports the observation count, either an R-squared or a first-stage F-statistic, and the de; restud_2026_restud_rdag027 p.18-18 Table 2: The main table stacks OLS in panel (a) and SSIV in panel (b) for the same five outcomes, alternates columns wi |
| `controls_progressive_columns` | 2 | 25% | restud_2026_restud_rdag027 p.18-18 Table 2: The main table stacks OLS in panel (a) and SSIV in panel (b) for the same five outcomes, alternates columns wi; restud_89_1_6 p.28-29 Table 4 and notes: The main table starts by replicating the original ADH preferred column, then progressively swaps or adds shift |
| `in_main_text` | 1 | 12% | restud_89_1_6 p.28-29 Table 4 and notes: The main table starts by replicating the original ADH preferred column, then progressively swaps or adds shift |
| `other:no_stars_no_r2` | 1 | 12% | restud_89_1_6 p.27-29 Tables 3 and 4: Tables report coefficients with standard errors in parentheses, first-stage F statistics and observation count |
| `stars_used` | 1 | 12% | restud_2026_restud_rdag027 p.18-42 Notes to Tables 2 through 6, 9, 10: Every table note ends with the clustering statement (60 by 60 mile grid cells following Bester, Conley and Han |

### variable_construction (papers with this category: 7/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `instrument_construction` | 6 | 75% | aer_112_2_1 p.13-14 Section III, equations 2-3: The instrument is constructed by interacting fixed pre-period migrant location shares with a machine-learning-; aer_113_3_7 p.24-24 Section III.B: The excluded instrument for the individual-level 2SLS is the interaction of county-level AP intensity with the |
| `standardized_index` | 4 | 50% | aer_112_2_1 p.32-33 Section V, equation 11: Mechanism-stage outcomes are standardized onto a common scale so that effects on very different local-governme; aer_113_3_7 p.22-23 Section III.A, Views on Immigration Policy: Indices aggregating multiple survey questions on immigration or on placebo policies are built by standardizing |
| `treatment_definition` | 4 | 50% | aer_112_2_1 p.9-9 Section III, Functional Form: The treatment variable is defined as the percentile rank, rather than the raw magnitude, of a commuting zone's; qje_140_1_10 p.31-31 Section V.A.1, equation (5): Constructs the municipal-level exposure measure as a shift-share combining 1939 preexposure industry employmen |
| `in_main_text` | 3 | 38% | restud_2026_restud_rdag027 p.16-17 Section 4.2, equations (4.2) and (4.3): Predicted shifts are built by LASSO on origin-county push factors plus their squares and interactions, applied; restud_89_1_6 p.21-22 Section 6.2.1, footnote 39: Outcome, treatment and instrument are defined in notation that separates exposure shares (lagged local industr |
| `outcome_definition` | 3 | 38% | aer_112_2_1 p.18-22 Section IV.A: Two outcome families are defined: average adult income rank by childhood commuting zone from tax records, and ; restud_2026_restud_rdag027 p.14-15 Section 4.1; Figure 3 notes: Four binary county outcomes (memorials, UDC chapters, second KKK chapters, lynchings of Black people) are summ |
| `in_footnote` | 2 | 25% | restud_2026_restud_rdag027 p.17-17 Footnote 12: Confederate place names are matched conservatively using a restrictive set of distinguishing names to minimise; restud_89_1_6 p.21-22 Section 6.2.1, footnote 39: Outcome, treatment and instrument are defined in notation that separates exposure shares (lagged local industr |
| `measurement_error_discussed` | 2 | 25% | aer_112_2_1 p.21-21 Section IV.A, footnote: The authors note that the causal exposure-effect proxy used for one of the two outcome families is not availab; restud_2026_restud_rdag027 p.17-17 Footnote 12: Confederate place names are matched conservatively using a restrictive set of distinguishing names to minimise |
| `logs_or_ihs` | 1 | 12% | restud_2026_restud_rdag027 p.16-16 Section 4.2; Table 2 notes: Baseline controls are log 1870 population and log county area; all continuous controls enter quadratically, wi |
| `other:incomplete_shares_control` | 1 | 12% | restud_89_1_6 p.14-16 Section 4.2, Section 4.3, footnote 31: Because exposure shares do not sum to one, the paper controls for the sum of shares (lagged manufacturing shar |
| `other:skill_classification` | 1 | 12% | qje_140_1_10 p.25-25 Section IV.A.2, footnote 24: Splits industries and local exposure into high-skill and low-skill categories using a published measure of his |

### writing_structure (papers with this category: 8/8)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_heavy` | 6 | 75% | aer_112_2_1 p.6-36 throughout: The main text repeatedly defers construction details, additional outcomes, and further robustness results to a; qje_140_1_10 p.55-58 Section VII: Collects robustness checks, additional linkage analysis, heterogeneity, and further extensions into one later  |
| `results_previewed_in_intro` | 6 | 75% | aer_112_2_1 p.2-5 Introduction: The introduction previews the paper's main quantitative findings and mechanism results before the formal empir; aer_113_3_7 p.3-6 Introduction: The introduction previews the paper's three empirical parts in order (AP-text effects, diffusion to outlets, e |
| `contribution_paragraph` | 5 | 62% | aer_112_2_1 p.4-5 Introduction: Early introduction paragraphs explicitly position the paper's contribution relative to prior Great Migration a; qje_140_1_4 p.8-10 Section I.A: A dedicated related-literature subsection immediately follows the introduction and organizes prior work into s |
| `data_before_design` | 5 | 62% | aer_112_2_1 p.6-11 Section II precedes Section III: The data and descriptive-statistics section is placed before the empirical-strategy section, so descriptive co; aer_113_3_7 p.8-31 Sections I-III: Each of the three empirical parts follows the same internal ordering of data, then empirical strategy, then re |
| `roadmap_paragraph` | 5 | 62% | aer_112_2_1 p.2-5 Introduction: The introduction previews the paper's main quantitative findings and mechanism results before the formal empir; aer_113_3_7 p.3-6 Introduction: The introduction previews the paper's three empirical parts in order (AP-text effects, diffusion to outlets, e |
| `mechanisms_after_main` | 4 | 50% | aer_113_3_7 p.31-33 Section III.D-E: Magnitude interpretation and mechanism discussion are placed in their own labeled subsections at the end of th; aer_114_7_10 p.25-28 Section IV.D: The medical-innovation interaction analysis, framed by the paper as mechanism evidence, is placed after the co |
| `main_result_first` | 3 | 38% | restud_2026_restud_rdag027 p.6-43 Sections 2 to 7: Order is conceptual framework, historical background, descriptive selection and sorting, outcome measurement, ; restud_89_1_6 p.4-31 Sections 2-6: Theory (setting, framework, extensions, inference) precedes the empirical application; within the application  |
| `robustness_separate_section` | 2 | 25% | aer_113_3_7 p.31-33 Section III.D-E: Magnitude interpretation and mechanism discussion are placed in their own labeled subsections at the end of th; qje_140_1_10 p.55-58 Section VII: Collects robustness checks, additional linkage analysis, heterogeneity, and further extensions into one later  |
| `design_before_data` | 1 | 12% | restud_89_1_6 p.4-31 Sections 2-6: Theory (setting, framework, extensions, inference) precedes the empirical application; within the application  |
| `in_main_text` | 1 | 12% | restud_2026_restud_rdag027 p.7-33 Section 2.1; openings of Sections 5 and 6: A conceptual framework with two conditions and three channels is introduced first and each later section opens |
| `online_appendix_not_available` | 1 | 12% | aer_112_2_1 p.6-36 throughout: The main text repeatedly defers construction details, additional outcomes, and further robustness results to a |
| `other:framework_guides_empirical_sections` | 1 | 12% | restud_2026_restud_rdag027 p.7-33 Section 2.1; openings of Sections 5 and 6: A conceptual framework with two conditions and three channels is introduced first and each later section opens |
| `other:iv_as_secondary_design` | 1 | 12% | rfs_2026_rfs_hhaf080 p.5-37 Introduction and Section 4.3: The IV is introduced after the mechanism evidence and framed as building on it (firms exploit the unsecured na |
| `other:no_roadmap_paragraph` | 1 | 12% | rfs_2026_rfs_hhaf080 p.26-42 Sections 3.3, 4.1, 4.3.3: There is no roadmap paragraph and no separate robustness section; robustness is folded into the end of each re |
| `other:no_separate_robustness_section` | 1 | 12% | rfs_2026_rfs_hhaf080 p.26-42 Sections 3.3, 4.1, 4.3.3: There is no roadmap paragraph and no separate robustness section; robustness is folded into the end of each re |
| `other:practitioner_recommendations` | 1 | 12% | restud_89_1_6 p.5-31 footnote 4, Section 6.1 closing, Section 6.2.2, Section 7: The paper phrases parts of its guidance as explicit recommendations to practitioners (how to write the instrum |
| `other:robustness_embedded_in_results` | 1 | 12% | aer_112_2_1 p.30-31 Section IV.C: Alternative-explanation and robustness checks are placed as the closing subsection of the results section rath |
| `other:running_example` | 1 | 12% | restud_89_1_6 p.5-12 Sections 2-3: A running labour supply example with import tariffs as shocks is used throughout the theory sections to ground |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 11 | aer_113_3_7 s1.se.cluster_level (paper: Standard errors in the outlet-level diffusion regressions are clustere / card: s1/s2/s3/s4: se.type=cluster, se.cluster_level=['source_code'].); aer_113_3_7 s5.se.cluster_level (paper: Standard errors in the county/respondent-level CCES regressions (reduc / card: s5/s6: se.type=cluster, se.cluster_level=['fips'].) |
| cluster_level | unknown | 1 | aer_112_2_1 s1.se.cluster_level (paper: Table notes state only that standard errors are shown in parentheses,  / card: s1.se.type and s1.se.cluster_level are both null, and the card's readi) |
| cluster_level | paper_only | 1 | qje_140_1_4 specifications (paper: For the co-inventor spillover regression (Table III) the text separate / card: No specification extracted in the card corresponds to the co-inventor ) |
| cluster_level | code_only | 1 | qje_140_1_4 s3.se.cluster_level (paper: The main text does not state a cluster level for the shift-share IV re / card: The card records two-way clustering at the region and decade level for) |
| comparison_group | paper_only | 4 | aer_112_2_1 d1.comparison_group (paper: The text describes an alternative shift-share instrument built from a  / card: d1.comparison_group and s1.comparison_group are both null.); aer_114_7_10 s1.comparison_group (paper: Comparison group is counties without a Duke funding commitment (never/ / card: s1 comparison_group=null) |
| controls | paper_only | 5 | aer_112_2_1 s1.controls_summary (paper: Baseline controls are named explicitly: the recent-migrant population  / card: s1.controls_summary is null; only the unresolved macro name baseline_c); aer_113_3_7 s5.controls_summary (paper: Respondent-level CCES regressions control for age, age squared, gender / card: s5/s6: controls_summary=null; unresolved_symbols=['$indiv_controls'], ) |
| controls | agree | 3 | qje_140_1_4 s2.controls_summary (paper: The migrant event-study and interaction specifications are described a / card: The card's controls_summary field is unset (null) for the extracted sp); restud_2026_restud_rdag027 s2.controls; s4.controls (paper: Odd columns: county size controls plus 1870 Southern share; even colum / card: $demo_ctrls plus pct_Southerners_white1870 in s1/s3; $all_ctrls plus p) |
| data_source | paper_only | 6 | aer_112_2_1 data[0].source_hint (paper: Data sources are named explicitly: complete-count IPUMS censuses, a hi / card: data[0].source_hint is null; only a dataset filename and unit of obser); aer_113_3_7 data (paper: Data sources are named explicitly throughout: a newswire full-text dat / card: data=[] (the card's data-source list is empty).) |
| data_source | agree | 1 | rfs_2026_rfs_hhaf080 data[0] (paper: Credit registry, M-Contran survey, Banque de France FinTech data, scra / card: Three intermediate admin files with unknown access; one is a scraped I) |
| diagnostic | paper_only | 6 | aer_113_3_7 x1 (paper: A dynamic difference-in-differences specification with leads and lags  / card: diagnostics x1: kind=pretrend_test, status=unknown, spec_ids=['s7'], n); aer_113_3_7 x2 (paper: First-stage F-statistics are reported in every table with a 2SLS panel / card: diagnostics x2: kind=weak_iv, status=unknown, spec_ids=['s6'], no stat) |
| diagnostic | agree | 4 | aer_112_2_1 x1 (paper: A first-stage coefficient and F-statistic for the excluded instrument  / card: Diagnostic x1 records kind first_stage tied to specification s1, with ); aer_112_2_1 x2 (paper: Table 1 tests the instrument against pre-1940 school-attendance and ed / card: Diagnostic x2 records a pretrend_test on pre-1940 enrollment and educa) |
| estimator | agree | 10 | aer_112_2_1 s1.estimator (paper: The paper reports OLS, reduced-form, and two-stage-least-squares estim / card: Specifications s1-s3 all use the ivreg2 command with estimator field s); aer_113_3_7 s1.estimator (paper: Diffusion is estimated by a generalized difference-in-differences OLS  / card: s1: estimator=hdfe_ols, command=reghdfe, formula reghdfe num_IllimmImm) |
| estimator | code_only | 1 | qje_140_1_4 s3.formula_or_call (paper: The text names a shift-share instrumental-variables strategy based on  / card: The card's IV specification (s3) is a two-stage-least-squares regressi) |
| fixed_effects | agree | 10 | aer_113_3_7 s1.fixed_effects (paper: The baseline diffusion specification (equation 2) includes outlet and  / card: s1: fixed_effects=['year_month','source_code'].); aer_113_3_7 s2.fixed_effects (paper: A robustness column adds state-by-year-month fixed effects to absorb s / card: s2: fixed_effects=['year_month##state__','source_code','year_month'].) |
| fixed_effects | paper_only | 2 | aer_112_2_1 s1.fixed_effects (paper: The text states that baseline controls include census region fixed eff / card: s1.fixed_effects is null; the code trace could not resolve the baselin); restud_89_1_6 s2.fixed_effects (paper: Period FE and Census division FE in the ADH replication column; period / card: fe=None on all specs; ivreghdfe present in packages) |
| fixed_effects | disagree | 1 | qje_140_1_4 s1.fixed_effects (paper: The main text describes the leads-and-lags event-study specification ( / card: The card's leads-and-lags specification (s1) additionally absorbs a te) |
| other | paper_only | 1 | aer_114_7_10 d1.variant (paper: Design is named specifically as a staggered-adoption difference-in-dif / card: d1 method=did, variant=null) |
| other | unknown | 1 | restud_2026_restud_rdag027 s3.instrument (paper: Instrument is a LASSO-predicted push-factor shift-share scaled by 1870 / card: Instrument variable iv_mig_hat1_00 used in s3/s4; construction not tra) |
| other | agree | 1 | restud_89_1_6 d1.outcomes (paper: Other outcomes (unemployment, non-participation, wages) reported in Su / card: d1 outcomes y d_sh_unempl d_sh_nilf d_avg_lnwkwage) |
| outputs | paper_only | 7 | aer_113_3_7 outputs (paper: The paper presents seven main numbered tables and seven main numbered  / card: outputs.tables=[] and outputs.figures=[] (both empty).); aer_114_7_10 outputs.tables (paper: Six numbered main tables and five numbered main figures reported in th / card: outputs.tables=[] and outputs.figures=[] in the card) |
| outputs | disagree | 1 | aer_112_2_1 outputs.tables (paper: The main text alone contains nine numbered tables and nine numbered fi / card: outputs.tables lists two table records and outputs.figures lists one b) |
| robustness | paper_only | 5 | aer_112_2_1 robustness (paper: Two dedicated tables plus additional appendix analyses report alternat / card: The card's robustness array is empty.); aer_114_7_10 robustness (paper: Extensive robustness section covering alternative estimators, alternat / card: robustness array is empty in the card) |
| robustness | agree | 1 | restud_89_1_6 s4 (paper: Null-imposed confidence intervals and Adao et al. SEs in Table C2; ove / card: robustness [] but s4 ssiv_null_imposed with cluster sic3 present) |
| sample | paper_only | 5 | aer_112_2_1 s1.sample (paper: The text describes a fixed analysis sample of non-southern commuting z / card: s1.sample and the design-level sample fields are null in the card.); qje_140_1_4 s2.sample (paper: The migrant event-study sample is built by one-to-one exact matching o / card: The card leaves the sample field unset (null) for both event-study spe) |
| sample | agree | 2 | aer_113_3_7 s4.sample (paper: The right-hand panel of the main diffusion table restricts the sample  / card: s4: sample='Subset of outlets meeting sample criteria (NPsample==1)'.); aer_114_7_10 pipeline.sample_restrictions[0] (paper: Main analysis restricted to North Carolina counties and birth years 19 / card: pipeline sample_restrictions: statefip==37 (North Carolina) births, 19) |
| se_type | agree | 2 | restud_2026_restud_rdag027 s3.se.type (paper: Cluster-robust; robustness to Conley and Adao et al. SEs in appendix. / card: se=cluster for all four specs; no alternative SE spec recorded.); restud_89_1_6 s1.se (paper: Conventional state-clustered SEs reported as an alternative in Supplem / card: s1 ivreg2 at observation level with cluster clus) |
| se_type | unknown | 1 | aer_114_7_10 s2.se.type (paper: Text does not separately describe the standard-error method used speci / card: s2 se.type=null, se.cluster_level=null (unresolved in code trace)) |
| weights | agree | 6 | aer_112_2_1 s2.weights (paper: One family of specifications, the childhood exposure-effect regression / card: s2.weights records an analytic weight expression based on the inverse ); aer_113_3_7 s1.weights (paper: Diffusion regressions are weighted by the number of articles using the / card: s1: weights='num_imm' (pweight).) |
| weights | paper_only | 1 | aer_114_7_10 s1.weights (paper: Preferred specifications weight observations by county-by-year (or wav / card: s1 weights=null; s2 formula references an unresolved iw=weightvar) |
| weights | code_only | 1 | rfs_2026_rfs_hhaf080 s1.weights (paper: No regression weights are mentioned; matching is five nearest neighbou / card: pweight=weight in both s1 and s2.) |

## Gaps the readers reported

- (1) No stated clustering level or explicit SE-type (robust versus clustered) description in any main-table note; only 'stand
- (1) No preregistration, IRB approval, or human-subjects consent statement anywhere in the text (the study uses historical ad
- (1) No explicit statement of the statistical software or package versions used for estimation anywhere in the main text.
- (1) No single consolidated summary-statistics table; sample means and standard deviations are distributed across the individ
- (1) No explicit few-clusters correction or wild-bootstrap discussion is given despite treatment varying at a commuting-zone 
- (1) No formal covariate balance table comparing outlet or county characteristics across levels of AP intensity appears in th
- (1) No explicit adjustment for multiple hypothesis testing is discussed despite estimating effects for five separate immigra
- (1) No preregistration, IRB approval, or data-collection consent statement is present anywhere in the read text.
- (1) No explicit statement of statistical software version or package citations (e.g., for reghdfe or ivreghdfe) appears in t
- (1) The online appendix is referenced extensively throughout (text-analysis validation, additional figures and tables, robus
- (1) No preregistration, pre-analysis plan, or IRB/ethics statement found anywhere in the main text.
- (1) No explicit multiple-testing adjustment stated despite reporting many outcome subgroups (race splits) and robustness var
- (1) No dedicated summary-statistics table appears in the main text itself; it is referenced as being in the online appendix 
- (1) No explicit statement of statistical software beyond what can be inferred from the recipe card's Stata commands (reghdfe
- (1) No formal density or manipulation test is reported, consistent with the design not relying on a running-variable cutoff.
- (1) No preregistration, IRB approval, or participant-consent statement of any kind appears in the read text (category prereg
- (1) No explicit statement of analysis software or version (for example Stata and its version) appears in the main text; soft
- (1) No R-squared is reported in any of the main regression tables read (Table III, IV, VI-XI); tables report N and, for some
- (1) No explicit discussion of cluster-count adequacy, wild-bootstrap correction, or other few-cluster inference concerns app
- (1) No explicit multiple-hypothesis-testing correction is discussed in the main text across the many outcome families examin
- (1) The paper's Online Appendix (identification checks, most robustness tables, heterogeneity detail, and shift-share-specif
- (1) No explicit multiple-testing adjustment is discussed anywhere in the empirical section despite every main table reportin
- (1) No preregistration, pre-analysis plan, or IRB/consent statement is present; the paper uses secondary administrative pate
- (1) No first-stage or weak-instrument statistic for the shift-share IV strategy appears in the extracted main text; the reci
- (1) The formal balance table for the migrant/placebo matching procedure is not in the main text; the paper points to the onl
- (1) No explicit discussion of attrition in the underlying patent samples beyond the general undercount caveat for the addres
- (1) No explicit justification for the grid-cell cluster size beyond citing Bester, Conley and Hansen.
- (1) No multiple-testing adjustment across the five outcomes or the many heterogeneity moderators.
- (1) No software or package named in the main text.
- (1) No balance table for the instrument; instrument validity is supported by the random-shifts placebo and control-set check

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
