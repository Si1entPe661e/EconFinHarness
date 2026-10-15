# General task coordination

EconFinHarness combines a general coordination layer with focused capabilities. Research methods, project management, writing and software tasks use the same dependency, evidence and recovery concepts. Paper reproduction is one application.

Start with the requested outcome and completion criteria. A single edit or explanation can proceed directly. Use durable state when a task spans dependencies, collaborators, sessions or failures; keep an existing project engine authoritative.

| Need | Load initially | Responsibility |
|---|---|---|
| Coordinate a compound task | `task-orchestration-efh` | Orchestrator: dependency graph, bounded dispatch, integration |
| Define scope, milestones and ownership | `project-planning-efh` | Project planner |
| Inspect progress, risks and handoff | `project-status-efh` | Project manager |
| Write a full analytical/technical/project report | `report-writing-efh` | Report writer |
| Prepare a decision memo, status briefing or slide narrative | `briefing-writing-efh` | Briefing writer |
| Revise supplied prose | `document-editing-efh` | Editor |
| Check and fix defensive writing and argument logic ([revise module](../workflows/revise-writing.md)) | `defensive-writing-check-efh`, then `logic-check-efh` | Drafting writer inline, or editor via `final-revision` |
| Write an academic manuscript | `academic-writing-efh` | Academic writer |
| Trace consequential claims | `evidence-tracking-efh` | Producer or scoped evidence reviewer |
| Recover failed or interrupted work | `failure-recovery-efh` | Current executor or orchestrator |
| Design or implement empirical analysis | [Research composition](../skill-composition.md) | Analyst / implementer; select the applicable method |
| Check research code for a requested scope or concrete issue ([code audit](../workflows/audit-code.md)) | `code-audit-efh` | Implementer, or reviewer via `code-audit` |
| Review a multi-script research pipeline before delivery ([pipeline review](../workflows/pipeline-review.md)) | `pipeline-review-efh` | Implementer inline, or pipeline reviewer via `pipeline-review` |

Report, briefing, editing and manuscript work ends with the [revise module](../workflows/revise-writing.md) unless its skip conditions apply. Analysis and replication pipelines of several scripts end with the [pipeline review](../workflows/pipeline-review.md) under the same rule.

The [route catalog](routes.json) maps explicit capabilities to roles and initial skills. It is a dispatch aid, not a keyword classifier or an automatic permission grant. Roles are responsibilities; one agent may perform several serially.

Four objects connect the work:

1. **Task:** purpose, inputs, dependencies, owner, outputs, acceptance checks and replay policy.
2. **Attempt:** actual execution or handoff, input revision, logs, outcome and failure reason.
3. **Artifact:** a versioned source, decision, result, code file or document with a locator.
4. **Evidence:** a claim linked to artifacts, its support judgment and verification scope. Work completion and claim validity remain distinct.

Read [dispatch](dispatch.md) for decomposition and context or [contracts](contracts.md) for state and evidence. Load only the part needed.

If a project already uses Snakemake, Prefect, targets, Make or another engine, run that engine as a task and record its outputs rather than translating its graph into another system. Otherwise ordinary versioned files can hold durable state: a task list with dependencies and owners, a decision log and an evidence ledger.
