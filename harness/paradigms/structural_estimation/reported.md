# Reported practice: `structural_estimation` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 14 paper notes (12 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | AER: 5, ReStud: 4, JPE: 3, Econometrica: 1, QJE: 1 |
| year | 2018: 1, 2019: 1, 2021: 1, 2022: 2, 2023: 2, 2025: 5, 2026: 2 |
| papers with at least one observation in category | magnitude_interpretation: 11, mechanism_evidence: 10, presentation_convention: 10, diagnostic_reported: 10, writing_structure: 9, variable_construction: 9, robustness_reported: 9, replication_statement: 9, data_access: 8, limitation_stated: 8, specification_reporting: 8, sample_construction: 7, inference_justification: 7, external_validity: 6, other: 5, design_statement: 5, heterogeneity_reported: 4 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_108_4_3 | AER | 2018 | main_text | no | e1a6e542f5d2 |
| aer_109_7_8 | AER | 2019 | main_text | no | 285490849842 |
| aer_111_4_3 | AER | 2021 | full | yes | 500f457d1b91 |
| aer_112_10_8 | AER | 2022 | full | yes | df1a1baa7d3d |
| aer_112_5_9 | AER | 2022 | full | yes | c70eb5a02596 |
| ecta_2025_ecta22303 | Econometrica | 2025 | full | yes | e8342e263d9f |
| jpe_2025_735509 | JPE | 2025 | full | yes | 8fe8171adef6 |
| jpe_2025_736209 | JPE | 2025 | full | yes | d917e492e66f |
| jpe_2026_740222 | JPE | 2026 | full | yes | 98c23fe93722 |
| qje_140_1_4 | QJE | 2025 | partial | yes | 793bd3a24ebb |
| restud_2025_restud_rdae072 | ReStud | 2025 | full | yes | b59e78835737 |
| restud_2026_restud_rdag013 | ReStud | 2026 | full | yes | b781b6e5a7dc |
| restud_90_2_4 | ReStud | 2023 | full | yes | fcf9f1232ea0 |
| restud_90_5_11 | ReStud | 2023 | full | yes | b9f9dec1a4cb |

## Practices by category and tag


### data_access (papers with this category: 8/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 5 | 36% | aer_108_4_3 p.17-17 Section IIB: Describes the analysis data as coming from linked Swedish government administrative registers covering unemplo; aer_112_10_8 p.14-16 Section II; References entry for Statistics Denmark: The data section labels its main sources as government administrative registers, with a single private commerc |
| `commercial` | 2 | 14% | aer_112_10_8 p.14-16 Section II; References entry for Statistics Denmark: The data section labels its main sources as government administrative registers, with a single private commerc; jpe_2025_735509 p.11-11 Section II.B, footnote: Supplements the hand-collected subsidy dataset with commercial financial-database records to fill in firm indu |
| `data_access_procedure_described` | 2 | 14% | aer_112_10_8 p.14-16 Section II; References entry for Statistics Denmark: The data section labels its main sources as government administrative registers, with a single private commerc; jpe_2025_735509 p.12-12 Section II.B, footnote: Describes a manual data-access procedure for state budget and tax-expenditure documents, stating that when suc |
| `data_restricted` | 2 | 14% | aer_108_4_3 p.17-17 Section IIB: Describes the analysis data as coming from linked Swedish government administrative registers covering unemplo; ecta_2025_ecta22303 p.7-8 Section 2.2: The underlying data are described as administrative program records assembled during loan underwriting, includ |
| `public_use` | 2 | 14% | restud_90_2_4 p.7-9 Section 4, footnotes 9 and 10: Main adoption data come from public yearbooks and an archived web database; auxiliary data from a national age; restud_90_5_11 p.14-15 footnote 14, Section 3: Main data are public-use CPS microdata from IPUMS with a dataset citation; the ACS is used for a self-replicat |
| `linked_records` | 1 | 7% | jpe_2025_735509 p.11-11 Section II.B, footnote: Supplements the hand-collected subsidy dataset with commercial financial-database records to fill in firm indu |
| `online_appendix_not_available` | 1 | 7% | aer_112_10_8 p.14-16 Section II; References entry for Statistics Denmark: The data section labels its main sources as government administrative registers, with a single private commerc |
| `other:regulator_administrative_data` | 1 | 7% | restud_2026_restud_rdag013 p.8-9 Section 2.3: Data come from the state environmental regulator's administrative records (identifiers, scores, inspections, v |
| `survey_collected` | 1 | 7% | restud_90_5_11 p.14-15 footnote 14, Section 3: Main data are public-use CPS microdata from IPUMS with a dataset citation; the ACS is used for a self-replicat |
| `web_scraped` | 1 | 7% | restud_90_2_4 p.7-9 Section 4, footnotes 9 and 10: Main adoption data come from public yearbooks and an archived web database; auxiliary data from a national age |

### design_statement (papers with this category: 5/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 5 | 36% | aer_112_10_8 p.6-7 Section I, model setup: The paper states its estimand as structural preference parameters (reference dependence, loss aversion, financ; jpe_2025_735509 p.1-4 Abstract; Introduction: Frames identification as a private-value open-outcry ascending (English) scoring auction in which states bid s |
| `estimand_named` | 4 | 29% | aer_112_10_8 p.6-7 Section I, model setup: The paper states its estimand as structural preference parameters (reference dependence, loss aversion, financ; jpe_2025_735509 p.1-4 Abstract; Introduction: Frames identification as a private-value open-outcry ascending (English) scoring auction in which states bid s |
| `identifying_assumption_explicit` | 4 | 29% | aer_112_10_8 p.9-23 Section I.B footnote; Section III.C Fact 3: The reference point for loss aversion is assumed to equal the nominal original purchase price throughout, an a; jpe_2025_735509 p.27-33 Section IV, Assumptions 1-6: States a numbered sequence of formal assumptions underlying identification, covering truthful revelation of co |
| `threats_discussed` | 4 | 29% | aer_112_10_8 p.3-5 Introduction: The introduction explicitly names three confounds that could generate a spurious loss-aversion pattern in list; jpe_2025_735509 p.29-29 Section IV.A, Assumption 4 discussion: Explicitly flags that the independence assumption needed for consistent profit-parameter estimates should not  |
| `identification_caveat` | 1 | 7% | restud_2026_restud_rdag013 p.12-12 Section 3.3: After the descriptive deterrence regressions the authors state that a causal relationship cannot be ascertaine |
| `in_main_text` | 1 | 7% | restud_2026_restud_rdag013 p.2-4 Section 1 (Introduction): The paper states its question as the effectiveness of linked regulation and answers it by building and estimat |
| `instrument_exclusion_argued` | 1 | 7% | restud_90_2_4 p.25-26 Section 6.4, footnote 29: Endogeneity of digital movie availability is handled in two steps following Gowrisankaran, Park and Rysman: ti |

### diagnostic_reported (papers with this category: 10/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 5 | 36% | jpe_2025_735509 p.41-41 Section V.D; online appendix table: Reports a state-identity fit check in an appendix table comparing simulated versus observed shares of firms wi; jpe_2026_740222 p.34-34 Section V.B, referencing an online-appendix figure: For the structural heat-rate-curve comparison, a bootstrap-based confidence band around the difference between |
| `in_main_text` | 5 | 36% | aer_111_4_3 p.33-34 Section V.C, Figure 8: The paper compares the shape of the pooled empirical retirement-age density around statutory ages against the ; jpe_2025_735509 p.37-38 Figure 4: Reports a scatterplot of observed runner-up subsidy offers against predicted runner-up valuations, together wi |
| `in_footnote` | 3 | 21% | aer_112_10_8 p.23-24 Section III.E footnote: A footnote checks that property and household observables, including renovation expenditures, are balanced and; aer_112_5_9 p.21-21 footnote 25: A joint F-test of whether the transparent-IV experience profile is flat, and a parallel test for the hidden-IV |
| `online_appendix_not_available` | 2 | 14% | aer_112_10_8 p.23-24 Section III.E footnote: A footnote checks that property and household observables, including renovation expenditures, are balanced and; jpe_2026_740222 p.34-34 Section V.B, referencing an online-appendix figure: For the structural heat-rate-curve comparison, a bootstrap-based confidence band around the difference between |
| `balance_table` | 1 | 7% | jpe_2025_735509 p.31-31 Section IV.B, referencing online appendix: Cites an appendix exercise comparing location characteristics of winning, runner-up (bidding), and non-partici |
| `density_test` | 1 | 7% | aer_111_4_3 p.33-34 Section V.C, Figure 8: The paper compares the shape of the pooled empirical retirement-age density around statutory ages against the  |
| `other:constant_returns_test` | 1 | 7% | aer_112_5_9 p.21-21 footnote 25: A joint F-test of whether the transparent-IV experience profile is flat, and a parallel test for the hidden-IV |
| `other:first_stage_estimates_in_appendix` | 1 | 7% | restud_2026_restud_rdag013 p.22-22 Section 6: First-stage (offline) estimates are relegated to an online appendix table while second- and third-stage estima |
| `other:heterogeneous_responsiveness_check` | 1 | 7% | restud_2026_restud_rdag013 p.11-18 Sections 3.3 and 5.1.1: An appendix table is cited to support a modelling assumption (increasing differences) by showing that high-vio |
| `other:likelihood_ratio_test` | 1 | 7% | restud_90_2_4 p.11-11 Section 4, Table 3 discussion: A likelihood ratio test comparing the preferred policy function against one including competitors' digital ado |
| `other:model_fit` | 1 | 7% | restud_90_2_4 p.27-27 Section 6.5.1, Supplementary Appendix C.4: Model fit of the first-stage policy function (predicted versus actual digital screen shares) is reported in th |
| `other:model_fit_by_subgroup` | 1 | 7% | restud_90_5_11 p.26-26 Section 6.4, footnote 29: Model-predicted employment responses by mobility quartile are compared with estimated responses and a test of  |
| `other:model_fit_check` | 1 | 7% | jpe_2025_735509 p.37-38 Figure 4: Reports a scatterplot of observed runner-up subsidy offers against predicted runner-up valuations, together wi |
| `other:model_fit_moments_table` | 1 | 7% | restud_2026_restud_rdag013 p.22-23 Table 5, Figure 4, Section 6.1: Model fit is assessed by a table listing each estimation moment with its simulated and empirical value, follow |
| `other:moment_matching_table` | 1 | 7% | restud_2025_restud_rdae072 p.31-32 Section 6.4, Table 9: Model fit is diagnosed by backing out structural shocks with the Kalman smoother, feeding a single shock type  |
| `other:non_targeted_moment_check` | 1 | 7% | qje_140_1_4 p.53-55 Section IV.B.2, Figures VI-VIII: The model-versus-data validation exercise reports moments that were not calibration targets as an additional d |
| `other:reduced_form_support` | 1 | 7% | restud_90_2_4 p.11-25 Supplementary Appendix B: Reduced-form evidence that gradual adoption is driven by rising digital availability, and a discussion of inst |
| `other:rkd_style_balance_check` | 1 | 7% | aer_112_10_8 p.23-24 Section III.E footnote: A footnote checks that property and household observables, including renovation expenditures, are balanced and |
| `other:simulation_check` | 1 | 7% | restud_90_2_4 p.19-19 Section 6.1: The finite horizon length is validated by simulating industry trajectories and reporting the share reaching th |
| `overid_test` | 1 | 7% | restud_90_5_11 p.31-31 footnote 34, Appendix Table A15: For the structural model, an appendix robustness check calibrates two more parameters so the system is overide |

### external_validity (papers with this category: 6/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `site_specific` | 5 | 36% | aer_112_10_8 p.16-38 Section II.C; Section V.C: Findings are framed throughout in terms of the specific Danish mortgage-market rules, down-payment regulation ; ecta_2025_ecta22303 p.5-6 Section 1: The authors explicitly discuss that their sample of households who recently experienced a disaster is a distin |
| `scaling_discussed` | 4 | 29% | ecta_2025_ecta22303 p.37-37 Section 6, footnote 36: The conclusion explicitly cautions that the specific magnitudes of collateral aversion may not generalize acro; jpe_2025_735509 p.43-43 Section VI.B, footnote: States that its estimated responsiveness to subsidies pertains to a sample of unusually large discretionary de |
| `time_period_specific` | 2 | 14% | aer_112_10_8 p.16-38 Section II.C; Section V.C: Findings are framed throughout in terms of the specific Danish mortgage-market rules, down-payment regulation ; jpe_2025_735509 p.42-42 Section VI.A: Frames the counterfactual analysis as specific to the sample period's set of observed deals and location funda |
| `other:mechanism_decomposition_for_portability` | 1 | 7% | restud_2026_restud_rdag013 p.2-5 Sections 1 and 1.1: External validity is argued through the mechanism decomposition: which channel dominates is said to determine  |

### heterogeneity_reported (papers with this category: 4/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `split_sample` | 4 | 29% | aer_112_10_8 p.36-37 Section V.B; Figure 10: Interaction between financial constraints and behavioral responses is explored graphically and with a formal r; jpe_2025_735509 p.34-34 Section V.A: Estimates the profit and valuation model separately for manufacturing and trade/services firms throughout, rat |
| `interaction` | 2 | 14% | aer_112_10_8 p.36-37 Section V.B; Figure 10: Interaction between financial constraints and behavioral responses is explored graphically and with a formal r; restud_90_2_4 p.25-28 Section 6.3, Table 5: Heterogeneity in profits per digital screen enters through the parameterization itself (size, art house, compe |
| `mechanism_motivated` | 2 | 14% | restud_2026_restud_rdag013 p.25-26 Table 6 and Section 7.3.1: Counterfactual results are reported separately for multi-plant firms, single-plant firms and all firms, with t; restud_90_2_4 p.25-28 Section 6.3, Table 5: Heterogeneity in profits per digital screen enters through the parameterization itself (size, art house, compe |
| `exploratory_labelled` | 1 | 7% | aer_112_10_8 p.36-37 Section V.B; Figure 10: Interaction between financial constraints and behavioral responses is explored graphically and with a formal r |
| `quantile` | 1 | 7% | restud_2026_restud_rdag013 p.26-27 Section 7.3.5 and Figure 5: Targeting heterogeneity is shown by a LOWESS-smoothed plot of the change in inspection probability across plan |

### inference_justification (papers with this category: 7/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_justification_found` | 3 | 21% | aer_112_10_8 p.29-29 Section IV.C, Estimation: Standard errors for the structural parameters are computed by re-estimating the entire pipeline, hedonic model; jpe_2025_735509 p.34-36 Section V.A; Tables 3-4: Does not discuss the source or properties of the standard errors reported alongside the structural profit and  |
| `in_appendix` | 1 | 7% | restud_2025_restud_rdae072 p.30-31 Section 6.2-6.3, footnote 41: For the structural model, parameters not pinned down by calibration targets are given posterior distributions  |
| `in_footnote` | 1 | 7% | restud_2025_restud_rdae072 p.7-9 Table 1 notes, Table 3 notes, footnote 11: Uncertainty for the cyclical correlation coefficients in the descriptive tables is reported as estimated stand |
| `in_main_text` | 1 | 7% | restud_2025_restud_rdae072 p.7-9 Table 1 notes, Table 3 notes, footnote 11: Uncertainty for the cyclical correlation coefficients in the descriptive tables is reported as estimated stand |
| `other:bayesian_posterior` | 1 | 7% | restud_2025_restud_rdae072 p.30-31 Section 6.2-6.3, footnote 41: For the structural model, parameters not pinned down by calibration targets are given posterior distributions  |
| `other:block_bootstrap` | 1 | 7% | aer_109_7_8 p.37-38 Section VIIB footnote, Table 11 notes: For the structural model's welfare and counterfactual estimates, inference is performed by re-estimating the f |
| `other:bootstrap_at_firm_level` | 1 | 7% | restud_2026_restud_rdag013 p.22-22 Table 4 notes: Standard errors for the structural parameters are obtained by a bootstrap that resamples with replacement at t |
| `other:bootstrap_reestimation` | 1 | 7% | aer_112_10_8 p.29-29 Section IV.C, Estimation: Standard errors for the structural parameters are computed by re-estimating the entire pipeline, hedonic model |
| `other:bootstrap_se` | 1 | 7% | qje_140_1_4 p.48-48 Table IV notes: Standard errors for the simulated-method-of-moments calibrated parameters are described as computed by a boots |
| `other:parametric_bootstrap` | 1 | 7% | restud_90_2_4 p.22-22 Section 6.1.2, Supplementary Appendix C.2: Standard errors for structural parameters use a parametric bootstrap; the authors explain that resampling mark |
| `other:varhac_se_for_correlations` | 1 | 7% | restud_2025_restud_rdae072 p.7-9 Table 1 notes, Table 3 notes, footnote 11: Uncertainty for the cyclical correlation coefficients in the descriptive tables is reported as estimated stand |

### limitation_stated (papers with this category: 8/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `interpretation_caveat` | 8 | 57% | aer_109_7_8 p.39-40 Conclusion, first caveat: The authors state that their structural welfare measure captures only the cash-equivalent transfer value of a ; aer_112_10_8 p.36-39 Section V.B; Conclusion: The authors state plainly that their model cannot rationalize the finding that financially constrained sellers |
| `identification_caveat` | 4 | 29% | aer_112_10_8 p.36-39 Section V.B; Conclusion: The authors state plainly that their model cannot rationalize the finding that financially constrained sellers; jpe_2025_735509 p.42-42 Section VI.A, footnote: States that the counterfactual is a partial-equilibrium exercise that holds each state's corporate tax rate an |
| `data_coverage` | 2 | 14% | jpe_2025_735509 p.13-13 Section II.B, Limitations of the data: States that in-kind components of subsidy deals, such as land grants or regulatory exemptions, are valued usin; qje_140_1_4 p.47-47 Section IV.A, footnote: The paper flags that the quantitative results depend on the calibration assumption that the EU and United Stat |
| `in_footnote` | 2 | 14% | restud_2025_restud_rdae072 p.1-1 footnote 1, Figure 1: The downward trend in the aggregate utilization series is acknowledged in the first footnote; the author state; restud_2026_restud_rdag013 p.15-15 Footnote 14: The authors note that ruling out production shifting makes their linked-regulation conclusions conservative, i |
| `external_validity` | 1 | 7% | qje_140_1_4 p.47-47 Section IV.A, footnote: The paper flags that the quantitative results depend on the calibration assumption that the EU and United Stat |
| `measurement` | 1 | 7% | jpe_2025_735509 p.13-13 Section II.B, Limitations of the data: States that in-kind components of subsidy deals, such as land grants or regulatory exemptions, are valued usin |
| `other:first_order_approximation` | 1 | 7% | restud_90_5_11 p.12-12 Section 2.4 after Theorem 1: The welfare formula is flagged as first-order and reliant on the envelope theorem; the authors state when a fi |
| `other:scope_limitation` | 1 | 7% | aer_112_10_8 p.24-29 Section III.D; Section IV.B: The unconditional level of the annual listing propensity is explicitly described as beyond the scope of what t |
| `selection` | 1 | 7% | jpe_2025_735509 p.14-14 Section II.B, Limitations of the data: Notes that because the dataset only contains firms observed receiving a discretionary subsidy, location decisi |

### magnitude_interpretation (papers with this category: 11/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 9 | 64% | aer_109_7_8 p.34-34 Section VIIB, Parameter Estimates and Model Fit: Estimated labor supply elasticities from the structural model are benchmarked against ranges reported in a cit; aer_112_10_8 p.1-33 Abstract; Section IV.D: Reference dependence and loss aversion are interpreted in relative terms, as the share of utility that realize |
| `back_of_envelope` | 7 | 50% | aer_109_7_8 p.36-37 Section VIIB, Household Valuation of DI Receipt: Willingness to pay for a DI allowance is expressed per dollar of induced fiscal cost and as a share of househo; aer_112_10_8 p.30-31 Section IV.D, discussion of model 6: The moving-shock and search-cost parameters are translated into externally interpretable units, an annualized  |
| `precision_discussed` | 5 | 36% | aer_111_4_3 p.35-35 Section VI.A: The authors explicitly note when an estimated structural parameter is precisely estimated relative to the othe; aer_112_10_8 p.33-33 Section IV.D, end: Overall structural fit is summarized with a single average prediction-error statistic across all matched momen |
| `monetary_terms` | 4 | 29% | aer_109_7_8 p.36-37 Section VIIB, Household Valuation of DI Receipt: Willingness to pay for a DI allowance is expressed per dollar of induced fiscal cost and as a share of househo; aer_112_10_8 p.30-31 Section IV.D, discussion of model 6: The moving-shock and search-cost parameters are translated into externally interpretable units, an annualized  |
| `relative_to_mean` | 3 | 21% | qje_140_1_4 p.59-67 Section IV.C: Quantitative policy counterfactuals are reported both as a percentage change relative to the baseline balanced; restud_2026_restud_rdag013 p.23-25 Section 7.1 and Table 6: Because social costs are identified only up to scale, counterfactual effectiveness is reported as percentage c |
| `cost_benefit` | 1 | 7% | aer_109_7_8 p.36-37 Section VIIB, Household Valuation of DI Receipt: Willingness to pay for a DI allowance is expressed per dollar of induced fiscal cost and as a share of househo |
| `other:dual_metric_triangulation` | 1 | 7% | aer_112_5_9 p.25-26 Section IVB: The gap between private and social returns, interpreted as the signaling value of education, is computed two d |
| `other:model_fit_summary` | 1 | 7% | aer_112_10_8 p.33-33 Section IV.D, end: Overall structural fit is summarized with a single average prediction-error statistic across all matched momen |
| `other:percent_change_from_baseline` | 1 | 7% | jpe_2025_735509 p.45-45 Table 5; Section VI.C: Expresses the headline counterfactual result as a percentage change in aggregate welfare relative to a no-subs |
| `other:percentage_change_due_to_scale_normalisation` | 1 | 7% | restud_2026_restud_rdag013 p.23-25 Section 7.1 and Table 6: Because social costs are identified only up to scale, counterfactual effectiveness is reported as percentage c |
| `other:relative_utility_share` | 1 | 7% | aer_112_10_8 p.1-33 Abstract; Section IV.D: Reference dependence and loss aversion are interpreted in relative terms, as the share of utility that realize |
| `other:time_to_adoption` | 1 | 7% | restud_90_2_4 p.31-32 Section 7.3, Figure 5: Adoption delay is summarized as differences in years to reach fixed adoption milestones across scenarios, plot |

### mechanism_evidence (papers with this category: 10/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `model_guided` | 8 | 57% | aer_108_4_3 p.30-30 Section VB, Proposition 2: Uses a formal proposition characterizing how moral hazard cost and consumption smoothing gain evolve over the ; aer_109_7_8 p.37-38 Section VIIB, Table 11: Structural counterfactual simulations that shut down spousal labor supply adjustment, savings, or reapplicatio |
| `intermediate_outcomes` | 2 | 14% | aer_112_10_8 p.22-23 Section III.B; Figure 5: Regional variation in demand concavity is linked to the homogeneity of the local housing stock as an intermedi; qje_140_1_4 p.41-43 Section III.B.3, Table II: The change in co-inventors' share of local collaborators after a colleague emigrates is treated as direct evid |
| `ruled_out_alternatives` | 2 | 14% | ecta_2025_ecta22303 p.28-29 Section 5.1.2, Figure 10: Borrowers with no remaining financial stake in their home (already underwater on an existing mortgage) are exa; restud_90_2_4 p.28-31 Section 7.1 to 7.3, Supplementary Appendix D.3: The decomposition of surplus loss into downstream externalities and upstream coordination failure is produced  |
| `heterogeneity_as_mechanism` | 1 | 7% | ecta_2025_ecta22303 p.28-29 Section 5.1.2, Figure 10: Borrowers with no remaining financial stake in their home (already underwater on an existing mortgage) are exa |
| `in_appendix` | 1 | 7% | jpe_2025_736209 p.33-33 Section V.A, model description; Appendix D: Builds a simple structural model, detailed in an appendix, that separates a wealth-effect channel from informa |
| `other:counterfactual_decomposition` | 1 | 7% | restud_2026_restud_rdag013 p.24-24 Section 7.2: Mechanisms are separated by a numerical decomposition: one channel is isolated by holding the score-to-action  |
| `other:valuation_correlates` | 1 | 7% | jpe_2025_735509 p.37-37 Section V.A, Tables 3-4 discussion: Reports the estimated correlates of the runner-up valuation function, such as local unemployment and income pe |
| `suggestive_labelled` | 1 | 7% | jpe_2025_735509 p.3-47 Introduction; Section VI.D: Presents the association between a governor facing reelection and a higher estimated willingness to pay for fi |

### other (papers with this category: 5/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:software_not_named` | 2 | 14% | aer_109_7_8 p.34-34 Section VIIA, footnote on estimation procedure: The paper does not name the statistical or numerical software used for estimation anywhere in the main text; o; restud_90_5_11 p.1-34 whole main text: No statistical software or packages are named in the main text. |
| `in_main_text` | 1 | 7% | restud_2025_restud_rdae072 p.30-30 Section 6.2: To reduce the estimation burden, a set of steady-state targets is imposed throughout Bayesian estimation, so t |
| `other:calibration_from_statute` | 1 | 7% | restud_2026_restud_rdag013 p.19-20 Sections 5.1.4, 5.2 and footnote 19: Several model parameters are calibrated directly from the regulator's published rules (penalty escalations, sc |
| `other:calibration_within_estimation` | 1 | 7% | restud_2025_restud_rdae072 p.30-30 Section 6.2: To reduce the estimation burden, a set of steady-state targets is imposed throughout Bayesian estimation, so t |
| `other:identification_of_counterfactuals` | 1 | 7% | restud_90_2_4 p.31-31 footnote 34: A footnote cites results establishing that subsidy counterfactuals are identified under payoff normalizations  |
| `other:multi_step_estimation_described` | 1 | 7% | restud_2026_restud_rdag013 p.20-20 Section 5.2: Estimation is laid out as three explicit steps (offline calibration, simulated method of moments for firms wit |

### presentation_convention (papers with this category: 10/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `summary_stats_table` | 7 | 50% | aer_108_4_3 p.45-45 Table 1: Presents summary statistics using the mean and three percentiles of each variable's distribution rather than m; ecta_2025_ecta22303 p.8-8 Table I: A detailed summary-statistics table reporting the mean, standard deviation, and several percentiles for key bo |
| `no_stars` | 4 | 29% | aer_109_7_8 p.16-38 Tables 3-11 generally: Result tables do not use significance stars; instead they report standard errors in parentheses and, for sever; aer_112_10_8 p.27-35 Tables 2 and 3: The structural-parameter tables report standard errors in parentheses beneath each point estimate together wit |
| `notes_state_se` | 4 | 29% | aer_109_7_8 p.16-38 Tables 3-11 generally: Result tables do not use significance stars; instead they report standard errors in parentheses and, for sever; aer_112_10_8 p.18-26 Figures 2, 4, 6, 7: Figures throughout use binned-average plots with polynomial or nonparametric smoothers overlaid, and several e |
| `map` | 3 | 21% | ecta_2025_ecta22303 p.7-7 Section 2.1, Figure 2: A choropleth-style map of participating ZIP codes is used to describe the geographic coverage of the sample ra; jpe_2025_735509 p.15-44 Figure 1; Figure 7: Uses choropleth-style United States maps to show the geographic distribution of subsidy giving and, separately |
| `notes_state_sample` | 3 | 21% | aer_109_7_8 p.16-38 Tables 3-11 generally: Result tables do not use significance stars; instead they report standard errors in parentheses and, for sever; ecta_2025_ecta22303 p.8-8 Table I: A detailed summary-statistics table reporting the mean, standard deviation, and several percentiles for key bo |
| `appendix_tables_numbered_a` | 2 | 14% | restud_2026_restud_rdag013 p.7-28 various: Online appendix tables are referenced with an A- prefix and appendix sections by number throughout the main te; restud_90_5_11 p.3-33 Figures 1 to 4, Appendix Tables A1, A4: Figures include maps of state policy variation for example occupations, coefficient plots with confidence band |
| `binscatter` | 2 | 14% | aer_112_10_8 p.18-26 Figures 2, 4, 6, 7: Figures throughout use binned-average plots with polynomial or nonparametric smoothers overlaid, and several e; jpe_2025_735509 p.29-30 Figure 3: Uses binned scatterplots that control for other covariates as the main graphical device for illustrating the i |
| `coefficient_plot` | 2 | 14% | qje_140_1_4 p.53-55 Figures VI, VII, VIII: Model-fit figures in the quantitative section adopt one consistent visual convention, overlaying data-based es; restud_90_5_11 p.3-33 Figures 1 to 4, Appendix Tables A1, A4: Figures include maps of state policy variation for example occupations, coefficient plots with confidence band |
| `in_main_text` | 2 | 14% | jpe_2025_735509 p.29-30 Figure 3: Uses binned scatterplots that control for other covariates as the main graphical device for illustrating the i; restud_2025_restud_rdae072 p.7-8 Tables 1-3: Descriptive fact tables list region and sector rows with start dates, averages, standard deviations, shares of |
| `raw_data_plot` | 2 | 14% | qje_140_1_4 p.53-55 Figures VI, VII, VIII: Model-fit figures in the quantitative section adopt one consistent visual convention, overlaying data-based es; restud_90_2_4 p.8-11 Figures 1 and 2: Descriptive figures show observation dates with the industry adoption share, the cost time series, and a decom |
| `appendix_heavy` | 1 | 7% | aer_112_10_8 p.1-43 Throughout: The paper relies heavily on a large lettered online appendix, cited dozens of times throughout for additional  |
| `online_appendix_not_available` | 1 | 7% | aer_112_10_8 p.1-43 Throughout: The paper relies heavily on a large lettered online appendix, cited dozens of times throughout for additional  |
| `other:counterfactual_path_figure` | 1 | 7% | restud_90_2_4 p.32-34 Figure 5, Tables 6 to 8: Counterfactual results are shown as multi-panel diffusion path figures (screens and movies) under benchmarks a |
| `other:equation_terms_annotated` | 1 | 7% | restud_2026_restud_rdag013 p.14-15 Equations (3) and (5): Key equations are annotated with under-braces labelling each economic component (flow benefit, inspection, exp |
| `other:model_fit_plot` | 1 | 7% | aer_109_7_8 p.35-36 Figures 5 and 6: Model fit is presented visually by overlaying observed and simulated series, for spousal earnings dynamics ove |
| `other:state_variable_table` | 1 | 7% | restud_90_2_4 p.18-18 Table 4: A table lists every state variable of the model with a description and whether it is observed, estimated or un |
| `other:timing_diagram` | 1 | 7% | restud_2026_restud_rdag013 p.13-14 Section 4.1.4 and Figure 3: The model timing is summarised in a numbered timeline and a timing diagram figure. |
| `stars_used` | 1 | 7% | restud_90_5_11 p.20-30 Tables 2 to 5 notes: Tables use three-level significance stars defined in notes; notes state the fixed effects, cluster level, samp |

### replication_statement (papers with this category: 9/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 8 | 57% | aer_109_7_8 p.1-42 Title-page footnote and reference list: The paper follows the journal's standard practice of directing readers to the article's online page for additi; aer_112_10_8 p.1-41 Page 1 footnote; References: A front-matter footnote directs readers to the article's online DOI landing page for additional materials and  |
| `data_public` | 5 | 36% | jpe_2025_735509 p.49-49 Data Availability: Includes a dedicated data-availability statement citing a Harvard Dataverse replication package containing the; qje_140_1_4 p.69-69 Data Availability statement: A dedicated data-availability statement at the end of the article names the public repository and identifier w |
| `code_public` | 4 | 29% | jpe_2025_735509 p.49-49 Data Availability: Includes a dedicated data-availability statement citing a Harvard Dataverse replication package containing the; restud_2026_restud_rdag013 p.28-28 Data Availability: A Data Availability paragraph states that data and code are on Zenodo with a DOI. |
| `data_access_procedure_described` | 2 | 14% | aer_109_7_8 p.1-42 Title-page footnote and reference list: The paper follows the journal's standard practice of directing readers to the article's online page for additi; ecta_2025_ecta22303 p.41-41 Back matter, replication statement: A replication-package DOI is given in the back matter, and the article states that the authors were granted an |
| `in_footnote` | 2 | 14% | aer_112_10_8 p.1-41 Page 1 footnote; References: A front-matter footnote directs readers to the article's online DOI landing page for additional materials and ; restud_2025_restud_rdae072 p.30-30 footnote 41: The estimation platform (Dynare) and the solution method (log-linearization around the steady state) are named |
| `software_named` | 2 | 14% | qje_140_1_4 p.33-33 Section III.A.1: A commercial third-party software product is named and described for one specific analysis step, inferring an ; restud_2025_restud_rdae072 p.30-30 footnote 41: The estimation platform (Dynare) and the solution method (log-linearization around the steady state) are named |
| `data_restricted` | 1 | 7% | ecta_2025_ecta22303 p.41-41 Back matter, replication statement: A replication-package DOI is given in the back matter, and the article states that the authors were granted an |
| `online_appendix_not_available` | 1 | 7% | qje_140_1_4 p.69-69 Supplementary Material statement: The article repeatedly refers throughout the main text to an Online Appendix published separately at the journ |
| `other:journal_verified_reproducibility` | 1 | 7% | ecta_2025_ecta22303 p.41-41 Back matter, replication statement: The journal states it checked the submitted code and data for the ability to generate the paper's tables and f |
| `other:software_not_named` | 1 | 7% | restud_2026_restud_rdag013 p.1-29 whole paper: No software or package is named in the main text for estimation or regressions. |

### robustness_reported (papers with this category: 9/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_specification` | 7 | 50% | aer_109_7_8 p.30-30 Section VIIA, online Appendix Table A10: The paper states that neither the welfare estimates nor the counterfactual results are materially affected by ; aer_112_10_8 p.33-36 Table 3; Section V.A: A dedicated table re-estimates the complete structural parameter vector under three alternative hedonic fair-v |
| `in_appendix` | 7 | 50% | aer_109_7_8 p.30-30 Section VIIA, online Appendix Table A10: The paper states that neither the welfare estimates nor the counterfactual results are materially affected by ; aer_111_4_3 p.35-35 text reference to online Appendix Table A7: Robustness of the structural reference-dependence parameter estimates to alternative functional forms and to e |
| `in_main_text` | 5 | 36% | aer_109_7_8 p.37-38 Table 11: A dedicated counterfactual table varies three model assumptions in turn, spousal labor supply adjustment, avai; aer_112_10_8 p.33-36 Table 3; Section V.A: A dedicated table re-estimates the complete structural parameter vector under three alternative hedonic fair-v |
| `summarized_in_one_table` | 4 | 29% | aer_109_7_8 p.37-38 Table 11: A dedicated counterfactual table varies three model assumptions in turn, spousal labor supply adjustment, avai; aer_112_10_8 p.33-36 Table 3; Section V.A: A dedicated table re-estimates the complete structural parameter vector under three alternative hedonic fair-v |
| `sensitivity_bounds` | 3 | 21% | aer_109_7_8 p.37-38 Table 11: A dedicated counterfactual table varies three model assumptions in turn, spousal labor supply adjustment, avai; ecta_2025_ecta22303 p.32-33 Table V: The structural home-attachment estimate's sensitivity to several assumed parameters (risk aversion, outside bo |
| `alt_estimator` | 2 | 14% | jpe_2025_735509 p.46-46 Section VI.C, referencing appendix table K.4: Reports a robustness estimation that drops the random coefficient from the profit function and instead uses an; restud_90_2_4 p.30-30 Section 7.1, Supplementary Appendix D.2: The planner benchmark obtained by random search over adoption paths is cross-checked by explicitly solving a r |
| `alt_sample` | 2 | 14% | jpe_2025_735509 p.34-35 Section V.A, footnotes: States that results are not sensitive to how ties in the runner-up assignment are broken when multiple locatio; restud_90_2_4 p.9-9 footnote 13: A footnote reports that an alternative distance-band market definition yields similar competitor counts. |
| `in_footnote` | 2 | 14% | jpe_2025_735509 p.34-35 Section V.A, footnotes: States that results are not sensitive to how ties in the runner-up assignment are broken when multiple locatio; restud_90_2_4 p.9-9 footnote 13: A footnote reports that an alternative distance-band market definition yields similar competitor counts. |
| `online_appendix_not_available` | 1 | 7% | qje_140_1_4 p.48-66 Sections IV.A, IV.C.2-3: The calibration section references a robustness exercise on the parameter governing crowding out between inven |
| `other:calibration_grid` | 1 | 7% | restud_90_5_11 p.28-31 Section 7.2, Table 5, footnote 30: Two unidentified structural parameters are calibrated from cited literature ranges and the structural table re |
| `other:simulation_based_robustness` | 1 | 7% | aer_112_10_8 p.33-34 Section V.A: A simulation exercise perturbs the model with seller-side private information about property quality that is i |
| `suggestive_labelled` | 1 | 7% | jpe_2025_735509 p.47-47 Section VI.D, referencing appendix figure: Runs a thought-experiment sensitivity exercise, explicitly labeled as not evidence-based, showing how quickly  |

### sample_construction (papers with this category: 7/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 7 | 50% | aer_108_4_3 p.17-18 Section IIB: Constructs the analysis sample by linking three administrative Swedish registers, an unemployment history regi; aer_112_10_8 p.14-16 Section II, subsections A-E: Multiple administrative registers (tax and transaction records, the housing register, mortgage data from the c |
| `sample_period_stated` | 7 | 50% | aer_108_4_3 p.16-18 Section IIA-B: States the administrative sample spans a specific multi-year period, while the household expenditure survey us; aer_112_10_8 p.14-16 Section II, subsections A-E: Multiple administrative registers (tax and transaction records, the housing register, mortgage data from the c |
| `exclusions_justified` | 6 | 43% | aer_108_4_3 p.16-16 Section IIA: Restricts the analysis sample to workers with a minimum prior employment history before layoff who contribute ; aer_112_10_8 p.16-17 Section II.E footnote: Each sample exclusion (foreclosures, zero-size properties, extreme prices, within-family and flagged-anomalous |
| `unit_of_observation_stated` | 6 | 43% | aer_108_4_3 p.16-16 Section IIA: Restricts the analysis sample to workers with a minimum prior employment history before layoff who contribute ; aer_112_10_8 p.16-17 Section II.E, Final Merged Data: The share of official sale transactions that could be matched to listings data is reported explicitly, and fin |
| `sample_size_reported_per_table` | 3 | 21% | aer_112_10_8 p.16-17 Section II.E, Final Merged Data: The share of official sale transactions that could be matched to listings data is reported explicitly, and fin; jpe_2025_735509 p.4-12 Introduction; Section II.B: States the analysis sample covers a fixed multi-year window, is restricted to deals above a minimum dollar thr |
| `in_appendix` | 2 | 14% | restud_2025_restud_rdae072 p.30-30 Section 6.2, footnote 40: The Bayesian estimation matches four detrended U.S. macro series (real consumption, real investment, real exog; restud_2026_restud_rdag013 p.9-9 Section 2.3: The small share of inspections conducted by the federal EPA rather than the state regulator is retained in the |
| `matching_or_linkage_described` | 2 | 14% | aer_112_10_8 p.14-16 Section II, subsections A-E: Multiple administrative registers (tax and transaction records, the housing register, mortgage data from the c; jpe_2025_735509 p.11-12 Section II.B, footnotes: Describes filling missing job and investment figures for a large share of observations by reading individual n |
| `restricted_data_used` | 2 | 14% | aer_108_4_3 p.17-18 Section IIB: Constructs the analysis sample by linking three administrative Swedish registers, an unemployment history regi; aer_112_10_8 p.16-16 Section II.D, Owner/Seller Demographics: The seller demographic, income and wealth data are drawn from population-wide official Danish civil and tax re |
| `in_footnote` | 1 | 7% | restud_2025_restud_rdae072 p.30-30 Section 6.2, footnote 40: The Bayesian estimation matches four detrended U.S. macro series (real consumption, real investment, real exog |
| `in_main_text` | 1 | 7% | restud_2025_restud_rdae072 p.6-8 Section 2.1-2.2, Tables 1-3 and notes: Sources for the stylized facts are named in text and table notes: the Federal Reserve Board and BEA for the U. |
| `other:multiple_sampling_criteria_rows` | 1 | 7% | restud_2025_restud_rdae072 p.6-7 Section 2.1, Table 2: The firm-level long-term underutilization table presents rows under successively stricter sampling criteria (a |

### specification_reporting (papers with this category: 8/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `baseline_then_variants` | 5 | 36% | aer_112_10_8 p.27-28 Table 2: The main structural-parameter table reports eight nested model variants as rows, each adding a friction or a s; aer_112_5_9 p.24-24 Table 2: The structural-parameter table is organized into separate labeled panels for the underlying model parameters,  |
| `se_type_in_notes` | 3 | 21% | aer_112_10_8 p.27-28 Table 2: The main structural-parameter table reports eight nested model variants as rows, each adding a friction or a s; restud_2026_restud_rdag013 p.22-22 Table 4 notes: The structural estimates table reports parameter estimates with standard errors and a note describing how they |
| `controls_progressive_columns` | 1 | 7% | restud_90_2_4 p.12-12 Table 3: The first-stage policy function table shows four ordered probit specifications that progressively add market d |
| `mean_of_dependent_reported` | 1 | 7% | jpe_2025_735509 p.35-36 Tables 3-4, notes: States the mean and median of the dependent variable for each estimation subsample in the table notes rather t |
| `n_reported` | 1 | 7% | restud_90_2_4 p.12-12 Table 3: The first-stage policy function table shows four ordered probit specifications that progressively add market d |
| `other:model_selection_criterion` | 1 | 7% | restud_90_2_4 p.27-27 Section 6.5.1: The preferred first-stage specification is chosen by AIC among the four columns and carried into the second st |
| `other:moment_progression` | 1 | 7% | aer_112_10_8 p.29-32 Section IV.D, Results: Because estimation matches binned data moments rather than running a single regression, the paper frames its s |
| `other:no_fit_statistic_reported` | 1 | 7% | jpe_2025_735509 p.35-36 Tables 3-4: Reports point estimates and standard errors for each structural profit and valuation parameter in the main est |
| `other:panel_structured_table` | 1 | 7% | aer_112_5_9 p.24-24 Table 2: The structural-parameter table is organized into separate labeled panels for the underlying model parameters,  |
| `other:variable_glossary_table` | 1 | 7% | aer_112_10_8 p.10-10 Table 1: A dedicated table lays out every state variable, calibrated parameter and structural parameter with its econom |
| `weights_stated` | 1 | 7% | restud_90_5_11 p.22-30 Section 5.3; Table 5 notes: Weighting is stated only in the structural table notes: earnings weights for the MORG sample and final weights |

### variable_construction (papers with this category: 9/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `outcome_definition` | 5 | 36% | aer_112_10_8 p.18-19 Section III.A: The listing premium is defined as the log difference between the observed initial listing price and the hedoni; jpe_2025_735509 p.28-28 Section IV.A, Assumption 3: Defines the runner-up location's valuation for the firm as a function of observed location and firm characteri |
| `measurement_error_discussed` | 4 | 29% | aer_112_10_8 p.16-17 Section II.F, equation (6): Fair house value is estimated from a hedonic pricing regression of log sale price on time-varying property cha; jpe_2025_735509 p.32-32 Section IV.B, footnote: Constructs the number-of-bidders variable from the firm's self-reported short list rather than from observed s |
| `treatment_definition` | 4 | 29% | jpe_2025_735509 p.28-28 Section IV.A, Assumption 2: Defines firm profit in a location as a linear function of observed location and firm characteristics plus a no; qje_140_1_4 p.18-18 Section II.B.1, footnote: In the structural model, a country-specific productivity differential faced by migrants is introduced specific |
| `deflated_or_real_terms` | 2 | 14% | aer_111_4_3 p.11-11 Section I.D: Lifetime-income and budget-constraint variables underlying the simulation are discounted to present value usin; restud_90_2_4 p.8-9 Section 4, Figure 1b: The adoption cost series is built from a manufacturer survey list price net of the VPF subsidy plus ancillary  |
| `logs_or_ihs` | 2 | 14% | aer_112_10_8 p.16-17 Section II.F; footnote: Potential gains and potential home equity are constructed as log differences between the hedonic-model predict; restud_2026_restud_rdag013 p.9-9 Section 2.3 and Table 1: Plant and firm scores are transformed with log(1+x) because of a long right tail; the authors explain that zer |
| `in_appendix` | 1 | 7% | restud_2026_restud_rdag013 p.7-8 Section 2.2, equation (1): The firm score is defined by an explicit formula (a complexity-point weighted average of plant scores), and th |
| `other:bidder_count_definition` | 1 | 7% | jpe_2025_735509 p.32-32 Section IV.B, footnote: Constructs the number-of-bidders variable from the firm's self-reported short list rather than from observed s |
| `other:demand_function_estimation` | 1 | 7% | aer_112_10_8 p.20-21 Section III.B; Figure 4: The two demand primitives that convert a listing premium into a sale probability and a realized price premium  |
| `other:duration_normalization` | 1 | 7% | jpe_2025_735509 p.13-13 Section II.B: Normalizes every subsidy deal to a common contract length so that deals with different payout horizons are com |
| `other:hedonic_valuation_model` | 1 | 7% | aer_112_10_8 p.16-17 Section II.F, equation (6): Fair house value is estimated from a hedonic pricing regression of log sale price on time-varying property cha |
| `other:key_construct_definition` | 1 | 7% | ecta_2025_ecta22303 p.13-14 Section 3.1: The paper's central outcome construct, collateral aversion, is formally defined within the stylized household  |
| `other:latent_index_construction` | 1 | 7% | aer_109_7_8 p.28-28 Section VIIA, Preference Specification: For the structural model, a disability severity index with a small number of ordered categories is constructed |
| `other:observable_heterogeneity_by_sector` | 1 | 7% | restud_2026_restud_rdag013 p.6-10 Sections 2.1.1 and 3.2: Observable plant heterogeneity is proxied by six NAICS-based sectors; unobserved heterogeneity is modelled as  |
| `other:profit_function_definition` | 1 | 7% | jpe_2025_735509 p.28-28 Section IV.A, Assumption 2: Defines firm profit in a location as a linear function of observed location and firm characteristics plus a no |
| `other:reference_point_construction` | 1 | 7% | aer_112_10_8 p.16-17 Section II.F; footnote: Potential gains and potential home equity are constructed as log differences between the hedonic-model predict |
| `other:state_space_discretization` | 1 | 7% | restud_90_2_4 p.26-27 Section 6.5.1, Figure 3, footnote 30: The within-theatre adoption share is coarsened onto a grid that differs by theatre size class; the choice is j |
| `other:valuation_function_definition` | 1 | 7% | jpe_2025_735509 p.28-28 Section IV.A, Assumption 3: Defines the runner-up location's valuation for the firm as a function of observed location and firm characteri |
| `winsorization` | 1 | 7% | ecta_2025_ecta22303 p.8-8 Table I note: Several monetary variables in the main summary-statistics table are winsorized at the extreme tails, with the  |

### writing_structure (papers with this category: 9/14)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `results_previewed_in_intro` | 9 | 64% | aer_108_4_3 p.3-4 Introduction: Previews the paper's three main empirical findings in an enumerated First, Second, Finally structure within th; aer_109_7_8 p.3-4 Introduction: The introduction previews the paper's main quantitative findings in ordered bullets before the design and data |
| `contribution_paragraph` | 8 | 57% | aer_108_4_3 p.4-4 Introduction: Includes a dedicated contribution paragraph positioning the paper relative to three separate literatures: theo; aer_109_7_8 p.3-4 Introduction: The introduction previews the paper's main quantitative findings in ordered bullets before the design and data |
| `roadmap_paragraph` | 6 | 43% | aer_108_4_3 p.4-4 Introduction, final paragraph: Closes the introduction with an explicit roadmap paragraph describing the content of each subsequent numbered ; aer_112_10_8 p.5-6 End of Introduction: The paper is organized model-first: the structural model is presented in Section I before the data and reduced |
| `appendix_heavy` | 5 | 36% | aer_108_4_3 p.17-36 throughout Sections II-V: Relies extensively on a multi-part online technical appendix for proofs, additional robustness checks, constru; jpe_2025_735509 p.11-47 Throughout, appendix citations A-M: Relies extensively on a lettered online appendix, spanning many named appendix sections cited throughout the m |
| `data_before_design` | 3 | 21% | jpe_2025_735509 p.8-20 Section II before Section III: Presents the institutional background, new dataset, descriptive statistics, and reduced-form correlations befo; restud_2026_restud_rdag013 p.6-8 Section 2: Institutional context precedes data, and the context section is organised as short definitional subsections (w |
| `design_before_data` | 3 | 21% | aer_112_10_8 p.5-6 End of Introduction: The paper is organized model-first: the structural model is presented in Section I before the data and reduced; qje_140_1_4 p.2-3 Section I: The article places the full theoretical model before the empirical section, and the empirical section before t |
| `robustness_separate_section` | 3 | 21% | aer_112_10_8 p.33-39 Section V title and placement: Robustness and validation material is grouped into its own dedicated section placed after the main structural ; restud_2026_restud_rdag013 p.6-28 Sections 2 to 7: Order is context, data, descriptive analysis, model, estimation and identification, results and fit, counterfa |
| `online_appendix_not_available` | 2 | 14% | aer_108_4_3 p.17-36 throughout Sections II-V: Relies extensively on a multi-part online technical appendix for proofs, additional robustness checks, constru; ecta_2025_ecta22303 p.17-17 Section 3.4, and throughout: Substantial technical and robustness detail (full bunching derivations, additional heterogeneity results, and  |
| `appendix_reliance` | 1 | 7% | restud_2026_restud_rdag013 p.16-28 Sections 4 to 7: The main text repeatedly defers derivations, algorithms, calibration details, decomposition implementation and |
| `descriptive_before_model` | 1 | 7% | restud_2026_restud_rdag013 p.6-28 Sections 2 to 7: Order is context, data, descriptive analysis, model, estimation and identification, results and fit, counterfa |
| `mechanisms_after_main` | 1 | 7% | restud_90_5_11 p.5-33 Sections 2 to 9: Order is model, data, empirical strategy, reduced-form results (opportunity cost first, then wages, then hours |
| `other:companion_paper_appendix` | 1 | 7% | ecta_2025_ecta22303 p.17-17 Section 3.4, and throughout: Substantial technical and robustness detail (full bunching derivations, additional heterogeneity results, and  |
| `other:context_section_with_definitional_subsections` | 1 | 7% | restud_2026_restud_rdag013 p.6-8 Section 2: Institutional context precedes data, and the context section is organised as short definitional subsections (w |
| `other:descriptive_facts_motivate_model` | 1 | 7% | restud_90_2_4 p.10-11 Section 4: Two stylized facts from the data (gradual within-firm rollout, no local strategic interaction) are stated expl |
| `other:related_literature_in_intro` | 1 | 7% | jpe_2025_735509 p.7-8 Introduction, 'Related literature': Places the literature-positioning discussion as a labeled subsection within the introduction itself rather tha |
| `other:sufficient_statistics_then_structural` | 1 | 7% | restud_90_5_11 p.27-28 Section 7 intro, 7.1, 7.2: The welfare section presents two complementary routes: a sufficient-statistics reading of the reduced-form mom |
| `roadmap_absent` | 1 | 7% | restud_2026_restud_rdag013 p.2-6 Sections 1, 1.1, 1.2: The introduction previews the counterfactual findings, the mechanism decomposition and additional counterfactu |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | paper_only | 1 | aer_111_4_3 d1.implementation_features (paper: The bunching estimation excludes a region around each threshold when f / card: No bandwidth or exclusion-window field is populated for design d1 or a) |
| bandwidth | unknown | 1 | aer_112_10_8 s2.sample (paper: The appendix regression-kink implementation of the listing-premium hoc / card: Card specification s2 shows a formula with a local-polynomial order an) |
| bandwidth | code_only | 1 | ecta_2025_ecta22303 s1.notes / x2 (paper: The traditional bunching estimator's counterfactual is described in th / card: Spec s1's notes record a specific polynomial degree and three cutpoint) |
| cluster_level | agree | 5 | aer_112_5_9 s1.se.cluster_level;s2.se.cluster_level;s3.se.cluster_level (paper: Standard errors are clustered at the local labor market region. / card: s1, s2, and s3 all cluster on the local-labor-market-region variable.); jpe_2025_736209 s1.se.cluster_level (paper: Standard errors in the main Uganda ANCOVA regressions are clustered at / card: s1 and s2 record se=cluster on ent_id (enterprise id), consistent with) |
| cluster_level | unknown | 3 | aer_111_4_3 s1.se.cluster_level (paper: The paper does not mention clustering of standard errors at any level. / card: s1.se.cluster_level=null for every specification.); jpe_2025_735509 s1.se.type; s4.se.type (paper: Gives no statement anywhere in the main text about how standard errors / card: Specs s1-s4 record se.type=null and se.cluster_level=null, i.e. the SE) |
| cluster_level | paper_only | 3 | ecta_2025_ecta22303 s2.se.cluster_level (paper: Standard errors in the default model are stated as clustered at the di / card: Spec s2's se.type and se.cluster_level fields are both null (unknown),); qje_140_1_4 specifications (paper: For the co-inventor spillover regression (Table III) the text separate / card: No specification extracted in the card corresponds to the co-inventor ) |
| cluster_level | code_only | 1 | qje_140_1_4 s3.se.cluster_level (paper: The main text does not state a cluster level for the shift-share IV re / card: The card records two-way clustering at the region and decade level for) |
| comparison_group | paper_only | 4 | aer_111_4_3 d1.comparison_group (paper: The design's comparison is explicit throughout: statutory-age disconti / card: d1.comparison_group=null.); ecta_2025_ecta22303 d2.comparison_group (paper: The paper explicitly names the control/comparison group for the differ / card: Design d2's comparison_group field is null (unknown).) |
| comparison_group | agree | 2 | aer_112_10_8 s2.comparison_group (paper: The appendix regression-kink check is a single-threshold kink design a / card: Card specification s2.comparison_group is null, consistent with a kink); jpe_2025_736209 s3.se; s5.se (paper: Kenya same-day comparisons against the pure control use randomization  / card: s3/s4 (Tables2_A7_A8_B5_C3.do) record se=cluster on village_id; s5/s6 ) |
| controls | agree | 5 | aer_111_4_3 s3.bindings[0] (paper: Column 3 adds worker controls including income, education, gender, mar / card: s3 binds global controls_ind to a variable list (schooly2 lifeearn lli); aer_112_5_9 s1;s2;s3 (paper: No individual-level covariates beyond the fixed effects appear in the  / card: The traced commands for s1, s2, and s3 show no covariates beyond the a) |
| controls | paper_only | 5 | aer_112_10_8 s1.controls_summary (paper: The hedonic model's control set is spelled out in the text: time-varyi / card: Card specification s1.controls_summary is null; only the outcome varia); ecta_2025_ecta22303 s2.controls_summary (paper: The paper lists the specific borrower and home covariates added across / card: Spec s2's controls_summary field is null.) |
| controls | unknown | 1 | restud_2025_restud_rdae072 s3.controls (paper: Table 6 controls for the lagged information set, firm size, age and ag / card: s3 shows a single regressor and no control list.) |
| data_source | paper_only | 7 | aer_112_10_8 data (paper: The paper names four core administrative data sources plus one commerc / card: The card's top-level data array is empty; no data sources are recorded); aer_112_5_9 d1 (paper: Data are Statistics Norway administrative registries (population, inco / card: The traced Stata commands reference variable names consistent with a N) |
| data_source | agree | 4 | aer_111_4_3 data[0].name (paper: The main administrative data are named as coming from the German State / card: data[0].name=RTZN, type=admin, source_hint=null; evidence line 'use $d); jpe_2025_736209 root.languages; root.files_read (paper: A Data Availability statement cites a Harvard Dataverse replication pa / card: The card records languages=['Stata'] and files_read=10, consistent wit) |
| diagnostic | paper_only | 10 | aer_111_4_3 diagnostics (paper: The paper reports a density-shape comparison test (Figure 8) used to d / card: diagnostics=[] (empty array) at the card level.); aer_112_10_8 diagnostics (paper: The paper reports an extensive set of diagnostics: hedonic fit-statist / card: The card's diagnostics array is empty.) |
| diagnostic | agree | 3 | aer_112_5_9 x3 (paper: No overidentification test is discussed or applicable, since the desig / card: diag x3 (overid) is recorded as not_applicable.); qje_140_1_4 x1 (paper: The main text names the shift-share IV strategy but reports no first-s / card: The card's single diagnostic record for a first-stage check has status) |
| diagnostic | disagree | 1 | aer_112_5_9 x2 (paper: First-stage F-statistics are reported in the main first-stage table fo / card: diag x2 (weak_iv) is recorded as not_found_in_scope.) |
| diagnostic | unknown | 1 | ecta_2025_ecta22303 x1 (paper: The main text does not report a formal bandwidth-sensitivity check for / card: Diagnostic x1 (bandwidth_selection) is recorded with status 'unknown' ) |
| estimator | agree | 14 | aer_111_4_3 s1.estimator (paper: Reduced-form effects are estimated by OLS on discontinuity-level bunch / card: s1-s5 all record estimator=ols, command=reg.); aer_112_10_8 s1.formula_or_call (paper: The hedonic fair-value model is estimated as an OLS regression of log  / card: Card specification s1 records the same command and formula, an OLS reg) |
| estimator | paper_only | 4 | aer_111_4_3 specifications (paper: Section VI.A states that reference-dependence parameters are recovered / card: The specifications array contains only the OLS reduced-form regression); aer_112_10_8 designs (paper: The paper's primary estimator for its main claims is a structural mode / card: The card records only two designs, an OLS hedonic regression (d1/s1) a) |
| estimator | code_only | 2 | qje_140_1_4 s3.formula_or_call (paper: The text names a shift-share instrumental-variables strategy based on  / card: The card's IV specification (s3) is a two-stage-least-squares regressi); restud_2026_restud_rdag013 s1.estimator (paper: Table 3 deterrence regressions are described only as regressions of vi / card: s1 to s3 use ppmlhdfe (Poisson PPML) for n_violations.) |
| fixed_effects | agree | 7 | aer_112_10_8 s1.fixed_effects (paper: The hedonic model's fixed effects are described as year-cross-municipa / card: Card specification s1 lists fixed_effects as year and komstr, matching); aer_112_5_9 s1.fe;s2.fe;s3.fe (paper: Every specification includes birth-cohort and childhood-municipality f / card: s1, s2, and s3 all absorb the municipality (tkom) and cohort variables) |
| fixed_effects | paper_only | 3 | aer_111_4_3 s3.fixed_effects (paper: Table 4 lists pathway fixed effects and year-of-birth fixed effects as / card: s3.fixed_effects=null and s4.fixed_effects=null; the underlying formul); jpe_2026_740222 s1.fixed_effects (paper: Table 2 lists a progression of fixed effects for the preferred column: / card: Specification s1.fixed_effects is null; the card's evidence trace only) |
| fixed_effects | disagree | 2 | qje_140_1_4 s1.fixed_effects (paper: The main text describes the leads-and-lags event-study specification ( / card: The card's leads-and-lags specification (s1) additionally absorbs a te); restud_2026_restud_rdag013 s1.fixed_effects (paper: Table 3 column (1) lists year FE and unit FE 'Category, Firm'. / card: s1 absorbs year, naics_2, c_fe, region_fe.) |
| other | paper_only | 2 | ecta_2025_ecta22303 structural (paper: The paper documents a fully specified structural model in the main tex / card: The card's dedicated 'structural' field is null; the structural design); jpe_2025_736209 x3 (paper: States that sharpened q-values control the false discovery rate within / card: Diagnostic x3 (multiple_testing) is recorded as unknown in the card.) |
| other | agree | 2 | restud_2025_restud_rdae072 s2 (paper: Standard deviations of cyclical correlations computed with the VARHAC  / card: s2: varhac_est call in CU_Facts.m.); restud_90_2_4 s3 (paper: Time dummy coefficients regressed on digital availability instrumented / card: ivreg(time_FE ~ dmovies | us_dmovies_share)) |
| outputs | paper_only | 8 | aer_111_4_3 s1.output_ids (paper: The reduced-form regressions are explicitly reported in Table 4 of the / card: s1-s5.output_ids are all empty arrays; no table is linked to any speci); aer_112_10_8 outputs (paper: The paper contains four numbered main tables and ten main figures repo / card: The card's outputs.tables and outputs.figures arrays are both empty.) |
| outputs | disagree | 3 | aer_112_5_9 s1.outputs;s2.outputs;s3.outputs (paper: The main text presents two numbered tables (first-stage estimates; str / card: The card records three table outputs (t1, t2, t3) and no figure output); jpe_2025_736209 tables; figures (paper: The main text presents four numbered tables and two numbered figures,  / card: The card records tables=0 and figures=0, i.e. no table or figure ident) |
| outputs | unknown | 1 | restud_90_5_11 outputs (paper: Five main tables and four figures plus appendix tables A1 to A15 and f / card: Card records 2 tables and 1 figure from files read (coverage partial).) |
| robustness | paper_only | 7 | aer_111_4_3 robustness (paper: The paper references robustness checks for the structural parameters a / card: robustness=[] (empty array) at the card level.); aer_112_10_8 robustness (paper: The paper reports a dedicated robustness table re-estimating the full  / card: The card's robustness array is empty.) |
| robustness | agree | 1 | restud_90_5_11 s5 (paper: IV using indicators for large positive or negative residual licensed s / card: s5 ivreghdfe with i.residual_cat as instrument in robustness_subsample) |
| sample | paper_only | 8 | aer_111_4_3 s1.sample (paper: Section I.D describes the discontinuity-level bunching sample and its  / card: s1-s5.sample is null; the formula shows an unexplained 'if incl==1' fi); ecta_2025_ecta22303 s2.sample (paper: The paper states explicit sample restrictions: the default analysis is / card: Spec s2's sample field is null (unknown); the card's data records for ) |
| sample | disagree | 1 | aer_112_5_9 robustness.alt_control_group(base=s2,var=s3) (paper: The analysis rests on two economically distinct samples, hidden IV (no / card: The card frames the transparent-sample regression (s3) as an alt_contr) |
| sample | code_only | 1 | restud_2025_restud_rdae072 s1 (paper: Macro estimation uses four detrended U.S. series; the sample period is / card: s1 estimation command names datafile data_estimate_v8 with nobs=277.) |
| sample | agree | 1 | restud_2026_restud_rdag013 s3.sample (paper: Column (3) of Table 3 restricts to plant-years with an inspection. / card: s3 conditions on inspection==1.) |
| se_type | unknown | 2 | aer_111_4_3 s1.se.type (paper: Table 4 notes state standard errors are obtained by bootstrap, resampl / card: s1.se.type=robust (vce(r)); s2.se.type=iid (no vce option) at the trac); restud_2026_restud_rdag013 s1.se (paper: No SE type or cluster level stated for Tables 2 and 3. / card: se null for all specs.) |
| se_type | agree | 2 | aer_112_10_8 s1.se (paper: The main text does not discuss standard errors or clustering for the h / card: Card specification s1 records se.type and se.cluster_level as null.); jpe_2026_740222 s1.se.type (paper: Standard errors are described throughout as clustered (never heteroske / card: s1.se.type = cluster, traced to the cluster argument of the feols call) |
| se_type | paper_only | 2 | restud_2026_restud_rdag013 d2 (paper: Structural SEs from firm-level bootstrap (Table 4 notes). / card: No structural estimation spec recorded in the card.); restud_90_2_4 s1.se (paper: Parametric bootstrap with a stated number of replications for structur / card: se null for all specs) |
| se_type | code_only | 1 | jpe_2025_735509 s5.se.type (paper: Presents standard errors next to each structural parameter estimate wi / card: Specs s5-s6 record se.type='other:hessian_inverse', evidenced by code ) |
| weights | agree | 7 | aer_111_4_3 s1.weights (paper: Table 4 notes state that all regressions are weighted by group size. / card: s1-s5 all record weights=aweight=weight.); aer_112_10_8 s1.weights (paper: No mention of regression weights appears in the discussion of the hedo / card: Card specifications s1.weights and s2.weights are both null.) |
| weights | unknown | 2 | restud_2025_restud_rdae072 s3.weights (paper: No weights are mentioned for any regression. / card: s3.weights is null.); restud_90_2_4 s1.weights (paper: No weights mentioned / card: weights null) |
| weights | paper_only | 1 | jpe_2026_740222 s1.weights (paper: The baseline specification is described as an unweighted average effec / card: s1.weights is null (unknown), with no evidence trace either confirming) |

## Gaps the readers reported

- (1) No explicit software or code availability statement appears anywhere in the read text.
- (1) No explicit data or replication package availability statement appears anywhere in the read text (consistent with this b
- (1) No explicit discussion of standard-error clustering appears; the data are individual unemployment spells with bootstrap 
- (1) No preregistration, IRB approval, or participant-consent statement of any kind appears in the read text.
- (1) No formal multiple hypothesis testing correction is discussed despite many separate mechanism and robustness checks bein
- (1) The paper's online technical Appendices A through D and the separate online Appendix B and C figures and tables, referen
- (1) No explicit sentence justifying judge-level clustering (versus, e.g., department-level or two-way clustering) was found 
- (1) No formal weak-instrument statistic (such as an F-statistic or Kleibergen-Paap statistic) for the 2SLS first stage is re
- (1) No explicit discussion of the small number of clusters (75 judges) as a few-clusters problem, and no wild-cluster-bootst
- (1) No named statistical software or package (e.g., Stata, R, MATLAB) for either the IV estimation or the structural model e
- (1) No explicit pre-registration or IRB/ethics statement was found in the extracted text.
- (1) The online appendix (tables and figures referenced repeatedly, e.g., A1-A10) is not part of the extracted text, so appen
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
- (1) The online Appendix (tables A.1-A.4, Appendix B on the partially transparent instrument, Appendix C on heterogeneous ret
- (1) No explicit justification is given in the text for clustering standard errors at the local-labor-market level specifical
- (1) No discussion of multiple-testing or family-wise error concerns appears despite the paper reporting a separate IV estima
- (1) No preregistration, IRB, or ethics statement is found anywhere in the main text, and the paper does not flag this as ina
- (1) No balance table comparing observable characteristics of the hidden IV sample against the transparent IV sample is repor
- (1) No explicit software or package name is stated in the main text for the IV, NLLS, or robustness estimations.
- (1) No formal data-or-code availability statement appears in the main text; only a footnote directs readers to the online ar

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
