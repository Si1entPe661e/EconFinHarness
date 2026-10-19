# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `ssaggregate`

Used in 8 of 1904 Stata papers (0.4%) — module to create shock-level aggregates for shift-share IV.

Options (share of these 8 papers): `n` 100%, `s` 100%, `l` 100%, `controls` 100%, `sfilename` 75%, `t` 62%, `addmissing` 50%, `sfile` 25%.

Most common option set: `controls`, `l`, `n`, `s`, `sfilename`, `t`; at least one call in 2 papers (25%).

```stata
ssaggregate `balancevars' z [aw=wei], ///
	n(sic87dd) t(year) s(ind_share) sfilename(Lshares) l(czone) controls("`basecontrols'")  
```
ReStud 2022, [doi:10.1093/restud/rdab030](https://doi.org/10.1093/restud/rdab030), `code/zenodo_4619197/BHJ_Replication_Archive/BHJ Replication Archive/ADH/Code/Table3.do` lines 34-35.

Next most common option set: `addmissing`, `controls`, `l`, `n`, `s`, `sfilename`, `t`; at least one call in 2 papers (25%).

```stata
ssaggregate `outcomes' [aw=mean_weight], n(bank) t(quarter_year) s(s_fbt) sfilename(shares) l(firm) addmissing controls("`controls'") 
```
ReStud 2022, [doi:10.1093/restud/rdab065](https://doi.org/10.1093/restud/rdab065), `code/zenodo_5094270/Supplementary_-_July2021/Supplementary - July2021/dofile.do` line 936.

### `ivreg_ss`

Used in 5 of 1904 Stata papers (0.3%) — module to compute confidence intervals, standard errors, and p-values in an IV regression in which the excluded instrumental variable has a shift-share structure.

Options (share of these 5 papers): `endogenous_var` 100%, `shiftshare_iv` 100%, `share_varlist` 100%, `control_varlist` 60%, `weight_var` 40%, `akmtype` 40%, `cluster_var` 40%.

Most common option set: `control_varlist`, `endogenous_var`, `share_varlist`, `shiftshare_iv`; at least one call in 1 paper (20%).

```stata
		ivreg_ss dlrexp, endogenous_var(dlrdom) shiftshare_iv(dvehpopz_g2_2) ///
		share_varlist(weight01002-weight99999) control_varlist(dtfpy dlavrwage sid10-sid33)
```
AER 2021, [doi:10.1257/aer.20181853](https://doi.org/10.1257/aer.20181853), `code/code/Table_7_AlternativeIVs.do` lines 241-242.

Next most common option set: `akmtype`, `endogenous_var`, `share_varlist`, `shiftshare_iv`, `weight_var`; at least one call in 1 paper (20%).

```stata
ivreg_ss D_`depvar', endogenous_var(IMR) shiftshare_iv($shock) share_varlist(lambda*) ///
 weight_var(weight) akmtype(1) 
```
AER 2022, [doi:10.1257/aer.20191234](https://doi.org/10.1257/aer.20191234), `code/Code/Analysis/Appendix/Tables/F5_inference.do` lines 121-122.
