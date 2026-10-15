# Changelog

## Unreleased

- **Breaking:** keep `harness/` to guides only. The coordination runtime, its native host bridge and design notes, the maintainer checks, the role synchronization script and the general, native-project and War Discourse demonstrations move to local, undistributed folders. Published guides no longer point to them: orchestration, recovery, planning and dispatch guidance describe an existing project engine or versioned task, decision and evidence files, and the paper-first workflow and two-pass pricing reference no longer cite the example runner. A skill may still bundle a script or template that its own steps call.
- Add `econfinharness uninstall`: it removes only the host links and command the checkout installed, by host (`--tool`) or project (`--project`), and deletes the managed checkout only with `--remove-checkout` when it has no local changes or unpushed commits.
- **Breaking:** move the installer from `harness/maintenance/install.py` to the repository root (`install.py`, documented in `INSTALL.md`). Installations made earlier stop at `econfinharness update` without changing files; one update through the bootstrap (`curl -fsSL .../install.sh | bash -s -- update`) fast-forwards the checkout and retargets the command. A local structure check rejects runners, tests, runtimes, installers and demonstrations under `harness/`.
- Slim the skills from the first pilot: move every `checklist.md` (14), the research-record copies under `references/research-records.md` (8), five unlinked `references.md` lists and six unlinked templates to local maintenance material. Each affected skill points to `harness/paradigms/` for recorded practice instead; `did-efh`, `iv-efh` and `rdd-efh` keep the `references.md` DOI registers that the method recommendations cite, and linked templates stay.
- Slim `rdd-efh` to the shape of the other method skills: the 381-line R analysis template leaves the skill for local maintenance material, and `code-examples.md` adds R and Stata counts of observations, support points and clusters inside the bandwidth on each side. The observation counts reproduce rdrobust's effective sample sizes.
- Add a writing revise module (`harness/workflows/revise-writing.md`) as the final stage of manuscript, report, briefing and editing work: a defensive-writing check and fix, then a logic check and fix, then a fact comparison.
- Add `defensive-writing-check-efh`, which merges the MIT-licensed `anti-defensive-writing` skill with launch principles for presenting results (a paper as a product launch, not a progress report) under explicit integrity and genre limits.
- Add `logic-check-efh` for straw men, rebuttals of unmade claims, contradictions, incoherent progression, sycophancy, parroting, rhetorical symmetry, intensifiers, anthropomorphism, metaphor, idioms, jargon and filler.
- Add a standard-library revision comparison that lists changed numbers, units, citations and evidential wording (causal, certainty, significance, attribution), with negation handling and regression checks; add a `final-revision` capability route, a native budget check for every route and a reusable prompt.
- Add a pipeline review before delivery (`harness/workflows/pipeline-review.md`). A check-only `pipeline-reviewer` role and the `pipeline-review-efh` skill keep checks at consequential data boundaries. They find comparison with published values, variants and run machinery outside their own scripts, as well as silenced errors, fallback branches, typed numbers and missing boundary checks, and cite a line, a run-time count, a constructed case or a rerun for each finding. Counts of conditionals, assertions or print statements are never findings.
- Revise paper-first replication from a blind reproduction compared with its authors' code: collate every mention of a variable and rank ambiguities; start from the model terms the paper names; check what can silently change a number; assert only what the program relies on; compare published values in one program with one rule and say what a match establishes; check each variant's code against its declared rule; keep the delivered pipeline to building, estimating and exporting, with one guard against stale results and no tests of its own run machinery; limit negative examples to hand-written numerical routines; mark specification entries written after the first fit as post-result.
- Add variable construction from several measurements or informants (reporter rules, a logged search to identify a descriptive variable, and a units-or-scaling exception where the data identify the definition) to `panel-data-checks-efh`, with checks for values off a declared scale, missing sources in derived indicators, near-constant regressors and totals over copied values; add randomization strata, missing-covariate indicators and minimal heterogeneity terms to `rct-efh`; require a retained computation for negative or equivalence claims in `evidence-tracking-efh`; scope the implementer's bug-fix check to allow a retained inspection run in research pipelines.
- Add write-time rules for lean research code (`harness/skills/pipeline-review-efh/references/lean-code.md`): no existence branches, progress printing, handlers around data steps, redundant, published-value or package-algebra assertions, status files or self-tests; assert once where a relied-on property is created; one completion marker where the runtime hides failure. Linked from AGENTS.md, the implementer role, the analysis and replication workflows and the composition guide, with a structure check. In an unprompted analysis task, delivered scripts shrank from 192-302 to 113-115 lines with identical estimates.
- Add `pipeline-review` and `code-audit` capability routes; fitted-sample boundary counts, missing-value behavior and delivered checks for Stata, R, Python and MATLAB in the panel-check examples; hooks in the analysis, replication, audit, dispatch and composition guides; a reusable prompt; and structure checks. Generalize stored-code and scale examples in the panel checks.

## 0.5.0

- Rename all 39 skill IDs and directories with the `-efh` suffix to distinguish EconFinHarness skills from other projects.
- Update skill cross-references, capability routes, shared roles, examples and preservation-fixture paths while retaining research-record contents.
- Migrate installer-owned and verified legacy skill links to the namespaced IDs; preserve other projects' same-name skills and historical local records.
- Preserve custom skill kind, version and status fields under supported frontmatter metadata; validate every skill with the skill-creator validator.

## 0.4.1

- Add a terminal bootstrap and `econfinharness install`, `update` and `status` commands, with global installation by default and optional project setup.
- Reuse Git clone/fetch/fast-forward operations, preserve conflicting user files and configuration, and add offline installation/update regression checks.

## 0.4.0 - 2026-10-12

- Add focused project planning, status, report writing, briefing, editing, evidence and recovery skills, with synchronized Codex and Claude Code roles.
- Add general task routing and workflows while retaining empirical research as a specialized branch.
- Keep skill and role use installation-free; document the optional Python coordination runtime separately for durable task state, checked artifacts, bounded retries and native host handoffs.
- Add deterministic checks and authored general demonstrations, plus a native project delivery workflow that requires actual host agent returns.
- Move detailed research records into linked references, preserving their exact content and keeping entrypoints focused.
- Add paper-first replication guidance, a two-pass pricing reference and an independently written War Discourse example. Third-party data, source programs and PDFs remain external inputs.
- Distribute maintained sources, checks and examples; exclude local corpora, datasets, third-party snapshots, private configuration and generated outputs.

## 0.3.1 - 2026-10-03

- Replace host skill copies and Claude Code role copies with relative symlinks to shared files under `harness/`.
- Move Codex TOML role configurations into `harness/agents/codex/`, leaving only project settings at the root tool entry point.
- Distribute method guides, source skills and roles, and tool entry points without local CLI tools or standalone research records.

## 0.3.0 - 2026-10-03

- Move the public CLI to `tools/fh.py` and research examples to `examples/code-cards/` and `examples/paper-notes/`.
- Consolidate all 31 source skills and nine source roles under `harness/`.
- Keep existing method-summary exclusions under `examples/exclusions/`.
- Exclude the entire local build directory from the public tree and remove the legacy compatibility CLI from distribution.
- Allow optional corpus search to use an existing index selected with `--index`.

## 0.2.0 - 2026-10-03

- Provide 20 method skills and nine shared research skills, with estimation and export examples in R, Python, Stata and MATLAB where applicable.
- Connect method selection, sample checks, fixed effects, inference, result presentation and writing through a shared composition guide.
- Include 11 workflows, 12 reusable task prompts, nine roles and two reading skills.
- Retain 88 code cards, 91 paper-practice notes and existing method observations and recommendations.
- Provide English documentation and a quick start that works without the local corpus or search index.
- Distribute only reusable research material, lightweight tools and generated host configurations.
