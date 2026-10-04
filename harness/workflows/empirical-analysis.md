# Implement an empirical analysis

Use the [composition guide](../skill-composition.md) to select relevant steps. One agent can perform the necessary responsibilities; continue an existing analysis at the step that needs work.

1. Define the question, estimand, available data and existing research choices. Select the main method and use `literature-verification` when a claim needs support.
2. Construct the sample using applicable `panel-data-checks`. Define observation units, dates, treatment/instrument/prediction timing, weights and comparison groups. Prediction tasks also define training, validation, test samples and label availability.
3. Specify the model, controls, fixed effects and diagnostics under the main method. Combine with `inference-clustering` to account for assignment, sampling and dependence. Preserve specialized intervals and tests, and decide effects separately from clustering.
4. Implement and run the selected model. Retain fitted objects or method-specific numerical results. Inspect the fitted/evaluation sample, absorbed variables, singleton/bandwidth/matching losses and actual cluster counts.
5. Revisit affected choices when identifying variation disappears, instruments are weak, clusters are few, support is poor or prediction leaks. Use a common sample for appropriate comparisons; otherwise explain differences. Do not select specifications by significance.
6. Use the [presentation workflow](present-results.md) and `tables-figures` for descriptions, balance, main results, diagnostics and necessary sensitivities from the same analysis.
7. Use `research-explanation` or `academic-writing` for requested interpretation or prose. Correct conflicts between results and text using actual outputs.

Deliver the scripts, requested results and a concise explanation of research choices, output locations and substantive gaps.

For a company panel: `panel-data-checks → panel-fe + inference-clustering → tables-figures`. With a staggered province policy, use `did` as the main method and `event-study` for dynamics. Firm/year effects do not automatically imply firm clustering. Count clusters on the fitted sample.
