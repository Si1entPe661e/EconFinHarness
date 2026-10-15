---
name: academic-writing-efh
description: Write or revise academic prose using actual research results and traceable literature.
---

# Academic writing

Use the available plan, actual results, figures and literature. Do not require an administrative output bundle before writing.

- Organize the section around data and sample, the specification and identifying assumptions, results, magnitude and uncertainty, robustness and limitations as relevant.
- Read numerical values from actual outputs. Keep the sample, fixed effects, weights and standard errors consistent between text and table notes.
- Separate estimates from interpretation and prior literature. Use causal language only when the design supports it.
- Report meaningful units, uncertainty and a sourced benchmark; explain what a null result can and cannot rule out.
- Cite papers with artid / DOI, and mark citations or details that could not be confirmed.
- Leave a clear placeholder for missing material. Do not invent estimates or claim a check was run when it was not.
- Use plain academic prose. Avoid quality claims without evidence and generic limitations that do not apply to the study.
- For a long manuscript, `templates/claims_to_evidence.md` can help connect key claims to outputs. It is optional; individual paragraphs do not need a separate mapping file.
- If the underlying results change, revisit the affected text as needed.

Before delivery, run the [revise module](../../workflows/revise-writing.md) unless its skip conditions apply: `defensive-writing-check-efh`, then `logic-check-efh`, then the fact comparison. Deliver the requested draft or revision. Table notes and pending items can be included in the same document.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Use the selected method and tables-figures-efh outputs to preserve estimand, sample, units, FE, weights and uncertainty in prose. Numerical or interpretation conflicts return to the affected analysis/output step; a writing-only request does not trigger new estimation.

## Research records

Recorded practice is in `harness/paradigms/`: each method's folder and `_all/reported.md` across methods. It describes what papers did, not what is correct.
