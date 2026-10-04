# did references

Verification: `verified_online` = DOI resolved through the Crossref API on 2026-09-08 with title, journal and authors matching; `verified_repo` = file in this repository; `unverified` = from memory, not resolved.

| ref | kind | verification | note |
|---|---|---|---|
| Callaway, Sant'Anna (2021), Difference-in-Differences with multiple time periods, J. Econometrics 225. DOI 10.1016/j.jeconom.2020.12.001 | paper | verified_online | group-time ATTs; `did`, `csdid` |
| Sun, Abraham (2021), Estimating dynamic treatment effects in event studies with heterogeneous treatment effects, J. Econometrics 225. DOI 10.1016/j.jeconom.2020.09.006 | paper | verified_online | interaction-weighted estimator; `eventstudyinteract`, fixest `sunab` |
| de Chaisemartin, D'Haultfoeuille (2020), Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects, AER 110. DOI 10.1257/aer.20181169 | paper | verified_online | negative weights; `did_multiplegt` |
| Goodman-Bacon (2021), Difference-in-differences with variation in treatment timing, J. Econometrics 225. DOI 10.1016/j.jeconom.2021.03.014 | paper | verified_online | TWFE decomposition; `bacondecomp` |
| Borusyak, Jaravel, Spiess (2024), Revisiting Event-Study Designs: Robust and Efficient Estimation, REStud. DOI 10.1093/restud/rdae007 | paper | verified_online | imputation estimator; `did_imputation` |
| Rambachan, Roth (2023), A More Credible Approach to Parallel Trends, REStud. DOI 10.1093/restud/rdad018 | paper | verified_online | sensitivity bounds; `HonestDiD` |
| Roth (2022), Pretest with Caution: Event-Study Estimates after Testing for Parallel Trends, AER: Insights 4. DOI 10.1257/aeri.20210236 | paper | verified_online | pre-testing caveat |
| Roth, Sant'Anna, Bilinski, Poe (2023), What's trending in difference-in-differences?, J. Econometrics 235. DOI 10.1016/j.jeconom.2023.03.008 | paper | verified_online | synthesis and practical guidance |
| Arkhangelsky, Athey, Hirshberg, Imbens, Wager (2021), Synthetic Difference-in-Differences, AER 111. DOI 10.1257/aer.20190159 | paper | verified_online | synthetic DID |
| Bertrand, Duflo, Mullainathan (2004), How Much Should We Trust Differences-in-Differences Estimates?, QJE 119. DOI 10.1162/003355304772839588 | paper | verified_online | serial correlation and clustering |
| Cameron, Gelbach, Miller (2008), Bootstrap-Based Improvements for Inference with Clustered Errors, REStat 90. DOI 10.1162/rest.90.3.414 | paper | verified_online | wild cluster bootstrap |
| Abadie, Athey, Imbens, Wooldridge (2022), When Should You Adjust Standard Errors for Clustering?, QJE 138. DOI 10.1093/qje/qjac038 | paper | verified_online | cluster level from design |
| MacKinnon, Nielsen, Webb (2023), Cluster-robust inference: A guide to empirical practice, J. Econometrics 232. DOI 10.1016/j.jeconom.2022.04.001 | paper | verified_online | practical clustering guide |
| Correia, Guimaraes, Zylkin (2020), Fast Poisson estimation with high-dimensional fixed effects, Stata Journal 20. DOI 10.1177/1536867X20909691 | software_doc | verified_online | `ppmlhdfe` |
| fixest R package (CRAN). DOI 10.32614/CRAN.package.fixest | software_doc | verified_online | `feols`, `sunab`, `i()` |
| reghdfe (Correia), Stata command documentation | software_doc | unverified | absorb / vce options; version-dependent singleton handling |
| aer_114_7_10, restud_2026_restud_rdag080 | corpus_card | verified_repo | group-time ATT estimators (`csdid`, `att_gt`) |
| restud_2026_restud_rdag056 | corpus_card | verified_repo | `did_multiplegt` with pre-trend plot output code |
| aer_113_1_1 | corpus_card | verified_repo | TWFE event study with hand-built leads and lags, `felm` and `reghdfe` |
| held out for evaluation (not used here): aer_110_9_10, aer_113_3_7, aer_114_6_6, aer_115_3_8, restud_90_5_11, restud_92_2_14, rfs_2025_rfs_hhaf065 | corpus_card | verified_repo | see harness/paradigms/did/reported.md |
| restud_2026_restud_rdag011, restud_2026_restud_rdaf071 | corpus_card | verified_repo | `did_imputation` with pre-trend tests and PPML variants |
| aer_111_12_8 | corpus_card | verified_repo | synthetic DID implementation in R (method paper code) |
| harness/paradigms/did/observed.md, harness/paradigms/event_study/observed.md | paradigm | verified_repo | generated observed practice with pointers |
