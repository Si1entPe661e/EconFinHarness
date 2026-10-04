# Repository guidance

EconFinHarness provides empirical research skills, method guides and selected research-practice records. Work from the research question and available files. Use only the relevant methods and keep ordinary tasks direct.

## Research work

- For compound tasks, read `harness/skill-composition.md`. Select the main method before combining sample checks, estimation, inference and presentation.
- Keep the estimand, variable timing, weights, fixed effects, fitted sample and inference consistent across code, tables, figures and prose. Determine fixed effects and clustering separately.
- Use actual model objects and numerical outputs. State missing information and distinguish static code reading, synthetic demonstrations and reproduction with original data.
- Keep code observations, paper statements and methodological recommendations distinct. Cite papers by DOI or artid and retain relevant source lines or page pointers.
- Use existing cards, notes and method summaries. New extraction, corpus collection or rebuilding belongs to an explicitly scoped task.
- Roles describe responsibilities. One agent may perform several roles; reviews and delegation should serve a concrete need.

## Repository layout

- `harness/`: source skills, roles, composition guidance, methods, workflows and task prompts, including the reading skills and roles.
- `tools/`: the lightweight CLI for reading materials and synchronizing host configurations.
- `examples/`: code cards, paper-practice notes and the existing exclusion lists used by method summaries.
- `.agents/`, `.claude/`, `.codex/`: host configurations generated from source roles and skills. Refresh them with `python3 tools/fh.py sync-adapters` after source changes.
- `Paper/`, when available locally: an optional research corpus excluded from public version control. A fresh clone does not include it.
- `harness_build/`, when present locally: historical construction materials excluded from public version control and not required by the public tools.

## Editing and access

Maintain repository documentation, code, comments and reusable prompts in English. Keep changes focused and preserve existing research material. Use repository-relative paths in maintained files and Conventional Commits for commit messages.

Do not modify audited local corpus metadata or databases during ordinary research tasks. Do not collect datasets, full replication archives or paper PDFs into this repository. Respect source licenses and access restrictions. Original third-party code remains separate from the public harness.

Use the runtime actually available in the current environment. Stata examples require Stata; do not assume a local installation. Do not execute financial transactions or use the research corpus as an investment tool.
