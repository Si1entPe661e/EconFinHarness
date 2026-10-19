# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `randcmd`

Used in 6 of 1904 Stata papers (0.3%) — module to compute randomization inference p-values.

Options (share of these 6 papers): `reps` 100%, `treatvars` 100%, `seed` 67%, `strata` 50%, `calc1` 33%, `calc2` 33%, `groupvar` 33%.

Most common option set: `reps`, `seed`, `treatvars`; at least one call in 2 papers (33%).

```stata
randcmd((treat1 treat2 treat3) reg end_mhscore treat1 treat2 treat3 $control_list i.unionID mhscore if main==1, vce(cluster villageID)) ///
		((treat1 treat2 treat3) reg end_swb treat1 treat2 treat3 $control_list i.unionID swb if main==1, vce(cluster villageID)) ///
		((treat1 treat2 treat3) reg end_iccscore treat1 treat2 treat3 $control_list i.unionID iccscore if main==1, vce(cluster villageID)), ///
		treatvars(treat1 treat2 treat3) seed(1234) reps(1000)
```
QJE 2026, [doi:10.1093/qje/qjag001](https://doi.org/10.1093/qje/qjag001), `code/dataverse_WJAOOA/Replication files SVZ 2025/Replication files SVZ 2025/Analysis/3.results_main_exhibits.do` lines 706-709.

Next most common option set: `calc1`, `calc2`, `groupvar`, `reps`, `seed`, `strata`, `treatvars`; at least one call in 1 paper (17%).

```stata
for var hcH2NormalDeliveryFac  hpPrefH2PostNat0d_6w hpPrefH2Attendance hpPrefH2Child0_59moWei hpPrefH2BCGUn1yr  hpPrefH2OPV3rdDose hpPrefH2measles : ///
	randcmd ((DD_pl) areg X caT after DD afterPl DD_pl goodNetwork hpStaff  map1 map2 hmisDistrictRateG12 if XNM > 2, absorb(province) cluster(district) ), ///
		treatvars(caT) strata(strat_pairwise_group) groupvar(district) reps(10000) seed(1) calc1(replace DD = caT*after) calc2(replace DD_pl = caT*afterPl)
```
AER 2020, [doi:10.1257/aer.20180326](https://doi.org/10.1257/aer.20180326), `code/AER_data/2 - Analysis.do` lines 1641-1643.
