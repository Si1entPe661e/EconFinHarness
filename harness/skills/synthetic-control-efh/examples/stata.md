# Stata examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1904 Stata replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `synth`

Used in 8 of 1904 Stata papers (0.4%) — module to implement Synthetic Control Methods for Comparative Case Studies.

Options (share of these 8 papers): `trperiod` 88%, `trunit` 88%, `keep` 75%, `replace` 50%, `figure` 25%.

Most common option set: `keep`, `replace`, `trperiod`, `trunit`; at least one call in 2 papers (25%).

```stata
			cap synth ln_mort_age100_all_10c ln_mort_age100_all_10c(201101) ln_mort_age100_all_10c(201102) ln_mort_age100_all_10c(201103) ln_mort_age100_all_10c(201104), trunit(`trunit') trperiod(201301) keep("./1_build/_confidential/synth/proc/synth_pair`i'.dta") replace
```
AER 2024, [doi:10.1257/aer.20200956](https://doi.org/10.1257/aer.20200956), `code/replicate_information/1_build/build.do` line 1378.
