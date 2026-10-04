# Choose the result presentation

Use only the sections relevant to the requested output. Each table/figure should answer a recognizable research question.

| Result | What to show | Keep explicit |
|---|---|---|
| Sample and descriptive statistics | Observation/unit counts, time coverage, per-variable N, mean/SD and useful quantiles; restrictions when sample losses matter | Observation unit, missingness, weights and variable units. SD describes dispersion; it is not the SE of a mean. |
| Experimental or matched balance | Arm/group counts, baseline means, standardized differences and any design-appropriate joint test; weighted balance after matching | Randomization blocks/clusters or matching weights, overlap and retained population. Do not use independent-sample t tests automatically for a cluster experiment. |
| Regression and panel FE | Main coefficients or contrasts with selected SE/intervals, N, FE, controls, weights and cluster counts | Within versus overall fit; omitted/absorbed variables; meaningful sample differences. |
| IV and shift-share | First stage, reduced form, IV and relevant OLS comparison; excluded instruments, strength diagnostics and weak-IV inference when needed | Common sample/controls, diagnostic's name/distribution, shock-level inference where appropriate. A weak-IV confidence set can be unbounded or disconnected. |
| RCT | ITT contrasts, assigned/retained counts, baseline adjustment and attrition; compliance first stage/LATE only when justified | Assigned arm versus receipt, outcome families and multiplicity adjustment, effect units and randomization inference. |
| Matching | Before/after balance, overlap, unmatched treated units, effective weighted sample and ATT/ATE estimate | Retained target population, replacement/weights and matching-appropriate uncertainty. |
| DID and panel event study | Overall/cohort/dynamic ATT as appropriate; event-time estimate/interval plot and support; sensitivity if needed | Comparison group, omitted period, tail handling, cohort aggregation, anticipation, pointwise versus simultaneous bands. |
| RDD and diff-in-disc | Outcome jump or change in jumps, robust interval when available, bandwidths/order/kernel and effective N by side/cell; first stage if fuzzy | Local estimand and bias correction. A descriptive RD plot is not itself the estimator. A joint local-regression interval is not automatically bias-corrected RD inference. |
| Synthetic control | Treated/synthetic paths, gap, pre-fit, donor weights and placebo/sensitivity comparisons | Donor contamination, fit restrictions and what placebo ranks assume. |
| Bunching | Histogram, counterfactual density, exclusion region, excess/missing mass and sensitivity | Bin width, normalization, rounding, counterfactual choices and assumptions needed for any elasticity. |
| GMM and structural models | Parameters with supported uncertainty, moment/choice fit, important identifying/overidentification diagnostics and numerical convergence; counterfactual outcomes if requested | Normalizations, calibrated parameters, moment weights, simulation, preliminary-stage uncertainty and extrapolation. |
| ML nuisance estimation | Causal parameter/interval plus out-of-fold nuisance and overlap diagnostics | Score/estimand, fold unit, trimming and dependence; nuisance predictive accuracy is not the treatment estimate. |
| ML prediction and predictive regression | Held-out loss versus a feasible benchmark, evaluation N/dates, subgroup/time stability and forecast-comparison inference where justified | Feature/label timing, held-out split, overlapping horizons and tuning. Training metrics cannot be labelled test performance. |
| Fama–MacBeth | Mean date-level slopes and HAC uncertainty, dates used and cross-sectional coverage | Timing/scaling, generated betas where relevant, and period rather than stacked-observation inference. |
| Portfolio sorts and return event studies | Portfolio legs/spreads, factor-relative alpha or AR/CAR/BHAR with uncertainty; constituent/event counts and windows | Formation weights and breakpoints, simple versus compounded returns, benchmark and common-event dependence. |

## Arrange the output

Use separate panels or tables when outcomes have different units, estimands or uncertainty procedures. A compact layout can contain: sample/balance; main results; design diagnostics; sensitivity. Include only the pieces needed for the actual study, not every category by default.

Put detailed alternative specifications in an appendix when that improves the argument, while retaining results needed to judge the main claim. Do not hide unsuccessful reasonable variants or replace the main comparison with the most significant one.

For unbounded sets, missing estimates or irregular intervals, use an explicit value/label and a note. Do not force them into a symmetric coefficient-plus-SE cell.

## Read and export the right quantity

- fixest/modelsummary/esttab can export supported fitted models. Confirm the exporter retains the chosen covariance and reference distribution.
- Nonlinear effects should come from a marginal-effects/contrast result, including its own uncertainty.
- Event-study interaction-weighted estimates, group-time ATT, weak-IV sets, bootstrap p-values, forecast losses and fitted moments may need their method-specific numeric arrays/tables.
- When a package's generic model extractor omits the desired quantity, export the actual numeric result as a labelled data frame. Do not substitute the underlying raw regression coefficient.
