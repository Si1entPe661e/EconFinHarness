# Research examples

| Path | Contents |
|---|---|
| `code-cards/` | 88 code cards describing recorded research implementations |
| `paper-notes/` | 91 notes describing research practices reported in paper text |
| `exclusions/` | Existing paper exclusion lists used to interpret method-summary denominators |

Cards describe source-code implementation; notes describe authors' statements. Keep these distinct from methodological recommendations in `harness/paradigms/`. DOI/artid identifiers and line/page pointers locate the original sources.

The JSON records retain existing research content. Input hashes and historical local text pointers describe the original readings; original replication files, full paper text and build records are not distributed.

Read these files directly or use the [CLI](../tools/README.md):

```bash
python3 tools/fh.py exemplars did --limit 3
python3 tools/fh.py recipe aer_110_5_5 --specs
```

The reading roles and skills are maintained under `harness/agents/` and `harness/skills/`. See the [main quick start](../README.md).
