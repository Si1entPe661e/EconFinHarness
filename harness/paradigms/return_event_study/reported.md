# Reported practice: `return_event_study` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 5 paper notes (5 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | RFS: 3, JFE: 2 |
| year | 2024: 2, 2025: 2, 2026: 1 |
| papers with at least one observation in category | sample_construction: 5, variable_construction: 4, magnitude_interpretation: 4, presentation_convention: 4, specification_reporting: 3, mechanism_evidence: 3, writing_structure: 3, data_access: 3, design_statement: 2, diagnostic_reported: 2, robustness_reported: 2, limitation_stated: 2, inference_justification: 2, replication_statement: 1, heterogeneity_reported: 1, other: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| jfe_2024_j_jfineco_2024_103809 | JFE | 2024 | full | yes | 3776fdfeb8c7 |
| jfe_2025_j_jfineco_2025_104150 | JFE | 2025 | full | yes | d509ecfbe6d0 |
| rfs_2024_rfs_hhae045 | RFS | 2024 | full | yes | 5e68c13b1e2d |
| rfs_2025_rfs_hhae056 | RFS | 2025 | full | yes | a8a927075f51 |
| rfs_2026_rfs_hhaf081 | RFS | 2026 | full | yes | 34b87230ff18 |

## Practices by category and tag


### data_access (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `commercial` | 3 | 60% | rfs_2024_rfs_hhae045 p.13-42 Sections 2.1, 3.1, footnote 20: Data come from commercial databases (ISS Voting Analytics, CRSP, Compustat, IBES, Thomson 13-F, WRDS SEC Analy; rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data  |
| `data_restricted` | 2 | 40% | rfs_2024_rfs_hhae045 p.13-42 Sections 2.1, 3.1, footnote 20: Data come from commercial databases (ISS Voting Analytics, CRSP, Compustat, IBES, Thomson 13-F, WRDS SEC Analy; rfs_2026_rfs_hhaf081 p.6-41 Section 1.1; Appendix Table A1: All primary text data and most firm variables come from commercial vendors (Thomson One, Capital IQ, Revelio L |
| `linked_records` | 2 | 40% | rfs_2024_rfs_hhae045 p.13-42 Sections 2.1, 3.1, footnote 20: Data come from commercial databases (ISS Voting Analytics, CRSP, Compustat, IBES, Thomson 13-F, WRDS SEC Analy; rfs_2026_rfs_hhaf081 p.6-41 Section 1.1; Appendix Table A1: All primary text data and most firm variables come from commercial vendors (Thomson One, Capital IQ, Revelio L |
| `public_use` | 2 | 40% | rfs_2024_rfs_hhae045 p.13-42 Sections 2.1, 3.1, footnote 20: Data come from commercial databases (ISS Voting Analytics, CRSP, Compustat, IBES, Thomson 13-F, WRDS SEC Analy; rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data  |
| `web_scraped` | 1 | 20% | rfs_2025_rfs_hhae056 p.7-34 Sections 1.1, 2.3, 3.2 footnote 16, 3.5, 4: Inputs are commercial databases (CRSP, Compustat, IBES), a commercial vendor's public brand list, factor data  |

### design_statement (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `estimand_named` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.6-7 Section 4.1: The short-run analysis is framed as a standard event-study design estimating cumulative abnormal returns aroun |
| `in_main_text` | 1 | 20% | rfs_2024_rfs_hhae045 p.9-13 Sections 1.3, 1.4: Hypotheses are numbered (H1 to H4b) and derived from institutional theory before any data are shown; one hypot |
| `other:hypotheses_formalized` | 1 | 20% | rfs_2024_rfs_hhae045 p.9-13 Sections 1.3, 1.4: Hypotheses are numbered (H1 to H4b) and derived from institutional theory before any data are shown; one hypot |
| `other:rd_like_regression` | 1 | 20% | rfs_2024_rfs_hhae045 p.43-43 Section 4.6: The event-study regression controls for the running variable within the narrow band and is described as functi |

### diagnostic_reported (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `placebo_outcomes` | 2 | 40% | jfe_2024_j_jfineco_2024_103809 p.8-9 Discussion around Table 2 and Appendix Table A.7: The paper reports a placebo-style check across other cabinet changes during the period, most of which the text; rfs_2025_rfs_hhae056 p.14-14 footnote 10: A footnote reports checking the announcement-day return of list inclusion to rule out a discount-rate shock st |
| `in_appendix` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-9 Discussion around Table 2 and Appendix Table A.7: The paper reports a placebo-style check across other cabinet changes during the period, most of which the text |
| `in_footnote` | 1 | 20% | rfs_2025_rfs_hhae056 p.14-14 footnote 10: A footnote reports checking the announcement-day return of list inclusion to rule out a discount-rate shock st |

### heterogeneity_reported (papers with this category: 1/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `interaction` | 1 | 20% | rfs_2026_rfs_hhaf081 p.35-37 Section 4.2; Table 9 columns 2 to 5: Heterogeneity in market reaction is examined through interactions of tone with an indicator for the deepest ca |
| `mechanism_motivated` | 1 | 20% | rfs_2026_rfs_hhaf081 p.35-37 Section 4.2; Table 9 columns 2 to 5: Heterogeneity in market reaction is examined through interactions of tone with an indicator for the deepest ca |

### inference_justification (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_justification_found` | 2 | 40% | rfs_2025_rfs_hhae056 p.31-33 Tables 10 and 11: For the earnings-surprise and announcement-return panel regressions the tables give t-statistics but the text ; rfs_2026_rfs_hhaf081 p.14-36 Notes to Tables 3, 4, 6, 7, 8, 9: Firm-level clustering is used for firm-year regressions and double clustering by firm and analyst for report-l |
| `cluster_at_unit_level` | 1 | 20% | rfs_2026_rfs_hhaf081 p.14-36 Notes to Tables 3, 4, 6, 7, 8, 9: Firm-level clustering is used for firm-year regressions and double clustering by firm and analyst for report-l |
| `twoway_cluster` | 1 | 20% | rfs_2026_rfs_hhaf081 p.14-36 Notes to Tables 3, 4, 6, 7, 8, 9: Firm-level clustering is used for firm-year regressions and double clustering by firm and analyst for report-l |

### limitation_stated (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `measurement` | 2 | 40% | rfs_2024_rfs_hhae045 p.5-5 Introduction, footnote 3: The introduction has a limitations paragraph: reliance on voluntary disclosure as a proxy for actual engagemen; rfs_2025_rfs_hhae056 p.6-34 Introduction; Section 4: The authors acknowledge the absence of exogenous variation, concede that an omitted mispriced variable cannot  |
| `identification_caveat` | 1 | 20% | rfs_2025_rfs_hhae056 p.6-34 Introduction; Section 4: The authors acknowledge the absence of exogenous variation, concede that an omitted mispriced variable cannot  |
| `interpretation_caveat` | 1 | 20% | rfs_2024_rfs_hhae045 p.5-5 Introduction, footnote 3: The introduction has a limitations paragraph: reliance on voluntary disclosure as a proxy for actual engagemen |

### magnitude_interpretation (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `compared_to_literature` | 3 | 60% | jfe_2024_j_jfineco_2024_103809 p.8-8 Section 5.1 discussion of Table 2: The short-run reaction around the single most surprising episode is explicitly compared to a behavioral-financ; rfs_2025_rfs_hhae056 p.15-33 Section 2.1; Section 3.5: Monthly alphas are translated into annual and cumulative excess returns over the sample; the announcement-retu |
| `back_of_envelope` | 1 | 20% | rfs_2025_rfs_hhae056 p.15-33 Section 2.1; Section 3.5: Monthly alphas are translated into annual and cumulative excess returns over the sample; the announcement-retu |
| `monetary_terms` | 1 | 20% | rfs_2026_rfs_hhaf081 p.33-37 Section 4.1 and 4.2; footnotes 10 to 15: Economic significance is stated as a one-unit tone change relative to the sample mean of the outcome, one SD c |
| `other:benchmark_against_nonculture_tone` | 1 | 20% | rfs_2026_rfs_hhaf081 p.33-37 Section 4.1, 4.2: The culture tone effect is benchmarked against the effect of nonculture tone in the same regression, with the  |
| `other:calculation_shown_in_footnote` | 1 | 20% | rfs_2026_rfs_hhaf081 p.33-37 Section 4.1 and 4.2; footnotes 10 to 15: Economic significance is stated as a one-unit tone change relative to the sample mean of the outcome, one SD c |
| `other:estimators_compared` | 1 | 20% | rfs_2024_rfs_hhae045 p.42-43 Sections 4.5, 4.6: Magnitudes from the staggered DiD and the standard panel are compared side by side, and a null result in the e |
| `precision_discussed` | 1 | 20% | rfs_2024_rfs_hhae045 p.42-43 Sections 4.5, 4.6: Magnitudes from the staggered DiD and the standard panel are compared side by side, and a null result in the e |
| `relative_to_mean` | 1 | 20% | rfs_2026_rfs_hhaf081 p.33-37 Section 4.1 and 4.2; footnotes 10 to 15: Economic significance is stated as a one-unit tone change relative to the sample mean of the outcome, one SD c |
| `sd_units` | 1 | 20% | rfs_2026_rfs_hhaf081 p.33-37 Section 4.1 and 4.2; footnotes 10 to 15: Economic significance is stated as a one-unit tone change relative to the sample mean of the outcome, one SD c |

### mechanism_evidence (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `intermediate_outcomes` | 3 | 60% | jfe_2025_j_jfineco_2025_104150 p.19-19 Section 5.4: Stock-market reactions to issuance announcements are used as an independent, investor-side check on the certif; rfs_2025_rfs_hhae056 p.23-33 Section 3: Mechanisms are addressed in a dedicated section with five sub-tests: value of rebalancing, exposure to intangi |
| `heterogeneity_as_mechanism` | 1 | 20% | rfs_2025_rfs_hhae056 p.23-33 Section 3: Mechanisms are addressed in a dedicated section with five sub-tests: value of rebalancing, exposure to intangi |
| `ruled_out_alternatives` | 1 | 20% | rfs_2025_rfs_hhae056 p.23-33 Section 3: Mechanisms are addressed in a dedicated section with five sub-tests: value of rebalancing, exposure to intangi |

### other (papers with this category: 1/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `other:funding_and_acknowledgments` | 1 | 20% | rfs_2026_rfs_hhaf081 p.1-2 Title page footnote: Funding sources, editor, referees, discussants and seminar venues are listed on the title page, together with  |

### presentation_convention (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_tables_numbered_a` | 2 | 40% | rfs_2025_rfs_hhae056 p.1-38 Title page note; Sections 2.1, 2.3, 2.4, 5: Supplementary results are referenced as Internet Appendix Table or Figure numbers; the appendix is hosted by t; rfs_2026_rfs_hhaf081 p.23-41 Section 3.1; Appendix Table A1; Table IA8: Full summary statistics are relegated to the Internet Appendix (numbered IA), while a variable-definition appe |
| `notes_state_se` | 2 | 40% | jfe_2024_j_jfineco_2024_103809 p.8-14 Notes to Tables 2-8: All regression tables use a conventional three-tier significance-star convention and state the standard-error ; rfs_2024_rfs_hhae045 p.19-46 Tables 2 to 12 notes: Three-level stars from two-tailed tests are used throughout; table notes restate the treatment definition, sam |
| `stars_used` | 2 | 40% | jfe_2024_j_jfineco_2024_103809 p.8-14 Notes to Tables 2-8: All regression tables use a conventional three-tier significance-star convention and state the standard-error ; rfs_2024_rfs_hhae045 p.19-46 Tables 2 to 12 notes: Three-level stars from two-tailed tests are used throughout; table notes restate the treatment definition, sam |
| `summary_stats_table` | 2 | 40% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share; rfs_2026_rfs_hhaf081 p.23-41 Section 3.1; Appendix Table A1; Table IA8: Full summary statistics are relegated to the Internet Appendix (numbered IA), while a variable-definition appe |
| `coefficient_plot` | 1 | 20% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share |
| `in_appendix` | 1 | 20% | rfs_2026_rfs_hhaf081 p.23-41 Section 3.1; Appendix Table A1; Table IA8: Full summary statistics are relegated to the Internet Appendix (numbered IA), while a variable-definition appe |
| `notes_state_sample` | 1 | 20% | rfs_2024_rfs_hhae045 p.19-46 Tables 2 to 12 notes: Three-level stars from two-tailed tests are used throughout; table notes restate the treatment definition, sam |
| `online_appendix_not_available` | 1 | 20% | rfs_2025_rfs_hhae056 p.1-38 Title page note; Sections 2.1, 2.3, 2.4, 5: Supplementary results are referenced as Internet Appendix Table or Figure numbers; the appendix is hosted by t |
| `other:disclosure_examples_appendix` | 1 | 20% | rfs_2024_rfs_hhae045 p.48-50 Appendix A, Appendix B: Appendices provide a timeline of treatment and measurement windows and reproduced examples of actual disclosur |
| `other:timeline_appendix` | 1 | 20% | rfs_2024_rfs_hhae045 p.48-50 Appendix A, Appendix B: Appendices provide a timeline of treatment and measurement windows and reproduced examples of actual disclosur |
| `raw_data_plot` | 1 | 20% | rfs_2025_rfs_hhae056 p.10-24 Figures 1 to 5; Table 3: Figures include an industry count bar chart, a heat map of industry affiliation by year, a size-category share |

### replication_statement (papers with this category: 1/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `code_public` | 1 | 20% | rfs_2025_rfs_hhae056 p.39-39 Code Availability paragraph: A code availability statement at the end of the conclusion gives a Harvard Dataverse DOI for the replication c |
| `replication_package_cited` | 1 | 20% | rfs_2025_rfs_hhae056 p.39-39 Code Availability paragraph: A code availability statement at the end of the conclusion gives a Harvard Dataverse DOI for the replication c |

### robustness_reported (papers with this category: 2/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_estimator` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-12 Discussion of Appendix Tables A.3, A.9, A.13-A.15, A.17-A.18: A long list of appendix specification checks is summarized in the text, covering alternative return transforma |
| `alt_sample` | 1 | 20% | rfs_2024_rfs_hhae045 p.43-44 Table 10 columns 5-6, Table IA-10: The return event study is re-run after dropping 8-K filings that bundle other material items, with the exclude |
| `alt_specification` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-12 Discussion of Appendix Tables A.3, A.9, A.13-A.15, A.17-A.18: A long list of appendix specification checks is summarized in the text, covering alternative return transforma |
| `in_appendix` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-12 Discussion of Appendix Tables A.3, A.9, A.13-A.15, A.17-A.18: A long list of appendix specification checks is summarized in the text, covering alternative return transforma |
| `in_main_text` | 1 | 20% | rfs_2024_rfs_hhae045 p.43-44 Table 10 columns 5-6, Table IA-10: The return event study is re-run after dropping 8-K filings that bundle other material items, with the exclude |

### sample_construction (papers with this category: 5/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `exclusions_justified` | 3 | 60% | jfe_2025_j_jfineco_2025_104150 p.19-19 Section 5.4; Table 11 notes: The stock-reaction sample keeps only SLL issuances with an identifiable public announcement date located throu; rfs_2024_rfs_hhae045 p.42-43 Footnote 21, Table 10 notes: For the return event study, low-priced stocks are dropped to omit potentially distressed firms, stated in a fo |
| `data_source_named` | 2 | 40% | jfe_2024_j_jfineco_2024_103809 p.5-5 Section 3.1: The financial and board-membership data are described as hand-collected from several archival sources, includi; rfs_2025_rfs_hhae056 p.7-8 Section 1.1: The data section documents the vendor's list eligibility criteria and its three-step valuation methodology at  |
| `matching_or_linkage_described` | 2 | 40% | jfe_2025_j_jfineco_2025_104150 p.19-19 Section 5.4; Table 11 notes: The stock-reaction sample keeps only SLL issuances with an identifiable public announcement date located throu; rfs_2025_rfs_hhae056 p.7-8 Section 1.1: The data section documents the vendor's list eligibility criteria and its three-step valuation methodology at  |
| `sample_size_reported_per_table` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-14 Tables 2-8: Every main regression table reports the firm count and observation count directly beneath the coefficients, al |

### specification_reporting (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `cluster_level_in_notes` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-15 Notes to Tables 2, 3, 6, 7, 8: Table notes state the standard-error type and clustering level directly beneath each table rather than only in |
| `controls_progressive_columns` | 1 | 20% | rfs_2025_rfs_hhae056 p.32-33 Tables 10 and 11: The announcement-return table lists year and industry fixed effects as Yes/No rows and adds controls across co |
| `fe_listed_in_table` | 1 | 20% | rfs_2025_rfs_hhae056 p.32-33 Tables 10 and 11: The announcement-return table lists year and industry fixed effects as Yes/No rows and adds controls across co |
| `mean_of_dependent_reported` | 1 | 20% | rfs_2026_rfs_hhaf081 p.34-36 Table 8 panel A; Table 9 panel A: For the report-level analyses, a panel A of the results table reports summary statistics (mean, quartiles, SD) |
| `n_reported` | 1 | 20% | rfs_2025_rfs_hhae056 p.32-33 Tables 10 and 11: The announcement-return table lists year and industry fixed effects as Yes/No rows and adds controls across co |
| `other:controls_collapsed_in_table` | 1 | 20% | rfs_2026_rfs_hhaf081 p.36-36 Table 9 panel B: The event-study table shows key report-level controls explicitly but collapses other analyst and firm controls |
| `se_type_in_notes` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.8-15 Notes to Tables 2, 3, 6, 7, 8: Table notes state the standard-error type and clustering level directly beneath each table rather than only in |
| `summary_stats_table` | 1 | 20% | rfs_2026_rfs_hhaf081 p.34-36 Table 8 panel A; Table 9 panel A: For the report-level analyses, a panel A of the results table reports summary statistics (mean, quartiles, SD) |

### variable_construction (papers with this category: 4/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `outcome_definition` | 4 | 80% | jfe_2024_j_jfineco_2024_103809 p.6-8 Section 4.1 and Table 2 notes: Cumulative abnormal returns for the event-study tables are constructed from a one-factor market-model residual; rfs_2024_rfs_hhae045 p.14-15 Section 2.2.1, Table 1 notes: Outcomes are built by a Python script that flags engagement keywords within a fixed character distance of shar |
| `matching_or_linkage_described` | 1 | 20% | rfs_2026_rfs_hhaf081 p.40-40 Appendix Table A1, Local analyst: The local-analyst indicator is built by geocoding analyst office and firm headquarters addresses with a map AP |
| `measurement_error_discussed` | 1 | 20% | rfs_2024_rfs_hhae045 p.14-16 Section 2.2, footnote 11: Because some disclosures are in images the script cannot read, the RD subsample is hand-checked; script-only r |
| `other:geocoding` | 1 | 20% | rfs_2026_rfs_hhaf081 p.40-40 Appendix Table A1, Local analyst: The local-analyst indicator is built by geocoding analyst office and firm headquarters addresses with a map AP |
| `other:hand_collection` | 1 | 20% | rfs_2024_rfs_hhae045 p.14-16 Section 2.2, footnote 11: Because some disclosures are in images the script cannot read, the RD subsample is hand-checked; script-only r |
| `other:market_adjusted_returns` | 1 | 20% | rfs_2024_rfs_hhae045 p.42-43 Section 4.6, footnote 20: Abnormal returns are compounded daily returns over short windows around the first 8-K disclosing the vote, min |
| `other:missing_coding_rule` | 1 | 20% | rfs_2024_rfs_hhae045 p.16-16 Section 2.2.2: Coding of missing breadth measures is made explicit: set to zero when no engagement is disclosed, treated as m |
| `other:text_keyword_measure` | 1 | 20% | rfs_2024_rfs_hhae045 p.14-15 Section 2.2.1, Table 1 notes: Outcomes are built by a Python script that flags engagement keywords within a fixed character distance of shar |
| `other:variable_appendix` | 1 | 20% | rfs_2024_rfs_hhae045 p.50-52 Appendix C, Table C1: All variables are defined in a dedicated appendix table, and every table note points to it. |
| `treatment_definition` | 1 | 20% | jfe_2024_j_jfineco_2024_103809 p.5-6 Section 3.2 and Section 4.1, equation (1): Jewish connection is operationalized two ways: a continuous measure equal to the share of Jewish board members |

### writing_structure (papers with this category: 3/5)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `contribution_paragraph` | 3 | 60% | rfs_2024_rfs_hhae045 p.2-6 Introduction: The introduction walks through every result in order and then gives several contribution paragraphs; no roadma; rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `data_before_design` | 3 | 60% | rfs_2024_rfs_hhae045 p.2-6 Introduction: The introduction walks through every result in order and then gives several contribution paragraphs; no roadma; rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `mechanisms_after_main` | 3 | 60% | rfs_2024_rfs_hhae045 p.44-47 Section 5: Placebo thresholds and the agency-conflict analysis are gathered in an Additional Tests section after the main; rfs_2025_rfs_hhae056 p.14-39 Sections 2 to 5: Empirical sections proceed from the headline factor regressions, to weighting sensitivity, to characteristic-c |
| `results_previewed_in_intro` | 3 | 60% | rfs_2024_rfs_hhae045 p.2-6 Introduction: The introduction walks through every result in order and then gives several contribution paragraphs; no roadma; rfs_2025_rfs_hhae056 p.1-14 Introduction; Section 1: The introduction opens with practitioner epigraphs, motivates limitations of the input measure, previews the m |
| `main_result_first` | 2 | 40% | rfs_2025_rfs_hhae056 p.14-39 Sections 2 to 5: Empirical sections proceed from the headline factor regressions, to weighting sensitivity, to characteristic-c; rfs_2026_rfs_hhaf081 p.6-37 Sections 1 to 4: The method section comes first and embeds validation and a first M&A application; descriptive comparison acros |
| `appendix_heavy` | 1 | 20% | rfs_2026_rfs_hhaf081 p.6-32 Footnotes 2, 7, 8, 9; Section 4 opening: Robustness has no separate section; extra analyses live in Internet Appendix tables and are summarized in long |
| `in_footnote` | 1 | 20% | rfs_2026_rfs_hhaf081 p.6-32 Footnotes 2, 7, 8, 9; Section 4 opening: Robustness has no separate section; extra analyses live in Internet Appendix tables and are summarized in long |
| `other:subsection_summary_sentences` | 1 | 20% | rfs_2025_rfs_hhae056 p.16-39 Sections 2.1 to 5: Each subsection closes with an Overall sentence summarizing what the tests show, and each mechanism subsection |
| `robustness_separate_section` | 1 | 20% | rfs_2024_rfs_hhae045 p.44-47 Section 5: Placebo thresholds and the agency-conflict analysis are gathered in an Additional Tests section after the main |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | agree | 1 | rfs_2024_rfs_hhae045 s1.formula_or_call (paper: Fixed bandwidths of 2.5, 5 and 10 points plus CCF data-driven bandwidt / card: Single call with h(0.025 0.025); other bandwidths not recorded.) |
| cluster_level | agree | 2 | jfe_2025_j_jfineco_2025_104150 specifications.s1.se.cluster_level (paper: Table 4 notes state standard errors clustered at the firm level / card: s1.se.cluster_level = [id_firm]); rfs_2026_rfs_hhaf081 s1.se.cluster_level (paper: Firm-level clustering for Table 3 validation regressions. / card: s1.se cluster on gvkey.) |
| cluster_level | code_only | 1 | rfs_2025_rfs_hhae056 d4.implementation_features (paper: No standard error type or clustering stated for the announcement-retur / card: reg CAR bb, vce(cluster permno)) |
| cluster_level | paper_only | 1 | rfs_2026_rfs_hhaf081 specifications (paper: Report-level Tables 8 and 9 double-cluster by firm and analyst. / card: No specification record for Table 8-9.do; card only has s1 from Table ) |
| comparison_group | paper_only | 1 | jfe_2025_j_jfineco_2025_104150 specifications.s1.comparison_group (paper: Comparison group is explicitly defined as never-SLL-issuer control fir / card: s1.comparison_group and s2.comparison_group are both null) |
| controls | agree | 2 | rfs_2024_rfs_hhae045 s1.controls_summary (paper: RD deliberately includes no covariates or FE. / card: controls_summary null, fixed_effects null; the call has no covariates.); rfs_2026_rfs_hhaf081 s1.controls_summary (paper: Table 3 controls are lagged firm size and ROA. / card: s1 controls_summary l1size, l1roa.) |
| controls | paper_only | 1 | jfe_2024_j_jfineco_2024_103809 s2.controls_summary (paper: Even-numbered columns of the main tables add a stated set of firm-leve / card: s2.controls_summary is null.) |
| data_source | paper_only | 4 | jfe_2024_j_jfineco_2024_103809 data[0].source_hint (paper: Financial and board data are described as hand-collected from named ar / card: data[0].source_hint and data[1].source_hint are null; the card records); jfe_2025_j_jfineco_2025_104150 data.panel_firmyear.source_hint (paper: Appendix Table A.1 attributes variables to named commercial sources: D / card: data record panel_firmyear has type=null, access=unknown, source_hint=) |
| data_source | agree | 1 | rfs_2025_rfs_hhae056 data (paper: CRSP, Compustat, IBES, Interbrand list, factor libraries, SEC EDGAR fi / card: CRSP, CRSP-Compustat merged, I/B/E/S, Factors.xlsx; no EDGAR or Interb) |
| diagnostic | paper_only | 4 | jfe_2024_j_jfineco_2024_103809 diagnostics (paper: The paper reports a pre-trends figure, a covariate-balance table, and  / card: diagnostics is an empty list in the card.); jfe_2025_j_jfineco_2025_104150 diagnostics.x1.status (paper: Text states that the event-study plot shows parallel pre-issuance tren / card: diagnostics x1 (pretrend_test) has status=unknown, only noting that pr) |
| diagnostic | agree | 3 | jfe_2025_j_jfineco_2025_104150 diagnostics.x2 (paper: Table 5 reports covariate balance (assets, leverage, ROA, Q, ESG score / card: diagnostics x2 (balance) status=observed, describing a clttest of size); rfs_2024_rfs_hhae045 x1 (paper: Density manipulation test (CJM) across bandwidths and years in Table 4 / card: x1 density_test status unknown, note Table 4A, rddensity called.) |
| estimator | agree | 7 | jfe_2024_j_jfineco_2024_103809 s2.estimator (paper: Difference-in-differences with firm and trading-day fixed effects, est / card: Specification s2 (design d2, method did) records estimator hdfe_ols vi); jfe_2024_j_jfineco_2024_103809 s1.estimator (paper: Event-study cumulative abnormal returns from a one-factor market model / card: Specification s1 (design d1, method return_event_study) records estima) |
| estimator | paper_only | 2 | jfe_2024_j_jfineco_2024_103809 designs (paper: Coarsened Exact Matching (Iacus et al., 2012) is described as a fourth / card: The card's designs and specifications list only d1/d2/d3 (return_event); jfe_2025_j_jfineco_2025_104150 designs.d1.method (paper: Identification combines a panel OLS quasi-DID, a propensity-score matc / card: d1 records only method=event_study with role, variant, treatment and c) |
| fixed_effects | paper_only | 4 | jfe_2024_j_jfineco_2024_103809 s2.fixed_effects (paper: The difference-in-differences specification includes firm fixed effect / card: s2.fixed_effects is null in the card's structured fields, even though ); rfs_2024_rfs_hhae045 s1.fixed_effects (paper: Industry (one-digit SIC) and year FE in ATE regressions; firm and year / card: Only the RD spec is carded; fixed_effects null.) |
| fixed_effects | agree | 3 | jfe_2025_j_jfineco_2025_104150 specifications.s1.fixed_effects (paper: Table 4 col. 1/4/7 lists Country x Year FE and Industry x Year FE as t / card: s1.fixed_effects = [id_cyear, id_indyear] from tab4.do line 39); jfe_2025_j_jfineco_2025_104150 specifications.s2.fixed_effects (paper: Table 6 notes list Firm x Cohort FE and Year x Cohort FE for the stack / card: s2.fixed_effects = [id_firmpair, id_yearpair] from fig4.do line 15) |
| other | agree | 2 | rfs_2024_rfs_hhae045 s1.formula_or_call (paper: Triangular kernel for all local polynomial estimators; cutoff at the 7 / card: c(0.7) in the call; kernel not stated in the call (rdrobust default is); rfs_2026_rfs_hhaf081 d1.implementation_features (paper: Pipeline: C99 segmentation, BERT boilerplate filter, keyword plus BERT / card: d1 llm_extraction with two-round GPT extraction, RAG, boilerplate filt) |
| outputs | paper_only | 3 | jfe_2025_j_jfineco_2025_104150 outputs.tables (paper: Paper presents eleven main numbered tables and six main numbered figur / card: outputs.tables and outputs.figures are both empty arrays); rfs_2024_rfs_hhae045 outputs (paper: Twelve main tables and six figures plus Internet Appendix tables IA-1  / card: outputs.tables and figures empty although per-table scripts exist.) |
| outputs | agree | 1 | rfs_2025_rfs_hhae056 outputs.tables (paper: Thirteen numbered tables and five figures with stars and t-statistics / card: six table outputs via outreg2/esttab with coef and tstat; stars null; ) |
| robustness | paper_only | 5 | jfe_2024_j_jfineco_2024_103809 robustness (paper: The paper describes an extensive robustness program spanning alternati / card: robustness is an empty list in the card.); jfe_2025_j_jfineco_2025_104150 robustness (paper: Paper reports multiple named robustness checks: log-transformed ESG sc / card: card robustness array is empty) |
| sample | paper_only | 4 | jfe_2024_j_jfineco_2024_103809 pipeline.sample_restrictions (paper: The difference-in-differences analysis is run on a balanced panel of f / card: pipeline.sample_restrictions is an empty list and s1/s2/s3 sample fiel); rfs_2024_rfs_hhae045 pipeline.sample_restrictions (paper: First-time entrants into the narrow band, missing controls dropped, cr / card: sample null; pipeline.sample_restrictions empty.) |
| se_type | agree | 5 | jfe_2024_j_jfineco_2024_103809 s2.se.cluster_level (paper: Baseline panel regressions (returns, volatility, risk-adjusted returns / card: s2.se.type is cluster with cluster_level firm.); jfe_2024_j_jfineco_2024_103809 s1.se (paper: The event-study table (Table 2) note states only that standard errors  / card: s1.se.type is cluster with cluster_level firm, taken from the clus(fir) |
| se_type | paper_only | 1 | jfe_2024_j_jfineco_2024_103809 specifications (paper: The firm-year dividend regressions and the media-coverage regression a / card: No specification in the card corresponds to the dividend regression or) |
| weights | paper_only | 1 | jfe_2025_j_jfineco_2025_104150 specifications.s1.weights (paper: Section 5.1 and Table 7 describe overlap-weighted regressions using pr / card: Neither s1 nor s2 records a weighting specification, and no specificat) |
| weights | agree | 1 | rfs_2025_rfs_hhae056 s1.notes; s2.notes; s3.notes (paper: Equal-weighted baseline, straight value-weighted and capped value-weig / card: s1 mean collapse, s2 market-value weighted collapse, s3 capped value w) |

## Gaps the readers reported

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
- (1) No explicit rationale for the two-way clustering levels beyond matching the FE structure.
- (1) No power discussion for the RD subsample apart from a passing remark on sample size in the event study.
- (1) No data availability statement for the proprietary ISS file or FOIA data; only code availability is given.
- (1) No multiple-testing adjustment discussed despite many outcomes and placebo thresholds.
- (1) No preregistration or ethics statement (not expected for archival data).
- (1) No standard error type or clustering justification is given for the earnings-surprise and announcement-return regression
- (1) Newey-West lag length is never stated in the text.
- (1) No data availability statement and no software named; only a code DOI.
- (1) No explicit roadmap paragraph in the introduction.
- (1) No formal validation test of the text-based measure beyond example firms and a correlation with the vendor portfolio.
- (1) Several robustness checks are described as unreported or not tabulated.
- (1) No justification given for the clustering levels (firm; firm and analyst).
- (1) No discussion of LLM output stochasticity (temperature, repeated runs) or of prompt-version sensitivity beyond the chain
- (1) No inter-annotator agreement reported for the human annotation benchmark.
- (1) No data availability statement beyond the code DOI; access procedures for commercial text corpora not described.
- (1) No preregistration, IRB or ethics statement.
- (1) No explicit external validity discussion (S&P 1500 firms, US sample).

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
