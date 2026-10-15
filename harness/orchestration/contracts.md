# Task, artifact and evidence contracts

## Tasks and attempts

A task defines its output and checks before dispatch. Dependencies express readiness, while input paths express the source revision. Include local programs and configuration files among inputs when changes should trigger re-execution. Selected role/initial skill contents and route selection also participate in agent signatures. Runtime/environment versions can be captured in an input environment record.

| State | Meaning |
|---|---|
| `pending` | Not yet attempted, explicitly recovered, or invalidated by a revision |
| `running` | A command or native-agent handoff owns an attempt token |
| `succeeded` | Outputs were fingerprinted and declared checks passed for the captured inputs |
| `failed` | Execution failed or its bounded transient retry policy exhausted |
| `needs_attention` | Missing input, failed acceptance check, interruption or unresolved execution condition |

A task with unfinished dependencies is not ready. The project is execution-complete only when every required task succeeds. This says nothing by itself about semantic correctness or whether every claim is supported.

Each attempt retains its token, input/dependency signature, logs and outcome. An old worker cannot complete a new attempt, and a retry stops if recovery has transferred responsibility during its delay. A source, upstream revision or output hash change invalidates affected successful descendants. Prior attempts and evidence records remain in the append-only event history. Completion checks are read-only; changed inputs or outputs during checking invalidate completion.

## Evidence

An optional ledger entry contains:

```json
{
  "id": "capacity-claim",
  "claim": "The planned workload exceeds stated capacity.",
  "status": "verified",
  "task": "capacity-check",
  "verification": "Compared totals and units in the cited fields; scope is arithmetic, not forecast validity.",
  "sources": [{"path": "results/capacity.json", "locator": "planned_hours and available_hours"}]
}
```

Status vocabulary: `reported`, `verified`, `inferred`, `conflicting`, `open`. Verification needs its actual scope; a producer's claim of success is insufficient. Source pointers have a file and line/page/field/section locator. Fingerprint file sources and the producing task revision when freshness matters; support judgments are attested, not inferred by a hash. A web source should be cited with URL/version/access date in the document and, when permitted, a small local source note for a checkable ledger pointer.

Freshness is separate from support: `current` means local source hashes and the producing task revision still agree; `stale` means they do not or cannot be checked. A current inference remains an inference. Open evidence has no support implied. A finished investigation may correctly conclude that evidence is conflicting.

Decision records can be ordinary versioned files: question, selected choice, rationale, source pointers and affected work. Include them as task inputs to make decision changes invalidate downstream artifacts. Keep the user's existing issue tracker or project document authoritative.

## Scope of enforcement

Checks of graph structure, path containment, output ownership, dispatch context, retry policy, fingerprints and declared acceptance criteria neither sandbox arbitrary programs nor prevent an agent from opening unrelated files. Host permissions, user instructions and domain judgment still apply. A file hash is change detection, not a backup or proof of truth; preserve needed versions in the project's existing version-control/storage system.
