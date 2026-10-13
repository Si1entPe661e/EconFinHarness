# War Discourse: independent reproduction example

This example implements the main empirical path in Hirshleifer, Mai and Pukthuanthong (2025), *War Discourse and the Cross Section of Expected Stock Returns*, DOI `10.1111/jofi.13482`, from the supplied paper and Internet Appendix. Author programs, command histories and packaged output workbooks are not read.

## Run

From the repository root:

```bash
python3 harness/examples/war-discourse/run_all.py
```

Requirements: Python 3.9 or later (standard library only); an available `Rscript`; and R packages `sandwich`, `jsonlite`, `ggplot2`, and `testthat`. The runner uses the installed R environment and records `sessionInfo()`. It does not install packages or run third-party programs.

Local inputs must already exist under `examples/war-discourse/Disclosure Statement-20230479/input/`. They are not distributed with this example. The two supplied PDFs are the specification sources; source page pointers and manually transcribed comparison values are in `specification.json` and `published_targets.json`.

Outputs go to `outputs/war-discourse-reproduction/`: a readable HTML report, numeric CSVs, fitted result objects, monthly industry slopes, standalone PNG/EPS figures, checks and runtime logs. Source PDFs, third-party programs and data stay separate from the public harness.

## What is independently reconstructed

- Portfolio inclusion from the larger supplied return panels, rather than taking the supplied filtered membership as an answer.
- Expanding AR innovations from supplied War index levels, with separate calendar-lag, observed-lag and published-series tracks.
- Full-sample two-pass pricing, Shanken covariance and first-pass beta diagnostics; Tables I-IV and the two additional portfolio families.
- Rolling 60-month, lagged-beta industry regressions for Table V, with per-asset eligibility and HAC sensitivity.
- Cross-sectional and time-series mimicking portfolios; spanning regressions; available topic, tail-beta, index and subsample comparisons; a VAR decomposition identity check and the second protocol stage.

The initial `War_base` mapping follows the descriptive mean in the text. A separately labelled `War_main` track was added after the already-declared index sensitivities reproduced the main pricing table closely. The original track is retained. A supplied-innovation control is a **post-implementation diagnostic**, not independent AR reconstruction. It helps distinguish factor-construction discrepancies from pricing implementation errors.

## Boundaries and unresolved choices

The full NYT corpus and stock characteristics needed to reconstruct all portfolios are unavailable. Results therefore condition on supplied index levels and portfolio returns. The exact AR initialization, first-pass beta covariance, industry tie/eligibility rules and HAC tuning are not fully specified in the paper. Numerical comparisons do not prove upstream seed-word provenance. Both raw and adjusted cross-sectional R-squared are exported because the table values can differ from the written definition.

This is a complete runnable example task, not a claim that every analysis in the 86-page Internet Appendix has been reproduced. The report records the exact coverage and unresolved differences. In particular, the full topic estimation, ARMA robustness, analytical-news test and complete first-stage protocol/three-pass inference are not claimed as reproduced.

## Checks and package reuse

`checks.R` tests the data-only reader, timing, AR boundaries, missing months, two-pass identities, Shanken covariance, factor units, HAC and a working graphics device. `verify_outputs.py` checks the actual exported results, common comparison samples, input immutability and source fingerprints. `harness/checks/check_paper_first.py` guards the workflow's author-code boundary. Publication matches are reported separately from these implementation checks.

The installed `sandwich` package supplies robust covariance routines; the local snapshot under `sample_repository/cran__sandwich/source/sandwich/` was consulted for documentation. The one-entry-point, input-preservation and session-report patterns were informed by `sample_repository/yhoriuchi__replication-package-guide/`. Neither repository's code is vendored, and its project setup instructions are not imposed on this example. References: Zeileis (2004), DOI `10.18637/jss.v011.i10`; Shanken (1992), DOI `10.1093/rfs/5.1.1`.
