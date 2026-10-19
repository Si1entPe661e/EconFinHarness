# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `gmm::gmm`

Used in 5 of 1163 R papers (0.4%) — Generalized Method of Moments and Generalized Empirical Likelihood.

Options (share of these 5 papers): `t0` 60%, `itermax` 40%, `wmatrix` 40%, `x` 40%.

Most common option set: none; at least one call in 1 paper (20%).

```r
    fit = gmm(p.obj, subdata, params0)
```
JFE 2022, [doi:10.1016/j.jfineco.2021.09.025](https://doi.org/10.1016/j.jfineco.2021.09.025), `code/mendeley_yvvmsz4dkt_v1/replication_code/replication_code/producing_tables_and_figures/14_estimate_gmm_with_shock_size_cutoffs.R` line 111.

Next most common option set: `control`, `crit`, `itermax`, `method`, `t0`, `type`, `wmatrix`; at least one call in 1 paper (20%).

```r
  ma <- gmm(function_for_estimation,data_for_gmm, t0=initial_points,
            crit=1e-6,type = "iterative", method="BFGS",control = list(maxit=100),itermax = 100, wmatrix=w_matrix)
```
ReStud 2026, [doi:10.1093/restud/rdag032](https://doi.org/10.1093/restud/rdag032), `code/zenodo_18764264/replication_package/empirics/script/gmm_functions.R` lines 48-49.
