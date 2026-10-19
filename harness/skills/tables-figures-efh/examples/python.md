# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `matplotlib.pyplot.subplots`

Used in 248 of 864 Python papers (29%) — Python plotting package.

Options (share of these 248 papers): `figsize` 83%, `sharex` 17%, `sharey` 13%, `nrows` 8%, `ncols` 8%, `dpi` 6%, `gridspec_kw` 5%, `constrained_layout` 4%, `tight_layout` 3%, `squeeze` 2%.

Most common option set: `figsize`; at least one call in 166 papers (67%).

```python
fig, ax = plt.subplots(figsize=(4,3))
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf056](https://doi.org/10.1093/jrsssb/qkaf056), `code/github_lx10077_TrGoF/simulation_codes/contour_TrGoF.py` line 144; license file: MIT.

Next most common option set: none; at least one call in 62 papers (25%).

```python
fig, ax = plt.subplots()
```
IJOC 2026, [doi:10.1287/ijoc.2023.0474](https://doi.org/10.1287/ijoc.2023.0474), `code/github_INFORMSJoC_2023.0474/scripts/tests.py` line 40; license file: MIT.

### `matplotlib.pyplot.savefig`

Used in 232 of 864 Python papers (27%) — Python plotting package.

Options (share of these 232 papers): `bbox_inches` 49%, `dpi` 39%, `format` 15%, `pad_inches` 4%, `transparent` 3%, `**` 0.9%, `facecolor` 0.9%.

Most common option set: none; at least one call in 102 papers (44%).

```python
        plt.savefig(out)
```
IJOC 2026, [doi:10.1287/ijoc.2024.0595](https://doi.org/10.1287/ijoc.2024.0595), `code/github_INFORMSJoC_2024.0595/src/9_Interpretability/Standard_SHAP/main.py` line 151; license file: MIT.

Next most common option set: `bbox_inches`; at least one call in 63 papers (27%).

```python
        plt.savefig(outpath, bbox_inches='tight')
```
MPC 2026, [doi:10.1007/s12532-025-00294-y](https://doi.org/10.1007/s12532-025-00294-y), `code/github_dominicflocco_spdca/utils/utils.py` line 413; license file: MIT.

### `matplotlib.pyplot.figure`

Used in 210 of 864 Python papers (24%) — Python plotting package.

Options (share of these 210 papers): `figsize` 82%, `dpi` 8%, `constrained_layout` 1%, `tight_layout` 1.0%, `facecolor` 1.0%, `frameon` 1.0%.

Most common option set: `figsize`; at least one call in 157 papers (75%).

```python
    plt.figure(figsize=(5,4))
```
IJOC 2026, [doi:10.1287/ijoc.2024.1005](https://doi.org/10.1287/ijoc.2024.1005), `code/github_INFORMSJoC_2024.1005/src/CG_Main.py` line 439; license file: MIT.

Next most common option set: none; at least one call in 61 papers (29%).

```python
    fig = plt.figure()
```
IJOC 2026, [doi:10.1287/ijoc.2023.0068](https://doi.org/10.1287/ijoc.2023.0068), `code/github_INFORMSJoC_2023.0068/src/UTILS.py` line 340; license file: GPL.

### `matplotlib.pyplot.show`

Used in 203 of 864 Python papers (23%) — Python plotting package.

Options (share of these 203 papers): `block` 3%.

Most common option set: none; at least one call in 198 papers (98%).

```python
plt.show()
```
IJOC 2026, [doi:10.1287/ijoc.2023.0048](https://doi.org/10.1287/ijoc.2023.0048), `code/github_INFORMSJoC_2023.0048/scripts/AdditionalLaTeXFigures.py` line 239; license file: MIT.

### `matplotlib.pyplot.legend`

Used in 180 of 864 Python papers (21%) — Python plotting package.

Options (share of these 180 papers): `loc` 53%, `fontsize` 28%, `bbox_to_anchor` 17%, `frameon` 11%, `ncol` 10%, `title` 7%, `handles` 6%, `prop` 4%, `framealpha` 3%, `labels` 3%.

Most common option set: none; at least one call in 102 papers (57%).

```python
plt.legend()
```
IJOC 2026, [doi:10.1287/ijoc.2023.0130](https://doi.org/10.1287/ijoc.2023.0130), `code/github_INFORMSJoC_2023.0130/scripts/visualization.py` line 23; license file: MIT.

Next most common option set: `loc`; at least one call in 43 papers (24%).

```python
    plt.legend(loc=2)
```
IJOC 2026, [doi:10.1287/ijoc.2024.0886](https://doi.org/10.1287/ijoc.2024.0886), `code/github_INFORMSJoC_2024.0886/src/tactical_design_sdd/figure_functions.py` line 262; license file: MIT.

### `matplotlib.pyplot.xlabel`

Used in 178 of 864 Python papers (21%) — Python plotting package.

Options (share of these 178 papers): `fontsize` 35%, `size` 2%, `fontweight` 2%, `labelpad` 1%, `**` 1%, `fontdict` 1%.

Most common option set: none; at least one call in 137 papers (77%).

```python
plt.xlabel("x")
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf067](https://doi.org/10.1093/jrsssb/qkaf067), `code/github_fschur_robust_deconfounding/experiments/mueller.py` line 69; license file: MIT.

Next most common option set: `fontsize`; at least one call in 58 papers (33%).

```python
plt.xlabel('Rows', fontsize=14)
```
IJOC 2026, [doi:10.1287/ijoc.2024.0736](https://doi.org/10.1287/ijoc.2024.0736), `code/github_INFORMSJoC_2024.0736/scripts/Exp-plot_cluvrp.ipynb` cell 3, line 22; license file: MIT.

### `matplotlib.pyplot.ylabel`

Used in 178 of 864 Python papers (21%) — Python plotting package.

Options (share of these 178 papers): `fontsize` 37%, `size` 2%, `fontweight` 2%, `rotation` 2%, `labelpad` 2%, `color` 1%, `**` 1%, `fontdict` 1%.

Most common option set: none; at least one call in 135 papers (76%).

```python
plt.ylabel('F1')
```
IJOC 2026, [doi:10.1287/ijoc.2023.0514](https://doi.org/10.1287/ijoc.2023.0514), `code/github_INFORMSJoC_2023.0514/results/plot_curve.ipynb` cell 13, line 18; license file: MIT.

Next most common option set: `fontsize`; at least one call in 58 papers (33%).

```python
    plt.ylabel(r'Time (s)',fontsize = 20)
```
IJOC 2026, [doi:10.1287/ijoc.2024.0776](https://doi.org/10.1287/ijoc.2024.0776), `code/github_INFORMSJoC_2024.0776/Denoising/QR_code_denoising.ipynb` cell 18, line 137; license file: MIT.

### `matplotlib.pyplot.plot`

Used in 167 of 864 Python papers (19%) — Python plotting package.

Options (share of these 167 papers): `label` 67%, `color` 50%, `linewidth` 32%, `linestyle` 31%, `marker` 23%, `alpha` 12%, `markersize` 11%, `lw` 7%, `ls` 5%, `markevery` 5%.

Most common option set: none; at least one call in 72 papers (43%).

```python
        plt.plot(KX,Z)
```
JASA 2026, [doi:10.1080/01621459.2025.2573523](https://doi.org/10.1080/01621459.2025.2573523), `code/github_ucsf-deb_bifs/bifs/bifs_util/util.py` line 205; license file: BSD.

Next most common option set: `label`; at least one call in 53 papers (32%).

```python
            plt.plot(x[:, 0], x[:, 1], '.r', label='X')
```
JASA 2026, [doi:10.1080/01621459.2025.2610033](https://doi.org/10.1080/01621459.2025.2610033), `code/figshare_31049466/code/code/other_tests/private_me/data.py` line 38; license file: MIT.
