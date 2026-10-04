# References: inference-clustering

All entries are `unverified`. No entry was checked against an online source or against the corpus while this skill was written. Verify before citing any entry in a research output. Where a DOI is not certain it is omitted rather than guessed.

| ref | kind | verification | note |
|---|---|---|---|
| White, "A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct Test for Heteroskedasticity" (1980), Econometrica | method paper | unverified | Heteroskedasticity-robust variance. |
| Newey and West, "A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix" (1987), Econometrica | method paper | unverified | HAC variance estimator. |
| Andrews, "Heteroskedasticity and Autocorrelation Consistent Covariance Matrix Estimation" (1991), Econometrica | method paper | unverified | Automatic bandwidth selection for HAC. |
| Bertrand, Duflo and Mullainathan, "How Much Should We Trust Differences-in-Differences Estimates?" (2004), Quarterly Journal of Economics | method paper | unverified | Serial correlation in panel difference-in-differences and its effect on inference. |
| Cameron, Gelbach and Miller, "Bootstrap-Based Improvements for Inference with Clustered Errors" (2008), Review of Economics and Statistics | method paper | unverified | Wild cluster bootstrap with few clusters. |
| Cameron, Gelbach and Miller, "Robust Inference with Multiway Clustering" (2011), Journal of Business and Economic Statistics | method paper | unverified | Multi-way cluster-robust variance. |
| Cameron and Miller, "A Practitioner's Guide to Cluster-Robust Inference" (2015), Journal of Human Resources | survey | unverified | Practical guide to cluster level choice and few-cluster corrections. |
| Abadie, Athey, Imbens and Wooldridge, "When Should You Adjust Standard Errors for Clustering?" (2023), Quarterly Journal of Economics | method paper | unverified | Design-based versus sampling-based justification for clustering. Verify year and outlet before citing. |
| MacKinnon and Webb, "Wild Bootstrap Inference for Wildly Different Cluster Sizes" (2017), Journal of Applied Econometrics | method paper | unverified | Cluster size imbalance and treated cluster counts. |
| Roodman, MacKinnon, Nielsen and Webb, "Fast and Wild: Bootstrap Inference in Stata Using boottest" (2019), Stata Journal | software paper | unverified | Implementation and options of the wild cluster bootstrap in Stata. |
| Pustejovsky and Tipton, "Small-Sample Methods for Cluster-Robust Variance Estimation and Hypothesis Testing in Fixed Effects Models" (2018), Journal of Business and Economic Statistics | method paper | unverified | CR2 correction and Satterthwaite degrees of freedom. |
| Driscoll and Kraay, "Consistent Covariance Matrix Estimation with Spatially Dependent Panel Data" (1998), Review of Economics and Statistics | method paper | unverified | Cross-sectional dependence in panels. |
| Conley, "GMM Estimation with Cross Sectional Dependence" (1999), Journal of Econometrics | method paper | unverified | Spatial dependence and distance-based variance estimation. |
| Young, "Channeling Fisher: Randomization Tests and the Statistical Insignificance of Seemingly Significant Experimental Results" (2019), Quarterly Journal of Economics | method paper | unverified | Randomization inference in applied work. |
| Athey and Imbens, "The Econometrics of Randomized Experiments" (2017), Handbook of Economic Field Experiments | survey | unverified | Design-based inference and randomization tests. |
| Stata Manual, `regress`, `vce_option`, `newey`, `ivregress` | software documentation | unverified | https://www.stata.com/manuals/ Check the installed version. |
| `reghdfe` documentation | software documentation | unverified | http://scorreia.com/software/reghdfe/ Singleton handling and degrees of freedom adjustments. |
| `boottest` documentation | software documentation | unverified | Distributed via SSC. Check the help file of the installed version for null imposition and weight type. |
| `xtscc` documentation | software documentation | unverified | Distributed via SSC. Driscoll-Kraay implementation for Stata. |
| fixest documentation (R) | software documentation | unverified | https://lrberge.github.io/fixest/ `vcov`, `cluster`, `ssc()` small-sample corrections, panel HAC and Driscoll-Kraay options. |
| sandwich documentation (R) | software documentation | unverified | https://sandwich.r-forge.r-project.org/ `vcovHC`, `vcovCL`, `NeweyWest`. |
| clubSandwich documentation (R) | software documentation | unverified | https://cran.r-project.org/package=clubSandwich CR0 to CR3 corrections and Satterthwaite tests. |
| fwildclusterboot documentation (R) | software documentation | unverified | https://cran.r-project.org/package=fwildclusterboot Wild cluster bootstrap. |
| statsmodels documentation (Python) | software documentation | unverified | https://www.statsmodels.org/ `cov_type` values HC0 to HC3, `cluster`, `HAC`, and the `use_correction` option. |
| linearmodels documentation (Python) | software documentation | unverified | https://bashtage.github.io/linearmodels/ Panel estimators and clustered covariance options. |
| pyfixest documentation (Python) | software documentation | unverified | https://py-econometrics.github.io/pyfixest/ Variance specification argument names change across releases. |
