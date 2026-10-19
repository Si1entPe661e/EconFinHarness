# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `bootstrap`

Used in 115 of 1904 Stata papers (6%) — Bootstrap sampling and estimation.

Options (share of these 115 papers): `reps` 97%, `seed?` 59%, `cluster` 49% (`idcluster` 6%), `saving` 23%, `idcluster` 14%, `nodots` 11%, `nowarn` 9%, `strata` 9%, `nodrop` 8%, `level` 3%.

Most common option set: `reps`, `seed?`; at least one call in 21 papers (18%).

```stata
    bootstrap r(diff), seed(1848) reps(1000): pdiff 
```
RFS 2026, [doi:10.1093/rfs/hhae063](https://doi.org/10.1093/rfs/hhae063), `code/dataverse_8DUJZB/replication_code_LWWW/replication_final0403.do` line 82.

### `newey`

Used in 62 of 1904 Stata papers (3%) — Regression with Newey-West standard errors.

Options (share of these 62 papers): `lag` 100%, `force?` 16%, `noconstant` 5%.

Most common option set: `lag`; at least one call in 53 papers (85%).

```stata
newey pmf, lag(12)
```
ReStud 2024, [doi:10.1093/restud/rdad041](https://doi.org/10.1093/restud/rdad041), `code/zenodo_7617222/replication_package_v2/replication_package_v2/Replication_Package_for_Empirics/Table1/Table1_master.do` line 74; license file: MIT.

### `xtivreg2`

Used in 46 of 1904 Stata papers (2%) — module to perform extended IV/2SLS, GMM and AC/HAC, LIML and k-class regression for panel data models.

Options (share of these 46 papers): `fe` 98%, `cluster` 76%, `first` 35%, `i` 28%, `partial` 26%, `savefirst` 20%, `robust` 17%, `savefprefix` 13%, `cl` 11%, `ffirst` 11%.

Most common option set: `cluster`, `fe`; at least one call in 12 papers (26%).

```stata
	xtivreg2 f`i'.L0dy DSR_H_RoTW if xsample == 1,  fe cluster(id Year)
```
RFS 2026, [doi:10.1093/rfs/hhaf114](https://doi.org/10.1093/rfs/hhaf114), `code/dataverse_0Z5QUQ/RFS_Final_Zip/Do_Files/4_Tables.do` line 2715.

### `boottest`

Used in 31 of 1904 Stata papers (2%) — module to provide fast execution of the wild bootstrap with null imposed.

Options (share of these 31 papers): `seed` 52%, `reps` 48%, `nograph` 39%, `boottype` 35%, `cluster` 32%, `weight` 16%, `bootcluster` 13%, `nogr` 13%, `small` 13%, `level` 10%.

Most common option set: `boottype`; at least one call in 3 papers (10%).

```stata
    boottest HD_Mixed, boottype(wild)
```
JPE 2025, [doi:10.1086/736212](https://doi.org/10.1086/736212), `code/dataverse_DF8XXE/JPE_Replication_Code_Analysis/03 line_level_regressions.do` line 47.

### `xtscc`

Used in 21 of 1904 Stata papers (1%) — module to calculate robust standard errors for panels with cross-sectional dependence.

Options (share of these 21 papers): `fe` 57%, `lag` 52%.

Most common option set: none; at least one call in 9 papers (43%).

```stata
xtscc `vars' `FE'
```
ReStud 2026, [doi:10.1093/restud/rdaf055](https://doi.org/10.1093/restud/rdaf055), `code/zenodo_14288617/replication/replication/routines/A_Stata_regression.do` line 50.

Next most common option set: `fe`; at least one call in 7 papers (33%).

```stata
	xtscc `x'`h' `controls_LP' `controls_LP_US'  l(1/`nlags_shock').`mpshock' `mpshock', fe 	
```
ReStud 2025, [doi:10.1093/restud/rdaf109](https://doi.org/10.1093/restud/rdaf109), `code/zenodo_17642344/REPLICATION_PACKAGE_HANK_Devaluation_Oct2025/REPLICATION_PACKAGE_HANK_Devaluation_Oct2025/Local_Projections/Run_MP_quarterly_Replication.do` line 810.

### `serrbar`

Used in 13 of 1904 Stata papers (0.7%) — Graph standard error bar chart.

Options (share of these 13 papers): `xtitle` 85%, `xlabel` 77%, `ytitle` 77%, `scale` 69%, `legend` 46%, `mvopts` 46%, `ylabel` 46%, `yline` 38%, `addplot` 31%, `graphregion` 31% (`color` 31%).

Most common option set: ``options'?`, `scale`, `xlabel`, `xtitle`; at least one call in 1 paper (8%).

```stata
		serrbar `value' `stderr' `order' if `order'<=`max',  xlabel(none) xtitle(Variable) `options' scale(2)
```
AER 2019, [doi:10.1257/aer.20180609](https://doi.org/10.1257/aer.20180609), `code/data/datastore/Newspaper-Entry--Gentzkow-et-al-/data/20091316_data/external/plotcoeffs_nolab.ado` line 58.

### `qreg2`

Used in 11 of 1904 Stata papers (0.6%) — module to perform quantile regression with robust and clustered standard errors.

Options (share of these 11 papers): `cluster` 64%, `q` 36%, `quantile` 27%.

Most common option set: `cluster`; at least one call in 4 papers (36%).

```stata
qreg2 BF CV if $exp1, cluster(subject)
```
AER 2023, [doi:10.1257/aer.20191927](https://doi.org/10.1257/aer.20191927), `code/tables.do` line 24.

### `newey2`

Used in 6 of 1904 Stata papers (0.3%) — module to extend newey (HAC covariance estimation).

Options (share of these 6 papers): `lag` 100%, `force` 83%.

Most common option set: `force`, `lag`; at least one call in 5 papers (83%).

```stata
	newey2 failure p_LPM_4, lag(`L') force
```
QJE 2026, [doi:10.1093/qje/qjaf044](https://doi.org/10.1093/qje/qjaf044), `code/dataverse_Q22XR1/qje-repkit-to-upload/qje-repkit-to-upload/code/71_banks_at_risk.do` line 108.

Next most common option set: `lag`; at least one call in 3 papers (50%).

```stata
	newey2 delay_gm density_norm, lag(3)
```
Econometrica 2024, [doi:10.3982/ecta18422](https://doi.org/10.3982/ecta18422), `code/zenodo_10637043/replication_package_v7/replication-cp/code/analysis_reduced_form/Figure 4 road tech.do` line 35.

## Inference options of estimation commands

### `regress`

Used in 1431 of 1904 Stata papers (75%) — Linear regression.

Inference options (share of these 1431 papers): `robust` 40%, `cluster` 40%, `vce` 23% (`cluster` 17%, `robust` 6%).

Most common option set: none; at least one call in 1093 papers (76%).

```stata
reg `lhs' `rhs'
```
RFS 2026, [doi:10.1093/rfs/hhag032](https://doi.org/10.1093/rfs/hhag032), `code/dataverse_4DACEC/code_analysis/9_rsu_psu_magnitudes.do` line 103; license file: MIT.

Next most common option set: `robust`; at least one call in 532 papers (37%).

```stata
	reg testmay, robust
```
QJE 2025, [doi:10.1093/qje/qjaf015](https://doi.org/10.1093/qje/qjaf015), `code/dataverse_N7534Z/MPC2008-Public-main_descriptive_stats_code/schedule_table.do` line 83; license file: GPL.

### `reghdfe`

Used in 736 of 1904 Stata papers (39%) — Linear regression with multiple fixed effects. Also supports individual FEs with group-level outcomes.

Inference options (share of these 736 papers): `cluster` 60%, `vce` 54% (`cluster` 43%, `robust` 16%).

Most common option set: `cluster`; at least one call in 439 papers (60%).

```stata
	eststo m3 : reghdfe exports_g withdraw_times_post post, absorb(pair_FE partner_time_FE industry_time_FE) cluster(pair_FE)
```
RFS 2026, [doi:10.1093/rfs/hhag045](https://doi.org/10.1093/rfs/hhag045), `code/dataverse_2EVES4/1_code/4_3_did_bilateral_productlevel.do` line 60; license file: BSD.

Next most common option set: `vce`; at least one call in 394 papers (54%).

```stata
eststo reg_3: reghdfe `price_var' `holding_var', a(period gpcb_id) vce(cluster gpcb_id)
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_trading/make_elasticity_table_hetero.do` line 97; license file: BSD.

### `areg`

Used in 472 of 1904 Stata papers (25%) — Linear regression with many indicator.

Inference options (share of these 472 papers): `cluster` 52%, `robust` 21%, `vce` 21% (`cluster` 19%, `robust` 3%).

Most common option set: `cluster`; at least one call in 220 papers (47%).

```stata
areg lnxi `x' , a(ipcyear) cluster(ipc)
```
JFE 2026, [doi:10.1016/j.jfineco.2026.104276](https://doi.org/10.1016/j.jfineco.2026.104276), `code/mendeley_d322y5hbmx_v1/TBSL_Process_Replication/code_and_data/Table7.do` line 46.

Next most common option set: none; at least one call in 218 papers (46%).

```stata
areg fy, a(sector) 
```
Econometrica 2026, [doi:10.3982/ecta21849](https://doi.org/10.3982/ecta21849), `code/zenodo_17537119/ECMA_replication_to_submit/ECMA_replication_to_submit/codes/sector_firm_year_effs.do` line 33.

### `xtreg`

Used in 219 of 1904 Stata papers (12%) — Linear models for panel data.

Inference options (share of these 219 papers): `cluster` 44%, `vce` 26% (`cluster` 18%, `robust` 6%), `robust` 17%.

Most common option set: none; at least one call in 87 papers (40%).

```stata
xtreg   wagetemp c.exper c.age c.cum_2yr c.cum_4yr b1997.year i.in_2yr i.in_4yr i.in_grad_school i.workPT i.grad_2yr i.grad_4yr if wflg & female==1, fe
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_data-cleaning_nlsy97/wage_cleaning.do` line 76; license file: GPL.

Next most common option set: `cluster`; at least one call in 84 papers (38%).

```stata
			xi: xtreg `outcome' x1 x2 i.year z, cl(region) fe
```
ReStud 2026, [doi:10.1093/restud/rdaf080](https://doi.org/10.1093/restud/rdaf080), `code/zenodo_16614282/ReSTUD_MS_35738/ReSTUD MS 35738/Code/Analysis/reduced_form_analysis.do` line 1344.

### `ivreghdfe`

Used in 184 of 1904 Stata papers (10%) — Extended instrumental variable regressions with multiple levels of fixed effects.

Inference options (share of these 184 papers): `cluster` 73%, `vce` 10%, `robust` 8%, `dkraay` 2%.

Most common option set: `cluster`; at least one call in 134 papers (73%).

```stata
capture: ivreghdfe `y' (`d' = `z') `x', cluster(`cluster') 
```
ReStud 2026, [doi:10.1093/restud/rdag029](https://doi.org/10.1093/restud/rdag029), `code/zenodo_17503831/clean_archive/applications/src/cleaning/clean_bloom.do` line 37.

Next most common option set: none; at least one call in 61 papers (33%).

```stata
	ivreghdfe `y' $r2 , $ops
```
QJE 2026, [doi:10.1093/qje/qjag040](https://doi.org/10.1093/qje/qjag040), `code/dataverse_QUMRNN/Noncompete-Experiment-Replication/Noncompete-Experiment-Replication/JointCode/earnings_experiment_het.do` line 23.

### `logit`

Used in 150 of 1904 Stata papers (8%) — Logistic regression, reporting.

Inference options (share of these 150 papers): `cluster` 20%, `vce` 19% (`cluster` 13%, `robust` 3%), `robust` 10%.

Most common option set: none; at least one call in 98 papers (65%).

```stata
			logit S Z_* X_* ZX_*
```
AER 2021, [doi:10.1257/aer.20190221](https://doi.org/10.1257/aer.20190221), `code/code/analysis/master.do` line 425; license file: GPL.

Next most common option set: `vce`; at least one call in 28 papers (19%).

```stata
	logit depvar `indepvar' `controls' i.`specs_panelvar', vce(cluster `specs_panelvar')
```
ReStud 2026, [doi:10.1093/restud/rdag044](https://doi.org/10.1093/restud/rdag044), `code/zenodo_19036252/LooseMP/LooseMP/code/analysis/FigureA10.do` line 52.

### `probit`

Used in 150 of 1904 Stata papers (8%) — Probit regression.

Inference options (share of these 150 papers): `cluster` 25%, `vce` 24% (`cluster` 20%, `robust` 3%), `robust` 9%.

Most common option set: none; at least one call in 87 papers (58%).

```stata
quietly probit crisis3y bank_debt
```
JPE 2025, [doi:10.1086/733423](https://doi.org/10.1086/733423), `code/dataverse_TIL7KK/Main_Step3.do` line 16; license file: BSD.

Next most common option set: `vce`; at least one call in 36 papers (24%).

```stata
	probit removed jscore $cfe ,  vce( cluster $clusterop )
```
ReStud 2026, [doi:10.1093/restud/rdaf044](https://doi.org/10.1093/restud/rdaf044), `code/zenodo_14293584/helensdotter_replication/analysis/code/analysis.do` line 3128.
