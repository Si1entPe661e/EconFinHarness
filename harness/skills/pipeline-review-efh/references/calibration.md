# Calibration

Read this before writing findings. A finding names a location, its evidence, the role or boundary at stake, what a silent failure or the current placement would change, and the action.

## Three questions for every check

1. **Boundary.** Does it guard keys, merge cardinality, the sample rule, assignment or group membership, cluster identifiers, timing, weights, a value domain or missing propagation?
2. **Consequence.** If the property failed without an error, would a reported estimate, N or label change?
3. **Reliance.** Does later code rely on it, for example a one-to-one merge, one row per unit in a stacked file, or a bounded scale entering an index?

Keep a check when question 1 names a boundary and question 2 or 3 is yes. Remove it only when all three are no. Move it when it compares with published values or only reports progress to its producer. When unsure, keep it and mark `author input`.

A guard is redundant only when the lines before it establish the property by construction, such as the mean of a variable just standardized. A property that depends on the input data, such as every unit having exactly one arm or a key being non-missing, is never established by construction.

## Classify code by what it does

- A conditional that creates or changes values (`if` qualifiers, `cond()`, `ifelse()`, `case_when()`, `np.where()`, logical indexing) is a specification rule. It needs a declared rule and an explicit missing-value branch, not a guard.
- A conditional that stops the run (`assert`, `stopifnot`, `raise`, `error`) is a guard. Judge it with the three questions.
- A conditional that switches modes, variants or paths takes the role of what it switches and moves with it.
- An error-swallowing wrapper (`capture`, `try`, `tryCatch`, `except`) is proportionate around idempotent housekeeping, such as making a folder or dropping a program that may not exist. Around reading, joining, building or estimating it can hide a boundary failure.
- Printing estimates, fitted N and cluster counts is provenance; keep it. A tabulation, duplicate listing or missing-value count placed directly after the operation it inspects is a proportionate check. Printing every intermediate data state in delivered scripts is a readability item at most.

## Common constructs

An `if` that lays out a table, a `display` of a progress count and a `print` of a data head are not findings by themselves; if nothing uses or cites them and they fill the log, they are rank 6. An `if` guard on a path or global that the entry point always sets is an unreachable guard, also rank 6. A `capture` or `try` around a merge or an estimation is rank 1 or 2, because it can hide a boundary failure. A missing `assert` matters only where a boundary is unguarded and its count is nonzero or unknown.

## Over-engineered validation and its replacement

[Lean code](lean-code.md) lists the common patterns (existence branches, progress printing, handlers around data steps, redundant or published-value assertions, re-verified package algebra, self-testing run machinery) and their lean replacements. Each is a finding only after the three questions above.

Missing error handling in a research script is not a finding: a stopped run is the right response.

## Not findings

- Counts of `if`, `assert`, `capture`, `try`, `print`, `display` or `stopifnot` lines, comment volume or script length, in either direction. A package with no assertions is not deficient by count, and one with many is not over-engineered by count.
- Control flow that implements the specification, such as branches by group, respondent type or period; comments that state a rule; labels.
- Cleaning code whose length follows the raw data; a different but working idiom, package or style.
- Missing unit tests in analysis code.
- Unit-specific corrections in cleaning code that cite a source. At most suggest a correction file that the build reads. An edit or drop keyed on an identifier is a finding only when it sits in an analysis script or changes the sample rule.
- A significance legend or a fixed threshold typed in a note.
- A gap between a result and its published value.

## Assertion or comparison

Assert what the program must satisfy whatever the paper reports: unique and non-missing keys, merge cardinality, exclusive arms, non-missing cluster identifiers, the stated sample rule, and the result of a declared cleaning rule. Compare what the paper reports: N, means, coefficients, standard errors and p-values. An asserted published N stops the build when a correct data fix changes the sample, and it rewards reproducing another package's errors. Rewrite it as the sample rule it stood for and move the target to the comparison program.

## Run machinery

How much is proportionate depends on how the runtime reports a failed step and on the audience. Stata in batch mode exits 0 after an error, so it needs a completion marker, removed at the start and written last, and a check of the log for error lines. R and Python exit nonzero, so the exit status suffices. A public package exercised by repository tests can justify a runner and its tests; a single reproduction cannot.

## Ranking

1. A missing or broken guard at a boundary where a silent failure changes a reported number, including a handler or forced option that can hide one.
2. Published values read or asserted in build or exhibit scripts, which can stop or steer the build.
3. Variant code that departs from its declared rule; a cited check with no retained computation.
4. Exhibit numbers typed by hand or rounded before export.
5. Placement: variants in exhibit scripts, several match rules, excess run machinery.
6. Readability: unreachable guards, bulk printing, duplicated blocks, inconsistent names for one variant, comments that cite only an identifier.

Report at most ten findings; one finding lists every location of a repeated pattern.

## Rerun and effect

Before applying changes, copy the numeric results files or note their commit. After the rerun, compare each file byte for byte (`cmp before.csv after.csv`), or read both versions and require exact equality at full precision; drop fields that record a date or run time. A move or removal that changes any number is reverted and reported.

A change caused by an added boundary check is reported with its rule, its alternative and its effect, measured on the primary specification as the change in N and in units of the estimate's own standard error. It is a post-result change under the producing workflow and is never reverted to restore agreement with a published value. Agreement with a published value is never the effect.

## Integrity limits

- Never propose, rank or justify a change by whether it moves a result toward a published value.
- Never encode another package's errors or unit-specific edits as rules.
- Never remove a check that guards a consequential boundary, even when asked for leaner code; rewrite it into an equivalent form, or state the conflict and keep it.
- A moved check still runs somewhere.
