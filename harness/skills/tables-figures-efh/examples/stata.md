# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `graph export`

Used in 1215 of 1904 Stata papers (64%) — Export current graph.

Options (share of these 1215 papers): `replace` 100%, `as` 34% (`pdf` 22%, `png` 9%, `eps` 9%), `width` 8%, `name` 7%, `height` 3%, `preview?` 3%, `fontface` 2%, `logo?` 1%, `font?` 0.7%, `mag` 0.7%.

Most common option set: `replace`; at least one call in 928 papers (76%).

```stata
graph export "${figures}/fig_1.png", replace 
```
RFS 2026, [doi:10.1093/rfs/hhag045](https://doi.org/10.1093/rfs/hhag045), `code/dataverse_2EVES4/1_code/3_2_descriptive_figures.do` line 71; license file: BSD.

Next most common option set: `as`, `replace`; at least one call in 349 papers (29%).

```stata
graph export ../output/log_difference.pdf, as(pdf) replace
```
QJE 2025, [doi:10.1093/qje/qjaf015](https://doi.org/10.1093/qje/qjaf015), `code/dataverse_N7534Z/MPC2008-Public-main_graph_nipaVcex_code/dist_measurement_error.do` line 98; license file: GPL.

### `twoway`

Used in 1003 of 1904 Stata papers (53%) — Two-way graphs.

Options (share of these 1003 papers): `legend` 89% (`order` 48%, `label` 24%, `labels` 6%, `rows` 5%), `xtitle` 84%, `ytitle` 83%, `xlabel` 67%, `ylabel` 64%, `graphregion` 59% (`color` 43%, `fcolor` 17%, `margin` 4%), `title` 39%, `xline` 37%, `yline` 32%, `yscale` 30% (`range` 21%, `rescale` 6%, `titlegap` 2%).

Most common option set: none; at least one call in 197 papers (20%).

```stata
twoway 
```
Econometrica 2026, [doi:10.3982/ecta21849](https://doi.org/10.3982/ecta21849), `code/zenodo_17537119/ECMA_replication_to_submit/ECMA_replication_to_submit/codes/graph_earn_hours_interacted.do` line 88.

### `esttab`

Used in 919 of 1904 Stata papers (48%) — Display formatted regression table.

Options (share of these 919 papers): `replace` 88%, `label` 71%, `se` 64%, `keep` 57%, `b` 55%, `cells?` 51% (`b` 17%), `star` 49%, `stats?` 49% (`r2` 7%), `nomtitles` 44%, `noobs` 42%.

Most common option set: none; at least one call in 43 papers (5%).

```stata
esttab reg_D_apcds reg_D_cyc reg_D_bf reg_D_scr reg_D_esp 
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_phone_survey/create_regression_tables_KW.do` line 140; license file: BSD.

### `outreg2`

Used in 429 of 1904 Stata papers (23%) — Arrange regression, summary, and tabulation into an illustrative table.

Options (share of these 429 papers): `replace` 80%, `append?` 71%, `ctitle` 48%, `keep` 46%, `dec` 41%, `nocons` 41%, `addstat` 39%, `addtext` 38%, `excel` 37%, `label` 35%.

Most common option set: `replace`; at least one call in 24 papers (6%).

```stata
    outreg2 using "$outpath/table5_iv", replace
```
RFS 2026, [doi:10.1093/rfs/hhag032](https://doi.org/10.1093/rfs/hhag032), `code/dataverse_4DACEC/code_analysis/5_iv_baseline.do` line 118; license file: MIT.

### `graph combine`

Used in 395 of 1904 Stata papers (21%) — Combine multiple graphs.

Options (share of these 395 papers): `graphregion` 53% (`color` 39%, `fcolor` 11%, `margin` 5%), `xsize` 43%, `ysize` 42%, `ycommon` 34%, `rows` 31%, `cols` 25%, `xcommon` 22%, `col?` 22%, `iscale` 20%, `title` 20%.

Most common option set: none; at least one call in 39 papers (10%).

```stata
	graph combine s1 s2 s3 s4
```
QJE 2026, [doi:10.1093/qje/qjaf044](https://doi.org/10.1093/qje/qjaf044), `code/dataverse_Q22XR1/qje-repkit-to-upload/qje-repkit-to-upload/code/71_banks_at_risk.do` line 89.

### `tabstat`

Used in 369 of 1904 Stata papers (19%) — Compact table of summary statistics.

Options (share of these 369 papers): `statistics` 78% (`mean` 52%, `n` 12%, `sum` 9%, `count` 6%), `by` 60%, `columns` 34% (`statistics` 18%), `save` 28%, `stats` 19% (`mean` 12%, `n` 3%, `sum` 3%, `min` 2%), `format` 18%, `longstub` 5%, `nototal` 3%, `varwidth` 2%, `labelwidth` 1%.

Most common option set: `by`, `statistics`; at least one call in 115 papers (31%).

```stata
tabstat inv, stat(sum) by(year)
```
QJE 2026, [doi:10.1093/qje/qjag041](https://doi.org/10.1093/qje/qjag041), `code/dataverse_8P3S0V/replication_ding26/programs/02_to_matlab_v06.do` line 116.

Next most common option set: `by`; at least one call in 87 papers (24%).

```stata
tabstat lf, by(year)
```
ReStud 2026, [doi:10.1093/restud/rdaf030](https://doi.org/10.1093/restud/rdaf030), `code/zenodo_14780637/RESTUD_MS31175-4_ReplicationFiles/ReplicationFilesForRESTUD/Stata_and_data/Code/_prepKK.do` line 35.

### `coefplot`

Used in 280 of 1904 Stata papers (15%) — Plotting regression coefficients and other.

Options (share of these 280 papers): `vertical?` 72%, `xtitle` 66%, `ytitle` 65%, `keep` 63%, `graphregion` 62% (`color` 47%, `fcolor` 13%), `yline` 61%, `xline` 57%, `xlabel` 55%, `ylabel` 55%, `ciopts` 52% (`recast` 34%, `lcolor` 8%, `color` 4%, `lwidth` 4%).

Most common option set: none; at least one call in 4 papers (1%).

```stata
	coefplot (matrix(coeffmat[,1]), ci((coeffmat[,2] coeffmat[,3])) ciopts(recast(rcap) lcolor(gs4)) mcolor(gs4) graphr(c(white) margin(medsmall)) xline(0, lpattern(dash)) xline(`base4') bgcolor(white)) 
```
ReStud 2026, [doi:10.1093/restud/rdag027](https://doi.org/10.1093/restud/rdag027), `code/zenodo_17361408/BFFPT_RESTUD_replication/code/3_figureb3.do` line 134.

### `graph bar`

Used in 267 of 1904 Stata papers (14%) — Bar charts.

Options (share of these 267 papers): `over` 95%, `ytitle` 85%, `legend` 75% (`label` 27%, `order` 22%, `size` 5%, `position` 4%), `bar` 69%, `graphregion` 55% (`color` 43%, `fcolor` 10%, `margin` 3%), `ylabel` 50%, `title` 25%, `b1title?` 24%, `stack` 23%, `asyvars` 19%.

Most common option set: `over`; at least one call in 12 papers (4%).

```stata
	graph bar, over(min_grade_gifted)
```
JPE 2026, [doi:10.1086/743389](https://doi.org/10.1086/743389), `code/dataverse_MNX4AG/Code/JPE_FIGURES.do` line 446.
