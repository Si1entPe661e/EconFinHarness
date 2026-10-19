# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `StatsAPI.stderror`

Used in 10 of 164 Julia papers (6%) — Return the standard errors for the coefficients of the model.

Most common option set: none; at least one call in 10 papers (100%).

```julia
    stderror(rr)[findfirst(rr.coefnames .== string(x))]
```
RFS 2026, [doi:10.1093/rfs/hhaf062](https://doi.org/10.1093/rfs/hhaf062), `code/dataverse_GFCSRE/empirics/empirics/julia/functions_plots.jl` line 235.

## Inference options of estimation commands
