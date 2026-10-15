---
name: logic-check-efh
description: Check and fix argument logic and expression discipline in prose, such as straw men, rebuttals of unmade claims, contradictions, incoherent progression, sycophancy, parroting, reflexive symmetry, intensifiers, anthropomorphism, metaphor, idioms, unneeded jargon and filler. Use as the revise module's second pass or for logic checks (逻辑检查).
---

# Logic check and fix

Check that each paragraph advances a traceable argument and that its wording claims no more than can be verified. In the revise module it follows the defensive pass and removes inflation that pass introduced.

## Map the argument first

Record the central claim with its premises and evidence; each position attributed to others (user, cited author, "the literature", referee) with its source locator; and the definitions, samples, estimands and key numbers later sections rely on, with locations. For a multi-section document, write the map to a file such as `draft.argmap.md` and update it after each section.

## Categories

Argument integrity:

1. **Straw man (稻草人)**: an attributed position, including a gap claim about prior work, is weaker or more extreme than its source, and the text rebuts that version.
2. **Refuting an unmade claim (反驳空气)**: the text rebuts a position that no source, user, referee or earlier section stated.
3. **Internal contradiction (前后矛盾)**: a later premise conflicts with an earlier judgment without explanation, including drift in numbers, definitions, samples, estimands or causal language.
4. **Incoherent logic (逻辑断裂)**: consecutive sentences lack an inferential link, so related material accumulates without advancing the paragraph's claim.
5. **Sycophancy (谄媚)**: agreement with the requester's, author's, referee's or decision-maker's view beyond the evidence, praise in place of analysis, or positions attributed to someone who did not state them.
6. **Parroting (复读)**: restating the user, a source or earlier text in new words and presenting the restatement as analysis.

Expression discipline:

7. **Reflexive rhetorical symmetry (文体过度对称)**: "not A but B", "on the one hand… on the other", "on the surface… in reality" without a real contrast, or recurring through a section.
8. **Intensifier overuse (过度使用级别修饰)**: "very", "fundamentally", "truly", "profoundly" and similar at a degree the text cannot verify.
9. **Unwarranted anthropomorphism (无端拟人化)**: abstractions given intent, desire, judgment or agency beyond field convention.
10. **Excessive metaphor (过度比喻)**: figures that replace the mechanism, stack up or mix.
11. **Native-speaker idioms and slang (母语者俚语)**: colloquialisms that obscure meaning for an international readership.
12. **Excessive technical terminology (过度技术化名词)**: undefined jargon, acronyms or borrowed terms where plain words carry the meaning.
13. **Filler (废话)**: content whose deletion loses no argument, including boilerplate, repeated conclusions, ritual signposting and offers of further work ("接下来我们可以……").

Signals, tests, fixes and legitimate uses are in [categories](references/categories.md).

## Integrity limits

Replacement claims, magnitudes, citations and restated positions come only from the draft, the supplied sources or a `literature-verification-efh` record. Otherwise write `[author: needed fact]` and mark the row `author input`. Do not resolve a contradiction by choosing a side the sources do not settle.

## Procedure

1. Map the argument. Gather the user's verbatim request and stated positions, referee comments and the sources the draft summarizes or attributes positions to. A straw man whose source is unavailable is `author input`; a rebuttal of an uncited generic opponent is a finding.
2. Read paragraph by paragraph: state each paragraph's claim, then ask what each sentence adds and how it follows from the previous one.
3. Delete, rewrite, reorder, add a missing step from material in the draft or its sources, or mark `author input`. Fix a contradiction only when a source settles it, citing that source; otherwise mark both locations `author input`.
4. Keep the legitimate uses in categories, such as "the model predicts", defined specialist terms, a contrast that is the argument, the conclusion's one restatement of the takeaway and identification threats with their answers.
5. Reread changed paragraphs, then follow the [revision workflow](../../workflows/revise-writing.md).

## Output

First the blocking findings: unresolved contradictions, straw men and missing premises of the central claim. Then every instance in document order:

| Location | Original | Category | Problem or reason kept | Revision | Action |
|---|---|---|---|---|---|

Give one row per defect, listing every location. Action is `fixed`, `proposed`, `kept` or `author input` (any decision left to the author; say in Revision whether the text changed). Record `kept` only for plausible candidates. Write in the draft's language, keeping action labels and placeholders unchanged. Check-only mode returns only the findings and table. The reviser obeys the same rules: no praise of the draft, and no confirming a user's account of a source unread.
