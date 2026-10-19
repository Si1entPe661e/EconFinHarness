# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `ivreg::ivreg`

Used in 7 of 1163 R papers (0.6%) — Instrumental-Variable Regression by 2SLS, 2SM, or 2SMM Estimation.

Options (share of these 7 papers): `data` 100%.

Most common option set: `data`; at least one call in 7 papers (100%).

```r
  model <- ivreg(formula_spec, data = reg_dframe)
```
QJE 2024, [doi:10.1093/qje/qjad031](https://doi.org/10.1093/qje/qjad031), `code/dataverse_LHH29P/readi_evaluation_replication_run_benefit_cost_regressions_R/modeling_functions.R` line 75; license file: GPL.
