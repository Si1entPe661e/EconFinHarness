# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `psmatch2`

Used in 25 of 1904 Stata papers (1%) — module to perform full Mahalanobis and propensity score matching, common support graphing, and covariate imbalance testing.

Options (share of these 25 papers): `neighbor` 52%, `noreplacement` 40%, `caliper` 36%, `common` 32%, `pscore` 24%, `out` 20%, `outcome` 20%, `logit` 16%, `norepl` 12%, `n` 12%.

Most common option set: none; at least one call in 2 papers (8%).

```stata
	qui: psmatch2 treat $psvar_list
```
JFE 2025, [doi:10.1016/j.jfineco.2025.104136](https://doi.org/10.1016/j.jfineco.2025.104136), `code/mendeley_sx62b72p97_v2/replication_package_MOS2025/replication_package_MOS2025/program/MOS_replication_program.do` line 389.

### `cem`

Used in 9 of 1904 Stata papers (0.5%) — module to perform Coarsened Exact Matching.

Options (share of these 9 papers): `treatment` 78%, `k2k` 33%, `tr` 22%.

Most common option set: `k2k`, `treatment`; at least one call in 3 papers (33%).

```stata
cem state county logcumoil6 oil_202003 hlength prodmonth, treatment(ds_exp)  k2k 
```
RFS 2025, [doi:10.1093/rfs/hhaf099](https://doi.org/10.1093/rfs/hhaf099), `code/dataverse_IPVSH4/_ Replication Package/! Replication Package/Stata/Code/Main.do` line 1035.

Next most common option set: `treatment`; at least one call in 3 papers (33%).

```stata
cem black_share60, treatment(literacy_nc)
```
JPE 2025, [doi:10.1086/736766](https://doi.org/10.1086/736766), `code/dataverse_HIY143/appendix_c.do` line 56.
