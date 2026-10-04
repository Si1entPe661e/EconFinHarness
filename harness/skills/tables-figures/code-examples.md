# Result export commands

Examples use standardized variable names and an existing in-memory analysis sample. Export to an explicit results folder, replace only the requested outputs, and retain the chosen fitted results. Paths below are illustrative.

## 1. R: absorbed fixed effects and LaTeX with etable

df contains y, x, baseline, firm and year. The analyst has selected firm clustering. Both models use the same complete input sample; cluster counts below use each model's actual retained observations.

~~~r
library(fixest)
dir.create("results", showWarnings = FALSE, recursive = TRUE)
vars <- c("y", "x", "baseline", "firm", "year")
sample <- df[complete.cases(df[, vars]), vars]
m1 <- feols(y ~ x + baseline | firm, data = sample, cluster = ~firm)
m2 <- feols(y ~ x + baseline | firm + year, data = sample, cluster = ~firm)
models <- list("Firm FE" = m1, "Firm and year FE" = m2)
clusters <- vapply(models, function(m) {
  length(unique(sample$firm[obs(m)]))
}, integer(1))
etable(
  models, file = "results/main.tex", tex = TRUE, replace = TRUE,
  digits = 3, fitstat = ~n + wr2,
  signif.code = c("***" = 0.01, "**" = 0.05, "*" = 0.10),
  dict = c(x = "Main regressor", baseline = "Baseline control"),
  extralines = list("Firm clusters" = clusters),
  notes = "Standard errors clustered by firm are in parentheses."
)
numeric_table <- etable(models, tex = FALSE, digits = 6, fitstat = ~n + wr2)
write.csv(numeric_table, "results/main_display.csv", row.names = FALSE)
coefficient_rows <- do.call(rbind, lapply(names(models), function(name) {
  m <- models[[name]]
  ct <- coeftable(m)
  ci <- confint(m)
  data.frame(model = name, term = rownames(ct), estimate = ct[, 1],
             std_error = ct[, 2], statistic = ct[, 3], p_value = ct[, 4],
             ci_low = ci[, 1], ci_high = ci[, 2],
             n = nobs(m), firm_clusters = clusters[[name]], row.names = NULL)
}))
write.csv(coefficient_rows, "results/main_numeric.csv", row.names = FALSE)
~~~

main_display.csv contains a formatted table; main_numeric.csv retains numeric coefficients and uncertainty. etable reads the stored inference unless explicitly overridden. For two-way clustering, count and label both dimensions.

## 2. R: HTML/LaTeX and a table data frame with modelsummary

Continue from the fitted models above. Firm FE labels below reflect these specific model calls.

~~~r
library(modelsummary)
rows <- data.frame(
  term = c("Firm FE", "Year FE", "Firm clusters"),
  "Firm FE" = c("Yes", "No", as.character(clusters[[1]])),
  "Firm and year FE" = c("Yes", "Yes", as.character(clusters[[2]])),
  check.names = FALSE
)
stars <- c("***" = 0.01, "**" = 0.05, "*" = 0.10)
modelsummary(
  models, output = "results/main.html", fmt = 3,
  statistic = "({std.error})", stars = stars,
  coef_map = c(x = "Main regressor", baseline = "Baseline control"),
  gof_map = c("nobs"), add_rows = rows,
  notes = "Standard errors clustered by firm are in parentheses."
)
modelsummary(
  models, output = "results/main_modelsummary.tex", fmt = 3,
  statistic = "({std.error})", stars = stars,
  coef_map = c(x = "Main regressor", baseline = "Baseline control"),
  gof_map = c("nobs"), add_rows = rows
)
tab <- modelsummary(models, output = "data.frame", fmt = NULL, stars = FALSE)
write.csv(tab, "results/modelsummary_rows.csv", row.names = FALSE)
~~~

LaTeX exports are table fragments. Include the chosen backend's required preamble packages when inserting them into a paper: etable/booktabs output uses booktabs, while modelsummary's tinytable backend can require tabularray and its printed support commands.

fmt = NULL preserves available numeric precision, but this data frame can also contain labels and fit statistics. Use the explicit coefficient export in example 1 for a uniform numeric coefficient table. Do not override vcov merely to get an export; a changed covariance can change p-values and stars. Use escape = FALSE only for deliberately supplied LaTeX/HTML markup.

## 3. Stata: stored estimates, FE/cluster rows and regression export

The loaded data contain y, x, baseline, firm and year. reghdfe and estout commands are user-written. The example creates LaTeX and RTF files from the same stored results.

~~~stata
capture mkdir results
eststo clear
tempvar common
gen byte `common' = !missing(y, x, baseline, firm, year)
reghdfe y x baseline if `common', absorb(firm) vce(cluster firm)
estadd local firm_fe "Yes"
estadd local year_fe "No"
tempvar tag1
egen `tag1' = tag(firm) if e(sample)
quietly count if `tag1' == 1
estadd scalar G_firm = r(N)
eststo m1

reghdfe y x baseline if `common', absorb(firm year) vce(cluster firm)
estadd local firm_fe "Yes"
estadd local year_fe "Yes"
tempvar tag2
egen `tag2' = tag(firm) if e(sample)
quietly count if `tag2' == 1
estadd scalar G_firm = r(N)
eststo m2

esttab m1 m2 using "results/main.tex", replace booktabs ///
    b(3) se(3) star(* 0.10 ** 0.05 *** 0.01) ///
    keep(x baseline) coeflabels(x "Main regressor" baseline "Baseline control") ///
    mtitles("Firm FE" "Firm and year FE") ///
    stats(N G_firm firm_fe year_fe, ///
          labels("Observations" "Firm clusters" "Firm FE" "Year FE")) ///
    addnotes("Standard errors clustered by firm are in parentheses.")
esttab m1 m2 using "results/main.rtf", replace ///
    b(3) se(3) star(* 0.10 ** 0.05 *** 0.01) keep(x baseline) ///
    stats(N G_firm firm_fe year_fe)
~~~

Count clusters on e(sample), not all loaded rows. Clear stored estimates before a new table, and name the models explicitly to avoid stale wildcard selections. replace rewrites this output; append adds content and can duplicate tables if repeatedly rerun.

## 4. Stata: descriptive statistics with estpost/esttab

~~~stata
estpost tabstat y x baseline, statistics(count mean sd p5 p50 p95) columns(statistics)
esttab using "results/descriptive.tex", replace booktabs ///
    cells("count(fmt(0)) mean(fmt(3)) sd(fmt(3)) p5(fmt(3)) p50(fmt(3)) p95(fmt(3))") ///
    collabels("N" "Mean" "SD" "P5" "Median" "P95") ///
    nonumber nomtitles noobs label
~~~

Counts are nonmissing observations per variable. This is a descriptive table; its SD columns are not standard errors or experimental balance tests.

## 5. Stata: a numeric coefficient table in Excel

Restore a specific fitted model. r(table) is produced by the replayed regress command; do not assume every estimator populates it the same way.

~~~stata
regress y x baseline i.year, vce(cluster firm)
matrix result = r(table)'
putexcel set "results/coefficients.xlsx", replace
putexcel A1 = matrix(result), names
~~~

For an estimator with a custom ATT, interval set or bootstrap result, export its actual result matrices rather than the underlying regression's r(table). putexcel is built in; Excel output can require a separate table title and notes for presentation.

## 6. Python: statsmodels regression tables with summary_col

df contains complete y/x/baseline/firm/year data. This example uses explicit FE indicators and is suitable when their dimension is manageable.

~~~python
from pathlib import Path
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col

out = Path("results")
out.mkdir(parents=True, exist_ok=True)
sample = df[["y", "x", "baseline", "firm", "year"]].dropna().copy()
fits = []
for formula in [
    "y ~ x + baseline + C(firm)",
    "y ~ x + baseline + C(firm) + C(year)",
]:
    fits.append(smf.ols(formula, data=sample).fit(
        cov_type="cluster",
        cov_kwds={"groups": sample["firm"], "use_correction": True},
        use_t=True,
    ))
table = summary_col(
    fits, model_names=["Firm FE", "Firm and year FE"],
    stars=True, float_format="%0.3f",
    regressor_order=["x", "baseline"], drop_omitted=True,
    info_dict={"N": lambda r: f"{r.nobs:.0f}"},
)
(out / "main.html").write_text(table.as_html(), encoding="utf-8")
(out / "main.tex").write_text(table.as_latex(), encoding="utf-8")
(out / "main.txt").write_text(str(table), encoding="utf-8")
~~~

summary_col uses the result's p-values for its documented star convention. Add notes identifying covariance, FE, weights and actual clusters when finalizing the table. It is a statsmodels exporter and should not be passed an unsupported PanelOLS or custom ATT object.

## 7. Python: method-specific numeric results and panel models

The first part exports the actual PanelOLS coefficient results without parsing formatted output. The input index must be firm then year.

~~~python
import pandas as pd
from linearmodels.panel import PanelOLS

panel = sample.set_index(["firm", "year"]).sort_index()
assert not panel.index.duplicated().any()
model = PanelOLS.from_formula(
    "y ~ 1 + x + baseline + EntityEffects + TimeEffects",
    data=panel, drop_absorbed=True,
)
result = model.fit(cov_type="clustered", cluster_entity=True, debiased=True)
ci = result.conf_int(level=0.95)
rows = pd.DataFrame({
    "term": result.params.index,
    "estimate": result.params.to_numpy(),
    "std_error": result.std_errors.to_numpy(),
    "p_value": result.pvalues.to_numpy(),
    "ci_low": ci.iloc[:, 0].to_numpy(),
    "ci_high": ci.iloc[:, 1].to_numpy(),
})
rows["n"] = result.nobs
rows["firm_clusters"] = result.resids.index.get_level_values("firm").nunique()
rows.to_csv(out / "panel_numeric.csv", index=False)
rows.to_excel(out / "panel_numeric.xlsx", index=False)
~~~

For group-time ATT, forecast metrics, structural moments, balance or sensitivity results, first build a labelled numeric frame from that method's actual output. Then the export operations are:

~~~python
from pathlib import Path

out = Path("results")
out.mkdir(parents=True, exist_ok=True)
numeric_results.to_csv(out / "method_results.csv", index=False)
numeric_results.to_excel(out / "method_results.xlsx", index=False)
numeric_results.to_html(out / "method_results.html", index=False,
                        float_format=lambda x: f"{x:.3f}")
numeric_results.to_latex(out / "method_results.tex", index=False,
                         escape=True, float_format=lambda x: f"{x:.3f}")
~~~

numeric_results is the actual result frame supplied by the method step, not invented estimates. to_latex needs pandas' LaTeX rendering dependencies; Excel needs an appropriate writer. Explicitly label bootstrap/permutation p-values, simultaneous bounds or unusual confidence sets rather than replacing them with generic normal intervals.

## 8. R: an event-study figure from the same fitted estimator

For a fitted Sun–Abraham fixest object named event_fit, preserve its clustering/aggregation and export the plot directly.

~~~r
pdf("results/event-study.pdf", width = 7, height = 4.5)
iplot(event_fit, ref.line = 0, xlab = "Event time",
      main = "Dynamic treatment effects")
dev.off()
~~~

Label the reference period, comparison group and whether intervals are pointwise or simultaneous in the accompanying note. For RD, use the RD estimator/plot commands and report the window and cutoff; do not relabel an arbitrary polynomial fit as the RD estimate.

## 9. R: firm/time FE with province clustering and weights

df contains y, x, baseline, firm, year, province and positive weight. The analyst has chosen province-level dependence based on assignment/sampling. Fixed effects remain firm and year. Few independent provinces may need the inference skill's specialized procedure rather than the analytic covariance illustrated here.

~~~r
library(fixest)
dir.create("results", showWarnings = FALSE, recursive = TRUE)
vars <- c("y", "x", "baseline", "firm", "year", "province", "weight")
d <- df[complete.cases(df[, vars]), vars]
stopifnot(all(is.finite(d$weight)), all(d$weight > 0),
          !anyDuplicated(d[, c("firm", "year")]))
fit <- feols(y ~ x + baseline | firm + year, data = d,
             weights = ~weight, cluster = ~province)
used <- d[obs(fit), ]
G <- length(unique(used$province))
etable(fit, tex = TRUE, file = "results/panel_province.tex", replace = TRUE,
       fitstat = ~n + wr2, extralines = list("Province clusters" = G),
       notes = "Weighted estimates; firm and year FE; SE clustered by province.")
ct <- coeftable(fit)
ci <- confint(fit)
numbers <- data.frame(
  term = rownames(ct), estimate = ct[, 1], std_error = ct[, 2],
  statistic = ct[, 3], p_value = ct[, 4],
  ci_low = ci[, 1], ci_high = ci[, 2], n = nobs(fit),
  province_clusters = G, row.names = NULL
)
write.csv(numbers, "results/panel_province_numeric.csv", row.names = FALSE)
~~~

Use the same fit and numbers for subsequent discussion. If the covariance or fitted sample changes, regenerate the affected interval/test/table fields and notes. A label change alone does not require refitting the model.
