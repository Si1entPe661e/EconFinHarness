---
name: ml-prediction
description: Machine learning prediction with leakage-safe preprocessing, group/time splits, training-only tuning, benchmarks and held-out evaluation. Use for prediction, not causal identification or nuisance-score inference.
kind: method
---

# Machine learning prediction

## When to use

Use to predict outcomes, classify events or compare forecasting models. Use ml-nuisance when predictions enter an orthogonal causal score; predictive accuracy alone is not a causal estimate.

## Inputs

Target and prediction horizon, feature availability dates, sample/independent groups, time ordering, evaluation unit, training/validation/test split, benchmark, loss metric and deployment or research use.

## Procedure

1. Define what is predicted and when. Inspect leakage from future labels, revised data, post-event features and duplicated/related units.
2. Choose splits matching generalization: unseen groups need group splits; forecasting needs chronological splits; repeated panel dates often require date-based blocks plus appropriate group treatment. Do not apply row-wise TimeSeriesSplit to a panel with mixed same-date rows.
3. Fit imputation, scaling, selection and dimensionality reduction inside the training pipeline. Tune within training/validation; retain a final untouched evaluation set.
4. Compare simple feasible benchmarks with the flexible model using a prespecified loss. Match classification metrics to imbalance and costs; choose probability thresholds/calibration using training/validation only.
5. Evaluate once on the held-out population/time span, preserving dependence in intervals or resampling. Report subgroup and temporal performance, missingness and coverage rather than only the best aggregate score.
6. Distinguish feature importance or SHAP associations from causal explanations. Correlated predictors and distribution shifts affect attribution and transportability.
7. When predictions form portfolios or treatment heterogeneity groups, form them out of sample and apply the corresponding finance/causal skill's inference. Model selection over many variants needs an honest evaluation strategy.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) gives a complete group-split random-forest pipeline with training-only randomized search, plus a chronological alternative for one time series.

Return split/feature timing, held-out metrics versus benchmark, selected tuning values and material limits.
