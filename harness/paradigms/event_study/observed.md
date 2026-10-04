# Observed practices: `event_study` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 8 validated recipe cards (8 designs, 19 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | Stata: 6, R: 3, Python: 1 |
| journal | ReStud: 4, Econometrica: 1, JFE: 1, JPE: 1, RFS: 1 |
| year | 2025: 3, 2026: 3, 2023: 1, 2024: 1 |
| coverage | partial: 8 |
| variant | unknown: 8 |

Excluded (held out): qje_139_1_2, rfs_2024_rfs_hhae015

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| ecta_2024_ecta19872 | Econometrica | 2024 | partial | Stata | d2542afe3a89 |
| jfe_2025_j_jfineco_2025_104150 | JFE | 2025 | partial | Stata | ae1876f6b30d |
| jpe_2026_740222 | JPE | 2026 | partial | R | d293619802d1 |
| restud_2025_restud_rdae091 | ReStud | 2025 | partial | Stata | 66cf5a7ba433 |
| restud_2026_restud_rdaf071 | ReStud | 2026 | partial | Stata, R | 9296fd2f202a |
| restud_2026_restud_rdag011 | ReStud | 2026 | partial | Stata, Python | 99f324f7e405 |
| restud_90_5_13 | ReStud | 2023 | partial | R | 167c1843b508 |
| rfs_2025_rfs_hhaf065 | RFS | 2025 | partial | Stata | f29ba4a87d9c |

## Observations

### Estimators (specification.estimator)

Denominator 8 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `hdfe_ols` | 5 | 62% | 5 | Stata 3, R 2 | ecta_2024_ecta19872 s1 code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:45-45; jfe_2025_j_jfineco_2025_104150 s2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15; jpe_2026_740222 s1 code/dataverse_GZMO6B/replication/code/5_empirical_analysis/table1_heat_rate.R:162-162 |
| `ols` | 2 | 25% | 2 | Stata 1, R 1 | restud_2025_restud_rdae091 s20 code/zenodo_10983057/v2/v2/main_figures.do:72-72; restud_90_5_13 s1 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-compareCIs.R:33-33 |
| `other:sdid` | 1 | 12% | 1 | Stata 1 | restud_2026_restud_rdag011 s5 code/zenodo_15675543/Replication_package_for_Jumpstarting_an_International_Currency/Replication package for Jumpstarting an International Currency/ReplicationCode/Codes/Part1Analysis1.do:770-770 |
| `poisson_ppml` | 1 | 12% | 9 | Stata 1 | rfs_2025_rfs_hhaf065 s1 code/dataverse_VX7HYE/rfs_tables.do:196-196 |

### Commands / functions called

Denominator 8 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `reghdfe` | 2 | 25% | 2 | Stata 2 | jfe_2025_j_jfineco_2025_104150 s2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15; restud_2026_restud_rdaf071 s3 code/zenodo_16539681/Replication/Replication/code/do/2_analysis/main/figure2.do:45-45 |
| `acreg` | 1 | 12% | 1 | Stata 1 | restud_2025_restud_rdae091 s20 code/zenodo_10983057/v2/v2/main_figures.do:72-72 |
| `createSensitivityResults_relativeMagnitudes` | 1 | 12% | 2 | R 1 | restud_90_5_13 s1 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-compareCIs.R:33-33 |
| `did_multiplegt_old` | 1 | 12% | 1 | Stata 1 | ecta_2024_ecta19872 s1 code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55 |
| `felm` | 1 | 12% | 1 | R 1 | restud_90_5_13 s3 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/LovenheimWillen-Scripts/LovenheimWillen-EstimateEventStudies.R:25-26 |
| `feols` | 1 | 12% | 1 | R 1 | jpe_2026_740222 s1 code/dataverse_GZMO6B/replication/code/5_empirical_analysis/table1_heat_rate.R:162-162 |
| `ppmlhdfe` | 1 | 12% | 9 | Stata 1 | rfs_2025_rfs_hhaf065 s1 code/dataverse_VX7HYE/rfs_tables.do:196-196 |
| `rmvnorm` | 1 | 12% | 1 | R 1 | restud_90_5_13 s5 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/simulationStudy/simulationStudy_drawEventStudyCoefficients_parallelTrends.R:53-53 |
| `sdid` | 1 | 12% | 1 | Stata 1 | restud_2026_restud_rdag011 s5 code/zenodo_15675543/Replication_package_for_Jumpstarting_an_International_Currency/Replication package for Jumpstarting an International Currency/ReplicationCode/Codes/Part1Analysis1.do:770-770 |

### Package attributed to the specification

Denominator 8 papers; unknown in 5.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `lfe` | 1 | 33% | 1 | R 1 | restud_90_5_13 s3 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/LovenheimWillen-Scripts/LovenheimWillen-EstimateEventStudies.R:25-26 |
| `ppmlhdfe` | 1 | 33% | 7 | Stata 1 | rfs_2025_rfs_hhaf065 s2 code/dataverse_VX7HYE/rfs_tables.do:199-199 |
| `sdid` | 1 | 33% | 1 | Stata 1 | restud_2026_restud_rdag011 s5 code/zenodo_15675543/Replication_package_for_Jumpstarting_an_International_Currency/Replication package for Jumpstarting an International Currency/ReplicationCode/Codes/Part1Analysis1.do:770-770 |

### Standard-error type

Denominator 8 papers; unknown in 4.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `cluster` | 4 | 100% | 12 | Stata 3, R 1 | ecta_2024_ecta19872 s1 code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55; jfe_2025_j_jfineco_2025_104150 s2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15; jpe_2026_740222 s1 code/dataverse_GZMO6B/replication/code/5_empirical_analysis/table1_heat_rate.R:162-162 |

### Number of clustering dimensions

Denominator 8 papers; unknown in 5.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `1` | 3 | 100% | 11 | Stata 3 | ecta_2024_ecta19872 s1 code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55; jfe_2025_j_jfineco_2025_104150 s2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15; rfs_2025_rfs_hhaf065 s1 code/dataverse_VX7HYE/rfs_tables.do:196-196 |

### Number of fixed-effect dimensions

Denominator 8 papers; unknown in 6.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `1` | 1 | 50% | 9 | Stata 1 | rfs_2025_rfs_hhaf065 s1 code/dataverse_VX7HYE/rfs_tables.do:196-196 |
| `2` | 1 | 50% | 1 | Stata 1 | jfe_2025_j_jfineco_2025_104150 s2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15 |

### Diagnostics (kind:status[:observation])

Denominator 5 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `pretrend_plot:not_found_in_scope` | 2 | 40% | - | R 1, Stata 1 | restud_90_5_13 x2 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-PlotEventStudy.R:; rfs_2025_rfs_hhaf065 x1 code/dataverse_VX7HYE/rfs_figures.do: |
| `balance:observed:call_present:unscoped` | 1 | 20% | - | Stata 1 | jfe_2025_j_jfineco_2025_104150 x2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/tab5.do:27-29 |
| `event_window:observed:call_present` | 1 | 20% | - | Stata 1 | restud_2026_restud_rdag011 x2 code/zenodo_15675543/Replication_package_for_Jumpstarting_an_International_Currency/Replication package for Jumpstarting an International Currency/ReplicationCode/Codes/Part1Analysis1.do:1042-1042 |
| `heterogeneous_treatment_effects:unknown` | 1 | 20% | - | unknown 1 | rfs_2025_rfs_hhaf065 x2 : |
| `pretrend_plot:observed:output_code_present` | 1 | 20% | - | Stata 1 | restud_2025_restud_rdae091 x1 code/zenodo_10983057/v2/v2/main_figures.do:76-76 |
| `pretrend_test:observed:call_present` | 1 | 20% | - | R 1 | restud_90_5_13 x1 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-compareCIs.R:20-24 |
| `pretrend_test:unknown` | 1 | 20% | - | unknown 1 | jfe_2025_j_jfineco_2025_104150 x1 : |

### Robustness checks linked to these specifications (type:relationship)

Denominator 3 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `alt_estimator:confirmed` | 2 | 100% | - | Stata 1, R 1 | restud_2026_restud_rdag011 robustness[3] code/zenodo_15675543/Replication_package_for_Jumpstarting_an_International_Currency/Replication package for Jumpstarting an International Currency/ReplicationCode/Codes/Part1Analysis1.do:770-770; restud_90_5_13 robustness[0] code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/LovenheimWillen-Scripts/LovenheimWillen-constructSensitivityPlots.R:36-37 |

### Classification basis of the design

Denominator 8 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 6 | 75% | - | Stata 4, R 2 | ecta_2024_ecta19872 d1 code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55; jpe_2026_740222 d1 code/dataverse_GZMO6B/replication/code/5_empirical_analysis/table1_heat_rate.R:161-162; restud_2025_restud_rdae091 d2 code/zenodo_10983057/v2/v2/main_figures.do:49-72 |
| `unknown` | 2 | 25% | - | Stata 2 | jfe_2025_j_jfineco_2025_104150 d1 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15; rfs_2025_rfs_hhaf065 d1 code/dataverse_VX7HYE/rfs_tables.do:193-193 |

### Macro / wrapper resolution status of the recorded calls

Denominator 8 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 6 | 75% | 8 | Stata 4, R 2 | ecta_2024_ecta19872 s1 code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55; jfe_2025_j_jfineco_2025_104150 s2 code/mendeley_zhrnypkcyb_v2/Final_Replication_Package/Final Replication Package/Code and Instructions/fig4.do:15-15; jpe_2026_740222 s1 code/dataverse_GZMO6B/replication/code/5_empirical_analysis/table1_heat_rate.R:161-162 |
| `partial` | 3 | 38% | 11 | Stata 2, R 1 | restud_2026_restud_rdaf071 s3 code/zenodo_16539681/Replication/Replication/code/do/2_analysis/main/figure2.do:45-45; restud_90_5_13 s3 code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/LovenheimWillen-Scripts/LovenheimWillen-EstimateEventStudies.R:25-25; rfs_2025_rfs_hhaf065 s1 code/dataverse_VX7HYE/rfs_tables.do:196-196 |

### Languages of the replication package

Denominator 8 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `Stata` | 6 | 75% | - | Stata 6 | ecta_2024_ecta19872  :; jfe_2025_j_jfineco_2025_104150  :; restud_2025_restud_rdae091  : |
| `R` | 3 | 38% | - | R 3 | jpe_2026_740222  :; restud_2026_restud_rdaf071  :; restud_90_5_13  : |
| `Python` | 1 | 12% | - | Python 1 | restud_2026_restud_rdag011  : |

## Free-text observations (not counted)

### implementation feature (5)

- **ecta_2024_ecta19872** (code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55): Staggered treatment 1992-2009
- **ecta_2024_ecta19872** (code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55): Linear trends by 2-digit sector
- **ecta_2024_ecta19872** (code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55): Dynamic effects: 12 leads/lags
- **ecta_2024_ecta19872** (code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55): Placebo tests: 4 lags
- **ecta_2024_ecta19872** (code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:55-55): Robust SE clustered at firm

### author stated assumption (2)

- **restud_90_5_13** (code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-compareCIs.R:20-25): parallel trends assumption may be violated
- **restud_90_5_13** (code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-compareCIs.R:33-33): Use createSensitivityResults_relativeMagnitudes to bound post-treatment violations

### sample restriction (2)

- **ecta_2024_ecta19872** (code/zenodo_11431164/Uploaded_4thRound/Uploaded_4thRound/Scripts_Simulated/Main Results/mainreg_eligbefore_sim.do:21-21): Balanced panel 1992-2009; positive employment; complete reporting
- **restud_90_5_13** (code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-import.R:20-20): Benzarti-Carloni: extracts event study coefficients matching treatment year pattern

### convention (5)

- **restud_2025_restud_rdae091** (code/zenodo_10983057/v2/v2/create_provinces.do:12-12): Conditional logic on id variable: replace name_en based on id values
- **restud_2025_restud_rdae091** (code/zenodo_10983057/v2/v2/create_provinces.do:6-8): Treatment and control variables interact with famine indicator (famine=1 if year==1932)
- **restud_2025_restud_rdae091** (code/zenodo_10983057/v2/v2/create_provinces.do:199-200): Outcome variable is forward difference: fmortality = f.mortality (captures 1933 outcome from 1932 covariates)
- **restud_2026_restud_rdag011** (code/zenodo_15675543/Replication_package_for_Jumpstarting_an_International_Currency/Replication package for Jumpstarting an International Currency/ReplicationCode/Codes/Part1Analysis1.do:119-120): Global variables for control specifications ($Tradecontrols, $PolicyControls, $NeighbourControls, $LogControls) used across all did_imputation specifications
- **restud_90_5_13** (code/zenodo_7388015/HonestParallelTrends_RESTUD_ReplicationFiles/HonestParallelTrends_RESTUD_ReplicationFiles/Code/BenzartiCarloni-Scripts/BenzartiCarloni-import.R:31-31): Intermediate results stored as RDS objects in Temp/ for sequential loading


## Gaps and caveats

- facet package: unknown in 5/8 papers; shares are computed over the 3 known papers only
- facet se_type: unknown in 4/8 papers; shares are computed over the 4 known papers only
- facet cluster_dimensions: unknown in 5/8 papers; shares are computed over the 3 known papers only
- facet fixed_effects_count: unknown in 6/8 papers; shares are computed over the 2 known papers only
- 8/8 cards have no specification-to-output links; output facets cover the remaining cards only
- no design variants recorded; variant-conditional rules cannot be derived from this set

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
