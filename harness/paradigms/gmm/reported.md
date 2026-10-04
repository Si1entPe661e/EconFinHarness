# Reported practice: `gmm` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 3 paper notes (3 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | ReStud: 2, JFE: 1 |
| year | 2023: 1, 2024: 1, 2026: 1 |
| papers with at least one observation in category | diagnostic_reported: 3, presentation_convention: 3, writing_structure: 3, replication_statement: 3, data_access: 3, design_statement: 2, other: 2, sample_construction: 1, variable_construction: 1, specification_reporting: 1, inference_justification: 1, heterogeneity_reported: 1, mechanism_evidence: 1, limitation_stated: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| jfe_2024_j_jfineco_2023_103746 | JFE | 2024 | full | yes | 9ff4e91a324b |
| restud_2026_restud_rdag013 | ReStud | 2026 | full | yes | b781b6e5a7dc |
| restud_90_5_11 | ReStud | 2023 | full | yes | b9f9dec1a4cb |

## Practices by category and tag


### data_access (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `commercial` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.3-13 throughout, footnotes and Table 8 note: Draws on standard commercial/licensed financial databases (implied by Compustat-style variable names) combined |
| `other:regulator_administrative_data` | 1 | 33% | restud_2026_restud_rdag013 p.8-9 Section 2.3: Data come from the state environmental regulator's administrative records (identifiers, scores, inspections, v |
| `public_use` | 1 | 33% | restud_90_5_11 p.14-15 footnote 14, Section 3: Main data are public-use CPS microdata from IPUMS with a dataset citation; the ACS is used for a self-replicat |
| `survey_collected` | 1 | 33% | restud_90_5_11 p.14-15 footnote 14, Section 3: Main data are public-use CPS microdata from IPUMS with a dataset citation; the ACS is used for a self-replicat |

### design_statement (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `estimand_named` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.1-2 Section 1, Introduction: Frames its estimand as a measurement/construct-validity question: whether HXZ/FF5F factor-model performance is |
| `identifying_assumption_explicit` | 1 | 33% | restud_2026_restud_rdag013 p.20-21 Section 5.3.1: Identification of the second-stage parameters is exposited informally through a simplified one-period, single- |
| `threats_discussed` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.2-16 Introduction and Conclusion: Explicitly declines to take a stance on whether findings reflect risk or mispricing, stating this cannot be re |

### diagnostic_reported (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 2 | 67% | jfe_2024_j_jfineco_2023_103746 p.11-12 Tables 6-7 notes: Reports sum-of-squared and mean-absolute pricing errors as the fit diagnostic for every stochastic-discount-fa; restud_2026_restud_rdag013 p.22-23 Table 5, Figure 4, Section 6.1: Model fit is assessed by a table listing each estimation moment with its simulated and empirical value, follow |
| `in_appendix` | 1 | 33% | restud_90_5_11 p.31-31 footnote 34, Appendix Table A15: For the structural model, an appendix robustness check calibrates two more parameters so the system is overide |
| `in_footnote` | 1 | 33% | restud_90_5_11 p.31-31 footnote 34, Appendix Table A15: For the structural model, an appendix robustness check calibrates two more parameters so the system is overide |
| `other:model_fit_moments_table` | 1 | 33% | restud_2026_restud_rdag013 p.22-23 Table 5, Figure 4, Section 6.1: Model fit is assessed by a table listing each estimation moment with its simulated and empirical value, follow |
| `other:pricing_error_fit_statistics` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.11-12 Tables 6-7 notes: Reports sum-of-squared and mean-absolute pricing errors as the fit diagnostic for every stochastic-discount-fa |
| `overid_test` | 1 | 33% | restud_90_5_11 p.31-31 footnote 34, Appendix Table A15: For the structural model, an appendix robustness check calibrates two more parameters so the system is overide |

### heterogeneity_reported (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `mechanism_motivated` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.10-12 Section 4, Tables 6-7: Organizes the macro-factor pricing results around a between-portfolio-group contrast, comparing which of twelv |
| `other:cross_portfolio_group_heterogeneity` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.10-12 Section 4, Tables 6-7: Organizes the macro-factor pricing results around a between-portfolio-group contrast, comparing which of twelv |

### inference_justification (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:identity_weighting_matrix_stated` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.10-10 Section 4, GMM setup: States that the GMM pricing tests use an identity weighting matrix at a first-stage estimation, a specific cho |

### limitation_stated (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_coverage` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.10-10 Section 4: Flags its review of the macroeconomic-shock literature underlying the chosen factor list as necessarily incomp |
| `identification_caveat` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.2-16 Introduction and Conclusion: States it is difficult to definitively conclude whether a factor model captures risk or mispricing absent a st |
| `interpretation_caveat` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.2-2 Section 1, Introduction: Explicitly declines to take a position on which specific driver of equity-financing costs (agency frictions, r |

### mechanism_evidence (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `ruled_out_alternatives` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.10-11 Section 4, Table 6 discussion: Partially rules out technology/productivity-shock explanations for the AG/INVT/AREC advantage by showing those |

### other (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:multi_step_estimation_described` | 1 | 33% | restud_2026_restud_rdag013 p.20-20 Section 5.2: Estimation is laid out as three explicit steps (offline calibration, simulated method of moments for firms wit |
| `other:software_not_named` | 1 | 33% | restud_90_5_11 p.1-34 whole main text: No statistical software or packages are named in the main text. |

### presentation_convention (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_tables_numbered_a` | 2 | 67% | restud_2026_restud_rdag013 p.7-28 various: Online appendix tables are referenced with an A- prefix and appendix sections by number throughout the main te; restud_90_5_11 p.3-33 Figures 1 to 4, Appendix Tables A1, A4: Figures include maps of state policy variation for example occupations, coefficient plots with confidence band |
| `stars_used` | 2 | 67% | jfe_2024_j_jfineco_2023_103746 p.4-15 Tables 1-10 notes: Uses the same stars convention in every table note, spelling out the same three conventional significance thre; restud_90_5_11 p.20-30 Tables 2 to 5 notes: Tables use three-level significance stars defined in notes; notes state the fixed effects, cluster level, samp |
| `summary_stats_table` | 2 | 67% | restud_2026_restud_rdag013 p.9-9 Table 1: A summary statistics table reports N, mean, standard deviation and the 1st and 99th percentiles for key variab; restud_90_5_11 p.3-33 Figures 1 to 4, Appendix Tables A1, A4: Figures include maps of state policy variation for example occupations, coefficient plots with confidence band |
| `coefficient_plot` | 1 | 33% | restud_90_5_11 p.3-33 Figures 1 to 4, Appendix Tables A1, A4: Figures include maps of state policy variation for example occupations, coefficient plots with confidence band |
| `map` | 1 | 33% | restud_90_5_11 p.3-33 Figures 1 to 4, Appendix Tables A1, A4: Figures include maps of state policy variation for example occupations, coefficient plots with confidence band |
| `notes_state_sample` | 1 | 33% | restud_90_5_11 p.20-30 Tables 2 to 5 notes: Tables use three-level significance stars defined in notes; notes state the fixed effects, cluster level, samp |
| `notes_state_se` | 1 | 33% | restud_90_5_11 p.20-30 Tables 2 to 5 notes: Tables use three-level significance stars defined in notes; notes state the fixed effects, cluster level, samp |

### replication_statement (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `code_public` | 3 | 100% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: States, in a Data availability statement, a Mendeley Data DOI as the location where the paper's code and data ; restud_2026_restud_rdag013 p.28-28 Data Availability: A Data Availability paragraph states that data and code are on Zenodo with a DOI. |
| `data_public` | 3 | 100% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: States, in a Data availability statement, a Mendeley Data DOI as the location where the paper's code and data ; restud_2026_restud_rdag013 p.28-28 Data Availability: A Data Availability paragraph states that data and code are on Zenodo with a DOI. |
| `replication_package_cited` | 3 | 100% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: States, in a Data availability statement, a Mendeley Data DOI as the location where the paper's code and data ; restud_2026_restud_rdag013 p.28-28 Data Availability: A Data Availability paragraph states that data and code are on Zenodo with a DOI. |
| `online_appendix_not_available` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.16-16 Appendix. Supplementary material: Points to supplementary material via the article's own DOI as a location separate from the Mendeley code/data  |
| `other:software_not_named` | 1 | 33% | restud_2026_restud_rdag013 p.1-29 whole paper: No software or package is named in the main text for estimation or regressions. |

### sample_construction (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: Names the external repository location of the underlying data and code in a Data availability statement rather |
| `other:no_dedicated_data_section` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Has no separate Data or Sample section; data sources, coverage, and construction procedures appear only in foo |

### specification_reporting (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:fit_statistics_reported` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.11-12 Tables 6-7: Reports sum-of-squared and mean-absolute pricing errors (annualized) in the GMM pricing tables in place of R2, |

### variable_construction (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `measurement_error_discussed` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.3-3 Section 1, footnote 8: Constructs total, physical, and intangible capital measures following a cited method that adds off-balance-she |
| `other:ar1_residualization` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.9-10 Section 4, macro-factor list: Transforms macroeconomic shock variables heterogeneously by source: several series use AR(1) residuals to isol |
| `other:survey_based_index_construction` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.14-14 Section 5, footnote 24: Constructs an aggregate overextrapolation index from survey-based return expectations via a recursively estima |
| `outcome_definition` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.3-3 Section 1, footnote 8: Constructs total, physical, and intangible capital measures following a cited method that adds off-balance-she |

### writing_structure (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 3 | 100% | jfe_2024_j_jfineco_2023_103746 p.1-2 Section 1, Introduction: Opens the introduction with a contribution paragraph framing the paper as challenging the theoretical interpre; restud_2026_restud_rdag013 p.2-6 Sections 1, 1.1, 1.2: The introduction previews the counterfactual findings, the mechanism decomposition and additional counterfactu |
| `results_previewed_in_intro` | 3 | 100% | jfe_2024_j_jfineco_2023_103746 p.1-3 Section 1, Introduction: Previews every major finding in the introduction in the order the later sections present them, with footnotes ; restud_2026_restud_rdag013 p.2-6 Sections 1, 1.1, 1.2: The introduction previews the counterfactual findings, the mechanism decomposition and additional counterfactu |
| `appendix_heavy` | 2 | 67% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Has no separate Robustness section; alternative-measure and alternative-specification checks are embedded as s; restud_90_5_11 p.5-33 Sections 2 to 9: Order is model, data, empirical strategy, reduced-form results (opportunity cost first, then wages, then hours |
| `mechanisms_after_main` | 2 | 67% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Organizes the paper as a chain of sections that each resolve one sub-question in sequence (which alternative m; restud_90_5_11 p.5-33 Sections 2 to 9: Order is model, data, empirical strategy, reduced-form results (opportunity cost first, then wages, then hours |
| `roadmap_paragraph` | 2 | 67% | jfe_2024_j_jfineco_2023_103746 p.1-3 Section 1, Introduction: Previews every major finding in the introduction in the order the later sections present them, with footnotes ; restud_90_5_11 p.2-5 Section 1: The introduction previews the design, main results, and structural conclusions, includes a literature contribu |
| `data_before_design` | 1 | 33% | restud_2026_restud_rdag013 p.6-8 Section 2: Institutional context precedes data, and the context section is organised as short definitional subsections (w |
| `design_before_data` | 1 | 33% | restud_90_5_11 p.5-33 Sections 2 to 9: Order is model, data, empirical strategy, reduced-form results (opportunity cost first, then wages, then hours |
| `other:context_section_with_definitional_subsections` | 1 | 33% | restud_2026_restud_rdag013 p.6-8 Section 2: Institutional context precedes data, and the context section is organised as short definitional subsections (w |
| `other:no_dedicated_robustness_section` | 1 | 33% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Has no separate Robustness section; alternative-measure and alternative-specification checks are embedded as s |
| `roadmap_absent` | 1 | 33% | restud_2026_restud_rdag013 p.2-6 Sections 1, 1.1, 1.2: The introduction previews the counterfactual findings, the mechanism decomposition and additional counterfactu |
| `robustness_separate_section` | 1 | 33% | restud_90_5_11 p.5-33 Sections 2 to 9: Order is model, data, empirical strategy, reduced-form results (opportunity cost first, then wages, then hours |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 1 | restud_90_5_11 s1.se.cluster_level (paper: Clustered at the state-occupation cell. / card: cluster on state_occ in s1 to s5.) |
| comparison_group | agree | 1 | jfe_2024_j_jfineco_2023_103746 d1.implementation_features (paper: Portfolio breakpoints throughout use NYSE cutoffs, e.g. NYSE quintile  / card: Design d1 implementation_features lists NYSE-based breakpoints for por) |
| controls | agree | 1 | jfe_2024_j_jfineco_2023_103746 d3.implementation_features (paper: Spanning regressions control for the remaining factors in the HXZ mode / card: Design d3 implementation_features records the AG factor added to HXZ () |
| controls | paper_only | 1 | restud_2026_restud_rdag013 s4.controls (paper: Table 2 adds environmental justice index and region FE in columns (2)  / card: s4 records only the baseline logit with scores and year/NAICS FE.) |
| data_source | agree | 2 | jfe_2024_j_jfineco_2023_103746 data (paper: The Data availability statement names a Mendeley Data DOI (10.17632/tz / card: The card's data array is empty, but the traced code path (code/mendele); restud_2026_restud_rdag013 s1.source (paper: Data and code on Zenodo (DOI 10.5281/zenodo.16987699). / card: Card file paths are under code/zenodo_16987699.) |
| data_source | paper_only | 1 | restud_90_5_11 s1.weights (paper: CPS basic monthly via IPUMS, ACS for self-replication, hand-collected  / card: Weights earnwt and wtfinl identify CPS; data source not otherwise reco) |
| diagnostic | paper_only | 4 | jfe_2024_j_jfineco_2023_103746 diagnostics (paper: GMM pricing tables report sum of squared pricing errors (SSQE) and mea / card: The card's diagnostics array is empty; no fit-statistic record was ext); restud_2026_restud_rdag013 x1 (paper: Model fit reported as moment comparison table and type-correlation bin / card: Diagnostics x1 balance and x2 first_stage marked unknown.) |
| diagnostic | agree | 1 | restud_90_5_11 x1 (paper: No pre-trend test; the design is cross-sectional two-way FE, not a pan / card: diag x1 pretrend_test not_found_in_scope.) |
| estimator | agree | 4 | jfe_2024_j_jfineco_2023_103746 d4.method (paper: Maximum Sharpe ratio comparison tests (Barillas and Shanken 2017; Bari / card: Design d4 records method other:maximum_sharpe_ratio_test with bias-adj); restud_2026_restud_rdag013 s4.estimator (paper: Table 2 uses logit regressions for inspection with year and NAICS sect / card: s4: logit inspection on log scores with i.year and i.naics_cat_fe.) |
| estimator | code_only | 2 | jfe_2024_j_jfineco_2023_103746 s1.estimator (paper: The 17 pages of main text read never name Fama-MacBeth or a two-step c / card: Design d2 and specifications s1-s2 record a Fama-MacBeth two-step cros); restud_2026_restud_rdag013 s1.estimator (paper: Table 3 deterrence regressions are described only as regressions of vi / card: s1 to s3 use ppmlhdfe (Poisson PPML) for n_violations.) |
| fixed_effects | agree | 2 | restud_2026_restud_rdag013 s2.fixed_effects (paper: Table 3 columns (2) and (3) use year and plant FE. / card: s2 and s3 absorb year and c_re_fe (plant identifier).); restud_90_5_11 s1.fe (paper: Occupation, state, industry, survey month-year FE plus demographic str / card: s1 fe = strata, statefip, occ, ind, my.) |
| fixed_effects | disagree | 1 | restud_2026_restud_rdag013 s1.fixed_effects (paper: Table 3 column (1) lists year FE and unit FE 'Category, Firm'. / card: s1 absorbs year, naics_2, c_fe, region_fe.) |
| outputs | paper_only | 2 | jfe_2024_j_jfineco_2023_103746 outputs.tables (paper: The main text contains ten numbered tables (Tables 1-10) and two figur / card: The card's outputs.tables and outputs.figures arrays are both empty.); restud_2026_restud_rdag013 outputs (paper: Tables 1 to 6 and Figures 1 to 5 in the main text. / card: Card records zero tables and figures.) |
| outputs | unknown | 1 | restud_90_5_11 outputs (paper: Five main tables and four figures plus appendix tables A1 to A15 and f / card: Card records 2 tables and 1 figure from files read (coverage partial).) |
| robustness | paper_only | 1 | jfe_2024_j_jfineco_2023_103746 robustness (paper: A dedicated 144-measure model-mining robustness exercise (Section 2.2) / card: The card's robustness array is empty; this exercise was not captured b) |
| robustness | agree | 1 | restud_90_5_11 s5 (paper: IV using indicators for large positive or negative residual licensed s / card: s5 ivreghdfe with i.residual_cat as instrument in robustness_subsample) |
| sample | paper_only | 2 | jfe_2024_j_jfineco_2023_103746 pipeline.sample_restrictions (paper: Table notes state regressions and portfolio tests use monthly data fro / card: pipeline.sample_restrictions records only a generic non-missing-return); restud_90_5_11 s1.sample (paper: Employed adults in a stated age band, universally licensed occupations / card: Specs condition on sample == 1 or wagesample == 1; the restriction's c) |
| sample | agree | 1 | restud_2026_restud_rdag013 s3.sample (paper: Column (3) of Table 3 restricts to plant-years with an inspection. / card: s3 conditions on inspection==1.) |
| se_type | agree | 1 | jfe_2024_j_jfineco_2023_103746 s2.se.type (paper: Spanning regressions (Tables 3-5) state standard errors are corrected  / card: Specification s2 (xtfmb_mion second step) records se.type=hac_newey_we) |
| se_type | code_only | 1 | jfe_2024_j_jfineco_2023_103746 s1.se.type (paper: No cross-sectional/iid standard-error procedure for a Fama-MacBeth fir / card: Specification s1 records se.type=iid as the default xtfmb_mion behavio) |
| se_type | unknown | 1 | restud_2026_restud_rdag013 s1.se (paper: No SE type or cluster level stated for Tables 2 and 3. / card: se null for all specs.) |
| se_type | paper_only | 1 | restud_2026_restud_rdag013 d2 (paper: Structural SEs from firm-level bootstrap (Table 4 notes). / card: No structural estimation spec recorded in the card.) |
| weights | paper_only | 1 | jfe_2024_j_jfineco_2023_103746 s5.weights (paper: Table titles and notes specify value-weighted (VW) portfolio returns a / card: None of the extracted specifications (s1, s2, s3, s5) record a weights) |
| weights | agree | 1 | restud_90_5_11 s1.weights, s2.weights (paper: Earnings weights for MORG wage sample, final weights otherwise; stated / card: s1 aw=earnwt for lwage; s2 and s4 aw=wtfinl for hours and education.) |

## Gaps the readers reported

- (1) No dedicated summary-statistics table (means/SDs of key variables) found anywhere in the 17 pages of main text read.
- (1) No explicit description in the main text of sample-construction filters typical of asset-pricing studies (e.g., minimum 
- (1) No justification given for the specific choice of a 12-lag Newey-West correction.
- (1) No discussion of cross-sectional dependence or standard-error clustering beyond the time-series Newey-West adjustment; n
- (1) No preregistration, IRB approval, or research-ethics statement; not applicable to this archival financial-data study and
- (1) No explicit external-validity or generalization discussion (e.g., to non-U.S. markets, periods outside 1972-2018, or tes
- (1) No back-of-envelope dollar-value, cost-benefit, or elasticity translation of the Sharpe-ratio or GMM pricing-error magni
- (1) Online appendix content (Section A, Section D, Tables E1-E14) referenced by footnote roughly a dozen times could not be 
- (1) No statement of standard error type or clustering level for the descriptive logit and deterrence regressions (Tables 2 a
- (1) No software or package named for estimation.
- (1) No preregistration or ethics statement (administrative data, none expected).
- (1) Online appendix not included in the text file; appendix robustness is known only through main-text references.
- (1) No explicit roadmap paragraph in the introduction.
- (1) No statistical software or package is named in the paper text.
- (1) R-squared and dependent-variable means are not reported in regression tables.
- (1) No IRB, preregistration, or ethics statement (secondary public data).
- (1) No formal first-stage or weak-IV statistic is reported for the IV robustness column in the main text.
- (1) Appendices A to E are online supplements not included in the text file; their content is known only from main-text refer

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
