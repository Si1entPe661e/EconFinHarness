# Observed practices: `panel_fe` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 7 validated recipe cards (7 designs, 24 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | Stata: 7, MATLAB: 2, Shell: 2, Mathematica: 1, Python: 1, R: 1, SAS: 1 |
| journal | ReStud: 2, AER: 1, Econometrica: 1, JFE: 1, JPE: 1, QJE: 1 |
| year | 2026: 4, 2020: 1, 2024: 1, 2025: 1 |
| coverage | partial: 7 |
| variant | unknown: 7 |

Excluded (held out): aer_113_3_2, rfs_2026_rfs_hhaf081

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| aer_110_5_5 | AER | 2020 | partial | Stata | 60d05dbd2cd9 |
| ecta_92_2_2 | Econometrica | 2024 | partial | Stata, R | 49923149ab2f |
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | partial | Stata, SAS | 540e3dc7853a |
| jpe_2026_740226 | JPE | 2026 | partial | Stata | 079df41ea9ad |
| qje_2026_qje_qjag041 | QJE | 2026 | partial | Stata, MATLAB, Shell | 2cf08bc991af |
| restud_2025_restud_rdaf104 | ReStud | 2025 | partial | Stata, MATLAB | dffaf207fe63 |
| restud_2026_restud_rdag013 | ReStud | 2026 | partial | Python, Stata, Mathematica, Shell | 83ade0c22dcc |

## Observations

### Estimators (specification.estimator)

Denominator 7 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `hdfe_ols` | 4 | 57% | 17 | Stata 4 | aer_110_5_5 s1 code/Do-files/Reach-of-Radio---Results--ROBUST-.do:216-216; jfe_2026_j_jfineco_2025_104223 s1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23; jpe_2026_740226 s5 code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164 |
| `ols` | 2 | 29% | 3 | Stata 2 | ecta_92_2_2 s1 code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62; restud_2025_restud_rdaf104 s1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230 |
| `logit` | 1 | 14% | 1 | Stata 1 | restud_2026_restud_rdag013 s4 code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/src/build/do_descriptive_analysis.do:149-149 |
| `poisson_ppml` | 1 | 14% | 3 | Stata 1 | restud_2026_restud_rdag013 s1 code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/src/build/do_descriptive_analysis.do:239-239 |

### Commands / functions called

Denominator 7 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `reghdfe` | 3 | 43% | 15 | Stata 3 | jfe_2026_j_jfineco_2025_104223 s1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23; jpe_2026_740226 s5 code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164; qje_2026_qje_qjag041 s2 code/dataverse_8P3S0V/replication_ding26/programs/21_heterogeneity_02.do:76-76 |
| `reg` | 2 | 29% | 3 | Stata 2 | ecta_92_2_2 s1 code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62; restud_2025_restud_rdaf104 s1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230 |
| `logit` | 1 | 14% | 1 | Stata 1 | restud_2026_restud_rdag013 s4 code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/src/build/do_descriptive_analysis.do:149-149 |
| `ppmlhdfe` | 1 | 14% | 3 | Stata 1 | restud_2026_restud_rdag013 s1 code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/src/build/do_descriptive_analysis.do:239-239 |
| `reg2hdfespatial` | 1 | 14% | 1 | Stata 1 | aer_110_5_5 s2 code/Do-files/Reach-of-Radio---Results--CONLEY-.do:344-344 |
| `xtreg` | 1 | 14% | 1 | Stata 1 | aer_110_5_5 s1 code/Do-files/Reach-of-Radio---Results--ROBUST-.do:216-216 |

### Package attributed to the specification

Denominator 7 papers; unknown in 6.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `reghdfe` | 1 | 100% | 1 | Stata 1 | jpe_2026_740226 s5 code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164 |

### Standard-error type

Denominator 7 papers; unknown in 2.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `cluster` | 1 | 20% | 1 | Stata 1 | restud_2025_restud_rdaf104 s1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230 |
| `conley_spatial` | 1 | 20% | 1 | Stata 1 | aer_110_5_5 s2 code/Do-files/Reach-of-Radio---Results--CONLEY-.do:344-344 |
| `iid` | 1 | 20% | 1 | Stata 1 | qje_2026_qje_qjag041 s2 code/dataverse_8P3S0V/replication_ding26/programs/21_heterogeneity_02.do:76-76 |
| `randomization_inference` | 1 | 20% | 2 | Stata 1 | ecta_92_2_2 s1 code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62 |
| `robust` | 1 | 20% | 1 | Stata 1 | aer_110_5_5 s1 code/Do-files/Reach-of-Radio---Results--ROBUST-.do:216-216 |
| `twoway_cluster` | 1 | 20% | 13 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23 |

### Number of clustering dimensions

Denominator 7 papers; unknown in 4.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `1` | 2 | 67% | 3 | Stata 2 | ecta_92_2_2 s1 code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62; restud_2025_restud_rdaf104 s1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230 |
| `2` | 1 | 33% | 13 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23 |

### Number of fixed-effect dimensions

Denominator 7 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `2` | 3 | 50% | 10 | Stata 3 | ecta_92_2_2 s1 code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62; jfe_2026_j_jfineco_2025_104223 s1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23; restud_2026_restud_rdag013 s2 code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/src/build/do_descriptive_analysis.do:245-245 |
| `1` | 2 | 33% | 2 | Stata 2 | jpe_2026_740226 s5 code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164; restud_2025_restud_rdaf104 s1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230 |
| `3+` | 2 | 33% | 2 | Stata 2 | qje_2026_qje_qjag041 s2 code/dataverse_8P3S0V/replication_ding26/programs/21_heterogeneity_02.do:76-76; restud_2026_restud_rdag013 s1 code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/src/build/do_descriptive_analysis.do:239-239 |

### Weighted estimation

Denominator 7 papers; unknown in 6.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `weighted` | 1 | 100% | 1 | Stata 1 | restud_2025_restud_rdaf104 s1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230 |

### Diagnostics (kind:status[:observation])

Denominator 3 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `balance:unknown` | 1 | 33% | - | unknown 1 | ecta_92_2_2 x1 : |
| `bandwidth_selection:observed:call_present` | 1 | 33% | - | Stata 1 | restud_2025_restud_rdaf104 x1 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/set_exclusion_distance.do:29-29 |
| `density_test:not_found_in_scope` | 1 | 33% | - | Stata 1 | restud_2025_restud_rdaf104 x2 code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do: |
| `pretrend_plot:not_found_in_scope` | 1 | 33% | - | Stata 1 | aer_110_5_5 x1 code/Do-files/Reach-of-Radio---Results--ROBUST-.do: |

### Robustness checks linked to these specifications (type:relationship)

Denominator 2 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `alt_functional_form:unresolved` | 1 | 100% | - | Stata 1 | aer_110_5_5 robustness[1] code/Do-files/Reach-of-Radio---Results--CONLEY-.do:391-403 |
| `alt_se:confirmed` | 1 | 100% | - | Stata 1 | aer_110_5_5 robustness[0] code/Do-files/Reach-of-Radio---Results--ROBUST-.do:1-6 |

### Classification basis of the design

Denominator 7 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 6 | 86% | - | Stata 6 | aer_110_5_5 d1 code/Do-files/Reach-of-Radio---Results--ROBUST-.do:202-225; jfe_2026_j_jfineco_2025_104223 d1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23; jpe_2026_740226 d2 code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164 |
| `author_statement` | 1 | 14% | - | Stata 1 | ecta_92_2_2 d1 code/zenodo_8408320/replication/replication/code/endline_2_prepare.do:579-581 |

### Designs with a known main/secondary/robustness role

Denominator 7 papers; unknown in 6.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `known` | 1 | 100% | - | Stata 1 | qje_2026_qje_qjag041 d2 code/dataverse_8P3S0V/replication_ding26/programs/21_heterogeneity_02.do:3-3 |

### Macro / wrapper resolution status of the recorded calls

Denominator 7 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 5 | 71% | 21 | Stata 5 | ecta_92_2_2 s1 code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62; jfe_2026_j_jfineco_2025_104223 s1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23; jpe_2026_740226 s5 code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164 |
| `partial` | 1 | 14% | 2 | Stata 1 | aer_110_5_5 s1 code/Do-files/Reach-of-Radio---Results--ROBUST-.do:216-216 |
| `resolved` | 1 | 14% | 1 | Stata 1 | qje_2026_qje_qjag041 s2 code/dataverse_8P3S0V/replication_ding26/programs/21_heterogeneity_02.do:76-76 |

### Languages of the replication package

Denominator 7 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `Stata` | 7 | 100% | - | Stata 7 | aer_110_5_5  :; ecta_92_2_2  :; jfe_2026_j_jfineco_2025_104223  : |
| `MATLAB` | 2 | 29% | - | MATLAB 2 | qje_2026_qje_qjag041  :; restud_2025_restud_rdaf104  : |
| `Shell` | 2 | 29% | - | Shell 2 | qje_2026_qje_qjag041  :; restud_2026_restud_rdag013  : |
| `Mathematica` | 1 | 14% | - | Mathematica 1 | restud_2026_restud_rdag013  : |
| `Python` | 1 | 14% | - | Python 1 | restud_2026_restud_rdag013  : |
| `R` | 1 | 14% | - | R 1 | ecta_92_2_2  : |
| `SAS` | 1 | 14% | - | SAS 1 | jfe_2026_j_jfineco_2025_104223  : |

## Free-text observations (not counted)

### implementation feature (11)

- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): interaction with epsilonit (intermediary exposure)
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): two-way clustering (permno, date)
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): multiple shock types tested
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164): Fixed effects at program level (codigo_prog)
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164): Multiple sets of controls (models a-f)
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164): Model a: individual baseline characteristics
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/4_value_added_model.do:164-164): Model f: adds prior school and college peer characteristics
- **restud_2025_restud_rdaf104** (code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:214-214): Triangular kernel weighting: max(1-tribdist/h, 0)
- **restud_2025_restud_rdaf104** (code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:214-214): Running variable: tribdist_signed (signed distance to tributary confluence)
- **restud_2025_restud_rdaf104** (code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:214-214): Bandwidth selection via rdbwselect (optimal MSE-RD, CCD)
- **restud_2025_restud_rdaf104** (code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:214-214): Clustered bootstrap for standard errors (1000 replications)

### sample restriction (3)

- **ecta_92_2_2** (code/zenodo_8408320/replication/replication/code/endline_2_prepare.do:579-579): Eligible borrowers: type==1 borrowers in baseline and 2016 endline, or eligible_2017==1 in 2017 endline
- **ecta_92_2_2** (code/zenodo_8408320/replication/replication/code/survey_analysis.do:62-62): Analysis restricted to el_eligible==1 sample
- **restud_2026_restud_rdag013** (code/zenodo_16987699/inspections_final_v2_zip/inspections_final_v2/snakefile:13-13): Data years 2012-2020

### convention (10)

- **aer_110_5_5** (code/Do-files/Reach-of-Radio---Results--ROBUST-.do:70-70): Global macro system for paths and variable lists
- **ecta_92_2_2** (code/zenodo_8408320/replication/replication/Master.do:10-10): Global macros for data, code, tables, figures directories (${dropbox}, ${data}, ${code}, ${temp_data}, ${tables}, ${figures})
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): Fixed effects specification: ab(permno date) notation in reghdfe specifies stock-by-time two-way FE absorption
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): Interaction syntax: c.intermediary_shock#c.epsilonit creates fully-interacted term
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table2_and_Table3.do:11-11): Portfolio-level analysis: data aggregated to quintile × date level before ivreg2 estimation
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:78-78): Output names: figures exported as .png in Figures/ subdirectory; tables as .tex in Tables/ subdirectory
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:163-164): Bandwidth stored in global macro after rdrobust call (${bw_r}, ${br_r}) for reuse in heterogeneous subgroup analysis to ensure consistency
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:14-15): Sampling conditions stored as global macros: ${cond_saber11} = 'eligible_sisben==1', ${cond_sisben} = 'eligible_saber11==1'
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:36-36): matrix ry2014 stores rdrobust results for table/figure production
- **restud_2025_restud_rdaf104** (code/zenodo_17085642/replication_folder_share/replication_folder_share/code/analysis_tracts.do:230-230): Fixed effects absorbed (not shown in coefficient table) via absorb() option

### unresolved reference (1)

- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:12-12): Data loading source: ${data}/data_RD and ${data2}/PILA_cuatrimestral datasets not publicly available in code


## Gaps and caveats

- facet package: unknown in 6/7 papers; shares are computed over the 1 known papers only
- facet cluster_dimensions: unknown in 4/7 papers; shares are computed over the 3 known papers only
- facet weights: unknown in 6/7 papers; shares are computed over the 1 known papers only
- facet robustness_type: unknown in 1/2 papers; shares are computed over the 1 known papers only
- facet role_known: unknown in 6/7 papers; shares are computed over the 1 known papers only
- 6/7 cards have no specification-to-output links; output facets cover the remaining cards only
- no design variants recorded; variant-conditional rules cannot be derived from this set

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
