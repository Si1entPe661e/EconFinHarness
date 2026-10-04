---
name: research-explanation
description: Explain existing research code, methods, results or project progress for the user.
---

# Research explanation

Read the sources needed to answer the user's question. Infer the audience from the request when clear; ask only if an ambiguous audience would materially change the explanation.

- Explain what matters in a useful order: purpose, relevant inputs, main operations, outputs and interpretation.
- Link useful file locations or use artid / DOI when citing papers. Mark inference or missing information in ordinary prose.
- For progress, use actual work and available files; investigate uncertainty about completion when it matters.
- Use diagrams when they clarify relationships.
- Default to chat. A saved Markdown note is optional, using `templates/explanation.md` when useful.

Explanations use existing material and do not create new numerical results.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Follow only the analysis steps needed to answer the question: sample, method, uncertainty and output. Explain the actual result quantity and identify consequential mismatches; explanation alone does not require rerunning the pipeline.
