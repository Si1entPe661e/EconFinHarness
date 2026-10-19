# MATLAB examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1084 MATLAB replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `unique`

Used in 339 of 1084 MATLAB papers (31%) — Unique values.

Options (share of these 339 papers): `rows?` 3%.

Most common option set: none; at least one call in 338 papers (100%).

```matlab
qd.infos.size_of_action_space = length(unique(A));
```
IJOC 2026, [doi:10.1287/ijoc.2025.1183](https://doi.org/10.1287/ijoc.2025.1183), `code/github_INFORMSJoC_2025.1183/scripts/q_tools/clinical_flexstages_generate.m` line 123; license file: MIT.

### `exist`

Used in 287 of 1084 MATLAB papers (26%) — Check existence of variable, script, function, folder, or class.

Options (share of these 287 papers): `bayestopt_?` 9%, `dataset_?` 9%, `estim_params_?` 9%, `estimation_info?` 9%, `dataset_info?` 8%, `oo_recursive_?` 8%, `X?` 4%, `OCTAVE_VERSION?` 3%, `alpha?` 3%, `N?` 2%.

Most common option set: none; at least one call in 197 papers (69%).

```matlab
if ~exist('L')
```
MPC 2026, [doi:10.1007/s12532-026-00306-5](https://doi.org/10.1007/s12532-026-00306-5), `code/github_Wu-Can_ALM-SNCG-SMM/subfun/mypsqmr.m` line 43; license file: GPL.

### `strjoin`

Used in 31 of 1084 MATLAB papers (3%) — Join strings in array.

Most common option set: none; at least one call in 31 papers (100%).

```matlab
abip_ldl = strjoin(abip_ldl);
```
IJOC 2025, [doi:10.1287/ijoc.2023.0017](https://doi.org/10.1287/ijoc.2023.0017), `code/github_INFORMSJoC_2023.0017/src/abip-lp/compile_direct.m` line 72; license file: MIT.

### `containers.Map`

Used in 19 of 1084 MATLAB papers (2%) — Object that maps unique keys to values.

Most common option set: none; at least one call in 18 papers (95%).

```matlab
genreMap = containers.Map(genreNames, 1:nGenres);
```
IJOC 2026, [doi:10.1287/ijoc.2025.1169](https://doi.org/10.1287/ijoc.2025.1169), `code/github_INFORMSJoC_2025.1169/src/utils/prepare_movielens1m.m` line 48; license file: MIT.

### `ismissing`

Used in 19 of 1084 MATLAB papers (2%) — Find missing values.

Most common option set: none; at least one call in 19 papers (100%).

```matlab
    tostata=tostata(~any(ismissing(tostata),2),:);
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_estimation-stage3-5-structural/runmodel_consump_jointsearchfrictions_WCabsorb.m` line 177; license file: GPL.

### `outerjoin`

Used in 19 of 1084 MATLAB papers (2%) — Outer join between two tables or timetables.

Options (share of these 19 papers): `MergeKeys` 68%, `Keys` 63%, `Type` 53%, `RightVariables` 21%.

Most common option set: `Keys`, `MergeKeys`; at least one call in 6 papers (32%).

```matlab
            obj.output_it = outerjoin(obj.output_it,xi_plant,...
                'Keys','id_plant','MergeKeys',true);
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_model_matlab_.etsCounter/etsCounter.m` lines 212-213; license file: BSD.

Next most common option set: `Keys`, `MergeKeys`, `Type`; at least one call in 6 papers (32%).

```matlab
T = outerjoin(Q, P, 'Keys', 'Date', 'MergeKeys', true, 'Type', 'left');
```
ReStud 2026, [doi:10.1093/restud/rdag081](https://doi.org/10.1093/restud/rdag081), `code/zenodo_18527736/Replication_MSFD_with_OFI/Replication_MSFD_with_OFI_g/Data/FDIC_aggregate/build_profitability_input.m` line 39.

### `rmmissing`

Used in 14 of 1084 MATLAB papers (1%) — Remove missing entries.

Options (share of these 14 papers): `DataVariables` 21%.

Most common option set: none; at least one call in 12 papers (86%).

```matlab
        d = rmmissing(d);
```
JASA 2025, [doi:10.1080/01621459.2024.2448029](https://doi.org/10.1080/01621459.2024.2448029), `code/github_yzhanghf_JASA-TM-2022-0839/plot_CDF_approximation_error_deter.m` line 32; license file: MIT.

Next most common option set: `DataVariables`; at least one call in 3 papers (21%).

```matlab
    SpotLow = rmmissing(SpotLow, 'DataVariables',{'Dates'});
```
JFE 2024, [doi:10.1016/j.jfineco.2024.103886](https://doi.org/10.1016/j.jfineco.2024.103886), `code/mendeley_mkm2z8p6gf_v2/Codes4Sharing/Step0g_computeHighLow.m` line 89.

### `validatestring`

Used in 14 of 1084 MATLAB papers (1%) — Check validity of text.

Options (share of these 14 papers): `legendflex?` 21%, `shade?` 21%, `hatchfill2?` 14%.

Most common option set: none; at least one call in 10 papers (71%).

```matlab
checkPosition = @(x) any(validatestring(x, validPositions));
```
Econometrica 2024, [doi:10.3982/ecta17513](https://doi.org/10.3982/ecta17513), `code/zenodo_10459782/Replication_package_r/Replication package_r/Replication/labelpoints.m` line 365; license file: BSD.

Next most common option set: `legendflex?`; at least one call in 3 papers (21%).

```matlab
validatestring(Opt.box, {'on', 'off'}, 'legendflex', 'box');
```
RFS 2026, [doi:10.1093/rfs/hhag062](https://doi.org/10.1093/rfs/hhag062), `code/dataverse_recovered/13958988/support_code/legendflex.m` line 299.
