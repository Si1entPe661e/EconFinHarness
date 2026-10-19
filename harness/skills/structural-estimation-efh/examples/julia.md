# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `Base.findmin`

Used in 25 of 164 Julia papers (15%) — For an array input, returns the value in the codomain and index of the corresponding value which minimize `f` over the given dimensions.

Options (share of these 25 papers): `dims` 8%.

Most common option set: none; at least one call in 23 papers (92%).

```julia
    d = c[findmin(degree_list)[2]]
```
MPC 2026, [doi:10.1007/s12532-026-00307-4](https://doi.org/10.1007/s12532-026-00307-4), `code/github_foreverdyz_ParallelCliqueMerge/src/generate_cliques/clique_extension.jl` line 86; license file: GPL.

### `JuMP.optimizer_with_attributes`

Used in 19 of 164 Julia papers (12%) — Groups an optimizer constructor with the list of attributes `attrs`.

Most common option set: none; at least one call in 19 papers (100%).

```julia
    println(JuMP.optimizer_with_attributes(GLPK.Optimizer))
```
IJOC 2026, [doi:10.1287/ijoc.2025.1130](https://doi.org/10.1287/ijoc.2025.1130), `code/github_INFORMSJoC_2025.1130/test/old/optimizer_with_attributes_test.jl` line 5; license file: GPL.

### `Gurobi.Optimizer`

Used in 15 of 164 Julia papers (9%) — Create a new Optimizer object.

Most common option set: none; at least one call in 15 papers (100%).

```julia
    model = direct_model(Gurobi.Optimizer())
```
IJOC 2026, [doi:10.1287/ijoc.2022.0221](https://doi.org/10.1287/ijoc.2022.0221), `code/github_INFORMSJoC_2022.0221/src/example.jl` line 49; license file: MIT.

### `JuMP.set_optimizer`

Used in 14 of 164 Julia papers (9%) — Creates an empty `MOI.AbstractOptimizer` instance by calling `MOI.instantiate` on `optimizer_factory` and sets it as the optimizer of `model`.

Options (share of these 14 papers): `add_bridges` 14%.

Most common option set: none; at least one call in 14 papers (100%).

```julia
    set_optimizer(model, OSQP.Optimizer)
```
MPC 2026, [doi:10.1007/s12532-025-00301-2](https://doi.org/10.1007/s12532-025-00301-2), `code/github_tjdiamandis_GeNIOSExperiments.jl/experiments/1-elastic-net-compare.jl` line 81; license file: MIT.

### `MathOptInterface.get`

Used in 13 of 164 Julia papers (8%) — Return an attribute `attr` of the optimizer `optimizer`.

Most common option set: none; at least one call in 13 papers (100%).

```julia
          sort(MOI.get(uno, attr); by = string)
```
MPC 2026, [doi:10.1007/s12532-026-00310-9](https://doi.org/10.1007/s12532-026-00310-9), `code/github_cvanaret_Uno/interfaces/Julia/test/MOI_wrapper.jl` line 202; license file: MIT.

### `MathOptInterface.set`

Used in 13 of 164 Julia papers (8%) — Assign `value` to the attribute `attr` of the optimizer `optimizer`.

Most common option set: none; at least one call in 13 papers (100%).

```julia
    MOI.set(model, attr, "off")
```
IJOC 2026, [doi:10.1287/ijoc.2025.1449](https://doi.org/10.1287/ijoc.2025.1449), `code/github_INFORMSJoC_2025.1449/test/test_model.jl` line 138; license file: GPL.

### `MathOptInterface.Model`

Used in 11 of 164 Julia papers (7%) — An abstraction layer for mathematical optimization solvers.

Options (share of these 11 papers): `filename` 45%, `format` 27%.

Most common option set: none; at least one call in 9 papers (82%).

```julia
        MOI.Utilities.UniversalFallback(MOI.Utilities.Model{Float64}()),
```
MPC 2026, [doi:10.1007/s12532-026-00340-3](https://doi.org/10.1007/s12532-026-00340-3), `code/github_GioniMexi_FW-MIQCQP-Heuristic/FrankWolfe.jl/src/moi_oracle.jl` line 283; license file: MIT.

Next most common option set: `filename`; at least one call in 4 papers (36%).

```julia
        MOI.FileFormats.Model(filename = "a.b")
```
IJOC 2022, [doi:10.1287/ijoc.2021.1067](https://doi.org/10.1287/ijoc.2021.1067), `code/github_jump-dev_MathOptInterface.jl/test/FileFormats/test_FileFormats.jl` line 143; license file: MIT.

### `MathOptInterface.ObjectiveSense`

Used in 10 of 164 Julia papers (6%) — An `AbstractModelAttribute` for the objective sense of the objective function, which must be an `OptimizationSense`.

Most common option set: none; at least one call in 10 papers (100%).

```julia
    lower_sense = MOI.get(lower, MOI.ObjectiveSense())
```
IJOC 2024, [doi:10.1287/ijoc.2022.0135](https://doi.org/10.1287/ijoc.2022.0135), `code/github_INFORMSJoC_2022.0135/src/mibs.jl` line 71; license file: MIT.
