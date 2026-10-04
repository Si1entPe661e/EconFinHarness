# Lightweight CLI

Use Python 3.8 or later. The included tools require only the standard library.

```bash
python3 harness_build/cli/fh.py skills list
python3 harness_build/cli/fh.py agents list
python3 harness_build/cli/fh.py workflows show empirical-analysis
python3 harness_build/cli/fh.py presets show panel-implement
python3 harness_build/cli/fh.py exemplars did --limit 3
python3 harness_build/cli/fh.py recipe aer_110_5_5 --specs
python3 harness_build/cli/fh.py status
```

These commands read included files without rebuilding research material.

`sync-adapters` copies source roles and skills into project host configuration. Use `--host claude` or `--host codex` to select a host, or `--output-dir <directory>` to inspect copies elsewhere.

`search` is a separate optional feature for an existing local corpus index. A fresh clone does not include that database; the command reports its absence and does not rebuild it. `fhb.py` is a compatibility entry for status and local index search.
