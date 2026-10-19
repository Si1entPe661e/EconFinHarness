# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `gmm::gmm`

Used in 5 of 1163 R papers (0.4%) — Generalized Method of Moments and Generalized Empirical Likelihood.

Options (share of these 5 papers): `t0` 60%, `itermax` 40%, `x` 40%, `wmatrix` 40%.

Most common option set: `itermax`, `lower`, `optfct`, `tol`, `upper`; at least one call in 1 paper (20%).

```r
Base_result<-gmm(myg2_par_multi,myX_list,tet0,optfct="nlminb",lower=lb,upper=ub,tol = 1e-8, itermax=10000)
```
AER 2024, [doi:10.1257/aer.20211242](https://doi.org/10.1257/aer.20211242), `code/Code/proc_output_Table6_base2.R` line 52.

Next most common option set: `eqConst`, `t0`, `x`; at least one call in 1 paper (20%).

```r
        dGMM <- gmm(y ~ z, x = zw,t0=t0,eqConst=fixi)
```
AER 2024, [doi:10.1257/aer.20211653](https://doi.org/10.1257/aer.20211653), `code/code/estimate.R` line 34.
