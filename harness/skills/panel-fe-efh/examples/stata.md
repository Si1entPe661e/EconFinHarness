# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `reghdfe`

Used in 736 of 1904 Stata papers (39%) — Linear regression with multiple fixed effects. Also supports individual FEs with group-level outcomes.

Options (share of these 736 papers): `absorb` 98%, `cluster` 60%, `vce` 54% (`cluster` 43%, `robust` 16%), `residuals` 24%, `noabsorb?` 13%, `noconstant` 10%, `keepsingletons` 5%, `old?` 2%, `tolerance` 2%, `compile?` 1%.

Most common option set: `absorb`, `cluster`; at least one call in 410 papers (56%).

```stata
reghdfe pchdadjshrout pchdadjshrpass,a($fe) cluster(permno yq)
```
RFS 2026, [doi:10.1093/rfs/hhag032](https://doi.org/10.1093/rfs/hhag032), `code/dataverse_4DACEC/code_analysis/5_iv_baseline.do` line 116; license file: MIT.

Next most common option set: `absorb`, `vce`; at least one call in 359 papers (49%).

```stata
	reghdfe `var' treat_post productivity_cd2 ///
	ln_totalassets b_equitytotalassets ///
	b_roa b_netloansdepst b_loangrowth ipol*, ///
    absorb(bvd_id year country_num#year industry_num#year) ///
	vce(cluster city_num) 
```
RFS 2026, [doi:10.1093/rfs/hhag045](https://doi.org/10.1093/rfs/hhag045), `code/dataverse_2EVES4/1_code/4_2_did_citylevel_treatment.do` lines 495-499; license file: BSD.

### `xtset`

Used in 672 of 1904 Stata papers (35%) — Declare data to be panel data.

Options (share of these 672 papers): `clear` 5%, `yearly` 4%, `delta` 4%, `quarterly` 2%, `monthly` 2%, `weekly` 0.3%.

Most common option set: none; at least one call in 641 papers (95%).

```stata
    xtset uID t
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_sim-results/cfl.do` line 147; license file: GPL.

### `xtreg`

Used in 219 of 1904 Stata papers (12%) — Linear models for panel data.

Options (share of these 219 papers): `fe` 94%, `cluster` 44%, `vce` 26% (`cluster` 18%, `robust` 6%), `i?` 18%, `robust` 17%, `re` 5%, `nonest?` 4%.

Most common option set: `cluster`, `fe`; at least one call in 68 papers (31%).

```stata
			xi: xtreg `outcome' x1 x2 i.year z, cl(region) fe
```
ReStud 2026, [doi:10.1093/restud/rdaf080](https://doi.org/10.1093/restud/rdaf080), `code/zenodo_16614282/ReSTUD_MS_35738/ReSTUD MS 35738/Code/Analysis/reduced_form_analysis.do` line 1344.

Next most common option set: `fe`; at least one call in 58 papers (26%).

```stata
xtreg `price_var' `holding_var', fe
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_trading/make_elasticity_table_hetero.do` line 107; license file: BSD.

### `ivreghdfe`

Used in 184 of 1904 Stata papers (10%) — Extended instrumental variable regressions with multiple levels of fixed effects.

Options (share of these 184 papers): `cluster` 73%, `absorb` 66%, `a` 27%, `first` 25%, `savefirst` 11%, `cl` 11%, `ffirst` 10%, `vce` 10%, `robust` 8%, `abs` 7%.

Most common option set: `absorb`, `cluster`; at least one call in 77 papers (42%).

```stata
		 ivreghdfe  `depvar'   onemonth twomonth threemonth lag1rbtindicator `controlvars'  if insample `rebatesample' [weight=finlwt21], cluster(cuid) absorb(`absorbvars')  
```
QJE 2025, [doi:10.1093/qje/qjaf015](https://doi.org/10.1093/qje/qjaf015), `code/dataverse_N7534Z/MPC2008-Public-main_psmjregressions_code/table2_schedule_interaction.do` line 105; license file: GPL.

### `ppmlhdfe`

Used in 63 of 1904 Stata papers (3%) — module for Poisson pseudo-likelihood regression with multiple levels of fixed effects.

Options (share of these 63 papers): `absorb` 78%, `cluster` 52%, `vce` 43%, `a` 25%, `d` 22%, `cl` 10%, `nocons` 5%, `abs` 5%, `noconstant` 5%, `noabsorb` 5%.

Most common option set: `absorb`, `cluster`; at least one call in 23 papers (37%).

```stata
ppmlhdfe returns logdistance   if fromstate != tostate & year==2004, cluster(tostate fromstate) absorb(tostate fromstate)
```
ReStud 2026, [doi:10.1093/restud/rdag049](https://doi.org/10.1093/restud/rdag049), `code/zenodo_19240923/Restud_Replication_Package/Restud Replication Package/code/exhibits/gravity_table.do` line 31.

Next most common option set: `absorb`, `vce`; at least one call in 15 papers (24%).

```stata
ppmlhdfe X_ij x_temp, absorb(fe_i_ppml=i fe_j_ppml=j) vce(cluster i j)
```
Econometrica 2026, [doi:10.3982/ecta19350](https://doi.org/10.3982/ecta19350), `code/zenodo_17841577/DT_zenodo/LODES_gravity_analysis/code/compare_gravity_estimators_time_impute.do` line 34.

### `xtivreg2`

Used in 46 of 1904 Stata papers (2%) — module to perform extended IV/2SLS, GMM and AC/HAC, LIML and k-class regression for panel data models.

Options (share of these 46 papers): `fe` 98%, `cluster` 76%, `first` 35%, `i` 28%, `partial` 26%, `savefirst` 20%, `robust` 17%, `savefprefix` 13%, `ffirst` 11%, `cl` 11%.

Most common option set: `cluster`, `fe`; at least one call in 12 papers (26%).

```stata
	xtivreg2 f`i'.L0dy DSR_H_RoTW if xsample == 1,  fe cluster(id Year)
```
RFS 2026, [doi:10.1093/rfs/hhaf114](https://doi.org/10.1093/rfs/hhaf114), `code/dataverse_0Z5QUQ/RFS_Final_Zip/Do_Files/4_Tables.do` line 2715.

### `clogit`

Used in 28 of 1904 Stata papers (1%) — Conditional (fixed-effects) logistic.

Options (share of these 28 papers): `group` 100%, `cluster` 29%, `vce` 18% (`cluster` 18%), `robust` 7%, `nonest` 7%, `constraints` 7%, `or` 7%.

Most common option set: `group`; at least one call in 13 papers (46%).

```stata
clogit chosen x* z,group(ID)
```
JPE 2026, [doi:10.1086/740223](https://doi.org/10.1086/740223), `code/dataverse_JCXVD9/Expedia_flexible_logit_epsiloninthebox_programs/flexiblelogit_bootstrap.do` line 22.

Next most common option set: `cluster`, `group`; at least one call in 7 papers (25%).

```stata
eststo: clogit buy_shares_dummy ar1_std_lag12 lag_12mnth_all_ws  $control_purch [pw=weight], group(pnr_day) cluster(pnr)  
```
JFE 2026, [doi:10.1016/j.jfineco.2026.104291](https://doi.org/10.1016/j.jfineco.2026.104291), `code/mendeley_vzptvmwm9s_v2/JFEreplication/JFE_10_Analysis.do` line 922.

### `xtivreg`

Used in 18 of 1904 Stata papers (0.9%) — Instrumental variables and two-stage least squares for panel-data models.

Options (share of these 18 papers): `fe` 94%, `vce` 67% (`cluster` 61%), `first` 22%, `i?` 17%.

Most common option set: `fe`, `vce`; at least one call in 10 papers (56%).

```stata
		xtivreg gsmall_dep1  i.year (gSmallFirm1 = bartikGS1), fe vce(cluster state)
```
RFS 2025, [doi:10.1093/rfs/hhaf042](https://doi.org/10.1093/rfs/hhaf042), `code/dataverse_WI5FZ3/GSS_3digit.do` line 20.

Next most common option set: `fe`; at least one call in 4 papers (22%).

```stata
	eststo: xtivreg `x' midline endline (loanuse comploanuse = interpost inter4post), fe
```
AER 2024, [doi:10.1257/aer.20220711](https://doi.org/10.1257/aer.20220711), `code/Data-and-Do-file/loan_main.do` line 1013.
