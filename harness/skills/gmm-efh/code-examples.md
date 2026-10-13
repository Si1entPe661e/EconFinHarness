# GMM commands

## R: explicit observation-level IV moments

df contains y, endogenous d and excluded z1/z2. The model is y = alpha + beta*d + error, with instruments (1,z1,z2). This call uses MDS moment covariance and is appropriate only when moment scores are serially uncorrelated; it is not clustered inference.

~~~r
library(gmm)
d <- df[complete.cases(df[, c("y", "d", "z1", "z2")]), ]
data_gmm <- as.matrix(d[, c("y", "d", "z1", "z2")])
moments <- function(theta, x) {
  error <- x[, 1] - theta[1] - theta[2] * x[, 2]
  instruments <- cbind(1, x[, 3], x[, 4])
  instruments * error
}
fit <- gmm(
  g = moments, x = data_gmm, t0 = c(0, 1),
  type = "twoStep", vcov = "MDS", optfct = "optim",
  method = "BFGS", control = list(maxit = 1000)
)
summary(fit)
print(colMeans(moments(coef(fit), data_gmm)))
~~~

For a time series, order observations and choose an appropriate HAC covariance/weighting rule. For clusters, use a GMM implementation with cluster-aware moment covariance; changing the final SE alone does not change the GMM weighting matrix.

## Stata: clustered linear IV-GMM

~~~stata
keep if !missing(y, d, z1, z2, x1, unit)
ivreg2 y x1 (d = z1 z2), gmm2s cluster(unit) first
~~~

x1 is exogenous and enters the instrument set as well as the equation. ivreg2 is user-written. Compare 2SLS and GMM under the same sample/instrument set, and interpret the overidentification test conditionally on instrument validity and the model.
