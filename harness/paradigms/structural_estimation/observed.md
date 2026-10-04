# Observed practices: `structural_estimation` (draft, generated)

Generated 2026-09-08T18:37:31Z by fhb distill fh-distill-0.1.0 from 4 validated recipe cards (4 designs, 7 specifications). Counting unit: paper. Shares are computed over papers with a known value; unknown counts are shown separately and never mean "not used". Recommendations are kept separately in `recommendations.md`.

## Denominators

| dimension | counts |
|---|---|
| language | Stata: 3, MATLAB: 2, R: 2, Shell: 2, C: 1, Python: 1 |
| journal | ReStud: 2, Econometrica: 1, JPE: 1 |
| year | 2025: 3, 2023: 1 |
| coverage | partial: 4 |
| variant | unknown: 2, discrete_choice: 1, dynamic_auction_demand: 1 |

## Inputs

| artid | journal | year | coverage | languages | card sha256 |
|---|---|---|---|---|---|
| ecta_2025_ecta22303 | Econometrica | 2025 | partial | R, MATLAB, C, Shell | 582eabfeb41e |
| jpe_2025_735509 | JPE | 2025 | partial | Stata, R | b9bfe1a70546 |
| restud_90_5_11 | ReStud | 2023 | partial | Stata, Python | a0076029c654 |
| restud_92_2_7 | ReStud | 2025 | partial | Stata, MATLAB, Shell | 50a2117e7feb |

## Observations

### Design variants (design.variant)

Denominator 4 papers; unknown in 2.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `discrete_choice` | 1 | 50% | - | R 1 | jpe_2025_735509 d2 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:128-128 |
| `dynamic_auction_demand` | 1 | 50% | - | MATLAB 1 | restud_92_2_7 d1 code/zenodo_10416565/replication_package/replication_package/code/fn_bids.m:30-30 |

### Estimators (specification.estimator)

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `gmm` | 2 | 50% | 2 | Stata 2 | restud_90_5_11 s6 code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/structural_subsample.do:63-63; restud_92_2_7 s2 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:210-210 |
| `mle` | 2 | 50% | 3 | R 1, MATLAB 1 | jpe_2025_735509 s5 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:62-62; restud_92_2_7 s1 code/zenodo_10416565/replication_package/replication_package/code/step_5_estimation.m:66-66 |
| `cox_hazard` | 1 | 25% | 1 | Stata 1 | restud_92_2_7 s3 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:65-66 |
| `hdfe_ols` | 1 | 25% | 1 | R 1 | ecta_2025_ecta22303 s3 code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/scripts/Structural_Model_Fitting.R:369-369 |

### Commands / functions called

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `gmm` | 2 | 50% | 2 | Stata 2 | restud_90_5_11 s6 code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/structural_subsample.do:63-63; restud_92_2_7 s2 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:210-210 |
| `feols` | 1 | 25% | 1 | R 1 | ecta_2025_ecta22303 s3 code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/scripts/Structural_Model_Fitting.R:369-369 |
| `fminunc` | 1 | 25% | 1 | MATLAB 1 | restud_92_2_7 s1 code/zenodo_10416565/replication_package/replication_package/code/step_5_estimation.m:66-66 |
| `ml model d0` | 1 | 25% | 1 | Stata 1 | restud_92_2_7 s3 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:65-66 |
| `mle2` | 1 | 25% | 2 | R 1 | jpe_2025_735509 s5 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:95-96 |

### Package attributed to the specification

Denominator 4 papers; unknown in 3.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `bbmle` | 1 | 100% | 2 | R 1 | jpe_2025_735509 s5 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:95-96 |

### Standard-error type

Denominator 4 papers; unknown in 2.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `bootstrap` | 1 | 50% | 1 | MATLAB 1 | restud_92_2_7 s1 code/zenodo_10416565/replication_package/replication_package/code/step_5_estimation.m:124-124 |
| `iid` | 1 | 50% | 1 | Stata 1 | restud_92_2_7 s3 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:65-66 |
| `other:hessian_inverse` | 1 | 50% | 2 | R 1 | jpe_2025_735509 s5 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:205-205 |
| `robust` | 1 | 50% | 1 | Stata 1 | restud_92_2_7 s2 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:215-216 |

### Number of fixed-effect dimensions

Denominator 4 papers; unknown in 2.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `0` | 1 | 50% | 2 | MATLAB 1 | restud_92_2_7 s1 code/zenodo_10416565/replication_package/replication_package/code/step_5_estimation.m:80-81 |
| `1` | 1 | 50% | 1 | Stata 1 | restud_92_2_7 s2 code/zenodo_10416565/replication_package/replication_package/code/step_3_firststage.do:210-210 |
| `2` | 1 | 50% | 1 | R 1 | ecta_2025_ecta22303 s3 code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/scripts/Structural_Model_Fitting.R:374-374 |

### Diagnostics (kind:status[:observation])

Denominator 1 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `overid:unknown` | 1 | 100% | - | unknown 1 | restud_90_5_11 x2 : |

### Output formats

Denominator 4 papers; unknown in 3.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `tex` | 1 | 100% | - | unknown 1 | restud_92_2_7 t1 code/zenodo_10416565/replication_package/replication_package/README.md:126-130 |

### Classification basis of the design

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `code_trace` | 4 | 100% | - | R 2, Stata 1, MATLAB 1 | ecta_2025_ecta22303 d3 code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/Master.R:200-222; jpe_2025_735509 d2 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:128-128; restud_90_5_11 d2 code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/structural_subsample.do:3-5 |

### Designs with a known main/secondary/robustness role

Denominator 4 papers; unknown in 1.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `known` | 3 | 100% | - | R 1, Stata 1, MATLAB 1 | ecta_2025_ecta22303 d3 code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/Master.R:200-222; restud_90_5_11 d2 code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/structural_subsample.do:3-5; restud_92_2_7 d1 code/zenodo_10416565/replication_package/replication_package/code/fn_bids.m:30-30 |

### Macro / wrapper resolution status of the recorded calls

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `direct` | 3 | 75% | 6 | R 2, MATLAB 1 | ecta_2025_ecta22303 s3 code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/scripts/Structural_Model_Fitting.R:369-369; jpe_2025_735509 s5 code/dataverse_M7MEXG/BiddingForFirms_ReplicationPackage_code/Hv.R:95-96; restud_92_2_7 s1 code/zenodo_10416565/replication_package/replication_package/code/step_5_estimation.m:80-81 |
| `partial` | 1 | 25% | 1 | Stata 1 | restud_90_5_11 s6 code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/structural_subsample.do:63-63 |

### Languages of the replication package

Denominator 4 papers; unknown in 0.

| value | papers | share of known | specs | by language | evidence (artid record path:lines) |
|---|---|---|---|---|---|
| `Stata` | 3 | 75% | - | Stata 3 | jpe_2025_735509  :; restud_90_5_11  :; restud_92_2_7  : |
| `MATLAB` | 2 | 50% | - | MATLAB 2 | ecta_2025_ecta22303  :; restud_92_2_7  : |
| `R` | 2 | 50% | - | R 2 | ecta_2025_ecta22303  :; jpe_2025_735509  : |
| `Shell` | 2 | 50% | - | Shell 2 | ecta_2025_ecta22303  :; restud_92_2_7  : |
| `C` | 1 | 25% | - | C 1 | ecta_2025_ecta22303  : |
| `Python` | 1 | 25% | - | Python 1 | restud_90_5_11  : |

## Free-text observations (not counted)

### sample restriction (3)

- **ecta_2025_ecta22303** (code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/scripts/estimate_notch_updated.R:28-28): Loan amount must be positive (Phys_Amount_Disbursed > 0)
- **ecta_2025_ecta22303** (code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/scripts/estimate_notch_updated.R:31-31): Must have verified loss amount (non-missing Current_Verified_Loss)
- **restud_90_5_11** (code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/analysis_subsample.do:28-29): Exclude universally licensed occupations (gt==1)

### convention (3)

- **ecta_2025_ecta22303** (code/zenodo_14871772/analysis_-_Replication_2_/analysis - Replication/Master.R:42-42): Relative file paths throughout (./data/, ./figures/, ./tables/, ./scripts/); working directory set to analysis - Replication/
- **restud_90_5_11** (code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/modules/README.md:11-11): Results stored to CSV via store_est_tpl, then templated into LaTeX tables via table_from_tpl.py
- **restud_90_5_11** (code/zenodo_7140346/KleinerSoltas_replication3/REPLICATION/code/analysis/analysis_subsample.do:42-42): Data weights used: earnwt (CPS earnings weight), wtfinl (CPS final weight)


## Gaps and caveats

- facet variant: unknown in 2/4 papers; shares are computed over the 2 known papers only
- facet package: unknown in 3/4 papers; shares are computed over the 1 known papers only
- facet se_type: unknown in 2/4 papers; shares are computed over the 2 known papers only
- facet fixed_effects_count: unknown in 2/4 papers; shares are computed over the 2 known papers only
- facet output_format: unknown in 3/4 papers; shares are computed over the 1 known papers only
- 2/4 cards have no specification-to-output links; output facets cover the remaining cards only
- fewer than 5 papers: shares are not meaningful; use as pointers only

## Evidence pointer format

`artid` + card sha256 (see Inputs) + record id (d = design, s = specification, x = diagnostic, t/f = output) + source path relative to `Paper/<Journal>/articles/<artid>/` + inclusive line range. Re-verify against the current card and source before citing.
