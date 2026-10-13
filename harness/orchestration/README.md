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
| Write an academic manuscript | `academic-writing-efh` | Academic writer |
| Trace consequential claims | `evidence-tracking-efh` | Producer or scoped evidence reviewer |
| Recover failed or interrupted work | `failure-recovery-efh` | Current executor or orchestrator |
| Design or implement empirical analysis | [Research composition](../skill-composition.md) | Analyst / implementer; select the applicable method |

The [route catalog](routes.json) maps explicit capabilities to roles and initial skills. It is a dispatch aid, not a keyword classifier or an automatic permission grant. Roles are responsibilities; one agent may perform several serially.

Four objects connect the work:

1. **Task:** purpose, inputs, dependencies, owner, outputs, acceptance checks and replay policy.
2. **Attempt:** actual execution or handoff, input revision, logs, outcome and failure reason.
3. **Artifact:** a versioned source, decision, result, code file or document with a locator.
4. **Evidence:** a claim linked to artifacts, its support judgment and verification scope. Work completion and claim validity remain distinct.

Read [dispatch](dispatch.md) for decomposition and context, [contracts](contracts.md) for state and evidence, [runtime](runtime.md) for local commands/checkpoints, or [native dispatch](native.md) for the host tool bridge. Load only the part needed. [Reuse notes](reuse-notes.md) distinguish inspected external patterns from mechanisms tested here.

The runtime uses Python's `graphlib`, `sqlite3`, `subprocess` and hashing primitives. It resumes local command DAGs, selects dependency-ready native dispatches, bounds context and verifies observed host returns. An active host orchestrator makes the actual native tool calls; it is not a distributed workflow service or an LLM backend. If a project already uses Snakemake, Prefect, targets, Make or another engine, run that engine as a task and record its outputs rather than translating its graph into another system.
