---
name: predictive-regression
description: Time-series predictive regressions with predetermined predictors, overlapping return horizons and genuinely out-of-sample forecasts. Address persistent predictors, finite-sample bias, HAC and benchmark comparisons.
kind: method
---

# Predictive regressions

## When to use

Use for forecasting future outcomes/returns from information available at the forecast origin. A contemporaneous regression or a full-sample fitted value is not an out-of-sample forecast.

## Inputs

Regular time index, forecast origin/target horizon, predictor release dates, return units, expanding/rolling training rule, benchmark, initial evaluation date and dependence/inference assumptions.

## Procedure

1. Align x_t with the intended future y. Verify calendar continuity and publication lags. For an h-period target, specify sum/compound/average returns and overlapping origins.
2. State the in-sample regression and dependence. Persistent predictors correlated with return innovations can generate finite-sample bias; ordinary HAC addresses covariance, not that bias.
3. Use justified persistent-predictor/weak-predictability inference when necessary, and explain stationarity assumptions. A conventional t-statistic alone may be misleading.
4. Choose an expanding/rolling forecast rule and initial training period before evaluation. At each origin, use only outcomes already realized and transformations/tuning fitted on available training data.
5. Compare with a feasible benchmark, such as the recursive historical mean; report MSE, out-of-sample R-squared and stability by period. Do not select the evaluation interval by performance.
6. Handle overlapping forecast errors with horizon-compatible dependence. For nested forecast comparisons use a suitable nested-model test, such as Clark–West under its assumptions, rather than automatically using an ordinary loss-difference test.
7. Distinguish statistical predictive gains from implementation claims. Transaction costs, risk and model selection require separate evidence; report unsuccessful variants when relevant.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives explicit forward-horizon construction/HAC and recursive one-step forecasts. Return timing, evaluation sample, feasible benchmark, forecast metrics and the inferential limitations.
