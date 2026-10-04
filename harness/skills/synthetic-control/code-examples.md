# Synthetic-control commands

The synthdid package supplies both classical SCM and synthetic DID. sc_estimate below is the classical estimator.

## R: classical SCM

~~~r
library(synthdid)
data("california_prop99")
setup <- panel.matrices(california_prop99)
sc <- sc_estimate(setup$Y, setup$N0, setup$T0)
print(sc)
plot(sc)
weights <- attr(sc, "weights")$omega
print(weights)
Y <- setup$Y
N0 <- setup$N0
T0 <- setup$T0
stopifnot(N0 == nrow(Y) - 1L)
synthetic <- as.numeric(crossprod(weights, Y[seq_len(N0), , drop = FALSE]))
treated <- as.numeric(Y[N0 + 1L, ])
gap <- treated - synthetic
pre_rmspe <- sqrt(mean(gap[seq_len(T0)]^2))
post_effect <- mean(gap[seq.int(T0 + 1L, ncol(Y))])
print(c(pre_rmspe = pre_rmspe, post_effect = post_effect))
~~~

For the user's panel, rows of Y must be donors first and treated units last; columns are pretreatment periods first, then treatment periods. panel.matrices requires its documented balanced-panel treatment structure. The explicit trajectory calculation above is for one treated unit.

## R: donor removal and in-space placebo effects

~~~r
leave_one_out <- sapply(seq_len(N0), function(j) {
  sc_estimate(Y[-j, , drop = FALSE], N0 - 1L, T0)
})
print(leave_one_out)

placebos <- lapply(seq_len(N0), function(j) {
  donors <- setdiff(seq_len(N0), j)
  Yp <- rbind(Y[donors, , drop = FALSE], Y[j, , drop = FALSE])
  fit <- sc_estimate(Yp, length(donors), T0)
  w <- attr(fit, "weights")$omega
  g <- Yp[nrow(Yp), ] - as.numeric(crossprod(w, Yp[seq_along(donors), , drop = FALSE]))
  c(effect = as.numeric(fit), pre_rmspe = sqrt(mean(g[seq_len(T0)]^2)))
})
print(do.call(rbind, placebos))
~~~

The truly treated unit is excluded from donor placebos. Compare pre-fit before interpreting ranks or post/pre RMSPE ratios; do not automatically treat these comparisons as randomization p-values.
