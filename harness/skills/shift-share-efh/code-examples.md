# Shift-share commands

Single-period example: units has unique unit, y, x, control and positive weight; exposure has unique unit/shock pairs and nonnegative share; shocks has unique shock, g and shock_group. g is the excluded shock. x is endogenous treatment. All shocks affecting an exposure must be present.

## R: construct the instrument and residualized shock-level variables

~~~r
library(fixest)
stopifnot(!anyDuplicated(units$unit), !anyDuplicated(shocks$shock),
          !anyDuplicated(exposure[, c("unit", "shock")]),
          all(exposure$share >= 0), all(units$weight > 0))
stopifnot(all(exposure$unit %in% units$unit),
          all(exposure$shock %in% shocks$shock))
stopifnot(!anyNA(units[, c("unit", "y", "x", "control", "weight")]),
          !anyNA(exposure), !anyNA(shocks))
joined <- merge(exposure, shocks, by = "shock", all.x = TRUE)
joined$contribution <- joined$share * joined$g
z <- aggregate(contribution ~ unit, joined, sum)
names(z)[2] <- "z"
u <- merge(units, z, by = "unit", all.x = TRUE)
stopifnot(!anyNA(u$z))
total <- aggregate(share ~ unit, exposure, sum)
u <- merge(u, total, by = "unit", all.x = TRUE)
u$ry <- residuals(lm(y ~ control + share, data = u, weights = weight))
u$rx <- residuals(lm(x ~ control + share, data = u, weights = weight))
e <- merge(exposure, u[, c("unit", "ry", "rx", "weight")], by = "unit")
e$mass <- e$share * e$weight
e$wy <- e$mass * e$ry
e$wx <- e$mass * e$rx
a <- aggregate(cbind(mass, wy, wx) ~ shock, e, sum)
a <- a[a$mass > 0, ]
a$y_bar <- a$wy / a$mass
a$x_bar <- a$wx / a$mass
a <- merge(a, shocks, by = "shock", all.x = TRUE)
shock_iv <- feols(
  y_bar ~ 0 | x_bar ~ g, data = a,
  weights = ~mass, cluster = ~shock_group
)
summary(shock_iv)
~~~

This illustrates a single-period residualized shock design. A no-intercept shock regression preserves the exposure-weighted IV moment after residualization. Add shock controls and period conditioning consistently when required. Clustered shock SE rely on enough independent shock groups; this construction alone does not prove the shock assumptions.

## Stata: exposure and shock regressions

On the exposure-level sample, z is already the constructed instrument and clus is the design's exposure dependence group:

~~~stata
ivreg2 y control share (x = z) [aw=weight], cluster(clus) first
~~~

On an already residualized/aggregated shock-level sample, mass is exposure weight and shock_group indexes dependent shocks:

~~~stata
ivreg2 y_bar (x_bar = g) [aw=mass], nocons cluster(shock_group) first
~~~

Do not run the second call on raw unit-level data. ssaggregate can perform the residualization/aggregation when configured with the actual share file, unit keys, shock keys and full control set; omitting those arguments changes the estimand.
