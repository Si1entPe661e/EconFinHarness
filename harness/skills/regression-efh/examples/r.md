# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `stats::lm`

Used in 395 of 1163 R papers (34%) — Fitting Linear Models.

Options (share of these 395 papers): `data` 58%, `weights` 13%, `formula` 4%, `na.action` 4%, `subset` 3%, `weight` 1%, `x` 1%, `w` 0.8%, `y` 0.8%.

Most common option set: none; at least one call in 240 papers (61%).

```r
    summary(lm(m~0+X))$coefficients[,'Estimate']
```
JASA 2026, [doi:10.1080/01621459.2025.2529602](https://doi.org/10.1080/01621459.2025.2529602), `code/github_chenxuan-he_GoFHD2/real_data/real_data_cortisol/utils_mediation.R` line 232; license file: MIT.

Next most common option set: `data`; at least one call in 208 papers (53%).

```r
    model <- lm(formula, data = data, ...)
```
JASA 2026, [doi:10.1080/01621459.2026.2661377](https://doi.org/10.1080/01621459.2026.2661377), `code/figshare_32125854/reproducibility_repo/seqdx_jasa_repo-public/seqdx/R/recurstep.R` line 23; license file: GPL.

### `stats::glm`

Used in 143 of 1163 R papers (12%) — Fitting Generalized Linear Models.

Options (share of these 143 papers): `family` 97%, `data` 67%, `weights` 14%, `formula` 6%, `control` 4%, `offset` 4%, `subset` 3%, `na.action` 3%, `x` 3%, `y` 3%.

Most common option set: `data`, `family`; at least one call in 86 papers (60%).

```r
    logistic <- glm(y ~ ., family = "binomial",
                    data = data.frame(y = factor(y_train), x = x_train))
```
JRSSB 2026, [doi:10.1093/jrsssb/qkag037](https://doi.org/10.1093/jrsssb/qkag037), `code/github_HaoyuGeng_ART/real-data/mnist/changeAUC/get_change_point_v1.R` lines 36-37; license file: GPL.

Next most common option set: `family`; at least one call in 51 papers (36%).

```r
  summary(glm(x ~ z, family = Gamma()))$coef[2, 4]
```
JASA 2025, [doi:10.1080/01621459.2024.2353948](https://doi.org/10.1080/01621459.2024.2353948), `code/github_ananyaroy97_Generalized-Data-Thinning-Using-Sufficient-Statistics/utilities_estimate.R` line 52; license file: MIT.

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

Options (share of these 90 papers): `lambda` 84%, `family` 62%, `alpha` 59%, `intercept` 48%, `x` 37%, `y` 37%, `standardize` 31%, `penalty.factor` 26%, `nlambda` 6%, `weights` 6%.

Most common option set: `alpha`, `lambda`; at least one call in 11 papers (12%).

```r
  beta1 <- as.vector(glmnet(X_matrix1, Y1, alpha = 1, lambda = lambda)$beta)
```
JASA 2026, [doi:10.1080/01621459.2025.2519814](https://doi.org/10.1080/01621459.2025.2519814), `code/figshare_29473607/OnlineSupplements2/OnlineSupplements/Code/Rmarkdown/Real_data/Supermarket.Rmd` line 54.

### `fixest::feols`

Used in 67 of 1163 R papers (6%) — Fixed-effects OLS estimation.

Options (share of these 67 papers): `data` 94%, `cluster` 60%, `weights` 24%, `vcov` 22%, `panel.id` 12%, `fml` 10%, `lean` 7%, `se` 7%, `warn` 7%, `split` 6%.

Most common option set: `data`; at least one call in 32 papers (48%).

```r
p_color <- feols(
  vote ~ exposure + hardship + god + manhood + duty + military + injustice + patriotism + camaraderie |
    sw0(birth_year + birth_state + vet + state^county),
  data = df
) |>
```
QJE 2026, [doi:10.1093/qje/qjaf046](https://doi.org/10.1093/qje/qjaf046), `code/dataverse_LSPICA/code/16_questionnaires.R` lines 102-106; license file: BSD.

Next most common option set: `cluster`, `data`; at least one call in 29 papers (43%).

```r
    feols(reg_fml, cluster = ~icpsr, data = dt)
```
QJE 2025, [doi:10.1093/qje/qjaf017](https://doi.org/10.1093/qje/qjaf017), `code/dataverse_R1PCY6/congress_immigration_replication/congress_immigration_replication/code/analysis/appendix/rollcall_cd_ancestry.R` line 206; license file: BSD.

### `stats::rpois`

Used in 56 of 1163 R papers (5%) — The Poisson Distribution.

Options (share of these 56 papers): `lambda` 29%, `n` 5%.

Most common option set: none; at least one call in 41 papers (73%).

```r
      Y[i]=rpois(1,Y_phat[i])
```
IJOC 2026, [doi:10.1287/ijoc.2024.0946](https://doi.org/10.1287/ijoc.2024.0946), `code/github_INFORMSJoC_2024.0946/src/Example 2.R` line 186; license file: MIT.

Next most common option set: `lambda`; at least one call in 13 papers (23%).

```r
  Cxi=rpois(1,lambda = A)
```
JASA 2026, [doi:10.1080/01621459.2025.2552513](https://doi.org/10.1080/01621459.2025.2552513), `code/figshare_30066932/R_code_0331/R code_0331/Simulation/Unbalanced/unbalanced_p=10.R` line 977.

### `lmtest::coeftest`

Used in 47 of 1163 R papers (4%) — Inference for Estimated Coefficients.

Options (share of these 47 papers): `vcov` 66%, `vcov.` 21%, `cluster` 9%, `lag` 4%.

Most common option set: `vcov`; at least one call in 27 papers (57%).

```r
      broom::tidy(lmtest::coeftest(model, vcov = nw_vcov))
```
ReStud 2026, [doi:10.1093/restud/rdag085](https://doi.org/10.1093/restud/rdag085), `code/zenodo_20598953/ReplicationPackageRestud_v2/ReplicationPackageRestud/code/table1.R` line 74; license file: MIT.

Next most common option set: none; at least one call in 15 papers (32%).

```r
        results = unclass(coeftest(regs[[i]]))
```
JPE 2025, [doi:10.1086/733423](https://doi.org/10.1086/733423), `code/dataverse_TIL7KK/Model/loading_package_and_functions.R` line 85; license file: BSD.

### `plm::plm`

Used in 15 of 1163 R papers (1%) — Linear Models for Panel Data.

Options (share of these 15 papers): `model` 100%, `data` 87%, `index` 67%, `effect` 33%.

Most common option set: `data`, `index`, `model`; at least one call in 7 papers (47%).

```r
  "(1)" = plm(formula_no_int,   data = panel,
              index = c("Country", "date"), model = "within"),
```
QJE 2026, [doi:10.1093/qje/qjag025](https://doi.org/10.1093/qje/qjag025), `code/dataverse_JG5NTA/replication_package/replication_package/data/01_tables.R` lines 79-80.
