# Independent estimators derived from the paper and stated statistical formulas.
# Standard-library QR/OLS and sandwich::NeweyWest provide the numerical backends.

month_id <- function(ym) {
  z <- round(12 * as.numeric(ym))
  if (any(!is.finite(z)) || any(abs(12 * ym - z) > 1e-5))
    stop("Dates must identify calendar months, not arbitrary fractional years.")
  as.integer(z)
}

month_label <- function(id) sprintf("%04d-%02d", id %/% 12, id %% 12 + 1L)

validate_months <- function(x) {
  if (!is.data.frame(x) || !"ym" %in% names(x)) stop("A data frame with ym is required.")
  x$month <- month_id(x$ym)
  if (anyDuplicated(x$month)) stop("Conflicting or duplicate monthly keys.")
  x[order(x$month), , drop = FALSE]
}

read_input <- function(relative, input_root, access_log = NULL) {
  permitted <- c("texts/war_indexes.rds", "texts/top_words.rds",
                 "texts/top_10_war_articles.rds", "texts/narrative_dictionary.rds",
                 "texts/sample_tokenized_texts.rds", "test_portfolios_original.rds",
                 "test_portfolios.rds", "traded_factors.rds", "nontraded_factors.rds",
                 "crisis_events_full_sample.rds", "ff_portfolios.rds",
                 "narrative_factors.rds", "beta_portfolios.rds", "gw_macro_predictors.RDS",
                 "stocks_monthly.rds", "war_factors.rds")
  if (!relative %in% permitted) stop("Input is outside the paper-first data allowlist.")
  root <- normalizePath(input_root, mustWork = TRUE)
  path <- normalizePath(file.path(root, relative), mustWork = TRUE)
  if (!startsWith(path, paste0(root, .Platform$file.sep))) stop("Input escapes data root.")
  if (!is.null(access_log)) cat(relative, "\n", sep = "", file = access_log, append = TRUE)
  readRDS(path)
}

fingerprint_inputs <- function(paths) {
  hashes <- tools::md5sum(paths)
  if (anyNA(hashes)) stop("Cannot fingerprint missing or unreadable input files.")
  hashes
}

premium_caption <- function() paste(
  "Calendar lags preserve the 1978 news-data gap; observed lags bridge it.",
  "Supplied portfolio returns are inputs; index provenance remains unresolved.",sep="\n")

ar_innovations <- function(month, x, start = 1926L * 12L, gap = "calendar",
                           include_current = TRUE, min_pairs = 12L) {
  stopifnot(length(month) == length(x), gap %in% c("calendar", "observed"))
  if (is.unsorted(month, strictly = TRUE)) stop("AR input months must be unique and sorted.")
  lag_x <- if (gap == "calendar") x[match(month - 1L, month)] else c(NA_real_, head(x, -1L))
  lag_month <- if (gap == "calendar") month-1L else c(NA_integer_,head(month,-1L))
  usable <- is.finite(x) & is.finite(lag_x) & month >= start & !is.na(lag_month) & lag_month>=start
  out <- rep(NA_real_, length(x))
  # Sufficient statistics reproduce expanding OLS without thousands of refits.
  n <- sx <- sy <- sxx <- sxy <- 0
  update <- function(i) {
    if (usable[i]) {
      n <<- n + 1; sx <<- sx + lag_x[i]; sy <<- sy + x[i]
      sxx <<- sxx + lag_x[i]^2; sxy <<- sxy + lag_x[i] * x[i]
    }
  }
  for (i in seq_along(x)) {
    if (include_current) update(i)
    denom <- sxx - sx^2 / max(n, 1)
    if (usable[i] && n >= min_pairs && denom > .Machine$double.eps) {
      rho <- (sxy - sx * sy / n) / denom
      out[i] <- x[i] - (sy / n - rho * sx / n) - rho * lag_x[i]
    }
    if (!include_current) update(i)
  }
  out
}

prepare_portfolios <- function(x, start = 1972L * 12L + 6L, end = 2016L * 12L + 11L) {
  x <- validate_months(x)
  z <- x[x$month >= start & x$month <= end, , drop = FALSE]
  assets <- setdiff(names(z), c("ym", "month"))
  if (!length(assets)) stop("No test assets.")
  keep <- vapply(z[assets], function(a) all(is.finite(a)), logical(1))
  list(data = z[c("month", assets[keep])], before = length(assets),
       retained = sum(keep), excluded = assets[!keep], months = nrow(z))
}

two_pass <- function(returns, factors, residual_df = "T", include_factor_cov = TRUE) {
  R <- as.matrix(returns); F <- as.matrix(factors)
  stopifnot(nrow(R) == nrow(F), ncol(F) >= 1L)
  ok <- rowSums(!is.finite(R)) == 0L & rowSums(!is.finite(F)) == 0L
  R <- R[ok, , drop = FALSE]; F <- F[ok, , drop = FALSE]
  TT <- nrow(R); NN <- ncol(R); KK <- ncol(F)
  if (TT <= KK + 2L || NN <= KK + 1L) stop("Insufficient observations or assets.")
  X <- cbind(Intercept = 1, F)
  ts_qr <- qr(X)
  if (ts_qr$rank != ncol(X)) stop("Rank-deficient time-series factors.")
  ts_coef <- qr.coef(ts_qr, R)
  E <- qr.resid(ts_qr, R)
  B <- t(ts_coef[-1L, , drop = FALSE])
  Z <- cbind(Intercept = 1, B)
  cs_qr <- qr(Z)
  if (cs_qr$rank != ncol(Z)) stop("Rank-deficient estimated exposures.")
  # A QR left inverse avoids allocating an N-by-N identity for large panels.
  A <- matrix(0, ncol(Z), NN)
  A[cs_qr$pivot, ] <- backsolve(qr.R(cs_qr), t(qr.Q(cs_qr)))
  rownames(A) <- colnames(Z)
  mu <- colMeans(R)
  lambda <- drop(A %*% mu)
  names(lambda) <- colnames(Z)
  errors <- drop(mu - Z %*% lambda)
  Fc <- sweep(F, 2L, colMeans(F))
  SigmaF <- crossprod(Fc) / TT
  c_shanken <- drop(t(lambda[-1L]) %*% solve(SigmaF, lambda[-1L]))
  denom <- if (residual_df == "T") TT else TT - KK - 1L
  influence <- E %*% t(A)
  V <- (1 + c_shanken) * crossprod(influence) / (denom * TT)
  if (include_factor_cov) V[-1L, -1L] <- V[-1L, -1L] + SigmaF / TT
  se <- sqrt(pmax(diag(V), 0))
  tstat <- lambda / se
  # The normal asymptotic reference distribution is explicit.
  p <- 2 * pnorm(-abs(tstat))
  invXX <- chol2inv(qr.R(ts_qr))
  beta_se <- sqrt(outer(diag(invXX)[-1L], colSums(E^2) / (TT - KK - 1L)))
  beta_t <- ts_coef[-1L, , drop = FALSE] / beta_se
  list(lambda = lambda, se = se, t = tstat, p = p, covariance = V,
       r2 = 1 - sum(errors^2) / sum((mu - mean(mu))^2),
       adjusted_r2 = 1 - (sum(errors^2) / (NN - KK - 1L)) / (sum((mu - mean(mu))^2) / (NN - 1L)),
       mape = mean(abs(errors)), T = TT, N = NN, K = KK,
       beta = B, beta_t = beta_t, alpha = ts_coef[1L, ],
       residuals = E, errors = errors, used = which(ok), shanken = c_shanken,
       monthly_lambda = R %*% t(A), condition = kappa(Z))
}

result_rows <- function(fit, table, assets, model, variant = "calendar") {
  data.frame(table = table, assets = assets, model = model, variant = variant,
             term = names(fit$lambda), estimate = fit$lambda, se = fit$se,
             t = fit$t, p = fit$p, r2 = fit$r2, adjusted_r2 = fit$adjusted_r2,
             mape = fit$mape, N = fit$N, T = fit$T, K = fit$K,
             shanken = fit$shanken, condition = fit$condition, row.names = NULL)
}

hac_mean <- function(x, lag = 6L, month = seq_along(x)) {
  if (any(!is.finite(x))) stop("HAC requires the explicitly selected finite time series.")
  if (length(month) != length(x) || is.unsorted(month, strictly = TRUE))
    stop("HAC months must be unique and sorted.")
  grid <- seq.int(min(month), max(month))
  # Missing months receive zero estimating scores, never zero return estimates.
  # Rescaling the package covariance retains the actual observation denominator.
  scores <- numeric(length(grid))
  scores[match(month, grid)] <- x - mean(x)
  fit <- lm(scores ~ 1)
  V <- sandwich::NeweyWest(fit, lag = lag, prewhite = FALSE, adjust = FALSE)
  se <- sqrt(V[1, 1]) * length(grid) / length(x)
  c(estimate = mean(x), se = se, t = mean(x) / se, N = length(x),
    calendar_months = length(grid), missing_months = length(grid)-length(x))
}

rank_quintile <- function(x) {
  if (any(!is.finite(x))) stop("Rank only the actual finite cross-section.")
  # Average ranks retain ties; quintile labels become 0, .25, .5, .75, 1.
  pmin(4L, floor(5L * (rank(x, ties.method = "average") - 1L) / length(x))) / 4
}

calendar_hac_vcov <- function(fit, month, lag = 6L) {
  if (length(month)!=nobs(fit) || is.unsorted(month,strictly=TRUE))
    stop("Covariance months must match fitted observations in order.")
  if (all(diff(month)==1L))
    return(sandwich::NeweyWest(fit,lag=lag,prewhite=FALSE,adjust=FALSE))
  scores <- sandwich::estfun(fit)
  grid <- seq.int(min(month),max(month))
  padded <- matrix(0,length(grid),ncol(scores))
  padded[match(month,grid),] <- scores
  meat <- crossprod(padded)
  for (j in seq_len(min(lag,nrow(padded)-1L))) {
    g <- crossprod(padded[(j+1L):nrow(padded),,drop=FALSE],padded[1:(nrow(padded)-j),,drop=FALSE])
    meat <- meat + (1-j/(lag+1))*(g+t(g))
  }
  bread <- sandwich::bread(fit)/nobs(fit)
  out <- bread %*% meat %*% bread
  dimnames(out) <- list(names(coef(fit)),names(coef(fit)))
  out
}

industry_fmb <- function(returns, factors, crisis_names, window = 60L,
                         min_complete = 60L, rank_mode = "quintile", window_mode = "calendar") {
  stopifnot(all(crisis_names %in% names(factors)))
  months <- returns$month
  common <- match(months, factors$month)
  R <- as.matrix(returns[setdiff(names(returns), "month")])
  F <- as.matrix(factors[common, setdiff(names(factors), "month"), drop = FALSE])
  out <- list(); beta_dates <- integer(); r2 <- numeric(); counts <- integer()
  for (ii in seq_along(months)) {
    target <- months[ii]
    idx <- which(months < target & (window_mode == "observed" | months >= target - window))
    good <- rowSums(!is.finite(F[idx, , drop = FALSE])) == 0L
    idx <- idx[good]
    if (window_mode == "observed") idx <- tail(idx, window)
    if (length(idx) < min_complete) next
    eligible <- colSums(!is.finite(R[idx, , drop = FALSE])) == 0L & is.finite(R[ii, ])
    if (sum(eligible) <= ncol(F) + 1L) next
    X <- cbind(1, F[idx, , drop = FALSE])
    q <- qr(X)
    if (q$rank != ncol(X)) next
    B <- t(qr.coef(q, R[idx, eligible, drop = FALSE])[-1L, , drop = FALSE])
    if (rank_mode == "quintile") {
      for (nm in crisis_names) B[, nm] <- rank_quintile(B[, nm])
    }
    Z <- cbind(Intercept = 1, B)
    y <- R[ii, eligible]
    cs <- lm.fit(Z, y)
    if (cs$rank != ncol(Z)) next
    out[[length(out) + 1L]] <- cs$coefficients
    beta_dates <- c(beta_dates, target)
    r2 <- c(r2, 1 - sum(cs$residuals^2) / sum((y - mean(y))^2))
    counts <- c(counts, sum(eligible))
  }
  list(slopes = do.call(rbind, out), month = beta_dates, r2 = r2,
       N = counts, skipped = setdiff(months, beta_dates))
}
