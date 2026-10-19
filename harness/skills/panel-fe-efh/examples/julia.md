# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `FixedEffectModels.fe`

Used in 7 of 164 Julia papers (4%) — Mark a variable as a high-dimensional fixed effect (a categorical variable to be absorbed) inside a `@formula` passed to `reg` or `partial_out`, e.g.

Most common option set: none; at least one call in 7 papers (100%).

```julia
    fe_reg = reg(df_, @formula(y ~ t + fe(m)), save=:fe)
```
Econometrica 2026, [doi:10.3982/ecta20608](https://doi.org/10.3982/ecta20608), `code/zenodo_17430585/Hsiao_palmoil/Hsiao_palmoil/code/data/yields.jl` line 10.
