# Reported practice: `ml_prediction` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 6 paper notes (5 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | Econometrica: 2, AER: 1, QJE: 1, ReStud: 1, RFS: 1 |
| year | 2024: 1, 2025: 2, 2026: 3 |
| papers with at least one observation in category | variable_construction: 5, replication_statement: 5, design_statement: 3, heterogeneity_reported: 3, mechanism_evidence: 3, limitation_stated: 3, presentation_convention: 3, writing_structure: 3, specification_reporting: 2, inference_justification: 2, diagnostic_reported: 2, robustness_reported: 2, magnitude_interpretation: 2, sample_construction: 2, data_access: 2, external_validity: 1, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_114_2_5 | AER | 2024 | full | no | 325256be4d9c |
| ecta_2025_ecta19303 | Econometrica | 2025 | full | yes | a7bb07b44219 |
| ecta_2026_ecta21180 | Econometrica | 2026 | full | yes | 2a3737042536 |
| qje_140_1_3 | QJE | 2025 | full | yes | 6e375de3d173 |
| restud_2026_restud_rdag080 | ReStud | 2026 | full | yes | feb48766a8b7 |
| rfs_2026_rfs_hhag042 | RFS | 2026 | full | yes | d63dc3bb1fac |

## Practices by category and tag


### data_access (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 1 | 17% | qje_140_1_3 p.17-17 Section IV.A: The tax and audit data underlying the analysis are described as confidential administrative records obtained t |
| `commercial` | 1 | 17% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `data_restricted` | 1 | 17% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `linked_records` | 1 | 17% | qje_140_1_3 p.18-18 Section IV.B: Race information is not directly available in the tax data and is instead produced by linking or combining sev |
| `public_use` | 1 | 17% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |

### design_statement (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identifying_assumption_explicit` | 3 | 50% | ecta_2025_ecta19303 p.3-8 Introduction; Section 2.2: The paper states its estimand as functionals of the CATE (a best linear predictor, sorted group effects, and a; qje_140_1_3 p.13-14 Section III.B: The race-imputation step relies on an explicit conditional-independence assumption, that name and geography ar |
| `threats_discussed` | 2 | 33% | ecta_2025_ecta19303 p.8-10 Section 2.3: The paper frames its contribution as agnostic: it avoids assuming the machine-learning proxy is a consistent e; rfs_2026_rfs_hhag042 p.3-9 Introduction; Section 1.2 Motivation for modeling choices: A dedicated subsection motivates each modeling assumption of the belief simulator (sophisticated optimizing in |
| `design_variant_named` | 1 | 17% | ecta_2025_ecta19303 p.8-10 Section 2.3: The paper frames its contribution as agnostic: it avoids assuming the machine-learning proxy is a consistent e |
| `estimand_named` | 1 | 17% | ecta_2025_ecta19303 p.3-8 Introduction; Section 2.2: The paper states its estimand as functionals of the CATE (a best linear predictor, sorted group effects, and a |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.3-9 Introduction; Section 1.2 Motivation for modeling choices: A dedicated subsection motivates each modeling assumption of the belief simulator (sophisticated optimizing in |

### diagnostic_reported (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 2 | 33% | ecta_2025_ecta19303 p.32-33 Table II: Goodness-of-fit diagnostics comparing candidate machine-learning proxies are reported with interquartile range; qje_140_1_3 p.19-20 Figure I: A calibration exercise compares estimated race probabilities against self-reported race in the matched validat |
| `in_footnote` | 1 | 17% | qje_140_1_3 p.30-31 Section VI, footnote: To assess whether the single-state validation sample generalizes, the authors match to voter records in severa |
| `other:calibration_check` | 1 | 17% | qje_140_1_3 p.19-20 Figure I: A calibration exercise compares estimated race probabilities against self-reported race in the matched validat |
| `other:goodness_of_fit_diagnostic` | 1 | 17% | ecta_2025_ecta19303 p.32-33 Table II: Goodness-of-fit diagnostics comparing candidate machine-learning proxies are reported with interquartile range |
| `other:match_representativeness_check` | 1 | 17% | qje_140_1_3 p.30-31 Section VI, footnote: To assess whether the single-state validation sample generalizes, the authors match to voter records in severa |

### external_validity (papers with this category: 1/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 1 | 17% | qje_140_1_3 p.46-47 Conclusion: In the conclusion, the authors distinguish causes of the disparity that tax-authority administrators could add |
| `site_specific` | 1 | 17% | qje_140_1_3 p.18-31 Section IV.B; Section VI robustness: Validation of the race-imputation approach relies primarily on matched records from a single state, and the au |

### heterogeneity_reported (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `ml_heterogeneity` | 2 | 33% | ecta_2025_ecta19303 p.33-34 Table IV; Figure 4: Heterogeneity is summarized by sorting units into ranked groups based on a machine-learning-predicted treatmen; restud_2026_restud_rdag080 p.23-30 Section 6.2; Figure 8: Conditional average treatment effects are estimated with an honest causal forest adapted to a difference-in-di |
| `exploratory_labelled` | 1 | 17% | qje_140_1_3 p.28-29 Figure VI: Disparities are broken out by marital status, filer gender, and dependent-claiming status among EITC claimants |
| `mechanism_motivated` | 1 | 17% | restud_2026_restud_rdag080 p.23-30 Section 6.2; Figure 8: Conditional average treatment effects are estimated with an honest causal forest adapted to a difference-in-di |
| `other:contrast_with_ad_hoc_subgroups` | 1 | 17% | ecta_2025_ecta19303 p.3-3 Introduction: The paper frames its group-based heterogeneity approach as a disciplined alternative to the common practice of |
| `quantile` | 1 | 17% | ecta_2025_ecta19303 p.33-34 Table IV; Figure 4: Heterogeneity is summarized by sorting units into ranked groups based on a machine-learning-predicted treatmen |
| `split_sample` | 1 | 17% | qje_140_1_3 p.28-29 Figure VI: Disparities are broken out by marital status, filer gender, and dependent-claiming status among EITC claimants |

### inference_justification (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `multiple_testing_adjustment` | 2 | 33% | ecta_2025_ecta19303 p.16-17 Section 3.4: When two machine-learning proxy methods are close competitors on the goodness-of-fit criterion, the paper disc; restud_2026_restud_rdag080 p.23-23 Section 6.2: The causal forest is motivated partly as a way to avoid multiple testing across many candidate heterogeneity d |
| `other:coverage_calibration_by_simulation` | 1 | 17% | ecta_2025_ecta19303 p.23-24 Section 4.4: The paper recommends using the un-discounted nominal confidence level rather than a more conservative bound, j |
| `other:quantile_aggregated_inference` | 1 | 17% | ecta_2025_ecta19303 p.18-24 Section 4: In place of a single asymptotic standard error, confidence intervals and p-values are built by aggregating res |

### limitation_stated (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identification_caveat` | 2 | 33% | ecta_2025_ecta19303 p.35-35 Section 6.2: The covariate associations uncovered by the classification analysis are explicitly flagged as potentially refl; qje_140_1_3 p.47-47 Conclusion: The conclusion notes that for higher-income taxpayers, whose audit selection may not be fully automated, the a |
| `interpretation_caveat` | 2 | 33% | ecta_2025_ecta19303 p.39-40 Section 7: The authors state that requiring a pre-specified low-dimensional model of heterogeneity would avoid the power ; rfs_2026_rfs_hhag042 p.4-10 Introduction; Section 1.3: The authors acknowledge that the simulated belief distribution may lack features other researchers deem import |
| `external_validity` | 1 | 17% | qje_140_1_3 p.47-47 Conclusion: The authors state explicitly that their analysis is limited to disparities affecting Black taxpayers and does  |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.4-10 Introduction; Section 1.3: The authors acknowledge that the simulated belief distribution may lack features other researchers deem import |
| `power` | 1 | 17% | ecta_2025_ecta19303 p.39-40 Section 7: The authors state that requiring a pre-specified low-dimensional model of heterogeneity would avoid the power  |
| `selection` | 1 | 17% | ecta_2025_ecta19303 p.35-35 Section 6.2: The covariate associations uncovered by the classification analysis are explicitly flagged as potentially refl |

### magnitude_interpretation (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `relative_to_mean` | 2 | 33% | ecta_2025_ecta19303 p.32-33 Section 6.2: The pooled average treatment effect implied by the machine-learning-based estimator is compared against the si; qje_140_1_3 p.2-41 Introduction; literature discussion: The paper interprets its unconditional audit-rate disparity by benchmarking it against the overall population  |
| `compared_to_literature` | 1 | 17% | qje_140_1_3 p.2-41 Introduction; literature discussion: The paper interprets its unconditional audit-rate disparity by benchmarking it against the overall population  |
| `other:internal_consistency_check` | 1 | 17% | ecta_2025_ecta19303 p.32-33 Section 6.2: The pooled average treatment effect implied by the machine-learning-based estimator is compared against the si |
| `precision_discussed` | 1 | 17% | ecta_2025_ecta19303 p.33-33 Table III: The paper reports that estimated heterogeneity-loading coefficients are close to the value indicating a well-c |

### mechanism_evidence (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `suggestive_labelled` | 2 | 33% | ecta_2025_ecta19303 p.34-36 Section 6.2; Table V: Classification analysis is used to describe which baseline characteristics differ between the most- and least-; qje_140_1_3 p.45-45 Section VII.C, footnote: Beyond the algorithmic-objective channel, the authors state they separately checked and found no evidence that |
| `heterogeneity_as_mechanism` | 1 | 17% | ecta_2025_ecta19303 p.34-36 Section 6.2; Table V: Classification analysis is used to describe which baseline characteristics differ between the most- and least- |
| `in_appendix` | 1 | 17% | qje_140_1_3 p.45-45 Section VII.C, footnote: Beyond the algorithmic-objective channel, the authors state they separately checked and found no evidence that |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.33-35 Section 5.6; Equations (6) to (8); Table 12: The measure is decomposed into a model-disagreement part and an information-set part by re-expressing the beli |
| `model_guided` | 1 | 17% | rfs_2026_rfs_hhag042 p.33-35 Section 5.6; Equations (6) to (8); Table 12: The measure is decomposed into a model-disagreement part and an information-set part by re-expressing the beli |
| `ruled_out_alternatives` | 1 | 17% | qje_140_1_3 p.45-45 Section VII.C, footnote: Beyond the algorithmic-objective channel, the authors state they separately checked and found no evidence that |

### other (papers with this category: 1/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |
| `other:conflict_disclosure` | 1 | 17% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |

### presentation_convention (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_stars` | 2 | 33% | ecta_2025_ecta19303 p.33-37 Table notes, Tables III-VI: Main result tables report split-aggregated point estimates with interval bounds in parentheses and two-sided p; qje_140_1_3 p.28-28 Table I: The disparity tables and figures report point estimates with standard errors or confidence intervals rather th |
| `appendix_tables_numbered_a` | 1 | 17% | rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `binscatter` | 1 | 17% | qje_140_1_3 p.19-25 Figures I-IV: Several figures use binned scatterplots, grouping taxpayers into equal-sized bins by predicted race probabilit |
| `coefficient_plot` | 1 | 17% | ecta_2025_ecta19303 p.33-33 Figure 4: Group-level heterogeneity estimates are displayed in a coefficient-style plot with joint confidence bands alon |
| `in_appendix` | 1 | 17% | rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `notes_state_se` | 1 | 17% | ecta_2025_ecta19303 p.33-37 Table notes, Tables III-VI: Main result tables report split-aggregated point estimates with interval bounds in parentheses and two-sided p |

### replication_statement (papers with this category: 5/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `code_public` | 3 | 50% | ecta_2025_ecta19303 p.44-44 Editorial footer: A public replication package containing code and data is deposited with a persistent DOI, and an editorial not; qje_140_1_3 p.48-48 Data Availability statement: The paper includes a formal data-availability statement pointing to a public replication archive hosted on an  |
| `replication_package_cited` | 3 | 50% | ecta_2025_ecta19303 p.44-44 Editorial footer: A public replication package containing code and data is deposited with a persistent DOI, and an editorial not; qje_140_1_3 p.48-48 Data Availability statement: The paper includes a formal data-availability statement pointing to a public replication archive hosted on an  |
| `software_named` | 3 | 50% | ecta_2025_ecta19303 p.38-38 Section 6.3, Comment 6.4: The machine-learning proxy models are implemented through a named R package with specific method identifiers r; ecta_2026_ecta21180 p.13-14 Section 4.2: Specific estimation software components, including a policy-tree search algorithm and causal or random-forest  |
| `data_public` | 2 | 33% | ecta_2025_ecta19303 p.44-44 Editorial footer: A public replication package containing code and data is deposited with a persistent DOI, and an editorial not; rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `data_restricted` | 1 | 17% | qje_140_1_3 p.48-48 Data Availability statement: The same statement implicitly distinguishes the replication code, which is shared, from the underlying confide |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |

### robustness_reported (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_estimator` | 2 | 33% | ecta_2025_ecta19303 p.29-29 Section 6, referencing Supplemental Appendix G: Results from purely predictive machine-learning proxies, as opposed to the paper's causal-learner variants, ar; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `alt_sample` | 2 | 33% | ecta_2025_ecta19303 p.29-29 Section 6, footnote: The paper reports, in a footnote rather than a table, that results are qualitatively similar under an alternat; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `in_appendix` | 2 | 33% | ecta_2025_ecta19303 p.29-29 Section 6, referencing Supplemental Appendix G: Results from purely predictive machine-learning proxies, as opposed to the paper's causal-learner variants, ar; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `online_appendix_not_available` | 2 | 33% | ecta_2025_ecta19303 p.29-29 Section 6, referencing Supplemental Appendix G: Results from purely predictive machine-learning proxies, as opposed to the paper's causal-learner variants, ar; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `alt_specification` | 1 | 17% | rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `in_footnote` | 1 | 17% | ecta_2025_ecta19303 p.29-29 Section 6, footnote: The paper reports, in a footnote rather than a table, that results are qualitatively similar under an alternat |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.33-46 Section 5.6; Table 12; Appendix C Table C1: Robustness of the measure to its own construction is shown in the main text by re-running sorts with four hype |
| `other:alt_aggregation_rule` | 1 | 17% | ecta_2025_ecta19303 p.29-29 Section 6, referencing Supplemental Appendix H: An alternative interval-construction rule, aimed at capturing the majority of split-specific values rather tha |
| `summarized_in_one_table` | 1 | 17% | rfs_2026_rfs_hhag042 p.33-46 Section 5.6; Table 12; Appendix C Table C1: Robustness of the measure to its own construction is shown in the main text by re-running sorts with four hype |

### sample_construction (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `sample_period_stated` | 2 | 33% | qje_140_1_3 p.17-31 Section IV.A; robustness across years discussion: The primary results focus on one tax year chosen because audit outcomes were most fully resolved at analysis t; rfs_2026_rfs_hhag042 p.11-15 Section 2; Table 3 notes: The full data period and the shorter out-of-sample test period are stated separately; the gap is explained by  |
| `data_access_procedure_described` | 1 | 17% | qje_140_1_3 p.18-18 Section IV.B, footnote: Data-linkage and validation steps that required nonanonymized taxpayer identifiers were carried out by governm |
| `data_source_named` | 1 | 17% | qje_140_1_3 p.17-17 Section IV.A: The core analysis uses comprehensive, confidential administrative tax-return microdata for a full national fil |
| `exclusions_justified` | 1 | 17% | qje_140_1_3 p.18-30 Section IV.B; robustness table discussion: A subset of taxpayers lack one or more inputs needed to impute race; rather than dropping them, the main analy |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.11-15 Section 2; Table 3 notes: The full data period and the shorter out-of-sample test period are stated separately; the gap is explained by  |
| `matching_or_linkage_described` | 1 | 17% | qje_140_1_3 p.17-18 Section IV.B: To obtain ground-truth race information for validation, the authors match tax records to publicly available st |
| `restricted_data_used` | 1 | 17% | qje_140_1_3 p.17-17 Section IV.A: The core analysis uses comprehensive, confidential administrative tax-return microdata for a full national fil |

### specification_reporting (papers with this category: 2/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `baseline_then_variants` | 1 | 17% | ecta_2025_ecta19303 p.32-33 Table II: Before settling on a main specification, the paper reports a dedicated comparison table ranking several machin |
| `fe_listed_in_table` | 1 | 17% | qje_140_1_3 p.28-28 Table I: Because the design is a bounds/disparity estimator rather than a panel regression, none of the reported specif |
| `se_type_in_notes` | 1 | 17% | ecta_2025_ecta19303 p.33-37 Tables III-VI: Result tables report split-aggregated point estimates together with interval bounds in parentheses and two-sid |
| `weights_stated` | 1 | 17% | ecta_2025_ecta19303 p.31-31 Section 6.2: The paper states that the village-level regressions used to estimate the key features include district-by-time |

### variable_construction (papers with this category: 5/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `deflated_or_real_terms` | 1 | 17% | qje_140_1_3 p.17-17 Section IV.A: Dollar-denominated quantities drawn from research audits conducted in earlier years are converted to a common  |
| `in_appendix` | 1 | 17% | rfs_2026_rfs_hhag042 p.7-45 Equation (4); footnote 4; Section 2.1; Appendix B Table B1: The key variable is defined by equation as the cross-investor standard deviation of forecasts; the constructio |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.7-45 Equation (4); footnote 4; Section 2.1; Appendix B Table B1: The key variable is defined by equation as the cross-investor standard deviation of forecasts; the constructio |
| `measurement_error_discussed` | 1 | 17% | aer_114_2_5 p.11-20 Section I footnote 18 and Section III footnote 28: One claimant characteristic used in a supplemental table is a predicted-benefits variable built from a machine |
| `other:covariate_definition` | 1 | 17% | ecta_2025_ecta19303 p.31-31 Section 6.2: The covariate vector used to build machine-learning proxies is a broad set of baseline village-level demograph |
| `other:covariate_selection` | 1 | 17% | ecta_2026_ecta21180 p.13-14 Section 4.2: Candidate covariates for the policy tree are narrowed to those flagged as important by both a lasso importance |
| `other:protected_class_probability_construction` | 1 | 17% | qje_140_1_3 p.13-13 Section III.B: The key explanatory variable is not observed race but an estimated probability that the primary filer is Black |
| `other:rescaling` | 1 | 17% | ecta_2025_ecta19303 p.38-38 Section 6.3, Comment 6.4: Outcomes and covariates are rescaled onto a common bounded range before being passed to the machine-learning t |
| `outcome_definition` | 1 | 17% | qje_140_1_3 p.17-17 Section IV.A: The audit outcome is a binary indicator for whether a filed return was ever selected for an operational or res |
| `standardized_index` | 1 | 17% | rfs_2026_rfs_hhag042 p.7-45 Equation (4); footnote 4; Section 2.1; Appendix B Table B1: The key variable is defined by equation as the cross-investor standard deviation of forecasts; the constructio |
| `treatment_definition` | 1 | 17% | rfs_2026_rfs_hhag042 p.7-45 Equation (4); footnote 4; Section 2.1; Appendix B Table B1: The key variable is defined by equation as the cross-investor standard deviation of forecasts; the constructio |
| `winsorization` | 1 | 17% | rfs_2026_rfs_hhag042 p.13-45 Table 1 notes; Table 6 notes; Table 11 notes; Table B1 notes: Winsorization thresholds differ by use: summary statistics winsorize both tails at one level, regression contr |

### writing_structure (papers with this category: 3/6)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 3 | 50% | ecta_2025_ecta19303 p.3-4 Introduction: The introduction states the paper's three targeted estimands, a best linear predictor, sorted group effects, a; qje_140_1_3 p.5-7 Introduction: Following the results preview, the introduction sets out the paper's contributions in distinct paragraphs: a s |
| `results_previewed_in_intro` | 3 | 50% | ecta_2025_ecta19303 p.4-5 Introduction: The introduction previews the paper's applied narrative and headline finding of large treatment-effect heterog; qje_140_1_3 p.2-4 Introduction: The introduction previews the paper's main findings in an explicit ordinal sequence before the corresponding s |
| `appendix_heavy` | 2 | 33% | ecta_2025_ecta19303 p.36-37 Section 6.2: Robustness checks for the empirical application are not gathered into a separate labeled robustness subsection; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `design_before_data` | 2 | 33% | ecta_2025_ecta19303 p.5-5 Introduction: The paper's own roadmap paragraph places the theoretical identification, estimation, and inference sections ah; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `mechanisms_after_main` | 2 | 33% | qje_140_1_3 p.22-31 Sections VI-VII: The paper structures its empirical sections so headline disparity estimates come first, robustness checks for ; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `roadmap_paragraph` | 2 | 33% | ecta_2025_ecta19303 p.5-5 Introduction: The paper's own roadmap paragraph places the theoretical identification, estimation, and inference sections ah; qje_140_1_3 p.7-7 end of Introduction: The introduction closes with an explicit roadmap paragraph mapping each numbered section to its topic, from in |
| `robustness_separate_section` | 2 | 33% | qje_140_1_3 p.22-31 Sections VI-VII: The paper structures its empirical sections so headline disparity estimates come first, robustness checks for ; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `in_footnote` | 1 | 17% | rfs_2026_rfs_hhag042 p.16-41 footnotes 11, 16, 17: Footnotes carry substantive supplementary analyses (an earnings-announcement test for the long leg, definition |
| `in_main_text` | 1 | 17% | rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `main_result_first` | 1 | 17% | rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 4 | ecta_2026_ecta21180 s1.se.cluster_level; s2.se.cluster_level (paper: No clustering of standard errors is discussed anywhere in the text. / card: se.cluster_level is null for both specifications, consistent with no c); qje_140_1_3 s1-s3 (paper: Standard errors for the headline table come from an asymptotic-distrib / card: Recorded se fields for s1-s3 are 'robust/None' or 'None/None', with no) |
| cluster_level | paper_only | 1 | ecta_2025_ecta19303 specifications[*].se.cluster_level (paper: Standard errors are clustered at the village level. / card: se.cluster_level is null in every extracted specification (s1, s2, s4,) |
| comparison_group | paper_only | 4 | ecta_2025_ecta19303 specifications[s5].comparison_group (paper: The treated group receives the full bundled policy (incentives, social / card: comparison_group is null on every specification record; the underlying); ecta_2026_ecta21180 d1.comparison_group; s1.comparison_group; s2.comparison_group (paper: Five policies are compared, with the fully untreated policy used as th / card: comparison_group is null in the design record and in both specificatio) |
| controls | paper_only | 3 | ecta_2025_ecta19303 specifications[*].controls_summary; variable_construction (paper: The covariate set used for the proxies and for the classification anal / card: controls_summary is null on every specification and the card's variabl); ecta_2026_ecta21180 s1.controls_summary; s2.controls_summary (paper: Covariates selected via lasso and causal-forest importance rankings, p / card: controls_summary is null for both specifications; the traced call show) |
| controls | agree | 1 | rfs_2026_rfs_hhag042 s2.family_description (paper: Table 6 adds controls in three steps (4, 6, then 12 characteristics) b / card: s2 family of 3 specifications with increasing controls (5, 7, 12 chara) |
| data_source | paper_only | 3 | ecta_2026_ecta21180 data (paper: Data combine 30-minute household electricity-usage records and a pre-e / card: The top-level data array in the card is empty; no data source entry wa); qje_140_1_3 packages (paper: Explicitly names its data sources as confidential IRS administrative m / card: The printed card summary lists only software packages (sklearn, statsm) |
| data_source | agree | 2 | ecta_2025_ecta19303 data[0] (paper: The analysis dataset is a village-by-month panel built from administra / card: The card records a single input dataset at village-month level, typed ); restud_2026_restud_rdag080 d1 (paper: CDDA designated-area database, Landsat NDVI, Li et al. nightlights, HI / card: Variable names greenness, foundationCS, cddaid consistent with CDDA an) |
| diagnostic | paper_only | 2 | ecta_2025_ecta19303 outputs.tables[t1] vs diagnostics[] (paper: A dedicated table compares candidate machine-learning proxies on goodn / card: This comparison is captured only as a table output, not as an entry in); ecta_2026_ecta21180 diagnostics (paper: An instrument-validity specification test targeting the exclusion-type / card: The diagnostics array in the card is empty.) |
| diagnostic | code_only | 1 | qje_140_1_3 x1 (paper: The main text only states that additional detail on the predictive mod / card: diag x1 tagged multiple_testing, described as '5 cross-validation fold) |
| diagnostic | agree | 1 | qje_140_1_3 x2 (paper: Reports a dual-bootstrap procedure, citing an external methodology pap / card: diag x2 tagged pretrend_test, described as a dual bootstrap procedure ) |
| estimator | agree | 9 | ecta_2026_ecta21180 s1.estimator; s2.estimator (paper: Optimal policy is estimated by empirical welfare maximization over dep / card: Both specifications call two_step_ewm_tree(..., depth = c(3,3)) from t); qje_140_1_3 s1 (paper: Trains a random forest regression model on randomly sampled audit data / card: s1: RandomForestRegressor, method=ml_prediction, variant=random_forest) |
| estimator | paper_only | 2 | ecta_2025_ecta19303 specifications[]; tags.methods (paper: ML proxies are built with four candidate learners (elastic net, gradie / card: Specifications record random_forest, lasso, and neural_net trained via); qje_140_1_3 s1-s4 (paper: Reports probability-weighted and linear closed-form disparity estimato / card: Records four modeling specs (s1 RandomForestRegressor, s2 RandomForest) |
| fixed_effects | agree | 5 | ecta_2025_ecta19303 conventions[]; specifications[s5].fixed_effects (paper: The village-level regressions are stated to include district-by-time ( / card: A repository-level conventions note records that the code builds a fix); ecta_2026_ecta21180 s1.fixed_effects; s2.fixed_effects (paper: The assignment rule is a nonparametric partition of the covariate spac / card: fixed_effects is null for both specifications, with no fixed-effect te) |
| other | paper_only | 1 | rfs_2026_rfs_hhag042 packages (paper: Investor models are random forests; robustness uses gradient boosted t / card: packages include scikit-learn and xgboost with usage unknown; no desig) |
| outputs | agree | 2 | ecta_2025_ecta19303 outputs.tables[t1..t6]; outputs.figures[f1] (paper: The main text presents a descriptive-statistics table, a method-compar / card: The card records six table outputs matching the method-comparison, bes); rfs_2026_rfs_hhag042 s3.family_description (paper: Six panel columns: SUV, turnover, historical volatility at t and t+1 / card: s3 family: six outcomes SUV, turnover, realized volatility (current an) |
| outputs | paper_only | 2 | ecta_2026_ecta21180 outputs.tables; outputs.figures; s1.output_ids; s2.output_ids (paper: The paper presents five main numbered tables and two main figures cove / card: outputs.tables and outputs.figures are both empty arrays, and both spe); qje_140_1_3 tables=0, figures=0 (paper: Presents numbered main-text tables and numbered main-text figures, eac / card: The card's --specs summary reports zero recorded tables and zero recor) |
| outputs | disagree | 1 | restud_2026_restud_rdag080 outputs (paper: Four main tables, eight main figures and appendix tables A.3 to A.16. / card: tables 0, figures 2 with partial coverage.) |
| robustness | paper_only | 3 | ecta_2025_ecta19303 robustness=[]; provenance.files_skipped (paper: Robustness checks are reported for an alternative main/auxiliary split / card: The card's robustness array is empty, and its provenance explicitly li); ecta_2026_ecta21180 robustness (paper: An empirical Monte Carlo study compares the proposed inference procedu / card: The robustness array in the card is empty, and no evidence entries ref) |
| robustness | agree | 1 | restud_2026_restud_rdag080 robustness[0] (paper: TWFE and matched TWFE reported as alternatives to the preferred estima / card: Robustness record alt_estimator base s2 variant s3 confirmed; s1 alt u) |
| sample | agree | 2 | ecta_2025_ecta19303 pipeline.sample_restrictions (paper: The main comparison restricts to villages that received one specific b / card: Two recorded sample restrictions match this: villages flagged as in th); ecta_2026_ecta21180 s1.sample; s2.sample; s1.formula_or_call; s2.formula_or_call (paper: The selection-absent targeting policy is restricted to choose only bet / card: The two traced specification calls use differently named input data ob) |
| sample | paper_only | 2 | qje_140_1_3 d1-d4 (paper: The sample is the full national filing population for a primary study  / card: The printed design records do not surface a sample-restriction field d); rfs_2026_rfs_hhag042 pipeline.sample_restrictions (paper: Common stocks on NYSE/AMEX/NASDAQ, excluding financials, utilities and / card: pipeline.sample_restrictions empty; s1 to s3 sample null) |
| sample | unknown | 1 | restud_2026_restud_rdag080 s2.sample (paper: Some estimations use a stratified 1 percent random sample of never-tre / card: Script named 4_CS_small.R uses object strat_sample; sample restriction) |
| se_type | paper_only | 3 | ecta_2026_ecta21180 s1.se.type; s2.se.type (paper: Confidence intervals for the welfare estimates come from a bespoke cro / card: se.type is null for both specifications; the resampling and cross-fitt); restud_2026_restud_rdag080 s1.se (paper: Multiplier bootstrap standard errors for the doubly-robust estimator. / card: s1 se type null.) |
| se_type | agree | 2 | ecta_2025_ecta19303 diagnostics[x2].description (paper: In place of a classical standard-error type, inference is reported as  / card: se.type is null in every specification, but a separate diagnostics rec); rfs_2026_rfs_hhag042 s1.se (paper: Newey-West adjusted t-statistics with six lags for all tables (footnot / card: s1.se hac_newey_west, kernel=bartlett, maxlags=6) |
| se_type | code_only | 1 | qje_140_1_3 s3 (paper: Main text does not describe the decomposition's standard errors as com / card: s3 code explicitly requests cov_type='HC1' (heteroskedasticity-robust)) |
| weights | paper_only | 2 | ecta_2026_ecta21180 s1.weights; s2.weights (paper: The empirical welfare objective inversely weights each observation by  / card: weights is null for both specifications; the traced call at this line ); restud_2026_restud_rdag080 s1.weights (paper: Aggregation weights by treated cell counts across country, cohort and  / card: w null on all specs.) |
| weights | agree | 1 | ecta_2025_ecta19303 conventions[]; specifications[s5].weights (paper: Village-level estimations are weighted by village population. / card: A conventions note and the felm/lm specification records show a weight) |
| weights | unknown | 1 | rfs_2026_rfs_hhag042 s1.weights (paper: Both equal- and value-weighted sorts reported in Table 3; conditional  / card: s1.weights null; helper function takes a weighting argument) |

## Gaps the readers reported

- (1) No explicit multiple-testing correction is stated despite many characteristic-interaction and subgroup comparisons (Tabl
- (1) No preregistration or pre-analysis plan is mentioned for either the administrative-data analysis or the supplemental sur
- (1) No IRB approval, ethics approval, or participant consent language appears anywhere in the extracted text for the survey.
- (1) No statistical software or package (e.g., Stata, R, Python) is named anywhere in the main text.
- (1) No dedicated 'Data Availability Statement' section appears in the extracted text; the only replication reference is a da
- (1) No sample weights are mentioned for any reported regression.
- (1) Online appendix content (referenced repeatedly as online Appendix Tables/Figures A1-A10 and Sections A-D) is a separate 
- (1) No formal balance-test statistic (e.g., a joint test or per-variable significance test) accompanies the descriptive-stat
- (1) No explicit discussion of attrition or of whether any villages or village-months were dropped after random assignment; t
- (1) No stated multiple-testing adjustment for the many individual covariates examined in the classification analysis, beyond
- (1) The paper repeatedly refers to a Supplemental Appendix for proofs and additional tables and figures; that document is no
- (1) No explicit ex ante power calculation or minimum-detectable-effect statement is given for the heterogeneity analysis in 
- (1) No discussion of multiple-testing adjustment despite pairwise comparisons across five policies presented in two tables.
- (1) No explicit discussion of standard-error clustering at any level; inference relies solely on the resampling test-sample 
- (1) No separate appendix or online supplementary section is present in this extracted text, although an online appendix is r
- (1) No explicit IRB or human-subjects ethics statement in the main text beyond the trial registry number.
- (1) No joint balance test or omnibus statistic reported for the three-arm randomization; only pairwise variable-by-variable 
- (1) No explicit preregistration, pre-analysis plan, or IRB/ethics statement appears in the main text; the paper analyzes exi
- (1) The Online Appendix, referenced repeatedly for proofs, additional tables (A.1-A.25 range), and extended robustness or me
- (1) No explicit clustering-level justification (choice of cluster variable) is stated anywhere in the main text; inference i
- (1) The main text does not itself state which software packages or versions were used to fit the random forest or linear-pro
- (1) No placebo-cutoff or placebo-outcome diagnostic in the regression-discontinuity or event-study sense is used, consistent
- (1) No discussion of few-cluster issues; cluster counts are only implied by the number of CDDA areas.
- (1) No preregistration or ethics statement (not expected for remote-sensing data).
- (1) No summary statistics table for the estimation sample in the main text; Table 1 is a balance table on a descriptive spli
- (1) Sample sizes for the main doubly-robust estimates are not reported in main-text tables; counts appear only as bar panels
- (1) Online appendices A-E are referenced throughout but are not part of the text file.
- (1) No justification given for the Newey-West lag length beyond citing the correction
- (1) No reasoning offered for the clustering dimensions in panel regressions (month and firm; day)
- (1) No multiple-testing adjustment discussed despite many sorts, proxies and market-phase splits

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
