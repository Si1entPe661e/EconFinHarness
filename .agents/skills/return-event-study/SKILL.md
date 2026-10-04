---
name: return-event-study
description: Financial return event studies around announcements using estimation windows, expected-return models, abnormal returns and CAR/BHAR. Align trading dates and account for event clustering, overlap and selection.
kind: method
---

# Return event studies

## When to use

Use for asset-price responses around defined announcements or events. Use event-study/did for panel policy dynamics. A short-window CAR association requires additional assumptions to interpret as the event's causal effect.

## Inputs

Asset and event identifiers, timestamp and market calendar, returns/risk-free/factors, estimation/event windows, exposure/controls, confounding announcements, repeated-event and event-date dependence.

## Procedure

1. Define event timing, information arrival and day zero. Map weekends, holidays and after-close announcements to the relevant trading session using actual market calendars.
2. Separate the estimation window from the event window and anticipation buffer. Set minimum usable observations and rank requirements without selecting windows by realized CAR.
3. Estimate expected returns using a market/factor model or a justified benchmark. Keep raw/excess returns and scales consistent; inspect thin trading, splits, missing prices and delisting handling.
4. Compute AR and CAR over trading-day event windows. CAR sums abnormal simple returns; BHAR compounds realized and benchmark wealth and is not the same statistic.
5. Inspect concurrent news, overlapping events, event-induced variance and common event dates. Repeated firm events and date shocks require compatible inference; cross-sectional independence is often implausible.
6. Report average effects and any cross-sectional exposure regressions with predetermined controls. Account for first-stage expected-return estimation when the inferential method requires it; generic CAR-regression SE do not automatically provide that correction.
7. Check windows, benchmarks, anticipation and placebo dates. Long-horizon BHAR needs particular care about skewness, rebalancing and benchmark selection.

## Skill composition

For a compound analysis, read harness/skill-composition.md and combine this method with relevant panel-data-checks, inference-clustering and tables-figures steps. Preserve this method's estimand and specialized inference; generic clustering or export must not replace them. Use the actual fitted/evaluation sample, weights, FE and numerical results throughout. Revisit affected steps when sample, identification, covariance or prediction splits change; load other methods only for a relevant design branch.

## Commands and output

[code-examples.md](code-examples.md) fits an event-specific market model, builds a complete-window CAR and runs a cross-sectional regression. Return timing/window definitions, usable events, AR/CAR summaries and inference/causal limitations.
