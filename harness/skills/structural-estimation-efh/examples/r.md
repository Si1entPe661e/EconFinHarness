# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `stats::optim`

Used in 120 of 1163 R papers (10%) — General-purpose Optimization.

Options (share of these 120 papers): `method` 81%, `control` 52%, `fn` 52%, `par` 46%, `lower` 45%, `upper` 39%, `gr` 21%, `hessian` 12%, `X` 6%, `Y` 5%.

Most common option set: `method`; at least one call in 9 papers (8%).

```r
  pars_gvb  <- optim( c(0,0), kl_gaussian_target, method = "BFGS")
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf082](https://doi.org/10.1093/jrsssb/qkaf082), `code/github_Francesco16p_SkewAppr_Post/Section 4.1 [Simulation]/Functions_Poisson_1D.R` line 186; license file: MIT.

### `stats::optimize`

Used in 50 of 1163 R papers (4%) — One Dimensional Optimization.

Options (share of these 50 papers): `interval` 48%, `maximum` 34%, `lower` 28%, `upper` 28%, `tol` 22%, `f` 12%, `l` 8%, `alpha` 8%, `d` 4%, `b` 4%.

Most common option set: none; at least one call in 8 papers (16%).

```r
  optimize(function(z, ...) (p - sum2llr_cdf_chi2(z, tuning.power, alpha, lambda0, null = null, upper.integration.limit, ...))^2,
           c(2*lower1, upper.integration.limit))$minimum
```
JASA 2026, [doi:10.1080/01621459.2025.2544397](https://doi.org/10.1080/01621459.2025.2544397), `code/github_richarddmorey_MoreyDavisStober_pcurveASA/R_utility/unused_utility_pcurve.R` lines 203-204; license file: MIT.

### `nleqslv::nleqslv`

Used in 24 of 1163 R papers (2%) — Solving systems of nonlinear equations with Broyden or Newton.

Options (share of these 24 papers): `control` 46%, `fn` 29%, `x` 21%, `method` 17%, `jac` 12%, `global` 8%.

Most common option set: none; at least one call in 10 papers (42%).

```r
  root <- nleqslv(120, f)   # 0.5 is the initial guess
```
RFS 2026, [doi:10.1093/rfs/hhag070](https://doi.org/10.1093/rfs/hhag070), `code/dataverse_A9NGRV/StocksAsLotteriesPackage/StocksAsLotteriesPackage_5/codes/figures_theory.R` line 457.

Next most common option set: `control`; at least one call in 5 papers (21%).

```r
	fitg <- nleqslv(g0, EEg, control = cntl)
```
JASA 2026, [doi:10.1080/01621459.2026.2723402](https://doi.org/10.1080/01621459.2026.2723402), `code/figshare_33352559/reproducibility_materials/reproducibility_materials/Reproducibility/Shared Functions/cqr.R` line 246.

### `stats::nlm`

Used in 18 of 1163 R papers (2%) — Non-Linear Minimization.

Options (share of these 18 papers): `iterlim` 33%, `print.level` 22%, `p` 22%, `hessian` 17%, `stepmax` 17%, `f` 17%, `ndigit` 11%, `gradtol` 11%, `typsize` 11%, `x` 11%.

Most common option set: none; at least one call in 4 papers (22%).

```r
beta=nlm(f,c(1,1,1,1,1,1,1,1,1,1,1))
```
JPE 2025, [doi:10.1086/736207](https://doi.org/10.1086/736207), `code/dataverse_SDDSES/MD_DWMD.R` line 55.

### `CVXR::Problem`

Used in 15 of 1163 R papers (1%) — Create an Optimization Problem.

Options (share of these 15 papers): `constraints` 27%.

Most common option set: none; at least one call in 12 papers (80%).

```r
    prob <- Problem(objective,
                    list(p_norm(coef, "inf") <= 1,
                         p_norm(D %*% coef, 1) <= lambda))
```
JASA 2026, [doi:10.1080/01621459.2026.2670746](https://doi.org/10.1080/01621459.2026.2670746), `code/figshare_32316049/np-qualint-JASA.R` lines 281-283; license file: MIT.

Next most common option set: `constraints`; at least one call in 4 papers (27%).

```r
  problem <- Problem(objective, constraints = list(sum(betaHat)== 1, betaHat >= 0))
```
JASA 2026, [doi:10.1080/01621459.2025.2542553](https://doi.org/10.1080/01621459.2025.2542553), `code/figshare_29828922/codes_revised/codes revised/codes for data analysis/causal_fx_kfilter_nomatch.R` line 1092.

### `CVXR::Variable`

Used in 15 of 1163 R papers (1%) — Create an Optimization Variable.

Options (share of these 15 papers): `PSD` 13%.

Most common option set: none; at least one call in 14 papers (93%).

```r
  lambda <- Variable(r)
```
JRSSB 2025, [doi:10.1093/jrsssb/qkaf009](https://doi.org/10.1093/jrsssb/qkaf009), `code/github_JinyuanChang-Lab_BayesianPenalizedEL/Comparison with the Optimization Methods/opt_optim_Linear_IV.R` line 27; license file: GPL.

### `nloptr::nloptr`

Used in 13 of 1163 R papers (1%) — R interface to NLopt.

Options (share of these 13 papers): `opts` 100%, `eval_f` 92%, `x0` 85%, `lb` 77%, `ub` 69%, `eval_g_ineq` 46%, `eval_grad_f` 38%, `eval_jac_g_ineq` 31%, `eval_g_eq` 23%, `eval_jac_g_eq` 15%.

Most common option set: `eval_f`, `eval_g_ineq`, `eval_grad_f`, `eval_jac_g_ineq`, `lb`, `opts`, `ub`, `x0`; at least one call in 2 papers (15%).

```r
  res<-nloptr(x0=x0,eval_f=eval_f,eval_grad_f=eval_grad_f,eval_g_ineq=eval_g_ineq,
              eval_jac_g_ineq=eval_jac_g,
              opts=opts,lb=rep(0,K),ub=rep(1,K))
```
JASA 2025, [doi:10.1080/01621459.2025.2476786](https://doi.org/10.1080/01621459.2025.2476786), `code/figshare_28590278/online_supplements_13_/online_supplements/code/project/bsnip_experiment/mixed_mirt.R` lines 450-452.

### `CVXR::Minimize`

Used in 11 of 1163 R papers (0.9%) — Create a Minimization Objective.

Most common option set: none; at least one call in 11 papers (100%).

```r
       prob <- Problem(Minimize(obj),constr)
```
Econometrica 2025, [doi:10.3982/ecta19153](https://doi.org/10.3982/ecta19153), `code/zenodo_15171317/spadystouli_MS19153_replication/spadystouli_MS19153_replication/GTR_implementation/xpert8d_ss.R` line 108.
