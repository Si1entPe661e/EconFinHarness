# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

## Inference options of estimation commands

### `statsmodels.api.OLS().fit`

Used in 44 of 864 Python papers (5%) — Statistical computations and models for Python.

Inference options (share of these 44 papers): `cov_type` 23%, `cov_kwds` 16%.

Most common option set: none; at least one call in 38 papers (86%).

```python
        model_l = sm.OLS(y, x).fit()
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf067](https://doi.org/10.1093/jrsssb/qkaf067), `code/github_fschur_robust_deconfounding/experiments/utils_experiments.py` line 86; license file: MIT.

Next most common option set: `cov_kwds`, `cov_type`; at least one call in 7 papers (16%).

```python
    tval = sm.OLS(hl["H-L"], hl["const"]).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags}).tvalues["const"]
```
RFS 2026, [doi:10.1093/rfs/hhag042](https://doi.org/10.1093/rfs/hhag042), `code/dataverse_BO8SQ8/programs/programs/02_analysis/helper.py` line 734; license file: BSD.
