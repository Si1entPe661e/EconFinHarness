# Return event-study commands

daily has event_id, firm, event_date, tau, ret, rf, mktret and exposure. tau is trading-session event time already aligned to the announcement timestamp; ret/rf/mktret are simple decimal returns. Events can duplicate firm-day observations across separate event_id windows.

## Python: market-model AR and CAR

~~~python
import numpy as np
import pandas as pd
import statsmodels.api as sm

assert not daily.duplicated(["event_id", "tau"]).any()
rows = []
for event_id, event in daily.groupby("event_id"):
    estimation = event.loc[event["tau"].between(-250, -30)].dropna(
        subset=["ret", "rf", "mktret"])
    window = event.loc[event["tau"].between(-1, 1)].sort_values("tau")
    if len(estimation) < 120:
        continue
    if set(window["tau"]) != {-1, 0, 1}:
        continue
    if window[["ret", "rf", "mktret"]].isna().any().any():
        continue
    X = sm.add_constant(estimation["mktret"] - estimation["rf"],
                        has_constant="add")
    if np.linalg.matrix_rank(X) < 2:
        continue
    fit = sm.OLS(estimation["ret"] - estimation["rf"], X).fit()
    Xe = sm.add_constant(window["mktret"] - window["rf"],
                         has_constant="add")
    expected_excess = fit.predict(Xe)
    ar = window["ret"] - window["rf"] - expected_excess
    for col in ["firm", "event_date", "exposure"]:
        assert event[col].nunique(dropna=False) == 1
    rows.append({
        "event_id": event_id, "firm": event["firm"].iloc[0],
        "event_date": event["event_date"].iloc[0],
        "exposure": event["exposure"].iloc[0],
        "car": ar.sum(), "estimation_n": len(estimation),
    })
cars = pd.DataFrame(rows)
print(cars[["car", "estimation_n"]].describe())
~~~

The 120-observation rule and windows are illustrative. Report all excluded-event reasons and assess selection. This constructs CAR but does not yet provide an event-study variance accounting for estimated expected returns or event-induced dependence.

## R: cross-sectional exposure relation with two-way clustering

cars additionally contains predetermined size and baseline controls. event_date is the shared announcement-date dependence group.

~~~r
library(fixest)
fit <- feols(car ~ exposure + size + baseline, data = cars,
             cluster = ~firm + event_date)
summary(fit)
~~~

## Stata

~~~stata
regress car exposure size baseline, vce(cluster firm)
reghdfe car exposure size baseline, noabsorb vce(cluster firm event_date)
~~~

reghdfe is user-written. Two-way cluster inference needs enough firm and date groups; if all observations share one event date, this call cannot manufacture independent event-date variation. A different design/inference argument is needed.
