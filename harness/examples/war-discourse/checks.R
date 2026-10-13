# Run with: Rscript harness/examples/war-discourse/checks.R
source("harness/examples/war-discourse/methods.R")
library(testthat)

test_that("the paper-first reader rejects programs, outputs and traversal", {
  root <- tempfile(); dir.create(root)
  saveRDS(data.frame(ym = 2000), file.path(root, "traded_factors.rds"))
  expect_equal(nrow(read_input("traded_factors.rds", root)), 1L)
  for (bad in c("../codes/00_protocol_nc.R", ".Rhistory", "../output/Table_1.xlsx", "other.rds"))
    expect_error(read_input(bad, root), "allowlist")
  external <- tempfile(fileext = ".rds"); saveRDS(1, external)
  file.symlink(external, file.path(root, "war_factors.rds"))
  expect_error(read_input("war_factors.rds", root), "escapes")
  unlink(c(root, external), recursive = TRUE)
})

test_that("access-log paths remain exact and fingerprintable", {
  root <- tempfile(); dir.create(root)
  saveRDS(1, file.path(root,"traded_factors.rds"))
  log <- tempfile()
  read_input("traded_factors.rds",root,log)
  logged <- readLines(log)
  expect_identical(logged,"traded_factors.rds")
  expect_false(anyNA(tools::md5sum(file.path(root,logged))))
  expect_error(fingerprint_inputs(file.path(root,"missing.rds")),"Cannot fingerprint")
  unlink(c(root,log),recursive=TRUE)
})

test_that("monthly keys reject duplicates and retain calendar gaps", {
  expect_equal(month_id(c(1978 + 7/12, 1978 + 10/12)), c(23743L, 23746L))
  expect_error(validate_months(data.frame(ym = c(2000, 2000))), "duplicate")
  mm <- 24000L + c(0:14, 16:30)
  xx <- sin(seq_along(mm)) + seq_along(mm)/10
  a <- ar_innovations(mm, xx, start = min(mm), min_pairs = 3)
  b <- ar_innovations(mm, xx, start = min(mm), min_pairs = 3, gap = "observed")
  expect_true(is.na(a[16]))
  expect_true(is.finite(b[16]))
})

test_that("expanding innovations cannot use future values", {
  mm <- 24000L + 0:59
  xx <- sin(seq_along(mm)/3) + seq_along(mm)/20
  yy <- xx; yy[40:60] <- yy[40:60] + 500
  for (inc in c(TRUE, FALSE)) {
    a <- ar_innovations(mm, xx, start = min(mm), include_current = inc)
    b <- ar_innovations(mm, yy, start = min(mm), include_current = inc)
    expect_equal(a[1:39], b[1:39])
    j <- 35
    ii <- 2:(j - as.integer(!inc))
    fit <- lm(xx[ii] ~ xx[ii-1L])
    prediction <- coef(fit)[1] + coef(fit)[2] * xx[j-1L]
    expect_equal(a[j], unname(xx[j] - prediction), tolerance = 1e-10)
  }
})

test_that("an AR estimation start excludes all earlier lagged information", {
  mm <- 23000L+0:79; xx <- sin(seq_along(mm)/3)
  changed <- xx; changed[1:20] <- changed[1:20]+1000
  for (gap in c("calendar","observed")) {
    a <- ar_innovations(mm,xx,start=mm[21],gap=gap)
    b <- ar_innovations(mm,changed,start=mm[21],gap=gap)
    expect_equal(a[21:80],b[21:80],tolerance=1e-10)
  }
})

set.seed(13482)
F <- matrix(rnorm(240 * 2), 240, 2, dimnames = list(NULL, c("f1", "f2")))
B <- matrix(rnorm(24), 12, 2)
R <- matrix(.01, 240, 12) + F %*% t(B) +
  matrix(rep(drop(B %*% c(.05, -.03)), each = 240), 240, 12) +
  matrix(rnorm(240 * 12, sd = .3), 240, 12)

test_that("two-pass uses average returns and full-sample exposures", {
  z <- two_pass(R, F)
  reference <- lm(colMeans(R) ~ z$beta)
  expect_equal(unname(z$lambda), unname(coef(reference)), tolerance = 1e-10)
  expect_equal(unname(colMeans(z$monthly_lambda)), unname(z$lambda))
  expect_equal(z$r2, summary(reference)$r.squared, tolerance = 1e-10)
  expect_equal(z$adjusted_r2, summary(reference)$adj.r.squared, tolerance = 1e-10)
})

test_that("Shanken covariance agrees with dense cross-asset calculation", {
  z <- two_pass(R, F)
  Z <- cbind(1, z$beta); A <- solve(crossprod(Z), t(Z))
  SigmaE <- crossprod(z$residuals) / nrow(R)
  SigmaF <- cov(F) * (nrow(F)-1)/nrow(F)
  reference <- (1 + z$shanken) * A %*% SigmaE %*% t(A) / nrow(R)
  reference[-1, -1] <- reference[-1, -1] + SigmaF / nrow(R)
  expect_equal(unname(z$covariance), unname(reference), tolerance = 1e-10)
  expect_true(min(eigen(z$covariance, symmetric = TRUE)$values) > 0)
})

test_that("factor units and level shifts cannot change pricing conclusions", {
  z <- two_pass(R, F)
  scaled <- two_pass(R, sweep(F, 2, c(10, .1), `*`))
  expect_equal(unname(scaled$lambda[-1]), unname(z$lambda[-1] * c(10, .1)))
  expect_equal(scaled$t, z$t, tolerance = 1e-9)
  shifted <- two_pass(R, sweep(F, 2, c(100, -10), `+`))
  expect_equal(shifted$lambda, z$lambda, tolerance = 1e-8)
  expect_equal(shifted$t, z$t, tolerance = 1e-8)
})

test_that("HAC explicitly implements Newey-West 1987 and not package defaults", {
  x <- sin(1:120/5) + cos(1:120/13)
  z <- hac_mean(x, lag = 6)
  fit <- lm(x ~ 1)
  e <- x - mean(x); n <- length(e)
  lrv <- sum(e^2)/n
  for (j in 1:6) lrv <- lrv + 2 * (1 - j/7) * sum(e[(j+1):n] * e[1:(n-j)])/n
  expect_equal(unname(z["se"]), sqrt(lrv/n), tolerance = 1e-12)
  expect_equal(unname(z["se"]), sqrt(sandwich::NeweyWest(fit, lag=6, prewhite=FALSE, adjust=FALSE)[1,1]))
})

test_that("HAC uses calendar distance across missing months", {
  x <- c(1, 3, 2, 5, 8, 4); mm <- c(1L, 2L, 5L, 6L, 9L, 10L)
  e <- x - mean(x); total <- sum(e^2)
  for (j in 1:3) {
    pairs <- which(outer(mm, mm, `-`) == j, arr.ind = TRUE)
    total <- total + 2 * (1-j/4) * sum(e[pairs[,1]] * e[pairs[,2]])
  }
  expect_equal(unname(hac_mean(x, 3, mm)["se"]), sqrt(total)/length(x), tolerance=1e-12)
  expect_false(isTRUE(all.equal(hac_mean(x, 3, mm)["se"], hac_mean(x, 3)["se"])))
})

test_that("regression HAC preserves the same calendar spacing as mean HAC", {
  x <- c(1,3,2,5,8,4); mm <- c(1L,2L,5L,6L,9L,10L)
  fit <- lm(x~1)
  expect_equal(sqrt(calendar_hac_vcov(fit,mm,3)[1,1]),unname(hac_mean(x,3,mm)["se"]),tolerance=1e-12)
  fit2 <- lm(x~I(x^2))
  expect_equal(calendar_hac_vcov(fit2,1:6,3),sandwich::NeweyWest(fit2,lag=3,prewhite=FALSE,adjust=FALSE))
  expect_error(calendar_hac_vcov(fit2,1:5,3),"match fitted")
})

test_that("industry predictions cannot use contemporaneous or future returns", {
  mm <- 24000L + 0:79
  rr <- data.frame(month = mm, R[, 1:12][1:80, ])
  ff <- data.frame(month = mm, WarFac = F[1:80,1], MKT = F[1:80,2])
  z <- industry_fmb(rr, ff, "WarFac", window=24, min_complete=24)
  changed <- rr; changed[70:80, -1] <- changed[70:80, -1] + 100
  zz <- industry_fmb(changed, ff, "WarFac", window=24, min_complete=24)
  expect_equal(z$slopes[z$month<mm[70], ], zz$slopes[zz$month<mm[70], ])
  expect_equal(range(rank_quintile(1:30)), c(0,1))
  expect_equal(rank_quintile(c(1,1,2,3,4))[1], rank_quintile(c(1,1,2,3,4))[2])
  missing_asset <- rr; missing_asset[1:30, 13] <- NA_real_
  incomplete <- industry_fmb(missing_asset, ff, "WarFac", window=24, min_complete=24)
  expect_equal(min(incomplete$month), min(z$month))
  expect_equal(incomplete$N[1], 11L)
})

cat("All independent implementation checks completed.\n")

test_that("vector graphics do not require svglite or an unavailable X11 library", {
  path <- tempfile(fileext=".eps")
  grDevices::postscript(path,width=4,height=3,onefile=FALSE)
  plot(1:3,1:3,main="Independent estimates")
  grDevices::dev.off()
  expect_true(file.exists(path) && file.info(path)$size>500)
  expect_true(any(grepl("%!PS-Adobe",readLines(path,warn=FALSE),fixed=TRUE)))
  unlink(path)
})

test_that("figure captions fit inside the actual export width", {
  path <- tempfile(fileext=".png")
  grDevices::png(path,width=9,height=5.5,units="in",res=180)
  lines <- strsplit(premium_caption(),"\n",fixed=TRUE)[[1]]
  widths <- vapply(lines,function(s) grid::convertWidth(
    grid::grobWidth(grid::textGrob(s,gp=grid::gpar(fontsize=9.6))),"inches",valueOnly=TRUE),numeric(1))
  grDevices::dev.off()
  expect_true(all(widths<8.6))
  unlink(path)
})
