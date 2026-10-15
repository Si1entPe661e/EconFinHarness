# Defensive-writing patterns

Use these signals to find candidates, then judge each by its function: does the sentence add evidence, scope, logic, conceptual precision or reader guidance? A phrase on this list is not automatically wrong, and a sentence absent from it can still be defensive.

## Types and signals

Use these type names in the instance table, translated when the table is in another language. Structural types are defined in [results and experiments](results-and-experiments.md). Record `kept` only for plausible candidates; a `kept` row takes the type it was a candidate for.

| Type | English signals | Chinese signals |
|---|---|---|
| Unnecessary disclaimer | "This paper does not claim…", "We do not attempt to…", "This is not to say…", "This should not be taken to mean…", "It is beyond the scope of this paper…" | 本文并不声称……、我们并不试图……、这并不是说……、这不应被理解为……、超出了本文的范围 |
| Stacked hedge | "may potentially suggest", "could possibly", "to some extent", "somewhat", "it might be argued that" | 或许可能、在一定程度上可能、似乎可能、某种意义上 |
| Self-weakening wording | "unfortunately", self-belittling "only" or "merely", "modest", "a preliminary attempt", "admittedly", "still lags far behind", "limited effect", "far from perfect" | 遗憾的是、自我贬低的仅/仅仅/只是、初步尝试、只能提供有限参考、仍有很大提升空间、仍明显落后、效果有限、不尽如人意、不可否认 |
| Self-limiting contrast | A "not X but Y" whose X is the author's own possible claim: "The goal is not X but Y", "Rather than arguing X, this paper argues Y", "Instead of a full theory, we…" | 目标不是 X，而是 Y；本文并非论证 X，而是论证 Y；与其说本文……不如说…… |
| Limitation-first opening | "Although this study has limitations…", "While the sample is small…", "Despite these shortcomings…" | 尽管本研究存在局限……、虽然样本有限……、尽管存在上述不足…… |
| Misplaced limitation | A caveat in the abstract, introduction, contribution paragraph, topic sentence, executive summary or conclusion that the claim there does not need; the same limitation repeated in several sections | 摘要、引言、贡献段、段首句或结论中重复出现的局限说明 |
| Process narration | "We first tried…, but…", "After several attempts…", "Initially we…" | 我们首先尝试了……但……、经过多次尝试……、起初我们…… |
| Conceded comparison | The paper's own method, estimate or contribution described as losing: "underperforms", "falls short of", "fails to beat", "is inferior to", "loses to" | 不如、落后于、未能超过、劣于、输给（指本文方法或贡献） |
| Unstated advantage | A gain that a test of the difference rejects at the paper's level, left unstated or called "competitive" or "comparable"; a design advantage the text does not state | 结果具有竞争力、表现相当（差异检验显著却未说明）、未说明的设计优势 |
| Unqualified advantage | An empirical advantage stated without its comparison, condition or test, such as an accuracy gain with no evaluation condition | 实证优势未说明比较对象、条件或检验 |
| Overclaim | A claim broader than its evidence, with or without a protective caveat such as "of course, this may not hold everywhere"; narrow the claim | 结论过宽（无论是否补一句"当然也存在局限"） |
| Weak ending | "Much work remains", "These results should be interpreted with great caution", a conclusion that introduces new weaknesses | 仍有大量工作有待完成、结果需谨慎解读、结论段新增一串不足 |
| Draft note | An author note, comment or tracked change, especially one proposing to drop or alter a result; quote it as `author input` and leave it in place | 稿件中的批注或备忘，尤其是建议删除或修改结果的批注 |

Also check: paragraphs whose first sentence is a caveat (a design statement that governs the estimate after it is not one); explanations added only to prevent a hypothetical misunderstanding of the author's own claim; contribution statements that diminish themselves; paragraphs that mix argument, caveat, apology, exception and clarification (give each paragraph one job); redundant "however", "nevertheless" and "although". Ritual signposting ("It is worth noting that", 值得注意的是), a "not A but B" whose A belongs to others or is decorative, and objection-and-rebuttal sentences ("One might worry that…") belong to the logic pass (filler, rhetorical symmetry, refuting an unmade claim); in a defensive-only run, report them here and apply the logic pass's keep rules.

## Keep these

- Hedges tied to the design or evidence: "is associated with" in an observational analysis, "suggests" for suggestive evidence, a single warranted "may", a condition such as "under these conditions", an interval or minimum detectable effect. Decide from the evidence, not from the word.
- Significance levels and p-values. "Only significant at the 10% level" may lose "only", but not the level: "is significant at the 10% level (p = 0.08)" or "在10%水平上显著（p = 0.08）". Never shorten it to "significant" or 显著.
- "Only", 仅 or 只 that restricts where, when or for whom a result holds: "significant only for firms below median size", "仅在2008年后的样本中显著". Deleting it widens the claim. Rephrase the tone if needed, but keep the restriction: "the effect is concentrated among firms below median size; for larger firms it is [author: estimate]".
- "Only" or 仅 as an informative count or share: "only 3% of firms adopt" when the rarity matters to the argument.
- The estimand label wherever a headline estimate is stated: intent-to-treat, LATE for compliers, local to the cutoff, ATT, partial equilibrium, the population and period. It is part of the claim, not a limitation.
- A guard against a misreading the paper's own estimate plausibly invites, stated once and preferably as positive scope: "The estimate measures reallocation across neighboring counties, not the aggregate employment effect."
- Identification threats and their answers, tested or not; the logic pass decides how they are stated.
- Wording about the studied policy, asset, fund, firm or population rather than the paper's own contribution: "active funds underperform their benchmarks by [x] a year", "该补贴对就业的效果有限（[x]，不显著）". These are findings.
- A magnitude characterized against a benchmark ("modest relative to [study]'s estimate", "economically small: 0.02 SD") and a diagnostic's verdict stated beside its statistic ("the test rejects parallel pre-trends, p = 0.01").
- "Preliminary" or 初步 for a genuinely preliminary design such as a pilot.
- A scope condition whose omission would mislead the reader in that exact sentence, including in the abstract or conclusion.
- A contrast that is itself the argument, for example distinguishing two estimands or two mechanisms.
- Limitations without which a reader would misread or misuse the result: an unresolved threat to identification, an estimand or population narrower than the headline wording, a measurement problem that changes the interpretation, or a condition for correct use. Cut generic limitations that hold for any study of its kind and bear on no stated claim.
- Legal, ethical and safety limits needed for accuracy or correct use, and disclosure statements the venue requires.
- A design statement placed before the estimate it governs, such as "The estimates in this section are descriptive"; leave it in place.
- In a response to referees, a direct acknowledgment of a valid point and the change made: "We agree; Section 5 now reports…".
- In reports and briefings, statements of what a check, test or completion does not establish.

## Placement

| Section | What belongs there |
|---|---|
| Abstract, executive summary, introduction, contribution paragraph, topic sentences, conclusion | The contribution and result; only qualifications essential to the stated claim |
| Data and methods | Sample, period, design assumptions and scope conditions, stated positively |
| Results | Conditions, metric, magnitude and uncertainty of each finding, favorable or not, and identification diagnostics |
| Discussion or limitations | One consolidated, specific statement per real limitation and what it means for interpretation |

Move a misplaced limitation; do not delete it. Moving or merging a single limitation sentence into its section is a local fix. When removing a repeated limitation, confirm that one statement of it remains in its section. A vague limitation with no statement in its section ("the results may not generalize") is restated there once as positive scope from the draft's own sample, period and outcome, for example "The estimates apply to [population] in [period] and measure [outcome]"; an `[author: …]` marker alone does not count as that statement. Deleting the last statement of a real limitation is `proposed`. A vague remark about sample size or precision is not a real limitation when the estimates carry standard errors or intervals; delete it as a local fix, and ask for the interval in an `author input` row if it is missing.

## Positive openings

"This paper examines…", "The analysis focuses on…", "The evidence indicates…", "This design allows…", "The central contribution is…", "In this setting, X is associated with Y"; 本文研究……、本文重点分析……、证据表明……、该设计可以……、主要贡献在于……. Use "X affects Y through…" (X 通过……影响 Y) only when the design identifies the effect and the draft makes the mechanism claim.

## Rewrite examples

The examples show phrasing only. Every bracketed placeholder is `[author: …]`; facts in a revision come from the draft or its sources.

| Defensive | Direct |
|---|---|
| We do not claim that these cases are representative of all contexts. | The analysis covers [author: cases, period, setting]. |
| This paper is not intended to provide a comprehensive theory of platform governance, but rather to examine one specific mechanism. | This paper identifies a mechanism through which platform governance changes participation. |
| This does not mean that policy design alone determines implementation outcomes. | Implementation outcomes depend on how policy design interacts with administrative capacity. (Only if the draft makes this argument with a design that supports it.) |
| We are not arguing that this model is superior in every situation. | The model is most useful when [author: condition stated in the draft]. |
| These results may potentially suggest that X could possibly be associated with Y. | X is associated with Y in this observational analysis. |
| While the sample is limited and cannot capture every variation, it still offers useful insights. | The sample covers [author: units, period, N]. If sample size limits precision, report the interval or minimum detectable effect in the results. |
| Unfortunately, the effect on wages is only 2% and statistically insignificant. | The wage effect is 2% and not statistically different from zero ([author: confidence level and interval]); the estimate rules out effects larger than [author: upper bound]. |
| The coefficient is only marginally significant (p = 0.08). | The coefficient is significant at the 10% level (p = 0.08). |
| We first tried OLS, which failed, and then moved to IV. | OLS gives [author: estimate]; we instrument X with Z because [author: endogeneity argument]. [author: if IV was adopted after the OLS result was seen, say so here.] Table [author: n] reports both. |
| We first tried two other data sources, which did not work, and only then used the survey. (memo) | The estimates come from the survey; two other data sources ([author: which]) did not yield usable estimates. |
| 本文仅在两个数据集上做了初步尝试，只能提供有限参考。 | 本文在两个数据集上评估该方法。 |
| 尽管本研究存在诸多不足，但仍具有一定参考价值。 | 本研究利用[author: 数据/设计]估计了[author: 效应]。（具体局限放到讨论部分） |

Metric example, given a draft that reports both numbers under the same test conditions:

| Defensive | Direct |
|---|---|
| 遗憾的是，该方法在准确率上仍明显落后于基线。 | 该方法将延迟从 100 ms 降至 60 ms，准确率为 89%，基线为 90%。 |

Keep 初步, 可能 and 提示 when the evidence warrants them. Do not add 显著, 全面领先, "significantly" or "substantially" to sound stronger; the logic pass checks intensifiers.

## Final pass

Reread the revision. Remove any remaining sentence whose main job is to protect the author's own claims against a hypothetical objection rather than add evidence, scope, logic or reader guidance; leave objection-and-rebuttal sentences to the logic pass. Confirm that every real limitation still appears once in its section. Then read for tone: direct and confident where the evidence supports it, with numbers rather than promotional adjectives carrying the strength.
