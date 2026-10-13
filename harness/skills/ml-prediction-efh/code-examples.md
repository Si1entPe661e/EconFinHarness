# Prediction commands

df contains y, x1, x2, x3 and unit. Features are available at the prediction origin. The first example evaluates generalization to unseen independent groups.

## Python: grouped holdout and grouped tuning

~~~python
import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import GroupKFold, GroupShuffleSplit, RandomizedSearchCV
from sklearn.pipeline import Pipeline

d = df.dropna(subset=["y", "unit"]).reset_index(drop=True)
X = d[["x1", "x2", "x3"]]
y = d["y"]
groups = d["unit"]
split = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=12345)
train, test = next(split.split(X, y, groups))
assert set(groups.iloc[train]).isdisjoint(set(groups.iloc[test]))
assert groups.iloc[train].nunique() >= 5
pipeline = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("rf", RandomForestRegressor(random_state=12345, n_jobs=1)),
])
search = RandomizedSearchCV(
    pipeline,
    param_distributions={
        "rf__n_estimators": [200, 500],
        "rf__max_depth": [None, 5, 10],
        "rf__min_samples_leaf": [5, 10, 20],
        "rf__max_features": ["sqrt", 0.5, 1.0],
    },
    n_iter=12, cv=GroupKFold(n_splits=5),
    scoring="neg_mean_squared_error", random_state=12345, n_jobs=-1,
)
search.fit(X.iloc[train], y.iloc[train], groups=groups.iloc[train])
prediction = search.predict(X.iloc[test])
benchmark = DummyRegressor(strategy="mean").fit(X.iloc[train], y.iloc[train])
baseline_prediction = benchmark.predict(X.iloc[test])
print(search.best_params_)
print({
    "rmse": np.sqrt(mean_squared_error(y.iloc[test], prediction)),
    "mae": mean_absolute_error(y.iloc[test], prediction),
    "benchmark_rmse": np.sqrt(mean_squared_error(y.iloc[test], baseline_prediction)),
})
~~~

The test groups are excluded from preprocessing and tuning. A random group holdout does not measure performance at future dates.

## Python: chronological tuning for a single time series

ts is one row per regularly spaced period with y_next, x1/x2/x3. y_next is a one-period-ahead target aligned with its forecast origin.

~~~python
from sklearn.model_selection import TimeSeriesSplit

ts = ts.sort_values("period").reset_index(drop=True)
assert ts["period"].is_unique
assert ts["period"].diff().dropna().eq(1).all()
cut = int(0.8 * len(ts))
train_ts = ts.iloc[:cut - 1].dropna(subset=["y_next"])
test_ts = ts.iloc[cut:].dropna(subset=["y_next"])
temporal_search = RandomizedSearchCV(
    pipeline,
    param_distributions=search.param_distributions,
    n_iter=12, cv=TimeSeriesSplit(n_splits=5, gap=1),
    scoring="neg_mean_squared_error", random_state=12345, n_jobs=-1,
)
temporal_search.fit(train_ts[["x1", "x2", "x3"]], train_ts["y_next"])
future_prediction = temporal_search.predict(test_ts[["x1", "x2", "x3"]])
print(np.sqrt(mean_squared_error(test_ts["y_next"], future_prediction)))
~~~

gap = 1 purges a one-period label overlap. Longer horizons or delayed labels require a larger purge based on actual realization dates. Do not reuse this row splitter unchanged for panel rows.
