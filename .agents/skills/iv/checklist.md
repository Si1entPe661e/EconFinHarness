# iv checklist (answer yes / no / unknown; "unknown" is a legitimate answer and must be reported as such)

Identification

1. Is the exclusion restriction argued from the design, not from first-stage significance?
2. Is independence (as-good-as-random assignment of the instrument, conditional on stated controls) argued and are those controls in every stage?
3. Is monotonicity discussed and are the compliers named?
4. Is the estimand written (LATE for which compliers; weighted average under heterogeneity)?

Instrument construction

5. Is the instrument built in code from pre-treatment information only?
6. For shift-share: are shares, shocks and the base period recorded, and is the source of exogeneity (shares or shocks) stated?
7. For leniency: is the leave-one-out construction used, is assignment restricted to the randomising unit, and is the first stage checked across the instrument's distribution?

Estimation

8. Do the first stage, reduced form and 2SLS use the same sample, weights and fixed effects (visible in the calls)?
9. Is the first-stage coefficient and SE reported?
10. Is a weak-instrument statistic reported that matches the SE structure (effective F or Kleibergen-Paap with clustering), not a homoskedastic F when SEs are clustered?
11. With a single instrument, is an Anderson-Rubin confidence set or tF-adjusted inference reported?
12. Is OLS reported for comparison with the same sample?
13. With overidentification, is the test reported with its caveat; when exactly identified, is it marked not applicable?

Inference

14. Is the cluster level the instrument's assignment level, stated with a rationale, and does the cluster variable reach the IV call?
15. For shock-level shift-share designs, is inference at the shock level or exposure-robust?
16. Is the number of clusters reported and, when small, is a small-cluster method used?

Diagnostics and robustness

17. Balance of predetermined covariates on the instrument reported?
18. Placebo outcomes reported where the design implies none should respond?
19. Alternative instrument definitions, samples and many-instrument estimators reported as planned?

Outputs and interpretation

20. Do table columns state their model, N, clusters, fixed effects, SE type and instruments?
21. Is the interpretation justified for the actual instruments and treatment, with compliers described when a LATE interpretation applies?

Corpus and card use

22. Were nulls and not_found_in_scope in cards treated as unknown rather than as "not done" (first stage is unknown in most IV cards)?
23. Are any restrictions on redistributing substantial reused code respected?
