# General coordination demonstrations

Run from the repository root:

```bash
python3 -B harness/examples/general/run_demo.py
```

Python 3.9+ and its standard library are sufficient. Outputs are local under `outputs/general-harness-demo/`; `--output /path/to/workspace` selects another location. Rerunning retains completed tasks and attempt history, and refreshes revised writing work.

The transient fault is injected once per workspace. Changing the Python executable or rebuilding a missing output starts a new task revision, whose attempt count can be one. The demo verifies the original failure, retry and completion from the retained event history.

Three small authored fixture projects exercise the same runtime:

- Project management: inspect deliverables, then dispatch and validate a plan with ownership, blocked work and acceptance criteria.
- Operational reporting: inject a declared exit-75 transient failure, retry once, retain arithmetic evidence, then validate a report and a concise briefing.
- Document editing: preserve factual qualifications, revise the source, invalidate the prior draft and evidence, then complete the new revision.

Agent packets are generated and completed with the same token/check protocol used for native-agent handoffs. Production is executed serially by this demonstration script. This is a test of coordination contracts and authored fixtures, not an LLM quality evaluation or a claim that live subagents were spawned. Existing research examples remain separate applications.
