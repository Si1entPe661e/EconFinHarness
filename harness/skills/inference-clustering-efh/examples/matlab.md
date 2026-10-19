# MATLAB examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1084 MATLAB replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `bootstrp`

Used in 10 of 1084 MATLAB papers (0.9%) — Bootstrap sampling.

Most common option set: none; at least one call in 8 papers (80%).

```matlab
tmp_opt_n_abs  = std(bootstrp(10000, @mean, pe2));
```
RFS 2026, [doi:10.1093/rfs/hhag054](https://doi.org/10.1093/rfs/hhag054), `code/dataverse_R6FBQZ/GithubRepository/GithubRepository/nac/NAC/matlab/NAC_main.m` line 296.

### `corrcov`

Used in 6 of 1084 MATLAB papers (0.6%) — Convert covariance matrix to correlation matrix.

Most common option set: none; at least one call in 6 papers (100%).

```matlab
    DeltaCorr      = corrcov(.5*Delta + .5*Delta');
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_parametric-bootstrap/computeSEs.m` line 117; license file: GPL.

## Inference options of estimation commands
