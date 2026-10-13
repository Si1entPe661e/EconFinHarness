# RD commands

df contains y, running, received, baseline and cluster_id. running is centred at zero. received is actual treatment, baseline a predetermined covariate, and cluster_id the dependence unit. Use a complete common sample for comparisons.

## R: sharp RD, covariates, fuzzy RD and plots

~~~r
library(rdrobust)
library(rddensity)
cols <- c("y", "running", "received", "baseline", "cluster_id")
d <- df[complete.cases(df[, cols]), cols]
sharp <- rdrobust(
  y = d$y, x = d$running, c = 0, p = 1, q = 2,
  kernel = "triangular", bwselect = "mserd",
  masspoints = "adjust", cluster = d$cluster_id
)
adjusted <- rdrobust(
  y = d$y, x = d$running, c = 0, p = 1, q = 2,
  covs = as.matrix(d["baseline"]), kernel = "triangular",
  bwselect = "mserd", masspoints = "adjust", cluster = d$cluster_id
)
first_stage <- rdrobust(
  y = d$received, x = d$running, c = 0, p = 1, q = 2,
  h = sharp$bws["h", ], b = sharp$bws["b", ],
  kernel = "triangular", cluster = d$cluster_id
)
fuzzy <- rdrobust(
  y = d$y, x = d$running, fuzzy = d$received, c = 0,
  p = 1, q = 2, kernel = "triangular", bwselect = "mserd",
  masspoints = "adjust", cluster = d$cluster_id
)
summary(sharp)
summary(first_stage)
summary(fuzzy)
summary(rddensity(X = d$running, c = 0))
rdplot(y = d$y, x = d$running, c = 0, p = 1,
       kernel = "triangular", h = sharp$bws["h", ])
~~~

Use the robust row for bias-corrected inference. The density test above has its own assumptions and does not inherit the outcome regression's cluster covariance. If clustering or discreteness undermines that test, discuss an appropriate alternative.

## R: a bandwidth sensitivity grid

~~~r
scales <- c(0.5, 0.75, 1, 1.25, 1.5)
sensitivity <- lapply(scales, function(s) {
  rdrobust(y = d$y, x = d$running, c = 0, p = 1, q = 2,
           h = s * sharp$bws["h", ], b = s * sharp$bws["b", ],
           kernel = "triangular", cluster = d$cluster_id,
           masspoints = "adjust")
})
names(sensitivity) <- as.character(scales)
lapply(sensitivity, summary)
~~~

The multipliers are illustrative choices; use the relevant units and support. A sharp outcome derivative can be estimated using deriv = 1, p = 2, q = 3, but it is not a treatment kink effect without the denominator slope change.

## Stata

~~~stata
keep if !missing(y, running, received, baseline, cluster_id)
rdrobust y running, c(0) p(1) q(2) kernel(triangular) bwselect(mserd) vce(cluster cluster_id) masspoints(adjust)
rdrobust y running, c(0) p(1) q(2) covs(baseline) kernel(triangular) bwselect(mserd) vce(cluster cluster_id)
rdrobust y running, fuzzy(received) c(0) p(1) q(2) kernel(triangular) bwselect(mserd) vce(cluster cluster_id)
rddensity running, c(0)
rdplot y running, c(0) p(1) kernel(triangular)
~~~

These calls require the rdrobust/rddensity commands. Python translations should preserve bandwidth, polynomial, kernel and bias correction rather than substituting an unrestricted polynomial OLS fit.
