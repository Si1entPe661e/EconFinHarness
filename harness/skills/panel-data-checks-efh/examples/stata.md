# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `merge`

Used in 1406 of 1904 Stata papers (74%) — Merge datasets.

Options (share of these 1406 papers): `nogenerate` 46%, `keepusing` 44%, `keep` 42% (`match` 17%, `master` 12%), `update` 19%, `generate` 17%, `assert` 11% (`match` 3%, `master` 2%, `using` 0.9%), `replace` 6%, `force` 5%, `nokeep?` 2%, `sort?` 2%.

Most common option set: none; at least one call in 1209 papers (86%).

```stata
merge m:1 fundno using l2
```
RFS 2026, [doi:10.1093/rfs/hhag032](https://doi.org/10.1093/rfs/hhag032), `code/dataverse_4DACEC/code_data_cleaning/3_merge_s12_crsp.do` line 19; license file: MIT.

Next most common option set: `nogenerate`; at least one call in 459 papers (33%).

```stata
merge 1:m bvdid year using `grid_status', nogen
```
RFS 2026, [doi:10.1093/rfs/hhag045](https://doi.org/10.1093/rfs/hhag045), `code/dataverse_2EVES4/1_code/1_3_firmvars_orbis.do` line 196; license file: BSD.

### `duplicates`

Used in 906 of 1904 Stata papers (48%) — Report, tag, or drop duplicate observations.

Options (share of these 906 papers): `force` 62%, `generate` 36% (`tag` 6%), `table` 0.2%, `divider` 0.2%, `sepby` 0.2%.

Most common option set: none; at least one call in 643 papers (71%).

```stata
	duplicates drop
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_emissions/construct_analysis_panel.do` line 190; license file: BSD.

Next most common option set: `force`; at least one call in 566 papers (62%).

```stata
duplicates drop t, force
```
QJE 2026, [doi:10.1093/qje/qjag012](https://doi.org/10.1093/qje/qjag012), `code/dataverse_CMEFMV/MS_42228 _replication/Data/1.main.do` line 791.

### `xtset`

Used in 672 of 1904 Stata papers (35%) — Declare data to be panel data.

Options (share of these 672 papers): `clear` 5%, `yearly` 4%, `delta` 4%, `quarterly` 2%, `monthly` 2%, `weekly` 0.3%.

Most common option set: none; at least one call in 641 papers (95%).

```stata
    xtset uID t
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_sim-results/cfl.do` line 147; license file: GPL.

### `tsset`

Used in 622 of 1904 Stata papers (33%) — Declare data to be time-series data.

Options (share of these 622 papers): `quarterly` 4%, `yearly` 4%, `clear` 4%, `monthly` 4%, `delta` 3%, `daily` 0.8%, `generic` 0.3%.

Most common option set: none; at least one call in 582 papers (94%).

```stata
tsset Year
```
JPE 2025, [doi:10.1086/733423](https://doi.org/10.1086/733423), `code/dataverse_TIL7KK/Main_Step3.do` line 8; license file: BSD.

### `assert`

Used in 402 of 1904 Stata papers (21%) — Verify truth of claim.

Options (share of these 402 papers): `fast` 0.7%, `rc0` 0.5%.

Most common option set: none; at least one call in 400 papers (100%).

```stata
	assert polcode!=. 
```
AER 2025, [doi:10.1257/aer.20230501](https://doi.org/10.1257/aer.20230501), `code/code_intl_climate/OECD_Climate_Heatplots.do` line 428; license file: GPL.

### `isid`

Used in 196 of 1904 Stata papers (10%) — Check for unique identifiers.

Options (share of these 196 papers): `missok` 7%, `sort` 5%.

Most common option set: none; at least one call in 190 papers (97%).

```stata
isid pid
```
Econometrica 2026, [doi:10.3982/ecta22160](https://doi.org/10.3982/ecta22160), `code/zenodo_15776949/replication_synthetic_davis_greenberg_jones/replication_synthetic_davis_greenberg_jones/do/0_cleanData.do` line 241.

### `unique`

Used in 185 of 1904 Stata papers (10%) — Unique values of a variable or group of variables.

Options (share of these 185 papers): `by` 14%, `generate` 12%, `detail` 2%.

Most common option set: none; at least one call in 173 papers (94%).

```stata
unique permno
```
ReStud 2024, [doi:10.1093/restud/rdad041](https://doi.org/10.1093/restud/rdad041), `code/zenodo_7617222/replication_package_v2/replication_package_v2/Replication_Package_for_Empirics/Figure2/create_profitability.do` line 39; license file: MIT.

### `mvencode`

Used in 41 of 1904 Stata papers (2%) — Change missing values to numeric values and vice versa.

Options (share of these 41 papers): `mv` 100%, `override` 71%.

Most common option set: `mv`, `override`; at least one call in 29 papers (71%).

```stata
		mvencode muhat, mv(0) over
```
Econometrica 2026, [doi:10.3982/ecta21097](https://doi.org/10.3982/ecta21097), `code/zenodo_17301245/final_replication_package/final_replication_package/code/02_data_affinity.do` line 516.

Next most common option set: `mv`; at least one call in 21 papers (51%).

```stata
mvencode combo*, mv(0)
```
QJE 2026, [doi:10.1093/qje/qjaf055](https://doi.org/10.1093/qje/qjaf055), `code/dataverse_RMSRWB/replication/replication/prog/create_premia.do` line 81.
