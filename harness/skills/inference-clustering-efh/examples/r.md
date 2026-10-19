# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `stats::vcov`

Used in 52 of 1163 R papers (4%) — Calculate Variance-Covariance Matrix for a Fitted Model Object.

Options (share of these 52 papers): `cluster` 6%, `method` 4%.

Most common option set: none; at least one call in 45 papers (87%).

```r
cov_matrix <- vcov(fm)
```
JASA 2025, [doi:10.1080/01621459.2025.2485357](https://doi.org/10.1080/01621459.2025.2485357), `code/figshare_28706779/reproducibility-scripts/reproducibility-scripts/0310-ols-distances.R` line 4; license file: MIT.

### `sandwich::vcovHC`

Used in 32 of 1163 R papers (3%) — Heteroscedasticity-Consistent Covariance Matrix Estimation.

Options (share of these 32 papers): `type` 91%.

Most common option set: `type`; at least one call in 28 papers (88%).

```r
robust_vcov <- function(model) vcovHC(model, type = "HC0")
```
ReStud 2026, [doi:10.1093/restud/rdag026](https://doi.org/10.1093/restud/rdag026), `code/zenodo_18825708/replication_package_submission/replication_package_submission/meta_analysis_replication.R` line 38; license file: CC-BY.

Next most common option set: none; at least one call in 7 papers (22%).

```r
forest.ate <- data.frame("aipw", paste0("Q", seq(num.rankings)), lmtest::coeftest(ols, vcov=sandwich::vcovHC(ols, "HC2"))[,1:2])
```
JASA 2025, [doi:10.1080/01621459.2024.2393466](https://doi.org/10.1080/01621459.2024.2393466), `code/github_som-shahlab_RATE-experiments/experiments/section_5_international_stroke_trial/analysis.Rmd` line 579; license file: GPL.

### `sandwich::NeweyWest`

Used in 16 of 1163 R papers (1%) — Newey-West HAC Covariance Matrix Estimation.

Options (share of these 16 papers): `lag` 62%, `prewhite` 56%, `adjust` 19%.

Most common option set: none; at least one call in 5 papers (31%).

```r
  NW = sqrt(diag(NeweyWest(consump1))))
```
Econometrica 2024, [doi:10.3982/ecta20417](https://doi.org/10.3982/ecta20417), `code/zenodo_10145562/SBA_Code/SBA_Code/renv/library/R-4.1/x86_64-w64-mingw32/AER/demo/Ch-Validation.R` line 245.

Next most common option set: `lag`, `prewhite`; at least one call in 5 papers (31%).

```r
    mod_robust = coeftest(mod, vcov. = NeweyWest(mod, lag = 1, prewhite = 0))
```
RFS 2025, [doi:10.1093/rfs/hhae081](https://doi.org/10.1093/rfs/hhae081), `code/dataverse_7PPQ1I/replication_package_codes_tables/table_11.R` line 80.

### `boot::boot`

Used in 13 of 1163 R papers (1%) — Bootstrap Resampling.

Options (share of these 13 papers): `R` 69%, `statistic` 46%, `data` 38%, `parallel` 23%, `ncpus` 15%.

Most common option set: none; at least one call in 4 papers (31%).

```r
boot.out = boot(Yvals,c_val,1000)
```
IJOC 2024, [doi:10.1287/ijoc.2022.0044](https://doi.org/10.1287/ijoc.2022.0044), `code/github_INFORMSJoC_2022.0044/scripts/DirectIUJackson_10ROAR.R` line 212; license file: MIT.

Next most common option set: `R`; at least one call in 3 papers (23%).

```r
bootreg <-boot(lab_binned, fn_boot, R=200)
```
ReStud 2025, [doi:10.1093/restud/rdae104](https://doi.org/10.1093/restud/rdae104), `code/zenodo_13742225/The_Child_Penalty_Atlas_-_Replication/The Child Penalty Atlas - Replication/Code/Figures/Scatter_Penalty_Regions_quadratic.R` line 223.

### `estimatr::lm_robust`

Used in 12 of 1163 R papers (1%) — Fast Estimators for Design-Based Inference.

Options (share of these 12 papers): `data` 100%, `se_type` 58%, `clusters` 50%, `cluster` 25%, `formula` 25%, `weights` 25%, `fixed_effects` 17%.

Most common option set: `clusters`, `data`, `se_type`; at least one call in 3 papers (25%).

```r
  model <- estimatr::lm_robust(formula,
                               data = data,
                               clusters = cluster,
                               se_type = "stata")
```
QJE 2024, [doi:10.1093/qje/qjad031](https://doi.org/10.1093/qje/qjad031), `code/dataverse_LHH29P/readi_evaluation_replication_run_regressions_R/generic_helper_functions.R` lines 493-496; license file: GPL.

Next most common option set: `data`; at least one call in 3 papers (25%).

```r
lm_robust(logY ~ y_pred_lsem + y_pred_bart, data = meps_test) %>% 
```
JASA 2025, [doi:10.1080/01621459.2025.2491155](https://doi.org/10.1080/01621459.2025.2491155), `code/figshare_29039267/BCMF-Paper/BCMF-Paper/CodeV1/CodeForSubmission/src/10_evaluate_models.R` line 84.

### `sandwich::vcovCL`

Used in 10 of 1163 R papers (0.9%) — Clustered Covariance Matrix Estimation.

Options (share of these 10 papers): `cluster` 100%, `type` 30%.

Most common option set: `cluster`; at least one call in 8 papers (80%).

```r
  cluster = vcovCL(lm, cluster = ~Year)
```
QJE 2026, [doi:10.1093/qje/qjaf054](https://doi.org/10.1093/qje/qjaf054), `code/dataverse_DQRO8L/AIKR_QJE_Replication-main/AIKR_QJE_Replication-main/final_analysis/Rscripts/marginal_predicted_figs.R` line 158.

Next most common option set: `cluster`, `type`; at least one call in 2 papers (20%).

```r
  vc <- vcovCL(model, cluster = cluster_vec, type = "HC3")
```
RFS 2026, [doi:10.1093/rfs/hhag034](https://doi.org/10.1093/rfs/hhag034), `code/dataverse_FPEQGK/replication-package_proud_not_own_stocks/replication-package_proud_not_own_stocks/replication/code/analysis/analyze_data_prolific.R` line 789.

### `multiwayvcov::cluster.vcov`

Used in 7 of 1163 R papers (0.6%) — Multi-Way Standard Error Clustering.

Options (share of these 7 papers): `cluster` 43%.

Most common option set: none; at least one call in 6 papers (86%).

```r
vcov_t2c6 <- cluster.vcov(lm_t2c6, dat_t2c6$address)
```
ReStud 2025, [doi:10.1093/restud/rdae041](https://doi.org/10.1093/restud/rdae041), `code/zenodo_10693520/code_final_submission/code_final_submission/empirical_application/2013-0442_data/Replication+Code_final.R` line 217.

Next most common option set: `cluster`; at least one call in 2 papers (29%).

```r
  coef <- coeftest(reg,  cluster.vcov(reg, cluster = data[[cluster]]))
```
AER 2021, [doi:10.1257/aer.20191777](https://doi.org/10.1257/aer.20191777), `code/Code/Utils/robustReg.R` line 130.

### `sandwich::sandwich`

Used in 7 of 1163 R papers (0.6%) — Making Sandwiches with Bread and Meat.

Options (share of these 7 papers): `meat` 57%, `meat.` 29%.

Most common option set: `meat`; at least one call in 4 papers (57%).

```r
  vcovCL <- dfc*sandwich(fm, meat=crossprod(u)/N)
```
ReStud 2024, [doi:10.1093/restud/rdae004](https://doi.org/10.1093/restud/rdae004), `code/zenodo_10104545/replication_package_JNS/replication_package_JNS/programs/02_analysis/FigA3_TabA4_code.R` line 72.

## Inference options of estimation commands

### `fixest::feols`

Used in 67 of 1163 R papers (6%) — Fixed-effects OLS estimation.

Inference options (share of these 67 papers): `cluster` 60%, `vcov` 22%, `se` 7%.

Most common option set: none; at least one call in 47 papers (70%).

```r
p_color <- feols(
  vote ~ exposure + hardship + god + manhood + duty + military + injustice + patriotism + camaraderie |
    sw0(birth_year + birth_state + vet + state^county),
  data = df
) |>
```
QJE 2026, [doi:10.1093/qje/qjaf046](https://doi.org/10.1093/qje/qjaf046), `code/dataverse_LSPICA/code/16_questionnaires.R` lines 102-106; license file: BSD.

Next most common option set: `cluster`; at least one call in 40 papers (60%).

```r
    feols(reg_fml, cluster = ~icpsr, data = dt)
```
QJE 2025, [doi:10.1093/qje/qjaf017](https://doi.org/10.1093/qje/qjaf017), `code/dataverse_R1PCY6/congress_immigration_replication/congress_immigration_replication/code/analysis/appendix/rollcall_cd_ancestry.R` line 206; license file: BSD.
