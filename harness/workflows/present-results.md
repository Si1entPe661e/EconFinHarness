# Present research results

Use [tables-figures](../skills/tables-figures/SKILL.md) and the [composition guide](../skill-composition.md). The `code-engineer` responsibility usually covers exports; combine with `writer` when prose is needed.

1. Identify the requested comparison, existing results and target format. Read existing export code and model selection. Extract values from fitted models, ATT/marginal effects, prediction metrics or other method-specific outputs.
2. Use the [result-type guide](../skills/tables-figures/result-types.md) to select sample descriptions, balance, main results, diagnostics and sensitivities. Distinguish coefficients, marginal effects, SD, SE, intervals, CAR and evaluation loss.
3. Confirm the estimand, fitted sample, units, weights, effects and inference. Resolve missing choices through the main method, `panel-data-checks` or `inference-clustering`.
4. Keep full precision and use the [export commands](../skills/tables-figures/code-examples.md): Stata stored estimates/esttab/estpost/putexcel, R etable/modelsummary, or Python summary_col and numerical result DataFrames. Export existing results without refitting for layout.
5. Label columns and panels clearly. Explain sample differences, controls, effects, weights, clusters and relevant diagnostics. Use the same inference for intervals, p-values and stars; describe special tests or irregular confidence sets separately.
6. Plot the same estimates and state reference periods, windows/bandwidths, support, axes and interval types. Export useful editable and final formats and inspect the files for numerical consistency and readability.
7. Preserve actual quantities in prose. Correct extraction/export discrepancies; when the sample, model or inference changes, update all affected outputs and text.

Deliver the requested files and a short explanation. State specific missing data, models or inference while presenting the available results.
