# Reported practice: `fama_macbeth` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 3 paper notes (3 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | RFS: 2, JFE: 1 |
| year | 2025: 1, 2026: 2 |
| papers with at least one observation in category | design_statement: 3, sample_construction: 3, variable_construction: 3, specification_reporting: 3, inference_justification: 3, robustness_reported: 3, presentation_convention: 3, writing_structure: 3, replication_statement: 3, data_access: 3, diagnostic_reported: 2, magnitude_interpretation: 2, limitation_stated: 2, external_validity: 1, heterogeneity_reported: 1, mechanism_evidence: 1, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | full | yes | e0a76ce6a2d4 |
| rfs_2025_rfs_hhae056 | RFS | 2025 | full | yes | a8a927075f51 |
| rfs_2026_rfs_hhag042 | RFS | 2026 | full | yes | d63dc3bb1fac |

## Practices by category and tag


### data_access (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `commercial` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold; rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data  |
| `data_restricted` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Beyond the deposited replication data, several auxiliary series used in the analysis are described as shared d; rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `public_use` | 2 | 67% | rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data ; rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `administrative` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The paper's primary inputs are commercial or subscription market and holdings databases (return data, 13F hold |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.1-41 Acknowledgements; Section 6.2; Table 8 notes: Core inputs are public-use (published characteristics dataset built on CRSP and Compustat); mechanism tests dr |
| `web_scraped` | 1 | 33% | rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data  |

### design_statement (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.4-8 Section 2, Propositions 1-2: The identification strategy rests on a stylized CARA mean-variance model (Section 2) yielding two numbered pro; rfs_2025_rfs_hhae056 p.14-19 Section 2, eq. (1) and eq. (2): The estimand is the abnormal return (alpha) of a long-only portfolio of top brands, estimated as the intercept |
| `estimand_named` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.4-8 Section 2, Propositions 1-2: The identification strategy rests on a stylized CARA mean-variance model (Section 2) yielding two numbered pro; rfs_2025_rfs_hhae056 p.14-19 Section 2, eq. (1) and eq. (2): The estimand is the abnormal return (alpha) of a long-only portfolio of top brands, estimated as the intercept |
| `threats_discussed` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.7-8 Section 4.1, Eq. (8): The residualized intermediation measure is constructed so that cross-sectional variation in the sorting variab; rfs_2025_rfs_hhae056 p.5-7 Introduction, alternative explanations paragraph: The introduction walks through alternative explanations (riskier intangible investment, organization capital,  |
| `identification_caveat` | 1 | 33% | rfs_2025_rfs_hhae056 p.5-7 Introduction, alternative explanations paragraph: The introduction walks through alternative explanations (riskier intangible investment, organization capital,  |
| `identifying_assumption_explicit` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.7-8 Section 4.1, Eq. (8): The residualized intermediation measure is constructed so that cross-sectional variation in the sorting variab |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.2-13 Introduction; Section 3 opening paragraph: The empirical object is a cross-sectional return-prediction test: whether a simulated disagreement measure (di |

### diagnostic_reported (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5, Appendix Fig. A.1 referenced: A time-series plot of the intermediary shock variables is placed in an appendix figure and referenced from the |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.22-30 Section 5.1 to 5.3; Figures 2, 3, 4; Tables 7, 8, 9: A long section validates the new measure against existing proxies: distribution of monthly rank correlations w |
| `other:measure_validation` | 1 | 33% | rfs_2026_rfs_hhag042 p.22-30 Section 5.1 to 5.3; Figures 2, 3, 4; Tables 7, 8, 9: A long section validates the new measure against existing proxies: distribution of monthly rank correlations w |

### external_validity (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.22-22 Section 6, Conclusion: In the conclusion, the author frames the equity-market estimates as a likely lower bound on the quantitative i |

### heterogeneity_reported (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `mechanism_motivated` | 1 | 33% | rfs_2025_rfs_hhae056 p.28-30 Section 3.4; Table 9: The only heterogeneity cut is the high versus low reported-intangibles split of best brands, which is explicit |
| `split_sample` | 1 | 33% | rfs_2025_rfs_hhae056 p.28-30 Section 3.4; Table 9: The only heterogeneity cut is the high versus low reported-intangibles split of best brands, which is explicit |

### inference_justification (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `newey_west` | 2 | 67% | rfs_2025_rfs_hhae056 p.15-22 Section 2.1; notes to Tables 4 to 9: Newey-West standard errors are used for factor regressions with the stated reason of allowing heteroskedastic ; rfs_2026_rfs_hhag042 p.16-20 footnote 9; Section 3.4: A footnote states that all reported t-statistics are Newey-West adjusted with a fixed lag count to address het |
| `in_footnote` | 1 | 33% | rfs_2026_rfs_hhag042 p.16-20 footnote 9; Section 3.4: A footnote states that all reported t-statistics are Newey-West adjusted with a fixed lag count to address het |
| `no_justification_found` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: No discussion of multiple-hypothesis-testing adjustment appears anywhere in the text despite many coefficients |

### limitation_stated (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `measurement` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and ; rfs_2025_rfs_hhae056 p.6-34 Introduction; Section 4: The authors acknowledge the absence of exogenous variation, concede that an omitted mispriced variable cannot  |
| `identification_caveat` | 1 | 33% | rfs_2025_rfs_hhae056 p.6-34 Introduction; Section 4: The authors acknowledge the absence of exogenous variation, concede that an omitted mispriced variable cannot  |
| `interpretation_caveat` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.10-10 Section 4.1: The author notes that the discount-rate and cashflow components of returns cannot be observed separately, and  |

### magnitude_interpretation (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 1 | 33% | rfs_2026_rfs_hhag042 p.16-33 Section 3.1; Section 3.4; Section 5.5: Economic magnitude of the regression slope is translated by multiplying the average slope by the decile spread |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.16-33 Section 3.1; Section 3.4; Section 5.5: Economic magnitude of the regression slope is translated by multiplying the average slope by the decile spread |
| `precision_discussed` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.9-18 throughout Section 4: Alongside point estimates, the paper repeatedly reports the associated t-statistics and describes estimates as |
| `sd_units` | 1 | 33% | rfs_2026_rfs_hhag042 p.16-33 Section 3.1; Section 3.4; Section 5.5: Economic magnitude of the regression slope is translated by multiplying the average slope by the decile spread |

### mechanism_evidence (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `heterogeneity_as_mechanism` | 1 | 33% | rfs_2025_rfs_hhae056 p.23-33 Section 3: Mechanisms are addressed in a dedicated section with five sub-tests: value of rebalancing, exposure to intangi |
| `intermediate_outcomes` | 1 | 33% | rfs_2025_rfs_hhae056 p.23-33 Section 3: Mechanisms are addressed in a dedicated section with five sub-tests: value of rebalancing, exposure to intangi |
| `ruled_out_alternatives` | 1 | 33% | rfs_2025_rfs_hhae056 p.23-33 Section 3: Mechanisms are addressed in a dedicated section with five sub-tests: value of rebalancing, exposure to intangi |

### other (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |
| `other:conflict_disclosure` | 1 | 33% | rfs_2026_rfs_hhag042 p.1-1 Acknowledgements: The front matter carries a disclaimer for an author's affiliation with an investment management firm, stating  |

### presentation_convention (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `notes_state_sample` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s; rfs_2025_rfs_hhae056 p.16-38 Tables 4 to 13: Tables use three-level significance stars with t-statistics in parentheses; notes restate the sample period, t |
| `notes_state_se` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.7-20 throughout, e.g. Tables 1, 4, 7: Table notes consistently reproduce the numbered estimating equation beneath the table itself, in addition to s; rfs_2025_rfs_hhae056 p.16-38 Tables 4 to 13: Tables use three-level significance stars with t-statistics in parentheses; notes restate the sample period, t |
| `stars_used` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.9-16 Tables 4-11: Regression tables use a conventional multi-tier significance-star convention alongside t-statistics reported i; rfs_2025_rfs_hhae056 p.16-38 Tables 4 to 13: Tables use three-level significance stars with t-statistics in parentheses; notes restate the sample period, t |
| `appendix_tables_numbered_a` | 2 | 67% | rfs_2025_rfs_hhae056 p.1-38 Title page note; Sections 2.1, 2.3, 2.4, 5: Supplementary results are referenced as Internet Appendix Table or Figure numbers; the appendix is hosted by t; rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `coefficient_plot` | 2 | 67% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share; rfs_2026_rfs_hhag042 p.12-29 Figures 1 to 4: Figures include a rolling-average time-series plot of the aggregate measure against other aggregates, a densit |
| `raw_data_plot` | 2 | 67% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share; rfs_2026_rfs_hhag042 p.12-29 Figures 1 to 4: Figures include a rolling-average time-series plot of the aggregate measure against other aggregates, a densit |
| `summary_stats_table` | 2 | 67% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share; rfs_2026_rfs_hhag042 p.13-43 Tables 1 to 16 notes: Tables use three-level significance stars with t-statistics in parentheses; every table note restates sample p |
| `in_appendix` | 1 | 33% | rfs_2026_rfs_hhag042 p.21-46 Section 4; Appendices A to C: Print appendices are lettered A to C with tables numbered A1, B1, C1; Internet Appendix material is referenced |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.13-43 Tables 1 to 16 notes: Tables use three-level significance stars with t-statistics in parentheses; every table note restates sample p |
| `online_appendix_not_available` | 1 | 33% | rfs_2025_rfs_hhae056 p.1-38 Title page note; Sections 2.1, 2.3, 2.4, 5: Supplementary results are referenced as Internet Appendix Table or Figure numbers; the appendix is hosted by t |

### replication_statement (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `replication_package_cited` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title; rfs_2025_rfs_hhae056 p.39-39 Code Availability paragraph: A code availability statement at the end of the conclusion gives a Harvard Dataverse DOI for the replication c |
| `code_public` | 2 | 67% | rfs_2025_rfs_hhae056 p.39-39 Code Availability paragraph: A code availability statement at the end of the conclusion gives a Harvard Dataverse DOI for the replication c; rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `data_public` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.22-22 Data availability section: A dedicated Data availability section states that replication materials are posted under a named dataset title; rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.11-44 Code and Data Availability; footnote 7: A Code and Data Availability statement after the conclusion gives a Harvard Dataverse DOI for replication code |
| `other:software_not_named_in_text` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.1-23 throughout: The manuscript text itself does not name the statistical software used to produce the reported estimates; the  |

### robustness_reported (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_specification` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.16-16 Section 4.5: Robustness checks reconstruct the residualized intermediation measure using both a stripped-down single-charac; rfs_2025_rfs_hhae056 p.20-21 Section 2.3 and footnote 14: Fama-MacBeth robustness covers industry-adjusted dependent variables, keeping observations with missing advert |
| `in_appendix` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.16-16 Section 4.5: Robustness checks reconstruct the residualized intermediation measure using both a stripped-down single-charac; rfs_2025_rfs_hhae056 p.20-21 Section 2.3 and footnote 14: Fama-MacBeth robustness covers industry-adjusted dependent variables, keeping observations with missing advert |
| `alt_sample` | 2 | 67% | rfs_2025_rfs_hhae056 p.20-21 Section 2.3 and footnote 14: Fama-MacBeth robustness covers industry-adjusted dependent variables, keeping observations with missing advert; rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `alt_control_group` | 1 | 33% | rfs_2025_rfs_hhae056 p.27-28 Section 3.3; Table 8: Overlap with a rival list-based anomaly (best workplaces) is handled by adding that portfolio's return as an e |
| `alt_estimator` | 1 | 33% | rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `in_footnote` | 1 | 33% | rfs_2025_rfs_hhae056 p.20-21 Section 2.3 and footnote 14: Fama-MacBeth robustness covers industry-adjusted dependent variables, keeping observations with missing advert |
| `in_main_text` | 1 | 33% | rfs_2025_rfs_hhae056 p.20-22 Section 2.4; Figure 4: Subperiod robustness is done by re-estimating excess returns within named macro regimes and within five-year b |
| `online_appendix_not_available` | 1 | 33% | rfs_2026_rfs_hhag042 p.20-22 Section 4; Internet Appendix A to H: A short robustness section summarizes in prose a battery of checks that live entirely in the Internet Appendix |
| `summarized_in_figure` | 1 | 33% | rfs_2025_rfs_hhae056 p.20-22 Section 2.4; Figure 4: Subperiod robustness is done by re-estimating excess returns within named macro regimes and within five-year b |

### sample_construction (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj; rfs_2025_rfs_hhae056 p.7-8 Section 1.1: The data section documents the vendor's list eligibility criteria and its three-step valuation methodology at  |
| `exclusions_justified` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: Microcap stocks, low-priced shares, and financial-sector SIC codes are excluded, each justified qualitatively ; rfs_2025_rfs_hhae056 p.19-19 Section 2.3 and footnote 13: For the cross-sectional regressions the universe is CRSP ordinary common shares on the three main exchanges, w |
| `sample_size_reported_per_table` | 2 | 67% | rfs_2025_rfs_hhae056 p.16-22 Tables 4 to 6 and Section 2.3: Each regression table reports the number of observations (months for factor regressions, stock-months for Fama; rfs_2026_rfs_hhag042 p.21-33 Table 6; Table 11: Observation counts are printed per column in the Fama-MacBeth table and in the panel regression table, but not |
| `unit_of_observation_stated` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj; rfs_2026_rfs_hhag042 p.11-13 Section 2; Table 1 notes: Sample is common stocks on NYSE, AMEX and NASDAQ; financial and utility firms are excluded, and low-priced sto |
| `data_public` | 1 | 33% | rfs_2026_rfs_hhag042 p.11-11 Section 2; footnote 7: Stock characteristics and returns come from a publicly available replication dataset (Jensen, Kelly, Pedersen) |
| `in_footnote` | 1 | 33% | rfs_2026_rfs_hhag042 p.11-11 Section 2; footnote 7: Stock characteristics and returns come from a publicly available replication dataset (Jensen, Kelly, Pedersen) |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.11-11 Section 2; footnote 7: Stock characteristics and returns come from a publicly available replication dataset (Jensen, Kelly, Pedersen) |
| `matching_or_linkage_described` | 1 | 33% | rfs_2025_rfs_hhae056 p.7-8 Section 1.1: The data section documents the vendor's list eligibility criteria and its three-step valuation methodology at  |
| `restricted_data_used` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.17-21 footnotes 4, 14, 26, 31: Several inputs are described as obtained directly from other researchers rather than a public repository (a he |
| `sample_period_stated` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.6-7 Section 3: The core sample links CRSP monthly stock returns for ordinary common shares on NYSE/Amex/Nasdaq, delisting-adj |

### specification_reporting (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `n_reported` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.7-7 Table 1: The Fama-MacBeth characteristics table reports the time-series-averaged coefficients, an observation count, an; rfs_2025_rfs_hhae056 p.20-22 Table 6 and notes: The Fama-MacBeth table adds controls progressively across five columns, labels the second column as the full m |
| `controls_progressive_columns` | 2 | 67% | rfs_2025_rfs_hhae056 p.20-22 Table 6 and notes: The Fama-MacBeth table adds controls progressively across five columns, labels the second column as the full m; rfs_2026_rfs_hhag042 p.19-21 Section 3.4; Table 6: The Fama-MacBeth table adds controls progressively across three columns, then swaps the dependent variable for |
| `r2_reported` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.7-7 Table 1: The Fama-MacBeth characteristics table reports the time-series-averaged coefficients, an observation count, an; rfs_2025_rfs_hhae056 p.20-22 Table 6 and notes: The Fama-MacBeth table adds controls progressively across five columns, labels the second column as the full m |
| `se_type_in_notes` | 2 | 67% | rfs_2025_rfs_hhae056 p.20-22 Table 6 and notes: The Fama-MacBeth table adds controls progressively across five columns, labels the second column as the full m; rfs_2026_rfs_hhag042 p.19-21 Section 3.4; Table 6: The Fama-MacBeth table adds controls progressively across three columns, then swaps the dependent variable for |
| `baseline_then_variants` | 1 | 33% | rfs_2025_rfs_hhae056 p.27-30 Tables 8 and 9: Later tables report only the coefficient of interest (alpha or the brand dummy) plus rows of Yes/No indicators |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.19-21 Section 3.4; Table 6: The Fama-MacBeth table adds controls progressively across three columns, then swaps the dependent variable for |
| `other:compact_alpha_only_tables` | 1 | 33% | rfs_2025_rfs_hhae056 p.27-30 Tables 8 and 9: Later tables report only the coefficient of interest (alpha or the brand dummy) plus rows of Yes/No indicators |

### variable_construction (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `winsorization` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.6-6 Section 3: Institutional-ownership percentages and firm characteristics used to construct the sorting variable are winsor; rfs_2025_rfs_hhae056 p.19-21 Section 2.3; Table 6 notes: Each characteristic control (beta, log size, book-to-market, momentum, asset growth, profitability, illiquidit |
| `treatment_definition` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.7-8 Section 4.1, Eq. (8): The primary sorting variable is defined as the period-by-period cross-sectional residual from regressing insti; rfs_2025_rfs_hhae056 p.19-23 Section 2.3 eq. (2); Section 3.1: The treatment is a dummy equal to one if the stock is in the most recent best-brands list; a later analysis sw |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.13-45 Table 1 notes; Table 6 notes; Table 11 notes; Table B1 notes: Winsorization thresholds differ by use: summary statistics winsorize both tails at one level, regression contr |
| `logs_or_ihs` | 1 | 33% | rfs_2025_rfs_hhae056 p.19-21 Section 2.3; Table 6 notes: Each characteristic control (beta, log size, book-to-market, momentum, asset growth, profitability, illiquidit |
| `other:median_split` | 1 | 33% | rfs_2025_rfs_hhae056 p.29-29 Section 3.4 and footnote 19: To separate internally versus externally built brands, the best-brand dummy is split into two dummies by a yea |
| `other:perpetual_inventory` | 1 | 33% | rfs_2025_rfs_hhae056 p.20-37 Section 2.3; Section 5: Brand capital and organization capital stocks are built by the perpetual inventory method, with parameters and |
| `outcome_definition` | 1 | 33% | rfs_2026_rfs_hhag042 p.13-44 Table 1 notes; Section 3.4; Appendix A Table A1: Control variable definitions and their source papers are given in the Table 1 notes and again in an appendix t |

### writing_structure (papers with this category: 3/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p; rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `mechanisms_after_main` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.3-17 Section 1.1; Section 5: Mechanism and alternative-explanation tests are organized into their own numbered section following the main p; rfs_2025_rfs_hhae056 p.14-39 Sections 2 to 5: Empirical sections proceed from the headline factor regressions, to weighting sensitivity, to characteristic-c |
| `results_previewed_in_intro` | 3 | 100% | jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul; rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `appendix_heavy` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `design_before_data` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.4-8 Sections 2-4: The paper places its theoretical model and numbered propositions (Section 2) before the data description (Sect; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `main_result_first` | 2 | 67% | rfs_2025_rfs_hhae056 p.14-39 Sections 2 to 5: Empirical sections proceed from the headline factor regressions, to weighting sensitivity, to characteristic-c; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `robustness_separate_section` | 2 | 67% | jfe_2026_j_jfineco_2025_104223 p.16-17 Section 4.5: Robustness checks are collected into a dedicated numbered subsection distinct from the main results subsection; rfs_2026_rfs_hhag042 p.6-46 Sections 1 to 7: Order is model of beliefs, then data, then main sorts and regressions, then a short robustness section pointin |
| `data_before_design` | 1 | 33% | rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `in_footnote` | 1 | 33% | rfs_2026_rfs_hhag042 p.16-41 footnotes 11, 16, 17: Footnotes carry substantive supplementary analyses (an earnings-announcement test for the long leg, definition |
| `in_main_text` | 1 | 33% | rfs_2026_rfs_hhag042 p.2-22 Introduction; Section 5 opening: The introduction previews headline results with numbers and organizes the paper around three enumerated contri |
| `other:subsection_summary_sentences` | 1 | 33% | rfs_2025_rfs_hhae056 p.16-39 Sections 2.1 to 5: Each subsection closes with an Overall sentence summarizing what the tests show, and each mechanism subsection |
| `roadmap_paragraph` | 1 | 33% | jfe_2026_j_jfineco_2025_104223 p.1-3 Section 1: The introduction previews the direction and qualitative pattern of the main empirical results before the resul |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 2 | jfe_2026_j_jfineco_2025_104223 s1.se.cluster_level (paper: Footnote states standard errors are clustered by date and double-clust / card: Card records se=twoway_cluster over ['permno','date'] for these specs.); rfs_2026_rfs_hhag042 s3.se (paper: Standard errors double-clustered by month and firm in Table 11 / card: s3.se twoway_cluster with cluster_entity=True; cluster_level null) |
| cluster_level | code_only | 1 | rfs_2025_rfs_hhae056 d4.implementation_features (paper: No standard error type or clustering stated for the announcement-retur / card: reg CAR bb, vce(cluster permno)) |
| comparison_group | paper_only | 1 | jfe_2026_j_jfineco_2025_104223 s18 (paper: Table 6 reports six distinct named comparison groups (same size quinti / card: Card records a single spec (s18) for the underlying regression command) |
| controls | agree | 2 | jfe_2026_j_jfineco_2025_104223 s10 (paper: Table 8 (and Table 1) regressions control for profitability, CAPM beta / card: Card's spec s10 command lists control terms profit beta Gat bm lnme ln); rfs_2026_rfs_hhag042 s2.family_description (paper: Table 6 adds controls in three steps (4, 6, then 12 characteristics) b / card: s2 family of 3 specifications with increasing controls (5, 7, 12 chara) |
| data_source | agree | 1 | rfs_2025_rfs_hhae056 data (paper: CRSP, Compustat, IBES, Interbrand list, factor libraries, SEC EDGAR fi / card: CRSP, CRSP-Compustat merged, I/B/E/S, Factors.xlsx; no EDGAR or Interb) |
| data_source | paper_only | 1 | rfs_2026_rfs_hhag042 data (paper: Jensen, Kelly, Pedersen characteristics dataset (CRSP/Compustat), plus / card: data array empty) |
| diagnostic | agree | 2 | jfe_2026_j_jfineco_2025_104223 x1 (paper: Main text does not describe a graphical pre-trend check specifically f / card: Card records diagnostic x1 (pretrend_plot) for design d3 with status n); rfs_2025_rfs_hhae056 x1 (paper: No multiple-testing adjustment mentioned; results reported across five / card: x1 multiple_testing not_found_in_scope) |
| estimator | agree | 6 | jfe_2026_j_jfineco_2025_104223 s1 (paper: Stock-level panel regressions in Tables 7-8 are estimated as OLS panel / card: Card records these specs as hdfe_ols estimated via Stata reghdfe with ); jfe_2026_j_jfineco_2025_104223 s14 (paper: Table 1 reports Fama-MacBeth time-series-averaged cross-sectional regr / card: Card records this as spec s14, estimator other:fama_macbeth, implement) |
| estimator | disagree | 1 | jfe_2026_j_jfineco_2025_104223 d3 / s18 (paper: Section 4.3 explicitly names the S&P 500 inclusion test a difference-i / card: Card classifies the same test under design d3 with method return_event) |
| fixed_effects | agree | 2 | jfe_2026_j_jfineco_2025_104223 s1.fe (paper: Text states that both time fixed effects (for common shocks) and stock / card: Card lists fe=['permno','date'] for the corresponding specs.); rfs_2026_rfs_hhag042 s3.formula_or_call (paper: Volume and volatility panel regressions include stock and time fixed e / card: s3 PanelOLS entity_effects=True, time_effects=True; fixed_effects fiel) |
| fixed_effects | paper_only | 1 | rfs_2025_rfs_hhae056 s1.fixed_effects (paper: Year and industry fixed effects in earnings-surprise and CAR regressio / card: fixed_effects null in all recorded specs; Table 10/11 scripts read but) |
| other | paper_only | 2 | jfe_2026_j_jfineco_2025_104223 heterogeneity (paper: Section 5 describes heterogeneity splits by hedge-fund holdings and by / card: Card's structured heterogeneity array is empty, so these splits are no); rfs_2026_rfs_hhag042 packages (paper: Investor models are random forests; robustness uses gradient boosted t / card: packages include scikit-learn and xgboost with usage unknown; no desig) |
| outputs | agree | 2 | rfs_2025_rfs_hhae056 outputs.tables (paper: Thirteen numbered tables and five figures with stars and t-statistics / card: six table outputs via outreg2/esttab with coef and tstat; stars null; ); rfs_2026_rfs_hhag042 s3.family_description (paper: Six panel columns: SUV, turnover, historical volatility at t and t+1 / card: s3 family: six outcomes SUV, turnover, realized volatility (current an) |
| robustness | paper_only | 3 | jfe_2026_j_jfineco_2025_104223 robustness (paper: Section 4.5 describes an extensive robustness battery (alternative cha / card: Card's structured robustness array is empty, so none of these checks a); rfs_2025_rfs_hhae056 robustness (paper: Weighting, intangible factors, best-workplaces overlap, subperiods, al / card: robustness array empty) |
| sample | paper_only | 3 | jfe_2026_j_jfineco_2025_104223 pipeline.sample_restrictions (paper: Section 3 states explicit sample restrictions: share codes 10/11, NYSE / card: Card's pipeline.sample_restrictions field is an empty list, not captur); rfs_2025_rfs_hhae056 s1.sample (paper: CRSP common shares on NYSE/Amex/Nasdaq, minimum monthly returns per ye / card: sample field null for all specs) |
| se_type | agree | 4 | jfe_2026_j_jfineco_2025_104223 s15.se.se_type (paper: Portfolio-level contemporaneous and predictive regressions report Newe / card: Card records se_type=hac_newey_west for the corresponding ivreg2 specs); jfe_2026_j_jfineco_2025_104223 s18.se.se_type (paper: The S&P 500 inclusion table states its t-statistics are based on Drisc / card: Card records the same spec (s18) generically as se_type=hac_newey_west) |
| se_type | paper_only | 1 | rfs_2026_rfs_hhag042 specifications (paper: Earnings-announcement daily panel clusters standard errors by day (Tab / card: No specification for the daily announcement panel in the card) |
| weights | paper_only | 1 | jfe_2026_j_jfineco_2025_104223 s1.weights (paper: Text states portfolios are equal-weighted at baseline and separately r / card: Card records weights=None (null) for all listed specs, not distinguish) |
| weights | agree | 1 | rfs_2025_rfs_hhae056 s1.notes; s2.notes; s3.notes (paper: Equal-weighted baseline, straight value-weighted and capped value-weig / card: s1 mean collapse, s2 market-value weighted collapse, s3 capped value w) |
| weights | unknown | 1 | rfs_2026_rfs_hhag042 s1.weights (paper: Both equal- and value-weighted sorts reported in Table 3; conditional  / card: s1.weights null; helper function takes a weighting argument) |

## Gaps the readers reported

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
