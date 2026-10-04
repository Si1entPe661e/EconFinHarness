---
name: code-annotation
description: Add useful English comments to research code while preserving its executable behavior.
---

# Code annotation

Read the code before commenting. Explain variable meaning, step purpose, implemented assumptions, inputs, outputs and non-obvious edge cases.

- Use the target language's comment syntax and keep executable statements in place.
- Preserve Stata continuation lines (`///`) and delimiter blocks, MATLAB continuation lines, strings and file encoding.
- Do not add Python docstrings unless requested; they can change observable behavior.
- Keep existing comments and avoid reformatting unrelated code.
- For corpus files under `Paper/`, deliver a derived copy, patch or sidecar using path and line numbers.
- For editable project code, make the requested comments directly.
- Inspect the diff; parse or run a focused comparison only when behavior is uncertain.
- If you find a logic problem, explain it rather than silently changing it as part of a comment task.

Deliver the requested annotated code or note. `templates/annotation-sidecar.md` is optional; no companion JSON is required.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Use relevant method/inference guidance to explain the existing analysis accurately. Keep executable behavior unchanged; an annotation-only task does not require running the full analysis workflow.
