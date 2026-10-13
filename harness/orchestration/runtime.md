# Optional local coordination adapter

Requires Python 3.9 or later, standard library only. Run the CLI from the repository root, or expose the repository on Python's module path. It uses `graphlib.TopologicalSorter` for DAG validation, SQLite transactions for checkpoints and native `subprocess` argument vectors for local commands. No shell-string evaluation, agent SDK, API key, package installation or provider configuration is required.

## Minimal task

Save a manifest in your workspace:

```json
{
  "version": 1,
  "goal": "Deliver a project capacity report",
  "tasks": [
    {"id": "measure", "kind": "command",
     "command": ["python3", "scripts/measure.py"],
     "inputs": ["inputs/workload.json", "scripts/measure.py"],
     "outputs": ["results/capacity.json"],
     "checks": [["python3", "scripts/check_capacity.py"]],
     "replay_safe": true,
     "retry": {"max_attempts": 2, "exit_codes": [75], "delay_seconds": 1}},
    {"id": "report", "kind": "agent", "capability": "report",
     "instruction": "Write a capacity report for the project lead; retain forecast uncertainty.",
     "needs": ["measure"], "inputs": ["results/capacity.json"],
     "outputs": ["report.html"]}
  ]
}
```

Include checker scripts as inputs too when they define completion criteria. Outputs are files, with distinct ownership; they must not overlap inputs or coordinator state. Paths are relative to the workspace and cannot escape via `..` or symlinks. This does not restrict what an arbitrary executed program can access; use the host sandbox and trusted task programs.

```bash
python3 -m harness.runtime --root /path/to/project --manifest task.json run
python3 -m harness.runtime --root /path/to/project --manifest task.json ready
python3 -m harness.runtime --root /path/to/project --manifest task.json packet report
```

`run` executes ready local commands and returns exit 2 while any required work remains incomplete, including ready agent tasks. It skips current successes. `packet` claims one agent task and emits its bounded context, role/skill paths, ownership, signature and token. The host executes it with a native agent tool or serially, then acknowledges the actual result:

```bash
python3 -m harness.runtime --root /path/to/project --manifest task.json complete report --token TOKEN_FROM_PACKET
python3 -m harness.runtime --root /path/to/project --manifest task.json status
python3 -m harness.runtime --root /path/to/project --manifest task.json evidence evidence.json
python3 -m harness.runtime --root /path/to/project --manifest task.json events
```

An attempt is not complete merely because the agent returned: outputs, unchanged inputs, matching token and declared checks must pass. Existing artifacts that were not regenerated need an explicit acceptance check; file existence alone is insufficient. The adapter does not judge report quality automatically. `evidence` reads an explicit claim record; relative record paths resolve inside the selected workspace, like the manifest. `status` keeps execution status separate from claim support/freshness.

State lives under workspace `.harness/`: a SQLite database and per-attempt logs. A configurable `--state-dir` can coexist with another project engine. Independent host dispatchers can claim different tasks; command execution in this adapter is serial. This is local coordination, not a distributed scheduler or a background daemon.

For authorized native agents, use the [native host bridge](native.md). It selects dependency-ready work, persists exact tool arguments before launch, binds actual host handles and validates terminal returns with the same completion checks. Selected role/skill revisions participate in an agent task's input signature. The [real project workflow](../examples/native-project/README.md) uses current repository files and actual checks rather than authored result fixtures.

## Recovery

Automatic retries are limited to 1–5 attempts and explicit nonzero exit codes or an opted-in timeout. They require `replay_safe: true` and local/read effects. Delay is bounded to 30 seconds. Input revisions are rechecked after the delay and when claiming the next attempt. Missing inputs, changed revisions, invalid output or failed checks do not retry automatically. Failure budgets persist across `run` invocations.

After an interruption or repair, inspect the logs, ensure the original worker has stopped and reconcile effects before recovery:

```bash
python3 -m harness.runtime --root /path/to/project --manifest task.json recover measure --reason "Worker stopped; corrected input schema; no external effects."
```

Recovery records the reason, invalidates the old token and starts a new explicit attempt budget. It does not kill a still-running process, undo effects or approve resubmission. External actions use host tools; the adapter refuses command tasks declared `effect: external`. Track an external operation's stable ID/outcome in the completion artifact and reconcile before retrying it through the host.

## Demonstrations and checks

```bash
python3 -B harness/examples/general/run_demo.py
python3 -B -m unittest discover -s harness/checks -p 'test_*.py'
python3 -B harness/maintenance/sync_roles.py --config
```

The demonstration covers project planning, operational reporting with transient failure, and document editing with a source revision. It uses small authored fixtures and serial role execution; it is not a benchmark of live multi-agent or LLM quality. The packet protocol is tested independently of a provider. Existing research examples continue to run with their domain-specific programs.
