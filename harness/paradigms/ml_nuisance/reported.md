# Reported practice: `ml_nuisance` (draft, generated from paper-practice notes)

Generated 2026-09-09T01:06:38Z by fhb papers distill fhb-papers-0.1.0 from 2 paper notes (2 with a linked recipe card). Counting unit: paper. A tag absent from a note means the reader did not record it, not that the paper lacks it. Do not edit; regenerate with `fhb papers distill`. Observed code practice is in `observed.md`; rules are in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| journal | AER: 2 |
| year | 2017: 1, 2023: 1 |
| papers with at least one observation in category | design_statement: 2, variable_construction: 2, specification_reporting: 2, inference_justification: 2, diagnostic_reported: 2, robustness_reported: 2, limitation_stated: 2, presentation_convention: 2, writing_structure: 2, replication_statement: 2, data_access: 2, sample_construction: 1, heterogeneity_reported: 1, mechanism_evidence: 1, magnitude_interpretation: 1, external_validity: 1 |

## Inputs

| artid | journal | year | coverage | card | note sha256 |
|---|---|---|---|---|---|
| aer_107_5_51 | AER | 2017 | full | yes | cc00a3a8a6d8 |
| aer_113_3_2 | AER | 2023 | full | yes | 5821238a2d46 |

## Practices by category and tag


### data_access (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `administrative` | 1 | 50% | aer_113_3_2 p.7-7 Section II: Describes its primary lease and payment data as obtained directly from a state land-management agency's admini |
| `data_access_procedure_described` | 1 | 50% | aer_107_5_51 p.1-1 footnote (dagger): A footnote directs readers to the article's DOI landing page for additional materials and the authors' disclos |
| `linked_records` | 1 | 50% | aer_113_3_2 p.9-9 Section II: Describes constructing its parcel-level dataset by linking the agency's lease records to an independently sour |
| `other:access_route_unstated` | 1 | 50% | aer_107_5_51 p.1-1 introduction: The note does not state whether the underlying illustrative data are public-use, restricted or administrative; |
| `public_use` | 1 | 50% | aer_113_3_2 p.7-7 Section II: Describes its primary lease and payment data as obtained directly from a state land-management agency's admini |

### design_statement (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `design_variant_named` | 2 | 100% | aer_107_5_51 p.1-1 Section I, para 2: Treatment is modeled as entering the outcome equation non-additively-separably, so treatment effects are fully; aer_113_3_2 p.10-15 Section III: Names two parallel design variants used to implement the comparison: fixed-effects regressions with location-b |
| `estimand_named` | 2 | 100% | aer_107_5_51 p.1-1 Section I, para 1: The note names the average treatment effect and the average treatment effect on the treated as its two focal p; aer_113_3_2 p.1-1 Abstract; Introduction: States its goal as directly measuring the gains from a centralized formal mechanism relative to informal decen |
| `identifying_assumption_explicit` | 2 | 100% | aer_107_5_51 p.1-1 Section I, para 1, eq. (1)-(2): Identification of ATE and ATTE rests on an unconfoundedness assumption attributed to Rosenbaum and Rubin (1983; aer_113_3_2 p.10-11 Section III: States its identifying assumption as variation in a parcel's mineral-allocation history within a narrowly defi |
| `threats_discussed` | 2 | 100% | aer_107_5_51 p.2-2 Section I, discussion after eq. (4): The central identification threat discussed is the estimator's sensitivity to small mistakes in high-dimension; aer_113_3_2 p.11-12 Section III: Discusses as the central threat to identification the possibility that the state or early land buyers had adva |
| `other:neyman_orthogonal_score` | 1 | 50% | aer_107_5_51 p.1-2 introduction and Section I: The design variant is named as Neyman-orthogonal moment-condition estimation with cross-fitting, built on doub |

### diagnostic_reported (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `in_main_text` | 2 | 100% | aer_107_5_51 p.3-4 Theorem 1: The note's only formal validity check for the estimator is a theorem establishing uniform asymptotic normality; aer_113_3_2 p.13-13 Table 3: Reports a formal balance table that regresses proxies for geological resource quality and for surface characte |
| `attrition_analysis` | 1 | 50% | aer_113_3_2 p.23-23 Section VA; Figure 4: Presents a quarter-by-quarter comparison, shown as a figure of point estimates with confidence intervals, of t |
| `balance_table` | 1 | 50% | aer_113_3_2 p.13-13 Table 3: Reports a formal balance table that regresses proxies for geological resource quality and for surface characte |
| `in_appendix` | 1 | 50% | aer_107_5_51 p.4-4 Section II, closing paragraph before Section III: The proof of the main theorem is not given in the printed note but is stated to be deferred to an online appen |

### external_validity (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `scaling_discussed` | 1 | 50% | aer_113_3_2 p.32-33 Section VIB: Devotes a dedicated subsection to discussing how the results from this specific public-land natural experiment |
| `site_specific` | 1 | 50% | aer_113_3_2 p.32-33 Section VIB: Devotes a dedicated subsection to discussing how the results from this specific public-land natural experiment |
| `time_period_specific` | 1 | 50% | aer_113_3_2 p.11-11 Section III: Frames its identifying variation as arising because the assignment of mineral rights was completed decades bef |

### heterogeneity_reported (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `exploratory_labelled` | 1 | 50% | aer_113_3_2 p.32-32 Section VIB, footnote referencing online Appendix Table: Discusses an appendix table that adds measures of lessor experience and sophistication to its main payment reg |
| `in_appendix` | 1 | 50% | aer_113_3_2 p.32-32 Section VIB, footnote referencing online Appendix Table: Discusses an appendix table that adds measures of lessor experience and sophistication to its main payment reg |
| `mechanism_motivated` | 1 | 50% | aer_113_3_2 p.26-27 Table 9: Tests whether the payment and output differences hold within the same firm by adding firm fixed effects to its |
| `split_sample` | 1 | 50% | aer_113_3_2 p.26-27 Table 9: Tests whether the payment and output differences hold within the same firm by adding firm fixed effects to its |

### inference_justification (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `no_justification_found` | 2 | 100% | aer_107_5_51 p.3-3 Section II: No clustering of standard errors is proposed or discussed anywhere in the note; the variance formula treats th; aer_113_3_2 p.13-16 Table 3 notes; Table 4 notes: Clusters standard errors throughout at the same spatial grid used to define its location fixed effects, but do |
| `cluster_at_assignment_level` | 1 | 50% | aer_113_3_2 p.13-16 Table 3 notes; Table 4 notes: Clusters standard errors throughout at the same spatial grid used to define its location fixed effects, but do |
| `other:analytic_asymptotic_se` | 1 | 50% | aer_107_5_51 p.3-3 Section II, para after eq. (7): Standard errors are constructed analytically as the square root of the sample average of the squared estimated |
| `other:confidence_interval_construction` | 1 | 50% | aer_107_5_51 p.3-3 Section II, after eq. (7): Confidence intervals are constructed in the standard normal-approximation form, centered at the point estimato |
| `other:mean_vs_median_aggregation` | 1 | 50% | aer_107_5_51 p.4-4 Section III: Two rules for aggregating across repeated splits are proposed, the across-split mean and the across-split medi |
| `other:repeated_splitting` | 1 | 50% | aer_107_5_51 p.4-4 Section III, para 2: The recommended remedy is to repeat the entire cross-fitting procedure many times over independent random part |
| `other:sample_splitting_variance` | 1 | 50% | aer_107_5_51 p.4-4 Section III, para 1: The authors argue that the specific random partition used for cross-fitting is itself an additional source of  |
| `other:variance_inflation_for_splitting` | 1 | 50% | aer_107_5_51 p.4-4 Section III, closing paragraphs: Two matching standard-error formulas are proposed that add a term for dispersion of the split-specific estimat |

### limitation_stated (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `identification_caveat` | 2 | 100% | aer_107_5_51 p.3-3 Assumption 1, closing remark: The authors state their regularity conditions are non-primitive and not the tightest possible, having been cho; aer_113_3_2 p.18-18 Section IVA, footnote: States that its attempt to decompose the output effect into an extensive drilling margin and an intensive prod |
| `data_coverage` | 1 | 50% | aer_113_3_2 p.30-30 Section VIA: Notes that no record exists of failed or attempted negotiations, or of the process leading up to a completed n |
| `external_validity` | 1 | 50% | aer_113_3_2 p.32-32 Section VIB: Acknowledges that its negotiation setting involves a public-agency intermediary that reviews and can improve n |

### magnitude_interpretation (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `back_of_envelope` | 1 | 50% | aer_113_3_2 p.33-33 Section VIB: Offers an informal cost-benefit comparison between the estimated payment gain from switching to a formal mecha |
| `cost_benefit` | 1 | 50% | aer_113_3_2 p.33-33 Section VIB: Offers an informal cost-benefit comparison between the estimated payment gain from switching to a formal mecha |
| `precision_discussed` | 1 | 50% | aer_113_3_2 p.24-25 Section VB: Explicitly notes where certain specifications, particularly the parcel-level and nonlinear zero-heavy-outcome  |
| `relative_to_mean` | 1 | 50% | aer_113_3_2 p.16-16 Table 4 notes; Section IVA: Interprets its estimated payment and output coefficients relative to the average value of the outcome for the  |

### mechanism_evidence (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `ruled_out_alternatives` | 1 | 50% | aer_113_3_2 p.30-31 Section VIA: Considers and partly rules out several alternative explanations for the estimated gap, including that negotiat |
| `suggestive_labelled` | 1 | 50% | aer_113_3_2 p.30-31 Section VIA: Considers and partly rules out several alternative explanations for the estimated gap, including that negotiat |
| `survey_evidence` | 1 | 50% | aer_113_3_2 p.31-31 Section VIA: Cites an external survey of private mineral-rights lessors, describing their reported search behavior and use  |

### presentation_convention (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_tables_numbered_a` | 1 | 50% | aer_113_3_2 p.12-32 Multiple footnotes citing online Appendix sections A-E: Refers throughout to a suite of alphabetically labeled online-appendix tables and figures for supplementary sp |
| `coefficient_plot` | 1 | 50% | aer_113_3_2 p.23-23 Figure 4: Presents one figure of quarter-specific point estimates with confidence intervals for its extensive-margin lea |
| `map` | 1 | 50% | aer_113_3_2 p.15-15 Figure 3: Includes one figure showing the raw geographic overlap of auctioned and negotiated leases within a concentrate |
| `no_stars` | 1 | 50% | aer_107_5_51 p.3-4 Theorem 1: Because no empirical results table appears in the main text, there is no stars-based significance convention t |
| `notes_state_sample` | 1 | 50% | aer_113_3_2 p.9-29 Table notes throughout: Places most interpretive and technical detail, including variable units, sample restrictions, and the standard |
| `notes_state_se` | 1 | 50% | aer_113_3_2 p.9-29 Table notes throughout: Places most interpretive and technical detail, including variable units, sample restrictions, and the standard |
| `online_appendix_not_available` | 1 | 50% | aer_113_3_2 p.12-32 Multiple footnotes citing online Appendix sections A-E: Refers throughout to a suite of alphabetically labeled online-appendix tables and figures for supplementary sp |
| `other:numbered_theorem_and_proof` | 1 | 50% | aer_107_5_51 p.3-3 Assumption 1, Theorem 1: The paper's central result is presented as a formally numbered theorem preceded by an explicit numbered assump |
| `other:short_note_format` | 1 | 50% | aer_107_5_51 p.1-1 footnotes and introduction: The piece is written in the compact journal proceedings note format, naming discussants and repeatedly cross-r |
| `raw_data_plot` | 1 | 50% | aer_113_3_2 p.15-15 Figure 3: Includes one figure showing the raw geographic overlap of auctioned and negotiated leases within a concentrate |
| `summary_stats_table` | 1 | 50% | aer_113_3_2 p.9-11 Table 1; Table 2: Opens its empirical section with descriptive summary-statistics tables comparing auctioned and negotiated leas |

### replication_statement (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `code_public` | 2 | 100% | aer_107_5_51 p.1-1 introduction, para 1: The introduction states that empirical illustrations and code implementing the method are available as supplem; aer_113_3_2 p.1-35 Acknowledgment footnote; References: States in an acknowledgment footnote that replication code is available through a cited data-repository identi |
| `replication_package_cited` | 2 | 100% | aer_107_5_51 p.1-1 introduction, para 1: The introduction states that empirical illustrations and code implementing the method are available as supplem; aer_113_3_2 p.1-35 Acknowledgment footnote; References: States in an acknowledgment footnote that replication code is available through a cited data-repository identi |
| `software_named` | 2 | 100% | aer_107_5_51 p.1-4 throughout: No specific statistical software or package is named anywhere in the printed note; software choices are left t; aer_113_3_2 p.14-14 Section III, footnote 22: Names the specific double/debiased machine-learning framework and estimation procedure it follows, citing the  |

### robustness_reported (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `alt_estimator` | 2 | 100% | aer_107_5_51 p.2-2 Section II, para 1: Robustness to the choice of first-stage learner is handled generically by stating the method is valid for any ; aer_113_3_2 p.21-21 Table 6: Reports both a linear per-acre specification and a pseudo-Poisson quasi-maximum-likelihood specification for i |
| `in_main_text` | 2 | 100% | aer_107_5_51 p.2-2 Section II, para 1: Robustness to the choice of first-stage learner is handled generically by stating the method is valid for any ; aer_113_3_2 p.16-17 Table 4: Reports the same payment regression under alternative sizes and interaction structures of the location and tim |
| `alt_fixed_effects` | 1 | 50% | aer_113_3_2 p.16-17 Table 4: Reports the same payment regression under alternative sizes and interaction structures of the location and tim |
| `alt_sample` | 1 | 50% | aer_113_3_2 p.17-18 Table 4 columns restricted to private surface: Re-estimates its main payment comparison on a sample restricted to leases where the state does not own the sur |
| `alt_specification` | 1 | 50% | aer_113_3_2 p.18-18 Section IVA, footnote referencing online Appendix E: States that it collected and digitized supplementary lease-contract clause data and re-checks whether unobserv |
| `in_appendix` | 1 | 50% | aer_113_3_2 p.18-18 Section IVA, footnote referencing online Appendix E: States that it collected and digitized supplementary lease-contract clause data and re-checks whether unobserv |
| `other:robustness_to_sample_split` | 1 | 50% | aer_107_5_51 p.4-4 Section III heading and content: The entire third section is framed as a robustness recommendation for one implementation choice, making infere |
| `summarized_in_one_table` | 1 | 50% | aer_113_3_2 p.16-17 Table 4: Reports the same payment regression under alternative sizes and interaction structures of the location and tim |

### sample_construction (papers with this category: 1/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `attrition_reported` | 1 | 50% | aer_113_3_2 p.20-20 Section IVB: Notes that production and royalty data are observed only through a fixed cutoff date, so output and revenue fo |
| `data_coverage` | 1 | 50% | aer_113_3_2 p.20-20 Section IVB: Notes that production and royalty data are observed only through a fixed cutoff date, so output and revenue fo |
| `data_source_named` | 1 | 50% | aer_113_3_2 p.7-7 Section II: Draws its lease and payment data from a state land-management agency's administrative records, describing this |
| `exclusions_justified` | 1 | 50% | aer_113_3_2 p.7-8 Section IIA: Lists specific sample restrictions, exclusion of leases outside shale formations, of leases outside a defined  |
| `matching_or_linkage_described` | 1 | 50% | aer_113_3_2 p.9-9 Section II: Constructs parcel-level outcomes by spatially matching leases to an independently sourced parcel boundary map, |
| `restricted_data_used` | 1 | 50% | aer_113_3_2 p.7-7 Section II: Draws its lease and payment data from a state land-management agency's administrative records, describing this |
| `sample_period_stated` | 1 | 50% | aer_113_3_2 p.7-9 Section II; Section IIA: Restricts most analyses to leases signed within a defined multi-year window overlapping the shale-development  |
| `unit_of_observation_stated` | 1 | 50% | aer_113_3_2 p.7-9 Section II; Section IIA: Restricts most analyses to leases signed within a defined multi-year window overlapping the shale-development  |

### specification_reporting (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `baseline_then_variants` | 2 | 100% | aer_107_5_51 p.2-2 Section II, para 1: The choice of first-stage machine learning method is treated as an interchangeable input to a single generic e; aer_113_3_2 p.16-17 Table 4: Reports its main payment table as a sequence of columns that vary the granularity and interaction structure of |
| `cluster_level_in_notes` | 1 | 50% | aer_113_3_2 p.16-16 Table 4 notes; Table 5 notes: States in table notes that standard errors are clustered by grid, matching whichever spatial grid size defines |
| `controls_progressive_columns` | 1 | 50% | aer_113_3_2 p.17-18 Table 4 columns for extra controls: Adds a further block of surface-quality control variables, shape regularity, a multiple-parcel indicator, land |
| `fe_listed_in_table` | 1 | 50% | aer_113_3_2 p.16-17 Table 4: Reports its main payment table as a sequence of columns that vary the granularity and interaction structure of |
| `mean_of_dependent_reported` | 1 | 50% | aer_113_3_2 p.16-16 Table 4 notes: States the sample mean of the dependent variable for the omitted negotiated group directly in the notes beneat |
| `n_reported` | 1 | 50% | aer_113_3_2 p.16-16 Table 4 notes: Reports the number of observations for every column of its fixed-effects and machine-learning tables, and addi |
| `other:algorithm_steps_as_specification` | 1 | 50% | aer_107_5_51 p.2-3 Section II.A, Steps 1-3: The estimator is presented as a three-step K-fold cross-fitting algorithm, partitioning the sample, fitting nu |
| `other:no_regression_table` | 1 | 50% | aer_107_5_51 p.3-4 Theorem 1: No table reporting point estimates, standard errors, sample sizes or fit statistics for an applied example app |
| `r2_reported` | 1 | 50% | aer_113_3_2 p.16-16 Table 4 notes: Reports the number of observations for every column of its fixed-effects and machine-learning tables, and addi |
| `se_type_in_notes` | 1 | 50% | aer_113_3_2 p.16-16 Table 4 notes; Table 5 notes: States in table notes that standard errors are clustered by grid, matching whichever spatial grid size defines |

### variable_construction (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `measurement_error_discussed` | 2 | 100% | aer_107_5_51 p.3-3 Assumption 1(iii) and following discussion: Convergence-rate conditions on the nuisance function estimators are stated only as high-level, non-primitive a; aer_113_3_2 p.20-21 Section IVB: Explains that because a large share of leases are never drilled and record exactly zero output and revenue in  |
| `outcome_definition` | 2 | 100% | aer_107_5_51 p.1-1 eq. (1): The outcome is modeled as an additively separable function of an unrestricted regression on treatment and cont; aer_113_3_2 p.16-20 Section IVA; Section IVB: Defines its primary payment outcome as the natural logarithm of the up-front bonus payment per acre, and defin |
| `treatment_definition` | 2 | 100% | aer_107_5_51 p.1-1 Section I, para 1; eq. (2): Treatment is defined as a binary indicator whose conditional mean given the controls is described as the prope; aer_113_3_2 p.14-14 Section III, equation (1): Defines its treatment indicator as whether a lease was allocated by auction rather than negotiation, with the  |
| `other:administrative_share_adjustment` | 1 | 50% | aer_113_3_2 p.7-7 Section II: Notes that administrative payment data for one leasing category are recorded only as a fixed statutory half-sh |
| `other:nuisance_function_definition` | 1 | 50% | aer_107_5_51 p.2-2 Section I, discussion before eq. (5)-(6): Nuisance parameters are defined as the pair of potential-outcome regression functions and the propensity score |
| `other:overlap_restriction` | 1 | 50% | aer_107_5_51 p.3-3 Assumption 1(ii): The formal assumption restricts every estimated propensity score to lie within a fixed interval strictly insid |
| `other:score_function_definition` | 1 | 50% | aer_107_5_51 p.2-2 eq. (5)-(6): For the ATE the moment score combines an augmented inverse-propensity-weighting-style correction for each trea |
| `other:zero_heavy_outcome_handling` | 1 | 50% | aer_113_3_2 p.20-21 Section IVB: Explains that because a large share of leases are never drilled and record exactly zero output and revenue in  |

### writing_structure (papers with this category: 2/2)

| tag | papers | share | example pointers (artid p.pages locator: statement) |
|---|---|---|---|
| `appendix_heavy` | 2 | 100% | aer_107_5_51 p.4-4 Section II, closing paragraph: The note relies on an online appendix for the proof of its only theorem, keeping the printed text limited to m; aer_113_3_2 p.12-32 Footnotes throughout: Frequently defers supporting analyses, including contractual-clause coding, a duration model of unleased spell |
| `contribution_paragraph` | 2 | 100% | aer_107_5_51 p.1-1 opening paragraph: The opening paragraph frames the note's contribution as illustrating, in the ATE and ATTE setting, a companion; aer_113_3_2 p.1-5 Introduction: Its introduction previews the main payment and output findings, situates the paper's contribution against shor |
| `roadmap_paragraph` | 2 | 100% | aer_107_5_51 p.1-1 opening paragraph, last sentence: The closing sentence of the introduction points readers to a companion working paper for more general discussi; aer_113_3_2 p.1-5 Introduction: Its introduction previews the main payment and output findings, situates the paper's contribution against shor |
| `data_before_design` | 1 | 50% | aer_113_3_2 p.5-10 Sections I-III: Presents institutional background and the data description before formally stating the empirical strategy and  |
| `design_before_data` | 1 | 50% | aer_107_5_51 p.1-4 overall structure: The note proceeds directly from the treatment-effect model and identification argument to the estimation algor |
| `in_main_text` | 1 | 50% | aer_113_3_2 p.16-21 Tables 4-6: Folds most robustness checks directly into its main results tables as additional columns rather than collectin |
| `main_result_first` | 1 | 50% | aer_113_3_2 p.15-25 Sections IV-VI: Presents its primary payment result before the output and allocative-efficiency results, and defers all discus |
| `mechanisms_after_main` | 1 | 50% | aer_113_3_2 p.15-25 Sections IV-VI: Presents its primary payment result before the output and allocative-efficiency results, and defers all discus |
| `results_previewed_in_intro` | 1 | 50% | aer_113_3_2 p.1-5 Introduction: Its introduction previews the main payment and output findings, situates the paper's contribution against shor |

## Paper versus code (concordance with recipe cards)

| item | status | count | examples |
|---|---|---|---|
| cluster_level | agree | 2 | aer_107_5_51 s1.se.cluster_level (paper: No clustering of standard errors is proposed or discussed anywhere in  / card: cluster_level is recorded as null for every traced specification.); aer_113_3_2 specifications.s1.se.cluster_level; specifications.s2.se.cluster_level (paper: States in table notes that standard errors are clustered by grid, matc / card: specifications.s1.se = {type: cluster, cluster_level: ['Grid10']}; spe) |
| controls | agree | 2 | aer_107_5_51 s1.controls_summary (paper: Controls enter only as the generic vector Z inside the nuisance functi / card: controls_summary is recorded as null for every traced specification, i); aer_113_3_2 specifications.s1.formula_or_call; specifications.s3.formula_or_call (paper: States that all specifications control flexibly for lease size, a spli / card: specifications.s1 and s2 formula_or_call include bs(Acres, df = 4); sp) |
| data_source | unknown | 1 | aer_107_5_51 data[0] / data[1] (paper: States only that empirical illustrations and code are available as sup / card: Card records two datasets (sipp1991.dta, penn_jae.dat) but leaves type) |
| data_source | paper_only | 1 | aer_113_3_2 data.0 (paper: Describes its lease- and royalty-level data as obtained directly from  / card: data[0] records access='unknown' and source_hint=null, evidenced in th) |
| diagnostic | agree | 2 | aer_107_5_51 diagnostics (paper: No empirical diagnostic such as a balance, first-stage, density or pla / card: Card's diagnostics array is empty.); aer_113_3_2 diagnostics.x1 (paper: Its stated identification diagnostics are a location-fixed-effect bala / card: diagnostics.x1 = {kind: 'pretrend_test', status: 'not_found_in_scope'}) |
| estimator | agree | 2 | aer_107_5_51 d1.estimand (paper: States the ATE (and, separately, the ATTE) as the target parameter. / card: Design d1 records its estimand as 'average treatment effect (ATE)'.); aer_113_3_2 specifications.s1; specifications.s3 (paper: Estimates lease-level regressions of log bonus payments on an auction  / card: designs.d1 (panel_fe): specifications.s1 is a feols call, LogBonus ~ A) |
| estimator | disagree | 1 | aer_107_5_51 d1.variant (paper: Main text presents a fully interactive treatment-effect model in which / card: Design d1 is classified with variant 'dml_plr' (partial linear regress) |
| fixed_effects | agree | 2 | aer_107_5_51 s1.fixed_effects (paper: The model has no fixed-effects terms; it is a potential-outcomes model / card: fixed_effects is recorded as null for every traced specification.); aer_113_3_2 specifications.s1.fixed_effects; specifications.s2.fixed_effects (paper: States that its bonus regressions include fixed effects for a spatial  / card: specifications.s1.fixed_effects = ['Grid10Yr','YearQtr']; specificatio) |
| other | agree | 1 | aer_107_5_51 s1.command / s2.command / s3.command / s4.command / s5.command / s6.command (paper: Names boosted, tree, random-forest and ensemble or hybrid methods as e / card: The six traced specifications implement RLasso, Trees, Forest, Boostin) |
| outputs | agree | 2 | aer_107_5_51 outputs.tables[0] (paper: No results table or figure appears in the main text; the estimator's o / card: Card records a single unformatted output, a result matrix printed to t); aer_113_3_2 outputs.tables.t1 (paper: Presents its bonus and output regression results in numbered in-text t / card: outputs.tables has one entry (t1) with output_ref 'stacked_regressions) |
| robustness | agree | 1 | aer_107_5_51 conventions[2].description (paper: Section III recommends repeating cross-fitting over many random partit / card: A recorded coding convention describes point estimates and standard er) |
| robustness | unknown | 1 | aer_113_3_2 outputs.tables.t1; specifications.s1 (paper: States in the main text that it reruns its bonus specification after a / card: All four recorded specifications come from a script named for lease ad) |
| sample | agree | 1 | aer_113_3_2 specifications.s2.sample; pipeline.sample_restrictions (paper: States that its output and production-revenue regressions restrict the / card: specifications.s2.sample = '!Censored'; specifications.s4.sample = '!C) |
| se_type | agree | 2 | aer_107_5_51 s1.se.type (representative of s1-s6) (paper: Reports an analytic asymptotic standard error built from the sample va / card: Each traced specification (s1-s6) records se.type as 'robust', compute); aer_113_3_2 specifications.s3.se; specifications.s4.se (paper: Gives no explicit standard-error or clustering description for its dou / card: specifications.s3.se = {type: 'iid', cluster_level: null}; specificati) |
| weights | agree | 2 | aer_107_5_51 s1.weights (paper: The final estimator averages the K fold-specific estimates with equal  / card: weights is recorded as null for every traced specification.); aer_113_3_2 specifications.s1.weights; specifications.s2.weights; specifications.s3.weights; specifications.s4.weights (paper: Makes no mention of regression weights for any reported specification; / card: specifications.s1 through s4 all record weights as null.) |

## Gaps the readers reported

- (1) No sample_construction observations: the main text never describes the empirical illustration's data source, unit of obs
- (1) No heterogeneity_reported observations: the model is stated to allow fully heterogeneous treatment effects, but no heter
- (1) No mechanism_evidence observations: the note is purely about estimation and inference for a treatment-effect parameter a
- (1) No magnitude_interpretation observations: with no empirical results table in the main text, there are no effect sizes to
- (1) No external_validity observations: generalizability of the ATE/ATTE beyond the (unstated) illustration sample is not dis
- (1) No preregistration_or_ethics observations: no preregistration, IRB approval or consent statement appears; only an NSF fu
- (1) No explicit statement that standard errors are or are not clustered; the absence of clustering is inferred from the vari
- (1) No explicit sentence justifies the choice of spatial grid as the clustering level beyond its correspondence to the fixed
- (1) No stated standard-error or clustering description is given anywhere for the double/debiased machine-learning specificat
- (1) No multiple-testing adjustment is described despite many outcome-by-specification combinations being reported and indivi
- (1) No preregistration, IRB approval, or consent statement; not applicable in an obvious sense, as the paper analyzes second
- (1) The paper's several online appendices (additional extensions, alternative outcome definitions, the lease-addenda contrac
- (1) No formal weak-instrument or first-stage statistic is reported anywhere, consistent with the design not using an instrum

## Pointer format

artid + note sha256 (Inputs) + observation id + page range + locator. Statements are the reader's paraphrases; re-read the page before citing.
