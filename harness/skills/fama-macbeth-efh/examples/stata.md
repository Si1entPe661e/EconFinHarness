# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `asreg`

Used in 24 of 1904 Stata papers (1%) — module to estimate rolling window regressions, Fama-MacBeth and by(group) regressions.

Options (share of these 24 papers): `fmb` 38%, `newey` 38%, `min` 25%, `wind` 25%, `fit` 21%, `by` 17%, `se` 17%, `fitted` 8%, `window` 8%.

Most common option set: `fmb`, `newey`; at least one call in 7 papers (29%).

```stata
asreg risk_dummy_F1   ${CL_c} INF_L1, fmb newey(2)
```
RFS 2026, [doi:10.1093/rfs/hhag020](https://doi.org/10.1093/rfs/hhag020), `code/dataverse_LIZIIP/RFS_SXZ_Uploaded_codes/Uploaded_codes/2_Regression_all_tables.do` line 42.

Next most common option set: none; at least one call in 4 papers (17%).

```stata
by idN: asreg y_eq1 x_eq1 
```
JFE 2026, [doi:10.1016/j.jfineco.2026.104291](https://doi.org/10.1016/j.jfineco.2026.104291), `code/mendeley_vzptvmwm9s_v2/JFEreplication/JFE_4_FormatExperimentalData.do` line 127.
