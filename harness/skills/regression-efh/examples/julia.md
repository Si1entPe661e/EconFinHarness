# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `GLM.lm`

Used in 12 of 164 Julia papers (7%) — Fit a linear model to data.

Options (share of these 12 papers): `wts` 25%.

Most common option set: none; at least one call in 10 papers (83%).

```julia
    model_glm = GLM.lm(X, Y)
```
IJOC 2026, [doi:10.1287/ijoc.2025.1446](https://doi.org/10.1287/ijoc.2025.1446), `code/github_INFORMSJoC_2025.1446/test/test_GLM.jl` line 34; license file: BSD.

Next most common option set: `wts`; at least one call in 3 papers (25%).

```julia
    fit = lm(term(Y) ~ term(X), d̄, wts=wt)
```
Econometrica 2026, [doi:10.3982/ecta23125](https://doi.org/10.3982/ecta23125), `code/zenodo_17903904/HMS_foodpolicy/HMS_foodpolicy/code/quantification/Fig.jl` line 41.

### `Distributions.Poisson`

Used in 9 of 164 Julia papers (5%) — A *Poisson distribution* describes the number of independent events occurring within a unit time interval, given the average rate of occurrence `λ`.

Most common option set: none; at least one call in 9 papers (100%).

```julia
    sample=rand(Poisson(lamda[i,j,d,t]),E)
```
IJOC 2026, [doi:10.1287/ijoc.2024.1086](https://doi.org/10.1287/ijoc.2024.1086), `code/github_INFORMSJoC_2024.1086/src/SAAandRO.ipynb` cell 7, line 90; license file: MIT.

### `FixedEffectModels.reg`

Used in 7 of 164 Julia papers (4%) — Estimate a linear model with high dimensional categorical variables / instrumental variables.

Options (share of these 7 papers): `save` 43%, `weights` 29%.

Most common option set: none; at least one call in 5 papers (71%).

```julia
    model = reg(filter(row -> row.AOM in Set([i for i in 0:18]), tb), formula)
```
QJE 2026, [doi:10.1093/qje/qjag009](https://doi.org/10.1093/qje/qjag009), `code/dataverse_SDOODF/_conf_displ_humcap_public/code/2_analysis/_old/FIG_D2_D3_gio_path.jl` line 72.

Next most common option set: `save`, `weights`; at least one call in 2 papers (29%).

```julia
        rr_y = reg(df, ff.lhs ~ rhs_res; weights=w, save=:residuals)
```
RFS 2026, [doi:10.1093/rfs/hhaf062](https://doi.org/10.1093/rfs/hhaf062), `code/dataverse_GFCSRE/empirics/empirics/julia/functions_plots.jl` line 177.
