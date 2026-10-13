# Predictive-regression commands

df contains period (consecutive integer month index), ret (simple decimal return) and x known at period's end. The first block predicts the next 12 months' sum of log returns; the second is a separate one-month simple-return forecasting exercise.

## R: overlapping 12-month target and HAC

~~~r
library(sandwich)
library(lmtest)
d <- df[order(df$period), ]
stopifnot(!anyDuplicated(d$period), all(diff(d$period) == 1),
          all(d$ret > -1, na.rm = TRUE))
h <- 12L
d$future_log_return <- NA_real_
if (nrow(d) > h) {
  for (i in seq_len(nrow(d) - h)) {
    future <- d$ret[seq.int(i + 1L, i + h)]
    if (all(is.finite(future))) d$future_log_return[i] <- sum(log1p(future))
  }
}
s <- d[complete.cases(d[, c("period", "future_log_return", "x")]), ]
stopifnot(all(diff(s$period) == 1))
fit <- lm(future_log_return ~ x, data = s)
coeftest(fit, vcov. = NeweyWest(fit, lag = h - 1L,
                               prewhite = FALSE, adjust = TRUE))
~~~

h-1 is a minimum overlap-based choice; additional persistence may require longer dependence treatment. These HAC SE do not correct persistent-predictor finite-sample bias.

## Python: recursive one-step forecasts and feasible historical mean

~~~python
import numpy as np
import pandas as pd
import statsmodels.api as sm

d = df[["period", "ret", "x"]].sort_values("period").reset_index(drop=True)
assert d["period"].is_unique
assert d["period"].diff().dropna().eq(1).all()
d["target"] = d["ret"].shift(-1)
initial_training = 120
rows = []
for origin in range(initial_training, len(d) - 1):
    # Rows before origin have next-month targets realized by this origin.
    train = d.iloc[:origin].dropna(subset=["x", "target"])
    current = d.iloc[origin]
    if len(train) < initial_training or not np.isfinite(current["x"]):
        continue
    X = sm.add_constant(train[["x"]], has_constant="add")
    fit = sm.OLS(train["target"], X).fit()
    forecast = float(fit.predict([[1.0, current["x"]]])[0])
    rows.append({
        "period": current["period"], "actual": current["target"],
        "forecast": forecast, "benchmark": train["target"].mean(),
    })
evaluation = pd.DataFrame(rows).dropna()
e_model = evaluation["actual"] - evaluation["forecast"]
e_benchmark = evaluation["actual"] - evaluation["benchmark"]
r2_oos = 1 - (e_model**2).mean() / (e_benchmark**2).mean()
print(r2_oos, len(evaluation))
# Clark-West adjusted loss differential for the nested mean vs linear model.
cw = e_benchmark**2 - e_model**2 + (
    evaluation["benchmark"] - evaluation["forecast"])**2
assert evaluation["period"].diff().dropna().eq(1).all()
cw_fit = sm.OLS(cw, np.ones((len(cw), 1))).fit(
    cov_type="HAC", cov_kwds={"maxlags": 6, "use_correction": True})
print(cw_fit.params, cw_fit.tvalues)
~~~

A positive adjusted-loss mean favors the larger model; inference is one-sided under the relevant nested-model conditions. The displayed HAC t-value is not a universal finite-sample test. For h > 1, purge training origins whose targets are not fully realized at the forecast date.
