# Panel FE commands

df contains unique unit/period observations, y, x, baseline, region and weight. region-by-period FE identify x only from variation remaining within those cells and units.

## R

~~~r
library(fixest)
one <- feols(y ~ x + baseline | unit, data = df, cluster = ~unit)
two <- feols(y ~ x + baseline | unit + period, data = df, cluster = ~unit)
region_time <- feols(y ~ x + baseline | unit + region^period,
                    data = df, cluster = ~unit)
weighted <- feols(y ~ x + baseline | unit + period,
                 data = df, weights = ~weight, cluster = ~unit)
etable(one, two, region_time, weighted)
~~~

Inspect dropped variables and observations. A coefficient omitted due to collinearity is not a zero effect.

## Stata

~~~stata
isid unit period
xtset unit period
xtreg y x baseline i.period, fe vce(cluster unit)
reghdfe y x baseline, absorb(unit period) vce(cluster unit)
reghdfe y x baseline, absorb(unit region#period) vce(cluster unit)
~~~

xtreg and reghdfe can differ in singleton handling and degrees-of-freedom corrections. A lagged outcome requires a separate dynamic-panel argument.

## Python

~~~python
from linearmodels.panel import PanelOLS

cols = ["unit", "period", "y", "x", "baseline"]
d = df[cols].dropna().copy()
assert not d.duplicated(["unit", "period"]).any()
panel = d.set_index(["unit", "period"]).sort_index()
model = PanelOLS.from_formula(
    "y ~ 1 + x + baseline + EntityEffects + TimeEffects",
    data=panel, drop_absorbed=True,
)
fit = model.fit(cov_type="clustered", cluster_entity=True, debiased=True)
print(fit.summary)
print(fit.nobs, fit.rsquared_within)
~~~

The MultiIndex order must be entity then time. Do not create calendar lags using row shifts across gaps.
