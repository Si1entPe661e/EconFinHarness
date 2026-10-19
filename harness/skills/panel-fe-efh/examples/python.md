# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `linearmodels.PanelOLS`

Used in 8 of 864 Python papers (0.9%) — Linear Panel, Instrumental Variable, Asset Pricing, and System Regression models for Python.

Options (share of these 8 papers): `entity_effects` 100%, `time_effects` 100%, `weights` 38%, `drop_absorbed` 25%, `other_effects` 25%.

Most common option set: `entity_effects`, `time_effects`; at least one call in 4 papers (50%).

```python
    mod = PanelOLS(y, x, entity_effects=True, time_effects = True)
```
RFS 2026, [doi:10.1093/rfs/hhag042](https://doi.org/10.1093/rfs/hhag042), `code/dataverse_BO8SQ8/programs/programs/02_analysis/analysis_predicting_suv_turnover_hv.py` line 117; license file: BSD.

Next most common option set: `drop_absorbed`, `entity_effects`, `time_effects`; at least one call in 2 papers (25%).

```python
    modelols = PanelOLS(input_data[yvar],input_data[xvars_copy],
                        entity_effects=entityfe,
                        time_effects=timefe,
                        drop_absorbed=drop_absorbed)
```
MS 2026, [doi:10.1287/mnsc.2024.05808](https://doi.org/10.1287/mnsc.2024.05808), `code/mendeley_2pg764w6gs_v1/7 MS Replication Package/support.py` lines 155-158.

### `linearmodels.PanelOLS().fit`

Used in 8 of 864 Python papers (0.9%) — Linear Panel, Instrumental Variable, Asset Pricing, and System Regression models for Python.

Options (share of these 8 papers): `cov_type` 100%, `cluster_entity` 88%, `cluster_time` 50%.

Most common option set: `cluster_entity`, `cluster_time`, `cov_type`; at least one call in 3 papers (38%).

```python
    mod = PanelOLS(data_reg['mapbiomas'], data_reg[['no_degradation','degradation','severe_degradation',
                                                    'Gaez_maize_high_rain','Gaez_soy_high_rain',
                                                    'Gaez_PSI','Cost_from_raster']],
                   entity_effects=False, time_effects=True).fit(cov_type='clustered', cluster_entity=True, cluster_time=False)
```
ReStud 2026, [doi:10.1093/restud/rdaf031](https://doi.org/10.1093/restud/rdaf031), `code/zenodo_14549060/package_EfficientConservation/package_EfficientConservation/Code/Degradation_regeneration.py` lines 106-109.

Next most common option set: `cluster_entity`, `cov_type`; at least one call in 3 papers (38%).

```python
res = mod.fit(cov_type='clustered', cluster_entity=True)
```
JFE 2025, [doi:10.1016/j.jfineco.2025.104062](https://doi.org/10.1016/j.jfineco.2025.104062), `code/mendeley_g8bjhvyzwj_v2/code/JFE_Code_Table6a.py` line 59.

### `PanelOLS().fit`

Used in 7 of 864 Python papers (0.8%).

Options (share of these 7 papers): `cov_type` 100%, `cluster_entity` 86%, `cluster_time` 43%, `low_memory` 29%.

Most common option set: `cluster_entity`, `cov_type`; at least one call in 3 papers (43%).

```python
            result = model.fit(cov_type='clustered', cluster_entity=True)
```
RFS 2025, [doi:10.1093/rfs/hhaf046](https://doi.org/10.1093/rfs/hhaf046), `code/dataverse_3KZHG9/replication_code.tar/replication_code/code/02_main_analysis.ipynb` cell 8, line 30.

Next most common option set: `cluster_entity`, `cluster_time`, `cov_type`; at least one call in 2 papers (29%).

```python
    res = res.fit(cov_type='clustered',
                    cluster_entity=True, cluster_time=True)
```
RFS 2024, [doi:10.1093/rfs/hhae047](https://doi.org/10.1093/rfs/hhae047), `code/dataverse_KPAM5B/Replication_Package_Gulen_Ion_Jens_Rossi_2024/Code/PYTHON/7_Table3_PanelA.ipynb` cell 7, lines 12-13.
