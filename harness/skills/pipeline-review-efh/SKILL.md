---
name: pipeline-review-efh
description: Review a multi-script research pipeline in any language before delivery. Keep checks on consequential data boundaries; find misplaced comparison, variant and run code, silenced errors, fallback branches, typed numbers and missing boundary checks. Never judges by counts of if, assert or print. Not for method or inference review.
---

# Pipeline review

A delivered pipeline builds data, estimates and exports, and stops when a property it relies on fails. Judge where code sits and which data boundaries are guarded, not how many checks exist: less code, same guarantees. The [workflow](../../workflows/pipeline-review.md) holds skip conditions, modes and the rerun rule. Read [calibration](references/calibration.md) before writing findings; [locate](references/locate.md) has search patterns.

## Evidence

Each finding cites a **line** read in context, a **run-time count** from a retained inspection script with its log line, a **constructed case** run through the coded and the declared rule, or a **rerun** comparing results files. Anything else is labelled a conjecture. A script you did not read has not been checked.

## Procedure

1. List the scripts the entry point runs, in order, with the files each reads and writes. Mark those that build fitted samples, those that read the file of published values (by path; do not open it), and where comparison, variant and run code sit.
2. Read every script that builds a fitted sample. Search the rest with the locate patterns and read each hit in context.
3. On each primary fitted sample, count values off a declared scale: out-of-range values, stored nonresponse codes, and non-integers on an integer scale even inside its range; missing sources in derived indicators; regressors constant on all but one or two rows; components copied to every member row before a total; and unmatched or repeated keys at joins that build the sample. Cite an inspection log that covers a count, or write one short inspection script outside the pipeline ([idioms](../panel-data-checks-efh/code-examples.md)). Without a runtime, list the counts as not run.
4. Run a constructed case through each declared variant, fallback and precedence rule and compare it with the declared text. Then classify and rank.

## Keep

- Guards on key uniqueness, merge cardinality and match status, the sample rule, assignment exclusivity, cluster identifiers, value domains and missing propagation, even when verbose; simplify only to an equivalent check.
- Estimation output, fitted N and cluster counts in the log, and a tabulation placed directly after the operation it inspects.
- Inspection scripts and logs, one comparison program, and one guard against stale results: a completion marker, or clearing only the derived folders the entry point creates.

Remove a check only when all three calibration questions answer no; when unsure, keep it and mark `author input`.

## Move or remove

Once confirmed, these are findings:

- published values read or asserted in a build or exhibit script ([paper-first step 6](../../workflows/paper-first-replication.md));
- variants estimated in exhibit scripts instead of one sensitivity script;
- run machinery beyond what the runtime's failure reporting needs, such as deletion beyond the derived folders the entry point creates;
- a silenced error or forced option at a data step, or around an estimation whose results are used later;
- a branch whose quantity depends on which file, variable, column or package exists, unless declared.

## Add

- Any nonzero step 3 count, including a regressor that acts as an observation dummy: propose a declared rule with its alternative, and a guard only where later code relies on the property, once, where it is created.
- Typed or pre-rounded exhibit numbers: read them from results ([tables and figures](../tables-figures-efh/SKILL.md)).
- Variant code that departs from its declared rule: correct one side and record which.
- A cited check without a retained script: retain it or label the claim a conjecture.

## Integrity

Justify a finding or fix by the boundary it guards. Never propose, rank or justify a change by whether it moves a result toward a published value; a gap to a published value is not a finding. Never encode another package's errors or unit-specific edits as rules. Add no frameworks, test suites or configuration files.

## Output

At most ten findings, ranked as in calibration, with repeated patterns grouped:

| Rank | Location | Evidence | Role or boundary | Finding and effect | Action | Status |
|---|---|---|---|---|---|---|

Action: `move`, `add`, `fix` or `remove`. Status: `applied`, `proposed`, `author input`, `conjecture` or `open` (not run). Then list each kept boundary guard with its location, one per line, and what was not read or run.
