# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `scoringRules::crps_sample`

Used in 6 of 1163 R papers (0.5%) — Scoring Rules for Parametric and Simulated Distribution Forecasts.

Options (share of these 6 papers): `y` 50%, `dat` 50%.

Most common option set: `dat`, `y`; at least one call in 3 papers (50%).

```r
    scores_ens[["crps"]] <- crps_sample(y = y, 
                                        dat = ens) }
```
JRSSB 2026, [doi:10.1093/jrsssb/qkag066](https://doi.org/10.1093/jrsssb/qkag066), `code/github_GGavrilos_SMCS/Wind_Gust/fn_eval.R` lines 540-541.

Next most common option set: none; at least one call in 3 papers (50%).

```r
        crps_vec[j] <- crps_sample(Ytest[j], zM[, j])
```
JASA 2026, [doi:10.1080/01621459.2025.2529025](https://doi.org/10.1080/01621459.2025.2529025), `code/github_kevinli1324_ADMIN-GP/R_Results/BART_emulation.R` line 67.
