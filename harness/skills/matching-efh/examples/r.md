# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `MatchIt::matchit`

Used in 12 of 1163 R papers (1%) — Nonparametric Preprocessing for Parametric Causal Inference.

Options (share of these 12 papers): `data` 92%, `method` 83%, `distance` 50%, `ratio` 33%, `link` 25%, `replace` 25%, `caliper` 17%.

Most common option set: `data`, `method`; at least one call in 2 papers (17%).

```r
m.out = matchit(
  D ~ g0 + dg0 + hdd0 + gsl0 + elevation + pd0,
  data = strat_sample[year == 1989 & !is.na(g0)  & !is.na(dg0) & !is.na(hdd0) & 
                        !is.na(gsl0) & !is.na(elevation) & !is.na(pd0),],
  method = 'cem'#,
  #distance = 'euclidean',
  # exact = 'pd0'
)
```
ReStud 2026, [doi:10.1093/restud/rdag080](https://doi.org/10.1093/restud/rdag080), `code/zenodo_18849776/EUForest_Workspace/EUForest Workspace/analysis/10_Robustness.r` lines 120-127.

### `MatchIt::match.data`

Used in 9 of 1163 R papers (0.8%) — Nonparametric Preprocessing for Parametric Causal Inference.

Most common option set: none; at least one call in 8 papers (89%).

```r
matched_nco2 <- match.data(nco_match_obj2)
```
QJE 2026, [doi:10.1093/qje/qjaf046](https://doi.org/10.1093/qje/qjaf046), `code/dataverse_LSPICA/code/05_camp_discrimination.R` line 84; license file: BSD.
