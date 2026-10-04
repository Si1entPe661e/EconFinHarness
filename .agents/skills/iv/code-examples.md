# IV commands

Examples use an in-memory df with y, d, z, x1, x2, unit and period; unit is the chosen cluster. Keep all variables, including cluster identifiers, complete on the shared sample. Replace column names to match the analysis.

## R: fixed effects, first stage, reduced form and 2SLS

~~~r
library(fixest)
vars <- c("y", "d", "z", "x1", "x2", "unit", "period")
d <- df[complete.cases(df[, vars]), vars]
fs <- feols(d ~ z + x1 + x2 | unit + period, data = d, cluster = ~unit)
rf <- feols(y ~ z + x1 + x2 | unit + period, data = d, cluster = ~unit)
ols <- feols(y ~ d + x1 + x2 | unit + period, data = d, cluster = ~unit)
iv <- feols(y ~ x1 + x2 | unit + period | d ~ z, data = d, cluster = ~unit)
summary(iv, stage = 1)
summary(iv, stage = 2)
fitstat(iv, ~ivf1 + ivwald1)
etable(fs, rf, ols, iv)
~~~

ivf1 and ivwald1 are package diagnostics; do not rename them as effective F statistics. For two endogenous variables and two instruments the IV part is d1 + d2 ~ z1 + z2; include both pairs in the complete-case sample and examine strength for each endogenous regressor.

## Stata: absorbed and explicit fixed effects

~~~stata
keep if !missing(y, d, z, x1, x2, unit, period)
ivreghdfe y x1 x2 (d = z), absorb(unit period) cluster(unit) first
ivreg2 y x1 x2 i.unit i.period (d = z), cluster(unit) first
ivreg2 y x1 x2 i.unit i.period (d = z), cluster(unit) liml first
~~~

ivreghdfe and ivreg2 are user-written commands. The second call is suitable when explicit FE indicators are manageable. LIML changes the estimator, not the exclusion argument.

## Python: 2SLS and first-stage results

~~~python
from linearmodels.iv import IV2SLS

cols = ["y", "d", "z", "x1", "x2", "unit", "period"]
sample = df[cols].dropna().copy()
fit = IV2SLS.from_formula(
    "y ~ 1 + x1 + x2 + C(unit) + C(period) + [d ~ z]",
    data=sample,
).fit(cov_type="clustered", clusters=sample["unit"], debiased=True)
print(fit.summary)
print(fit.first_stage.diagnostics)
print(fit.wooldridge_overid)
~~~

Explicit FE indicators can be expensive. The overidentification statistic is unavailable in an exactly identified design. Inspect the reported diagnostic distribution before interpreting an F or chi-squared statistic.

## R: Anderson–Rubin test at a specified null

This example tests H0: beta = beta0 with one endogenous regressor, one excluded instrument and the same controls/FE. It uses a cluster Wald test on the transformed reduced form.

~~~r
beta0 <- 0
d$y_null <- d$y - beta0 * d$d
ar <- feols(y_null ~ z + x1 + x2 | unit + period, data = d, cluster = ~unit)
wald(ar, keep = "^z$")
~~~

To construct a confidence set, invert this test over candidate beta values. Expand the search until boundary behavior is understood; a finite grid alone cannot establish boundedness. With few clusters, this analytic clustered test also needs an appropriate few-cluster treatment.
