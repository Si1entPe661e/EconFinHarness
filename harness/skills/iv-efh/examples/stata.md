# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `ivreghdfe`

Used in 184 of 1904 Stata papers (10%) — Extended instrumental variable regressions with multiple levels of fixed effects.

Options (share of these 184 papers): `cluster` 73%, `absorb` 66%, `a` 27%, `first` 25%, `savefirst` 11%, `cl` 11%, `ffirst` 10%, `vce` 10%, `robust` 8%, `abs` 7%.

Most common option set: `absorb`, `cluster`; at least one call in 77 papers (42%).

```stata
		 ivreghdfe  `depvar'   onemonth twomonth threemonth lag1rbtindicator `controlvars'  if insample `rebatesample' [weight=finlwt21], cluster(cuid) absorb(`absorbvars')  
```
QJE 2025, [doi:10.1093/qje/qjaf015](https://doi.org/10.1093/qje/qjaf015), `code/dataverse_N7534Z/MPC2008-Public-main_psmjregressions_code/table2_schedule_interaction.do` line 105; license file: GPL.

### `ivregress`

Used in 126 of 1904 Stata papers (7%) — Single-equation instrumental-variables regression.

Options (share of these 126 papers): `cluster` 43%, `robust` 31%, `vce` 26% (`cluster` 19%, `robust` 5%, `hac` 2%), `first` 23%, `noconstant` 6%, `small` 3%, `wmatrix` 3% (`hac` 2%).

Most common option set: none; at least one call in 40 papers (32%).

```stata
			ivregress 2sls separation (`outcomevar'=Z_`outcomevar')
```
Econometrica 2026, [doi:10.3982/ecta21849](https://doi.org/10.3982/ecta21849), `code/zenodo_17537119/ECMA_replication_to_submit/ECMA_replication_to_submit/codes/separation_split_sample.do` line 58.

Next most common option set: `cluster`; at least one call in 38 papers (30%).

```stata
quietly ivregress 2sls D.sdo_total_cc (D.treatment = meses_desde_cambio_cc) i.num_subidas i.num_bajadas i.fecha [pw = probab] , cluster(id_cns) 		
```
ReStud 2026, [doi:10.1093/restud/rdaf079](https://doi.org/10.1093/restud/rdaf079), `code/zenodo_15569936/cardspaper-zenodo/cardspaper-zenodo/02_appendix/01_code/TableOA14.do` line 136.

### `xtivreg2`

Used in 46 of 1904 Stata papers (2%) — module to perform extended IV/2SLS, GMM and AC/HAC, LIML and k-class regression for panel data models.

Options (share of these 46 papers): `fe` 98%, `cluster` 76%, `first` 35%, `i` 28%, `partial` 26%, `savefirst` 20%, `robust` 17%, `savefprefix` 13%, `cl` 11%, `ffirst` 11%.

Most common option set: `cluster`, `fe`; at least one call in 12 papers (26%).

```stata
	xtivreg2 f`i'.L0dy DSR_H_RoTW if xsample == 1,  fe cluster(id Year)
```
RFS 2026, [doi:10.1093/rfs/hhaf114](https://doi.org/10.1093/rfs/hhaf114), `code/dataverse_0Z5QUQ/RFS_Final_Zip/Do_Files/4_Tables.do` line 2715.

### `pdslasso`

Used in 23 of 1904 Stata papers (1%) — module for post-selection and post-regularization OLS or IV estimation and inference.

Options (share of these 23 papers): `cluster` 70%, `partial` 52%, `fe` 17%, `robust` 17%, `cl` 13%, `lopt` 13%, `pnotpen` 13%, `aset` 9%, `post` 9%, `rob` 9%.

Most common option set: `cluster`, `partial`; at least one call in 4 papers (17%).

```stata
pdslasso `depvar' `reg' (`pdsvars1' $controls_partial_resp) if `sample', partial($controls_partial_resp) cluster(id)
```
Econometrica 2026, [doi:10.3982/ecta21926](https://doi.org/10.3982/ecta21926), `code/zenodo_18969189/NCDs_2018/NCDs 2018/Replication/do-files/Analysis do-files/Final analysis do-files/graphs_pres_paper_v38.do` line 1764.

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

### `weakiv`

Used in 12 of 1904 Stata papers (0.6%) — module to perform weak-instrument-robust tests and confidence intervals for instrumental-variable (IV) estimation of linear, probit and tobit models.

Options (share of these 12 papers): `cluster` 17%, `estadd` 17%, `level` 17%, `md` 17%, `partial` 17%, `robust` 17%.

Most common option set: none; at least one call in 5 papers (42%).

```stata
	weakiv
```
ReStud 2026, [doi:10.1093/restud/rdaf044](https://doi.org/10.1093/restud/rdaf044), `code/zenodo_14293584/helensdotter_replication/analysis/code/analysis.do` line 789.

Next most common option set: `cluster`; at least one call in 2 papers (17%).

```stata
		weakiv ivreg2 ln_imr_pub `baseline_controls'  (tot_pay_`treat_type'_adj=instrument) _I*  [aw = births_pub], ///
		cluster(fips)
```
AER 2024, [doi:10.1257/aer.20230008](https://doi.org/10.1257/aer.20230008), `code/duke-replication/analysis/scripts/code/6.13_online_appendix_j_iv.do` lines 408-409.

### `weakivtest`

Used in 12 of 1904 Stata papers (0.6%) — module to perform weak instrument test for a single endogenous regressor in TSLS and LIML.

Most common option set: none; at least one call in 12 papers (100%).

```stata
weakivtest
```
JPE 2026, [doi:10.1086/738249](https://doi.org/10.1086/738249), `code/dataverse_KXAVHB/tablea3.do` line 131.

### `ssaggregate`

Used in 8 of 1904 Stata papers (0.4%) — module to create shock-level aggregates for shift-share IV.

Options (share of these 8 papers): `controls` 100%, `l` 100%, `n` 100%, `s` 100%, `sfilename` 75%, `t` 62%, `addmissing` 50%, `sfile` 25%.

Most common option set: `addmissing`, `controls`, `l`, `n`, `s`, `sfilename`, `t`; at least one call in 2 papers (25%).

```stata
ssaggregate `outcomes' [aw=mean_weight], n(bank) t(quarter_year) s(s_fbt) sfilename(shares) l(firm) addmissing controls("`controls'") 
```
ReStud 2022, [doi:10.1093/restud/rdab065](https://doi.org/10.1093/restud/rdab065), `code/zenodo_5094270/Supplementary_-_July2021/Supplementary - July2021/dofile.do` line 936.

Next most common option set: `controls`, `l`, `n`, `s`, `sfilename`, `t`; at least one call in 2 papers (25%).

```stata
ssaggregate `balancevars' z [aw=wei], ///
	n(sic87dd) t(year) s(ind_share) sfilename(Lshares) l(czone) controls("`basecontrols'")  
```
ReStud 2022, [doi:10.1093/restud/rdab030](https://doi.org/10.1093/restud/rdab030), `code/zenodo_4619197/BHJ_Replication_Archive/BHJ Replication Archive/ADH/Code/Table3.do` lines 34-35.
