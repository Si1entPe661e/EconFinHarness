# Regression commands

df contains y, x, baseline, unit and weight; binary_y is 0/1 and count_y is nonnegative. unit is the chosen cluster. Model calls assume complete inputs and economically appropriate controls.

## R

~~~r
library(fixest)
ols <- feols(y ~ x + baseline, data = df, cluster = ~unit)
wls <- feols(y ~ x + baseline, data = df, weights = ~weight, cluster = ~unit)
ppml <- fepois(count_y ~ x + baseline, data = df, cluster = ~unit)
interaction <- feols(y ~ x * baseline, data = df, cluster = ~unit)
etable(ols, wls, ppml, interaction)
~~~

The PPML coefficient exponentiates to a multiplicative conditional mean effect for a one-unit regressor change; with interactions its effect depends on the interacting variable.

## Stata

~~~stata
regress y c.x##c.baseline, vce(cluster unit)
margins, dydx(x) at(baseline=(0 1 2))
regress y x baseline [aw=weight], vce(cluster unit)
logit binary_y x baseline, vce(cluster unit)
margins, dydx(x)
poisson count_y x baseline, vce(cluster unit)
~~~

Analytic weights are illustrated here; survey probability weights require the intended survey design.

## Python

~~~python
import statsmodels.formula.api as smf
cols = ["y", "x", "baseline", "unit"]
d = df[cols].dropna().copy()
fit = smf.ols("y ~ x * baseline", data=d).fit(
    cov_type="cluster", cov_kwds={"groups": d["unit"], "use_correction": True},
    use_t=True,
)
print(fit.summary())
b = df[["binary_y", "x", "baseline", "unit"]].dropna().copy()
logit = smf.logit("binary_y ~ x + baseline", data=b).fit(
    disp=False, cov_type="cluster", cov_kwds={"groups": b["unit"]})
print(logit.get_margeff(at="overall").summary())
~~~

The cluster vector must match rows used by the model. For causal contrasts, covariate adjustment and marginalization need an explicit identification argument.
