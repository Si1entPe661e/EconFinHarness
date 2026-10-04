# Reported practice: `portfolio_sorts` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 4 paper notes (4 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | JFE: 2, RFS: 2 |
| year | 2024: 1, 2025: 1, 2026: 2 |
| papers with at least one observation in category | design_statement: 4, sample_construction: 4, variable_construction: 4, specification_reporting: 4, magnitude_interpretation: 4, presentation_convention: 4, writing_structure: 4, replication_statement: 4, data_access: 4, robustness_reported: 3, limitation_stated: 3, diagnostic_reported: 3, mechanism_evidence: 2, inference_justification: 2, heterogeneity_reported: 2, external_validity: 2, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| jfe_2024_j_jfineco_2023_103746 | JFE | 2024 | full | yes | 9ff4e91a324b |
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | full | yes | e0a76ce6a2d4 |
| rfs_2025_rfs_hhae056 | RFS | 2025 | full | yes | a8a927075f51 |
| rfs_2026_rfs_hhag042 | RFS | 2026 | full | yes | d63dc3bb1fac |

## Practices by category and tag


### data_access (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `commercial` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.3-13 throughout, footnotes and Table 8 note: Draws on standard commercial/licensed financial databases (implied by Compustat-style variable names) combined; jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold |
| `data_restricted` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Beyond the deposited replication data, several auxiliary series used in the analysis are described as shared d; rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `public_use` | 2 | 50% | rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data ; rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `administrative` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `web_scraped` | 1 | 25% | rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data  |

### design_statement (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `estimand_named` | 3 | 75% | jfe_2024_j_jfineco_2023_103746 p.1-2 Section 1, Introduction: Frames its estimand as a measurement/construct-validity question: whether HXZ/FF5F factor-model performance is; jfe_2026_j_jfineco_2025_104223 p.4-8 Section 2, Propositions 1-2: The identification strategy rests on a stylized CARA mean-variance model (Section 2) yielding two numbered pro |
| `design_variant_named` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.4-8 Section 2, Propositions 1-2: The identification strategy rests on a stylized CARA mean-variance model (Section 2) yielding two numbered pro; rfs_2026_rfs_hhag042 p.2-13 Introduction; Section 3 opening paragraph: The empirical object is a cross-sectional return-prediction test: whether a simulated disagreement measure (di |
| `identifying_assumption_explicit` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.7-8 Section 4.1, Eq. (8): The residualized intermediation measure is constructed so that cross-sectional variation in the sorting variab; rfs_2025_rfs_hhae056 p.8-14 Section 1.1 end; Section 2 opening and footnote 10: Portfolio formation is timed to the first day of the month after the list announcement so that the short-term  |
| `threats_discussed` | 2 | 50% | jfe_2024_j_jfineco_2023_103746 p.2-16 Introduction and Conclusion: Explicitly declines to take a stance on whether findings reflect risk or mispricing, stating this cannot be re; jfe_2026_j_jfineco_2025_104223 p.7-8 Section 4.1, Eq. (8): The residualized intermediation measure is constructed so that cross-sectional variation in the sorting variab |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.2-13 Introduction; Section 3 opening paragraph: The empirical object is a cross-sectional return-prediction test: whether a simulated disagreement measure (di |

### diagnostic_reported (papers with this category: 3/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 3 | 75% | jfe_2026_j_jfineco_2025_104223 p.8-8 Fig. 2: A figure plotting average characteristic quintiles over time for the top- and bottom-intermediation portfolios; rfs_2025_rfs_hhae056 p.10-12 Table 3; Figure 3; Section 1.2: Before the return tests the paper documents the size distribution of the portfolio firms against NYSE breakpoi |
| `balance_table` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.8-8 Fig. 2: A figure plotting average characteristic quintiles over time for the top- and bottom-intermediation portfolios |
| `in_appendix` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5, Appendix Fig. A.1 referenced: A time-series plot of the intermediary shock variables is placed in an appendix figure and referenced from the |
| `other:measure_validation` | 1 | 25% | rfs_2026_rfs_hhag042 p.22-30 Section 5.1 to 5.3; Figures 2, 3, 4; Tables 7, 8, 9: A long section validates the new measure against existing proxies: distribution of monthly rank correlations w |
| `other:portfolio_characteristics_table` | 1 | 25% | rfs_2026_rfs_hhag042 p.16-18 Section 3.2; Table 4: Before controlling for characteristics, the paper reports time-series averages of cross-sectional medians of f |
| `other:size_distribution_check` | 1 | 25% | rfs_2025_rfs_hhae056 p.10-12 Table 3; Figure 3; Section 1.2: Before the return tests the paper documents the size distribution of the portfolio firms against NYSE breakpoi |
| `other:state_dependence` | 1 | 25% | rfs_2026_rfs_hhag042 p.29-32 Section 5.4; Table 10: Time-variation checks split the sample at the median of many aggregate uncertainty, sentiment and factor-densi |
| `other:turnover_reported` | 1 | 25% | rfs_2025_rfs_hhae056 p.9-11 Tables 1 and 2; Figures 1 and 2: List turnover (additions and drops per year) and industry composition over time are tabulated and plotted to c |
| `summary_stats_table` | 1 | 25% | rfs_2025_rfs_hhae056 p.10-12 Table 3; Figure 3; Section 1.2: Before the return tests the paper documents the size distribution of the portfolio firms against NYSE breakpoi |

### external_validity (papers with this category: 2/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.22-22 Section 6, Conclusion: In the conclusion, the author frames the equity-market estimates as a likely lower bound on the quantitative i; rfs_2026_rfs_hhag042 p.10-22 Section 1.3; Section 4: International replication across developed and emerging markets is presented explicitly as evidence of externa |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.10-22 Section 1.3; Section 4: International replication across developed and emerging markets is presented explicitly as evidence of externa |

### heterogeneity_reported (papers with this category: 2/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `mechanism_motivated` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.17-19 Section 5.1, Table 9: The intermediation sort is re-formed separately using only hedge-fund holdings, and mutual-fund/advisor holdin; rfs_2026_rfs_hhag042 p.35-43 Tables 13, 15, 16: Heterogeneity is delivered through conditional (dependent) tercile-by-quintile sorts on mispricing score, borr |
| `split_sample` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.17-19 Section 5.1, Table 9: The intermediation sort is re-formed separately using only hedge-fund holdings, and mutual-fund/advisor holdin; rfs_2026_rfs_hhag042 p.35-43 Tables 13, 15, 16: Heterogeneity is delivered through conditional (dependent) tercile-by-quintile sorts on mispricing score, borr |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.35-43 Tables 13, 15, 16: Heterogeneity is delivered through conditional (dependent) tercile-by-quintile sorts on mispricing score, borr |

### inference_justification (papers with this category: 2/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `newey_west` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.9-13 Tables 4-5, 9-11, Figs. 3-6: Portfolio-level contemporaneous and predictive regressions report Newey-West standard errors using an automati; rfs_2026_rfs_hhag042 p.16-20 footnote 9; Section 3.4: A footnote states that all reported t-statistics are Newey-West adjusted with a fixed lag count to address het |
| `in_footnote` | 1 | 25% | rfs_2026_rfs_hhag042 p.16-20 footnote 9; Section 3.4: A footnote states that all reported t-statistics are Newey-West adjusted with a fixed lag count to address het |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.31-32 Table 10 notes; Section 5.4: Differences in the return spread between high and low uncertainty states are tested with a one-sided t-test, s |
| `no_justification_found` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: No discussion of multiple-hypothesis-testing adjustment appears anywhere in the text despite many coefficients |
| `other:one_sided_test` | 1 | 25% | rfs_2026_rfs_hhag042 p.31-32 Table 10 notes; Section 5.4: Differences in the return spread between high and low uncertainty states are tested with a one-sided t-test, s |

### limitation_stated (papers with this category: 3/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identification_caveat` | 2 | 50% | jfe_2024_j_jfineco_2023_103746 p.2-16 Introduction and Conclusion: States it is difficult to definitively conclude whether a factor model captures risk or mispricing absent a st; rfs_2025_rfs_hhae056 p.6-34 Introduction; Section 4: The authors acknowledge the absence of exogenous variation, concede that an omitted mispriced variable cannot  |
| `interpretation_caveat` | 2 | 50% | jfe_2024_j_jfineco_2023_103746 p.2-2 Section 1, Introduction: Explicitly declines to take a position on which specific driver of equity-financing costs (agency frictions, r; jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and  |
| `measurement` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and ; rfs_2025_rfs_hhae056 p.6-34 Introduction; Section 4: The authors acknowledge the absence of exogenous variation, concede that an omitted mispriced variable cannot  |

### magnitude_interpretation (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 1 | 25% | rfs_2025_rfs_hhae056 p.9-38 Section 1.2; Section 5: The number of firms per year is benchmarked against prior list-based anomaly studies, and the input-versus-out |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.32-38 Section 5.4; Section 6.1: The announcement-window effect is expressed as a percentage increase of the strategy spread relative to nonann |
| `other:cross_group_percent_change_comparison` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.13-14 Section 5, Table 8 discussion: Interprets the relative size of the debt-equity substitution effect through cross-group percent-change compari |
| `precision_discussed` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.9-18 throughout Section 4: Alongside point estimates, the paper repeatedly reports the associated t-statistics and describes estimates as |
| `relative_to_mean` | 1 | 25% | rfs_2026_rfs_hhag042 p.32-38 Section 5.4; Section 6.1: The announcement-window effect is expressed as a percentage increase of the strategy spread relative to nonann |
| `sd_units` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.9-16 throughout Section 4: Coefficients are consistently interpreted relative to a one-standard-deviation change in the standardized shoc |

### mechanism_evidence (papers with this category: 2/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `intermediate_outcomes` | 2 | 50% | jfe_2024_j_jfineco_2023_103746 p.13-14 Section 5, Table 8: Uses debt-versus-equity issuance behavior in high- versus low-sentiment periods as an intermediate-outcome tes; rfs_2026_rfs_hhag042 p.35-39 Section 6.1; Tables 13, 14: Mispricing versus risk is adjudicated by three steps: alphas across factor models, correlation with an existin |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.35-39 Section 6.1; Tables 13, 14: Mispricing versus risk is adjudicated by three steps: alphas across factor models, correlation with an existin |
| `model_guided` | 1 | 25% | rfs_2026_rfs_hhag042 p.33-35 Section 5.6; Equations (6) to (8); Table 12: The measure is decomposed into a model-disagreement part and an information-set part by re-expressing the beli |
| `ruled_out_alternatives` | 1 | 25% | rfs_2026_rfs_hhag042 p.35-39 Section 6.1; Tables 13, 14: Mispricing versus risk is adjudicated by three steps: alphas across factor models, correlation with an existin |

### other (papers with this category: 1/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |
| `other:conflict_disclosure` | 1 | 25% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |

### presentation_convention (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `stars_used` | 3 | 75% | jfe_2024_j_jfineco_2023_103746 p.4-15 Tables 1-10 notes: Uses the same stars convention in every table note, spelling out the same three conventional significance thre; jfe_2026_j_jfineco_2025_104223 p.9-16 Tables 4-11: Regression tables use a conventional multi-tier significance-star convention alongside t-statistics reported i |
| `summary_stats_table` | 3 | 75% | jfe_2026_j_jfineco_2025_104223 p.7-8 Tables 2-3: Summary statistics are split across two separate tables rather than combined into one: one reporting means and; rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share |
| `appendix_tables_numbered_a` | 2 | 50% | rfs_2025_rfs_hhae056 p.1-38 Title page note; Sections 2.1, 2.3, 2.4, 5: Supplementary results are referenced as Internet Appendix Table or Figure numbers; the appendix is hosted by t; rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `coefficient_plot` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.10-11 Figs. 3-6, Tables 4-5: Several main results are presented as coefficient plots across intermediation quintiles with shaded confidence; rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share |
| `notes_state_sample` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s; rfs_2026_rfs_hhag042 p.13-43 Tables 1 to 16 notes: Tables use three-level significance stars with t-statistics in parentheses; every table note restates sample p |
| `notes_state_se` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.10-11 Figs. 3-6, Tables 4-5: Several main results are presented as coefficient plots across intermediation quintiles with shaded confidence; rfs_2026_rfs_hhag042 p.13-43 Tables 1 to 16 notes: Tables use three-level significance stars with t-statistics in parentheses; every table note restates sample p |
| `in_appendix` | 1 | 25% | rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.13-43 Tables 1 to 16 notes: Tables use three-level significance stars with t-statistics in parentheses; every table note restates sample p |
| `online_appendix_not_available` | 1 | 25% | rfs_2025_rfs_hhae056 p.1-38 Title page note; Sections 2.1, 2.3, 2.4, 5: Supplementary results are referenced as Internet Appendix Table or Figure numbers; the appendix is hosted by t |
| `other:self_contained_table_notes` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.13-13 Table 8 note: Writes table notes to be self-contained, restating exact variable-construction formulas such as debt and equit |
| `raw_data_plot` | 1 | 25% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share |

### replication_statement (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: States, in a Data availability statement, a Mendeley Data DOI as the location where the paper's code and data ; jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title |
| `code_public` | 3 | 75% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: States, in a Data availability statement, a Mendeley Data DOI as the location where the paper's code and data ; rfs_2025_rfs_hhae056 p.39-39 Code Availability paragraph: A code availability statement at the end of the conclusion gives a Harvard Dataverse DOI for the replication c |
| `data_public` | 3 | 75% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: States, in a Data availability statement, a Mendeley Data DOI as the location where the paper's code and data ; jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `online_appendix_not_available` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.16-16 Appendix. Supplementary material: Points to supplementary material via the article's own DOI as a location separate from the Mendeley code/data  |
| `other:software_not_named_in_text` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: The manuscript text itself does not name the statistical software used to produce the reported estimates; the  |

### robustness_reported (papers with this category: 3/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_sample` | 3 | 75% | jfe_2024_j_jfineco_2023_103746 p.10-10 Section 4, footnote 20: Checks the debt-equity substitution finding in an unreported test using single-sorted rather than bivariate-so; jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5, Appendix Tables A.2-A.3: Separate robustness variants value-weight the portfolios instead of equal-weighting them and exclude the 2007- |
| `alt_specification` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.16-16 Section 4.5: Robustness checks reconstruct the residualized intermediation measure using both a stripped-down single-charac; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `in_appendix` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.16-16 Section 4.5: Robustness checks reconstruct the residualized intermediation measure using both a stripped-down single-charac; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `alt_control_group` | 1 | 25% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5, Appendix Tables A.4-A.5: The full robustness battery is repeated using holdings of the entire universe of 13F institutional investor ty |
| `alt_estimator` | 1 | 25% | rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `in_footnote` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.10-10 Section 4, footnote 20: Checks the debt-equity substitution finding in an unreported test using single-sorted rather than bivariate-so |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.33-46 Section 5.6; Table 12; Appendix C Table C1: Robustness of the measure to its own construction is shown in the main text by re-running sorts with four hype |
| `online_appendix_not_available` | 1 | 25% | rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `summarized_in_one_table` | 1 | 25% | rfs_2026_rfs_hhag042 p.33-46 Section 5.6; Table 12; Appendix C Table C1: Robustness of the measure to its own construction is shown in the main text by re-running sorts with four hype |

### sample_construction (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.16-16 Data availability: Names the external repository location of the underlying data and code in a Data availability statement rather; jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj |
| `sample_period_stated` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.7-13 Table 3-5 and Table 8 notes: States the sample period repeatedly in table notes rather than in a dedicated data section: spanning regressio; jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj |
| `exclusions_justified` | 3 | 75% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: Microcap stocks, low-priced shares, and financial-sector SIC codes are excluded, each justified qualitatively ; rfs_2025_rfs_hhae056 p.7-9 Sections 1.1 and 1.2; Table 1: The main signal is a commercial annual best-brands list; brands are mapped to stocks, analysis is at the stock |
| `unit_of_observation_stated` | 3 | 75% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj; rfs_2025_rfs_hhae056 p.7-9 Sections 1.1 and 1.2; Table 1: The main signal is a commercial annual best-brands list; brands are mapped to stocks, analysis is at the stock |
| `restricted_data_used` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Several inputs are described as obtained directly from other researchers rather than a public repository (a he; rfs_2026_rfs_hhag042 p.39-41 Section 6.2; footnote 17; Table 15 notes: Mechanism tests use proprietary short-lending fee data from IHS Markit and 13F institutional holdings from Tho |
| `data_public` | 1 | 25% | rfs_2026_rfs_hhag042 p.11-11 Section 2; footnote 7: Stock characteristics and returns come from a publicly available replication dataset (Jensen, Kelly, Pedersen) |
| `in_footnote` | 1 | 25% | rfs_2026_rfs_hhag042 p.11-11 Section 2; footnote 7: Stock characteristics and returns come from a publicly available replication dataset (Jensen, Kelly, Pedersen) |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.11-11 Section 2; footnote 7: Stock characteristics and returns come from a publicly available replication dataset (Jensen, Kelly, Pedersen) |
| `matching_or_linkage_described` | 1 | 25% | rfs_2025_rfs_hhae056 p.7-8 Section 1.1: The data section documents the vendor's list eligibility criteria and its three-step valuation methodology at  |
| `other:no_dedicated_data_section` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Has no separate Data or Sample section; data sources, coverage, and construction procedures appear only in foo |
| `other:nyse_breakpoints_stated` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.10-11 Table 6 note: States NYSE-based breakpoints (NYSE quintile cutoffs) as the portfolio-formation rule for every sorted-portfol |
| `web_scraped` | 1 | 25% | rfs_2025_rfs_hhae056 p.34-35 Section 4; Table 12 notes: For the text-based measure the authors download all annual filings from SEC EDGAR since digital filing became  |

### specification_reporting (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `weights_stated` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.11-13 Tables 6-8: States value-weighted portfolio returns and NYSE breakpoints directly in the table title or note for every sor; jfe_2026_j_jfineco_2025_104223 p.8-9 Section 4.2: The baseline portfolio tables are built on equal-weighted quintile portfolios, a weighting choice stated and j |
| `baseline_then_variants` | 2 | 50% | rfs_2025_rfs_hhae056 p.17-18 Table 5: The weighting table stacks the original equal-weighted alphas with alphas after excluding small caps, straight; rfs_2026_rfs_hhag042 p.14-15 Section 3.1; Table 3: The main portfolio table reports each decile and the high-minus-low spread with raw excess return and alphas f |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.14-15 Section 3.1; Table 3: The main portfolio table reports each decile and the high-minus-low spread with raw excess return and alphas f |
| `se_type_in_notes` | 1 | 25% | rfs_2026_rfs_hhag042 p.14-15 Section 3.1; Table 3: The main portfolio table reports each decile and the high-minus-low spread with raw excess return and alphas f |
| `stars_used` | 1 | 25% | rfs_2026_rfs_hhag042 p.14-15 Section 3.1; Table 3: The main portfolio table reports each decile and the high-minus-low spread with raw excess return and alphas f |

### variable_construction (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `standardized_index` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.1-9 Introduction footnote 3; Section 4.2: The composite intermediary-shock proxy is built by standardizing two previously published shock series separat; rfs_2026_rfs_hhag042 p.27-43 Section 5.3; Figure 4 notes; Section 6.3; Table 16 notes: Composite indices (a disagreement index and a limits-to-arbitrage index) are built by averaging or summing dec |
| `treatment_definition` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.7-8 Section 4.1, Eq. (8): The primary sorting variable is defined as the period-by-period cross-sectional residual from regressing insti; rfs_2025_rfs_hhae056 p.20-37 Section 2.3; Section 5: Brand capital and organization capital stocks are built by the perpetual inventory method, with parameters and |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.27-43 Section 5.3; Figure 4 notes; Section 6.3; Table 16 notes: Composite indices (a disagreement index and a limits-to-arbitrage index) are built by averaging or summing dec |
| `measurement_error_discussed` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.3-3 Section 1, footnote 8: Constructs total, physical, and intangible capital measures following a cited method that adds off-balance-she |
| `other:perpetual_inventory` | 1 | 25% | rfs_2025_rfs_hhae056 p.20-37 Section 2.3; Section 5: Brand capital and organization capital stocks are built by the perpetual inventory method, with parameters and |
| `other:survey_based_index_construction` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.14-14 Section 5, footnote 24: Constructs an aggregate overextrapolation index from survey-based return expectations via a recursively estima |
| `outcome_definition` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.3-3 Section 1, footnote 8: Constructs total, physical, and intangible capital measures following a cited method that adds off-balance-she |
| `winsorization` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.13-13 Table 8 note: Defines equity and debt issuance (mechanism outcomes) from standard balance-sheet items, scales them by lagged |

### writing_structure (papers with this category: 4/4)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.1-2 Section 1, Introduction: Opens the introduction with a contribution paragraph framing the paper as challenging the theoretical interpre; jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p |
| `mechanisms_after_main` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Organizes the paper as a chain of sections that each resolve one sub-question in sequence (which alternative m; jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p |
| `results_previewed_in_intro` | 4 | 100% | jfe_2024_j_jfineco_2023_103746 p.1-3 Section 1, Introduction: Previews every major finding in the introduction in the order the later sections present them, with footnotes ; jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul |
| `appendix_heavy` | 3 | 75% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Has no separate Robustness section; alternative-measure and alternative-specification checks are embedded as s; jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection |
| `design_before_data` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.4-8 Sections 2-4: The paper places its theoretical model and numbered propositions (Section 2) before the data description (Sect; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `main_result_first` | 2 | 50% | rfs_2025_rfs_hhae056 p.14-39 Sections 2 to 5: Empirical sections proceed from the headline factor regressions, to weighting sensitivity, to characteristic-c; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `roadmap_paragraph` | 2 | 50% | jfe_2024_j_jfineco_2023_103746 p.1-3 Section 1, Introduction: Previews every major finding in the introduction in the order the later sections present them, with footnotes ; jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul |
| `robustness_separate_section` | 2 | 50% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `data_before_design` | 1 | 25% | rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `in_footnote` | 1 | 25% | rfs_2026_rfs_hhag042 p.16-41 footnotes 11, 16, 17: Footnotes carry substantive supplementary analyses (an earnings-announcement test for the long leg, definition |
| `in_main_text` | 1 | 25% | rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `other:no_dedicated_robustness_section` | 1 | 25% | jfe_2024_j_jfineco_2023_103746 p.1-16 overall structure: Has no separate Robustness section; alternative-measure and alternative-specification checks are embedded as s |
| `other:subsection_summary_sentences` | 1 | 25% | rfs_2025_rfs_hhae056 p.16-39 Sections 2.1 to 5: Each subsection closes with an Overall sentence summarizing what the tests show, and each mechanism subsection |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 2 | jfe_2026_j_jfineco_2025_104223 s1.se.cluster_level (paper: Footnote states standard errors are clustered by date and double-clust / card: Card records se=twoway_cluster over ['permno','date'] for these specs.); rfs_2026_rfs_hhag042 s3.se (paper: Standard errors double-clustered by month and firm in Table 11 / card: s3.se twoway_cluster with cluster_entity=True; cluster_level null) |
| cluster_level | code_only | 1 | rfs_2025_rfs_hhae056 d4.implementation_features (paper: No standard error type or clustering stated for the announcement-retur / card: reg CAR bb, vce(cluster permno)) |
| comparison_group | agree | 1 | jfe_2024_j_jfineco_2023_103746 d1.implementation_features (paper: Portfolio breakpoints throughout use NYSE cutoffs, e.g. NYSE quintile  / card: Design d1 implementation_features lists NYSE-based breakpoints for por) |
| comparison_group | paper_only | 1 | jfe_2026_j_jfineco_2025_104223 s18 (paper: Table 6 reports six distinct named comparison groups (same size quinti / card: Card records a single spec (s18) for the underlying regression command) |
| controls | agree | 3 | jfe_2024_j_jfineco_2023_103746 d3.implementation_features (paper: Spanning regressions control for the remaining factors in the HXZ mode / card: Design d3 implementation_features records the AG factor added to HXZ (); jfe_2026_j_jfineco_2025_104223 s10 (paper: Table 8 (and Table 1) regressions control for profitability, CAPM beta / card: Card's spec s10 command lists control terms profit beta Gat bm lnme ln) |
| data_source | agree | 2 | jfe_2024_j_jfineco_2023_103746 data (paper: The Data availability statement names a Mendeley Data DOI (10.17632/tz / card: The card's data array is empty, but the traced code path (code/mendele); rfs_2025_rfs_hhae056 data (paper: CRSP, Compustat, IBES, Interbrand list, factor libraries, SEC EDGAR fi / card: CRSP, CRSP-Compustat merged, I/B/E/S, Factors.xlsx; no EDGAR or Interb) |
| data_source | paper_only | 1 | rfs_2026_rfs_hhag042 data (paper: Jensen, Kelly, Pedersen characteristics dataset (CRSP/Compustat), plus / card: data array empty) |
| diagnostic | agree | 2 | jfe_2026_j_jfineco_2025_104223 x1 (paper: Main text does not describe a graphical pre-trend check specifically f / card: Card records diagnostic x1 (pretrend_plot) for design d3 with status n); rfs_2025_rfs_hhae056 x1 (paper: No multiple-testing adjustment mentioned; results reported across five / card: x1 multiple_testing not_found_in_scope) |
| diagnostic | paper_only | 1 | jfe_2024_j_jfineco_2023_103746 diagnostics (paper: GMM pricing tables report sum of squared pricing errors (SSQE) and mea / card: The card's diagnostics array is empty; no fit-statistic record was ext) |
| estimator | agree | 7 | jfe_2024_j_jfineco_2023_103746 d4.method (paper: Maximum Sharpe ratio comparison tests (Barillas and Shanken 2017; Bari / card: Design d4 records method other:maximum_sharpe_ratio_test with bias-adj); jfe_2026_j_jfineco_2025_104223 s1 (paper: Stock-level panel regressions in Tables 7-8 are estimated as OLS panel / card: Card records these specs as hdfe_ols estimated via Stata reghdfe with ) |
| estimator | code_only | 1 | jfe_2024_j_jfineco_2023_103746 s1.estimator (paper: The 17 pages of main text read never name Fama-MacBeth or a two-step c / card: Design d2 and specifications s1-s2 record a Fama-MacBeth two-step cros) |
| estimator | disagree | 1 | jfe_2026_j_jfineco_2025_104223 d3 / s18 (paper: Section 4.3 explicitly names the S&P 500 inclusion test a difference-i / card: Card classifies the same test under design d3 with method return_event) |
| fixed_effects | agree | 2 | jfe_2026_j_jfineco_2025_104223 s1.fe (paper: Text states that both time fixed effects (for common shocks) and stock / card: Card lists fe=['permno','date'] for the corresponding specs.); rfs_2026_rfs_hhag042 s3.formula_or_call (paper: Volume and volatility panel regressions include stock and time fixed e / card: s3 PanelOLS entity_effects=True, time_effects=True; fixed_effects fiel) |
| fixed_effects | paper_only | 1 | rfs_2025_rfs_hhae056 s1.fixed_effects (paper: Year and industry fixed effects in earnings-surprise and CAR regressio / card: fixed_effects null in all recorded specs; Table 10/11 scripts read but) |
| other | paper_only | 2 | jfe_2026_j_jfineco_2025_104223 heterogeneity (paper: Section 5 describes heterogeneity splits by hedge-fund holdings and by / card: Card's structured heterogeneity array is empty, so these splits are no); rfs_2026_rfs_hhag042 packages (paper: Investor models are random forests; robustness uses gradient boosted t / card: packages include scikit-learn and xgboost with usage unknown; no desig) |
| outputs | agree | 2 | rfs_2025_rfs_hhae056 outputs.tables (paper: Thirteen numbered tables and five figures with stars and t-statistics / card: six table outputs via outreg2/esttab with coef and tstat; stars null; ); rfs_2026_rfs_hhag042 s3.family_description (paper: Six panel columns: SUV, turnover, historical volatility at t and t+1 / card: s3 family: six outcomes SUV, turnover, realized volatility (current an) |
| outputs | paper_only | 1 | jfe_2024_j_jfineco_2023_103746 outputs.tables (paper: The main text contains ten numbered tables (Tables 1-10) and two figur / card: The card's outputs.tables and outputs.figures arrays are both empty.) |
| robustness | paper_only | 4 | jfe_2024_j_jfineco_2023_103746 robustness (paper: A dedicated 144-measure model-mining robustness exercise (Section 2.2) / card: The card's robustness array is empty; this exercise was not captured b); jfe_2026_j_jfineco_2025_104223 robustness (paper: Section 4.5 describes an extensive robustness battery (alternative cha / card: Card's structured robustness array is empty, so none of these checks a) |
| sample | paper_only | 4 | jfe_2024_j_jfineco_2023_103746 pipeline.sample_restrictions (paper: Table notes state regressions and portfolio tests use monthly data fro / card: pipeline.sample_restrictions records only a generic non-missing-return); jfe_2026_j_jfineco_2025_104223 pipeline.sample_restrictions (paper: Section 3 states explicit sample restrictions: share codes 10/11, NYSE / card: Card's pipeline.sample_restrictions field is an empty list, not captur) |
| se_type | agree | 5 | jfe_2024_j_jfineco_2023_103746 s2.se.type (paper: Spanning regressions (Tables 3-5) state standard errors are corrected  / card: Specification s2 (xtfmb_mion second step) records se.type=hac_newey_we); jfe_2026_j_jfineco_2025_104223 s15.se.se_type (paper: Portfolio-level contemporaneous and predictive regressions report Newe / card: Card records se_type=hac_newey_west for the corresponding ivreg2 specs) |
| se_type | code_only | 1 | jfe_2024_j_jfineco_2023_103746 s1.se.type (paper: No cross-sectional/iid standard-error procedure for a Fama-MacBeth fir / card: Specification s1 records se.type=iid as the default xtfmb_mion behavio) |
| se_type | paper_only | 1 | rfs_2026_rfs_hhag042 specifications (paper: Earnings-announcement daily panel clusters standard errors by day (Tab / card: No specification for the daily announcement panel in the card) |
| weights | paper_only | 2 | jfe_2024_j_jfineco_2023_103746 s5.weights (paper: Table titles and notes specify value-weighted (VW) portfolio returns a / card: None of the extracted specifications (s1, s2, s3, s5) record a weights); jfe_2026_j_jfineco_2025_104223 s1.weights (paper: Text states portfolios are equal-weighted at baseline and separately r / card: Card records weights=None (null) for all listed specs, not distinguish) |
| weights | agree | 1 | rfs_2025_rfs_hhae056 s1.notes; s2.notes; s3.notes (paper: Equal-weighted baseline, straight value-weighted and capped value-weig / card: s1 mean collapse, s2 market-value weighted collapse, s3 capped value w) |
| weights | unknown | 1 | rfs_2026_rfs_hhag042 s1.weights (paper: Both equal- and value-weighted sorts reported in Table 3; conditional  / card: s1.weights null; helper function takes a weighting argument) |

## Gaps the readers reported

- (1) No dedicated summary-statistics table (means/SDs of key variables) found anywhere in the 17 pages of main text read.
- (1) No explicit description in the main text of sample-construction filters typical of asset-pricing studies (e.g., minimum 
- (1) No justification given for the specific choice of a 12-lag Newey-West correction.
- (1) No discussion of cross-sectional dependence or standard-error clustering beyond the time-series Newey-West adjustment; n
- (1) No preregistration, IRB approval, or research-ethics statement; not applicable to this archival financial-data study and
- (1) No explicit external-validity or generalization discussion (e.g., to non-U.S. markets, periods outside 1972-2018, or tes
- (1) No back-of-envelope dollar-value, cost-benefit, or elasticity translation of the Sharpe-ratio or GMM pricing-error magni
- (1) Online appendix content (Section A, Section D, Tables E1-E14) referenced by footnote roughly a dozen times could not be 
- (1) No pre-registration, IRB, or ethics statement is present; not applicable to this secondary-market asset-pricing study us
- (1) The paper's own text does not name the statistical software used for estimation; Stata/SAS are only identifiable from th
- (1) No first-stage or weak-instrument statistic appears anywhere in the main text, consistent with no stage of the empirical
- (1) The Online Appendix (Tables A.1-A.9, the Appendix A model extension, and Appendix B data details) referenced throughout 
- (1) No explicit multiple-hypothesis-testing correction is discussed despite many specifications and robustness tables being 
- (1) No standard error type or clustering justification is given for the earnings-surprise and announcement-return regression
- (1) Newey-West lag length is never stated in the text.
- (1) No data availability statement and no software named; only a code DOI.
- (1) No explicit roadmap paragraph in the introduction.
- (1) No formal validation test of the text-based measure beyond example firms and a correlation with the vendor portfolio.
- (1) Several robustness checks are described as unreported or not tabulated.
- (1) No justification given for the Newey-West lag length beyond citing the correction
- (1) No reasoning offered for the clustering dimensions in panel regressions (month and firm; day)
- (1) No multiple-testing adjustment discussed despite many sorts, proxies and market-phase splits
- (1) No software or package versions named in the paper text
- (1) R-squared and mean of the dependent variable not reported for Fama-MacBeth tables
- (1) Number of stocks per decile or per month not reported
- (1) Internet Appendix not available in the text file; its contents are known only from the prose summary in Section 4

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
