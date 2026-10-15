# Review a research pipeline before delivery

The pipeline review checks a research pipeline of several scripts before others run or read it: where comparison, variant and run code sits, which data boundaries are guarded, and which checks are missing. It applies `pipeline-review-efh` to Stata, R, Python, MATLAB or other code. Identification, inference and export correctness belong to the [code audit](audit-code.md).

**When to run.** Run it before delivering a pipeline of several scripts that others will run: a reproduction ([paper-first step 7](paper-first-replication.md)), an [empirical analysis](empirical-analysis.md), a replication package or a shared project. Also run it when several agents wrote parts of one pipeline and when the user asks. On an executed author package it runs check-only ([code reading](replicate-paper.md)).

**Skip conditions.** Unless the user asks, skip it for a single script, exploratory work that is not delivered, or a change to labels or layout only. Skip it when the user declines. These conditions apply wherever a workflow, skill or role refers to the review.

**Who runs it.** The implementer applies the skill to its own pipeline and may apply the changes. Dispatch capability `pipeline-review` (role `pipeline-reviewer`, check-only) in a fresh context when several agents wrote the pipeline, rules or variants were added after results were seen, the code will be released as a replication package, the code is someone else's, or the user asks. The dispatched reviewer returns findings and, on request, a diff; the owner applies them and runs steps 4 and 5.

## Steps

1. **Fix the context.** Record the runtime, how it reports a failed step, and the audience: a single reproduction, a shared project or a public package exercised by tests. These set how much run machinery is proportionate.
2. **Freeze results.** Copy the numeric results files, or note their commit, and keep the last clean log.
3. **Review** with `pipeline-review-efh`: map the scripts, read those that build fitted samples, count the data boundaries on each primary fitted sample, and run constructed cases through declared variants and fallbacks.
4. **Apply and rerun.** Change only code you own or were asked to change; propose the rest. Never remove a guard on keys, merges, the sample rule, value domains or missing propagation. Rerun the entry point and compare every numeric results file with the frozen copy at full precision. A move or removal must leave them unchanged; otherwise revert it and report. A change caused by an added boundary check is reported with its rule, its alternative and its effect as a post-result change under the producing workflow, and is never reverted to restore agreement with a published value.
5. **Deliver** the findings table, the kept guards, the diff and rerun result, and what was not examined. Unapplied findings go to the delivery notes. The review never blocks delivery.

## Handoff

Declare as inputs the entry point, the scripts it runs, the specification with its declared variants, the last log and the derived datasets the counts read. Name the file of published values by path only and leave out the comparison output: the review needs to know which scripts read published values, not the values. Declare as outputs the findings file, an inspection script and its log, and a diff file when proposed edits are wanted; inputs cannot also be outputs. For a pipeline larger than the default 40,000-character read budget, raise the dispatcher's `max_read_chars` rather than splitting the scripts, because misplaced code often spans several of them. The native return summary is short, so the table goes in the findings file; if the host refuses report files from a subagent, return the full table in the final message instead.

**Before a fan-out.** When parallel workers will write parts of one pipeline, give each dispatch packet the shared conventions: exhibits write numeric results files and read no published values; one comparison program applies one rule; declared variants run in one sensitivity script; one completion marker guards against stale results. Run the review once, at the join.
