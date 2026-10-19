# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `Base.Dict`

Used in 90 of 164 Julia papers (55%) — `Dict{K,V}()` constructs a hash table with keys of type `K` and values of type `V`.

Most common option set: none; at least one call in 90 papers (100%).

```julia
    return Dict()#"time_limit" => tilim,
```
IJOC 2026, [doi:10.1287/ijoc.2022.0221](https://doi.org/10.1287/ijoc.2022.0221), `code/github_INFORMSJoC_2022.0221/src/minlpsolvers.jl` line 62; license file: MIT.

### `Plots.savefig`

Used in 54 of 164 Julia papers (33%) — Save a Plot (the current plot if `plot` is not passed) to file.

Most common option set: none; at least one call in 54 papers (100%).

```julia
        savefig(fp, filename)
```
MPC 2026, [doi:10.1007/s12532-026-00340-3](https://doi.org/10.1007/s12532-026-00340-3), `code/github_GioniMexi_FW-MIQCQP-Heuristic/FrankWolfe.jl/examples/plot_utils.jl` line 202; license file: MIT.

### `LaTeXStrings.@L_str`

Used in 38 of 164 Julia papers (23%) — The LaTeXStrings module exists mainly to make LaTeX equations easier to type as literal strings, and so that the resulting strings display as ....

Most common option set: none; at least one call in 38 papers (100%).

```julia
	labels["dd_w010"] = "DD " * L"W=10"
```
IJOC 2026, [doi:10.1287/ijoc.2024.0686](https://doi.org/10.1287/ijoc.2024.0686), `code/github_INFORMSJoC_2024.0686/results/CombPricingDP-Interdiction-Grouping.jl` line 54; license file: MIT.

### `DataAPI.nrow`

Used in 27 of 164 Julia papers (16%) — Return the number of rows of table `t`.

Most common option set: none; at least one call in 27 papers (100%).

```julia
        df[!, col] = fill(fill_element, nrow(df))
```
MPC 2026, [doi:10.1007/s12532-026-00315-4](https://doi.org/10.1007/s12532-026-00315-4), `code/github_zavalab_PlasmoBendersExamples/CS2/GenX.jl/src/load_inputs/load_fuels_data.jl` line 47; license file: GPL.

### `Plots.annotate!`

Used in 15 of 164 Julia papers (9%) — Add annotations to an existing plot.

Options (share of these 15 papers): `color` 13%.

Most common option set: none; at least one call in 14 papers (93%).

```julia
    annotate!(x, y, t)
```
Econometrica 2026, [doi:10.3982/ecta23125](https://doi.org/10.3982/ecta23125), `code/zenodo_17903904/HMS_foodpolicy/HMS_foodpolicy/code/quantification/Fig.jl` line 25.

### `Plots.text`

Used in 13 of 164 Julia papers (8%) — Create a PlotText object wrapping a string with font info, for plot annotations.

Most common option set: none; at least one call in 12 papers (92%).

```julia
annotate!_(c,a,l) = annotate!((2017.5, co2(c).co2[end]+a, text(l, ts..., navy3)))
```
Econometrica 2026, [doi:10.3982/ecta20608](https://doi.org/10.3982/ecta20608), `code/zenodo_17430585/Hsiao_palmoil/Hsiao_palmoil/code/sumstats/emissions.jl` line 37.

### `Graphs.add_edge!`

Used in 9 of 164 Julia papers (5%) — The goal of *Graphs.jl* is to offer a performant platform for network and graph analysis in Julia, following the example of libraries such as ....

Most common option set: none; at least one call in 9 papers (100%).

```julia
                add_edge!(T,e)
```
IJOC 2026, [doi:10.1287/ijoc.2022.0295](https://doi.org/10.1287/ijoc.2022.0295), `code/github_INFORMSJoC_2022.0295/src/mrt_solution_algorithms.jl` line 336; license file: MIT.

### `Plots.plot`

Used in 8 of 164 Julia papers (5%) — Extract a subplot from an existing plot.

Options (share of these 8 papers): `label` 75%, `legend` 62%, `color` 50%, `xlabel` 50%, `ylabel` 50%, `layout` 25%, `size` 25%, `width` 25%, `xaxis` 25%, `yaxis` 25%.

Most common option set: `label`; at least one call in 3 papers (38%).

```julia
Plots.plot(x_domain, true_function.(x_domain); label = "truth")
```
IJOC 2026, [doi:10.1287/ijoc.2025.1446](https://doi.org/10.1287/ijoc.2025.1446), `code/github_INFORMSJoC_2025.1446/docs/src/tutorials/gaussian.jl` line 30; license file: BSD.

Next most common option set: none; at least one call in 2 papers (25%).

```julia
    Plots.plot(x -> rhs_EEm(x, fun_psi_ss(x)), 0.0, 10.0)
```
JPE 2024, [doi:10.1086/726904](https://doi.org/10.1086/726904), `code/dataverse_WM2VSE/QMT_model_replication.jl` line 70.
