# EconFinHarness

Research skills and method guides for finance, economics, management, operations research and statistics.

Use the harness with your own data or research code to design an analysis, implement an estimator, choose inference, present results or explain existing work. It includes 20 method skills, nine shared research skills, two reading skills, nine roles, 11 workflows and 12 task prompts.

## Quick start

```bash
git clone https://github.com/Si1entPe661e/EconFinHarness.git
cd EconFinHarness
```

Open this directory as the project root in your AI coding tool. The repository includes skill and role configurations for Codex and Claude Code. Start with a concrete request and the location of your data or code, for example:

> Read AGENTS.md and harness/skill-composition.md. Analyze my company panel in data/panel.csv using firm_id and year as the panel keys, y as the outcome and x as the main regressor. Use firm and year fixed effects, choose inference from the research design, inspect the fitted sample, and export a regression table with a concise interpretation. Prefer R.

Replace the example path and variable names with your own. The [composition guide](harness/skill-composition.md) connects method choice, sample checks, fixed effects, inference and result presentation. A single agent can carry out the relevant steps.

Reading the guides requires no software installation. Running an analysis requires the selected R, Python, Stata or MATLAB environment and the packages used by that analysis.

## Find the right material

| Task | Entry point |
|---|---|
| Choose and combine research skills | [Skill composition](harness/skill-composition.md) |
| Implement an empirical analysis | [Analysis workflow](harness/workflows/empirical-analysis.md) |
| Export tables and scientific figures | [Presentation workflow](harness/workflows/present-results.md) |
| Read estimation commands | [Skills and methods](harness/README.md) |
| Study summaries of recorded research practice | [Method materials](harness/paradigms/README.md) |
| Start from a reusable task prompt | [Task prompts](harness/presets/README.md) |

## Source guides and host configurations

| Directory | Purpose |
|---|---|
| `harness/` | Canonical skills, roles, methods, workflows and task prompts |
| `.agents/skills/` | Skill copies for Codex |
| `.claude/` | Skill copies and Claude Code role configurations |
| `.codex/` | Codex role configurations and project settings |

Skill copies carry the same research guidance as `harness/skills/`. Role configurations derive from `harness/agents/` and use the format expected by each host. Maintain the source guides under `harness/` and keep the included host copies consistent.

## Distribution

The public repository contains method guides, operational skills, role configurations, workflows, task prompts and existing summaries of recorded research practice. Code observations, paper statements and methodological recommendations have different evidentiary roles; practice frequencies do not establish validity.

Local CLI tools, standalone code cards and paper notes, the full article catalog, original replication source trees, paper PDFs, extracted full text and search databases are not distributed. Historical input pointers in method summaries describe their original source records. References to `Paper/<Journal>/articles/<artid>/` identify original source locations rather than files bundled here. Use the recorded DOI or repository link to locate the original publication or code under its own access and license terms.

Version: [harness/VERSION](harness/VERSION). License: [LICENSE](LICENSE).
