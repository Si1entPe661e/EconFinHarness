# Julia examples from published replication packages

Commands and functions related to this skill, as written in the author code of 164 Julia replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `Core.Array`

Used in 74 of 164 Julia papers (45%) — Construct an `N`-dimensional `Array` containing elements of type `T`, initialized with `missing` entries.

Most common option set: none; at least one call in 74 papers (100%).

```julia
    caps = Array{Int64, 1}()
```
IJOC 2026, [doi:10.1287/ijoc.2022.0221](https://doi.org/10.1287/ijoc.2022.0221), `code/github_INFORMSJoC_2022.0221/src/instance_reader.jl` line 332; license file: MIT.

### `Base.unique`

Used in 72 of 164 Julia papers (44%) — Return unique regions of `A` along dimension `dims`.

Options (share of these 72 papers): `dims` 3%.

Most common option set: none; at least one call in 72 papers (100%).

```julia
               if A[j, e[1]] == 1 && A[j, e[2]] == 1 && (length(unique(v3)) == 3)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0236](https://doi.org/10.1287/ijoc.2023.0236), `code/github_INFORMSJoC_2023.0236/src/core/utility.jl` line 64; license file: MIT.

### `Base.Matrix`

Used in 67 of 164 Julia papers (41%) — Construct a `Matrix{T}` of size `m`×`n`, initialized with `missing` entries.

Most common option set: none; at least one call in 67 papers (100%).

```julia
println(Matrix(A))  # Display as dense for readability
```
MPC 2026, [doi:10.1007/s12532-025-00292-0](https://doi.org/10.1007/s12532-025-00292-0), `code/github_PolyU-IOR_HPR-LP-C/bindings/julia/examples/example_direct_lp.jl` line 44; license file: MIT.

### `Base.Vector`

Used in 65 of 164 Julia papers (40%) — Construct a `Vector{T}` of length `m`, initialized with `missing` entries.

Most common option set: none; at least one call in 65 papers (100%).

```julia
        cs1 = COSMO.Constraint(spdiagm(ones(n)), zeros(n), COSMO.Box(Vector(l), u))
```
MPC 2026, [doi:10.1007/s12532-025-00301-2](https://doi.org/10.1007/s12532-025-00301-2), `code/github_tjdiamandis_GeNIOSExperiments.jl/experiments/4-constrained-ls-compare.jl` line 51; license file: MIT.

### `Base.joinpath`

Used in 55 of 164 Julia papers (34%) — Join path components into a full path.

Most common option set: none; at least one call in 55 papers (100%).

```julia
                include(joinpath(root, file))
```
MPC 2026, [doi:10.1007/s12532-026-00315-4](https://doi.org/10.1007/s12532-026-00315-4), `code/github_zavalab_PlasmoBendersExamples/CS2/GenX.jl/src/GenX.jl` line 76; license file: GPL.

### `Base.filter`

Used in 48 of 164 Julia papers (29%) — Return a vector similar to the array wrapped by the given `SkipMissing` iterator but with all missing elements and those for which `f` returns ....

Most common option set: none; at least one call in 48 papers (100%).

```julia
    for file in joinpath.(root, filter(is_test_file, files))
```
IJOC 2026, [doi:10.1287/ijoc.2025.1449](https://doi.org/10.1287/ijoc.2025.1449), `code/github_INFORMSJoC_2025.1449/test/runtests.jl` line 10; license file: GPL.

### `Base.@inbounds`

Used in 34 of 164 Julia papers (21%) — Eliminates array bounds checking within expressions.

Options (share of these 34 papers): `?` 26%, `i` 6%, `v` 6%, `x` 6%.

Most common option set: none; at least one call in 32 papers (94%).

```julia
    @inbounds R.u[i] * R.v[j]
```
MPC 2026, [doi:10.1007/s12532-026-00340-3](https://doi.org/10.1007/s12532-026-00340-3), `code/github_GioniMexi_FW-MIQCQP-Heuristic/FrankWolfe.jl/src/types.jl` line 133; license file: MIT.

Next most common option set: `?`; at least one call in 9 papers (26%).

```julia
        @inbounds c[tx] = a[tx] - b[tx]
```
IJOC 2025, [doi:10.1287/ijoc.2024.0983](https://doi.org/10.1287/ijoc.2024.0983), `code/github_INFORMSJoC_2024.0983/src/solver_gpu_core.jl` line 515; license file: MIT.

### `Base.join`

Used in 32 of 164 Julia papers (20%) — Join any `iterator` into a single string, inserting the given delimiter (if any) between adjacent items.

Options (share of these 32 papers): `kind` 6%, `on` 6%.

Most common option set: none; at least one call in 30 papers (94%).

```julia
	print(join(rows, "\n"))
```
IJOC 2026, [doi:10.1287/ijoc.2024.0686](https://doi.org/10.1287/ijoc.2024.0686), `code/github_INFORMSJoC_2024.0686/results/CombPricingDP-Interdiction-Grouping.jl` line 185; license file: MIT.
