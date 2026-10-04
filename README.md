# EconFinHarness

Research skills and method guides for finance, economics, management, operations research and statistics.

Use the harness with your own data or research code to design an analysis, implement an estimator, choose inference, present results or explain existing work. It includes 20 method skills, nine shared research skills, two reading skills, nine roles, 11 workflows, 12 task prompts, 88 code cards and 91 paper-practice notes.

## Quick start

```bash
git clone https://github.com/Si1entPe661e/EconFinHarness.git
cd EconFinHarness
```

Open this directory as the project root in your AI coding tool. The repository includes skill and role configurations for Codex and Claude Code. Start with a concrete request and the location of your data or code, for example:

> Read AGENTS.md and harness/skill-composition.md. Analyze my company panel in data/panel.csv using firm_id and year as the panel keys, y as the outcome and x as the main regressor. Use firm and year fixed effects, choose inference from the research design, inspect the fitted sample, and export a regression table with a concise interpretation. Prefer R.

Replace the example path and variable names with your own. The [composition guide](harness/skill-composition.md) connects method choice, sample checks, fixed effects, inference and result presentation. A single agent can carry out the relevant steps.

Reading the guides requires no software installation. The small CLI uses Python 3.8 or later and the standard library. Running an analysis requires the chosen R, Python, Stata or MATLAB environment and the packages used by that analysis; there is no need to install every package shown in the examples.

## Find the right material

| Task | Entry point |
|---|---|
| Choose and combine research skills | [Skill composition](harness/skill-composition.md) |
| Implement an empirical analysis | [Analysis workflow](harness/workflows/empirical-analysis.md) |
| Export tables and scientific figures | [Presentation workflow](harness/workflows/present-results.md) |
| Read estimation commands | [Skills and methods](harness/README.md) |
| Study recorded research practice | [Method materials](harness/paradigms/README.md), `examples/code-cards/`, `examples/paper-notes/` |
| Start from a reusable task prompt | [Task prompts](harness/presets/README.md) |

Optional CLI commands work with the material included in a fresh clone:

```bash
python3 tools/fh.py skills list
python3 tools/fh.py workflows show empirical-analysis
python3 tools/fh.py exemplars did --limit 3
python3 tools/fh.py status
```

All source roles and skills are under `harness/agents/` and `harness/skills/`. To refresh the included host copies:

```bash
python3 tools/fh.py sync-adapters
```

## Included material and local corpus

The public repository contains method guides, operational skills, role configurations, workflows, task prompts and selected research notes. Code cards describe recorded implementations; paper notes describe authors' reported practices. Frequencies of observed practice do not establish methodological validity.

The full article catalog, original replication source trees, paper PDFs, extracted full text and local search databases are not distributed. References to `Paper/<Journal>/articles/<artid>/` identify the original source location; those files are not present in a fresh clone. Use the recorded DOI or repository link to locate the original publication or code under its own access and license terms.

The `search` command is optional and requires an existing local SQLite index supplied with `--index <path>`, or placed at `local/fh_index.sqlite`. It is not part of the fresh-clone quick start. Skills, cards and notes remain usable without that index or the full corpus.

Version: [harness/VERSION](harness/VERSION). Contributions: [CONTRIBUTING.md](CONTRIBUTING.md). License and third-party attribution: [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
