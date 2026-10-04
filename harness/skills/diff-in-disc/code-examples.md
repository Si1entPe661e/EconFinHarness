# Difference-in-discontinuities commands

df contains y, running, post and unit. running is centred at the fixed cutoff, post is 0/1, and unit is the appropriate dependence group. h = 10 is an illustrative bandwidth in running-variable units.

## R: joint local linear regression

~~~r
library(fixest)
h <- 10
d <- df[complete.cases(df[, c("y", "running", "post", "unit")]), ]
stopifnot(all(d$post %in% c(0, 1)))
d <- d[abs(d$running) < h, ]
d$above <- as.integer(d$running >= 0)
d$jump_change <- d$above * d$post
d$triangular <- 1 - abs(d$running) / h
print(with(d, table(above, post)))
fit <- feols(
  y ~ above + post + jump_change + running +
      above:running + post:running + jump_change:running,
  data = d, weights = ~triangular, cluster = ~unit
)
summary(fit)
b <- coef(fit)
V <- vcov(fit)
pre_jump <- b["above"]
post_jump <- b["above"] + b["jump_change"]
post_se <- sqrt(V["above", "above"] + V["jump_change", "jump_change"] +
                2 * V["above", "jump_change"])
print(c(pre_jump = pre_jump, post_jump = post_jump, post_se = post_se))
confint(fit, parm = "jump_change")
~~~

jump_change is the difference in jumps at running = 0. The regression allows separate slopes by side and period. Repeat with justified bandwidths; these are local regression intervals without nonparametric bias correction.

## Stata

~~~stata
keep if !missing(y, running, post, unit)
assert inlist(post, 0, 1)
local h 10
keep if abs(running) < `h'
gen above = running >= 0
gen triweight = 1 - abs(running)/`h'
regress y i.above##i.post##c.running [aw=triweight], vce(cluster unit)
lincom 1.above
lincom 1.above + 1.above#1.post
lincom 1.above#1.post
~~~

For a fuzzy contrast, estimate the same equation with actual receipt as the outcome and jointly infer the ratio. Separately reported numerator/denominator standard errors are insufficient.
