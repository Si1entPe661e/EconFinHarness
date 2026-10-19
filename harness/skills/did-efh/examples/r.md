# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `did::aggte`

Used in 5 of 1163 R papers (0.4%) — Aggregate Group-Time Average Treatment Effects.

Options (share of these 5 papers): `type` 100%, `na.rm` 60%.

Most common option set: `na.rm`, `type`; at least one call in 3 papers (60%).

```r
      results_CS <- aggte(fit_attgt, type = "dynamic", na.rm = TRUE)
```
ReStud 2026, [doi:10.1093/restud/rdag063](https://doi.org/10.1093/restud/rdag063), `code/zenodo_18464228/replication_package_archive1/codes/2_rf/5_state_reins_DiD_premiums.R` line 501.

Next most common option set: `type`; at least one call in 2 papers (40%).

```r
est_2 <- aggte(est_1, type = "dynamic")
```
AER 2023, [doi:10.1257/aer.20210937](https://doi.org/10.1257/aer.20210937), `code/AER_DataReplication/code/CallawaySantAnna.R` line 24.

### `did::att_gt`

Used in 5 of 1163 R papers (0.4%) — Group-Time Average Treatment Effects.

Options (share of these 5 papers): `data` 100%, `gname` 100%, `idname` 100%, `tname` 100%, `yname` 100%, `clustervars` 80%, `control_group` 80%, `base_period` 60%, `allow_unbalanced_panel` 40%, `bstrap` 40%.

Most common option set: `allow_unbalanced_panel`, `base_period`, `clustervars`, `data`, `gname`, `idname`, `tname`, `yname`; at least one call in 1 paper (20%).

```r
      fit_attgt <-  att_gt(yname = yVar, tname = "year", idname = "id", gname = "G",
                           clustervars = "state", data = df, allow_unbalanced_panel = TRUE, base_period = "universal")
```
ReStud 2026, [doi:10.1093/restud/rdag063](https://doi.org/10.1093/restud/rdag063), `code/zenodo_18464228/replication_package_archive1/codes/2_rf/7_state_reins_DiD_reins_purchase.R` lines 523-524.

Next most common option set: `base_period`, `bstrap`, `cband`, `clustervars`, `control_group`, `data`, `gname`, `idname`, `tname`, `xformla`, `yname`; at least one call in 1 paper (20%).

```r
  example_attgt <- att_gt(yname = "greenness",
                          tname = "year",
                          idname = "uniqueid",
                          gname = "foundationCS",
                          xformla = as.formula(fml),
                          control_group = control_group,
                          base_period = 'universal',
                          clustervars = c("uniqueid", 'cddaid'),
                          data = cleandat,
                          cband = FALSE,
                          bstrap = FALSE
  )
```
ReStud 2026, [doi:10.1093/restud/rdag080](https://doi.org/10.1093/restud/rdag080), `code/zenodo_18849776/EUForest_Workspace/EUForest Workspace/analysis/10_Robustness.r` lines 788-799.
