## Procedure

1. Write the estimand and comparison group. Overall ATT, cohort-time ATTs, or dynamic effects by relative time; comparison from never-treated, not-yet-treated, or both. Record whether the design has one adoption date (two-way fixed effects is a natural estimator) or staggered adoption with possibly heterogeneous effects (two-way fixed effects can weight some comparisons negatively; choose a heterogeneity-robust estimator or justify TWFE).
2. Build the treatment variables explicitly: cohort (first treatment period), relative time, post indicator; define the never-treated cohort code the estimator expects. Check that units switch on once (no reversals) or document reversals and choose an estimator that handles them.
3. Run the panel checks (`panel-data-checks-efh`): unit-time uniqueness, balance, singleton units, treatment timing consistency across periods, the number of treated cohorts and the sample size per relative time.
4. Choose the estimator and record the choice: TWFE with leads and lags (binned endpoints, a stated reference period); Callaway-Sant'Anna group-time ATTs; Sun-Abraham interaction-weighted event study; de Chaisemartin-D'Haultfoeuille; Borusyak-Jaravel-Spiess imputation; stacked regression; synthetic DID. State the reference period and how endpoints are binned. Use a Goodman-Bacon decomposition as a diagnostic when TWFE is reported for staggered designs.
5. Inference: cluster at the level of treatment assignment (state, firm, district) and pass the cluster variable into the estimation call; report the number of clusters; with few clusters plan a wild cluster bootstrap or randomization inference. For multi-way dependence, state the rationale.
6. Diagnostics with decision rules written before estimation: pre-trend plot and test on leads (report both, with the caution that pre-testing changes inference), balance of covariates between treated and comparison units, heterogeneous treatment effect diagnostics for staggered designs (Bacon weights, comparison of TWFE with a robust estimator), sensitivity to parallel-trend violations (HonestDiD-style bounds) where the plan calls for it.
7. Robustness: alternative comparison group (never-treated only), alternative estimator, sample restrictions (drop always-treated, trim relative-time window), alternative fixed effects (unit and time versus unit-specific trends), alternative clustering.
8. Outputs from code: event-study plot with the reference period marked and confidence bands; tables with N, clusters, fixed effects, SE type, weights and the estimator; every column mapped to a plan specification id; JSON with the estimator options.

### Software commands

Use [code-examples.md](../code-examples.md) for complete calls and the required variables. Choose the sample, comparison group, weights and inference settings for the current research design.

- R: `fe3 = felm(allunits~Before+After+Chain|as.factor(BUYER_ZIP)+as.factor(Date)|0|BUYER_ZIP, data=d)` after loading `lfe`. The examples also cover `feols` TWFE and `sunab` event studies, `att_gt` and `aggte`, `synthdid_estimate`, and `bacondecomp::bacon`.
- Stata: `did_imputation trade bvd_id year Ei, fe(bvd_id year year#country_num) autosample cluster(BankID_num) tol(0.1)`. The examples also cover `reghdfe`, `eventstudyinteract`, `csdid` and `csdid_estat event`, dynamic imputation with `pretrends(18)`, legacy `did_multiplegt`, nonlinear `jwdid`, `bacondecomp`, and `honestdid`.
- Python: `model = PanelOLS(y, X, entity_effects=True, time_effects=True, drop_absorbed=True)` followed by `result = model.fit(cov_type='clustered', cluster_entity=True)`. The example includes imports, the panel index and the treatment-by-post regressor.

The option is `pretrends()`. Legacy `did_multiplegt` options require the matching interface; `did_multiplegt_dyn` uses different arguments.

## Missing information

- Treatment timing missing for some units: exclude them and record it as a sample restriction with the count, or treat as never-treated only with a stated reason.
- Unclear assignment level: report the clustering choice as unresolved and give two alternatives in the plan.
- No never-treated units: use not-yet-treated comparisons and say that long-run effects are not identified for the last cohort.
- Corpus card fields null: unknown, never "not done".
