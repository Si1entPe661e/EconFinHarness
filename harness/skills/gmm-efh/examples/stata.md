# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `xtivreg2`

Used in 46 of 1904 Stata papers (2%) — module to perform extended IV/2SLS, GMM and AC/HAC, LIML and k-class regression for panel data models.

Options (share of these 46 papers): `fe` 98%, `cluster` 76%, `first` 35%, `i` 28%, `partial` 26%, `savefirst` 20%, `robust` 17%, `savefprefix` 13%, `ffirst` 11%, `cl` 11%.

Most common option set: `cluster`, `fe`; at least one call in 12 papers (26%).

```stata
	xtivreg2 f`i'.L0dy DSR_H_RoTW if xsample == 1,  fe cluster(id Year)
```
RFS 2026, [doi:10.1093/rfs/hhaf114](https://doi.org/10.1093/rfs/hhaf114), `code/dataverse_0Z5QUQ/RFS_Final_Zip/Do_Files/4_Tables.do` line 2715.

### `gmm`

Used in 31 of 1904 Stata papers (2%) — Generalized method of moments estimation.

Options (share of these 31 papers): `winitial` 81% (`identity` 52%, `unadjusted` 23%), `instruments` 68%, `from` 45%, `vce` 42% (`cluster` 26%, `robust` 10%), `conv_maxiter` 29%, `wmatrix` 29% (`cluster` 10%, `unadjusted` 10%, `hac` 6%), `twostep` 26%, `onestep` 26%, `technique` 16%, `nocommonesample` 13%.

Most common option set: none; at least one call in 4 papers (13%).

```stata
eststo M`j': qui gmm ///
	 (eq1: conts_bulkCGT - {cons_bulk} -   backlog_bulkCGT_ln*{coeff_backlog} - inter_p_post_bulkCGT*{coeff_post_p} - ({bulk:P_CGT_bulkq `XB`j''})) ///
	 (eq2: conts_tankerCGT - {cons_tanker}  - backlog_tankerCGT_ln*{coeff_backlog} - inter_p_post_tankerCGT*{coeff_post_p}- ({tanker:P_CGT_tankerq `XT`j''})) ///
	 (eq3: conts_containerCGT - {cons_container}  - backlog_containerCGT_ln*{coeff_backlog}  - inter_p_post_containerCGT*{coeff_post_p} - ({container:P_CGT_containerq `XC`j''})) ///
	 vce(robust) ///
instruments(eq1: `Z' `XB`j'' ) ///
instruments(eq2: `Z' `XT`j'' ) ///
instruments(eq3: `Z' `XC`j'' ) ///
winitial(unadjusted, independent)  onestep nocommonesample
```
ReStud 2025, [doi:10.1093/restud/rdaf011](https://doi.org/10.1093/restud/rdaf011), `code/zenodo_14083198/Replication_BKZ_2024_v2/code/2_demand/Dem1_Demand_Estimation_GMM.do` lines 629-637.

### `xtabond2`

Used in 8 of 1904 Stata papers (0.4%) — module to extend xtabond dynamic panel data estimator.

Options (share of these 8 papers): `gmm` 62%, `robust` 62%, `iv` 50%, `twostep` 38%, `gmmstyle` 38%, `small` 25%, `h` 25%, `ivstyle` 25%.

Most common option set: `gmm`, `iv`, `robust`, `twostep`; at least one call in 2 papers (25%).

```stata
eststo ss1x: 
xtabond2 $yvar L(1/`y_L').$yvar L0.(`xchvars') `xcntrls' `xcntrls2'
if inrange(age,`a1',`a2') & lfp==1 , robust twostep
gmm($yvar,     lag(`wk_Lst' `wk_Len') collapse) 
iv(`xcntrls', equation(both)) 
iv(`xcntrls' `xcntrls2' `xchvars', equation(level)) ;
```
ReStud 2026, [doi:10.1093/restud/rdaf030](https://doi.org/10.1093/restud/rdaf030), `code/zenodo_14780637/RESTUD_MS31175-4_ReplicationFiles/ReplicationFilesForRESTUD/Stata_and_data/Code/HKZ_Table6_wages_selcorr.do` lines 89-94.
