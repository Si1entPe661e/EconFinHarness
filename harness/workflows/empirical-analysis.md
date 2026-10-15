# Implement an empirical analysis

Use the [composition guide](../skill-composition.md) to select relevant steps. One agent can perform the necessary responsibilities; continue an existing analysis at the step that needs work.

1. Define the question, estimand, available data and existing research choices. Select the main method and use `literature-verification-efh` when a claim needs support.
2. Construct the sample using applicable `panel-data-checks-efh`. Define observation units, dates, treatment/instrument/prediction timing, weights and comparison groups. Prediction tasks also define training, validation, test samples and label availability.
3. Specify the model, controls, fixed effects and diagnostics under the main method. Combine with `inference-clustering-efh` to account for assignment, sampling and dependence. Preserve specialized intervals and tests, and decide effects separately from clustering.
4. Implement and run the selected model in plain scripts that follow [lean code](../skills/pipeline-review-efh/references/lean-code.md). Retain fitted objects or method-specific numerical results. Inspect the fitted/evaluation sample, absorbed variables, singleton/bandwidth/matching losses and actual cluster counts.
5. Revisit affected choices when identifying variation disappears, instruments are weak, clusters are few, support is poor or prediction leaks. Use a common sample for appropriate comparisons; otherwise explain differences. Do not select specifications by significance.
6. Use the [presentation workflow](present-results.md) and `tables-figures-efh` for descriptions, balance, main results, diagnostics and necessary sensitivities from the same analysis.
7. Use `research-explanation-efh` or `academic-writing-efh` for requested interpretation or prose. Correct conflicts between results and text using actual outputs.

Deliver the scripts, requested results and a concise explanation of research choices, output locations and substantive gaps. Before delivering a pipeline of several scripts, run the [pipeline review](pipeline-review.md) unless its skip conditions apply.

For a company panel: `panel-data-checks-efh → panel-fe + inference-clustering-efh → tables-figures-efh`. With a staggered province policy, use `did-efh` as the main method and `event-study-efh` for dynamics. Firm/year effects do not automatically imply firm clustering. Count clusters on the fitted sample.
