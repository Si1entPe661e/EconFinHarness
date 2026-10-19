# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `statsmodels.api.OLS`

Used in 44 of 864 Python papers (5%) — Statistical computations and models for Python.

Options (share of these 44 papers): `endog` 14%, `exog` 14%, `missing` 5%.

Most common option set: none; at least one call in 38 papers (86%).

```python
        model_l = sm.OLS(y, x).fit()
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf067](https://doi.org/10.1093/jrsssb/qkaf067), `code/github_fschur_robust_deconfounding/experiments/utils_experiments.py` line 86; license file: MIT.

### `statsmodels.api.OLS().fit`

Used in 44 of 864 Python papers (5%) — Statistical computations and models for Python.

Options (share of these 44 papers): `cov_type` 23%, `cov_kwds` 16%.

Most common option set: none; at least one call in 38 papers (86%).

```python
    Y_tilde = (sm.OLS(Y,reg_tmp).fit()).resid    
```
JRSSB 2026, [doi:10.1093/jrsssb/qkag077](https://doi.org/10.1093/jrsssb/qkag077), `code/github_hongzi2021_Uniformly-Bounded-Neighbourhood-Interference/empirical_school/empirical_school.py` line 80; license file: MIT.

Next most common option set: `cov_kwds`, `cov_type`; at least one call in 7 papers (16%).

```python
    tval = sm.OLS(hl["H-L"], hl["const"]).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags}).tvalues["const"]
```
RFS 2026, [doi:10.1093/rfs/hhag042](https://doi.org/10.1093/rfs/hhag042), `code/dataverse_BO8SQ8/programs/programs/02_analysis/helper.py` line 734; license file: BSD.

### `sklearn.linear_model.LinearRegression`

Used in 42 of 864 Python papers (5%) — deprecated sklearn package, use scikit-learn instead.

Options (share of these 42 papers): `fit_intercept` 38%.

Most common option set: none; at least one call in 28 papers (67%).

```python
                'beta': LinearRegression(),
```
IJOC 2026, [doi:10.1287/ijoc.2023.0130](https://doi.org/10.1287/ijoc.2023.0130), `code/github_INFORMSJoC_2023.0130/src/ml_sk_implementation.py` line 173; license file: MIT.

Next most common option set: `fit_intercept`; at least one call in 15 papers (36%).

```python
        reg = LinearRegression(fit_intercept=False).fit(np.array(X), np.array(y))
```
IJOC 2026, [doi:10.1287/ijoc.2023.0245](https://doi.org/10.1287/ijoc.2023.0245), `code/github_INFORMSJoC_2023.0245/src/ m = 5/ADP.py` line 365; license file: MIT.

### `sklearn.linear_model.LinearRegression().fit`

Used in 33 of 864 Python papers (4%) — deprecated sklearn package, use scikit-learn instead.

Most common option set: none; at least one call in 33 papers (100%).

```python
    model.fit(x, y)
```
IJOC 2026, [doi:10.1287/ijoc.2025.1353](https://doi.org/10.1287/ijoc.2025.1353), `code/github_INFORMSJoC_2025.1353/scripts/parallel_experiments.py` line 124; license file: MIT.

### `sklearn.linear_model.LogisticRegression`

Used in 32 of 864 Python papers (4%) — deprecated sklearn package, use scikit-learn instead.

Options (share of these 32 papers): `random_state` 50%, `max_iter` 50%, `solver` 41%, `C` 38%, `penalty` 34%, `multi_class` 16%, `class_weight` 12%, `fit_intercept` 9%, `n_jobs` 6%.

Most common option set: none; at least one call in 5 papers (16%).

```python
    valid_params = LogisticRegression().get_params().keys()
```
JASA 2025, [doi:10.1080/01621459.2025.2468014](https://doi.org/10.1080/01621459.2025.2468014), `code/github_jaydu1_CausalMultiOutcomes/causarray/estimation.py` line 361; license file: MIT.

Next most common option set: `max_iter`; at least one call in 5 papers (16%).

```python
    LR = LogisticRegression(max_iter=1000)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0488](https://doi.org/10.1287/ijoc.2023.0488), `code/github_INFORMSJoC_2023.0488/src/Machine_Learning_Methods_for_Predictive_Modeling.py` line 100; license file: MIT.

### `statsmodels.formula.api.ols`

Used in 23 of 864 Python papers (3%) — Statistical computations and models for Python.

Options (share of these 23 papers): `data` 91%, `formula` 61%.

Most common option set: `data`, `formula`; at least one call in 14 papers (61%).

```python
            model = smf.ols(formula=formula, data=panel)
```
ReStud 2026, [doi:10.1093/restud/rdag047](https://doi.org/10.1093/restud/rdag047), `code/zenodo_19175276/Replication_Package_260506/Replication_Package_260416_restud_rev1/synthetic_replication/DGP Code/Synthetic Other Steel Plant Data - TableA1.py` line 298.

Next most common option set: `data`; at least one call in 11 papers (48%).

```python
fit = ols('NDEXP ~ C(FAM_SIZE) + INT_DATE_COPY ', data=df[df['Wave_filter']==1]).fit() #data=df[df['Wave_filter']==1]
```
QJE 2025, [doi:10.1093/qje/qjaf015](https://doi.org/10.1093/qje/qjaf015), `code/dataverse_N7534Z/MPC2008-Public-main_psmjsample_code/psmjsample.py` line 41; license file: GPL.

### `statsmodels.formula.api.ols().fit`

Used in 23 of 864 Python papers (3%) — Statistical computations and models for Python.

Options (share of these 23 papers): `cov_type` 52%, `cov_kwds` 30%, `use_t` 13%.

Most common option set: none; at least one call in 20 papers (87%).

```python
    model =smf.ols(function, data= temp).fit()
```
AER 2023, [doi:10.1257/aer.20210434](https://doi.org/10.1257/aer.20210434), `code/scripts_python/floor_effect/utils.py` line 41; license file: BSD.

Next most common option set: `cov_kwds`, `cov_type`; at least one call in 6 papers (26%).

```python
    results = model.fit(cov_type='cluster', cov_kwds={'groups': df['event_id']})
```
ReStud 2026, [doi:10.1093/restud/rdaf037](https://doi.org/10.1093/restud/rdaf037), `code/zenodo_14927953/RBE_replicationpackage_20250327/Analysis/code/RBE_03.py` line 1823.

### `sklearn.linear_model.LogisticRegression().fit`

Used in 22 of 864 Python papers (3%) — deprecated sklearn package, use scikit-learn instead.

Most common option set: none; at least one call in 21 papers (95%).

```python
        clf = clf.fit(X_scaled, y)
```
IJOC 2026, [doi:10.1287/ijoc.2025.1189](https://doi.org/10.1287/ijoc.2025.1189), `code/github_INFORMSJoC_2025.1189/predictive-python/fbvrptw/early_arrival_prob/early_arrival_prob.py` line 199; license file: MIT.
