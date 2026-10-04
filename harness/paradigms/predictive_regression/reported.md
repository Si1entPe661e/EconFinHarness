# Reported practice: `predictive_regression` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 2 paper notes (2 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | JFE: 1, RFS: 1 |
| year | 2026: 2 |
| papers with at least one observation in category | presentation_convention: 2, writing_structure: 2, replication_statement: 2, data_access: 2, design_statement: 1, sample_construction: 1, variable_construction: 1, inference_justification: 1, diagnostic_reported: 1, magnitude_interpretation: 1, limitation_stated: 1, external_validity: 1, specification_reporting: 1, mechanism_evidence: 1, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | full | yes | e0a76ce6a2d4 |
| rfs_2026_rfs_hhag042 | RFS | 2026 | full | yes | d63dc3bb1fac |

## Practices by category and tag


### data_access (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `commercial` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold; rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `data_restricted` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Beyond the deposited replication data, several auxiliary series used in the analysis are described as shared d; rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `administrative` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold |
| `in_main_text` | 1 | 50% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `public_use` | 1 | 50% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |

### design_statement (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.4-8 Section 2, Propositions 1-2: The identification strategy rests on a stylized CARA mean-variance model (Section 2) yielding two numbered pro |
| `estimand_named` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.4-8 Section 2, Propositions 1-2: The identification strategy rests on a stylized CARA mean-variance model (Section 2) yielding two numbered pro |

### diagnostic_reported (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5, Appendix Fig. A.1 referenced: A time-series plot of the intermediary shock variables is placed in an appendix figure and referenced from the |
| `in_main_text` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.12-13 Section 4.2.2, Table 5: Before interpreting the intermediary variable's incremental predictive power, the paper reports that the compo |
| `other:control_validity_check` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.12-13 Section 4.2.2, Table 5: Before interpreting the intermediary variable's incremental predictive power, the paper reports that the compo |

### external_validity (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.22-22 Section 6, Conclusion: In the conclusion, the author frames the equity-market estimates as a likely lower bound on the quantitative i |

### inference_justification (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `newey_west` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.9-13 Tables 4-5, 9-11, Figs. 3-6: Portfolio-level contemporaneous and predictive regressions report Newey-West standard errors using an automati |
| `no_justification_found` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: No discussion of multiple-hypothesis-testing adjustment appears anywhere in the text despite many coefficients |

### limitation_stated (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `interpretation_caveat` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and  |
| `measurement` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and  |

### magnitude_interpretation (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.13-13 Section 4.2.2: The variance-decomposition exercise bounding the share of conditional risk-premium variation attributable to t |
| `precision_discussed` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.9-18 throughout Section 4: Alongside point estimates, the paper repeatedly reports the associated t-statistics and describes estimates as |
| `sd_units` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.9-16 throughout Section 4: Coefficients are consistently interpreted relative to a one-standard-deviation change in the standardized shoc |

### mechanism_evidence (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Table 11: Panel regressions link the measure to contemporaneous and next-month trading volume and volatility as theory-i |
| `intermediate_outcomes` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Table 11: Panel regressions link the measure to contemporaneous and next-month trading volume and volatility as theory-i |

### other (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 50% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |
| `other:conflict_disclosure` | 1 | 50% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |

### presentation_convention (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_tables_numbered_a` | 1 | 50% | rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `in_appendix` | 1 | 50% | rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `notes_state_sample` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s |
| `notes_state_se` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s |
| `stars_used` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.9-16 Tables 4-11: Regression tables use a conventional multi-tier significance-star convention alongside t-statistics reported i |

### replication_statement (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_public` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title; rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `replication_package_cited` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title; rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `code_public` | 1 | 50% | rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `in_main_text` | 1 | 50% | rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `other:software_not_named_in_text` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: The manuscript text itself does not name the statistical software used to produce the reported estimates; the  |

### sample_construction (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj |
| `exclusions_justified` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: Microcap stocks, low-priced shares, and financial-sector SIC codes are excluded, each justified qualitatively  |
| `restricted_data_used` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Several inputs are described as obtained directly from other researchers rather than a public repository (a he |
| `sample_period_stated` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj |
| `unit_of_observation_stated` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj |

### specification_reporting (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `cluster_level_in_notes` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |
| `fe_listed_in_table` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |
| `in_main_text` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |
| `n_reported` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |
| `r2_reported` | 1 | 50% | rfs_2026_rfs_hhag042 p.32-33 Section 5.5; Equation (5); Table 11: The panel regression table lists controls, entity and time fixed effects as Yes rows, reports observations and |

### variable_construction (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:pls_composite_predictor` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.12-13 Section 4.2.2: A composite conditional risk-premium control is constructed via a two-step partial least squares procedure app |

### writing_structure (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_heavy` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `contribution_paragraph` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p; rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `design_before_data` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.4-8 Sections 2-4: The paper places its theoretical model and numbered propositions (Section 2) before the data description (Sect; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `mechanisms_after_main` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `results_previewed_in_intro` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul; rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `robustness_separate_section` | 2 | 100% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `in_footnote` | 1 | 50% | rfs_2026_rfs_hhag042 p.16-41 footnotes 11, 16, 17: Footnotes carry substantive supplementary analyses (an earnings-announcement test for the long leg, definition |
| `in_main_text` | 1 | 50% | rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `main_result_first` | 1 | 50% | rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `roadmap_paragraph` | 1 | 50% | jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 2 | jfe_2026_j_jfineco_2025_104223 s1.se.cluster_level (paper: Footnote states standard errors are clustered by date and double-clust / card: Card records se=twoway_cluster over ['permno','date'] for these specs.); rfs_2026_rfs_hhag042 s3.se (paper: Standard errors double-clustered by month and firm in Table 11 / card: s3.se twoway_cluster with cluster_entity=True; cluster_level null) |
| comparison_group | paper_only | 1 | jfe_2026_j_jfineco_2025_104223 s18 (paper: Table 6 reports six distinct named comparison groups (same size quinti / card: Card records a single spec (s18) for the underlying regression command) |
| controls | agree | 2 | jfe_2026_j_jfineco_2025_104223 s10 (paper: Table 8 (and Table 1) regressions control for profitability, CAPM beta / card: Card's spec s10 command lists control terms profit beta Gat bm lnme ln); rfs_2026_rfs_hhag042 s2.family_description (paper: Table 6 adds controls in three steps (4, 6, then 12 characteristics) b / card: s2 family of 3 specifications with increasing controls (5, 7, 12 chara) |
| data_source | paper_only | 1 | rfs_2026_rfs_hhag042 data (paper: Jensen, Kelly, Pedersen characteristics dataset (CRSP/Compustat), plus / card: data array empty) |
| diagnostic | agree | 1 | jfe_2026_j_jfineco_2025_104223 x1 (paper: Main text does not describe a graphical pre-trend check specifically f / card: Card records diagnostic x1 (pretrend_plot) for design d3 with status n) |
| estimator | agree | 4 | jfe_2026_j_jfineco_2025_104223 s1 (paper: Stock-level panel regressions in Tables 7-8 are estimated as OLS panel / card: Card records these specs as hdfe_ols estimated via Stata reghdfe with ); jfe_2026_j_jfineco_2025_104223 s14 (paper: Table 1 reports Fama-MacBeth time-series-averaged cross-sectional regr / card: Card records this as spec s14, estimator other:fama_macbeth, implement) |
| estimator | disagree | 1 | jfe_2026_j_jfineco_2025_104223 d3 / s18 (paper: Section 4.3 explicitly names the S&P 500 inclusion test a difference-i / card: Card classifies the same test under design d3 with method return_event) |
| fixed_effects | agree | 2 | jfe_2026_j_jfineco_2025_104223 s1.fe (paper: Text states that both time fixed effects (for common shocks) and stock / card: Card lists fe=['permno','date'] for the corresponding specs.); rfs_2026_rfs_hhag042 s3.formula_or_call (paper: Volume and volatility panel regressions include stock and time fixed e / card: s3 PanelOLS entity_effects=True, time_effects=True; fixed_effects fiel) |
| other | paper_only | 2 | jfe_2026_j_jfineco_2025_104223 heterogeneity (paper: Section 5 describes heterogeneity splits by hedge-fund holdings and by / card: Card's structured heterogeneity array is empty, so these splits are no); rfs_2026_rfs_hhag042 packages (paper: Investor models are random forests; robustness uses gradient boosted t / card: packages include scikit-learn and xgboost with usage unknown; no desig) |
| outputs | agree | 1 | rfs_2026_rfs_hhag042 s3.family_description (paper: Six panel columns: SUV, turnover, historical volatility at t and t+1 / card: s3 family: six outcomes SUV, turnover, realized volatility (current an) |
| robustness | paper_only | 2 | jfe_2026_j_jfineco_2025_104223 robustness (paper: Section 4.5 describes an extensive robustness battery (alternative cha / card: Card's structured robustness array is empty, so none of these checks a); rfs_2026_rfs_hhag042 robustness (paper: Robustness battery in Internet Appendix A to H (three-pass, nonlinear  / card: robustness array empty; run_analysis.py runs 16 analysis scripts in se) |
| sample | paper_only | 2 | jfe_2026_j_jfineco_2025_104223 pipeline.sample_restrictions (paper: Section 3 states explicit sample restrictions: share codes 10/11, NYSE / card: Card's pipeline.sample_restrictions field is an empty list, not captur); rfs_2026_rfs_hhag042 pipeline.sample_restrictions (paper: Common stocks on NYSE/AMEX/NASDAQ, excluding financials, utilities and / card: pipeline.sample_restrictions empty; s1 to s3 sample null) |
| se_type | agree | 3 | jfe_2026_j_jfineco_2025_104223 s15.se.se_type (paper: Portfolio-level contemporaneous and predictive regressions report Newe / card: Card records se_type=hac_newey_west for the corresponding ivreg2 specs); jfe_2026_j_jfineco_2025_104223 s18.se.se_type (paper: The S&P 500 inclusion table states its t-statistics are based on Drisc / card: Card records the same spec (s18) generically as se_type=hac_newey_west) |
| se_type | paper_only | 1 | rfs_2026_rfs_hhag042 specifications (paper: Earnings-announcement daily panel clusters standard errors by day (Tab / card: No specification for the daily announcement panel in the card) |
| weights | paper_only | 1 | jfe_2026_j_jfineco_2025_104223 s1.weights (paper: Text states portfolios are equal-weighted at baseline and separately r / card: Card records weights=None (null) for all listed specs, not distinguish) |
| weights | unknown | 1 | rfs_2026_rfs_hhag042 s1.weights (paper: Both equal- and value-weighted sorts reported in Table 3; conditional  / card: s1.weights null; helper function takes a weighting argument) |

## Gaps the readers reported

- (1) No pre-registration, IRB, or ethics statement is present; not applicable to this secondary-market asset-pricing study us
- (1) The paper's own text does not name the statistical software used for estimation; Stata/SAS are only identifiable from th
- (1) No first-stage or weak-instrument statistic appears anywhere in the main text, consistent with no stage of the empirical
- (1) The Online Appendix (Tables A.1-A.9, the Appendix A model extension, and Appendix B data details) referenced throughout 
- (1) No explicit multiple-hypothesis-testing correction is discussed despite many specifications and robustness tables being 
- (1) No justification given for the Newey-West lag length beyond citing the correction
- (1) No reasoning offered for the clustering dimensions in panel regressions (month and firm; day)
- (1) No multiple-testing adjustment discussed despite many sorts, proxies and market-phase splits
- (1) No software or package versions named in the paper text
- (1) R-squared and mean of the dependent variable not reported for Fama-MacBeth tables
- (1) Number of stocks per decile or per month not reported
- (1) Internet Appendix not available in the text file; its contents are known only from the prose summary in Section 4

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
