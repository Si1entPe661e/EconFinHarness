# iv references

Verification: `verified_online` = DOI resolved through the Crossref API on 2026-09-08 with title, journal and authors matching; `verified_repo` = file in this repository; `unverified` = from memory, not resolved.

| ref | kind | verification | note |
|---|---|---|---|
| Andrews, Stock, Sun (2019), Weak Instruments in Instrumental Variables Regression: Theory and Practice, Annual Review of Economics 11. DOI 10.1146/annurev-economics-080218-025643 | paper | verified_online | weak-IV diagnostics and robust inference guide |
| Lee, McCrary, Moreira, Porter (2022), Valid t-ratio Inference for IV, AER 112. DOI 10.1257/aer.20211063 | paper | verified_online | tF critical values for single-instrument t-ratios |
| Montiel Olea, Pflueger (2013), A Robust Test for Weak Instruments, JBES 31. DOI 10.1080/00401706.2013.806694 | paper | verified_online | effective F statistic; `weakivtest` |
| Kleibergen, Paap (2006), Generalized reduced rank tests using the singular value decomposition, J. Econometrics 133. DOI 10.1016/j.jeconom.2005.02.011 | paper | verified_online | KP rank statistics reported by ivreg2/ivreghdfe |
| Borusyak, Hull, Jaravel (2022), Quasi-Experimental Shift-Share Research Designs, REStud 89. DOI 10.1093/restud/rdab030 | paper | verified_online | shock-level identification and inference; `ssaggregate` |
| Goldsmith-Pinkham, Sorkin, Swift (2020), Bartik Instruments: What, When, Why, and How, AER 110. DOI 10.1257/aer.20181047 | paper | verified_online | share-based identification; Rotemberg weights |
| Abadie, Athey, Imbens, Wooldridge (2022), When Should You Adjust Standard Errors for Clustering?, QJE 138. DOI 10.1093/qje/qjac038 | paper | verified_online | cluster level from design |
| MacKinnon, Nielsen, Webb (2023), Cluster-robust inference: A guide to empirical practice, J. Econometrics 232. DOI 10.1016/j.jeconom.2022.04.001 | paper | verified_online | few clusters; bootstrap |
| Angrist, Pischke (2009), Mostly Harmless Econometrics, Princeton University Press. DOI 10.1515/9781400829828 | book | verified_online | LATE framework, first-stage reporting |
| Anderson, Rubin (1949), Estimation of the parameters of a single equation in a complete system of stochastic equations, Annals of Mathematical Statistics 20 | paper | unverified | AR confidence sets |
| Frandsen, Lefgren, Leslie (2023), Judging Judge Fixed Effects, AER | paper | unverified | leniency design tests; corpus card aer_113_1_8 holds the replication code |
| ivreg2 / ivreghdfe (Baum, Schaffer, Stillman; Correia), Stata command documentation | software_doc | unverified | first stage, KP statistics, cluster options |
| fixest R package (CRAN). DOI 10.32614/CRAN.package.fixest | software_doc | verified_online | IV syntax `y ~ x1 | fe | endo ~ inst`, `fitstat` |
| aer_113_1_8 | corpus_card | verified_repo | leniency IV method paper code (monotonicity/exclusion test observed) |
| restud_89_1_6 | corpus_card | verified_repo | shift-share method paper code (Borusyak-Hull-Jaravel) |
| rfs_2026_rfs_hhaf079 | corpus_card | verified_repo | `twostepweakiv` weak-IV robust inference observed |
| restud_2026_restud_rdaf044 | corpus_card | verified_repo | reduced form and IV with clustering, alternative samples |
| held out for evaluation (not used here): aer_112_5_9, jpe_132_9_2, qje_139_1_2 | corpus_card | verified_repo | see examples/exclusions/iv.json |
| harness/paradigms/iv/observed.md, harness/paradigms/shift_share/observed.md | paradigm | verified_repo | generated observed practice with pointers |
