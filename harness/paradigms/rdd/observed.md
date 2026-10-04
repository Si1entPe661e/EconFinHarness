# Observed practices: `rdd` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 10 validated recipe cards (12 designs, 32 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | Stata: 10, R: 3, MATLAB: 1, Python: 1 |
| journal | ReStud: 4, AER: 3, JPE: 1, QJE: 1, RFS: 1 |
| year | 2026: 3, 2024: 2, 2025: 2, 2020: 1, 2022: 1, 2023: 1 |
| coverage | partial: 9, minimal: 1 |
| variant | fuzzy: 4, unknown: 4, kink: 1, multiple_cutoffs_normalized: 1 |

Excluded (held out): aer_107_1_5, ecta_92_3_6, jpe_132_9_2, qje_140_1_11

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| aer_110_2_5 | AER | 2020 | partial | Stata | d32584402688 |
| aer_112_10_8 | AER | 2022 | partial | Stata, Python | 348eb4eb33a8 |
| aer_114_11_1 | AER | 2024 | partial | Stata | 5b72962dea23 |
| jpe_2026_740226 | JPE | 2026 | partial | Stata | 079df41ea9ad |
| qje_2026_qje_qjaf045 | QJE | 2026 | partial | Stata | b986edf0b8c6 |
| restud_2025_restud_rdae108 | ReStud | 2025 | partial | Stata | b087f50050bf |
| restud_2025_restud_rdaf004 | ReStud | 2025 | partial | Stata, R | 344c9dc1ea96 |
| restud_2026_restud_rdag071 | ReStud | 2026 | partial | Stata, R | 7dea8313ae4a |
| restud_90_1_3 | ReStud | 2023 | minimal | Stata, MATLAB, R | 9e8f71dbd90d |
| rfs_2024_rfs_hhae045 | RFS | 2024 | partial | Stata | 07529fc94ce7 |

## Observations

### Design variants (design.variant)

Denominator 10 papers; unknown in 4.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `fuzzy` | 4 | 67% | - | Stata 4 | aer_110_2_5 d2 code/aer_replication/dofiles/Table_fuzzy_iv.do:55-56; jpe_2026_740226 d1 code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:268-268; restud_2025_restud_rdae108 d2 code/zenodo_13314638/electoral_turnovers_replication_package/replication_package/do/3_2_3_table_3.do:8-8 |
| `kink` | 1 | 17% | - | Stata 1 | aer_112_10_8 d2 code/5_0_Appendix.do:1723-1723 |
| `multiple_cutoffs_normalized` | 1 | 17% | - | Stata 1 | aer_114_11_1 d1 code/code/main_analysis.do:471-471 |

### Estimators (specification.estimator)

Denominator 10 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `local_polynomial_rd` | 5 | 50% | 11 | Stata 5 | aer_112_10_8 s2 code/5_0_Appendix.do:1723-1723; jpe_2026_740226 s1 code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:67-67; qje_2026_qje_qjaf045 s1 code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/3a_main_regressions.do:374-375 |
| `local_linear_rd` | 4 | 40% | 15 | Stata 4 | aer_110_2_5 s1 code/aer_replication/dofiles/Table_main_results.do:62-62; aer_114_11_1 s1 code/code/ado/MultiPanelTabRD.ado:205-207; restud_2025_restud_rdae108 s1 code/zenodo_13314638/electoral_turnovers_replication_package/replication_package/do/3_2_1_table_1.do:6-6 |
| `2sls` | 1 | 10% | 3 | Stata 1 | restud_90_1_3 s1 code/zenodo_6456606/WHAT_IS_A_GOOD_SCHOOL/CODE/27_va_2sls.do:424-424 |
| `hdfe_ols` | 1 | 10% | 1 | Stata 1 | restud_2025_restud_rdaf004 s10 code/zenodo_14200854/Replication/Replication/Do/Pb2_dvui16m_regall_v2_uidata.do:156-156 |
| `ols` | 1 | 10% | 2 | Stata 1 | restud_90_1_3 s4 code/zenodo_6456606/WHAT_IS_A_GOOD_SCHOOL/CODE/47_validation.do:125-125 |

### Commands / functions called

Denominator 10 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `rdrobust` | 10 | 100% | 26 | Stata 10 | aer_110_2_5 s1 code/aer_replication/dofiles/Table_main_results.do:62-62; aer_112_10_8 s2 code/5_0_Appendix.do:1723-1723; aer_114_11_1 s1 code/code/ado/MultiPanelTabRD.ado:205-207 |
| `reghdfe` | 2 | 20% | 2 | Stata 2 | restud_2025_restud_rdaf004 s10 code/zenodo_14200854/Replication/Replication/Do/Pb2_dvui16m_regall_v2_uidata.do:156-156; restud_2026_restud_rdag071 s2 code/zenodo_19662388/package_34964_v2/package/admin_data/code/figures/step5_estimates_dayFine_no80.do:95-97 |
| `areg` | 1 | 10% | 1 | Stata 1 | restud_90_1_3 s5 code/zenodo_6456606/WHAT_IS_A_GOOD_SCHOOL/CODE/47_validation.do:134-134 |
| `ivreghdfe` | 1 | 10% | 3 | Stata 1 | restud_90_1_3 s1 code/zenodo_6456606/WHAT_IS_A_GOOD_SCHOOL/CODE/27_va_2sls.do:424-424 |

### Package attributed to the specification

Denominator 10 papers; unknown in 5.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `rdrobust` | 5 | 100% | 10 | Stata 5 | aer_112_10_8 s2 code/5_0_Appendix.do:1723-1723; jpe_2026_740226 s1 code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:67-67; qje_2026_qje_qjaf045 s1 code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/3a_main_regressions.do:374-375 |

### Standard-error type

Denominator 10 papers; unknown in 3.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `cluster` | 5 | 71% | 16 | Stata 5 | aer_110_2_5 s1 code/aer_replication/dofiles/Table_main_results.do:62-62; aer_114_11_1 s1 code/code/ado/MultiPanelTabRD.ado:205-205; qje_2026_qje_qjaf045 s1 code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/3a_main_regressions.do:356-357 |
| `robust` | 2 | 29% | 2 | Stata 2 | jpe_2026_740226 s1 code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:67-67; rfs_2024_rfs_hhae045 s1 code/dataverse_ABLKE4/Code/produce_table6_final.do:15-15 |

### Number of clustering dimensions

Denominator 10 papers; unknown in 7.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `1` | 3 | 100% | 8 | Stata 3 | aer_114_11_1 s2 code/code/main_analysis.do:121-121; restud_2025_restud_rdaf004 s10 code/zenodo_14200854/Replication/Replication/Do/Pb2_dvui16m_regall_v2_uidata.do:156-156; restud_2026_restud_rdag071 s1 code/zenodo_19662388/package_34964_v2/package/admin_data/code/figures/step5_estimates_dayFine_no80.do:87-87 |

### Number of fixed-effect dimensions

Denominator 10 papers; unknown in 6.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `1` | 3 | 75% | 3 | Stata 3 | restud_2025_restud_rdaf004 s10 code/zenodo_14200854/Replication/Replication/Do/Pb2_dvui16m_regall_v2_uidata.do:156-156; restud_2026_restud_rdag071 s2 code/zenodo_19662388/package_34964_v2/package/admin_data/code/figures/step5_estimates_dayFine_no80.do:95-97; restud_90_1_3 s5 code/zenodo_6456606/WHAT_IS_A_GOOD_SCHOOL/CODE/47_validation.do:134-134 |
| `2` | 1 | 25% | 2 | Stata 1 | qje_2026_qje_qjaf045 s1 code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/3a_main_regressions.do:374-375 |
| `3+` | 1 | 25% | 3 | Stata 1 | restud_90_1_3 s1 code/zenodo_6456606/WHAT_IS_A_GOOD_SCHOOL/CODE/27_va_2sls.do:424-424 |

### Diagnostics (kind:status[:observation])

Denominator 8 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `density_test:unknown` | 4 | 50% | - | unknown 4 | aer_110_2_5 x1 :; restud_2025_restud_rdaf004 x3 :; restud_2026_restud_rdag071 x1 : |
| `bandwidth_selection:observed:call_present` | 3 | 38% | - | Stata 3 | aer_110_2_5 x2 code/aer_replication/dofiles/Table_main_results.do:43-45; aer_114_11_1 x2 code/code/ado/MultiPanelTabRD.ado:200-200; jpe_2026_740226 x3 code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:67-67 |
| `balance:unknown` | 2 | 25% | - | unknown 2 | qje_2026_qje_qjaf045 x1 :; restud_2026_restud_rdag071 x2 : |
| `density_test:not_found_in_scope` | 2 | 25% | - | Stata 2 | aer_114_11_1 x1 code/code/main_analysis.do:; qje_2026_qje_qjaf045 x2 code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/0_master_results.do: |
| `density_test:observed:call_present` | 2 | 25% | - | Stata 2 | jpe_2026_740226 x1 code/dataverse_GXY45B/Code_Output/Fig_A1_A2.do:24-24; restud_2025_restud_rdae108 x2 code/zenodo_13314638/electoral_turnovers_replication_package/replication_package/do/3_1_3_figure_3.do:6-6 |
| `first_stage:observed:call_present` | 2 | 25% | - | Stata 2 | jpe_2026_740226 x4 code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:55-55; restud_2025_restud_rdae108 x1 code/zenodo_13314638/electoral_turnovers_replication_package/replication_package/do/3_1_2_figure_2.do:19-19 |
| `bandwidth_selection:unknown` | 1 | 12% | - | unknown 1 | restud_2025_restud_rdaf004 x4 : |
| `multiple_testing:unknown` | 1 | 12% | - | unknown 1 | qje_2026_qje_qjaf045 x4 : |
| `polynomial_order:observed:call_present` | 1 | 12% | - | Stata 1 | aer_114_11_1 x3 code/code/main_analysis.do:1087-1087 |
| `pretrend_test:unknown` | 1 | 12% | - | unknown 1 | qje_2026_qje_qjaf045 x3 : |

### Robustness checks linked to these specifications (type:relationship)

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `alt_bandwidth:confirmed` | 1 | 50% | - | Stata 1 | jpe_2026_740226 robustness[0] code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:162-164 |
| `alt_bandwidth:unresolved` | 1 | 50% | - | Stata 1 | aer_110_2_5 robustness[0] code/aer_replication/dofiles/Fig_bandwidth_sensitivity.do:24-45 |

### Classification basis of the design

Denominator 10 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 10 | 100% | - | Stata 10 | aer_110_2_5 d1 code/aer_replication/dofiles/Table_main_results.do:22-26; aer_112_10_8 d2 code/5_0_Appendix.do:1723-1723; aer_114_11_1 d1 code/code/main_analysis.do:925-925 |

### Macro / wrapper resolution status of the recorded calls

Denominator 10 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 9 | 90% | 23 | Stata 9 | aer_110_2_5 s1 code/aer_replication/dofiles/Table_main_results.do:62-62; aer_112_10_8 s2 code/5_0_Appendix.do:1723-1723; aer_114_11_1 s2 code/code/main_analysis.do:120-120 |
| `partial` | 4 | 40% | 9 | Stata 4 | aer_114_11_1 s1 code/code/ado/MultiPanelTabRD.ado:205-207; qje_2026_qje_qjaf045 s3 code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/3a_main_regressions.do:478-478; restud_2025_restud_rdae108 s2 code/zenodo_13314638/electoral_turnovers_replication_package/replication_package/do/3_2_1_table_1.do:48-48 |

### Languages of the replication package

Denominator 10 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `Stata` | 10 | 100% | - | Stata 10 | aer_110_2_5  :; aer_112_10_8  :; aer_114_11_1  : |
| `R` | 3 | 30% | - | R 3 | restud_2025_restud_rdaf004  :; restud_2026_restud_rdag071  :; restud_90_1_3  : |
| `MATLAB` | 1 | 10% | - | MATLAB 1 | restud_90_1_3  : |
| `Python` | 1 | 10% | - | Python 1 | aer_112_10_8  : |

## Free-text observations (not counted)

### implementation feature (5)

- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:268-268): Two independent running variables: SABER 11 score and SISBEN index
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:268-268): Sharp discontinuity at each cutoff (cutoff=0)
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:268-268): First stage: beneficiary_spp (receipt of Ser Pilo Paga scholarship)
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:268-268): Bandwidth selection: data-driven (rdrobust default)
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:268-268): Kernel: triangular (rdrobust default)

### sample restriction (8)

- **aer_110_2_5** (code/aer_replication/dofiles/Table_main_results.do:42-45): MSE-optimal bandwidth from rdbwselect
- **aer_110_2_5** (code/aer_replication/dofiles/Table_main_results.do:91-91): Fixed 1-meter window for alternative specs
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:13-13): keep if icfes_per==20142: sample cohort with ICFES exam date 2014/2
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:14-14): eligible_sisben==1 condition for SABER 11 running variable analysis
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:15-15): eligible_saber11==1 condition for SISBEN running variable analysis
- **qje_2026_qje_qjaf045** (code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/3a_main_regressions.do:50-50): Restrict to South==1
- **qje_2026_qje_qjaf045** (code/dataverse_08YUBP/TW-QJE2025-Replication/TW-QJE2025-Replication/code/1a_main.do:112-125): Exclude demsecond cases
- **restud_2026_restud_rdag071** (code/zenodo_19662388/package_34964_v2/package/admin_data/code/build/s04_build_analysis_data.do:37-37): Observation years up to 2019 for 6-month follow-up

### convention (6)

- **aer_114_11_1** (code/code/main_analysis.do:924-924): Running variable pc91_pca_tot_p from 1991 census population
- **aer_114_11_1** (code/code/main_analysis.do:972-972): Cluster ID variables: gp_code_jj11_num (Joshi-Johnson 1995 delimitation), gp_code_lgd21_num (LGD 2021 delimitation)
- **aer_114_11_1** (code/code/main_analysis.do:76-76): Analysis datasets organized under $analysis_data/ by topic: villagedirectory/, amenities/, financial/, nregs/, mission_antyodaya/, gp_elections/, gp_development_plan/
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/Tab_1_2_3_4_A3.do:163-164): Bandwidth stored in global macro after rdrobust call (${bw_r}, ${br_r}) for reuse in heterogeneous subgroup analysis to ensure consistency
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:14-15): Sampling conditions stored as global macros: ${cond_saber11} = 'eligible_sisben==1', ${cond_sisben} = 'eligible_saber11==1'
- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:36-36): matrix ry2014 stores rdrobust results for table/figure production

### unresolved reference (1)

- **jpe_2026_740226** (code/dataverse_GXY45B/Code_Output/3_Results_years_PILA.do:12-12): Data loading source: ${data}/data_RD and ${data2}/PILA_cuatrimestral datasets not publicly available in code


## Gaps and caveats

- facet package: unknown in 5/10 papers; shares are computed over the 5 known papers only
- facet cluster_dimensions: unknown in 7/10 papers; shares are computed over the 3 known papers only
- facet fixed_effects_count: unknown in 6/10 papers; shares are computed over the 4 known papers only
- 9/10 cards have no specification-to-output links; output facets cover the remaining cards only
- 1 minimal-coverage cards contribute positive findings only

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
