# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `glmnet::cv.glmnet`

Used in 92 of 1163 R papers (8%) — Lasso and Elastic-Net Regularized Generalized Linear Models.

Options (share of these 92 papers): `family` 58%, `alpha` 53%, `nfolds` 40%, `x` 36%, `y` 36%, `intercept` 34%, `standardize` 24%, `penalty.factor` 16%, `lambda` 14%, `type.measure` 13%.

Most common option set: `family`, `x`, `y`; at least one call in 9 papers (10%).

```r
lambda.cv <- cv.glmnet(x = as.matrix(xtrain), y = ytrain, family = "binomial")
```
JASA 2023, [doi:10.1080/01621459.2021.1938084](https://doi.org/10.1080/01621459.2021.1938084), `code/github_ytstat_RaSE-screening-codes/real_data.R` line 165; license file: GPL.

### `glmnet::glmnet`

Used in 90 of 1163 R papers (8%) — Lasso and Elastic-Net Regularized Generalized Linear Models.

Options (share of these 90 papers): `lambda` 84%, `family` 62%, `alpha` 59%, `intercept` 48%, `x` 37%, `y` 37%, `standardize` 31%, `penalty.factor` 26%, `weights` 6%, `nlambda` 6%.

Most common option set: `alpha`, `lambda`; at least one call in 11 papers (12%).

```r
  mod <- glmnet :: glmnet(X_tr, dat_tr[,1], alpha = alpha, lambda = mod_lambda)
```
JASA 2026, [doi:10.1080/01621459.2025.2529602](https://doi.org/10.1080/01621459.2025.2529602), `code/github_chenxuan-he_GoFHD2/simulation_codes/motivatingExample.R` line 56; license file: MIT.

### `randomForest::randomForest`

Used in 41 of 1163 R papers (4%) — Breiman and Cutlers Random Forests for Classification and Regression.

Options (share of these 41 papers): `data` 54%, `ntree` 51%, `x` 39%, `y` 39%, `mtry` 34%, `importance` 32%, `nodesize` 17%, `maxnodes` 12%, `na.action` 10%, `xtest` 7%.

Most common option set: `data`; at least one call in 7 papers (17%).

```r
forest_occ_1 <- randomForest(as.factor(occ_be) ~ . , data=occ_all_indep_1)
```
Econometrica 2026, [doi:10.3982/ecta21835](https://doi.org/10.3982/ecta21835), `code/zenodo_17803155/Replication_package/Replication package/R scripts/Random_forest_occupations.R` line 64.

### `mgcv::gam`

Used in 19 of 1163 R papers (2%) — Generalized additive models with integrated smoothness estimation.

Options (share of these 19 papers): `data` 84%, `family` 32%, `weights` 21%, `method` 16%, `formula` 11%, `select` 11%.

Most common option set: `data`; at least one call in 6 papers (32%).

```r
  GM_m_noagej <- gam(SE_j_hat ~ stage + dep + CVD + COPD + Diabetes + Renal + EP,
                     data = dfc2012_males)
```
JASA 2026, [doi:10.1080/01621459.2025.2547968](https://doi.org/10.1080/01621459.2025.2547968), `code/figshare_29950540/Code/Code/Reproduce/src/06_synthetic_males.R` lines 302-303; license file: GPL.

Next most common option set: `data`, `family`; at least one call in 4 papers (21%).

```r
        mod <- gam(formula, data = df, family = Gamma())
```
JASA 2025, [doi:10.1080/01621459.2023.2270748](https://doi.org/10.1080/01621459.2023.2270748), `code/figshare_24328745/Code_for_empirical_results/Code for empirical results/STAR_code/STAR_convex.R` line 106.

### `mgcv::s`

Used in 12 of 1163 R papers (1%) — Defining smooths in GAM formulae.

Options (share of these 12 papers): `bs` 42%, `k` 33%.

Most common option set: none; at least one call in 9 papers (75%).

```r
x5 <- mgcv::gam(Y~s(X[,5]))
```
JASA 2026, [doi:10.1080/01621459.2025.2555059](https://doi.org/10.1080/01621459.2025.2555059), `code/figshare_30153079/code/code/supermarket.R` line 190.

Next most common option set: `bs`; at least one call in 3 papers (25%).

```r
formu.min<-as.formula(y ~ s(x1,bs="cr"))
```
JASA 2025, [doi:10.1080/01621459.2025.2516181](https://doi.org/10.1080/01621459.2025.2516181), `code/figshare_29306909/simu.R` line 63.

### `grf::causal_forest`

Used in 11 of 1163 R papers (0.9%) — Generalized Random Forests.

Options (share of these 11 papers): `W.hat` 73%, `num.trees` 45%, `seed` 45%, `Y.hat` 36%, `X` 27%, `Y` 27%, `W` 27%, `min.node.size` 27%, `num.threads` 18%, `clusters` 18%.

Most common option set: `W`, `W.hat`, `X`, `Y`; at least one call in 1 paper (9%).

```r
c.forest <- causal_forest(X = x, Y =y, W = d, W.hat = pscore);
```
Econometrica 2025, [doi:10.3982/ecta19303](https://doi.org/10.3982/ecta19303), `code/zenodo_10871241/replication_package/replication_package/Code/figure3-CausalRF.R` line 125.

### `grf::regression_forest`

Used in 11 of 1163 R papers (0.9%) — Generalized Random Forests.

Options (share of these 11 papers): `X` 55%, `Y` 55%, `tune.parameters` 27%, `seed` 27%, `num.threads` 27%, `honesty` 18%, `min.node.size` 18%, `clusters` 18%, `equalize.cluster.weights` 18%.

Most common option set: none; at least one call in 2 papers (18%).

```r
  forest.Y <- regression_forest(X_pre, Y_pre)
```
ReStud 2026, [doi:10.1093/restud/rdag080](https://doi.org/10.1093/restud/rdag080), `code/zenodo_18849776/EUForest_Workspace/EUForest Workspace/analysis/8_grf.R` line 305.

Next most common option set: `X`, `Y`; at least one call in 2 papers (18%).

```r
  rf = regression_forest(X=x1, Y=y1)
```
JASA 2025, [doi:10.1080/01621459.2024.2356886](https://doi.org/10.1080/01621459.2024.2356886), `code/figshare_25860567/code_final_1_/code_final/simulated/scenario2_high.R` line 95.

### `ncvreg::cv.ncvreg`

Used in 10 of 1163 R papers (0.9%) — Regularization Paths for SCAD and MCP Penalized Regression Models.

Options (share of these 10 papers): `penalty` 100%, `family` 70%, `nfolds` 20%.

Most common option set: `family`, `penalty`; at least one call in 5 papers (50%).

```r
      cvreg.mod <- cv.ncvreg(X, Y, family = "gaussian", penalty = "SCAD")
```
JASA 2026, [doi:10.1080/01621459.2026.2681993](https://doi.org/10.1080/01621459.2026.2681993), `code/github_Anupreet-Porwal_DP-mix-block-g-prior/section6.2-simulation/02-run-methods.R` line 180.

Next most common option set: `penalty`; at least one call in 3 papers (30%).

```r
    fit0 = cv.ncvreg(X,Y,penalty = "lasso")
```
JRSSB 2026, [doi:10.1093/jrsssb/qkag110](https://doi.org/10.1093/jrsssb/qkag110), `code/github_SyChen94_RidgeInfer/source code/myDLassoncvreg.R` line 28.
