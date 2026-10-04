---
name: portfolio-sorts
description: Asset portfolio sorts using observable lagged signals, explicit breakpoints, formation weights and subsequent returns. Cover univariate/double sorts, long-short spreads, factor adjustment and time-series inference.
kind: method
---

# Portfolio sorts

## When to use

Use for descriptive characteristic-return relations or portfolios formed from predicted signals. Sorting does not establish a causal return effect and a paper portfolio is not automatically implementable.

## Inputs

Asset/calendar keys, formation signal and availability date, returns including delisting handling, lagged capitalization/weights, breakpoint universe, number of portfolios, holding/rebalancing rules and factor returns.

## Procedure

1. Define when the signal becomes observable and when returns start. Lag accounting information by release date; avoid future constituents, survivorship filters and future-data standardization.
2. Set filters and breakpoint universe before realized returns. State equal/value/capped weighting and why; inspect microcap concentration, ties and sparse bins.
3. For double sorts distinguish independent breakpoints from conditional second sorts. Annual formation, multi-month holding and overlapping cohorts require explicit cohort aggregation and weight drift.
4. Compute returns from formation weights and all eligible realized returns. Include delisting/corporate-action handling; do not silently drop missing future returns or rebalance with end-of-period capitalization.
5. Show each leg, spread and portfolio counts. Empty bins/missing legs should remain unavailable rather than being filled with zero.
6. Estimate mean spreads and factor-model intercepts with time-series inference appropriate to frequency and overlapping holdings. Factor alignment/units and whether returns are excess or zero-investment spreads matter.
7. Examine breakpoint/weight/sample sensitivity, turnover, liquidity and transaction costs if discussing implementation. Many signals/portfolios imply selection and multiple-testing concerns.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) constructs monthly deciles using NYSE breakpoints and lagged value weights, then runs Stata/R HAC factor regressions.

Return formation rules, counts, leg/spread returns and factor-adjusted results. This skill does not authorize investment transactions or personalized recommendations.
