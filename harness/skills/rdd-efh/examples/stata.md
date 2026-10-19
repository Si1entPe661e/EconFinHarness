# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `rdrobust`

Used in 33 of 1904 Stata papers (2%) — module to provide robust data-driven inference in the regression-discontinuity design.

Options (share of these 33 papers): `h` 61%, `c` 58%, `p` 55%, `vce` 52%, `kernel` 45%, `covs` 39%, `all` 36%, `fuzzy` 27%, `bwselect` 15%, `q` 9%.

Most common option set: none; at least one call in 3 papers (9%).

```stata
rdrobust const_event runvar
```
ReStud 2025, [doi:10.1093/restud/rdae108](https://doi.org/10.1093/restud/rdae108), `code/zenodo_13314638/electoral_turnovers_replication_package/replication_package/do/3_3_C5_appendix_figure_C5.do` line 6.
