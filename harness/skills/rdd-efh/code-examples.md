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

## R: observations, support points and clusters inside the bandwidth

~~~r
h <- sharp$bws["h", ]
left <- d$running < 0 & d$running > -h[1]
right <- d$running >= 0 & d$running < h[2]
data.frame(
  side = c("left", "right"),
  observations = c(sum(left), sum(right)),
  support_points = c(length(unique(d$running[left])), length(unique(d$running[right]))),
  clusters = c(length(unique(d$cluster_id[left])), length(unique(d$cluster_id[right])))
)
length(unique(d$cluster_id[left | right]))
~~~

The triangular kernel gives zero weight at the bandwidth edge, so the strict inequalities reproduce rdrobust's effective observations (`sharp$N_h`). A cluster with observations on both sides counts on each side; the last line counts it once. Few clusters inside the bandwidth weaken clustered inference (`inference-clustering-efh`). Few support points call for support-aware inference, not clustering on running-variable values.

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
generate byte rd_side = running >= 0 if (running < 0 & running > -e(h_l)) | (running >= 0 & running < e(h_r))
egen byte rd_point = tag(rd_side running) if !missing(rd_side)
egen byte rd_cluster = tag(rd_side cluster_id) if !missing(rd_side)
egen byte rd_any_cluster = tag(cluster_id) if !missing(rd_side)
tabstat rd_point rd_cluster if !missing(rd_side), by(rd_side) statistics(count sum)
count if rd_any_cluster == 1
rdrobust y running, c(0) p(1) q(2) covs(baseline) kernel(triangular) bwselect(mserd) vce(cluster cluster_id)
rdrobust y running, fuzzy(received) c(0) p(1) q(2) kernel(triangular) bwselect(mserd) vce(cluster cluster_id)
rddensity running, c(0)
rdplot y running, c(0) p(1) kernel(triangular)
~~~

After the first call, `rd_side` marks observations inside its bandwidth (0 left, 1 right). In `tabstat`, the counts are observations on each side, equal to `e(N_h_l)` and `e(N_h_r)`, and the sums are support points and clusters; `count` gives clusters inside the bandwidth on either side. These calls require the rdrobust/rddensity commands. Python translations should preserve bandwidth, polynomial, kernel and bias correction rather than substituting an unrestricted polynomial OLS fit.
