# Repository guidance

EconFinHarness coordinates general project work, evidence-based writing and empirical research. Work from the requested outcome and available files. Use only relevant capabilities and keep ordinary tasks direct.

## Task execution and research

- For compound tasks, start with `harness/orchestration/README.md`. Select the relevant capability and load detail progressively. Research analyses then use `harness/skill-composition.md` to connect the main method, sample, inference and presentation.
- Keep task dependencies, ownership, source revisions, actual check results and unresolved claims visible when they matter. Use the existing project engine, or versioned task and evidence files, for resumable work. A completion artifact is not proof that a substantive claim is true.
- Dispatch bounded responsibilities with relevant paths and acceptance checks. Avoid full-history handoffs and loading every skill. One agent may execute serially; delegation should serve a concrete dependency, capacity or verification need.
- Retry only classified, replay-safe work within a stated budget. Reconcile unknown external effects before resubmitting; preserve failed attempts and invalidate affected downstream work when sources change.
- Keep the estimand, variable timing, weights, fixed effects, fitted sample and inference consistent across code, tables, figures and prose. Determine fixed effects and clustering separately.
- Write research code lean (`harness/skills/pipeline-review-efh/references/lean-code.md`): let errors stop the run and assert only properties later code relies on (keys, merges, sample rule, value domains, missing values). Delivered scripts carry no existence branches, progress printing, handlers around data steps, re-verification of package results, status files or self-tests.
- Use actual model objects and numerical outputs. State missing information and distinguish static code reading, synthetic demonstrations and reproduction with original data.
- Keep code observations, paper statements and methodological recommendations distinct. Cite papers by DOI or artid and retain relevant source lines or page pointers.
- Use the included method summaries and any research records available locally. New extraction, corpus collection or rebuilding belongs to an explicitly scoped task.
- Roles describe responsibilities. One agent may perform several roles; reviews and delegation should serve a concrete need.

## Repository layout

- `harness/`: source skills, roles, composition guidance, methods, workflows and task prompts, including the reading skills and roles. It holds guides only: keep runners, tests, runtimes, installers and demonstrations out of it. A skill may bundle a small script or template that its own steps call.
- `install.sh` and `install.py`: the terminal installer described in `INSTALL.md`.
- `.agents/skills`: a relative symlink to `harness/skills/` for Codex discovery.
- `.claude/skills` and `.claude/agents`: relative symlinks to the shared skills and Markdown roles under `harness/`.
- `.codex/config.toml`: Codex project settings referring to TOML roles under `harness/agents/codex/`.
- `Paper/`, when available locally: an optional research corpus excluded from public version control. A fresh clone does not include it.
- Local tools, maintainer checks, demonstrations, standalone research records and construction materials are excluded from public version control. They are not prerequisites for using the guides.

## Editing and access

Maintain repository documentation, code, comments and reusable prompts in English. Keep changes focused and preserve existing research material. Use repository-relative paths in maintained files and Conventional Commits for commit messages.

For each code bug fixed, add a targeted check that exposes the failure and verifies the repair; in research analysis scripts a retained inspection run can serve as that check. Prefer applicable mature packages, projects or existing solutions over reimplementing them.

Edit the shared skills and Markdown roles under `harness/`; preserve the root symlinks. Keep each Codex TOML role consistent with its corresponding Markdown role.

Do not modify audited local corpus metadata or databases during ordinary research tasks. Do not collect datasets, full replication archives or paper PDFs into this repository. Respect source licenses and access restrictions. Original third-party code remains separate from the public harness.

Use the runtime actually available in the current environment. Stata examples require Stata; do not assume a local installation. Do not execute financial transactions or use the research corpus as an investment tool.
