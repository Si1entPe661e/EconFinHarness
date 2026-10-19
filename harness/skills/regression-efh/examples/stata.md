# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `regress`

Used in 1431 of 1904 Stata papers (75%) — Linear regression.

Options (share of these 1431 papers): `robust` 40%, `cluster` 40%, `vce` 23% (`cluster` 17%, `robust` 6%), `noconstant` 17%, `noc?` 2%, `absorb?` 2%, `nocon?` 1%, `level` 1%, `noheader` 0.8%, `a?` 0.8%.

Most common option set: none; at least one call in 1040 papers (73%).

```stata
reg `lhs' `rhs'
```
RFS 2026, [doi:10.1093/rfs/hhag032](https://doi.org/10.1093/rfs/hhag032), `code/dataverse_4DACEC/code_analysis/9_rsu_psu_magnitudes.do` line 103; license file: MIT.

Next most common option set: `robust`; at least one call in 509 papers (36%).

```stata
	reg testmay, robust
```
QJE 2025, [doi:10.1093/qje/qjaf015](https://doi.org/10.1093/qje/qjaf015), `code/dataverse_N7534Z/MPC2008-Public-main_descriptive_stats_code/schedule_table.do` line 83; license file: GPL.

### `reghdfe`

Used in 736 of 1904 Stata papers (39%) — Linear regression with multiple fixed effects. Also supports individual FEs with group-level outcomes.

Options (share of these 736 papers): `absorb` 98%, `cluster` 60%, `vce` 54% (`cluster` 43%, `robust` 16%), `residuals` 24%, `noabsorb?` 13%, `noconstant` 10%, `keepsingletons` 5%, `old?` 2%, `tolerance` 2%, `compile?` 1%.

Most common option set: `absorb`, `cluster`; at least one call in 410 papers (56%).

```stata
	eststo m3 : reghdfe exports_g withdraw_times_post post, absorb(pair_FE partner_time_FE industry_time_FE) cluster(pair_FE)
```
RFS 2026, [doi:10.1093/rfs/hhag045](https://doi.org/10.1093/rfs/hhag045), `code/dataverse_2EVES4/1_code/4_3_did_bilateral_productlevel.do` line 60; license file: BSD.

Next most common option set: `absorb`, `vce`; at least one call in 359 papers (49%).

```stata
eststo reg_3: reghdfe `price_var' `holding_var', a(period gpcb_id) vce(cluster gpcb_id)
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_trading/make_elasticity_table_hetero.do` line 97; license file: BSD.

### `areg`

Used in 472 of 1904 Stata papers (25%) — Linear regression with many indicator.

Options (share of these 472 papers): `absorb` 99%, `cluster` 52%, `robust` 21%, `vce` 21% (`cluster` 19%, `robust` 3%), `if?` 0.6%, `noomitted?` 0.6%, `using?` 0.4%, `keep?` 0.4%.

Most common option set: `absorb`, `cluster`; at least one call in 219 papers (46%).

```stata
areg lnxi `x' , a(ipcyear) cluster(ipc)
```
JFE 2026, [doi:10.1016/j.jfineco.2026.104276](https://doi.org/10.1016/j.jfineco.2026.104276), `code/mendeley_d322y5hbmx_v1/TBSL_Process_Replication/code_and_data/Table7.do` line 46.

Next most common option set: `absorb`; at least one call in 206 papers (44%).

```stata
areg fy, a(sector) 
```
Econometrica 2026, [doi:10.3982/ecta21849](https://doi.org/10.3982/ecta21849), `code/zenodo_17537119/ECMA_replication_to_submit/ECMA_replication_to_submit/codes/sector_firm_year_effs.do` line 33.

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
xtreg   wagetemp c.exper c.age c.cum_2yr c.cum_4yr b1997.year i.in_2yr i.in_4yr i.in_grad_school i.workPT i.grad_2yr i.grad_4yr if wflg & female==1, fe
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_data-cleaning_nlsy97/wage_cleaning.do` line 76; license file: GPL.

### `logit`

Used in 150 of 1904 Stata papers (8%) — Logistic regression, reporting.

Options (share of these 150 papers): `cluster` 20%, `vce` 19% (`cluster` 13%, `robust` 3%), `robust` 10%, `iterate` 7%, `or` 6%, `noconstant` 5%, `nolog?` 3%, `asis` 2%, `difficult` 1%, `nocon?` 1%.

Most common option set: none; at least one call in 85 papers (57%).

```stata
			logit S Z_* X_* ZX_*
```
AER 2021, [doi:10.1257/aer.20190221](https://doi.org/10.1257/aer.20190221), `code/code/analysis/master.do` line 425; license file: GPL.

Next most common option set: `cluster`; at least one call in 24 papers (16%).

```stata
logit divorce0 c.surplus i.year , clus(cluster)
```
Econometrica 2026, [doi:10.3982/ecta21097](https://doi.org/10.3982/ecta21097), `code/zenodo_17301245/final_replication_package/final_replication_package/code/06_divorce_logit.do` line 37.

### `probit`

Used in 150 of 1904 Stata papers (8%) — Probit regression.

Options (share of these 150 papers): `cluster` 25%, `vce` 24% (`cluster` 20%, `robust` 3%), `robust` 9%, `difficult` 3%, `iterate` 3%, `asis` 3%, `noconstant` 1%, `nocon?` 1%.

Most common option set: none; at least one call in 77 papers (51%).

```stata
quietly probit crisis3y bank_debt
```
JPE 2025, [doi:10.1086/733423](https://doi.org/10.1086/733423), `code/dataverse_TIL7KK/Main_Step3.do` line 16; license file: BSD.

Next most common option set: `cluster`; at least one call in 33 papers (22%).

```stata
probit F3bust LD3supply_GDP LD3demand_GDP ccode*, cluster(id)
```
RFS 2026, [doi:10.1093/rfs/hhaf114](https://doi.org/10.1093/rfs/hhaf114), `code/dataverse_0Z5QUQ/RFS_Final_Zip/Do_Files/4_Tables.do` line 960.

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

### `poisson`

Used in 34 of 1904 Stata papers (2%) — Poisson regression.

Options (share of these 34 papers): `robust` 29%, `cluster` 29%, `vce` 21% (`cluster` 12%, `robust` 9%), `iterate` 12%, `noconstant` 6%.

Most common option set: none; at least one call in 11 papers (32%).

```stata
 poisson nmbr_displ  ln_geodesic ln_nmbr_displ_parents d_displ_parents
```
QJE 2026, [doi:10.1093/qje/qjag009](https://doi.org/10.1093/qje/qjag009), `code/dataverse_SDOODF/_conf_displ_humcap_public/code/1_creation/_to_del/8_cost_od_iv_6_agg_23ethn.do` line 283.

Next most common option set: `robust`; at least one call in 7 papers (21%).

```stata
					poisson n after10white 1.after10white#1.in280380 after10notwhite ///
						1.after10notwhite#1.in280380 notwhite in280380, r
```
ReStud 2026, [doi:10.1093/restud/rdag037](https://doi.org/10.1093/restud/rdag037), `code/zenodo_18343807/REStud_Rep_MS33255/REStud_Rep_MS33255/code/3_001_apdx_ussc.do` lines 392-393.
