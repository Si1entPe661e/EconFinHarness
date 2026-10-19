# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `numpy.unique`

Used in 118 of 864 Python papers (14%) — Fundamental package for array computing in Python.

Options (share of these 118 papers): `return_counts` 22%, `axis` 11%, `return_index` 11%, `return_inverse` 9%.

Most common option set: none; at least one call in 96 papers (81%).

```python
        if np.unique(y).size >= 2:
```
IJOC 2026, [doi:10.1287/ijoc.2023.0493](https://doi.org/10.1287/ijoc.2023.0493), `code/github_INFORMSJoC_2023.0493/scripts/run_CAAC.py` line 370; license file: MIT.

Next most common option set: `return_counts`; at least one call in 22 papers (19%).

```python
    _, col_nrows = np.unique(indices, return_counts=True)
```
IJOC 2026, [doi:10.1287/ijoc.2024.0709](https://doi.org/10.1287/ijoc.2024.0709), `code/github_INFORMSJoC_2024.0709/src/instance_generator_grb.py` line 1139; license file: MIT.

### `pandas.merge`

Used in 72 of 864 Python papers (8%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 72 papers): `how` 88%, `on` 85%, `left_on` 29%, `right_on` 26%, `right_index` 11%, `indicator` 10%, `left_index` 10%, `validate` 8%, `left` 7%, `right` 7%.

Most common option set: `how`, `on`; at least one call in 48 papers (67%).

```python
ccm1=pd.merge(comp,ccm,how='left',on=['gvkey'])
```
RFS 2026, [doi:10.1093/rfs/hhag042](https://doi.org/10.1093/rfs/hhag042), `code/dataverse_BO8SQ8/programs/programs/00_preparation/download_data_sets/download_dgtw_return.py` line 161; license file: BSD.

Next most common option set: `on`; at least one call in 18 papers (25%).

```python
        df2 = pd.merge(df2, df, on="instance")
```
IJOC 2025, [doi:10.1287/ijoc.2023.0021](https://doi.org/10.1287/ijoc.2023.0021), `code/github_INFORMSJoC_2023.0021/codes/results/result_utils.py` line 209; license file: GPL.

### `pandas.read_csv().merge`

Used in 32 of 864 Python papers (4%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 32 papers): `on` 91%, `how` 88%, `left_on` 19%, `right_on` 19%, `validate` 12%, `suffixes` 6%.

Most common option set: `how`, `on`; at least one call in 24 papers (75%).

```python
    df = df.merge(cot, on="SEQN", how="inner") if "SEQN" in df.columns else df
```
JASA 2024, [doi:10.1080/01621459.2023.2191817](https://doi.org/10.1080/01621459.2023.2191817), `code/github_bilel-hatmi_proximal-causal-inference/simulations/datasets/process_datasets.py` line 308; license file: MIT.

Next most common option set: `how`, `left_on`, `right_on`; at least one call in 5 papers (16%).

```python
        users_2 = users_2.merge(if_visit, left_on='user', right_on='id', how='left')
```
ReStud 2025, [doi:10.1093/restud/rdad113](https://doi.org/10.1093/restud/rdad113), `code/zenodo_10020030/migration_networks_replication-main/migration_networks_replication-main/tables/table_A7_step2_visit_before.py` line 100.

### `pandas.DataFrame().merge`

Used in 26 of 864 Python papers (3%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 26 papers): `on` 81%, `how` 73%, `right_index` 23%, `left_index` 15%, `validate` 8%, `left_on` 8%.

Most common option set: `how`, `on`; at least one call in 14 papers (54%).

```python
    df = df.merge(aux, on='n', how='left')
```
MPC 2026, [doi:10.1007/s12532-025-00298-8](https://doi.org/10.1007/s12532-025-00298-8), `code/github_febattista_SDP_lift_and_project/scripts/analyze_results.py` line 160; license file: GPL.

Next most common option set: `on`; at least one call in 5 papers (19%).

```python
    _temp=_temp.merge(temp_zc,on=['date'])
```
AER 2025, [doi:10.1257/aer.20230486](https://doi.org/10.1257/aer.20230486), `code/Code/appendix_results2.ipynb` cell 1, line 72.

### `pandas.concat().drop_duplicates`

Used in 22 of 864 Python papers (3%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 22 papers): `subset` 68%, `keep` 50%, `inplace` 36%.

Most common option set: none; at least one call in 9 papers (41%).

```python
fundus = fundus.drop_duplicates()
```
JASA 2026, [doi:10.1080/01621459.2026.2644611](https://doi.org/10.1080/01621459.2026.2644611), `code/github_langzeng_mb-MPLE/AREDS_Preprocessing/areds_longitudinal.py` line 10.

Next most common option set: `subset`; at least one call in 6 papers (27%).

```python
        pd.concat(all_data, ignore_index=True)
        .drop_duplicates(subset=['date'])
```
JRSSB 2022, [doi:10.1111/rssb.12448](https://doi.org/10.1111/rssb.12448), `code/github_tsaiyachih_london-ulez-air-quality/scripts/01_download_era5_weather.py` lines 296-297; license file: MIT.

### `pandas.read_csv().drop_duplicates`

Used in 22 of 864 Python papers (3%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 22 papers): `subset` 64%, `inplace` 27%, `keep` 27%.

Most common option set: none; at least one call in 8 papers (36%).

```python
        timestamp = timestamp.drop_duplicates()
```
RFS 2026, [doi:10.1093/rfs/hhag002](https://doi.org/10.1093/rfs/hhag002), `code/dataverse_ZAKR8C/code.tar/code/get-block-timestamp.py` line 33.

Next most common option set: `subset`; at least one call in 7 papers (32%).

```python
                out_df = df.drop_duplicates(subset=["2"])
```
IJOC 2026, [doi:10.1287/ijoc.2024.0660](https://doi.org/10.1287/ijoc.2024.0660), `code/github_INFORMSJoC_2024.0660/src/runtimex.py` line 81; license file: MIT.

### `pandas.merge().drop`

Used in 21 of 864 Python papers (2%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 21 papers): `axis` 71%, `inplace` 48%, `columns` 48%.

Most common option set: `axis`, `inplace`; at least one call in 7 papers (33%).

```python
				df.drop([var], axis=1, inplace=True)
```
ReStud 2026, [doi:10.1093/restud/rdag063](https://doi.org/10.1093/restud/rdag063), `code/zenodo_18464228/replication_package_archive1/codes/3_model/config.py` line 272.

Next most common option set: `axis`; at least one call in 7 papers (33%).

```python
    crsp1=crsp1.drop(['me'], axis=1)
```
JPE 2026, [doi:10.1086/740220](https://doi.org/10.1086/740220), `code/dataverse_2QAGRH/DataCode/CCM.py` line 147.

### `pandas.concat().merge`

Used in 19 of 864 Python papers (2%) — Powerful data structures for data analysis, time series, and statistics.

Options (share of these 19 papers): `how` 84%, `on` 68%, `left_on` 32%, `right_on` 21%, `right_index` 16%, `indicator` 11%, `validate` 11%.

Most common option set: `how`, `on`; at least one call in 11 papers (58%).

```python
    data = data.merge(deep_preds, on='ReportID', how='left')        
```
IJOC 2025, [doi:10.1287/ijoc.2024.0835](https://doi.org/10.1287/ijoc.2024.0835), `code/github_INFORMSJoC_2024.0835/scripts/6-RankEvaluation/EvaluationFunc.py` line 76; license file: MIT.

Next most common option set: `how`, `left_on`, `right_on`; at least one call in 3 papers (16%).

```python
ltbl = ltbl.merge(
    open_banking_coding,
    how='left',
    left_on=['ISO3'],
    right_on=['country_code'])
```
JFE 2025, [doi:10.1016/j.jfineco.2024.103950](https://doi.org/10.1016/j.jfineco.2024.103950), `code/mendeley_v66vpgwbv8_v1/Pitchbook and Cross Country Analysis/pb_and_cross_country_tables_and_figures.py` lines 50-54.
