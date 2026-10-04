# Sample and panel commands

Use df with unit, period, y, x, treated and weight. period is an integer calendar index at one frequency, such as month number; treated is binary. lookup contains unit and region with at most one record per unit. Do not automatically drop conflicting duplicates.

## Python

~~~python
import numpy as np
import pandas as pd

key = ["unit", "period"]
assert df[key].notna().all().all(), "Missing panel key"
duplicates = df.loc[df.duplicated(key, keep=False)].sort_values(key)
print(duplicates)
assert duplicates.empty, "Resolve duplicate keys before continuing"
assert lookup["unit"].notna().all()
assert lookup["unit"].is_unique
print(lookup.loc[~lookup["unit"].isin(df["unit"])])
panel = df.merge(lookup, on="unit", how="left", validate="many_to_one",
                 indicator=True)
print(panel["_merge"].value_counts())
panel = panel.sort_values(key).copy()
gap = panel.groupby("unit")["period"].diff()
previous_y = panel.groupby("unit")["y"].shift()
panel["lag_y"] = previous_y.where(gap.eq(1))
reversals = panel.groupby("unit")["treated"].diff().lt(0)
print(panel.loc[reversals, key + ["treated"]])
first = panel["period"].where(panel["treated"].eq(1))
panel["first_treated"] = first.groupby(panel["unit"]).transform("min")
panel["event_time"] = panel["period"] - panel["first_treated"]
print(panel[["y", "x", "treated", "weight"]].isna().sum())
bad_weight = ~np.isfinite(panel["weight"]) | panel["weight"].lt(0)
print(panel.loc[bad_weight, key + ["weight"]])
print(panel.groupby("unit").size().describe())
print(panel.groupby("period")["unit"].nunique())
~~~

The reversal check assumes binary, observed treatment. Missing treatment requires inspection rather than being filled as untreated. first_treated is NaN for never-treated units; recode it only for the chosen estimator's interface.

## R: keys and calendar lags without a new dependency

~~~r
key <- c("unit", "period")
stopifnot(!anyNA(df[, key]))
dups <- duplicated(df[, key]) | duplicated(df[, key], fromLast = TRUE)
print(df[dups, ])
stopifnot(!any(dups))
d <- df[order(df$unit, df$period), ]
d$lag_y <- NA_real_
for (u in unique(d$unit)) {
  idx <- which(d$unit == u)
  if (length(idx) > 1L) {
    current <- idx[-1L]
    previous <- idx[-length(idx)]
    consecutive <- d$period[current] - d$period[previous] == 1
    d$lag_y[current[consecutive]] <- d$y[previous[consecutive]]
  }
}
print(colSums(is.na(d[, c("y", "x", "treated", "weight")])))
print(summary(table(d$unit)))
stopifnot(all(is.finite(d$weight)), all(d$weight >= 0))
~~~

## Stata

lookup.dta is an existing unit-level lookup file. Inspect merge losses before restricting to matched observations.

~~~stata
assert !missing(unit, period)
duplicates report unit period
duplicates list unit period
isid unit period
xtset unit period
xtdescribe
gen lag_y = L.y
bysort unit (period): gen reversal = treated < treated[_n-1] if _n > 1 & !missing(treated, treated[_n-1])
list unit period treated if reversal == 1
bysort unit: egen first_treated = min(cond(treated == 1, period, .))
gen event_time = period - first_treated
merge m:1 unit using "lookup.dta"
tabulate _merge
misstable summarize y x treated weight
assert weight >= 0 & weight < .
~~~

Stata's missing values compare greater than finite numbers; the upper-bound check matters. L.y respects the declared calendar gaps. Check the using file's unit key directly if a merge reports repeated keys.
