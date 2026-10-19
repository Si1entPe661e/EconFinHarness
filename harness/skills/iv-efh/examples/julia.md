# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

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
