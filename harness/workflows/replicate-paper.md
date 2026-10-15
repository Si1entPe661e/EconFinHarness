# Read code or independently reproduce a paper

Choose the reproduction mode before opening implementation files. A request to reproduce from the paper, work blind, or avoid code answers selects [paper-first replication](paper-first-replication.md). In that mode, read the paper and appendix, inspect authorized data, and write an independent implementation; do not open author programs, notebooks, command histories, or packaged answer tables. A file inventory is permitted. Keep this boundary unless the user changes it.

For an authorized code-reading or code-execution task, use `literature-verification-efh` to locate the paper and available source code, then read the actual sample construction, estimation and export calls. Choose methods through the [composition guide](../skill-composition.md).

- For static reading, explain observation units, variables/timing, estimands, effects, weights, inference and exports. Distinguish unobserved information from procedures not implemented.
- For translation or execution, preserve statistical meaning through `panel-data-checks-efh`, the main method and `inference-clustering-efh`. Use available software and authorized data, and inspect the fitted sample through the [analysis workflow](empirical-analysis.md). On an executed author package, run the [pipeline review](pipeline-review.md) check-only: an error both pipelines share cannot appear in a comparison of their results.
- For comparisons, use the [presentation workflow](present-results.md) to compare compatible estimands, samples and inference. Synthetic demonstrations establish implementation behavior, not original empirical estimates.

One agent may combine `literature`, `code-engineer` and `empirical-analyst` responsibilities. Deliver relevant scripts, outputs and actual differences, identifying the work as static reading, a synthetic demonstration or an original-data reproduction.
