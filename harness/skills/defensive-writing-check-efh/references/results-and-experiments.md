# Results, comparisons and experiments

Use this reference for principles 1 and 4 to 9, the structural types, the genre rules for openings and endings, and the change table.

## Structural types

These types describe the document rather than a phrase. Report each in the document-level findings and add a table row wherever it has a location.

| Type | Principle | Finding |
|---|---|---|
| Off-contribution narrative | 1 | Setup or sections that serve no stated contribution; a secondary or subgroup estimate leading, replacing or appearing unlabeled beside the primary one |
| Comparison framing | 4 | A comparison basis chosen after the results, a dropped benchmark, or the largest estimate used as the headline |
| Experiment without a job | 7 | An experiment, table or figure that answers none of the four questions below; part of the evidence map |
| Missing evidence | 7 | A claim that needs an analysis the draft lacks, such as an ablation or a test of a difference |
| Opening order | 8 | The abstract or introduction does not reach problem, gap, idea and central result; a memo that does not open with the decision |
| Ending | 9 | A conclusion that negates itself or drops the scope of the takeaway |

## Choose the comparison by an objective stated before the results

1. Find the objective in a source that predates the results: a request that commissioned the analysis before its results existed (not a later request to write or revise), a research plan, a pre-analysis plan or registration, a dated earlier version or design document, or the author's explicit statement that the objective came first. In a supplied draft, the author's statement of what the method is constructed to deliver also counts when the property follows from the construction (lower cost, latency or data needs, weaker assumptions); record it in a `kept` row. When the reviser also drafted the text, its own draft is not such a source.
2. Lead with comparisons on that objective. Report the conventional or pre-specified benchmark beside them, framed as a tradeoff when it is worse. Adding a one-sentence statement of that objective where the problem is introduced is a local fix.
3. A comparison basis may lead when it matches that objective and either is the field's standard basis for it (an equal compute or data budget for an efficiency objective, out-of-sample fit for a forecasting objective) or is documented in a source that predates the results. Report the conventional basis beside it in every case. A subpopulation, horizon or outcome basis always needs such a source.
4. Do not change the evaluation criteria to avoid an unfavorable result. Choosing the metric, sample, specification, horizon, reference period, outcome definition or benchmark after seeing which one favors the method is specification search. So are dropping a standard benchmark and reporting a favorable subsample as the main result.
5. When a source that predates the results states the objective and the method is worse on it, the comparison on that objective stays the lead comparison, described by conditions and size (principle 5); other metrics follow as further dimensions or tradeoffs. Do not ask whether the method was designed for another metric. When no objective is stated in such a source, keep the draft's comparisons in their order and add an `author input` row: "Which objective was the method designed for, and which dated document records it?" Changing the lead comparison is `proposed` until it is answered.

Economic magnitude complements statistical evidence and never replaces it. Describe an imprecise estimate by the range its interval rules out, not by the economic size of its point estimate.

Tradeoff sentence:

> Under the same test conditions, the method reduces latency from 100 ms to 60 ms; accuracy is 89% compared with the baseline's 90%.

Avoid "the lower accuracy reveals limitations of the method", and avoid omitting the accuracy number.

## Unfavorable results

1. Decide whether the result affects the central conclusion or its interpretation. If it does, it stays in the main text. If it answers the primary question, it also appears in the abstract.
2. State the conditions, metric, magnitude and uncertainty, keeping both numbers and the direction of the gap ("an 8% reduction, below the 12% that [author: study] reports for [measure]"). Use neutral verbs for the paper's own result ("is", "equals", "is lower than"), not "fails" or "loses".
3. When the draft, its tables or sources document a difference between the compared items (data, compute, tuning, sample, unit, outcome, estimand, assumptions), state it next to the result. A source's statement that its estimate covers components the draft's estimate excludes, or uses a different unit or outcome, links the gap to that difference: write that the two estimates measure different targets and name the components. A general property from a source or method skill without evidence that it operates here is stated as a candidate ("consistent with", with its citation) beside the result, with an `author input` row asking for the diagnostic. When the cause is unknown, do not supply one.
4. Check whether a claim exceeds the evidence. Narrow it to the supported conditions, or withdraw it.
5. Check whether a local observation has been described as a general defect of the method.
6. Put the limitation in the relevant section once. Keep in the abstract or conclusion only the qualifications without which the headline claim would mislead.

A null or imprecise estimate is a finding. Report what it rules out with the interval or minimum detectable effect, keep its significance statement, and do not apologize for it.

Diagnostics of the identifying assumption stay in the main text with their test statistics: pre-trend and placebo tests, covariate balance, first-stage strength, overidentification tests, density or manipulation tests and covariate continuity at a cutoff, and sensitivity bounds. Only extra detail on a diagnostic that passed may move to an appendix. A diagnostic qualifies the headline when its joint or pre-specified test rejects, or when the estimate without the failing units or periods differs from the headline by more than its standard error; state such a diagnostic once in the abstract and once in the conclusion. A single significant coefficient under a passing joint test, with an exclusion estimate close to the headline, stays in the main text with its numbers.

## Every experiment has a job

Each experiment, robustness table, heterogeneity analysis or figure answers at least one question:

- Does the method or effect hold?
- What explains the advantage or effect (mechanism, ablation)?
- Can alternative explanations be ruled out (placebo, falsification, alternative specifications)?
- Under what conditions does it apply (heterogeneity, external validity)?

Report the evidence map as a document-level finding: item, question, claim. For a report or briefing, map each piece of evidence to the decision it informs. Cutting, merging or moving an item that answers none or duplicates another follows the change table. Protected items are unfavorable results bearing on the conclusion, pre-specified outcomes and analyses, analyses a referee requested and identification diagnostics: they are never cut, and moving one leaves a main-text pointer with its direction, size and uncertainty. When an experiment is missing, name the claim that lacks support and add an `author input` row at that claim's location, for example: without an ablation of module A, the gain cannot be attributed to A. Do not write a blanket "the experiments are insufficient".

## State the advantage

- A design advantage (weaker assumptions, a new source of variation, new data, coverage, a capability prior methods lack) is stated directly, with what the compared methods require and a citation.
- A fixed quantity (cost, data requirements, runtime on stated hardware) is stated with the measured difference.
- An estimate or sample-dependent metric is called an advantage only when a test of the difference, or an interval for it, excludes zero at the level the paper uses, for example a Diebold-Mariano test, a paired bootstrap or a test of equal coefficients. Non-overlapping intervals at that level also suffice; a one-standard-error gap does not. "Relative to [author: baseline], [author: method] reduces out-of-sample RMSE by [author: magnitude] (Diebold-Mariano p = [author: value]) on [author: data]." When no such test is reported, give both numbers without the word "advantage" and ask for the test in an `author input` row. A difference the test does not reject stays "similar" or "comparable", with both numbers.

An advantage the draft's own numbers and tests show is not a new fact; state it. When the draft reports a design-based or heterogeneity-robust estimate beside a conventional one, state the difference in size and precision and the estimator property its sources state. Use "significant" only for a stated test.

## Openings

Abstract and introduction order: problem, gap in existing work, the idea, the central result with its main-specification estimate (the one in the paper's main table; when a pre-analysis plan fixes a different primary specification, report the plan's estimate beside it and ask which leads in an `author input` row), and the qualifications the headline needs, each once: its estimand and population label, and any diagnostic or null primary result that qualifies it. The answer to the primary or pre-specified question is the first estimate stated, whatever its sign; state a null or imprecise answer in words beside its estimate ("has no detectable effect on X (estimate, s.e.)"). The research plan fixes which question and outcome are primary; without a plan, the supplied draft or the analysis request does. A secondary outcome, subgroup or heterogeneity result may follow it, labeled as secondary, and never precedes or replaces it. A non-estimate contribution (design, data, capability) may lead. Do not headline the largest estimate across specifications, subsamples, horizons or outcomes. A gap limited to what a supplied source says it does or does not study is sourced; write it with that citation. Move process, background the reader already knows and secondary results later.

A decision memo or briefing opens, in at most four sentences, with the decision requested, the recommendation with its main condition, the cost and timing when the reader asked for them, and the risk the draft ranks highest; background figures follow. If an unresolved `author input` item could change the decision or who approves it, the opening says so. When deleting a defensive opening leaves no opening, or only a roadmap or other signposting, write that paragraph from the draft's own recommendation, figures and conditions; this is a local fix. In a report, a data gap without the owner or date the reader asked for is Missing evidence.

## Endings

Restate the main takeaway and its scope once, then the implication for the reader's decisions or research. A diagnostic or null primary result that qualifies the headline, by the threshold above, stays, stated plainly. Limitations already discussed are not repeated as a closing list. Future work is concrete and short. Do not end with a sentence that undercuts the result beyond what the evidence shows.

## Change table

A draft produced earlier in the same task counts as the agent's own draft. A request that invokes the launch principles for the opening and narrative is a structural-revision request for the abstract, introduction and conclusion.

| Change | Supplied draft | Agent's own draft |
|---|---|---|
| Local: rewording; deleting a sentence or paragraph that reports no estimate, test, diagnostic, comparison, limitation, scope condition, identification threat, deviation or disclosure and that no later claim, option or recommendation uses; adding or reordering sentences within one paragraph, and reordering paragraphs within the abstract or introduction to reach problem, gap, idea and central result, from the draft or its sources; moving or merging a single limitation sentence into its section; in a report or briefing, deleting a background fact that informs no decision and is not an estimate, test, diagnostic or comparison | Apply | Apply |
| Structural: reordering or merging sections; moving paragraphs between sections | `proposed` unless structural revision was requested | Apply |
| Moving an unprotected item without a job to an appendix, leaving a one-line main-text pointer | `proposed` unless the user asked for such cuts | Apply |
| Removing a reported estimate, test, diagnostic, comparison, experiment, table or figure; deleting the last statement of a real limitation | `proposed` | `proposed` |

For a line-editing request, apply wording-level fixes and propose content-level ones: paragraph deletion, reordering, added advantage statements and reordered comparisons.

## Referee comments

When simulating a referee, separate demonstrated problems, questions that need verification and optional extra experiments. When revising, address problems that affect the conclusion or its interpretation; do not turn every possible objection into a stated limitation.
