# Lean research code

Read this while writing research code, not only when reviewing it. A research script builds data, estimates and exports, and stops when something it relies on fails. The runtime's own error is the right response to a missing file, variable or package. Each extra line needs a data boundary it guards or a number it produces.

## By default

- One entry point runs plain scripts in order. A one-off analysis needs no wrappers, classes, frameworks or configuration files.
- Estimation output, the fitted N and cluster counts in the log are the provenance; keep them.
- Development checks (inspection tabulations, cross-checks, comparisons with expected or published values) go in separate scripts with their logs, outside the entry point. Keep the ones you cite.

## Conditionals

- A conditional that creates values (`if` qualifiers, `cond()`, `ifelse()`, `np.where()`) is part of the specification: give it an explicit missing-value branch.
- Do not branch on whether a file, variable, column, matrix row or package exists. Declare the input and let a missing one stop the run.
- Do not guard paths or globals that the entry point always sets, and do not validate the arguments of a program called from one place.

## Printing

- No progress messages, banners or stage counters, and no `list` or print of whole datasets in delivered scripts.
- An inspection tabulation sits directly after the operation it inspects, or in an inspection script.

## Assertions

Assert once, where the property is created, when later code relies on it: unique and non-missing keys, merge cardinality and match status, the sample rule, exclusive arms or groups, non-missing cluster identifiers, and the result of a declared cleaning rule (value domain, missing propagation). Do not assert:

- what the previous command already guarantees: `merge m:1` already requires unique keys in the using file, `reshape` checks its keys, and a variable just standardized has mean 0;
- published or expected values (N, means, coefficients); compare them in the comparison script;
- package algebra or built-in behaviour, such as F equal to the squared t, 2SLS equal to the reduced form over the first stage, a recomputed sandwich covariance, or how a built-in command treats ties;
- properties of your own run machinery.

## Error handling

`capture`, `try`, `tryCatch` and `except` are for idempotent housekeeping only (`capture mkdir`, `capture log close`, `capture program drop`). Never put them around reading, merging, building or estimating. Do not supply a default when a conversion fails (`destring, force`, `errors="coerce"`, `suppressWarnings(as.numeric(...))`) unless the specification declares that fill rule.

## Run machinery

- Stata in batch mode exits 0 after an error: erase one completion marker at the start, write it last, and check the log for `r(` error lines. R and Python exit nonzero on error, so the exit status suffices.
- No status files, error handlers that write files, input fingerprints, access logs, fault-injection modes, tests of guards or of the runner, or loops that check package presence; record package versions in the README.
- A public example exercised by repository tests is the exception, and says so.

## Replacements

| Over-engineered | Lean |
|---|---|
| Stata: `capture confirm variable x` then `if _rc { gen x = ... }` | define `x` once where it is created |
| Stata: `display "[2/7] Estimating Table 3"` | nothing; the command log shows it |
| Stata: `capture noisily ivreg2 ...` | `ivreg2 ...` |
| Stata: `assert e(N) == 500`, a published N | the sample rule where the sample is built; compare 500 in the comparison script |
| Stata: `merge m:1 id using f` followed by `isid id` on `f` | `merge m:1 id using f, assert(match)` |
| R: `if (!requireNamespace("fixest")) stop(...)` | `library(fixest)` |
| R: `tryCatch(read.csv(f), error = function(e) NULL)` | `read.csv(f)` |
| R: `message("Step 3 done")` | nothing |
| Python: `if "x" in df.columns: ... else: ...` | `df["x"]`; a missing column raises |
| Python: `try: res = model.fit() except Exception: pass` | `res = model.fit()` |
| Python: `pd.to_numeric(s, errors="coerce")` | `pd.to_numeric(s)`, or a declared rule for each nonresponse code |
| Any: a hand-coded sandwich covariance to check `vce(cluster ...)` | the package option, with its documentation cited |
| Any: comparison blocks in each exhibit script | one comparison script with one rule |
| Any: deleting output folders, guarding the deletion and testing the guard | one completion marker, or clearing only the derived folders the entry point creates |
