# Observed practices: `fama_macbeth` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 4 validated recipe cards (4 designs, 4 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | Python: 3, Stata: 3, Jupyter: 1, MATLAB: 1, SAS: 1 |
| journal | JFE: 2, RFS: 2 |
| year | 2026: 2, 2024: 1, 2025: 1 |
| coverage | partial: 3, minimal: 1 |
| variant | unknown: 3, two-step cross-sectional: 1 |

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| jfe_2024_j_jfineco_2023_103746 | JFE | 2024 | minimal | Stata, Python, Jupyter | 57b4f9fa808e |
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | partial | Stata, SAS | 540e3dc7853a |
| rfs_2025_rfs_hhae056 | RFS | 2025 | partial | Stata, Python | 49185ccbebf0 |
| rfs_2026_rfs_hhag042 | RFS | 2026 | partial | Python, MATLAB | 5a303477da95 |

## Observations

### Design variants (design.variant)

Denominator 4 papers; unknown in 3.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `two-step cross-sectional` | 1 | 100% | - | Stata 1 | jfe_2024_j_jfineco_2023_103746 d2 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:3-3 |

### Estimators (specification.estimator)

Denominator 3 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `other:fama_macbeth` | 3 | 100% | 4 | Stata 2, Python 1 | jfe_2024_j_jfineco_2023_103746 s1 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:37-37; jfe_2026_j_jfineco_2025_104223 s14 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table1.do:16-17; rfs_2026_rfs_hhag042 s2 code/dataverse_BO8SQ8/programs/programs/02_analysis/analysis_fama_macbeth.py:113-114 |

### Commands / functions called

Denominator 3 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `FamaMacBeth` | 1 | 33% | 1 | Python 1 | rfs_2026_rfs_hhag042 s2 code/dataverse_BO8SQ8/programs/programs/02_analysis/analysis_fama_macbeth.py:113-114 |
| `xtfmb` | 1 | 33% | 1 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s14 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table1.do:16-17 |
| `xtfmb_mion` | 1 | 33% | 2 | Stata 1 | jfe_2024_j_jfineco_2023_103746 s1 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:37-37 |

### Standard-error type

Denominator 3 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `hac_newey_west` | 2 | 100% | 2 | Stata 1, Python 1 | jfe_2024_j_jfineco_2023_103746 s2 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:102-102; rfs_2026_rfs_hhag042 s2 code/dataverse_BO8SQ8/programs/programs/02_analysis/analysis_fama_macbeth.py:114-114 |
| `iid` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2023_103746 s1 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:89-89 |

### Diagnostics (kind:status[:observation])

Denominator 1 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `multiple_testing:not_found_in_scope` | 1 | 100% | - | Stata 1 | rfs_2025_rfs_hhae056 x1 code/dataverse_JTU2GF/Table 6_9.do: |

### Classification basis of the design

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 4 | 100% | - | Stata 3, Python 1 | jfe_2024_j_jfineco_2023_103746 d2 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:3-3; jfe_2026_j_jfineco_2025_104223 d4 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table1.do:16-16; rfs_2025_rfs_hhae056 d2 code/dataverse_JTU2GF/Table 6_9.do:757-757 |

### Macro / wrapper resolution status of the recorded calls

Denominator 3 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 2 | 67% | 2 | Stata 1, Python 1 | jfe_2026_j_jfineco_2025_104223 s14 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table1.do:16-17; rfs_2026_rfs_hhag042 s2 code/dataverse_BO8SQ8/programs/programs/02_analysis/analysis_fama_macbeth.py:113-114 |
| `partial` | 1 | 33% | 2 | Stata 1 | jfe_2024_j_jfineco_2023_103746 s1 code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/ADOs/xtfmb_mion.ado:89-89 |

### Languages of the replication package

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `Python` | 3 | 75% | - | Python 3 | jfe_2024_j_jfineco_2023_103746  :; rfs_2025_rfs_hhae056  :; rfs_2026_rfs_hhag042  : |
| `Stata` | 3 | 75% | - | Stata 3 | jfe_2024_j_jfineco_2023_103746  :; jfe_2026_j_jfineco_2025_104223  :; rfs_2025_rfs_hhae056  : |
| `Jupyter` | 1 | 25% | - | Jupyter 1 | jfe_2024_j_jfineco_2023_103746  : |
| `MATLAB` | 1 | 25% | - | MATLAB 1 | rfs_2026_rfs_hhag042  : |
| `SAS` | 1 | 25% | - | SAS 1 | jfe_2026_j_jfineco_2025_104223  : |

## Free-text observations (not counted)

### implementation feature (5)

- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table1.do:16-16): lag(8) for time-series averaging
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table1.do:16-16): controls for multiple firm characteristics
- **rfs_2025_rfs_hhae056** (code/dataverse_JTU2GF/Table 6_9.do:757-757): monthly cross-sectional regressions
- **rfs_2025_rfs_hhae056** (code/dataverse_JTU2GF/Table 6_9.do:757-757): Newey-West lag(1) adjustment
- **rfs_2025_rfs_hhae056** (code/dataverse_JTU2GF/Table 6_9.do:757-757): time-series average of monthly coefficients

### sample restriction (2)

- **jfe_2024_j_jfineco_2023_103746** (code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/Anomalies_1_get_Sortvars_All.do:36-37): All sample group: filter on ret!=. (non-missing returns)
- **jfe_2024_j_jfineco_2023_103746** (code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/Anomalies_2_make_Portfolios.do:83-83): Portfolio_Analysis_wOverlap_gt Make_Portf Portf_Ret with overlapping option

### convention (6)

- **jfe_2024_j_jfineco_2023_103746** (code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/Combine_All_TimeSeries_Vars.do:45-45): Global macros defined in loops (foreach constructs) to apply factor sets across variable lists
- **jfe_2024_j_jfineco_2023_103746** (code/mendeley_tzxtm6ys99_v1/Cooper_Gulen_Ion_Replication_Code_And_Data/07_CODE/Anomalies_2_make_Portfolios.do:22-22): Anomaly names shorthand (e.g., AG, NOA, BM) used throughout for sort variables and factors
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): Fixed effects specification: ab(permno date) notation in reghdfe specifies stock-by-time two-way FE absorption
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): Interaction syntax: c.intermediary_shock#c.epsilonit creates fully-interacted term
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table2_and_Table3.do:11-11): Portfolio-level analysis: data aggregated to quintile × date level before ivreg2 estimation
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:78-78): Output names: figures exported as .png in Figures/ subdirectory; tables as .tex in Tables/ subdirectory


## Gaps and caveats

- facet variant: unknown in 3/4 papers; shares are computed over the 1 known papers only
- 4/4 cards have no specification-to-output links; output facets cover the remaining cards only
- 1 minimal-coverage cards contribute positive findings only
- fewer than 5 papers: shares are not meaningful; use as pointers only

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
