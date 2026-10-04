# Reported practice: `diff_in_disc` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 3 paper notes (2 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | JPE: 2, ReStud: 1 |
| year | 2024: 1, 2026: 2 |
| papers with at least one observation in category | design_statement: 2, specification_reporting: 2, diagnostic_reported: 2, sample_construction: 1, variable_construction: 1, inference_justification: 1, heterogeneity_reported: 1, limitation_stated: 1, presentation_convention: 1, writing_structure: 1, replication_statement: 1, data_access: 1, external_validity: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| jpe_132_9_2 | JPE | 2024 | full | yes | 81cfda54e6be |
| jpe_2026_739821 | JPE | 2026 | main_text | no | 934a3ac79eb2 |
| restud_2026_restud_rdag037 | ReStud | 2026 | full | yes | 23b104741be7 |

## Practices by category and tag


### data_access (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_access_procedure_described` | 1 | 33% | jpe_2026_739821 p.43-43 Data Availability section: States that the Data Availability section provides instructions for how to obtain the individual-level demogra |
| `data_restricted` | 1 | 33% | jpe_2026_739821 p.43-43 Data Availability section: States that the Data Availability section provides instructions for how to obtain the individual-level demogra |

### design_statement (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `continuity_at_cutoff_argued` | 2 | 67% | jpe_2026_739821 p.29-30 Section V.C, equations (4)-(5): Names a second design, a spatial regression-discontinuity difference-in-differences (RD-DD), comparing women b; restud_2026_restud_rdag037 p.22-23 Section 5.3, equation (6): For the Supreme Court decision, the author explains why the bunching counterfactual is not credible in that wi |
| `design_variant_named` | 2 | 67% | jpe_2026_739821 p.29-30 Section V.C, equations (4)-(5): Names a second design, a spatial regression-discontinuity difference-in-differences (RD-DD), comparing women b; restud_2026_restud_rdag037 p.22-23 Section 5.3, equation (6): For the Supreme Court decision, the author explains why the bunching counterfactual is not credible in that wi |

### diagnostic_reported (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `bandwidth_sensitivity` | 2 | 67% | jpe_2026_739821 p.34-34 Section V.C, robustness discussion (Figure E3, appendix): Reports that RD-DD estimates are checked across a range of bandwidths narrower and wider than the mean-squared; restud_2026_restud_rdag037 p.23-24 Table 6, Figure A11, Section 5.3: The time-discontinuity design reports an optimal bandwidth from Imbens and Kalyanaraman alongside wider and na |
| `in_appendix` | 2 | 67% | jpe_2026_739821 p.34-34 Section V.C, robustness discussion (Figure E3, appendix): Reports that RD-DD estimates are checked across a range of bandwidths narrower and wider than the mean-squared; restud_2026_restud_rdag037 p.22-23 Section 5.3, Figure A11: The paper checks that the pre-reform share of cases in the future bunching bin is stable near zero across year |
| `density_test` | 1 | 33% | restud_2026_restud_rdag037 p.22-23 Section 5.3, Figure A11: The paper checks that the pre-reform share of cases in the future bunching bin is stable near zero across year |
| `in_main_text` | 1 | 33% | restud_2026_restud_rdag037 p.22-23 Section 5.3, Figure A11: The paper checks that the pre-reform share of cases in the future bunching bin is stable near zero across year |
| `placebo_cutoffs` | 1 | 33% | restud_2026_restud_rdag037 p.23-24 footnote 18, Table A16: Placebo dates are checked: no change at the certiorari announcement or oral argument dates, and no change when |

### external_validity (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 1 | 33% | jpe_2026_739821 p.42-43 Section VII, Conclusion: Discusses whether the finding could generalize beyond France, noting that similar egalitarian inheritance laws |

### heterogeneity_reported (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_appendix` | 1 | 33% | jpe_2026_739821 p.39-40 Section VI.A (Tables A7-A9, appendix): Reports that the same soil-based heterogeneity pattern is checked using four finer soil-texture categories and |
| `interaction` | 1 | 33% | jpe_2026_739821 p.39-40 Section VI.A (Tables A7-A9, appendix): Reports that the same soil-based heterogeneity pattern is checked using four finer soil-texture categories and |

### inference_justification (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `spatial_hac` | 1 | 33% | jpe_2026_739821 p.16-34 Section IV.A; Section V.B 'Spatially adjusted errors'; Section V.C robustness: Reports Conley-type spatially adjusted standard errors under several distance cutoffs for both the DD and RD-D |

### limitation_stated (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_coverage` | 1 | 33% | jpe_2026_739821 p.15-15 Section III.C: Acknowledges that the crowdsourced genealogy database has lower data quality than the family-reconstitution da |

### presentation_convention (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `binscatter` | 1 | 33% | jpe_2026_739821 p.31-32 Figure 5: Presents RD-DD evidence as binned scatter plots of residualized fertility against distance to the inheritance  |
| `map` | 1 | 33% | jpe_2026_739821 p.12-15 Figures 2 and 3: Presents the constructed inheritance-rules atlas and the geographic distribution of sampled observations as ma |
| `rd_plot` | 1 | 33% | jpe_2026_739821 p.31-32 Figure 5: Presents RD-DD evidence as binned scatter plots of residualized fertility against distance to the inheritance  |

### replication_statement (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `code_public` | 1 | 33% | jpe_2026_739821 p.43-43 Data Availability section: States in a Data Availability section that code replicating the tables and figures is deposited in a named rep |
| `replication_package_cited` | 1 | 33% | jpe_2026_739821 p.43-43 Data Availability section: States in a Data Availability section that code replicating the tables and figures is deposited in a named rep |

### sample_construction (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `data_source_named` | 1 | 33% | jpe_2026_739821 p.14-15 Section III.C: Names crowdsourced online genealogies from a commercial genealogy website as a second fertility source, and de |
| `exclusions_justified` | 1 | 33% | jpe_2026_739821 p.14-15 Section III.C: Describes applying a horizontal sample restriction to the crowdsourced genealogy data, following a cited prior |
| `matching_or_linkage_described` | 1 | 33% | jpe_2026_739821 p.14-15 Section III.C: Names crowdsourced online genealogies from a commercial genealogy website as a second fertility source, and de |

### specification_reporting (papers with this category: 2/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `se_type_in_notes` | 2 | 67% | jpe_2026_739821 p.23-33 Table 2 note; Table 4 note: States in table notes that standard errors are clustered by municipality for the DD tables and by municipality; restud_2026_restud_rdag037 p.23-23 Table 6 and notes: The Alleyne table reports the pooled discontinuity and the year-specific discontinuity across columns that var |
| `cluster_level_in_notes` | 1 | 33% | jpe_2026_739821 p.23-33 Table 2 note; Table 4 note: States in table notes that standard errors are clustered by municipality for the DD tables and by municipality |
| `controls_progressive_columns` | 1 | 33% | restud_2026_restud_rdag037 p.23-23 Table 6 and notes: The Alleyne table reports the pooled discontinuity and the year-specific discontinuity across columns that var |
| `mean_of_dependent_reported` | 1 | 33% | jpe_2026_739821 p.33-33 Table 4: Reports the mean of the dependent variable as a table row for the spatial RD-DD estimates, allowing readers to |

### variable_construction (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `running_variable_definition` | 1 | 33% | jpe_2026_739821 p.30-30 Section V.C, equation (4): Defines the RD running variable as the geographic distance from a woman's birth municipality to the nearest in |

### writing_structure (papers with this category: 1/3)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `results_previewed_in_intro` | 1 | 33% | jpe_2026_739821 p.6-7 Section I, introduction: Previews the direction and approximate size of the main DD and RD-DD fertility effects, and the counterfactual |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| bandwidth | agree | 1 | jpe_132_9_2 x2 (paper: RD bandwidths are chosen via an MSE-optimal procedure computed separat / card: Diagnostic x2 (bandwidth_selection) records the mserd bandwidth-select) |
| cluster_level | paper_only | 2 | jpe_132_9_2 s3.se.cluster_level (paper: DD and DD-IV standard errors are clustered at the district level, the  / card: s2.se.type = cluster and s3.se.type = cluster, but s2.se.cluster_level); restud_2026_restud_rdag037 s1.se.cluster_level (paper: No clustering for the main table; state-level clustering for state spl / card: cluster_level null for s1 and s2; no prosecutor-level spec recorded.) |
| data_source | agree | 1 | jpe_132_9_2 data[2] (paper: Analysis combines two censuses, a poverty-targeting census subset, a v / card: The card's data[] array records census, geospatial, NSS household-surv) |
| data_source | paper_only | 1 | restud_2026_restud_rdag037 d1 (paper: USSC sentencing data plus EOUSA, NIBRS, STRIDE, NSDUH, Florida inmate  / card: Main script named for USSC; other sources not recorded.) |
| diagnostic | paper_only | 2 | jpe_132_9_2 x1 (paper: A first-stage weak-instrument F-statistic is reported for each DD-IV c / card: Diagnostic x1 (first_stage) has status 'unknown' with no recorded obse); jpe_132_9_2 diagnostics (paper: RD density/manipulation tests and multiple falsification exercises (wr / card: The card's diagnostics list contains only first_stage, bandwidth_selec) |
| diagnostic | unknown | 1 | restud_2026_restud_rdag037 x1 (paper: KS test of pre-2010 distributions by race, placebo reassignment exerci / card: x1 density_test with unknown details.) |
| estimator | agree | 2 | jpe_132_9_2 s1.estimator (paper: Sharp RD implemented via the rdrobust framework (Calonico-Cattaneo-Tit / card: s1.estimator = local_polynomial_rd, s1.command = rdrobust, s1.package ); restud_2026_restud_rdag037 s1.estimator, s2.estimator (paper: Linear probability model of a bunching-bin indicator on a post-2010 in / card: s1 and s2 are OLS regressions of in280290 on after2010 and on race-by-) |
| fixed_effects | paper_only | 3 | jpe_132_9_2 s1.fixed_effects (paper: Main RD specification (equation 1) includes state fixed effects and co / card: s1.fixed_effects is null; the card records no fixed-effects value for ); jpe_132_9_2 s2.fixed_effects (paper: Main DD specification (equation 2) includes district and year fixed ef / card: s2.fixed_effects is null; the card records only a bound local-macro va) |
| other | unknown | 1 | restud_2026_restud_rdag037 packages.rdplot (paper: RD-style plots of sentence around 280 g and time discontinuity around  / card: Package rdplot listed under Stata with unknown use.) |
| outputs | paper_only | 2 | jpe_132_9_2 outputs.tables (paper: The paper presents nine numbered main-text tables and nine main-text f / card: outputs.tables records only two table entries (table_rd_vdelec.tex and); restud_2026_restud_rdag037 outputs (paper: Seven main tables and five main figures plus about twenty-one appendix / card: One table and one figure recorded from the files read.) |
| robustness | agree | 1 | jpe_132_9_2 robustness[0] (paper: DD robustness checks include alternative bandwidths around the eligibi / card: robustness[0] (alt_bandwidth) and robustness[1] (alt_fixed_effects) ar) |
| robustness | paper_only | 1 | restud_2026_restud_rdag037 robustness (paper: Logit, probit and Poisson estimators, wider bins, alternative SEs, add / card: No robustness records in the card.) |
| sample | agree | 1 | jpe_132_9_2 pipeline.sample_restrictions[1] (paper: RD sample is restricted to single-habitation villages in first-wave di / card: pipeline.sample_restrictions records matching restriction logic (singl) |
| sample | paper_only | 1 | restud_2026_restud_rdag037 d1 (paper: Crack-cocaine cases 1999 to 2015 with missing, range-coded, flagged an / card: No sample restrictions recorded on d1 or s1.) |
| se_type | agree | 2 | jpe_132_9_2 s1.se.type (paper: RD standard errors are described as heteroskedasticity-robust nearest- / card: s1.se.type = robust, s1.se.cluster_level = null.); restud_2026_restud_rdag037 s1.se, s2.se (paper: Robust standard errors in parentheses for Table 2. / card: se robust in s1 and s2.) |

## Gaps the readers reported

- (1) No preregistration, IRB approval, or informed-consent statement appears anywhere in the main text; the study relies enti
- (1) No explicit justification is given in the main text for why RD standard errors are left unclustered while DD standard er
- (1) R-squared is not reported in the main RD or DD regression tables (rdrobust and reghdfe-style output favors bandwidth, cl
- (1) Appendices A, B and C are referenced dozens of times for balance tables, full robustness batteries, falsification tests 
- (1) The main text does not describe a step-by-step access procedure for the restricted low-income SECC subset or the Economi
- (1) No statement about sampling or survey weights anywhere in the main text; none of the reported specifications mention wei
- (1) No formal manipulation/density test (e.g. McCrary-style) for the RD running variable is reported in the read text; ident
- (1) No explicit multiple-hypothesis-testing adjustment is described despite many outcomes, subsamples, and specifications be
- (1) No preregistration, IRB approval, or participant-consent statement of any kind appears in the read text; the study uses 
- (1) No explicit statement of statistical software (e.g., Stata/R and version) appears in the main text.
- (1) The online appendixes A-H, referenced extensively for robustness tables, diagnostic figures, the formal model, and addit
- (1) The introduction contains an explicit contributions paragraph but no separate roadmap paragraph laying out the order of 
- (1) No explicit justification for using robust (unclustered) standard errors in the main specification.
- (1) No software or package named in the text; only a Zenodo DOI for data and code.
- (1) No preregistration, IRB or ethics statement.
- (1) Online appendix (Tables A1 to A21, Figures A1 to A12) is not included in the text file; appendix content is known only t
- (1) No multiple testing adjustment discussed for the many heterogeneity columns.

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
