# Reported practice: `rdd` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 11 paper notes (11 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | ReStud: 5, AER: 3, JPE: 1, QJE: 1, RFS: 1 |
| year | 2020: 1, 2022: 1, 2023: 1, 2024: 2, 2025: 2, 2026: 4 |
| papers with at least one observation in category | diagnostic_reported: 11, presentation_convention: 10, design_statement: 9, sample_construction: 9, variable_construction: 9, robustness_reported: 9, writing_structure: 9, replication_statement: 9, data_access: 9, specification_reporting: 8, inference_justification: 8, magnitude_interpretation: 8, external_validity: 8, mechanism_evidence: 7, limitation_stated: 7, heterogeneity_reported: 5, preregistration_or_ethics: 2, other: 2 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_110_2_5 | AER | 2020 | full | yes | 0d03fc7d8b3d |
| aer_112_10_8 | AER | 2022 | full | yes | df1a1baa7d3d |
| aer_114_11_1 | AER | 2024 | full | yes | 29289e1c44a7 |
| jpe_2026_740226 | JPE | 2026 | full | yes | 3af7c18d2956 |
| qje_2026_qje_qjaf045 | QJE | 2026 | full | yes | e108b4cedf90 |
| restud_2025_restud_rdae108 | ReStud | 2025 | full | yes | 7ef8bf174fab |
| restud_2025_restud_rdaf004 | ReStud | 2025 | full | yes | adc4b78e8b08 |
| restud_2026_restud_rdag037 | ReStud | 2026 | full | yes | 23b104741be7 |
| restud_2026_restud_rdag071 | ReStud | 2026 | full | yes | 99224bf0681d |
| restud_90_1_3 | ReStud | 2023 | full | yes | 20cf9df5f6ac |
| rfs_2024_rfs_hhae045 | RFS | 2024 | full | yes | 5e68c13b1e2d |

Excluded (paper-level hold-out `harness_build/evals/holdout/rdd.json`, not used for this method's skill evidence): aer_107_1_5, ecta_92_3_6, jpe_132_9_2, qje_140_1_11. Their notes still count in `_all`.

## Practices by category and tag


### data_access (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 7 | 64% | aer_114_11_1 p.9-10 Section II: Most outcome and covariate data derive from government administrative sources such as the Census of India, SEC; jpe_2026_740226 p.10-10 Section III, Data: Characterizes all six underlying data sources as government administrative records rather than survey-collecte |
| `data_restricted` | 6 | 55% | aer_110_2_5 p.8-8 Section I.C: One of the contemporary rental-price data sources is explicitly described as available only to verified real e; jpe_2026_740226 p.10-10 Section III, Data: Characterizes all six underlying data sources as government administrative records rather than survey-collecte |
| `linked_records` | 5 | 46% | restud_2025_restud_rdae108 p.6-7 Sections 2.1-2.2; Data Appendices A-I: All inputs are public databases, archives, books and online sources linked by the authors into a new election ; restud_2025_restud_rdaf004 p.10-33 Section 4; References: Data are administrative registers (employment, UI payments, welfare registry, health notifications) plus court |
| `public_use` | 4 | 36% | aer_114_11_1 p.9-10 Section II: Most outcome and covariate data derive from government administrative sources such as the Census of India, SEC; qje_2026_qje_qjaf045 p.14-16 Section III.A.3: Political and demographic covariates are drawn from aggregate historical census publications and linked geneal |
| `commercial` | 3 | 27% | qje_2026_qje_qjaf045 p.37-38 Section IV.B.2: The secondary newspaper analysis is built from a commercial, subscription-based newspaper archive service, wit; restud_2025_restud_rdaf004 p.10-33 Section 4; References: Data are administrative registers (employment, UI payments, welfare registry, health notifications) plus court |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.6-7 Sections 2.1-2.2; Data Appendices A-I: All inputs are public databases, archives, books and online sources linked by the authors into a new election  |

### design_statement (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 9 | 82% | aer_110_2_5 p.10-10 Section II.A: Identification rests on a spatial RD at the Voronoi-defined boundary of the well believed to have transmitted ; aer_114_11_1 p.13-13 Section III, bundled-treatment discussion: Authors choose to estimate the sharp discontinuity rather than a fuzzy RD instrumenting for one component of t |
| `threats_discussed` | 9 | 82% | aer_110_2_5 p.11-12 Section II.A: The authors flag that pump catchment membership is not a strict assignment rule because nearby wells are non-e; aer_114_11_1 p.13-14 Section III, identifying assumptions paragraph: Two identifying assumptions are stated explicitly: no manipulation of the running variable around the cutoff,  |
| `continuity_at_cutoff_argued` | 8 | 73% | aer_110_2_5 p.10-10 Section II.A: Identification rests on a spatial RD at the Voronoi-defined boundary of the well believed to have transmitted ; aer_114_11_1 p.13-14 Section III, identifying assumptions paragraph: Two identifying assumptions are stated explicitly: no manipulation of the running variable around the cutoff,  |
| `estimand_named` | 8 | 73% | aer_110_2_5 p.10-10 Section II.A: Identification rests on a spatial RD at the Voronoi-defined boundary of the well believed to have transmitted ; aer_114_11_1 p.11-11 Section III, equation (1): The estimand is the sharp RD coefficient on crossing the village population cutoff (one thousand residents) in |
| `identifying_assumption_explicit` | 8 | 73% | aer_110_2_5 p.27-28 Section III.G Possible Interpretations: A dedicated subsection separately argues against disease stigma and updated beliefs about water-source quality; aer_114_11_1 p.11-11 Section III, equation (1): The estimand is the sharp RD coefficient on crossing the village population cutoff (one thousand residents) in |
| `in_main_text` | 3 | 27% | restud_2025_restud_rdae108 p.10-11 Section 3.4.1, equation (1): The design is named as a close-elections regression discontinuity across countries with one observation per el; restud_2026_restud_rdag071 p.16-16 Section 4.1, equation (2): The reoffending analysis is framed as a sharp regression discontinuity design; the coefficient on the cutoff i |
| `in_appendix` | 2 | 18% | restud_2025_restud_rdae108 p.13-14 Section 3.5; Appendix A.2: For executive turnovers a fuzzy RD is used: the executive turnover indicator is instrumented by the sign of a ; rfs_2024_rfs_hhae045 p.23-24 Section 4.1, Figure 3, Table IA-6: Before validating the cutoff, the authors ask whether the same threshold matters to other constituents (the se |
| `instrument_exclusion_argued` | 2 | 18% | restud_2025_restud_rdae108 p.13-14 Section 3.5; Appendix A.2: For executive turnovers a fuzzy RD is used: the executive turnover indicator is instrumented by the sign of a ; restud_2026_restud_rdag071 p.23-24 Section 4.3.4, equation (3): Crossing the cutoff is later used as an instrument for the euro fine amount; three IV assumptions (relevance,  |
| `compliers_described` | 1 | 9% | aer_110_2_5 p.18-18 Section III, discussion following Table 3: The boundary-crossing indicator is presented as an intent-to-treat measure, with a separate fuzzy RD specifica |
| `in_footnote` | 1 | 9% | rfs_2024_rfs_hhae045 p.9-9 Footnotes 7 and 8: The authors report verifying their interpretation of the advisor's policy directly with the institution and ci |
| `other:hypotheses_formalized` | 1 | 9% | rfs_2024_rfs_hhae045 p.9-13 Sections 1.3, 1.4: Hypotheses are numbered (H1 to H4b) and derived from institutional theory before any data are shown; one hypot |
| `other:policy_verified_with_institution` | 1 | 9% | rfs_2024_rfs_hhae045 p.9-9 Footnotes 7 and 8: The authors report verifying their interpretation of the advisor's policy directly with the institution and ci |
| `randomization_described` | 1 | 9% | restud_90_1_3 p.9-9 Section 3.1, footnotes 11 and 12: The authors argue the tentative rule-based assignment cannot be gamed because cutoffs depend on the whole coho |

### diagnostic_reported (papers with this category: 11/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 10 | 91% | aer_110_2_5 p.16-16 Section III.A, referencing Appendix Figure B2: A manipulation test on the running variable's density, using the number of properties across the boundary, is ; aer_112_10_8 p.23-24 Section III.E footnote; online Appendix I.6: A companion regression kink design implementation of the listing-premium hockey stick is described as carried  |
| `balance_table` | 9 | 82% | aer_110_2_5 p.13-13 Table 1: A dedicated balance table reports RD coefficients for a wide set of pre-treatment property, sewer-access, and ; aer_114_11_1 p.13-13 Table 1: Table 1 tests six pre-delimitation covariates, including school presence, paved road, electrification, schedul |
| `density_test` | 9 | 82% | aer_110_2_5 p.16-16 Section III.A, referencing Appendix Figure B2: A manipulation test on the running variable's density, using the number of properties across the boundary, is ; aer_114_11_1 p.14-14 Section III: A manipulation/density test (Cattaneo, Jansson, and Ma 2018) is reported in the main text for the two census p |
| `in_main_text` | 9 | 82% | aer_110_2_5 p.13-13 Table 1: A dedicated balance table reports RD coefficients for a wide set of pre-treatment property, sewer-access, and ; aer_114_11_1 p.14-14 Section III: A manipulation/density test (Cattaneo, Jansson, and Ma 2018) is reported in the main text for the two census p |
| `bandwidth_sensitivity` | 7 | 64% | aer_110_2_5 p.16-16 Section III.A, footnote 30: A footnote asserts that results are robust to bandwidth choice throughout and points readers to an online appe; aer_114_11_1 p.29-29 Section IV.E, Robustness to Other RD Specifications: Robustness to a CER-optimal bandwidth, fixed bandwidths of 100 and 200, a quadratic polynomial, and a uniform  |
| `placebo_outcomes` | 7 | 64% | aer_110_2_5 p.13-17 Table 1; Table 3 panel A: Pre-epidemic rental prices and pre-epidemic cholera-exposure proxies are shown to be smooth across the boundar; aer_114_11_1 p.28-29 Figure 4, Section IV.E Placebo Checks: Figure 4 summarizes sixteen placebo estimates from four placebo strategies (other states, noncompliant UP dist |
| `placebo_cutoffs` | 6 | 55% | aer_110_2_5 p.26-27 Section III.F; Figure 5; Appendix Table B3: Four alternative catchment boundaries for other, unaffected wells are used as placebo treatment boundaries in ; aer_114_11_1 p.28-29 Figure 4, Section IV.E Placebo Checks: Figure 4 summarizes sixteen placebo estimates from four placebo strategies (other states, noncompliant UP dist |
| `first_stage_table` | 5 | 46% | aer_114_11_1 p.12-13 Table 1, Figure 1: Table 1 column 1 and Figure 1 report the first-stage effect of crossing the village population cutoff on the r; jpe_2026_740226 p.21-23 Table 3: Presents first-stage take-up results as a dedicated row in the instrumental-variable table alongside the reduc |
| `in_footnote` | 3 | 27% | aer_112_10_8 p.23-24 Section III.E footnote: A footnote checks that property and household observables, including renovation expenditures, are balanced and; restud_2025_restud_rdae108 p.15-16 Section 4.1; Figure 3; Appendix Figure C.2; Tables D.7, D.8; footnote 14: The Cattaneo et al. (2018) density test is the first identification check: a main-text figure for the full sam |
| `online_appendix_not_available` | 3 | 27% | aer_110_2_5 p.16-16 Section III.A, footnote 30: A footnote asserts that results are robust to bandwidth choice throughout and points readers to an online appe; aer_112_10_8 p.23-24 Section III.E footnote: A footnote checks that property and household observables, including renovation expenditures, are balanced and |
| `attrition_analysis` | 1 | 9% | aer_114_11_1 p.11-11 Section II, Combining Data Sources: Match rates between administrative datasets and the census backbone are reported and tested for discontinuity  |
| `leave_one_out` | 1 | 9% | qje_2026_qje_qjaf045 p.26-26 Section III.C.3: A leave-one-out exercise, described in the main text with results plotted in the appendix, drops sample observ |
| `other:imbalance_discussed` | 1 | 9% | rfs_2024_rfs_hhae045 p.28-29 Section 4.1 end, Figure IA-1: The few marginally imbalanced covariates are discussed individually: one is argued irrelevant because it does  |
| `other:permutation_test_covariate_continuity` | 1 | 9% | restud_2025_restud_rdae108 p.16-16 Section 4.1; Appendix Table C.8: Joint continuity of a large set of pre-election covariates at the cutoff is tested with the Canay and Kamat (2 |
| `other:rd_validation_of_value_added` | 1 | 9% | restud_90_1_3 p.16-16 Section 3.6.1, footnote 23, Supplementary Appendix F: The value-added estimates are validated by comparing the jump in actual outcomes at each cutoff with the jump  |
| `other:regression_kink_design` | 1 | 9% | aer_112_10_8 p.23-24 Section III.E footnote; online Appendix I.6: A companion regression kink design implementation of the listing-premium hockey stick is described as carried  |
| `other:rkd_style_balance_check` | 1 | 9% | aer_112_10_8 p.23-24 Section III.E footnote: A footnote checks that property and household observables, including renovation expenditures, are balanced and |
| `other:spatial_placebo_distribution` | 1 | 9% | aer_110_2_5 p.25-26 Section III.F, Falsification Tests; Figure 4: A separate falsification exercise compares the observed price gap against the distribution of price difference |
| `pre_trends_plot` | 1 | 9% | restud_2025_restud_rdae108 p.20-21 Section 4.2.2, equation (2); Figure 6: A dynamic RD estimates the effect separately for each post-election year and for a pre-election year; the pre- |
| `rd_plot` | 1 | 9% | restud_2025_restud_rdae108 p.12-22 Figure 2; Table 3 panel c: The first stage for the fuzzy design is shown both as binned RD plots of executive turnover probability agains |

### external_validity (papers with this category: 8/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `site_specific` | 7 | 64% | aer_110_2_5 p.3-3 Introduction: The authors present the single-parish, single-jurisdiction setting as a deliberate design choice that increase; aer_114_11_1 p.38-38 Section VI, Conclusion: Authors state findings are most directly applicable to north Indian local government design but argue the poli |
| `compliers_vs_population` | 5 | 46% | aer_114_11_1 p.3-3 Introduction: The main RD estimates are explicitly characterized as a local average treatment effect of moving into a GP of ; qje_2026_qje_qjaf045 p.32-33 Section IV.A.1: The authors distinguish their close-election local average treatment effect from the broader population of cou |
| `scaling_discussed` | 3 | 27% | aer_114_11_1 p.38-38 Section VI, Conclusion: Authors state findings are most directly applicable to north Indian local government design but argue the poli; jpe_2026_740226 p.43-44 Section VII, Conclusions: Discusses generalizability by contrasting the program's mandatory, near-universal exit exam and existing means |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.26-27 Sections 4.4.1-4.4.3; Appendix Tables E.4, E.5; Figures E.5, E.6: Locality of the RD estimate is addressed with three exercises: OLS in wider windows, a subsample of elections  |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.26-27 Sections 4.4.1-4.4.3; Appendix Tables E.4, E.5; Figures E.5, E.6: Locality of the RD estimate is addressed with three exercises: OLS in wider windows, a subsample of elections  |
| `other:contemporary_analogy_drawn` | 1 | 9% | aer_110_2_5 p.4-4 Introduction: The introduction draws an explicit analogy between the historical mechanism and modern disease-driven displace |
| `other:extrapolation_away_from_cutoff` | 1 | 9% | restud_2025_restud_rdae108 p.26-27 Sections 4.4.1-4.4.3; Appendix Tables E.4, E.5; Figures E.5, E.6: Locality of the RD estimate is addressed with three exercises: OLS in wider windows, a subsample of elections  |
| `time_period_specific` | 1 | 9% | qje_2026_qje_qjaf045 p.6-54 Section I; Section VI: The paper frames its finding as specific to the pre-Jim-Crow U.S. South and treats contemporary parallels with |

### heterogeneity_reported (papers with this category: 5/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `split_sample` | 5 | 46% | aer_114_11_1 p.35-35 Table 6: Table 6 splits the sample four ways (largest pre-delimitation village, pradhan's home village, direction of ca; jpe_2026_740226 p.30-30 Section IV.F: Summarizes subgroup analysis by baseline school disadvantage, sex, and parental education entirely in a brief  |
| `exploratory_labelled` | 3 | 27% | aer_114_11_1 p.27-27 Section IV.D: Authors explicitly flag that subsample-by-population-bin heterogeneity results are underpowered and that appar; jpe_2026_740226 p.30-30 Section IV.F: Does not label the baseline-characteristic subgroup comparisons as prespecified or exploratory, presenting the |
| `interaction` | 3 | 27% | aer_114_11_1 p.26-26 Table 4: Table 4 estimates heterogeneity continuously by interacting the RD treatment indicator with rescaled prior GP ; jpe_2026_740226 p.30-30 Section IV.F: Summarizes subgroup analysis by baseline school disadvantage, sex, and parental education entirely in a brief  |
| `mechanism_motivated` | 3 | 27% | qje_2026_qje_qjaf045 p.47-49 Table VII: A further heterogeneity table interacts the treatment with indicators for an all-Democrat or all-white local e; restud_2025_restud_rdae108 p.18-20 Section 4.2.1; Table 2; Figure 5; Appendix Tables E.1, E.3: Heterogeneity uses split samples at the median of the moderator computed among close elections, estimating the |
| `in_appendix` | 2 | 18% | jpe_2026_740226 p.30-30 Section IV.F: Summarizes subgroup analysis by baseline school disadvantage, sex, and parental education entirely in a brief ; restud_2025_restud_rdae108 p.18-20 Section 4.2.1; Table 2; Figure 5; Appendix Tables E.1, E.3: Heterogeneity uses split samples at the median of the moderator computed among close elections, estimating the |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.18-20 Section 4.2.1; Table 2; Figure 5; Appendix Tables E.1, E.3: Heterogeneity uses split samples at the median of the moderator computed among close elections, estimating the |
| `other:differences_reported_as_non_significant` | 1 | 9% | restud_2025_restud_rdae108 p.18-20 Section 4.2.1: Each heterogeneity split is preceded by a short statement of competing predictions, and the text comments on w |
| `prespecified` | 1 | 9% | qje_2026_qje_qjaf045 p.24-33 Table II, Panel B; Table IV: The paper splits the sample by whether a county was Democrat-won or electorally uncompetitive in the prior ele |

### inference_justification (papers with this category: 8/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `multiple_testing_adjustment` | 4 | 36% | aer_114_11_1 p.31-31 footnote 36: For the election-outcome table, the Romano-Wolf correction is applied to control the family-wise error rate ac; qje_2026_qje_qjaf045 p.22-50 Sections III.C and IV: Despite reporting many specifications, subsamples and heterogeneity splits across several tables, the text doe |
| `no_justification_found` | 4 | 36% | jpe_2026_740226 p.17-17 Table 1 note: Does not state an explicit clustering level or discuss why observations might be correlated within groups; sta; qje_2026_qje_qjaf045 p.22-50 Sections III.C and IV: Despite reporting many specifications, subsamples and heterogeneity splits across several tables, the text doe |
| `cluster_at_unit_level` | 3 | 27% | qje_2026_qje_qjaf045 p.19-19 Section III.B.1: Clustering standard errors at the county level is justified as accounting for local serial correlation in unob; restud_2025_restud_rdaf004 p.17-26 Table 2 notes; Table 3 notes: DiD standard errors are clustered at the firm level and RD standard errors at the individual level, stated onl |
| `randomization_inference` | 2 | 18% | restud_2025_restud_rdae108 p.2-24 Introduction; Section 4.3.3; Appendix F: Randomization inference following Cattaneo et al. (2015) is reported as a robustness alternative to the conven; restud_2025_restud_rdaf004 p.25-27 Section 6.1; Section 6.3, Supplementary Figure D3: For the RD, permutation tests compare the estimate at the true cutoff with a distribution of estimates at plac |
| `cluster_at_assignment_level` | 1 | 9% | aer_114_11_1 p.11-11 Section III, footnote 11: Standard errors are clustered at the gram panchayat level throughout, which the authors align with the level a |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.10-11 Section 3.4.1, footnote 11; Appendix Table D.6: Inference uses the robust bias-corrected standard errors and confidence intervals of Calonico et al. (2014) as |
| `in_footnote` | 1 | 9% | restud_2025_restud_rdae108 p.10-11 Section 3.4.1, footnote 11; Appendix Table D.6: Inference uses the robust bias-corrected standard errors and confidence intervals of Calonico et al. (2014) as |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.4-10 Introduction; Section 3.3.1: Multiple testing is addressed by aggregation rather than p-value correction: outcomes are grouped into summary |
| `other:block_bootstrap` | 1 | 9% | aer_114_11_1 p.28-29 Figure 4 notes: Confidence intervals for the average of main versus placebo RD coefficients in Figure 4 are built by block boo |
| `other:block_level_clustering` | 1 | 9% | aer_110_2_5 p.13-14 Table 1 notes; Section II.B footnote: Standard errors are clustered at the street-block level in essentially every table, on the premise that unobse |
| `other:cluster_level_robustness_check` | 1 | 9% | qje_2026_qje_qjaf045 p.25-25 Table III, Panel A: Robustness of inference to the choice of cluster level is shown, not as the primary justification, by re-clust |
| `other:coefficient_equality_test_across_subsamples` | 1 | 9% | restud_2025_restud_rdae108 p.20-20 Table 2 notes: Differences between subsample estimates are tested with the Clogg et al. (1995) method, with p-values reported |
| `other:conservative_se_choice` | 1 | 9% | aer_110_2_5 p.14-14 Section II.B, footnote 23: The authors compute an alternative spatial-HAC standard error for the baseline balance table and report choosi |
| `other:honest_ci` | 1 | 9% | restud_2026_restud_rdag071 p.25-27 Section 4.5; Table 3 column (5): Honest confidence intervals in the sense of Armstrong and Kolesar are reported in an appendix figure to accoun |
| `other:rdrobust_robust_se_default` | 1 | 9% | restud_2025_restud_rdae108 p.10-11 Section 3.4.1, footnote 11; Appendix Table D.6: Inference uses the robust bias-corrected standard errors and confidence intervals of Calonico et al. (2014) as |
| `other:robust_bias_corrected_rd` | 1 | 9% | rfs_2024_rfs_hhae045 p.30-33 Section 4.2, Table 6 notes: RD inference uses robust bias-corrected estimates and confidence intervals from the rdrobust framework, descri |
| `spatial_hac` | 1 | 9% | aer_110_2_5 p.14-14 Section II.B, footnote 23: The authors compute an alternative spatial-HAC standard error for the baseline balance table and report choosi |

### limitation_stated (papers with this category: 7/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `interpretation_caveat` | 6 | 55% | aer_114_11_1 p.37-37 Section V.B: Mechanism evidence in Section V is repeatedly described as more suggestive than definitive, since a village's ; jpe_2026_740226 p.21-21 Section IV.D: Notes that endogenous selection into taking the later college graduation exam could bias the skill-development |
| `identification_caveat` | 5 | 46% | aer_110_2_5 p.27-27 Section III.G, Stigma of Disease: The authors state they cannot fully rule out a role for disease stigma in the estimated price effect, treating; aer_114_11_1 p.13-13 Section III: Authors acknowledge that crossing the threshold bundles multiple simultaneous changes in population, geographi |
| `measurement` | 5 | 46% | aer_110_2_5 p.19-19 Section III.C, footnote 32: The authors flag that their migration measure only captures whether the primary occupant's recorded surname ch; aer_114_11_1 p.19-19 Section IV.A: Authors note they cannot separate whether infrastructure improvements reflect greater leader lobbying effort o |
| `data_coverage` | 4 | 36% | aer_110_2_5 p.23-23 Section III.E: An unexplained gap in digitized records for part of the parish in the latest historical wave is acknowledged a; qje_2026_qje_qjaf045 p.14-14 Section III.A.1, footnote: The authors note that the underlying historical lynching record is incomplete and discuss possible selective-r |
| `power` | 3 | 27% | aer_114_11_1 p.27-27 Section IV.D: Authors state that statistical power, particularly for the individually targeted programs outcome, limits how ; restud_2025_restud_rdae108 p.27-30 Section 4.5; footnote 30: Small-sample and power caveats are stated for ideology regressions and for the subsample with differentially b |
| `external_validity` | 1 | 9% | qje_2026_qje_qjaf045 p.35-36 Section IV.A.3: The paper is explicit that its RD estimate is a local average treatment effect concentrated among counties wit |
| `in_footnote` | 1 | 9% | restud_2025_restud_rdae108 p.27-30 Section 4.5; footnote 30: Small-sample and power caveats are stated for ideology regressions and for the subsample with differentially b |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.7-8 Section 2.2: A dedicated paragraph acknowledges imperfect coverage across countries and years, heterogeneous measurement qu |
| `selection` | 1 | 9% | jpe_2026_740226 p.29-29 Section IV.E: Acknowledges that recording informal-sector work as zero earnings could bias the formal-earnings effect if con |

### magnitude_interpretation (papers with this category: 8/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 5 | 46% | aer_114_11_1 p.31-31 Section V.A: The magnitude of the gram-sabha-attendance increase is interpreted with reference to Das (2015), who links a s; jpe_2026_740226 p.4-4 Introduction: Interprets the earnings effect relative to the control-group mean and separately benchmarks it against effect  |
| `relative_to_mean` | 5 | 46% | aer_114_11_1 p.20-20 Section IV.B: Component-outcome coefficients are routinely translated into a percent-of-mean change alongside the raw coeffi; jpe_2026_740226 p.4-4 Introduction: Interprets the earnings effect relative to the control-group mean and separately benchmarks it against effect  |
| `back_of_envelope` | 4 | 36% | aer_110_2_5 p.39-39 Appendix A: The empirical rental-price gap is translated into an implied disutility/discount parameter in the theoretical ; aer_114_11_1 p.38-38 Section VI, Conclusion: The conclusion reports a back-of-envelope cost-benefit figure, a direct annual cost per resident of creating a |
| `cost_benefit` | 3 | 27% | aer_110_2_5 p.39-39 Appendix A: The empirical rental-price gap is translated into an implied disutility/discount parameter in the theoretical ; aer_114_11_1 p.38-38 Section VI, Conclusion: The conclusion reports a back-of-envelope cost-benefit figure, a direct annual cost per resident of creating a |
| `precision_discussed` | 3 | 27% | qje_2026_qje_qjaf045 p.26-26 Section III.C.3: The authors compute an implied number of additional lynching events attributable to the estimated local averag; restud_2025_restud_rdae108 p.16-23 Section 4.2; Section 4.2.3; footnote 21: The text distinguishes point estimates that are positive but not significant from significant ones, reports p- |
| `sd_units` | 3 | 27% | aer_114_11_1 p.16-16 Section IV.A: The five main outcome families are each first summarized as a single index effect measured in standard-deviati; jpe_2026_740226 p.21-21 Section IV.D: Expresses the skill-development effect in standard-deviation units of the standardized college exam score and  |
| `elasticity` | 2 | 18% | restud_2025_restud_rdaf004 p.2-26 fn. 1; Table 2; Section 6.3: Effects are expressed relative to the treated baseline mean and as elasticities to earnings; the introduction ; restud_2026_restud_rdag071 p.19-26 Figure 7; Table 2: Effects are shown in three panels: point estimates, control-group means, and estimates relative to control mea |
| `monetary_terms` | 2 | 18% | restud_2026_restud_rdag037 p.31-32 Section 5.5.3, Table A21: A back-of-envelope exercise converts sentencing effects into sentence-years and dollar costs using a per-year ; restud_2026_restud_rdag071 p.19-26 Figure 7; Table 2: Effects are shown in three panels: point estimates, control-group means, and estimates relative to control mea |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.4-17 Introduction; Section 4.2; Appendix Tables D.10, B.3: Effects are expressed in standard deviation units of the differenced outcome throughout; estimates in natural  |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.4-17 Introduction; Section 4.2; Appendix Tables D.10, B.3: Effects are expressed in standard deviation units of the differenced outcome throughout; estimates in natural  |
| `online_appendix_not_available` | 1 | 9% | aer_114_11_1 p.38-38 Section VI, Conclusion: The conclusion reports a back-of-envelope cost-benefit figure, a direct annual cost per resident of creating a |
| `other:cross_period_magnitude_comparison` | 1 | 9% | aer_110_2_5 p.2-2 Introduction: The paper's central magnitude claim is framed as a comparison across waves spanning more than a century, argui |
| `other:persistence_used_as_interpretive_evidence` | 1 | 9% | aer_110_2_5 p.28-28 Section III.G, Devaluation of Water Infrastructure: The persistence of the effect long after the well water source had been replaced by piped water is used as int |

### mechanism_evidence (papers with this category: 7/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `intermediate_outcomes` | 6 | 55% | aer_110_2_5 p.20-22 Sections III.C-D: The proposed tenant-composition mechanism is supported with intermediate outcomes on residential turnover, hou; aer_114_11_1 p.31-33 Sections V.A-B, Table 5: Civic engagement measures and candidate characteristics such as criminal record, caste and wealth are used as  |
| `model_guided` | 5 | 46% | aer_110_2_5 p.39-40 Appendix A, back-of-the-envelope calculations: A theoretical model is calibrated with historical return-to-capital estimates and contract-renegotiation frequ; jpe_2026_740226 p.30-33 Section IV.G: Frames the improvement in college value-added as the mechanism connecting the financial-aid shock to later ski |
| `ruled_out_alternatives` | 5 | 46% | aer_114_11_1 p.33-37 Sections V.B, V.D: Elite capture, geographic compactness, and caste homogeneity are each tested using heterogeneity splits and ex; qje_2026_qje_qjaf045 p.22-24 Table II, columns 5-8: A general-violence explanation is partly addressed by estimating the same RD specification for white lynchings |
| `suggestive_labelled` | 4 | 36% | jpe_2026_740226 p.33-33 Table 5: Compares realized attainment and earnings effects against effects predicted purely from the estimated shift in; qje_2026_qje_qjaf045 p.51-54 Section V: The final section linking lynching to later Democratic electoral gains is explicitly characterized by the auth |
| `heterogeneity_as_mechanism` | 1 | 9% | aer_114_11_1 p.35-35 Section V.C, Table 6: Subsample splits by prior largest-village status and pradhan home village in Table 6 are used to distinguish a |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.11-29 Section 3.4.1; Section 5.1; Appendix Figure E.7, Tables E.6, E.7: Policy change is tested first on directional policy levels and then on the absolute value of the post minus pr |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.27-28 Section 4.5; Appendix Figure E.8, Tables E.8, E.9; footnotes 23, 24: Leader characteristics as an alternative channel are examined by running the RD on winner ideology scores and  |
| `other:absolute_value_outcome_for_non_directional_change` | 1 | 9% | restud_2025_restud_rdae108 p.11-29 Section 3.4.1; Section 5.1; Appendix Figure E.7, Tables E.6, E.7: Policy change is tested first on directional policy levels and then on the absolute value of the post minus pr |
| `other:case_studies` | 1 | 9% | restud_2025_restud_rdae108 p.23-23 Section 4.2.4; Appendix G, Figures G.1-G.4: Four country case studies with time-series figures are used in an appendix to illustrate the main result, intr |

### other (papers with this category: 2/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_footnote` | 1 | 9% | restud_2025_restud_rdae108 p.8-28 footnotes 9, 14, 15, 16, 20, 23, 24: Footnotes carry many pre-emptive checks (exclusion probability, small parliaments, prior free-and-fair electio |
| `other:evidence available upon request` | 1 | 9% | restud_2025_restud_rdaf004 p.25-25 Section 6.2 fn. 56: One piece of supporting evidence (dismissal-cycle density patterns) is described as available upon request rat |
| `other:reviewer_facing_footnotes` | 1 | 9% | restud_2025_restud_rdae108 p.8-28 footnotes 9, 14, 15, 16, 20, 23, 24: Footnotes carry many pre-emptive checks (exclusion probability, small parliaments, prior free-and-fair electio |

### preregistration_or_ethics (papers with this category: 2/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `irb_stated` | 2 | 18% | jpe_2026_740226 p.1-2 Acknowledgments footnote: States that the study received approval from a named university's institutional review board, citing a specifi; restud_2025_restud_rdaf004 p.30-30 Acknowledgments: Ethics approval from a university review board is reported with a protocol number in the acknowledgments. |

### presentation_convention (papers with this category: 10/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `coefficient_plot` | 9 | 82% | aer_114_11_1 p.25-28 Figures 3-4: Heterogeneity-by-population-bin results and the robustness/placebo summary are both presented as coefficient p; jpe_2026_740226 p.14-38 Figures 2-11: Pairs nearly every main results figure with a companion panel comparing pre- and post-policy outcomes for the  |
| `rd_plot` | 8 | 73% | aer_110_2_5 p.11-11 Figure 2 notes: RD figures throughout the paper use binned local averages at two bin widths overlaid with a fitted polynomial ; aer_114_11_1 p.12-25 Figures 1-3: Figures 1 through 3 present binned-scatter RD plots, showing population bins with fitted polynomial lines, for |
| `notes_state_se` | 7 | 64% | aer_114_11_1 p.13-13 Table 1 notes: Tables report exact p-values in brackets below clustered standard errors rather than significance stars, with ; jpe_2026_740226 p.17-42 Tables 1-6 and notes: Places a standard-error-in-parentheses convention beneath each coefficient throughout every results table, and |
| `appendix_tables_numbered_a` | 6 | 55% | aer_114_11_1 p.16-16 footnote 14, throughout: Online appendix tables and figures are consistently labeled with an A prefix, for example Table A3 or Figure A; jpe_2026_740226 p.8-8 Figure 1 caption: Labels every appendix table and figure with an A prefix and states, the first time an appendix item is cited,  |
| `notes_state_sample` | 6 | 55% | qje_2026_qje_qjaf045 p.21-50 Table notes throughout: Every regression table uses conventional significance stars at three thresholds and states in its own notes wh; restud_2025_restud_rdae108 p.12-22 Tables 1-3 notes; appendix references throughout: Tables use significance stars with the threshold legend in notes (the main table omits the ten percent star, o |
| `stars_used` | 5 | 46% | jpe_2026_740226 p.17-42 Tables 1-6 and notes: Places a standard-error-in-parentheses convention beneath each coefficient throughout every results table, and; qje_2026_qje_qjaf045 p.21-50 Table notes throughout: Every regression table uses conventional significance stars at three thresholds and states in its own notes wh |
| `binscatter` | 4 | 36% | aer_110_2_5 p.11-11 Figure 2 notes: RD figures throughout the paper use binned local averages at two bin widths overlaid with a fitted polynomial ; aer_114_11_1 p.12-25 Figures 1-3: Figures 1 through 3 present binned-scatter RD plots, showing population bins with fitted polynomial lines, for |
| `no_stars` | 4 | 36% | aer_110_2_5 p.13-24 Tables 1-8: None of the regression tables use significance stars; coefficients and clustered standard errors are reported ; aer_114_11_1 p.13-13 Table 1 notes: Tables report exact p-values in brackets below clustered standard errors rather than significance stars, with  |
| `online_appendix_not_available` | 4 | 36% | aer_114_11_1 p.16-16 footnote 14, throughout: Online appendix tables and figures are consistently labeled with an A prefix, for example Table A3 or Figure A; jpe_2026_740226 p.8-8 Figure 1 caption: Labels every appendix table and figure with an A prefix and states, the first time an appendix item is cited,  |
| `raw_data_plot` | 4 | 36% | jpe_2026_740226 p.14-38 Figures 2-11: Pairs nearly every main results figure with a companion panel comparing pre- and post-policy outcomes for the ; restud_2025_restud_rdae108 p.3-10 Figure 1; Appendix Figure B.2: Descriptive figures precede results: the share of elections with a turnover per half-decade in the main text,  |
| `summary_stats_table` | 4 | 36% | aer_110_2_5 p.13-13 Table 1: The paper's first table serves a dual role as both a pre-treatment summary-statistics table and a balance tabl; qje_2026_qje_qjaf045 p.14-14 Section III.A: Detailed summary statistics for the sample variables are deferred entirely to a lettered online-appendix secti |
| `event_study_figure` | 3 | 27% | restud_2025_restud_rdae108 p.13-21 Figures 5, 6, 7 notes: Subsample results and dynamic effects are shown as coefficient plots with robust confidence intervals at a low; restud_2025_restud_rdaf004 p.16-29 Figures 2 to 9; Tables 2, 3: Figures are event-study plots with confidence bands, binned RD plots with local linear fits, and coefficient p |
| `in_main_text` | 2 | 18% | qje_2026_qje_qjaf045 p.26-26 Figure V: The paper presents binned-scatter RD plots of the outcome against the loss margin, separately for Black and wh; restud_2025_restud_rdae108 p.13-17 Figures 2, 4 and notes: RD plots use sample means in fixed-width bins of the running variable with linear fits on each side, and print |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.3-10 Figure 1; Appendix Figure B.2: Descriptive figures precede results: the share of elections with a turnover per half-decade in the main text,  |
| `map` | 1 | 9% | restud_2025_restud_rdae108 p.3-10 Figure 1; Appendix Figure B.2: Descriptive figures precede results: the share of elections with a turnover per half-decade in the main text,  |
| `other:appendix_tables_numbered_b` | 1 | 9% | aer_110_2_5 p.40-48 Appendix B heading: Appendix tables and figures are labeled with a 'B' prefix rather than the more common 'A' prefix, because the  |
| `other:disclosure_examples_appendix` | 1 | 9% | rfs_2024_rfs_hhae045 p.48-50 Appendix A, Appendix B: Appendices provide a timeline of treatment and measurement windows and reproduced examples of actual disclosur |
| `other:doubles_as_balance_table` | 1 | 9% | aer_110_2_5 p.13-13 Table 1: The paper's first table serves a dual role as both a pre-treatment summary-statistics table and a balance tabl |
| `other:schematic_identification_figure` | 1 | 9% | restud_90_1_3 p.11-11 Figure 1: A schematic figure with hypothetical data is used to explain the two sources of identifying variation before a |
| `other:supplementary_appendices_lettered_by_topic` | 1 | 9% | restud_90_1_3 p.9-33 Footnotes and text pointers to Supplementary Appendices A to N: Supplementary material is organised into lettered appendices by topic (A through N) plus a B-series of figures |
| `other:timeline_appendix` | 1 | 9% | rfs_2024_rfs_hhae045 p.48-50 Appendix A, Appendix B: Appendices provide a timeline of treatment and measurement windows and reproduced examples of actual disclosur |

### replication_statement (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 8 | 73% | aer_114_11_1 p.42-42 References: A data-and-code citation with an ICPSR DOI is listed in the references, indicating a public openICPSR replicat; jpe_2026_740226 p.44-44 Data Availability statement: Points readers to a named external replication package hosted on a data repository for the code that reproduce |
| `code_public` | 6 | 55% | jpe_2026_740226 p.44-44 Data Availability statement: Points readers to a named external replication package hosted on a data repository for the code that reproduce; restud_2025_restud_rdae108 p.32-32 Data Availability; Supplementary Data: A Data Availability statement says data and code are publicly available on Zenodo with a DOI; supplementary da |
| `software_named` | 5 | 46% | aer_110_2_5 p.10-25 Section II.A footnote; Section III.F: Specific software tools are named directly in the text for constructing the geographic design, including a net; aer_114_11_1 p.11-11 Section III: The rdrobust Stata command and its methodological references (Calonico, Cattaneo, and Titiunik 2014; Calonico  |
| `data_access_procedure_described` | 4 | 36% | jpe_2026_740226 p.44-44 Data Availability statement: States that the underlying administrative microdata are proprietary and names the specific government agencies; restud_2025_restud_rdaf004 p.30-30 Data Availability: A data availability statement says most data are restricted Brazilian records; a Zenodo package with code, ins |
| `data_restricted` | 4 | 36% | jpe_2026_740226 p.44-44 Data Availability statement: States that the underlying administrative microdata are proprietary and names the specific government agencies; restud_2025_restud_rdaf004 p.30-30 Data Availability: A data availability statement says most data are restricted Brazilian records; a Zenodo package with code, ins |
| `data_public` | 3 | 27% | aer_114_11_1 p.42-42 References: A data-and-code citation with an ICPSR DOI is listed in the references, indicating a public openICPSR replicat; qje_2026_qje_qjaf045 p.54-55 Data Availability statement: The article includes a short Data Availability statement citing a Harvard Dataverse deposit as the location of |
| `in_footnote` | 1 | 9% | restud_2025_restud_rdaf004 p.12-12 Section 5 fn. 36: Stata packages used for the analysis (gtools, reghdfe/ftools, rdrobust, did_multiplegt, ebalance, estout) are  |
| `other:availability_deferred_to_journal_page` | 1 | 9% | aer_110_2_5 p.1-1 Title page footnote: Rather than stating data or code availability in the body text, a title-page footnote directs readers to the j |
| `other:software_not_named` | 1 | 9% | restud_2026_restud_rdag071 p.1-39 whole paper: No statistical software is named in the main text. |

### robustness_reported (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 9 | 82% | aer_110_2_5 p.24-24 Section III.F, BSP Boundary Definition; Appendix Table B5: The main specification is rerun using the original epidemiologist's hand-drawn boundary instead of the authors; aer_114_11_1 p.29-29 Section IV.E, Spillovers: A spillover check tests whether blocks with a higher share of just-above-cutoff villages show worse outcomes i |
| `alt_specification` | 7 | 64% | aer_114_11_1 p.29-29 Section IV.E, Financing: A financing robustness check uses GP accounting data to test whether smaller GPs mechanically receive more per; qje_2026_qje_qjaf045 p.25-29 Table III, Panel B: A single consolidated, numbered-row robustness table varies the control set from none to progressively richer  |
| `alt_sample` | 6 | 55% | aer_114_11_1 p.22-22 footnote 24: A robustness check drops villages potentially contaminated by simultaneous nearby splits near the 2015 thresho; jpe_2026_740226 p.21-21 Section IV.D: Repeats the college-exam skill-development analysis using a longer post-graduation window that includes exam s |
| `alt_bandwidth` | 5 | 46% | aer_110_2_5 p.18-18 Section III.B; Tables 3, 4, 6, 7, 8: Widening the estimation window to a common fixed bandwidth across nearly every outcome table is used both as a; qje_2026_qje_qjaf045 p.29-29 Table III, Panel C: Separate rows of the same robustness table vary the running-variable polynomial order from linear through quar |
| `in_main_text` | 5 | 46% | aer_110_2_5 p.17-17 Tables 2-8: Rather than relegating functional-form choice to an appendix, every main results table places local-linear and; jpe_2026_740226 p.21-21 Section IV.D: Repeats the college-exam skill-development analysis using a longer post-graduation window that includes exam s |
| `alt_estimator` | 4 | 36% | aer_110_2_5 p.17-17 Tables 2-8: Rather than relegating functional-form choice to an appendix, every main results table places local-linear and; qje_2026_qje_qjaf045 p.29-29 Table III, Panel C: Separate rows of the same robustness table vary the running-variable polynomial order from linear through quar |
| `in_footnote` | 3 | 27% | aer_114_11_1 p.22-22 footnote 24: A robustness check drops villages potentially contaminated by simultaneous nearby splits near the 2015 thresho; restud_2025_restud_rdae108 p.7-18 Section 2.2 footnote 7; Section 4.2 footnote 16; Section 4.3.7; Appendix Tables D.1-D.4: Alternative data sources for the same outcome (GDP growth, trade) and alternative democracy measures including |
| `summarized_in_one_table` | 3 | 27% | aer_110_2_5 p.24-24 Section III.F, BSP Boundary Definition; Appendix Table B5: The main specification is rerun using the original epidemiologist's hand-drawn boundary instead of the authors; qje_2026_qje_qjaf045 p.25-29 Table III, Panel B: A single consolidated, numbered-row robustness table varies the control set from none to progressively richer  |
| `summarized_in_figure` | 2 | 18% | qje_2026_qje_qjaf045 p.29-30 Section III.C.6; Online Appendix Figure C.1: Sample sensitivity is summarized in an appendix figure rather than a table, dropping each sample state and eac; restud_2025_restud_rdae108 p.11-26 Section 3.4.1; Section 4.4.1; Figure 7: OLS estimates, described as difference-in-differences because outcomes are differenced from the pre-election y |
| `alt_fixed_effects` | 1 | 9% | qje_2026_qje_qjaf045 p.25-29 Table III, Panel B: A single consolidated, numbered-row robustness table varies the control set from none to progressively richer  |
| `leave_one_out` | 1 | 9% | restud_2025_restud_rdae108 p.24-24 Sections 4.3.4-4.3.6; Appendix Table D.8: Index-construction robustness drops each component in turn, restricts to complete cases, uses a Pocock-type co |
| `online_appendix_not_available` | 1 | 9% | aer_114_11_1 p.22-22 footnote 24: A robustness check drops villages potentially contaminated by simultaneous nearby splits near the 2015 thresho |
| `other:alt_boundary_definition` | 1 | 9% | aer_110_2_5 p.24-24 Section III.F, BSP Boundary Definition; Appendix Table B5: The main specification is rerun using the original epidemiologist's hand-drawn boundary instead of the authors |
| `other:alternative_explanations_addressed` | 1 | 9% | aer_110_2_5 p.27-28 Section III.G: Two specific alternative explanations for the price gap, disease stigma and devaluation of the water source, a |
| `other:reweighting_to_population` | 1 | 9% | restud_2026_restud_rdag071 p.26-26 Section 4.5; Appendix Table B.8: To probe generalization the estimation sample is reweighted by logit-predicted probabilities of not appearing  |
| `other:supporting_text_search` | 1 | 9% | rfs_2024_rfs_hhae045 p.33-33 Section 4.3, Table IA-8: A supplementary check uses SEC EDGAR full-text search to see whether treated firms mention the proxy advisor i |

### sample_construction (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 9 | 82% | aer_110_2_5 p.8-10 Section I.C: Distinct data sources are stitched together by period: tax assessment records, a land registry sales database,; aer_114_11_1 p.9-10 Section II: Analysis combines Census of India rounds, the SHRUG village linkage panel, the Socioeconomic and Caste Census, |
| `sample_period_stated` | 9 | 82% | aer_110_2_5 p.7-7 Section I.C: The unit of observation is an individual residential address in one London parish, tracked as an unbalanced pa; aer_114_11_1 p.7-7 Section I.B: Two delimitation episodes anchor the sample periods: the 1995 delimitation using 1991 census population, and t |
| `sample_size_reported_per_table` | 9 | 82% | aer_110_2_5 p.16-24 Tables 2-8: Observation counts differ substantially across otherwise-comparable tables because the estimation sample is re; aer_114_11_1 p.13-13 Table 1: Every regression table reports the effective number of observations and the estimation bandwidth for each colu |
| `exclusions_justified` | 8 | 73% | aer_110_2_5 p.23-23 Section III.E, discussion of Table 3 panel D: For the latest historical wave the authors note an unexplained gap in digitized records for part of the parish; aer_114_11_1 p.9-9 footnote 9: Outcomes are restricted to those that are neither very rare nor near-universal among untreated villages near t |
| `unit_of_observation_stated` | 8 | 73% | aer_110_2_5 p.7-7 Section I.C: The unit of observation is an individual residential address in one London parish, tracked as an unbalanced pa; aer_114_11_1 p.9-9 Section II, opening paragraph: The unit of observation is the census village, stated to be advantageous because villages nest within GPs so o |
| `matching_or_linkage_described` | 5 | 46% | aer_114_11_1 p.9-9 Section II, Matching Villages to GPs: Villages are matched to GPs via the 2021 Local Government Directory for the post-2015 period and a Department ; restud_2025_restud_rdaf004 p.10-11 Sections 4.1 to 4.3, fn. 30: Court registers (from a private information provider compiling public tribunal data) are linked to the univers |
| `attrition_reported` | 4 | 36% | aer_110_2_5 p.23-23 Section III.E, discussion of Table 3 panel D: For the latest historical wave the authors note an unexplained gap in digitized records for part of the parish; restud_2025_restud_rdae108 p.7-7 Section 2.2; Appendix Tables B.1 and C.1: Outcome data coverage per outcome is tabulated in an appendix, and a separate appendix table checks that the f |
| `restricted_data_used` | 4 | 36% | aer_110_2_5 p.8-10 Section I.C: Distinct data sources are stitched together by period: tax assessment records, a land registry sales database,; jpe_2026_740226 p.10-10 Section III, Data: Lists six linked administrative sources spanning exam records, a household means-testing registry, financial-a |
| `in_footnote` | 3 | 27% | restud_2025_restud_rdae108 p.6-6 Section 2.1.1, footnote 5; Appendix Figure B.1: When academic sources are lacking, results are collected from Wikipedia; the share of such cases is disclosed ; restud_2026_restud_rdag071 p.18-18 footnote 28: A further exclusion of one speed limit zone from the main RD analysis is justified by an unexplained mass poin |
| `in_main_text` | 2 | 18% | restud_2025_restud_rdae108 p.6-7 Section 2.1.1; Data Appendix A: The election universe is built from V-Dem as the primary source and complemented by many named election databa; rfs_2024_rfs_hhae045 p.22-46 Tables 3 to 12: Every regression table reports the number of firms or firm-years; RD and balance tables report treated and con |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.6-6 Section 2.1.1, footnote 5; Appendix Figure B.1: When academic sources are lacking, results are collected from Wikipedia; the share of such cases is disclosed  |
| `linked_records` | 1 | 9% | restud_90_1_3 p.6-7 Section 2, data paragraphs: Each data source (entrance exam applications, three exam series, police arrests, birth registry, national insu |
| `other:completeness_cross_check` | 1 | 9% | rfs_2024_rfs_hhae045 p.13-13 Section 2.1: Sample completeness is cross-verified against a list of below-threshold firms supplied directly by the proxy a |
| `other:first_crossing_only` | 1 | 9% | rfs_2024_rfs_hhae045 p.13-14 Section 2.1, footnote 10: The RD subsample keeps only firms that fall within a narrow window around the threshold for the first time in  |
| `other:independent_audit_of_key_variables` | 1 | 9% | restud_2025_restud_rdae108 p.9-9 Section 3.1.1; Data Appendix H.4: The key running and treatment variables were checked through an independent audit covering all elections withi |
| `summary_stats_table` | 1 | 9% | restud_90_1_3 p.8-8 Table 1: The summary statistics table reports the number of individuals in each linked dataset panel and for each subgr |

### specification_reporting (papers with this category: 8/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `n_reported` | 7 | 64% | aer_110_2_5 p.16-24 Tables 2-8: Every specification table reports the estimation sample size and the outcome mean among untreated (outside-bou; aer_114_11_1 p.15-15 Table 2 notes: Each results table reports the RD point estimate, clustered standard error, bracketed p-value, dependent-varia |
| `baseline_then_variants` | 6 | 55% | aer_110_2_5 p.17-17 Table 3 layout: Each results table presents the same outcome across a fixed sequence of columns: local-linear baseline, local-; jpe_2026_740226 p.21-23 Table 3: Separates reduced-form intention-to-treat tables from a distinct instrumental-variable table that rescales the |
| `mean_of_dependent_reported` | 6 | 55% | aer_110_2_5 p.16-24 Tables 2-8: Every specification table reports the estimation sample size and the outcome mean among untreated (outside-bou; aer_114_11_1 p.15-15 Table 2 notes: Each results table reports the RD point estimate, clustered standard error, bracketed p-value, dependent-varia |
| `se_type_in_notes` | 6 | 55% | aer_110_2_5 p.16-24 Notes to Tables 2-8: Table notes state the standard-error type and clustering unit, list which control variables and fixed effects ; aer_114_11_1 p.15-15 Table 2 notes: Table notes uniformly restate that standard errors are clustered at the gram panchayat level and that reported |
| `cluster_level_in_notes` | 5 | 46% | aer_110_2_5 p.16-24 Notes to Tables 2-8: Table notes state the standard-error type and clustering unit, list which control variables and fixed effects ; aer_114_11_1 p.15-15 Table 2 notes: Table notes uniformly restate that standard errors are clustered at the gram panchayat level and that reported |
| `controls_progressive_columns` | 4 | 36% | aer_110_2_5 p.17-17 Table 3 layout: Each results table presents the same outcome across a fixed sequence of columns: local-linear baseline, local-; aer_114_11_1 p.26-26 Table 4: Table 4 augments the baseline RD specification with a continuous interaction term between the treatment dummy  |
| `fe_listed_in_table` | 3 | 27% | aer_110_2_5 p.16-24 Notes to Tables 2-8: Table notes state the standard-error type and clustering unit, list which control variables and fixed effects ; qje_2026_qje_qjaf045 p.22-24 Table II: The main results table explicitly lists, row by row, which fixed effects and spatial controls enter each colum |
| `weights_stated` | 3 | 27% | aer_110_2_5 p.16-16 Table 2 notes: Every RD specification is described as using a triangular kernel that weights observations by distance to the ; aer_114_11_1 p.11-11 Section III: All main specifications state use of a triangular kernel with MSE-optimal bandwidth selection following Caloni |
| `stars_used` | 2 | 18% | qje_2026_qje_qjaf045 p.24-24 Table II notes: Table notes state, for every main results table, that standard errors in parentheses are clustered at the coun; restud_2025_restud_rdae108 p.12-12 Table 1 and notes: The main table reports, per outcome column, the RD point estimate, robust standard error in parentheses, the p |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.12-12 Table 1 and notes: The main table reports, per outcome column, the RD point estimate, robust standard error in parentheses, the p |
| `other:all estimates rescaled by treated baseline mean` | 1 | 9% | restud_2025_restud_rdaf004 p.14-14 Section 5.3 fn. 39: All estimates throughout the paper are rescaled by the treated-group outcome mean in the year before layoff; a |
| `other:bandwidth_reported_per_column` | 1 | 9% | restud_2025_restud_rdae108 p.12-12 Table 1 and notes: The main table reports, per outcome column, the RD point estimate, robust standard error in parentheses, the p |
| `other:elasticity_row` | 1 | 9% | restud_2026_restud_rdag071 p.26-26 Table 2: The IV table stacks first stage, reduced form and IV panels, and reports control mean, an elasticity row, band |
| `other:kernel_and_polynomial_stated` | 1 | 9% | rfs_2024_rfs_hhae045 p.30-33 Section 4.2, Table 6 rows: The sharp RD omits covariates and FE, justified by the balance table; the text states the estimator (robust bi |
| `other:no_covariates_in_baseline` | 1 | 9% | restud_2025_restud_rdae108 p.10-24 Equation (1); Section 4.3.3; Appendix Tables D.11-D.15, D.17: The baseline RD includes no fixed effects or covariates; region and decade fixed effects and pre-election outc |
| `other:no_r2_reported` | 1 | 9% | aer_110_2_5 p.16-24 Tables 2-8: Every specification table reports the estimation sample size and the outcome mean among untreated (outside-bou |
| `other:rd_no_covariates_justified` | 1 | 9% | rfs_2024_rfs_hhae045 p.30-33 Section 4.2, Table 6 rows: The sharp RD omits covariates and FE, justified by the balance table; the text states the estimator (robust bi |

### variable_construction (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `running_variable_definition` | 9 | 82% | aer_110_2_5 p.12-12 Section II.B, equation (1): The running variable is defined as signed walking distance in meters from a property to the nearest point on t; aer_114_11_1 p.11-11 Section III, equation (1): Treatment is a dummy for village population at or above the cutoff (one thousand) in the relevant pre-delimita |
| `treatment_definition` | 9 | 82% | aer_110_2_5 p.10-10 Section II.A: Treatment status is an indicator for whether a property's nearest well by network (walking-distance) Voronoi p; aer_114_11_1 p.11-11 Section III, equation (1): Treatment is a dummy for village population at or above the cutoff (one thousand) in the relevant pre-delimita |
| `outcome_definition` | 7 | 64% | aer_110_2_5 p.12-24 Section II.B and Tables 3, 8: The primary outcome is a log transformation of property value, with the underlying value measure changing by p; jpe_2026_740226 p.10-21 Section III (source 5) and footnote 12: Constructs the skill-development outcome by summing scores on the generic-competency modules of the mandatory  |
| `standardized_index` | 6 | 55% | aer_110_2_5 p.10-10 Section I.C, footnote: A four-category socioeconomic status variable is built by recoding an eight-tier historical poverty classifica; aer_114_11_1 p.16-16 footnote 13: Multi-outcome indices for education, infrastructure, workfare and programs are built following Kling, Liebman, |
| `logs_or_ihs` | 4 | 36% | aer_110_2_5 p.12-24 Section II.B and Tables 3, 8: The primary outcome is a log transformation of property value, with the underlying value measure changing by p; aer_114_11_1 p.10-10 footnote 10: Candidate wealth (movable and immovable assets) is transformed with the inverse hyperbolic sine because of sub |
| `measurement_error_discussed` | 4 | 36% | aer_114_11_1 p.9-9 footnote 8: Authors note census village boundaries remain essentially fixed over the panel, with splits rare and concentra; qje_2026_qje_qjaf045 p.26-26 Section III.C.3: The authors acknowledge that the historical lynching record is incomplete and reason explicitly about how this |
| `data_source_named` | 1 | 9% | restud_2025_restud_rdae108 p.7-7 Section 2.2, footnote 7: Each economic outcome is tied to a named source (Penn World Tables version stated, IMF, ILO, World Bank), chos |
| `in_appendix` | 1 | 9% | restud_2025_restud_rdae108 p.8-14 Sections 3.1.1, 3.1.2, 3.5.1; Appendix Table B.2: Incumbency follows explicit rules (executive power held for a minimum number of days in a fixed pre-election w |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.8-14 Sections 3.1.1, 3.1.2, 3.5.1; Appendix Table B.2: Incumbency follows explicit rules (executive power held for a minimum number of days in a fixed pre-election w |
| `instrument_construction` | 1 | 9% | restud_90_1_3 p.14-15 Section 3.5, footnote 16: Attendance is defined as enrolment in the school at the time of the secondary completion exam; the instrument  |
| `other:distance_covariate_construction` | 1 | 9% | aer_110_2_5 p.8-9 Section I.C: Distance-to-amenity control variables (wells, sewers, churches, banks, a plague pit, etc.) are computed as wal |
| `other:hand_collection` | 1 | 9% | rfs_2024_rfs_hhae045 p.14-16 Section 2.2, footnote 11: Because some disclosures are in images the script cannot read, the RD subsample is hand-checked; script-only r |
| `other:heterogeneity_groups_predetermined` | 1 | 9% | restud_2026_restud_rdag071 p.20-26 Section 4.3, Figure 8 notes, Table 2 notes: Income quartiles for heterogeneity are defined from predetermined income measured one to two years before the  |
| `other:missing_coding_rule` | 1 | 9% | rfs_2024_rfs_hhae045 p.16-16 Section 2.2.2: Coding of missing breadth measures is made explicit: set to zero when no engagement is disclosed, treated as m |
| `other:outcomes_signed_so_higher_is_better` | 1 | 9% | restud_90_1_3 p.15-17 Section 3.5 and Section 4 (Dropout paragraph): Binary outcomes (no dropout, no teen birth, no arrest, formal employment) are coded so that higher values mean |
| `other:text_keyword_measure` | 1 | 9% | rfs_2024_rfs_hhae045 p.14-15 Section 2.2.1, Table 1 notes: Outcomes are built by a Python script that flags engagement keywords within a fixed character distance of shar |
| `other:variable_appendix` | 1 | 9% | rfs_2024_rfs_hhae045 p.50-52 Appendix C, Table C1: All variables are defined in a dedicated appendix table, and every table note points to it. |
| `winsorization` | 1 | 9% | restud_2025_restud_rdae108 p.7-10 Sections 2.2 and 3.3.1: Summary indices follow Kling et al. (2007): unweighted averages of standardized components, signed so higher i |

### writing_structure (papers with this category: 9/11)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `results_previewed_in_intro` | 9 | 82% | aer_110_2_5 p.2-2 Introduction: The introduction previews the paper's short-run and multi-decade quantitative findings before the formal empir; aer_114_11_1 p.2-3 Introduction: The introduction previews the paper's main quantitative findings in detail, including education, housing, sani |
| `appendix_heavy` | 8 | 73% | aer_110_2_5 p.24-26 Section III.F: Robustness checks are collected in a dedicated lettered subsection within the results section, though several ; aer_114_11_1 p.30-30 Section V: Mechanism analysis occupies its own section after all main results, organized around four theory-linked channe |
| `contribution_paragraph` | 8 | 73% | aer_110_2_5 p.3-3 Introduction: A contribution paragraph explicitly distinguishes the paper's small, single-institutional-environment setting ; aer_114_11_1 p.4-4 Introduction: The introduction contains explicit contribution paragraphs positioning the paper against three literatures: ca |
| `mechanisms_after_main` | 8 | 73% | aer_110_2_5 p.4-28 Sections I-IV: The paper presents historical background and data collection before the formal empirical strategy section, and; aer_114_11_1 p.30-30 Section V: Mechanism analysis occupies its own section after all main results, organized around four theory-linked channe |
| `data_before_design` | 7 | 64% | aer_110_2_5 p.4-28 Sections I-IV: The paper presents historical background and data collection before the formal empirical strategy section, and; jpe_2026_740226 p.6-15 Sections II-IV.A: Orders the empirical narrative as institutional background, then data, then design and validity, before turnin |
| `roadmap_paragraph` | 7 | 64% | aer_110_2_5 p.4-4 Introduction: A roadmap paragraph at the end of the introduction previews the organization of the paper section by section.; aer_114_11_1 p.5-5 end of Introduction: A roadmap paragraph at the end of the introduction states the section-by-section organization of the paper. |
| `robustness_separate_section` | 7 | 64% | aer_110_2_5 p.24-26 Section III.F: Robustness checks are collected in a dedicated lettered subsection within the results section, though several ; aer_114_11_1 p.28-28 Section IV.E: Robustness checks are consolidated into their own labeled subsection at the end of the results section rather  |
| `main_result_first` | 2 | 18% | restud_2025_restud_rdae108 p.14-31 Sections 4 and 5: Within results, identification checks come first, then the main table, heterogeneity, dynamics, fuzzy-RD execu; restud_2025_restud_rdaf004 p.6-29 Sections 2 to 7: Order is model, context, data, then for each design: identification, main dynamic results, measurement checks, |
| `online_appendix_not_available` | 2 | 18% | aer_114_11_1 p.30-30 Section V: Mechanism analysis occupies its own section after all main results, organized around four theory-linked channe; qje_2026_qje_qjaf045 p.14-50 Sections III-V: The main text repeatedly defers alternative outcome codings, fixed-bandwidth replications, additional inferenc |
| `in_main_text` | 1 | 9% | restud_2025_restud_rdae108 p.14-14 Section 3.5.1: Variable definitions are made concrete with named historical elections showing the values of running and treat |
| `other:assumption_tests_subsection` | 1 | 9% | restud_90_1_3 p.5-17 Sections 2 to 3.6: The order is context and data, then design with a subsection that tests each identifying and modelling assumpt |
| `other:definitions_illustrated_with_examples` | 1 | 9% | restud_2025_restud_rdae108 p.14-14 Section 3.5.1: Variable definitions are made concrete with named historical elections showing the values of running and treat |
| `other:each result tied to a model proposition` | 1 | 9% | restud_2025_restud_rdaf004 p.12-28 Section 5 opening; Section 6 opening; Section 7: Each empirical section states which model proposition it tests, and the mechanisms section revisits results pr |
| `other:epigraph_used` | 1 | 9% | aer_110_2_5 p.1-1 Title page: The paper opens with an epigraph quoted from a popular history book before the formal introduction begins, an  |
| `other:model_after_empirics` | 1 | 9% | restud_2026_restud_rdag071 p.28-31 Section 5: The theoretical model is presented after the empirical results and is explicitly positioned as rationalizing t |
| `other:two_part_paper` | 1 | 9% | restud_90_1_3 p.17-34 Sections 4, 5 and 5.4: The paper is structured as two linked empirical exercises: causal school effects (first part) feed as regresso |
| `other:validation_before_estimation` | 1 | 9% | rfs_2024_rfs_hhae045 p.23-30 Section 4.1, Table 4: Design validation (density, balance) is given its own subsection and table titled validity of research design  |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | agree | 7 | aer_110_2_5 x2 (paper: Bandwidth is chosen by an MSE-optimal, data-driven rule (Calonico-Catt / card: Diagnostic x2 records kind=bandwidth_selection, status=observed, descr); aer_114_11_1 x2 (paper: MSE-optimal bandwidth (Calonico, Cattaneo, and Titiunik 2014; Calonico / card: diagnostic x2 records bandwidth_selection status=observed, MSE-optimal) |
| bandwidth | paper_only | 2 | restud_2025_restud_rdaf004 s10.sample (paper: 45 days, symmetric / card: abs(t)<=${band} with band unspecified); restud_90_1_3 s4 (paper: Main models use all variation with a 5th-order polynomial; RD validati / card: rdrobust with uniform kernel, p(5); areg restricted to abs(score) with) |
| bandwidth | unknown | 1 | aer_112_10_8 s2.sample (paper: The appendix regression-kink implementation of the listing-premium hoc / card: Card specification s2 shows a formula with a local-polynomial order an) |
| cluster_level | agree | 5 | aer_110_2_5 s1.se.cluster_level (paper: Standard errors are clustered at the street-block level in essentially / card: s1, s2 and s7 record se.type=cluster with se.cluster_level left null, ); aer_114_11_1 s2.se.cluster_level (paper: Standard errors clustered at the gram panchayat level throughout (foot / card: se.type=cluster for s1-s5; cluster_level resolved to gp_code_jj11_num ) |
| cluster_level | paper_only | 3 | restud_2025_restud_rdae108 s1.se.cluster_level (paper: Baseline is unclustered; clustering at country by year is an appendix  / card: s1.se.cluster_level null; no clustered spec recorded.); restud_2026_restud_rdag037 s1.se.cluster_level (paper: No clustering for the main table; state-level clustering for state spl / card: cluster_level null for s1 and s2; no prosecutor-level spec recorded.) |
| cluster_level | unknown | 1 | restud_2025_restud_rdaf004 s1.se.cluster_level (paper: DiD standard errors clustered at the firm level / card: s1 to s5: cl(identificad)) |
| comparison_group | paper_only | 4 | aer_110_2_5 d1.comparison_group (paper: The comparison group is properties just outside the contaminated well' / card: Design d1 records comparison_group as null.); aer_114_11_1 d1.comparison_group (paper: Villages just below the 1,000-population cutoff serve as the compariso / card: comparison_group is null in design d1 and in all specifications s1-s5.) |
| comparison_group | agree | 1 | aer_112_10_8 s2.comparison_group (paper: The appendix regression-kink check is a single-threshold kink design a / card: Card specification s2.comparison_group is null, consistent with a kink) |
| controls | paper_only | 4 | aer_112_10_8 s1.controls_summary (paper: The hedonic model's control set is spelled out in the text: time-varyi / card: Card specification s1.controls_summary is null; only the outcome varia); jpe_2026_740226 s5.controls_summary (paper: Lists the specific baseline demographic, household, and high-school co / card: Leaves the controls-summary field unrecorded for the value-added speci) |
| controls | agree | 3 | aer_110_2_5 s2.controls_summary (paper: Covariates (distance to neighborhood amenities, sewer access) are adde / card: Specification s2's structured controls_summary field is null, though i); restud_90_1_3 s5 (paper: Sex, district of residence FE, religion FE, polynomial in entrance sco / card: s5 uses sea_sex, sea_religion dummies, sea_district dummies, score ter) |
| controls | unknown | 1 | restud_2025_restud_rdae108 s1.controls_summary (paper: No covariates in the baseline; pre-election outcome controls added in  / card: s1.controls_summary null.) |
| controls | disagree | 1 | restud_2025_restud_rdaf004 s10.controls (paper: RD baseline has only eligibility dummy, running variable and interacti / card: s10 adds worker and firm covariates (tempempr, lnrem, school, age, sec) |
| data_source | paper_only | 9 | aer_112_10_8 data (paper: The paper names four core administrative data sources plus one commerc / card: The card's top-level data array is empty; no data sources are recorded); jpe_2026_740226 data[0].source_hint (paper: Names six specific administrative agencies as data sources, describing / card: Records only two generically named datasets referenced in the code, wi) |
| data_source | agree | 3 | aer_110_2_5 data[0].name (paper: The analysis draws on tax assessment records, land-registry sales, a r / card: Card data[] entries name four Stata .dta files (Merged_1853_1864_data,); aer_114_11_1 data[0].name (paper: Village-level analysis datasets cover amenities, village directory, fi / card: data[] lists amenities_analysis.dta and village_analysis_cleaned.dta () |
| diagnostic | agree | 8 | aer_110_2_5 x1 (paper: A McCrary-style density (manipulation) test on the running variable is / card: Diagnostic x1 records kind=density_test, status=unknown, with a note t); aer_114_11_1 x3 (paper: A linear polynomial (p=1) is used in all main and robustness specifica / card: diagnostic x3 (polynomial_order) status=observed, p=1 default in Multi) |
| diagnostic | paper_only | 8 | aer_112_10_8 diagnostics (paper: The paper reports an extensive set of diagnostics: hedonic fit-statist / card: The card's diagnostics array is empty.); aer_114_11_1 x1 (paper: A density/manipulation test (Cattaneo, Jansson, and Ma 2018) is report / card: diagnostic x1 (density_test) has status=not_found_in_scope; rddensity ) |
| diagnostic | unknown | 1 | restud_2026_restud_rdag037 x1 (paper: KS test of pre-2010 distributions by race, placebo reassignment exerci / card: x1 density_test with unknown details.) |
| estimator | agree | 13 | aer_110_2_5 s1.estimator (paper: Local-linear RD with a triangular kernel and MSE-optimal bandwidth (Ca / card: Specifications s1, s2 and s7 record estimator local_linear_rd implemen); aer_112_10_8 s1.formula_or_call (paper: The hedonic fair-value model is estimated as an OLS regression of log  / card: Card specification s1 records the same command and formula, an OLS reg) |
| estimator | paper_only | 1 | aer_112_10_8 designs (paper: The paper's primary estimator for its main claims is a structural mode / card: The card records only two designs, an OLS hedonic regression (d1/s1) a) |
| fixed_effects | agree | 7 | aer_112_10_8 s1.fixed_effects (paper: The hedonic model's fixed effects are described as year-cross-municipa / card: Card specification s1 lists fixed_effects as year and komstr, matching); aer_114_11_1 s1.fixed_effects (paper: Equation (1) is a cross-sectional RD with polynomial controls only; no / card: fixed_effects is null for specifications s1-s5.) |
| fixed_effects | paper_only | 3 | aer_110_2_5 s1.fixed_effects (paper: Table 3 column 5 adds fixed effects for five equal-length boundary seg / card: Card specifications s1 and s2 both record fixed_effects as null; no bo); restud_2026_restud_rdag037 s1.fe (paper: No fixed effects in the main specification; district FE and race-speci / card: fe None for s1 and s2; no other specs recorded.) |
| fixed_effects | unknown | 1 | restud_2025_restud_rdae108 s1.fixed_effects (paper: No fixed effects in the baseline; region and decade FE only in appendi / card: s1.fixed_effects null.) |
| fixed_effects | disagree | 1 | restud_2025_restud_rdaf004 s10.fe (paper: RD: no fixed effects in the baseline local linear model / card: s10 absorb(mun)) |
| other | unknown | 1 | restud_2026_restud_rdag037 packages.rdplot (paper: RD-style plots of sentence around 280 g and time discontinuity around  / card: Package rdplot listed under Stata with unknown use.) |
| other | paper_only | 1 | restud_2026_restud_rdag071 methods (paper: IV via 2SLS with crossing the cutoff as instrument for fine amount / card: only rdd recorded as method) |
| other | agree | 1 | rfs_2024_rfs_hhae045 s1.formula_or_call (paper: Triangular kernel for all local polynomial estimators; cutoff at the 7 / card: c(0.7) in the call; kernel not stated in the call (rdrobust default is) |
| outputs | paper_only | 7 | aer_110_2_5 outputs.tables (paper: The paper presents eight main numbered regression tables and five main / card: Card outputs.tables lists two table records (t1, t2) built with the es); aer_112_10_8 outputs (paper: The paper contains four numbered main tables and ten main figures repo / card: The card's outputs.tables and outputs.figures arrays are both empty.) |
| outputs | agree | 2 | aer_114_11_1 outputs.tables (paper: Six numbered tables (Table 1 first stage/balance, Table 2 village amen / card: outputs.tables lists t1-t5 with captions matching Tables 1, 2, 3, and ); restud_2025_restud_rdae108 outputs.tables (paper: Three main tables (Tables 1-3) and seven main figures, plus lettered a / card: Tables t1-t3 exported with texsave from scripts named for Tables 1-3; ) |
| outputs | unknown | 1 | jpe_2026_740226 outputs.tables (paper: Presents six main numbered tables and eleven main numbered figures in  / card: Records one table and two figures as observed outputs, reflecting a pa) |
| outputs | disagree | 1 | restud_2026_restud_rdag071 outputs (paper: Three main tables and twelve figures plus appendix A/B figures and tab / card: tables=1 figures=0) |
| robustness | paper_only | 8 | aer_112_10_8 robustness (paper: The paper reports a dedicated robustness table re-estimating the full  / card: The card's robustness array is empty.); aer_114_11_1 robustness (paper: Section IV.E and the online appendix describe alternative bandwidths,  / card: the card's top-level robustness array is empty; these checks are not c) |
| robustness | agree | 2 | aer_110_2_5 robustness[0] (paper: A footnote states that results throughout the paper are robust to band / card: Robustness entry records type=alt_bandwidth, description 'Bandwidth se); restud_90_1_3 s2 (paper: Alternative polynomial orders in the running variable (Supplementary F / card: s2 and s3 re-run 2SLS with x_poly4 and x_poly3.) |
| robustness | disagree | 1 | jpe_2026_740226 robustness[0] (paper: States that a bandwidth-sensitivity appendix shows the main RD coeffic / card: Records only a different bandwidth-related practice, holding the bandw) |
| sample | agree | 5 | aer_114_11_1 s4.sample (paper: As one of several checks that another program does not use the same th / card: s4.sample = noncompliant_district_1995==0 and s5.sample = noncompliant); qje_2026_qje_qjaf045 specifications.s1.formula_or_call (paper: Core sample restricted to the eleven states of the former Confederacy  / card: All extracted specifications (s1-s4) condition on South==1 in the rdro) |
| sample | paper_only | 3 | jpe_2026_740226 s1.sample (paper: Reports the size of the exam-taker population, the excluded subgroup,  / card: Leaves the sample field unrecorded for every extracted RD specificatio); restud_2026_restud_rdag037 d1 (paper: Crack-cocaine cases 1999 to 2015 with missing, range-coded, flagged an / card: No sample restrictions recorded on d1 or s1.) |
| sample | unknown | 1 | restud_90_1_3 s1 (paper: Schools with weakest first stages excluded and used as omitted categor / card: Specs restrict to mark!=1; meaning of mark not recorded.) |
| se_type | agree | 6 | aer_110_2_5 s1.se.type (paper: Clustered standard errors are used as the primary inference method; Co / card: All extracted specifications (s1, s2, s7) record se.type=cluster; no s); aer_112_10_8 s1.se (paper: The main text does not discuss standard errors or clustering for the h / card: Card specification s1 records se.type and se.cluster_level as null.) |
| se_type | paper_only | 1 | restud_2025_restud_rdae108 s1.se.type (paper: Robust standard errors and p-values from the robust confidence interva / card: s1.se.type null.) |
| se_type | unknown | 1 | restud_90_1_3 s1.se (paper: No SE type stated for the 2SLS school effects; bootstrap CIs for varia / card: se None/None on all specs.) |
| weights | agree | 4 | aer_112_10_8 s1.weights (paper: No mention of regression weights appears in the discussion of the hedo / card: Card specifications s1.weights and s2.weights are both null.); qje_2026_qje_qjaf045 specifications.s1.weights (paper: No mention of regression weights appears anywhere in the description o / card: specifications.s1/s2/s3 all record weights as null.) |
| weights | unknown | 1 | jpe_2026_740226 s1.weights (paper: Does not describe any weighting scheme for the main RD or value-added  / card: Leaves the weights field unrecorded (null) for every extracted specifi) |
| weights | paper_only | 1 | restud_90_1_3 s1.weights (paper: Percentile-centred weights used for reweighted school effects and Tabl / card: w=None on all specs.) |

## Gaps the readers reported

- (1) No discussion found of multiple-testing or joint-significance adjustment across the many outcomes and specification vari
- (1) No formal preregistration, IRB, or human-subjects/ethics statement found; the study uses only historical archival and pr
- (1) No explicit statement of code or data deposit, or a citation to a public replication package, found in the body text; on
- (1) No R-squared statistic reported in any regression table in the main text or the appendix tables read.
- (1) The bandwidth-sensitivity figure and further discussion referenced in footnote 30 sit in the online appendix, which was 
- (1) No explicit justification found in the main text for choosing the shire level (rather than municipality or another unit)
- (1) No preregistration, IRB approval, or ethics/consent statement found anywhere in the read pages.
- (1) No explicit statement in the main text of the software or optimization package used to solve and estimate the structural
- (1) No formal first-stage or weak-instrument statistic reported in the main text for the demand-concavity instrumental varia
- (1) No description in the main text of the procedure for obtaining access to the restricted Danish administrative registers;
- (1) The online appendix (referenced dozens of times, spanning lettered sections A through K) was not included in the supplie
- (1) No explicit discussion of a few-clusters problem or wild-bootstrap inference, despite some robustness specifications clu
- (1) No pre-analysis plan, IRB approval, or ethics statement is mentioned anywhere in the main text (preregistration_or_ethic
- (1) No standalone descriptive summary-statistics table appears in the main text; dependent-variable means are reported only 
- (1) Recipe card diagnostic x1 (density test) is marked not_found_in_scope even though the paper reports specific density-tes
- (1) The paper's placebo and robustness checks (Section IV.E, online appendices C-F) are not captured as discrete items in th
- (1) The Online Appendix (Appendices A-J), referenced dozens of times for supplementary figures, tables and detailed derivati
- (1) No explicit statement of a clustering level or a rationale for the chosen standard-error type beyond citing the RD comma
- (1) No weak-instrument statistic (such as an F-statistic) is reported for the fuzzy RD/IV first stage beyond the first-stage
- (1) No discussion of multiple-hypothesis-testing correction despite many outcomes being estimated across six main tables and
- (1) No preregistration or pre-analysis plan is mentioned; only institutional review board approval is stated in the acknowle
- (1) The online appendices (A-D) referenced throughout for additional diagnostics, robustness checks, and heterogeneity resul
- (1) No explicit statement of the statistical software version or a full list of packages used beyond the named RD and densit
- (1) No preregistration, pre-analysis plan, IRB approval or ethics statement is mentioned anywhere in the text; the study rel
- (1) No explicit correction for multiple hypothesis testing is described despite the paper reporting results across many tabl
- (1) No summary-statistics table for the sample variables appears in the main text; it is deferred entirely to the online app
- (1) No R-squared or other overall model-fit statistic is reported in any regression table, consistent with the nonparametric
- (1) The paper's Online Appendix, referenced dozens of times for additional tables, figures and robustness checks, is a separ
- (1) No stated rationale for the baseline choice of unclustered robust RD standard errors; clustering appears only as a footn
- (1) No software or package names in the main text (rdrobust and rddensity appear only in the code).

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
