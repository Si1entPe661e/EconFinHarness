# Panel event-study commands

## R: Sun–Abraham staggered-adoption dynamics

df contains y, unit, year and cohort (first treatment year). year is a calendar-year integer; cohort = 9999 denotes never treated, outside the observed year range. Treatment is absorbing. Remove or separately handle always-treated units lacking pretreatment comparisons.

~~~r
library(fixest)
stopifnot(!anyDuplicated(df[, c("unit", "year")]))
fit <- feols(y ~ sunab(cohort, year, ref.p = -1) | unit + year,
             data = df, cluster = ~unit)
summary(fit)
iplot(fit, ref.line = 0, xlab = "Years relative to treatment",
       main = "Dynamic treatment effects")
att <- summary(fit, agg = "ATT")
print(att)
~~~

The package aggregates cohort-specific effects by relative period; inspect support before comparing distant lags. The plot's usual intervals are pointwise, not a simultaneous confidence band.

## Stata: interacted cohort event study

first_treat is the first treatment year and missing for never-treated units. The sample is an absorbing-adoption panel. These examples bin tails at -5 and +5 and omit -1.

~~~stata
isid unit year
gen never = missing(first_treat)
gen relative = year - first_treat if never == 0
forvalues k = 0/4 {
    gen L`k' = (relative == `k') & never == 0
}
gen L5 = relative >= 5 & relative < . & never == 0
forvalues k = 2/4 {
    gen F`k' = (relative == -`k') & never == 0
}
gen F5 = relative <= -5 & never == 0
eventstudyinteract y F5 F4 F3 F2 L0 L1 L2 L3 L4 L5, absorb(unit year) cohort(first_treat) control_cohort(never) vce(cluster unit)
matrix list e(b_iw)
matrix list e(V_iw)
~~~

eventstudyinteract is user-written. Its interaction-weighted estimates/covariance are in e(b_iw)/e(V_iw), rather than the unaggregated regression coefficients. Tail bins pool potentially different effects; change them deliberately rather than treating them as automatic defaults.
