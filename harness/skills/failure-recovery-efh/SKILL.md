---
name: failure-recovery-efh
description: Diagnose failed or interrupted tasks, choose bounded retries and resume from current checkpoints without duplicating effects or reporting stale success.
---

# Failure recovery

Inspect the failed attempt, error, current artifacts and affected dependencies before acting. Preserve useful work and logs.

| Failure | Response |
|---|---|
| Known transient service or resource error | Retry only the affected step, within an explicit attempt/time budget, if replay is safe. |
| Invalid input, missing dependency, bad schema or failing acceptance check | Repair or obtain the missing requirement; repeating the same action is not a remedy. |
| Process interruption | Check whether work is still running and whether effects occurred. Recover a checkpoint with that outcome recorded before re-dispatch. |
| Source/decision/output revision changed | Invalidate dependent work and rerun the affected branch. Preserve the earlier result as history. |
| External mutation with unknown outcome | Reconcile using a stable operation ID or read-only lookup. Do not automatically resubmit. |

Never treat a partial return, absent reviewer, stale file or exhausted retry budget as success. Propagate blocked dependencies while continuing independent work. A recovery changes execution status; it does not silently change the user's objective or a domain assumption.

For the local adapter, read [runtime recovery](../../orchestration/runtime.md#recovery). Its automatic retries require declared replay safety and matching exit codes; failed validation is not transient. Each code bug repaired needs a check that exposes the original failure.

For a native spawn with an absent receipt, use [native reconciliation](../../orchestration/native.md). Inspect the host's actual agent state before binding or resolving the request. A lost response is not proof that launch failed; a superseded worker still occupies capacity until its outcome is reconciled.
