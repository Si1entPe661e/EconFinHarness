# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `did_imputation`

Used in 18 of 1904 Stata papers (0.9%) — module to perform treatment effect estimation and pre-trend testing in event studies.

Options (share of these 18 papers): `autosample` 89%, `fe` 72%, `cluster` 56%, `horizons` 50%, `pretrends` 44%, `controls` 44%, `pretrend` 39%, `minn` 33%, `maxit` 28%, `hor` 22%.

Most common option set: `autosample`, `cluster`, `fe`; at least one call in 2 papers (11%).

```stata
    did_imputation ltotal estab year treated if sample==1, autosample ///
        fe(`fe_`c'') cluster(company)
```
ReStud 2026, [doi:10.1093/restud/rdag056](https://doi.org/10.1093/restud/rdag056), `code/zenodo_20014224/REStud_replication_files/REStud replication files/do-files/8 EEO-1 employment analysis.do` lines 932-933.

### `event_plot`

Used in 16 of 1904 Stata papers (0.8%) — module to plot the staggered-adoption diff-in-diff ("event study") estimates.

Options (share of these 16 papers): `graph_opt` 100%, `stub_lag` 62%, `stub_lead` 62%, `together` 62%, `ciplottype` 56%, `plottype` 50%, `lag_opt` 44%, `lag_ci_opt` 44%, `default_look` 44%, `noautolegend` 38%.

Most common option set: `ciplottype`, `graph_opt`, `lag_ci_opt`, `lag_opt`, `lead_ci_opt`, `lead_opt`, `plottype`, `stub_lag`, `stub_lead`; at least one call in 2 papers (12%).

```stata
event_plot mat1_twfe#mat3_twfe, stub_lag(g_#) stub_lead(g_m#) ciplottype(rcap) plottype(scatter) ///
		graph_opt(bgcolor(white) plotregion(color(white)) graphregion(color(white)) ///
		xline(0, lpattern(dash) lcolor(gs12) lwidth(thin)) legend(off) ///
		yline(0, lpattern(solid) lcolor(gs12) lwidth(thin)) legend(off) ///
		yscale(r(-0.05 0.1)) ytick(-0.05(0.05)0.1) ///
		ylabel(-0.05(0.05)0.1, labsize(small)) ///
		xscale(r(-3.5 2.5)) xtick(-3(1)2) xlabel(-3 "-7" -2 "-5" -1 "-3"  0 "-1"  1 "1" 2 "3" 3 "5", labsize(small)) ///
		ytitle("Working in Life Sciences", height(6) size(small)) title("TWFE", size(small)) ///
		xtitle("Year to/from Evolution Curriculum Reform", height(6) size(small)) xsize(5) ysize(4)) ///
		lag_opt(msymbol(D) mcolor(black) msize(small)) lead_opt(msymbol(D) mcolor(black) msize(small)) ///
		lag_ci_opt(lcolor(black) lwidth(medthin)) lead_ci_opt(lcolor(black) lwidth(medthin))
```
QJE 2024, [doi:10.1093/qje/qjae019](https://doi.org/10.1093/qje/qjae019), `code/dataverse_HYLZUO/Replication Package_code_acs_analysis/acs_output.do` lines 307-317.

### `eventstudyinteract`

Used in 14 of 1904 Stata papers (0.7%) — module to implement the interaction weighted estimator for an event study.

Options (share of these 14 papers): `cohort` 100%, `control_cohort` 100%, `absorb` 100%, `vce` 100%, `covariates` 50%.

Most common option set: `absorb`, `cohort`, `control_cohort`, `vce`; at least one call in 9 papers (64%).

```stata
    eventstudyinteract `variable' `lags' `leads', ///
        cohort(treatment_year)                    ///
        control_cohort(never_treated)             ///
        absorb(plant_id year)                     ///
        vce(cluster cluster_id)
```
ReStud 2026, [doi:10.1093/restud/rdag047](https://doi.org/10.1093/restud/rdag047), `code/zenodo_19175276/Replication_Package_260506/Replication_Package_260416_restud_rev1/synthetic_replication/Synthesized Do Files/Sun-eventstudy.do` lines 66-70.

Next most common option set: `absorb`, `cohort`, `control_cohort`, `covariates`, `vce`; at least one call in 6 papers (43%).

```stata
eventstudyinteract ext_tot_t post, cohort(startdaynr) control_cohort(Control) covariates($weather) absorb(participant_nr            trip_date exhausted) vce(cluster participant_nr)
```
ReStud 2026, [doi:10.1093/restud/rdag051](https://doi.org/10.1093/restud/rdag051), `code/zenodo_17965910/Replication_MOBIS/Replication_MOBIS/Mobis_regressions.do` line 608.

### `did_multiplegt`

Used in 13 of 1904 Stata papers (0.7%) — module to estimate sharp Difference-in-Difference designs with multiple groups and periods.

Options (share of these 13 papers): `breps` 100%, `cluster` 100%, `placebo` 77%, `dynamic` 62%, `robust_dynamic` 54%, `controls` 46%, `trends_nonparam` 31%, `average_effect` 31%, `save_results` 31%, `jointtestplacebo` 23%.

Most common option set: `breps`, `cluster`, `placebo`; at least one call in 2 papers (15%).

```stata
did_multiplegt F id_firm anno ndr_cal, placebo(3) breps(200) cluster(id_firm)
```
AER 2022, [doi:10.1257/aer.20201015](https://doi.org/10.1257/aer.20201015), `code/do/replication_do/Table_5.do` line 25.

Next most common option set: `breps`, `cluster`, `dynamic`, `placebo`; at least one call in 2 papers (15%).

```stata
did_multiplegt logca group ano treati,  placebo(4) breps(10) dynamic(4) cluster(cluster`y')
```
QJE 2024, [doi:10.1093/qje/qjad032](https://doi.org/10.1093/qje/qjad032), `code/dataverse_Z4QBWJ/Replication_package_code_program_appendices/Appendix_E1.do` line 746.

### `eventdd`

Used in 5 of 1904 Stata papers (0.3%) — module to panel event study models and generate event study plots.

Options (share of these 5 papers): `timevar` 100%, `graph_op` 100%, `ci` 100%, `accum` 60%, `lags` 60%, `leads` 60%, `noline` 60%, `method` 60%, `coef_op` 60%, `hdfe` 40%.

Most common option set: `absorb`, `accum`, `ci`, `ci_op`, `cluster`, `endpoints_op`, `graph_op`, `hdfe`, `lags`, `leads`, `noline`, `timevar`; at least one call in 1 paper (20%).

```stata
eventdd lynching_any all, hdfe absorb(week_date#state_fips fips) timevar(month_to_treat) cluster(state_fips) accum lags(6) leads(6) 
graph_op(ylabel(-.001(.001).002, grid labsize(med)) yscale(range(-.00125 .00225)) 
ytitle("Lynching", size(`tsize')) xtitle("Months to Screening", size(`tsize'))
xlabel(-6(1)6) xline(-.5, lcolor(red)) yline(0, lwidth("thin") lcolor(black)) 
 plotregion(fcolor(white) lcolor(white)) graphregion(fcolor(white) lcolor(white)) bgcolor(white) legend(off)) noline ci(rcap) ci_op(lcolor(`rcap_color')) endpoints_op(mcolor(maroon));
```
AER 2023, [doi:10.1257/aer.20201867](https://doi.org/10.1257/aer.20201867), `code/replication_FINAL_v2/code/figure3.do` lines 7-11.

Next most common option set: `absorb`, `accum`, `ci`, `cluster`, `hdfe`, `lags`, `leads`, `timevar`; at least one call in 1 paper (20%).

```stata
eventdd `y' all, hdfe absorb(`fe' fips) timevar(month_to_treat) cluster(state_fips) accum lags(6) leads(6) ci(rcap)
```
AER 2023, [doi:10.1257/aer.20201867](https://doi.org/10.1257/aer.20201867), `code/replication_FINAL_v2/code/figureA8.do` line 25.

### `sdid`

Used in 5 of 1904 Stata papers (0.3%) — module to perform synthetic difference-in-differences estimation, inference, and visualization.

Options (share of these 5 papers): `vce` 100%, `seed` 80%, `covariates` 80%, `reps` 40%, `graph` 40%.

Most common option set: `vce`; at least one call in 2 papers (40%).

```stata
sdid log_extortion muni_route ym comp_post,  vce(jackknife) 
```
ReStud 2025, [doi:10.1093/restud/rdae057](https://doi.org/10.1093/restud/rdae057), `code/zenodo_10855174/replication/code/nonaggression_pact_effect/effect_on_extortion_synthetic_dd.do` line 241.

Next most common option set: `covariates`, `vce`; at least one call in 2 papers (40%).

```stata
	sdid return_i firmn year treat, vce(placebo) covariates($controls) 
```
JFE 2024, [doi:10.1016/j.jfineco.2024.103809](https://doi.org/10.1016/j.jfineco.2024.103809), `code/mendeley_nkk2cyw4f6_v2/Replication/Replication/do/analysis_sdid.do` line 213.

### `twowayfeweights`

Used in 5 of 1904 Stata papers (0.3%) — module to estimate the weights and measure of robustness to treatment effect heterogeneity attached to two-way fixed effects regressions.

Options (share of these 5 papers): `type` 100%, `controls` 60%, `path` 40%.

Most common option set: `type`; at least one call in 2 papers (40%).

```stata
twowayfeweights cash_atw gvkey yearq max_ann56 if ll_window==1 , type(feTR)
```
JFE 2024, [doi:10.1016/j.jfineco.2024.103795](https://doi.org/10.1016/j.jfineco.2024.103795), `code/mendeley_9p3m5vgsyf_v2/replication_package_responses_to_fragility_posted/responsetofragility_resultsinpaper.do` line 478.

Next most common option set: `path`, `type`; at least one call in 1 paper (20%).

```stata
twowayfeweights ltot_cals_pc area period_reg expansion, type(feTR) path("$CLEANDATA/OTHER/weights_chaisemartin.dta")		
```
AER 2024, [doi:10.1257/aer.20220822](https://doi.org/10.1257/aer.20220822), `code/code/analysis/figure_A3.do` line 9.
