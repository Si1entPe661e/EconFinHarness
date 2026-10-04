# Cross-fitted nuisance commands

df contains y, d, pretreatment x1/x2/x3 and unit. unit groups dependent observations; groups are independently sampled and numerous enough for cluster inference. This is the partially linear model y = theta*d + g(X) + error. It is not an unrestricted heterogeneous-treatment ATE estimator.

## Python: grouped cross-fitting and PLR

~~~python
import numpy as np
import statsmodels.api as sm
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GroupKFold

cols = ["y", "d", "x1", "x2", "x3", "unit"]
sample = df[cols].dropna().reset_index(drop=True)
X = sample[["x1", "x2", "x3"]].to_numpy()
y = sample["y"].to_numpy()
d = sample["d"].to_numpy()
groups = sample["unit"].to_numpy()
assert sample["unit"].nunique() >= 5
y_hat = np.full(len(sample), np.nan)
d_hat = np.full(len(sample), np.nan)
folds = GroupKFold(n_splits=5)
for train, test in folds.split(X, y, groups):
    outcome = RandomForestRegressor(
        n_estimators=500, min_samples_leaf=10, max_features=1.0,
        random_state=12345, n_jobs=-1)
    treatment = RandomForestRegressor(
        n_estimators=500, min_samples_leaf=10, max_features=1.0,
        random_state=54321, n_jobs=-1)
    outcome.fit(X[train], y[train])
    treatment.fit(X[train], d[train])
    y_hat[test] = outcome.predict(X[test])
    d_hat[test] = treatment.predict(X[test])
assert np.isfinite(y_hat).all() and np.isfinite(d_hat).all()
y_residual = y - y_hat
d_residual = d - d_hat
assert np.mean(d_residual**2) > 1e-8
fit = sm.OLS(y_residual, d_residual[:, None]).fit(
    cov_type="cluster",
    cov_kwds={"groups": groups, "use_correction": True},
    use_t=True,
)
print(fit.params, fit.conf_int())
score = d_residual * (y_residual - fit.params[0] * d_residual)
print(np.mean(score), np.mean(d_residual**2))
~~~

The regression SE correspond to the PLR score under its asymptotic conditions. Grouped folds address training leakage across units; they do not guarantee those conditions or solve few-cluster inference. Hyperparameters here are illustrative; tune within the training fold if tuning is needed.

For binary-treatment ATE, the out-of-fold score instead is m1(X)-m0(X) + D*(Y-m1(X))/e(X) - (1-D)*(Y-m0(X))/(1-e(X)). Use arm-specific fits, overlap checks and the influence function for that target rather than relabeling the PLR result.
