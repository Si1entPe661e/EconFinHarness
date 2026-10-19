# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `lfe::felm`

Used in 84 of 1163 R papers (7%) — Linear Group Fixed Effects.

Options (share of these 84 papers): `data` 86%, `weights` 23%, `formula` 7%, `na.action` 4%, `exactDOF` 2%, `cmethod` 2%, `keepModel` 2%.

Most common option set: `data`; at least one call in 58 papers (69%).

```r
      mod <- felm(log_EBITD ~ winner + TFP, data = reg_data)
```
AER 2022, [doi:10.1257/aer.20190790](https://doi.org/10.1257/aer.20190790), `code/AER_replication_kit/2_MicrodataEstimation/LMS_auctions.R` line 111; license file: MIT.

Next most common option set: none; at least one call in 24 papers (29%).

```r
  tryCatch(felm(formula, data), error = function(e) NULL)
```
RFS 2026, [doi:10.1093/rfs/hhag063](https://doi.org/10.1093/rfs/hhag063), `code/dataverse_88JIH6/Replication package/Replication package/code/04_stock_market/stock_market_industry.R` line 16.

### `fixest::feols`

Used in 67 of 1163 R papers (6%) — Fixed-effects OLS estimation.

Options (share of these 67 papers): `data` 94%, `cluster` 60%, `weights` 24%, `vcov` 22%, `panel.id` 12%, `fml` 10%, `warn` 7%, `se` 7%, `lean` 7%, `weight` 6%.

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

### `fixest::i`

Used in 20 of 1163 R papers (2%) — Create, or interact variables with, factors.

Options (share of these 20 papers): `ref` 85%, `keep` 15%.

Most common option set: `ref`; at least one call in 15 papers (75%).

```r
raw.twfe = feols(greenness ~ i(D, ref = 0) | uniqueid + cddaid + year, 
```
ReStud 2026, [doi:10.1093/restud/rdag080](https://doi.org/10.1093/restud/rdag080), `code/zenodo_18849776/EUForest_Workspace/EUForest Workspace/analysis/10_Robustness.r` line 262.

Next most common option set: none; at least one call in 8 papers (40%).

```r
  summary(feols(upd ~ i(es_ind, trt, -6) | 
```
ReStud 2026, [doi:10.1093/restud/rdag012](https://doi.org/10.1093/restud/rdag012), `code/zenodo_16054543/movers_rep_no_conf_data/movers_rep_no_conf_data/Code/es_est_and_fig.R` line 48.

### `plm::plm`

Used in 15 of 1163 R papers (1%) — Linear Models for Panel Data.

Options (share of these 15 papers): `model` 100%, `data` 87%, `index` 67%, `effect` 33%.

Most common option set: `data`, `index`, `model`; at least one call in 7 papers (47%).

```r
  "(1)" = plm(formula_no_int,   data = panel,
              index = c("Country", "date"), model = "within"),
```
QJE 2026, [doi:10.1093/qje/qjag025](https://doi.org/10.1093/qje/qjag025), `code/dataverse_JG5NTA/replication_package/replication_package/data/01_tables.R` lines 79-80.

### `fixest::feglm`

Used in 13 of 1163 R papers (1%) — Fixed-effects GLM estimations.

Options (share of these 13 papers): `family` 100%, `data` 77%, `vcov` 38%, `glm.iter` 23%, `cluster` 15%, `lean` 15%.

Most common option set: `data`, `family`; at least one call in 6 papers (46%).

```r
    est_gravity_PPML = fixest::feglm(total_value_minus_nlink ~ 0 | 
                                 type.sender.year + type.receiver.year + type.sender.receiver, 
                                 family="poisson",
                                 data = df_type_pair_year)
```
ReStud 2026, [doi:10.1093/restud/rdaf080](https://doi.org/10.1093/restud/rdaf080), `code/zenodo_16614282/ReSTUD_MS_35738/ReSTUD MS 35738/Code/Analysis/model/Ukraine_simulation_functions.R` lines 71-74.

Next most common option set: `data`, `family`, `vcov`; at least one call in 2 papers (15%).

```r
c5<-feglm(us_share~treated_dummy:post|cohort_firm+cohort_time,vcov=~CN_firm_factsetid + year,
          family = "poisson",data=combined_dt2)
```
JFE 2026, [doi:10.1016/j.jfineco.2025.104192](https://doi.org/10.1016/j.jfineco.2025.104192), `code/mendeley_sw4y26xcd4_v2/c2_Figure4_china_supply_chain.R` lines 146-147.

### `fixest::fitstat`

Used in 12 of 1163 R papers (1%) — Computes fit statistics of fixest objects.

Options (share of these 12 papers): `simplify` 17%, `type` 17%.

Most common option set: none; at least one call in 9 papers (75%).

```r
      fitstat(., ~ f)    
```
ReStud 2026, [doi:10.1093/restud/rdaf026](https://doi.org/10.1093/restud/rdaf026), `code/zenodo_14976627/camps_replicationpackage/camps_replicationpackage/code/analysis/analysis.Rmd` line 2726.

Next most common option set: `simplify`; at least one call in 2 papers (17%).

```r
        dvm = fitstat(mod, "my", simplify = T)
```
AER 2025, [doi:10.1257/aer.20230328](https://doi.org/10.1257/aer.20230328), `code/code/utils.R` line 80.

### `fixest::fixef`

Used in 9 of 1163 R papers (0.8%) — Functions exported from list("nlme") to implement list("fixest") methods.

Most common option set: none; at least one call in 7 papers (78%).

```r
df = data.frame(fixef(m_iv1_fe)$njtc)
```
JPE 2026, [doi:10.1086/739325](https://doi.org/10.1086/739325), `code/dataverse_RY2CVR/code_2_estimation/12_demand_estimation.R` line 33.

### `fixest::setFixest_dict`

Used in 9 of 1163 R papers (0.8%) — Sets/gets the dictionary relabeling the variables.

Options (share of these 9 papers): `dict` 22%.

Most common option set: none; at least one call in 7 papers (78%).

```r
setFixest_dict(dict)
```
ReStud 2026, [doi:10.1093/restud/rdag060](https://doi.org/10.1093/restud/rdag060), `code/zenodo_20048287/MS33226-ReplicationPackage/MS33226-ReplicationPackage/src/data_analysis/library.R` line 107.

Next most common option set: `dict`; at least one call in 2 papers (22%).

```r
setFixest_dict(
  dict = c(foreign.born.std = "MC Foreign Born (Standardized)", 
           parents.foreign.born.std = "Parents Foreign Born (Standardized)", 
           gparents.foreign.born.std = "Grandparents Foreign Born (Standardized)", 
           imm.index.std = "Immigration Index (Standardized)",
           fb_pop.std = "Foreign Born Population \\\\ in Congressional District \\\\ (Standardized)",
           democrat.std = "Democrat (Standardized)"))
```
QJE 2025, [doi:10.1093/qje/qjaf017](https://doi.org/10.1093/qje/qjaf017), `code/dataverse_R1PCY6/congress_immigration_replication/congress_immigration_replication/code/analysis/speech_main.R` lines 63-69; license file: BSD.
