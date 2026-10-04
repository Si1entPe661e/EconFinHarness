# Portfolio-sort commands

stocks contains unique permno/month rows, signal, me, ret and exchange. month is a consecutive integer calendar-month index; exchange = "NYSE" defines breakpoints. signal in month t is assumed observable by t's end; if release dates are later, align availability first. ret includes the chosen delisting-return treatment.

## Python: monthly lagged-signal value-weighted deciles

~~~python
import numpy as np
import pandas as pd

d = stocks.sort_values(["permno", "month"]).copy()
assert not d.duplicated(["permno", "month"]).any()
groups = d.groupby("permno", sort=False)
consecutive = groups["month"].diff().eq(1)
d["signal_lag"] = groups["signal"].shift().where(consecutive)
d["me_lag"] = groups["me"].shift().where(consecutive)
formation = d.dropna(subset=["signal_lag", "me_lag", "exchange"]).copy()
formation = formation[formation["me_lag"] > 0]
rows = []
for month, assets in formation.groupby("month"):
    reference = assets.loc[assets["exchange"].eq("NYSE"), "signal_lag"]
    if len(reference) < 10:
        continue
    cuts = reference.quantile(np.arange(0.1, 1.0, 0.1)).to_numpy()
    if not np.all(np.diff(cuts) > 0):
        raise ValueError("Tied breakpoints: choose fewer portfolios or a justified tie rule")
    assets = assets.copy()
    assets["portfolio"] = pd.cut(
        assets["signal_lag"], bins=np.r_[-np.inf, cuts, np.inf],
        labels=range(1, 11), include_lowest=True).astype(int)
    assert assets["ret"].notna().all(), "Resolve missing realized returns without future-based exclusions"
    for portfolio, members in assets.groupby("portfolio"):
        rows.append({
            "month": month, "portfolio": portfolio, "n_assets": len(members),
            "return": np.average(members["ret"], weights=members["me_lag"]),
        })
returns = pd.DataFrame(rows)
wide = returns.pivot(index="month", columns="portfolio", values="return")
wide["high_minus_low"] = wide[10] - wide[1]
print(returns)
print(wide["high_minus_low"].describe())
~~~

Missing future returns trigger inspection; they do not determine membership. Missing bins remain missing. This implements one-month holdings; overlapping multi-month strategies need explicit formation cohorts.

## Stata: time-series factor adjustment

The current data have one row per month, exret1 is a portfolio excess return or a high-minus-low spread, and factors use the same return scale.

~~~stata
tsset month
newey exret1, lag(6)
newey exret1 mktrf smb hml mom, lag(6)
newey exret1 mktrf smb hml mom rmw cma, lag(6)
~~~

## R: factor-model alpha

~~~r
library(sandwich)
library(lmtest)
d <- portfolio_series[complete.cases(portfolio_series[, c("month", "spread", "mktrf", "smb", "hml")]), ]
d <- d[order(d$month), ]
stopifnot(!anyDuplicated(d$month), all(diff(d$month) == 1))
fit <- lm(spread ~ mktrf + smb + hml, data = d)
coeftest(fit, vcov. = NeweyWest(fit, lag = 6, prewhite = FALSE, adjust = TRUE))
~~~

The intercept is model-relative alpha. A long-short zero-investment spread already cancels a common risk-free return; a single long portfolio requires excess-return construction.
