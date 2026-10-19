# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `scipy.optimize.minimize`

Used in 71 of 864 Python papers (8%) — Fundamental algorithms for scientific computing in Python.

Options (share of these 71 papers): `method` 82%, `bounds` 54%, `jac` 42%, `options` 42%, `args` 32%, `constraints` 32%, `x0` 17%, `tol` 15%, `callback` 7%, `fun` 7%.

Most common option set: `bounds`, `constraints`, `method`; at least one call in 5 papers (7%).

```python
    res = minimize(obj, x0, bounds=bounds, constraints=cons, method='SLSQP')
```
IJOC 2026, [doi:10.1287/ijoc.2025.1570](https://doi.org/10.1287/ijoc.2025.1570), `code/github_INFORMSJoC_2025.1570/src/optimization.py` line 218; license file: MIT.

### `cvxpy.Minimize`

Used in 22 of 864 Python papers (3%) — A domain-specific language for modeling convex optimization problems in Python.

Most common option set: none; at least one call in 22 papers (100%).

```python
        prob = cp.Problem(cp.Minimize(0), constrs)
```
IJOC 2026, [doi:10.1287/ijoc.2025.1177](https://doi.org/10.1287/ijoc.2025.1177), `code/github_INFORMSJoC_2025.1177/src/LMI/lmi_pmm_abm.py` line 97; license file: Apache-2.0.

### `scipy.optimize.minimize_scalar`

Used in 16 of 864 Python papers (2%) — Fundamental algorithms for scientific computing in Python.

Options (share of these 16 papers): `method` 88%, `bounds` 81%, `options` 19%, `args` 12%.

Most common option set: `bounds`, `method`; at least one call in 8 papers (50%).

```python
        result = minimize_scalar(h, bounds=(eps, u0_upper - eps), method='bounded')
```
IJOC 2026, [doi:10.1287/ijoc.2025.1134](https://doi.org/10.1287/ijoc.2025.1134), `code/github_INFORMSJoC_2025.1134/src/main.py` line 282; license file: MIT.

Next most common option set: `bounds`, `method`, `options`; at least one call in 3 papers (19%).

```python
    a_k = minimize_scalar(myobj, bounds=[a, b], method='Bounded',
                          options=options).x
```
MPC 2023, [doi:10.1007/s12532-023-00242-8](https://doi.org/10.1007/s12532-023-00242-8), `code/github_bowmnath_mvee/mvee.py` lines 1286-1287; license file: MIT.
