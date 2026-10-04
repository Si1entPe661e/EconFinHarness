# References: panel-data-checks

All entries are `unverified`. Nothing in this table was checked against an online source or against the corpus while this skill was written. Verify before citing any entry in a research output. Where a DOI is not certain it is omitted rather than guessed.

| ref | kind | verification | note |
|---|---|---|---|
| Wooldridge, Econometric Analysis of Cross Section and Panel Data (2nd edition) | textbook | unverified | Panel structure, unbalanced panels, and sample selection from missing data. |
| Angrist and Pischke, Mostly Harmless Econometrics (2009) | textbook | unverified | Sample definition, attrition, and what a control adds or removes from the estimation sample. |
| Callaway and Sant'Anna, "Difference-in-Differences with Multiple Time Periods" (2021), Journal of Econometrics | method paper | unverified | Cohort structure and treatment timing bookkeeping in staggered designs. Cited here only for the timing consistency step. |
| Goodman-Bacon, "Difference-in-Differences with Variation in Treatment Timing" (2021), Journal of Econometrics | method paper | unverified | Why cohort composition and timing must be recorded before estimation. |
| Correia, "Singletons, Cluster-Robust Standard Errors and Fixed Effects: A Bad Mix" (working paper) | working paper | unverified | Singleton groups in fixed effect models and their effect on degrees of freedom. Verify the current version and title before citing. |
| Little and Rubin, Statistical Analysis with Missing Data | textbook | unverified | Missingness mechanisms and the difference between missing at random and missingness that is related to treatment. |
| Stata Manual, `duplicates`, `isid`, `merge`, `xtset`, `tsset`, `assert` | software documentation | unverified | https://www.stata.com/manuals/ Check the entry for the installed Stata version. |
| pandas documentation, `DataFrame.merge` (validate argument), `duplicated`, `set_index` | software documentation | unverified | https://pandas.pydata.org/docs/ The `validate` argument enforces merge cardinality. Check the installed version. |
| dplyr documentation, `left_join` with `relationship` and `unmatched` arguments | software documentation | unverified | https://dplyr.tidyverse.org/ Argument availability depends on the dplyr version. |
| data.table documentation, joins and keys | software documentation | unverified | https://rdatatable.gitlab.io/data.table/ |
| pointblank (R) and pandera (Python) data validation packages | software documentation | unverified | Optional tooling for expressing the checks in this skill as executable assertions. Not required by this skill. |
