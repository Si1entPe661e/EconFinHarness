# Sample and panel commands

These are inspection commands: run them while building the sample and keep them in an inspection script beside the analysis. In the delivered pipeline keep an assertion only where the program relies on the property, such as a unique key, a merge cardinality or the result of a declared cleaning rule.

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

For a declared discrete scale with support from `$lo` to `$hi` and a derived indicator:

~~~stata
list id x if !missing(x) & (x != round(x) | !inrange(x, $lo, $hi))
gen byte d = (x == 1) if !missing(x)
~~~

In Python use `(s == 1).where(s.notna())`; in R use `ifelse(is.na(x), NA, x == 1)`. A plain `x == 1` or `x != 1` assigns missing sources to a category.

Stata's missing values compare greater than finite numbers; the upper-bound check matters. L.y respects the declared calendar gaps. Check the using file's unit key directly if a merge reports repeated keys.

## Boundary counts on a fitted sample

Run these once in an inspection script after the estimation, not in the delivered pipeline, and cite the log lines. Reading code cannot show whether the values, indicators and totals on the rows actually fitted are what the specification declares. The [pipeline review](../pipeline-review-efh/SKILL.md) requires them on each primary fitted sample.

**Rows that move each regressor off its extreme values.** One or two rows means the regressor acts as an observation dummy.

~~~stata
* after the estimation command; $X lists the regressors as variables
foreach v of varlist $X {
    quietly summarize `v' if e(sample)
    local vmin = r(min)
    local vmax = r(max)
    quietly count if e(sample) & `v' != `vmin'
    local n_min = r(N)
    quietly count if e(sample) & `v' != `vmax'
    display "`v' " min(`n_min', r(N))
}
~~~

- R: `X <- model.matrix(fit)[, -1, drop = FALSE]; apply(X, 2, function(v) min(sum(v != min(v)), sum(v != max(v))))`
- Python (statsmodels): `{n: min((c != c.min()).sum(), (c != c.max()).sum()) for n, c in zip(res.model.exog_names, res.model.exog.T)}`; the constant shows 0.
- MATLAB (`fitlm`, numeric predictors): `X = table2array(mdl.Variables(mdl.ObservationInfo.Subset, mdl.PredictorNames)); min(sum(X ~= min(X)), sum(X ~= max(X)))`

**Groups whose members all carry the same value of a component.** Summing such a component over the group counts it once per member. A group-level value stored on every member row is normal; the problem is a total taken over it. Compare the count with the number of groups that have more than one member.

- Stata: `bysort g: egen double sd_x = sd(x)`, `egen byte first = tag(g)`, then `count if first & sd_x == 0`
- R: `d |> dplyr::summarise(n = dplyr::n(), k = dplyr::n_distinct(x), .by = g) |> dplyr::filter(n > 1, k == 1) |> nrow()`
- Python: `s = d.groupby("g")["x"].agg(["size", "nunique"]); int(((s["size"] > 1) & (s["nunique"] == 1)).sum())`
- MATLAB: `G = findgroups(T.g); n = splitapply(@numel, T.x, G); k = splitapply(@(v) numel(unique(v)), T.x, G); sum(n > 1 & k == 1)`

**Unmatched and repeated keys at a join.**

- Stata: `duplicates report key` in each file; `tabulate _merge` after the merge
- R: `anyDuplicated(b$key)`; `sum(!a$key %in% b$key)`
- Python: `b["key"].duplicated().sum()`; `(~a["key"].isin(b["key"])).sum()`
- MATLAB: `height(B) - numel(unique(B.key))`; `sum(~ismember(A.key, B.key))`

**Missing values in comparisons.** Each runtime turns a missing source into a category somewhere without an error.

| Runtime | Silent behavior | Safe form |
|---|---|---|
| Stata | Missing values exceed every number: `x > 0` and `x != 1` are true when `x` is missing; `x != .` keeps the extended codes `.a` to `.z`; `egen` `rowtotal()` and `total()` return 0 when every input is missing. | `gen byte d = (x == 1) if !missing(x)`; the `missing` option of `rowtotal()` and `total()` |
| R | `x == 1` is `NA` and propagates, but `x %in% 1` is `FALSE`; `case_when()` gives `NA` rows its default; `sum(na.rm = TRUE)` returns 0 for an all-missing group. | `ifelse(is.na(x), NA, x == 1)`; an `is.na(x) ~ NA_real_` branch first in `case_when()` |
| Python (pandas) | `s == 1` and `s > 0` are `False` for `NaN`; `np.where(s > 0, 1, 0)` returns 0; `groupby().sum()` returns 0 for an all-missing group. | `(s == 1).where(s.notna())`; `sum(min_count=1)` |
| MATLAB | `NaN == 1` and `NaN > 0` are false; `sum(x, "omitnan")` returns 0 for all-missing input. | `d = double(x == 1); d(isnan(x)) = NaN;` |

**Delivered checks after a declared rule.** Once a cleaning rule for a scale or a derived indicator is declared, later code relies on its result; assert it once, where the variable is created. `lo` and `hi` are the declared support (globals in Stata).

| Boundary | Stata | R | Python | MATLAB |
|---|---|---|---|---|
| Value domain | `assert x == round(x) & inrange(x, $lo, $hi) if !missing(x)` | `stopifnot(all(is.na(x) \| (x == round(x) & x >= lo & x <= hi)))` | `v = s.dropna(); assert ((v % 1 == 0) & v.between(lo, hi)).all()` | `assert(all(isnan(x) \| (x == round(x) & x >= lo & x <= hi)))` |
| Missing propagation, before a declared fill | `assert missing(d) if missing(x)` | `stopifnot(all(is.na(d[is.na(x)])))` | `assert d[x.isna()].isna().all()` | `assert(all(isnan(d(isnan(x)))))` |
