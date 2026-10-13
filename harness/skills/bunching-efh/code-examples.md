# Bunching commands

df$amount contains the quantity with a notch at 25,000. Parameters describe this illustrative scale; use the actual schedule, bins and response region for the application.

## R: notch bunching

~~~r
library(bunching)
amount <- df$amount[is.finite(df$amount)]
set.seed(12345)
fit <- bunchit(
  amount, binv = "median", zstar = 25000, binwidth = 100,
  bins_l = 240, bins_r = 750, t0 = 0, t1 = 1,
  notch = TRUE, rn = c(1000, 5000), extra_fe = 50000,
  poly = 9, correct_above_zu = FALSE, bins_excl_r = 0
)
print(fit)
~~~

bins_l/bins_r specify the fit range in bins; rn and extra_fe address other salient values. t0/t1 and notch determine schedule interpretation. The original parameter scale is not a universal recommendation; a ninth-order polynomial may be unstable.

## R: polynomial sensitivity with the same window

~~~r
orders <- c(5, 7, 9)
fits <- lapply(orders, function(order) {
  bunchit(
    amount, binv = "median", zstar = 25000, binwidth = 100,
    bins_l = 240, bins_r = 750, t0 = 0, t1 = 1,
    notch = TRUE, rn = c(1000, 5000), extra_fe = 50000,
    poly = order, correct_above_zu = FALSE, bins_excl_r = 0
  )
})
names(fits) <- as.character(orders)
lapply(fits, print)
~~~

Check how the package chooses its excluded region and inference. When changing bin width, adjust range/exclusion counts to keep economically comparable quantity intervals. Clustered data require a bootstrap that resamples clusters and reruns bunchit, rather than accepting an independent-observation uncertainty calculation.
