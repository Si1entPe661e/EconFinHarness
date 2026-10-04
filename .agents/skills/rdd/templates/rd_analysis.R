# rd_analysis.R -- regression discontinuity template (FinEconHarness skill `rdd`, version 0.2.3)
#
# Backend: R with rdrobust (local polynomial point estimates, bias-corrected robust inference,
# MSE-optimal bandwidths) and rddensity (manipulation test). Nothing here copies corpus code; the
# structure follows the rdd skill procedure. Every function returns plain lists so the caller can
# write JSON and a reviewer can trace each reported number to a call and its options.
#
# Version 0.2.0 responds to the independent audit in harness_build/pilot/runs/pilot-audit-code/reviews/
# (findings r1-r20): within-bandwidth cluster and support-point counts, a first stage estimated at
# the cutoff (also used for the cutoff-side guard), package warnings captured and the variance
# estimator actually used recorded, weights and covariates carried into every diagnostic and into
# the table, complete-case handling for covariates and weights, an explicit design argument, a
# two-sided bandwidth grid, kink designs through deriv, and an ordinary list of output files.
# Version 0.2.1 responds to the re-check (r21: placebo windows around the placebo cutoff; r24: covariates declared in
# rd_prepare adjust the estimate by default and the source of the covariate list is recorded).
# Version 0.2.2 responds to the empirical-analyst's research answer: the discreteness trigger is a support-point count
# (no share condition), with three levels after estimation (advisory / caveat below 20 in-bandwidth support points per
# side / do-not-certify below 10); mass at the cutoff is reported separately with rdrobust's masspoints setting; caveats and
# unresolved items are printed as table rows; kink designs return the outcome slope change only (numerator of the kink
# estimand; no policy-kink scaling and no fuzzy kink).
# Version 0.2.3: header corrected after the second re-check (r28); no behavioural change.
#
# Usage (see harness_build/evals/tests/run_rdd_tests.R for tested calls):
#   source("harness/skills/rdd/templates/rd_analysis.R")
#   prep <- rd_prepare(df, y = "y", x = "x", cutoff = 0, treatment = "d", cluster = "cl", design = "sharp")
#   est  <- rd_estimate(prep)                      # vce defaults to "cluster" when a cluster variable is given, else "nn"
#   diag <- rd_diagnostics(prep, est)
#   rd_report(prep, est, diag, out_dir = "out/rdd", spec_id = "s1")
#
# Design rules implemented:
#   * the running variable is centred at the cutoff; observations exactly at the cutoff are counted on the
#     right (rdrobust convention x >= c) and reported separately as mass_at_cutoff;
#   * when a treatment column is supplied, a first stage is estimated AT THE CUTOFF (local polynomial of
#     treatment on the centred running variable) and the estimate refuses to run when that jump is not positive;
#   * the design (sharp / fuzzy / kink) is declared by the caller; "auto" infers it from the compliance pattern
#     and records that the choice came from the data, with a warning when data and declaration disagree;
#   * every option (order, kernel, bandwidth selector and values on each side, variance estimator requested and
#     actually used, cluster variable, covariates, weights, derivative) is recorded in the estimate object;
#   * diagnostics reuse the main call's options (through .rd_fit) so that they describe the same specification;
#   * within-bandwidth cluster counts, treated clusters and running-variable support points are reported and
#     produce warnings and unresolved items when few.

suppressPackageStartupMessages({
  library(rdrobust)
  library(rddensity)
  library(jsonlite)
})

TEMPLATE_VERSION <- "0.2.3"
FEW_CLUSTERS_TOTAL <- 30
FEW_CLUSTERS_SIDE <- 5
FEW_SUPPORT_POINTS_SIDE <- 10       # do-not-certify level (matches rdrobust's own bwcheck floor); harness convention, not a literature value
CAVEAT_SUPPORT_POINTS_SIDE <- 20    # caveat-required level; harness convention

rd_env <- function() {
  list(template = "harness/skills/rdd/templates/rd_analysis.R", template_version = TEMPLATE_VERSION,
       r_version = R.version.string,
       rdrobust = as.character(utils::packageVersion("rdrobust")),
       rddensity = as.character(utils::packageVersion("rddensity")),
       platform = R.version$platform, recorded_at = format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ", tz = "UTC"))
}

.with_warnings <- function(expr) {
  msgs <- character(0)
  val <- withCallingHandlers(expr, warning = function(w) { msgs <<- c(msgs, conditionMessage(w)); invokeRestart("muffleWarning") })
  list(value = val, warnings = msgs)
}


.count_in_bw <- function(d, h, cluster = NULL, treatment = NULL) {
  left <- d$.xc < 0 & d$.xc >= -h[1]; right <- d$.xc >= 0 & d$.xc <= h[2]
  res <- list(n_left = sum(left), n_right = sum(right),
              support_points = list(left = length(unique(d$.xc[left])), right = length(unique(d$.xc[right]))))
  if (!is.null(cluster)) {
    cl <- d[[cluster]]
    res$clusters <- list(total = length(unique(cl[left | right])), left = length(unique(cl[left])), right = length(unique(cl[right])))
    if (!is.null(treatment)) res$treated_clusters <- length(unique(cl[(left | right) & d[[treatment]] == 1]))
  }
  res
}

# Core fit: one rdrobust call with the options recorded. cutoff_shift moves the cutoff on the centred scale
# (used by placebo cutoffs); subset restricts rows (used by placebo sides and donut).
.rd_fit <- function(prep, y_var = NULL, p = 1, q = NULL, kernel = "triangular", h = NULL, b = NULL, vce = "nn",
                    fuzzy = FALSE, covs = NULL, use_weights = TRUE, bwselect = "mserd", deriv = 0,
                    cutoff_shift = 0, subset = NULL, treatment_as_outcome = FALSE) {
  d <- prep$data
  if (!is.null(subset)) d <- d[subset, , drop = FALSE]
  yname <- if (treatment_as_outcome) prep$treatment else if (is.null(y_var)) prep$y else y_var
  args <- list(y = d[[yname]], x = d$.xc - cutoff_shift, c = 0, p = p, kernel = kernel, bwselect = bwselect, deriv = deriv)
  if (!is.null(q)) args$q <- q
  if (!is.null(h)) { args$h <- h; if (!is.null(b)) args$b <- b }
  cluster_var <- NULL
  if (vce == "cluster") {
    stopifnot(!is.null(prep$cluster))
    args$vce <- "cr1"; args$cluster <- d[[prep$cluster]]; cluster_var <- prep$cluster
  } else args$vce <- vce
  if (isTRUE(fuzzy) && !treatment_as_outcome) {
    if (is.null(prep$treatment)) stop(".rd_fit: fuzzy = TRUE requires a treatment column in rd_prepare")
    args$fuzzy <- d[[prep$treatment]]
  }
  if (!is.null(covs)) args$covs <- as.matrix(d[, covs, drop = FALSE])
  weights_var <- NULL
  if (use_weights && !is.null(prep$weights)) { args$weights <- d[[prep$weights]]; weights_var <- prep$weights }
  res <- .with_warnings(do.call(rdrobust::rdrobust, args))
  fit <- res$value
  hh <- unname(fit$bws[1, ]); bb <- unname(fit$bws[2, ])
  d_win <- d; d_win$.xc <- d$.xc - cutoff_shift   # windows are taken around the cutoff actually used by this fit (placebo cutoffs shift it)
  counts <- .count_in_bw(d_win, hh, cluster_var, if (!treatment_as_outcome) prep$treatment else NULL)
  list(fit = fit,
       outcome = yname, cutoff_shift = cutoff_shift,
       estimate = unname(fit$coef[1]), estimate_bc = unname(fit$coef[2]),
       se_conventional = unname(fit$se[1]), se_robust = unname(fit$se[3]),
       ci_robust = unname(fit$ci[3, ]), p_robust = unname(fit$pv[3]), level = fit$level,
       h = hh, b = bb, n_eff = unname(fit$N_h), n_total = sum(unname(fit$N)),
       p = p, q = if (is.null(q)) p + 1 else q, kernel = kernel, deriv = deriv,
       bwselect = if (is.null(h)) bwselect else "manual",
       vce_requested = vce, vce_used = as.character(fit$vce), cluster_var = cluster_var,
       n_clusters_sample = if (!is.null(cluster_var)) length(unique(d[[cluster_var]])) else NA_integer_,
       in_bandwidth = counts,
       fuzzy = isTRUE(fuzzy) && !treatment_as_outcome, covs = covs, weights_var = weights_var,
       masspoints_setting = as.character(fit$masspoints), package_warnings = res$warnings,
       call_options = list(p = p, q = if (is.null(q)) p + 1 else q, kernel = kernel, vce_requested = vce, vce_used = as.character(fit$vce),
                           cluster = cluster_var, bwselect = if (is.null(h)) bwselect else "manual", h = hh, b = bb, deriv = deriv,
                           fuzzy = isTRUE(fuzzy) && !treatment_as_outcome, covs = covs, weights = weights_var, cutoff_shift = cutoff_shift,
                           n_rows_passed = nrow(d)))
}

rd_prepare <- function(data, y, x, cutoff, treatment = NULL, cluster = NULL, covs = NULL, weights = NULL,
                       design = c("auto", "sharp", "fuzzy", "kink"), p = 1, kernel = "triangular", bwselect = "mserd",
                       vce = NULL, discrete_max_support = 100, discrete_share = 0.05) {
  design <- match.arg(design)
  stopifnot(is.data.frame(data), y %in% names(data), x %in% names(data))
  for (v in c(treatment, cluster, covs, weights)) if (!v %in% names(data)) stop("rd_prepare: column not found: ", v)
  n0 <- nrow(data)
  miss <- function(cols) if (is.null(cols)) rep(FALSE, n0) else Reduce(`|`, lapply(cols, function(v) is.na(data[[v]])))
  m_yx <- miss(c(y, x)); m_t <- miss(treatment) & !m_yx; m_cl <- miss(cluster) & !m_yx & !m_t
  m_cov <- miss(covs) & !m_yx & !m_t & !m_cl; m_w <- miss(weights) & !m_yx & !m_t & !m_cl & !m_cov
  keep <- !(m_yx | m_t | m_cl | m_cov | m_w)
  d <- data[keep, , drop = FALSE]
  d$.xc <- d[[x]] - cutoff
  if (is.null(vce)) vce <- if (!is.null(cluster)) "cluster" else "nn"
  warn <- character(0)
  n_unique <- length(unique(d$.xc))
  checks <- list(template_version = TEMPLATE_VERSION,
                 n_input = n0, n_used = nrow(d),
                 n_dropped = list(total = n0 - nrow(d), missing_y_or_x = sum(m_yx), missing_treatment = sum(m_t),
                                  missing_cluster = sum(m_cl), missing_covariates = sum(m_cov), missing_weights = sum(m_w)),
                 sample_note = "all counts below refer to the complete-case estimation sample (rows with y, x, treatment, cluster, covariates and weights all non-missing)",
                 n_left = sum(d$.xc < 0), n_right = sum(d$.xc >= 0),
                 support_both_sides = sum(d$.xc < 0) > 0 && sum(d$.xc >= 0) > 0,
                 support_points_running = n_unique, share_unique_running = n_unique / max(nrow(d), 1),
                 running_looks_discrete = n_unique <= discrete_max_support,
                 discreteness_note = "advisory screen on the number of distinct support points (harness convention: at most 100); the operative trigger is the in-bandwidth support count reported by rd_estimate",
                 mass_at_cutoff = sum(d$.xc == 0), share_at_cutoff = mean(d$.xc == 0),
                 mass_point_note = "observations exactly at the cutoff are a separate problem from few support points (rdrobust handles mass points through its masspoints option; a donut specification is the usual check)",
                 design_declared = design, design_used = NA_character_, design_source = NA_character_,
                 compliance_pattern = NA_character_, treatment_mean_above = NA_real_, treatment_mean_below = NA_real_,
                 n_clusters_sample = if (!is.null(cluster)) length(unique(d[[cluster]])) else NA_integer_)
  if (!checks$support_both_sides) warn <- c(warn, "no observations on one side of the cutoff")
  if (checks$running_looks_discrete) warn <- c(warn, sprintf(
    "running variable has only %d distinct support points: possibly discrete; the in-bandwidth support count after estimation decides (see the rdd skill discrete branch)", n_unique))
  if (checks$mass_at_cutoff > 0) warn <- c(warn, sprintf("%d observations (share %.3f) sit exactly at the cutoff: check a donut specification and rdrobust's masspoints handling", checks$mass_at_cutoff, checks$share_at_cutoff))
  prep <- list(data = d, y = y, x = x, cutoff = cutoff, treatment = treatment, cluster = cluster, covs = covs, weights = weights,
               options = list(p = p, kernel = kernel, bwselect = bwselect, vce = vce), checks = checks, first_stage = NULL)
  if (!is.null(treatment)) {
    tv <- d[[treatment]]
    if (!all(tv %in% c(0, 1))) stop("rd_prepare: treatment must be coded 0/1")
    checks$treatment_mean_above <- mean(tv[d$.xc >= 0]); checks$treatment_mean_below <- mean(tv[d$.xc < 0])
    sharp_pattern <- all(tv[d$.xc >= 0] == 1) && all(tv[d$.xc < 0] == 0)
    reversed_pattern <- all(tv[d$.xc >= 0] == 0) && all(tv[d$.xc < 0] == 1)
    checks$compliance_pattern <- if (sharp_pattern) "sharp_pattern" else if (reversed_pattern) "reversed_sharp_pattern" else "fuzzy_pattern"
    if (sharp_pattern || reversed_pattern) {
      # deterministic assignment: the first stage at the cutoff is exactly +1 (or -1 when the sides are swapped); rdrobust has nothing to estimate
      prep$first_stage <- list(estimate = if (sharp_pattern) 1 else -1, se_conventional = 0, se_robust = 0, ci_robust = rep(if (sharp_pattern) 1 else -1, 2), p_robust = 0,
                               h = NA_real_, b = NA_real_, n_eff = c(sum(d$.xc < 0), sum(d$.xc >= 0)), vce_used = NA_character_, package_warnings = character(0), call_options = NULL,
                               ci_excludes_zero = TRUE, note = "deterministic assignment from the compliance pattern; no local polynomial fit needed")
      if (reversed_pattern) warn <- c(warn, "first stage at the cutoff is not positive (estimate -1.000): treatment is 1 below and 0 above the cutoff; check the cutoff side / treatment definition before estimating")
    } else {
      fs <- tryCatch(.rd_fit(prep, p = p, kernel = kernel, vce = vce, bwselect = bwselect, treatment_as_outcome = TRUE), error = function(e) NULL)
      if (!is.null(fs) && is.finite(fs$estimate)) {
        prep$first_stage <- fs[c("estimate", "se_conventional", "se_robust", "ci_robust", "p_robust", "h", "b", "n_eff", "vce_used", "package_warnings", "call_options")]
        prep$first_stage$ci_excludes_zero <- !(fs$ci_robust[1] <= 0 && 0 <= fs$ci_robust[2])
        prep$first_stage$note <- "local polynomial RD of the treatment indicator on the centred running variable with the prepare options; the cutoff-side guard uses this estimate"
      } else {
        # fall back to a narrow-window mean difference (closest 10% of observations on each side) and say so
        ql <- stats::quantile(d$.xc[d$.xc < 0], 0.9); qr <- stats::quantile(d$.xc[d$.xc >= 0], 0.1)
        est_w <- mean(tv[d$.xc >= 0 & d$.xc <= qr]) - mean(tv[d$.xc < 0 & d$.xc >= ql])
        prep$first_stage <- list(estimate = est_w, se_conventional = NA_real_, se_robust = NA_real_, ci_robust = c(NA_real_, NA_real_), p_robust = NA_real_, h = c(-ql, qr), b = NA_real_,
                                 n_eff = c(sum(d$.xc < 0 & d$.xc >= ql), sum(d$.xc >= 0 & d$.xc <= qr)), vce_used = NA_character_, package_warnings = character(0), call_options = NULL,
                                 ci_excludes_zero = NA, note = "rdrobust could not fit the first stage; mean difference in the closest 10% of observations on each side")
        warn <- c(warn, "first stage at the cutoff could not be estimated by rdrobust; a narrow-window mean difference is used for the cutoff-side guard")
      }
      if (!is.finite(prep$first_stage$estimate) || prep$first_stage$estimate <= 0)
        warn <- c(warn, sprintf("first stage at the cutoff is not positive (estimate %.3f): check the cutoff side / treatment definition before estimating", prep$first_stage$estimate))
      if (isTRUE(!prep$first_stage$ci_excludes_zero))
        warn <- c(warn, "first stage at the cutoff has a robust CI that includes zero: weak first stage; a fuzzy estimate would be unreliable")
    }
    if (design == "auto") {
      checks$design_used <- if (sharp_pattern) "sharp" else "fuzzy"; checks$design_source <- "data"
      warn <- c(warn, sprintf("design inferred from the compliance pattern (%s); declare design explicitly from the plan", checks$design_used))
    } else {
      checks$design_used <- design; checks$design_source <- "declared"
      if (design == "sharp" && !sharp_pattern) warn <- c(warn, "declared sharp but the data show imperfect compliance (fuzzy_pattern)")
      if (design == "fuzzy" && sharp_pattern) warn <- c(warn, "declared fuzzy but compliance is perfect (sharp_pattern); the fuzzy estimate equals the sharp one")
    }
  } else {
    checks$design_used <- if (design == "auto") "sharp" else design
    checks$design_source <- if (design == "auto") "default_no_treatment_column" else "declared"
    if (design == "fuzzy") stop("rd_prepare: design = fuzzy requires a treatment column")
    if (design == "auto") warn <- c(warn, "no treatment column: estimates are reduced-form discontinuities in the outcome (intent-to-treat at the cutoff)")
  }
  checks$warnings <- warn
  prep$checks <- checks
  prep
}

rd_estimate <- function(prep, p = NULL, kernel = NULL, h = NULL, b = NULL, vce = NULL, design = NULL, covs = prep$covs,
                        bwselect = NULL, deriv = NULL, q = NULL, few_clusters_total = FEW_CLUSTERS_TOTAL, few_clusters_side = FEW_CLUSTERS_SIDE) {
  # covariates declared in rd_prepare adjust the estimate by default; pass covs = NULL explicitly to estimate without adjustment
  covs_source <- if (missing(covs)) "prep" else "argument"
  p <- if (is.null(p)) prep$options$p else p
  kernel <- if (is.null(kernel)) prep$options$kernel else kernel
  bwselect <- if (is.null(bwselect)) prep$options$bwselect else bwselect
  vce <- if (is.null(vce)) prep$options$vce else vce
  vce <- match.arg(vce, c("nn", "hc0", "hc1", "hc2", "hc3", "cluster"))
  design <- if (is.null(design)) prep$checks$design_used else match.arg(design, c("sharp", "fuzzy", "kink"))
  if (design == "fuzzy" && is.null(prep$treatment)) stop("rd_estimate: fuzzy design requires a treatment column in rd_prepare")
  if (design == "kink") { if (is.null(deriv)) deriv <- 1; if (is.null(p) || p < 2) p <- max(p, 2) } else if (is.null(deriv)) deriv <- 0
  if (!is.null(prep$treatment) && !is.null(prep$first_stage)) {
    fs <- prep$first_stage$estimate
    if (!is.finite(fs) || fs <= 0)
      stop("rd_estimate: first stage at the cutoff is not positive (estimate ", round(fs, 3), "); fix the cutoff side or the treatment variable instead of estimating")
  } else if (!is.null(prep$treatment) && is.null(prep$first_stage)) {
    if (!(prep$checks$treatment_mean_above > prep$checks$treatment_mean_below))
      stop("rd_estimate: treatment mean is not higher above the cutoff and no first stage could be estimated")
  }
  res <- .rd_fit(prep, p = p, q = q, kernel = kernel, h = h, b = b, vce = vce, fuzzy = (design == "fuzzy"), covs = covs, bwselect = bwselect, deriv = deriv)
  if (design == "kink") res$fuzzy <- FALSE
  res$covs_source <- covs_source
  res$spec <- list(outcome = prep$y, running = prep$x, cutoff = prep$cutoff, design = design, design_source = prep$checks$design_source,
                   estimand = switch(design, sharp = "average effect at the cutoff", fuzzy = "effect for compliers at the cutoff (local Wald ratio)", kink = "change in the slope of the outcome at the cutoff (numerator of the kink estimand; divide by the policy slope change for a sharp kink effect; fuzzy kink not supported)"))
  warn <- character(0); unresolved <- character(0)
  if (design == "fuzzy") {
    fs <- .rd_fit(prep, p = p, q = q, kernel = kernel, h = h, b = b, vce = vce, covs = covs, bwselect = bwselect, deriv = 0, treatment_as_outcome = TRUE)
    res$first_stage <- fs[c("estimate", "se_conventional", "se_robust", "ci_robust", "p_robust", "h", "b", "n_eff", "vce_used", "package_warnings", "call_options")]
    res$first_stage$ci_excludes_zero <- !(fs$ci_robust[1] <= 0 && 0 <= fs$ci_robust[2])
    res$first_stage$note <- "first stage with the main call's options (treatment on the centred running variable); the Wald ratio divides by this jump"
    if (!res$first_stage$ci_excludes_zero) { warn <- c(warn, "weak first stage inside the bandwidth (robust CI includes zero); the fuzzy estimate is unreliable"); unresolved <- c(unresolved, "weak first stage: consider a reduced-form (intent-to-treat) interpretation or a different design") }
  }
  if (!is.null(res$cluster_var)) {
    cb <- res$in_bandwidth$clusters
    if (cb$total < few_clusters_total || min(cb$left, cb$right) < few_clusters_side) {
      warn <- c(warn, sprintf("few clusters inside the bandwidth (total %d, left %d, right %d): cluster-robust inference is unreliable", cb$total, cb$left, cb$right))
      unresolved <- c(unresolved, "few clusters inside the bandwidth: plan a wild cluster bootstrap or randomization inference alternative before reporting")
    }
  }
  sp <- res$in_bandwidth$support_points
  res$discreteness_level <- if (min(sp$left, sp$right) < FEW_SUPPORT_POINTS_SIDE) "do_not_certify" else if (min(sp$left, sp$right) < CAVEAT_SUPPORT_POINTS_SIDE) "caveat_required" else "none"
  if (res$discreteness_level == "do_not_certify") {
    warn <- c(warn, sprintf("DO NOT CERTIFY: fewer than %d running-variable support points inside the bandwidth on a side (left %d, right %d); the local-polynomial CI is not credible; use honest CIs (discrete branch)", FEW_SUPPORT_POINTS_SIDE, sp$left, sp$right))
    unresolved <- c(unresolved, "discrete running variable inside the bandwidth: honest confidence intervals (RDHonest-type) are not computed by this template; decide whether to add that dependency")
  } else if (res$discreteness_level == "caveat_required") {
    warn <- c(warn, sprintf("caveat required: %d to %d support points inside the bandwidth on a side (left %d, right %d); report honest CIs alongside", FEW_SUPPORT_POINTS_SIDE, CAVEAT_SUPPORT_POINTS_SIDE - 1, sp$left, sp$right))
  }
  if (design == "kink" && !is.null(prep$treatment)) warn <- c(warn, "kink design: the treatment column is not used; the estimate is the change in the outcome slope (numerator of the kink estimand); a policy-kink scale (scalepar) and fuzzy kinks are not implemented")
  if (length(res$package_warnings)) warn <- c(warn, paste0("rdrobust: ", res$package_warnings))
  res$warnings <- warn; res$unresolved <- unresolved
  res
}

rd_diagnostics <- function(prep, est, h_multipliers = c(0.5, 0.75, 1, 1.25, 1.5, 2), n_placebo = 4,
                           donut = NULL, run_density = TRUE, run_balance = TRUE) {
  d <- prep$data
  o <- est$call_options
  common <- list(p = est$p, q = est$q, kernel = est$kernel, vce = est$vce_requested, covs = est$covs, bwselect = if (est$bwselect == "manual") prep$options$bwselect else est$bwselect, deriv = est$deriv)
  fit_with <- function(...) do.call(.rd_fit, c(list(prep = prep, fuzzy = est$fuzzy), common, list(...)))
  strip <- function(r) r[c("estimate", "se_robust", "ci_robust", "p_robust", "h", "b", "n_eff", "vce_used", "in_bandwidth", "package_warnings", "call_options")]
  out <- list(template_version = TEMPLATE_VERSION, spec_options = o)
  if (run_density) {
    den <- tryCatch(.with_warnings(rddensity::rddensity(X = d$.xc, c = 0)), error = function(e) NULL)
    out$density_test <- if (is.null(den)) list(status = "failed") else
      list(status = "observed", test = "rddensity (Cattaneo-Jansson-Ma local polynomial density test)", statistic = "test$t_jk (jackknife t)", t_stat = unname(den$value$test$t_jk),
           p_value = unname(den$value$test$p_jk), h_left = unname(den$value$h$left), h_right = unname(den$value$h$right), package_warnings = den$warnings,
           interpretation = "small p-value indicates a density discontinuity at the cutoff (possible manipulation); neither a rejection nor a non-rejection proves anything by itself")
  }
  if (!is.null(est$first_stage)) out$first_stage <- est$first_stage
  out$bandwidth_sensitivity <- lapply(h_multipliers, function(m) {
    r <- tryCatch(fit_with(h = est$h * m, b = est$b * m), error = function(e) NULL)
    if (is.null(r)) return(list(multiplier = m, h = est$h * m, status = "failed"))
    c(list(multiplier = m), strip(r))
  })
  qs_l <- stats::quantile(d$.xc[d$.xc < 0], probs = seq(0.2, 0.8, length.out = ceiling(n_placebo / 2)))
  qs_r <- stats::quantile(d$.xc[d$.xc >= 0], probs = seq(0.2, 0.8, length.out = floor(n_placebo / 2)))
  out$placebo_cutoffs <- lapply(c(qs_l, qs_r), function(cc) {
    side <- if (cc < 0) d$.xc < 0 else d$.xc >= 0
    r <- tryCatch(do.call(.rd_fit, c(list(prep = prep, fuzzy = FALSE, cutoff_shift = unname(cc), subset = side), common)), error = function(e) NULL)
    if (is.null(r)) return(list(cutoff = unname(cc) + prep$cutoff, status = "failed"))
    c(list(cutoff = unname(cc) + prep$cutoff, side = if (cc < 0) "left" else "right", treatment_held_fixed = TRUE,
           window_truncated_by_true_cutoff = (abs(unname(cc)) < r$h[if (cc < 0) 2 else 1])), strip(r))
  })
  if (run_balance && !is.null(prep$covs)) {
    out$covariate_balance <- lapply(prep$covs, function(v) {
      r <- tryCatch(do.call(.rd_fit, c(list(prep = prep, y_var = v, fuzzy = FALSE, h = est$h, b = est$b), common[setdiff(names(common), "covs")])), error = function(e) NULL)
      if (is.null(r)) return(list(covariate = v, status = "failed"))
      c(list(covariate = v, bandwidth_rule = "main estimate's bandwidths reused (same window)"), strip(r))
    })
  }
  if (!is.null(donut)) {
    r <- tryCatch(fit_with(subset = abs(d$.xc) > donut), error = function(e) NULL)
    out$donut <- if (is.null(r)) list(radius = donut, status = "failed") else c(list(radius = donut), strip(r))
  }
  alt_p <- if (est$p == 1) 2 else 1
  r <- tryCatch(do.call(.rd_fit, c(list(prep = prep, fuzzy = est$fuzzy), common[setdiff(names(common), c("p", "q"))], list(p = alt_p))), error = function(e) NULL)
  out$polynomial_order_check <- if (is.null(r)) list(p = alt_p, status = "failed") else c(list(p = alt_p, bandwidth_rule = "re-selected with the same selector"), strip(r))
  out$prepare_checks <- prep$checks
  out$estimate_warnings <- est$warnings; out$estimate_unresolved <- est$unresolved
  out
}

rd_plot <- function(prep, est, file = NULL, nbins = NULL) {
  d <- prep$data
  if (!is.null(file)) grDevices::pdf(file, width = 6, height = 4)
  on.exit(if (!is.null(file)) grDevices::dev.off(), add = TRUE)
  args <- list(y = d[[prep$y]], x = d$.xc, c = 0, p = est$p, kernel = est$kernel, h = est$h,
               x.label = paste0(prep$x, " - ", prep$cutoff), y.label = prep$y, title = "RD plot (binned means, local polynomial fit within bandwidth)")
  if (!is.null(nbins)) args$nbins <- nbins
  res <- .with_warnings(do.call(rdrobust::rdplot, args))
  invisible(list(warnings = res$warnings))
}

rd_table_tex <- function(est, spec_id = "s1", label = "RD estimate") {
  fmt <- function(v, k = 3) formatC(v, format = "f", digits = k)
  cb <- est$in_bandwidth$clusters
  se_row <- if (!is.null(est$cluster_var)) sprintf("%s, clustered by %s (%d clusters inside the bandwidth: %d left, %d right; %d in the sample)", est$vce_used, est$cluster_var, cb$total, cb$left, cb$right, est$n_clusters_sample) else est$vce_used
  lines <- c("\\begin{tabular}{lc}", "\\hline", paste0(" & (", spec_id, ") \\\\"), "\\hline",
    paste0(label, if (est$spec$design == "kink") " (slope change)" else "", " & ", fmt(est$estimate), " \\\\"),
    paste0("(conventional SE) & (", fmt(est$se_conventional), ") \\\\"),
    paste0("Robust bias-corrected ", est$level, "\\% CI & [", fmt(est$ci_robust[1]), ", ", fmt(est$ci_robust[2]), "] \\\\"),
    paste0("Design & ", est$spec$design, " (", est$spec$design_source, ") \\\\"),
    paste0("Bandwidth $h$ (left, right) & ", fmt(est$h[1]), ", ", fmt(est$h[2]), " [", est$bwselect, "] \\\\"),
    paste0("Polynomial order & ", est$p, if (est$deriv > 0) paste0(" (derivative ", est$deriv, ")") else "", " \\\\"), paste0("Kernel & ", est$kernel, " \\\\"),
    paste0("Effective N (left, right) & ", est$n_eff[1], ", ", est$n_eff[2], " \\\\"), paste0("N (sample) & ", est$n_total, " \\\\"),
    paste0("SE & ", se_row, " \\\\"),
    paste0("Covariates & ", if (is.null(est$covs)) "none" else paste(est$covs, collapse = ", "), " \\\\"),
    paste0("Weights & ", if (is.null(est$weights_var)) "none" else est$weights_var, " \\\\"))
  if (!is.null(est$first_stage)) lines <- c(lines, paste0("First stage at cutoff & ", fmt(est$first_stage$estimate), " [", fmt(est$first_stage$ci_robust[1]), ", ", fmt(est$first_stage$ci_robust[2]), "] \\\\"))
  tex_esc <- function(s) gsub("([%&_#])", "\\\\\\1", gsub("\\\\", "/", s))
  for (w in est$warnings) lines <- c(lines, paste0("Caveat & \\parbox[t]{9cm}{", tex_esc(substr(w, 1, 220)), "} \\\\"))
  for (u in est$unresolved) lines <- c(lines, paste0("Unresolved & \\parbox[t]{9cm}{", tex_esc(substr(u, 1, 220)), "} \\\\"))
  if (!is.null(est$discreteness_level) && est$discreteness_level != "none") lines <- c(lines, paste0("Discreteness level & ", est$discreteness_level, " \\\\"))
  c(lines, "\\hline", "\\end{tabular}",
    paste0("% notes: estimand: ", est$spec$estimand, "; point estimate is the conventional local polynomial estimate, the interval is the bias-corrected robust CI (Calonico-Cattaneo-Titiunik); ",
           "variance estimator as reported by rdrobust (", est$vce_used, "); generated by rd_analysis.R ", TEMPLATE_VERSION,
           if (length(est$warnings)) paste0("; warnings: ", paste(est$warnings, collapse = " | ")) else ""))
}

rd_report <- function(prep, est, diag, out_dir, spec_id = "s1") {
  dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
  est_out <- est[setdiff(names(est), "fit")]
  est_out$spec_id <- spec_id
  est_out$environment <- rd_env()
  jsonlite::write_json(est_out, file.path(out_dir, "estimates.json"), auto_unbox = TRUE, pretty = TRUE, digits = NA, null = "null", na = "null")
  jsonlite::write_json(diag, file.path(out_dir, "diagnostics.json"), auto_unbox = TRUE, pretty = TRUE, digits = NA, null = "null", na = "null")
  writeLines(rd_table_tex(est, spec_id), file.path(out_dir, "rd_table.tex"))
  pl <- rd_plot(prep, est, file = file.path(out_dir, "rd_plot.pdf"))
  files <- list(list(path = file.path(out_dir, "estimates.json"), kind = "results"), list(path = file.path(out_dir, "diagnostics.json"), kind = "results"),
                list(path = file.path(out_dir, "rd_table.tex"), kind = "table"), list(path = file.path(out_dir, "rd_plot.pdf"), kind = "figure"))
  writeLines(vapply(files, function(f) f$path, character(1)), file.path(out_dir, "outputs.txt"))
  invisible(list(spec_id = spec_id, design = est$spec$design, outputs = files, plot_warnings = pl$warnings))
}

run_rd <- function(data, y, x, cutoff, treatment = NULL, cluster = NULL, covs = NULL, weights = NULL, design = "auto",
                   p = 1, kernel = "triangular", bwselect = "mserd", vce = NULL, h = NULL, b = NULL, donut = NULL, deriv = NULL,
                   out_dir = NULL, spec_id = "s1") {
  prep <- rd_prepare(data, y, x, cutoff, treatment, cluster, covs, weights, design = design, p = p, kernel = kernel, bwselect = bwselect, vce = vce)
  est <- rd_estimate(prep, h = h, b = b, covs = covs, deriv = deriv)
  diag <- rd_diagnostics(prep, est, donut = donut)
  if (!is.null(out_dir)) rd_report(prep, est, diag, out_dir, spec_id)
  list(prep = prep, estimate = est, diagnostics = diag)
}
