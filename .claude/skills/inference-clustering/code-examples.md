# Inference commands

Choose the covariance from the design. df contains y, x, unit, period and state where used. Remove missing values jointly before passing a cluster vector. Lag and distance values below are examples, not universal defaults.

## R: heteroskedastic and clustered covariance

~~~r
library(fixest)
d <- df[complete.cases(df[, c("y", "x", "unit", "period")]), ]
hc <- feols(y ~ x, data = d, vcov = "hetero")
one <- feols(y ~ x | unit + period, data = d, vcov = ~unit)
two <- feols(y ~ x | unit + period, data = d, vcov = ~unit + period)
summary(one, ssc = ssc(K.adj = TRUE, G.adj = TRUE,
                      G.df = "min", t.df = "min"))
~~~

For survey sampling, use the survey design's strata, PSUs and weights. Regression clustering alone does not implement the full survey design.

## R: CR2 and HAC

~~~r
library(clubSandwich)
cr2 <- lm(y ~ x, data = d)
coef_test(cr2, vcov = "CR2", cluster = d$unit, test = "Satterthwaite")

library(sandwich)
library(lmtest)
ts <- df[complete.cases(df[, c("y", "x", "period")]), ]
ts <- ts[order(ts$period), ]
stopifnot(!anyDuplicated(ts$period), all(diff(ts$period) == 1))
m <- lm(y ~ x, data = ts)
coeftest(m, vcov. = NeweyWest(m, lag = 4, prewhite = FALSE, adjust = TRUE))
~~~

The HAC block requires one equally spaced time series. It must not be applied directly to an entity-stacked panel.

## R: Driscoll–Kraay and spatial covariance

~~~r
dk <- feols(y ~ x | unit + period, data = d, panel.id = ~unit + period,
            vcov = DK(4) ~ period)
geo <- df[complete.cases(df[, c("y", "x", "latitude", "longitude")]), ]
spatial <- feols(y ~ x, data = geo,
                 vcov = conley(100, distance = "spherical") ~ latitude + longitude)
summary(dk)
summary(spatial)
~~~

The Conley cutoff here is 100 km and fixest uses its implemented spatial kernel; state that choice when reporting it. This call covers spatial dependence, not an unspecified space-time covariance. DK needs enough distinct time periods.

## Stata: clustering, HAC and wild cluster bootstrap

~~~stata
reghdfe y x, absorb(unit period) vce(cluster unit)
reghdfe y x, absorb(unit period) vce(cluster unit period)
reghdfe y x, absorb(unit period) vce(cluster state)
boottest x, reps(9999) seed(12345) bootcluster(state) nograph
~~~

reghdfe and boottest are user-written commands. Verify the bootstrap's null and weight distribution for the intended use, particularly with few treated groups.

On a separate one-observation-per-period time series:

~~~stata
tsset period
newey y x, lag(4)
~~~

On a panel:

~~~stata
xtset unit period
xtscc y x, fe lag(4)
~~~

xtscc is a user-written Driscoll–Kraay estimator; include time indicators in x's control list when the model requires time FE.

## Python: panel and time-series covariance

~~~python
from linearmodels.panel import PanelOLS
import statsmodels.formula.api as smf

sample = df[["y", "x", "unit", "period"]].dropna().copy()
assert not sample.duplicated(["unit", "period"]).any()
panel = sample.set_index(["unit", "period"]).sort_index()
model = PanelOLS.from_formula("y ~ 1 + x + EntityEffects + TimeEffects", panel)
clustered = model.fit(cov_type="clustered", cluster_entity=True,
                      cluster_time=True, debiased=True)
dk = model.fit(cov_type="kernel", kernel="bartlett", bandwidth=4)

ts = sample.sort_values("period")
assert ts["period"].is_unique
assert ts["period"].diff().dropna().eq(1).all()
hac = smf.ols("y ~ x", data=ts).fit(
    cov_type="HAC", cov_kwds={"maxlags": 4, "use_correction": True})
~~~

Use separate panel and time-series inputs in practice; the uniqueness assertion deliberately rejects a multi-unit panel for ordinary HAC.

## Python: randomization inference within blocks

clusters has one row per assigned cluster: cluster, block, assigned, y. y is a fixed cluster-level outcome summary. This tests a sharp no-effect null for complete randomization with a fixed treated count within each block and equal assignment probabilities within blocks. It weights blocks by their number of clusters.

~~~python
import numpy as np

c = clusters[["cluster", "block", "assigned", "y"]].dropna().reset_index(drop=True)
assert c["cluster"].is_unique
assert c["assigned"].isin([0, 1]).all()
blocks = list(c.groupby("block", sort=False).indices.values())
for idx in blocks:
    assert 0 < c.loc[idx, "assigned"].sum() < len(idx)

outcome = c["y"].to_numpy()
assignment = c["assigned"].to_numpy()
def statistic(a):
    return sum(
        len(idx) / len(c) * (
            outcome[idx][a[idx] == 1].mean()
            - outcome[idx][a[idx] == 0].mean()
        ) for idx in blocks
    )

observed = statistic(assignment)
rng = np.random.default_rng(12345)
B = 9999
draws = np.empty(B)
for b in range(B):
    permuted = assignment.copy()
    for idx in blocks:
        permuted[idx] = rng.permutation(assignment[idx])
    draws[b] = statistic(permuted)
p_value = (1 + np.sum(np.abs(draws) >= abs(observed))) / (B + 1)
print(observed, p_value)
~~~

Change the assignment simulator if randomization used unequal probabilities, matched pairs, restricted allocations or a different weighting estimand.
