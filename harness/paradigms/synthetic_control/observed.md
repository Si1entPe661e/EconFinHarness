# Observed practices: `synthetic_control` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 2 validated recipe cards (2 designs, 5 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | R: 1, Stata: 1 |
| journal | JFE: 1, JPE: 1 |
| year | 2024: 1, 2026: 1 |
| coverage | minimal: 1, partial: 1 |
| variant | unknown: 2 |

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| jfe_2024_j_jfineco_2024_103809 | JFE | 2024 | minimal | Stata | 6da2e7ba75a8 |
| jpe_2026_742424 | JPE | 2026 | partial | R | b558e191a8f5 |

## Observations

### Estimators (specification.estimator)

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `synthetic_did` | 2 | 100% | 2 | Stata 1, R 1 | jfe_2024_j_jfineco_2024_103809 s3 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_sdid.do:213-213; jpe_2026_742424 s3 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:103-107 |
| `did_twfe` | 1 | 50% | 1 | R 1 | jpe_2026_742424 s2 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:96-101 |
| `synthetic_control` | 1 | 50% | 2 | R 1 | jpe_2026_742424 s1 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:89-94 |

### Commands / functions called

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `li2020` | 1 | 50% | 1 | R 1 | jpe_2026_742424 s4 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:109-113 |
| `scinference` | 1 | 50% | 2 | R 1 | jpe_2026_742424 s1 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:89-94 |
| `sdid` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s3 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_sdid.do:213-213 |
| `synthdid_estimate` | 1 | 50% | 1 | R 1 | jpe_2026_742424 s3 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:103-107 |

### Package attributed to the specification

Denominator 2 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `scinference` | 1 | 100% | 2 | R 1 | jpe_2026_742424 s1 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:89-94 |
| `synthdid` | 1 | 100% | 1 | R 1 | jpe_2026_742424 s3 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:103-107 |

### Standard-error type

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `bootstrap` | 1 | 50% | 2 | R 1 | jpe_2026_742424 s3 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:105-105 |
| `cluster` | 1 | 50% | 1 | R 1 | jpe_2026_742424 s1 code/dataverse_CVRPTZ/code_auxiliary scripts/intro_bias.R:47-47 |
| `randomization_inference` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s3 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_sdid.do:191-191 |

### Classification basis of the design

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 2 | 100% | - | Stata 1, R 1 | jfe_2024_j_jfineco_2024_103809 d3 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_sdid.do:181-181; jpe_2026_742424 d1 code/dataverse_CVRPTZ/code_auxiliary scripts/intro_bias.R:1-3 |

### Designs with a known main/secondary/robustness role

Denominator 2 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `known` | 1 | 100% | - | R 1 | jpe_2026_742424 d1 code/dataverse_CVRPTZ/code_auxiliary scripts/intro_bias.R:1-3 |

### Macro / wrapper resolution status of the recorded calls

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 1 | 50% | 4 | R 1 | jpe_2026_742424 s1 code/dataverse_CVRPTZ/code_auxiliary scripts/app_sweden.R:89-94 |
| `partial` | 1 | 50% | 1 | Stata 1 | jfe_2024_j_jfineco_2024_103809 s3 code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_sdid.do:213-213 |

### Languages of the replication package

Denominator 2 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `R` | 1 | 50% | - | R 1 | jpe_2026_742424  : |
| `Stata` | 1 | 50% | - | Stata 1 | jfe_2024_j_jfineco_2024_103809  : |

## Free-text observations (not counted)


## Gaps and caveats

- facet package: unknown in 1/2 papers; shares are computed over the 1 known papers only
- facet role_known: unknown in 1/2 papers; shares are computed over the 1 known papers only
- 2/2 cards have no specification-to-output links; output facets cover the remaining cards only
- 1 minimal-coverage cards contribute positive findings only
- fewer than 5 papers: shares are not meaningful; use as pointers only
- no design variants recorded; variant-conditional rules cannot be derived from this set

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
