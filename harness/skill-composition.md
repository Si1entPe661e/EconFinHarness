# Composing research skills

For general task routing, project management, reports and resumable execution, start with [orchestration](orchestration/README.md). This document is the empirical-analysis branch; a nonresearch task does not need to load the method table below.

Choose the relevant skills for a compound research task. A focused explanation, annotation, presentation change or bug fix needs only the relevant steps. Roles describe responsibilities; combining skills does not require multiple agents or a separate review.

## Choose the method first

Start with the question, estimand and data structure. Preserve an existing design when it remains applicable, and read only the skills and command examples needed for the task.

| Question or data structure | Main method and relevant branches |
|---|---|
| Conditional associations; linear or nonlinear regression | `regression-efh`; use `panel-fe-efh` for absorbed panel effects. A regression command alone does not establish causal identification. |
| Within-unit variation; one-way or multiple fixed effects | `panel-fe-efh`; route staggered policy adoption to `did-efh`. For short panels with lagged outcomes, consider dynamic bias and the moment conditions in `gmm-efh`. |
| Before/after comparisons or staggered treatment adoption | `did-efh`; use `event-study-efh` for dynamics and support. Do not substitute ordinary TWFE automatically for a heterogeneity-compatible estimator. |
| Dynamic responses around panel events | `event-study-efh`; use `did-efh` when identification comes from absorbing adoption. Repeated events and continuous shocks require their own design. |
| Treatment jumps at a known running-variable threshold | `rdd-efh`; the fuzzy branch requires a local first stage and appropriate inference. |
| A cutoff jump changes across periods or groups | `diff-in-disc-efh`, with `rdd-efh` for local support; assess stability of other cutoff effects and joint inference. |
| Excluded instruments shift an endogenous regressor | `iv-efh`; select branches for leniency, weak instruments or multiple endogenous regressors as needed. |
| Baseline shares multiplied by common shocks | `shift-share-efh`; also use `iv-efh` when exposure is an instrument. Distinguish shares-based and shocks-based identification and inference. |
| Randomized assignment | `rct-efh`; a noncompliance LATE also needs `iv-efh` conditions. Keep ITT defined by assignment. |
| Treatment/control matching on observed variables | `matching-efh`; a subsequent DID must preserve matching weights and satisfy `did-efh` assumptions. |
| Few treated units with credible donor trajectories | `synthetic-control-efh`; synthetic DID belongs to the corresponding `did-efh` branch. |
| Distributional bunching around a kink or notch | `bunching-efh`; density mass is not an RD outcome jump. |
| Explicit orthogonality conditions; IV-GMM or dynamic-panel moments | `gmm-efh`; consult `iv-efh` for linear-IV validity. Arbitrary lags are not automatically valid instruments. |
| Behavioral or equilibrium parameters and counterfactuals | `structural-estimation-efh`; combine with `gmm-efh` for GMM/SMM while preserving solution and simulation steps. |
| Machine learning assists causal estimation | `ml-nuisance-efh` and the underlying design. IV/DID needs valid design-specific orthogonal scores, not a relabeled ordinary PLR. |
| Average repeated cross-sectional slopes | `fama-macbeth-efh`; infer from the slope time series and address generated-beta uncertainty when applicable. |
| Asset sorts, portfolio returns and factor adjustment | `portfolio-sorts-efh`; ML-generated signals need out-of-sample formation under `ml-prediction-efh`. |
| Announcement abnormal returns; CAR/BHAR | `return-event-study-efh`; distinguish this from panel treatment-effect `event-study-efh`, and check event dates and dependence. |
| Time-series predictive regressions; rolling or recursive forecasts | `predictive-regression-efh`; retain feature availability, target realization dates, overlapping horizons and feasible benchmarks. |
| Classification or ML prediction | `ml-prediction-efh`; use group/time splits and keep tuning and transformations away from the test sample. Prediction accuracy does not establish a causal effect. |

Skills live at `harness/skills/<name>/SKILL.md`. Method choice is a research judgment, not a keyword rule that activates every branch.

## Shared analysis sequence

1. **Specify the research choices.** Define the estimand, sample, variables, weights, comparison group, model and identification assumptions. Use `literature-verification-efh` for claims that need sources.
2. **Construct the applicable sample.** Use relevant `panel-data-checks-efh` for observation units, keys, dates, merges, missingness, treatment timing and weights. Prediction tasks also retain splits and label availability.
3. **Choose the model and inference.** The main method defines the estimand, controls, fixed effects and specific diagnostics. `inference-clustering-efh` handles dependence, standard errors, intervals and tests. Decide fixed effects and clustering separately. Preserve specialized RD, matching, weak-IV, bootstrap and randomization inference.
4. **Fit the model and inspect its actual sample.** Keep variable definitions and selected weights, effects and inference consistent. Inspect losses from missingness, singletons, collinearity, bandwidths, matching or support restrictions. Compute N and cluster counts from fitted observations. Use a common comparison sample when appropriate, or explain sample differences.
5. **Present the same analysis.** `tables-figures-efh` reads fitted objects or method-specific numerical results using `harness/workflows/present-results.md`. Keep coefficients, SEs, p-values, intervals, stars, N and notes consistent. Diagnostics and evaluation metrics retain their own applicable samples. Before delivering a pipeline of several scripts, run the [pipeline review](workflows/pipeline-review.md).
6. **Explain or write.** Use `research-explanation-efh` for explanation and `academic-writing-efh` for prose. Preserve the actual estimand, sample, units and uncertainty rather than reconstructing numbers from rounded tables. Finish drafted prose with the [revise module](workflows/revise-writing.md).

Continue using existing variables, fitted objects, scripts and output paths. A short explanation or parameters in the analysis script are usually sufficient for coordination.

## Revisit affected steps

| Change or finding | What to revisit |
|---|---|
| Variables, merges, missingness, weights or sample restrictions change | Recheck the sample and affected models; update N, clusters, diagnostics and outputs. |
| Fixed effects absorb key variables or remove singletons | Check remaining identifying variation and fitted observations. An absorbed coefficient is not zero. |
| Few clusters, concentrated treatment or spatial/time dependence | Revisit inference; update estimates or uncertainty where needed, together with tables and conclusions. |
| Weak first stage, poor local support, poor donor fit or inadequate overlap | Return to the method's identification, support and inference branches. Formatting cannot resolve these issues. |
| Covariance, bootstrap p-values or interval rules change | Update affected SEs, p-values, intervals, stars, plots and prose. A covariance-only change does not require changing point estimates. |
| Prediction splits, features or label realization dates change | Refit and tune on permissible training observations; regenerate evaluation and portfolio results. |
| Exported results disagree with fitted objects | Correct extraction, model selection or formatting. Do not alter estimates to match an export. |
| Only labels, rounding or layout change | Re-export the affected output using the existing model and inference. |

## Role coordination

- `empirical-analyst`: research choices, the main method and identification assumptions, together with appropriate inference.
- `code-engineer`: implement the same design in [lean code](skills/pipeline-review-efh/references/lean-code.md), retain its actual sample and inference, and produce results.
- `writer` / `explainer`: use existing results for prose or explanation; flag numerical or estimand conflicts.
- `reviewer`: inspect the requested claim or a concrete issue in method, sample, inference or export.
- `pipeline-reviewer`: before delivery and check-only, keep boundary guards and find misplaced comparison, variant and run code and missing boundary checks.
- `literature`: provide verified literature and implementation sources for the current question.
- `project-manager`: coordinate necessary dependencies, responsibilities and progress for larger tasks.

One agent may perform several roles. A handoff states the research choices, actual files or objects, completed work and missing inputs. Continue existing work and explain substantive gaps while completing unaffected steps.

## Entry points

Use [empirical analysis](workflows/empirical-analysis.md) for a full implementation and [result presentation](workflows/present-results.md) for exports. Enter design, replication, review or writing workflows at the relevant step.
