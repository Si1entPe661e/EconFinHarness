# Fama–MacBeth commands

df contains permno, date, ret_exc_lead1m, signal, size and bm. Predictors are known at date and ret_exc_lead1m is the next month's excess return. Accounting characteristics need actual publication lags. All returns below use one consistent scale.

## Python

~~~python
import pandas as pd
from linearmodels.panel import FamaMacBeth

cols = ["permno", "date", "ret_exc_lead1m", "signal", "size", "bm"]
d = df[cols].dropna().copy()
assert not d.duplicated(["permno", "date"]).any()
panel = d.set_index(["permno", "date"]).sort_index()
y = panel["ret_exc_lead1m"] * 100
X = panel[["signal", "size", "bm"]].copy()
X["Const"] = 1.0
fit = FamaMacBeth(y, X).fit(
    cov_type="kernel", kernel="newey-west", bandwidth=6, debiased=True)
print(fit.summary)
print(fit.all_params)
~~~

The index order is asset then date. bandwidth = 6 is illustrative; choose it for the frequency, persistence and return horizon. Inspect dates for which cross-sectional parameters could not be estimated.

## Stata

date is a regular numeric monthly index in this block.

~~~stata
isid permno date
xtset permno date
xtfmb ret_exc_lead1m signal size bm, lag(6)
~~~

xtfmb is user-written. This is a characteristic regression, not automatically a two-pass estimated-beta pricing test.

## R: explicit date-level slopes and HAC average

~~~r
library(sandwich)
library(lmtest)
d <- df[complete.cases(df[, c("date", "ret_exc_lead1m", "signal", "size", "bm")]), ]
slope_list <- lapply(split(d, d$date), function(g) {
  if (nrow(g) <= 4L) return(NULL)
  fit <- lm(ret_exc_lead1m ~ signal + size + bm, data = g)
  if (fit$rank < 4L) return(NULL)
  data.frame(date = g$date[1], signal_slope = coef(fit)[["signal"]])
})
slopes <- do.call(rbind, slope_list)
stopifnot(!is.null(slopes))
slopes <- slopes[order(slopes$date), ]
mean_fit <- lm(signal_slope ~ 1, data = slopes)
coeftest(mean_fit, vcov. = NeweyWest(mean_fit, lag = 6,
                                    prewhite = FALSE, adjust = TRUE))
~~~

Inspect missing calendar dates before applying this HAC calculation: dropping a date must not turn distant dates into adjacent periods. Retain all coefficient series if reporting a full Fama–MacBeth table.
