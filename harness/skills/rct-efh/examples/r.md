# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `nbpMatching::distancematrix`

Used in 5 of 1163 R papers (0.4%) — Functions for Optimal Non-Bipartite Matching.

Most common option set: none; at least one call in 5 papers (100%).

```r
  distmat = distancematrix(distmat)
```
JASA 2025, [doi:10.1080/01621459.2025.2510711](https://doi.org/10.1080/01621459.2025.2510711), `code/figshare_29218013/supplements-zhe/code/code_matching/m0.R` line 51.

### `nbpMatching::nonbimatch`

Used in 5 of 1163 R papers (0.4%) — Functions for Optimal Non-Bipartite Matching.

Most common option set: none; at least one call in 5 papers (100%).

```r
    res<-nonbimatch(mdm2)
```
JASA 2024, [doi:10.1080/01621459.2023.2169701](https://doi.org/10.1080/01621459.2023.2169701), `code/figshare_21916525/ArchSimulateConcise.Rmd` line 349.

Next most common option set: `precision`; at least one call in 1 paper (20%).

```r
            optimalOutput <- nbpMatching::nonbimatch(optimalDistanceMatrix, 
                precision = 9)
```
JRSSB 2022, [doi:10.1111/rssb.12545](https://doi.org/10.1111/rssb.12545), `code/github_bikram12345k_BlockingAlgo/REORGANIZATION/supplement/section5/fixblockTools.R` lines 258-259.
