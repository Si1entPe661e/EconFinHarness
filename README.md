# EconFinHarness

General task coordination, project management and evidence-based writing, with specialized empirical research capabilities for finance, economics, management, operations research and statistics.

Start from the outcome: plan a project, coordinate dependent work, write a report or briefing, revise a document, or perform an empirical analysis. Focused skills and roles load on demand. Research methods and paper reproduction are applications of these general concepts.

## Quick start

Install skills globally from the terminal (macOS, Linux or WSL; Git and Python 3.9+ required):

```bash
curl -fsSL https://raw.githubusercontent.com/Si1entPe661e/EconFinHarness/main/install.sh | bash -s -- install
export PATH="$HOME/.local/bin:$PATH"
econfinharness status
```

The default installation serves Codex and Claude Code across projects. Update with `econfinharness update`; use `--tool codex` or `--tool claude` to select one host. Existing skills and configurations are preserved; `--skip-existing` keeps conflicting entries and reports them. See [installation options and project setup](harness/maintenance/README.md) for a download-then-run command, custom paths and project-scoped roles.

Alternatively, clone the repository and use its project configuration directly:

```bash
git clone https://github.com/Si1entPe661e/EconFinHarness.git
cd EconFinHarness
```

Open your working project in Codex or Claude Code; after a direct clone, open this repository as the project root to use its role configurations. In Codex, trust the project when prompted so its role settings can load. Open a new session after installing skills. No analysis package installation or local runtime startup is required to use the guides. Start with a concrete request and the location of your inputs, for example:

> Inspect this project's actual files and progress. Prepare a delivery plan with dependencies, owners and acceptance criteria, then implement the authorized next steps. Keep verified completion separate from planned work.

For general tasks, start with [orchestration](harness/orchestration/README.md); the [research composition guide](harness/skill-composition.md) is the empirical-analysis branch. A single agent can execute serially. Native-agent delegation uses bounded context and output ownership when useful and authorized.

Other starting requests:

> Read AGENTS.md and harness/skill-composition.md. Analyze my company panel in data/panel.csv using firm_id and year as the panel keys, y as the outcome and x as the main regressor. Use firm and year fixed effects, choose inference from the research design, inspect the fitted sample, and export a regression table with a concise interpretation. Prefer R.

> Write a technical report for the project lead from the supplied logs and results, then prepare a one-page decision briefing. Trace material claims, preserve uncertainties and flag evidence gaps.

Replace the example paths and variable names with your own. Empirical analyses require your data, the selected R, Python, Stata or MATLAB environment, and relevant packages. Local paper collections and search databases are optional and are not included in a clone.

## Find the right material

| Task | Entry point |
|---|---|
| Install globally, set up a project or update | [Terminal installer](harness/maintenance/README.md) |
| Coordinate tasks, evidence and recovery | [General orchestration](harness/orchestration/README.md) |
| Plan or maintain a project | [Project management](harness/workflows/project-management.md) |
| Write reports, briefings or revisions | [Reports](harness/workflows/write-report.md), [briefings](harness/workflows/prepare-briefing.md), [editing](harness/workflows/edit-document.md) |
| Choose and combine research skills | [Skill composition](harness/skill-composition.md) |
| Implement an empirical analysis | [Analysis workflow](harness/workflows/empirical-analysis.md) |
| Export tables and scientific figures | [Presentation workflow](harness/workflows/present-results.md) |
| Read estimation commands | [Skills and methods](harness/README.md) |
| Study summaries of recorded research practice | [Method materials](harness/paradigms/README.md) |
| Start from a reusable task prompt | [Task prompts](harness/presets/README.md) |
| Independently reproduce a paper without reading author code | [Paper-first workflow](harness/workflows/paper-first-replication.md) and [War Discourse example](harness/examples/war-discourse/README.md) |

## Optional advanced workflows

The [local coordination adapter](harness/orchestration/runtime.md) records task dependencies, checkpoints, source revisions, execution attempts and evidence for work that needs durable recovery. It requires Python 3.9+ and its standard library. It runs on demand, calls no model itself, and can wrap an existing project workflow engine. Ordinary skill and role use does not require it.

The [general demonstrations](harness/examples/general/README.md) exercise these contracts with authored fixtures. The [native host bridge](harness/orchestration/native.md) and [real project workflow](harness/examples/native-project/README.md) additionally require an active host agent to dispatch authorized native agents and observe their returns. Python alone does not launch those agents.

Maintainers can run the [implementation checks](harness/checks/README.md) from a fresh clone without local research data or corpus files.

## Repository content and tool entry points

| Directory | Purpose |
|---|---|
| `harness/` | Focused skills/roles, methods, workflows, checks, task prompts and optional coordination runtime |
| `.agents/skills` | Relative symlink to `harness/skills/` for Codex discovery |
| `.claude/skills` | Relative symlink to the same skills |
| `.claude/agents` | Relative symlink to `harness/agents/` for Claude Code roles |
| `.codex/config.toml` | Codex project settings pointing to `harness/agents/codex/` |

Edit skills under `harness/skills/` and role descriptions under `harness/agents/`. Both tools read the shared files through their entry points, so skill and Markdown role edits need no copying. Codex uses TOML role configurations under `harness/agents/codex/`; keep their instructions consistent with the corresponding Markdown roles.

Use a Git clone with symlink support; the tool entry points are relative links within the repository.

## Distribution

The public repository contains focused skills and roles, workflows, checks, authored demonstrations, method guides, existing summaries of recorded research practice and the optional coordination adapter. Code observations, paper statements and methodological recommendations have different evidentiary roles; practice frequencies do not establish validity. Execution success, artifact freshness and claim support are recorded separately.

Workstation-only collection/build tools, standalone code cards and paper notes, the full article catalog, original replication source trees, research datasets, paper PDFs, extracted full text, search databases and generated run outputs are not distributed. Historical input pointers in method summaries describe their original source records. References to `Paper/<Journal>/articles/<artid>/` identify original source locations rather than files bundled here. Use the recorded DOI or repository link to locate the original publication or code under its own access and license terms.

Version: [harness/VERSION](harness/VERSION). License: [LICENSE](LICENSE).
