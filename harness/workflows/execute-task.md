# Execute a general compound task

Use [general orchestration](../orchestration/README.md) to define the requested outcome, deliverables and completion checks. Keep simple work direct; for resumable work, use the existing project engine or the [local adapter](../orchestration/runtime.md).

Choose only the capabilities needed, declare dependencies and output ownership, execute ready work, verify actual artifacts and integrate the results. Native-agent dispatch uses bounded context and matching input revisions; one executor may work serially. Record material evidence and decisions, then revisit affected descendants after a change. Apply `failure-recovery` to actual failures with a classified, bounded policy.

Deliver the requested result, checks actually performed and unresolved items. Do not equate execution success with substantive verification.

For authorized native delegation, follow [the native host bridge](../orchestration/native.md). Let it select ready tasks, forward its exact host calls, bind actual returned handles and settle terminal receipts. Keep input sources immutable during a wave; a changed decision or artifact invalidates the affected branch.
