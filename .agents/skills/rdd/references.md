# rdd references

Verification: `verified_online` = DOI resolved through the Crossref API on 2026-09-08 with title, journal and authors matching; `verified_repo` = file in this repository; `unverified` = from memory, not resolved. Corpus exemplars are cited by artid and can be opened with `fh recipe <artid>`.

| ref | kind | verification | note |
|---|---|---|---|
| Calonico, Cattaneo, Titiunik (2014), Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs, Econometrica 82. DOI 10.3982/ECTA11757 | paper | verified_online | bias-corrected robust CIs; basis of rdrobust |
| Calonico, Cattaneo, Farrell, Titiunik (2017), rdrobust: Software for Regression-discontinuity Designs, Stata Journal 17. DOI 10.1177/1536867X1701700208 | software_doc | verified_online | Stata/R options: p, kernel, bwselect, vce, cluster, fuzzy |
| Calonico, Cattaneo, Farrell, Titiunik (2019), Regression Discontinuity Designs Using Covariates, REStat 101. DOI 10.1162/rest_a_00760 | paper | verified_online | covariate adjustment without changing the estimand |
| Cattaneo, Jansson, Ma (2020), Simple Local Polynomial Density Estimators, JASA 115. DOI 10.1080/01621459.2019.1635480 | paper | verified_online | density test used by rddensity |
| Cattaneo, Jansson, Ma (2018), Manipulation Testing Based on Density Discontinuity, Stata Journal 18. DOI 10.1177/1536867X1801800115 | software_doc | verified_online | rddensity command |
| McCrary (2008), Manipulation of the running variable in the regression discontinuity design: a density test, J. Econometrics 142. DOI 10.1016/j.jeconom.2007.05.005 | paper | verified_online | original density test |
| Imbens, Kalyanaraman (2012), Optimal Bandwidth Choice for the Regression Discontinuity Estimator, REStud 79. DOI 10.1093/restud/rdr043 | paper | verified_online | MSE-optimal bandwidth |
| Gelman, Imbens (2019), Why High-Order Polynomials Should Not Be Used in Regression Discontinuity Designs, JBES 37. DOI 10.1080/07350015.2017.1366909 | paper | verified_online | polynomial order rule |
| Kolesar, Rothe (2018), Inference in Regression Discontinuity Designs with a Discrete Running Variable, AER 108. DOI 10.1257/aer.20160945 | paper | verified_online | discrete running variable branch; honest CIs |
| Armstrong, Kolesar (2020), Simple and honest confidence intervals in nonparametric regression, Quantitative Economics 11. DOI 10.3982/QE1199 | paper | verified_online | RDHonest approach |
| Card, Lee, Pei, Weber (2015), Inference on Causal Effects in a Generalized Regression Kink Design, Econometrica 83. DOI 10.3982/ECTA11224 | paper | verified_online | kink designs |
| Lee, Lemieux (2010), Regression Discontinuity Designs in Economics, JEL 48. DOI 10.1257/jel.48.2.281 | paper | verified_online | practice guide |
| Imbens, Lemieux (2008), Regression discontinuity designs: A guide to practice, J. Econometrics 142. DOI 10.1016/j.jeconom.2007.05.001 | paper | verified_online | practice guide |
| Cattaneo, Titiunik (2022), Regression Discontinuity Designs, Annual Review of Economics 14. DOI 10.1146/annurev-economics-051520-021409 | paper | verified_online | survey of current practice |
| Cattaneo, Idrobo, Titiunik, A Practical Introduction to Regression Discontinuity Designs (Cambridge Elements, two volumes) | book | unverified | not resolved through Crossref in this pass |
| rdrobust R package (CRAN). DOI 10.32614/CRAN.package.rdrobust | software_doc | verified_online | Check the package version used by the analysis. |
| aer_114_11_1 | corpus_card | verified_repo | rdrobust with normalised multiple cutoffs, clustered SEs, bandwidth selection and polynomial order recorded |
| aer_110_2_5 | corpus_card | verified_repo | sharp and fuzzy RD (rdrobust and ivreghdfe), bandwidth sensitivity figure |
| held out for evaluation (not used here): aer_107_1_5, ecta_92_3_6, jpe_132_9_2, qje_140_1_11 | corpus_card | verified_repo | see harness_build/evals/holdout/rdd.json |
| restud_2025_restud_rdae108 | corpus_card | verified_repo | rdrobust sharp and fuzzy calls, rddensity, first stage |
| jpe_2026_740226 | corpus_card | verified_repo | rdrobust with bandwidth selection, density test, first stage |
| harness/paradigms/rdd/observed.md | paradigm | verified_repo | generated observed practice with pointers |
