---
name: task-orchestration-efh
description: Coordinate compound tasks across capabilities, dependencies and sessions; dispatch bounded context and verify handoffs. Use for substantial multi-step work, not a routine single edit.
---

# Task orchestration

Start from the requested outcome, inputs, constraints and completion criteria. Domain methods are capabilities inside a task, not the definition of the harness.

- Complete small tasks directly. For compound or resumable work, identify deliverables, dependency edges, owners and concrete completion checks. Use the existing project engine when present.
- Separate planning, production and verification responsibilities only when they improve the work. One agent may perform them serially. Use native delegation only when available and authorized.
- Dispatch one bounded responsibility with relevant paths, input revisions, allowed outputs, acceptance checks and unresolved choices. Do not send the entire conversation or preload every skill. Start with at most three applicable skills; references load when their branch becomes relevant.
- Parallelize independent tasks with distinct ownership. Join their results by task ID and input revision; an early return is progress, not a completed combined result. Resolve substantive conflicts before integrating.
- Verify actual artifacts and check outcomes before marking completion. Preserve failed attempts and open claims. Revisit affected descendants when sources, decisions or outputs change.

Read only the relevant detail:

- [Dispatch and context](../../orchestration/dispatch.md): task decomposition, context bounds, fan-out and handoffs.
- [Task and evidence contracts](../../orchestration/contracts.md): durable state and completion semantics.
- `failure-recovery-efh`: an actual failed or interrupted task.

Deliver the requested work plus its material unresolved items. Coordination files support execution; they do not replace it.
