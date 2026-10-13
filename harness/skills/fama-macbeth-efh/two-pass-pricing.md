# Estimated-beta pricing and rolling-beta regressions

Choose the estimator from the research question and source equations.

| Design | First stage | Second stage | Inference |
|---|---|---|---|
| Full-sample two-pass pricing | Time-series returns on a constant and factors, giving fixed estimated betas | Cross-sectional average returns on a constant and those betas | Account for generated betas; state the Shanken assumptions, covariance convention and reference distribution |
| Rolling-beta Fama-MacBeth | Betas estimated from data available through the formation date | Each month's returns on previously estimated betas | Average monthly slope series with dependence-aware inference; preserve actual calendar spacing |
| Characteristic Fama-MacBeth | Observable characteristics at formation | Each date's subsequent returns on known characteristics | Inference from date-level slopes; a Shanken correction is not automatic |

For the full-sample design, let `R` be T by N returns and `F` be T by K factors. Fit `R = 1 alpha' + F B' + E`, then form `Z = [1, B]`, `A = (Z'Z)^(-1)Z'` and `lambda = A mean(R)`. Use QR decompositions to fit the model and verify rank; do not silently replace unidentified exposures with a pseudo-inverse.

Under the usual correctly specified, serially independent beta-pricing assumptions, one asymptotic Shanken convention is

`V(lambda) = ((1+c) A Sigma_E A' + diag(0, Sigma_F)) / T`,

where `c = lambda_F' Sigma_F^(-1) lambda_F`. State whether residual and factor covariances use divisor T or degrees-of-freedom adjustments, and distinguish inference conditional on factor realizations, which omits the factor covariance term. This correction does not repair weak factors, misspecification or serial dependence. See Shanken (1992), DOI `10.1093/rfs/5.1.1`.

Useful checks include:

- Dense cross-asset covariance and the smaller residual-score calculation agree.
- Factor rescaling changes beta and premium units consistently, preserving t statistics and fit; a constant factor-level shift does not change results when the first stage includes an intercept.
- The average of monthly cross-sectional slopes using **fixed full-sample betas** equals the regression slope on average returns. This does not make rolling-beta estimates equivalent.
- Means, MAPE, raw and adjusted cross-sectional R-squared are explicitly distinguished. Compare each against the quantity named in the paper.
- Rolling betas never use target-month or future returns. Handle missing asset histories per asset rather than discarding all earlier dates because one asset starts late.
- After missing months, an observation lag differs from a calendar lag. Label both when a source leaves the convention ambiguous. For HAC, missing months must not become adjacent observations.

An independently written, runnable implementation and synthetic checks are in `harness/examples/war-discourse/methods.R` and `checks.R`. OLS uses base R QR routines; HAC uses the installed `sandwich` backend. Its source guards and data inputs belong to that example, not to every research task.
