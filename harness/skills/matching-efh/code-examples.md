# Matching commands

df contains binary treat, y, age, income and baseline; all covariates predate treatment. Examples target ATT.

## R: nearest-neighbor matching and balance

~~~r
library(MatchIt)
d <- df[complete.cases(df[, c("treat", "age", "income", "baseline")]), ]
m <- matchit(
  treat ~ age + income + baseline, data = d,
  method = "nearest", distance = "glm", link = "probit",
  estimand = "ATT", replace = TRUE, ratio = 1
)
summary(m, un = TRUE)
matched <- match.data(m)
print(table(matched$treat))
print(summary(matched$weights))
~~~

This call constructs a matched sample and weights. It does not by itself provide valid effect inference. With replacement, reused controls need appropriate handling; simply clustering on a single arbitrary matched-pair label is insufficient. match.data retains each original unit once with its aggregate weight.

## Stata: matching estimator with analytical variance

~~~stata
teffects psmatch (y) (treat age income baseline, probit), atet nneighbor(1)
tebalance summarize
~~~

teffects psmatch supplies its matching-specific analytical variance under its assumptions. For clustered assignment or dependent observations, choose a procedure that supports that dependence rather than assuming these SE apply.

For sample construction with explicit common-support restrictions:

~~~stata
psmatch2 treat age income baseline, probit neighbor(1) common
pstest age income baseline, both
tabulate treat _support
summarize _weight if _support == 1
~~~

psmatch2/pstest are user-written commands. common, replacement and ties affect retention/weights; the two estimators above need not produce the same ATT. psmatch2's default uncertainty treatment differs from teffects and should not be silently reused.
