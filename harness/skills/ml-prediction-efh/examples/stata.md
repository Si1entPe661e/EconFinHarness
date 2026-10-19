# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `lasso`

Used in 13 of 1904 Stata papers (0.7%) — Lasso for prediction and model selection.

Options (share of these 13 papers): `rseed` 31%, `selection` 23% (`adaptive` 15%), `nolog?` 15%.

Most common option set: none; at least one call in 6 papers (46%).

```stata
  lasso linear $pred_drug_var $std_lasso_vars
```
ReStud 2025, [doi:10.1093/restud/rdae079](https://doi.org/10.1093/restud/rdae079), `code/zenodo_10909964/Replication_package/Replication package/Data cleaning and processing/GR - Drug_predict.do` line 272.

Next most common option set: `rseed`, `selection`; at least one call in 2 papers (15%).

```stata
	lasso linear ln_pagerank_f fe_f cl_*, selection(adaptive) rseed(1234)
```
QJE 2025, [doi:10.1093/qje/qjaf024](https://doi.org/10.1093/qje/qjaf024), `code/dataverse_MDUW8B/REPLICATION_PACKAGE_codes/c04_Create_amenities_classification_separate.do` line 124.

### `lassocoef`

Used in 8 of 1904 Stata papers (0.4%) — Display coefficients after lasso estimation results.

Options (share of these 8 papers): `display` 62%, `sort` 25%.

Most common option set: none; at least one call in 3 papers (38%).

```stata
lassocoef
```
ReStud 2026, [doi:10.1093/restud/rdag027](https://doi.org/10.1093/restud/rdag027), `code/zenodo_17361408/BFFPT_RESTUD_replication/code/1c_lasso_tablea1_tablea2_tableb8.do` line 384.

Next most common option set: `display`; at least one call in 3 papers (38%).

```stata
	lassocoef, display(coef, penalized)
```
ReStud 2026, [doi:10.1093/restud/rdaf071](https://doi.org/10.1093/restud/rdaf071), `code/zenodo_16539681/Replication/Replication/code/do/2_analysis/appendix/tableA15.do` line 364.

### `dsregress`

Used in 6 of 1904 Stata papers (0.3%) — Double-selection lasso linear regression.

Options (share of these 6 papers): `controls` 100%, `vce` 83% (`cluster` 50%, `robust` 33%), `selection` 33%.

Most common option set: `controls`, `vce`; at least one call in 3 papers (50%).

```stata
		dsregress `outcome' treatment, ///
					 controls((i.strata `addon') $consideration) ///
					 vce(cluster employee_id)
```
QJE 2025, [doi:10.1093/qje/qjae039](https://doi.org/10.1093/qje/qjae039), `code/dataverse_9MRZEA/Replication_code_admin_function/function_admin__functions.do` lines 264-266.

Next most common option set: `controls`; at least one call in 1 paper (17%).

```stata
quietly dsregress app_after  High_f  if Treated_firm==0 & survey=="E1", controls($Blasso)
```
ReStud 2025, [doi:10.1093/restud/rdae094](https://doi.org/10.1093/restud/rdae094), `code/zenodo_13153322/RR_CIV_2024_107/Reproducibility package/Paper 2nd follow-up/Sub-dofiles/Tables and Graphs/Outputs Restud paper.do` line 4556.

### `rforest`

Used in 5 of 1904 Stata papers (0.3%) — module to implement Random Forest algorithm.

Options (share of these 5 papers): `type` 100%, `iter` 40%, `iterations` 40%, `numvars` 40%, `seed` 40%.

Most common option set: `iter`, `numvars`, `type`; at least one call in 1 paper (20%).

```stata
		cap: rforest qw $controls if qw!=., type(reg) iter(`i') numvars(`numvars')
```
AER 2025, [doi:10.1257/aer.20230393](https://doi.org/10.1257/aer.20230393), `code/Replication_package/Dofiles/7_analysis_experiment3.do` line 50.

Next most common option set: `iter`, `seed`, `type`; at least one call in 1 paper (20%).

```stata
qui rforest removed $controls cfe_* , type(reg) iter(500) seed(252164)
```
ReStud 2026, [doi:10.1093/restud/rdaf044](https://doi.org/10.1093/restud/rdaf044), `code/zenodo_14293584/helensdotter_replication/analysis/code/compliers.do` line 42.
