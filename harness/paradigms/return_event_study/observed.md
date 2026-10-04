# Observed practices: `return_event_study` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 3 validated recipe cards (3 designs, 2 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | Stata: 3, Python: 1, SAS: 1 |
| journal | JFE: 2, RFS: 1 |
| year | 2024: 1, 2025: 1, 2026: 1 |
| coverage | partial: 2, minimal: 1 |
| variant | unknown: 3 |

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| jfe_2024_j_jfineco_2024_103809 | JFE | 2024 | minimal | Stata | 6da2e7ba75a8 |
| jfe_2026_j_jfineco_2025_104223 | JFE | 2026 | partial | Stata, SAS | 540e3dc7853a |
| rfs_2025_rfs_hhae056 | RFS | 2025 | partial | Stata, Python | 49185ccbebf0 |

## Observations

### Estimators (specification.estimator)

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `2sls` | 1 | 50% | 1 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s18 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7 |
| `ols` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s1 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:294-294 |

### Commands / functions called

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `ivreg2` | 1 | 50% | 1 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s18 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7 |
| `reg` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s1 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:294-294 |

### Package attributed to the specification

Denominator 2 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `ivreg2` | 1 | 100% | 1 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s18 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7 |

### Standard-error type

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `cluster` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s1 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:294-294 |
| `hac_newey_west` | 1 | 50% | 1 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s18 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7 |

### Number of clustering dimensions

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `1` | 2 | 100% | 2 | Stata 2 | jfe_2024_j_jfineco_2024_103809 s1 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:294-294; jfe_2026_j_jfineco_2025_104223 s18 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7 |

### Diagnostics (kind:status[:observation])

Denominator 1 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `pretrend_plot:not_found_in_scope` | 1 | 100% | - | Stata 1 | jfe_2026_j_jfineco_2025_104223 x1 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do: |

### Classification basis of the design

Denominator 3 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 3 | 100% | - | Stata 3 | jfe_2024_j_jfineco_2024_103809 d1 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:106-106; jfe_2026_j_jfineco_2025_104223 d3 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7; rfs_2025_rfs_hhae056 d4 code/dataverse_JTU2GF/Table 11.do:832-832 |

### Macro / wrapper resolution status of the recorded calls

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 1 | 50% | 1 | Stata 1 | jfe_2026_j_jfineco_2025_104223 s18 code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7 |
| `partial` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s1 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:294-294 |

### Languages of the replication package

Denominator 3 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `Stata` | 3 | 100% | - | Stata 3 | jfe_2024_j_jfineco_2024_103809  :; jfe_2026_j_jfineco_2025_104223  :; rfs_2025_rfs_hhae056  : |
| `Python` | 1 | 33% | - | Python 1 | rfs_2025_rfs_hhae056  : |
| `SAS` | 1 | 33% | - | SAS 1 | jfe_2026_j_jfineco_2025_104223  : |

## Free-text observations (not counted)

### implementation feature (8)

- **jfe_2024_j_jfineco_2024_103809** (code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:106-106): CAPM 1-factor market model
- **jfe_2024_j_jfineco_2024_103809** (code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:106-106): Fama-French 3-factor market model
- **jfe_2024_j_jfineco_2024_103809** (code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_car.do:106-106): Estimation window: 300 to 60 trading days before event
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7): 30-month window before/after
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7): Newey-West HAC inference
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table6.do:7-7): multiple FF6 factor specifications with different control groups
- **rfs_2025_rfs_hhae056** (code/dataverse_JTU2GF/Table 11.do:832-832): cumulative abnormal return around earnings announcements
- **rfs_2025_rfs_hhae056** (code/dataverse_JTU2GF/Table 11.do:832-832): clustered standard errors by permno

### convention (4)

- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): Fixed effects specification: ab(permno date) notation in reghdfe specifies stock-by-time two-way FE absorption
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:23-23): Interaction syntax: c.intermediary_shock#c.epsilonit creates fully-interacted term
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table2_and_Table3.do:11-11): Portfolio-level analysis: data aggregated to quintile × date level before ivreg2 estimation
- **jfe_2026_j_jfineco_2025_104223** (code/mendeley_9z43x4c6yr_v2/Code/Analysis/Table7.do:78-78): Output names: figures exported as .png in Figures/ subdirectory; tables as .tex in Tables/ subdirectory


## Gaps and caveats

- facet package: unknown in 1/2 papers; shares are computed over the 1 known papers only
- 3/3 cards have no specification-to-output links; output facets cover the remaining cards only
- 1 minimal-coverage cards contribute positive findings only
- fewer than 5 papers: shares are not meaningful; use as pointers only
- no design variants recorded; variant-conditional rules cannot be derived from this set

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
