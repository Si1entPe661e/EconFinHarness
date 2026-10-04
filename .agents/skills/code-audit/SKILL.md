---
name: code-audit
description: Check research code and its statistical reasoning for a requested scope or a concrete issue.
---

# Research code checking

Use this skill when the user requests a code or research check, or a concrete unresolved issue needs investigation. It can also support ordinary self-checking; no special context is required.

- Read the relevant data construction, sample filters, merges and treatment definitions.
- Follow the actual estimator call, including macros or arguments that supply fixed effects, weights, bandwidths and clustering.
- Assess inference against assignment and dependence, including cluster counts and small-sample concerns.
- Trace the relevant output to its estimate; compare table notes and manuscript interpretation with the code and results.
- Distinguish main specifications, diagnostics and robustness exercises.
- For each meaningful issue, explain its location, evidence, effect and suggested correction. Separate confirmed problems from methodological risks and missing material.
- Say what you did not run or could not inspect. A working script alone does not settle identification.

Deliver a short finding list in chat or Markdown. `templates/audit-scope.md` is optional. No fixed verdict, report format or administrative check is required.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Read the relevant method and inspect the affected sample, estimation, inference and output chain. Keep the requested audit scope; report an export error separately from an identification or covariance problem.
