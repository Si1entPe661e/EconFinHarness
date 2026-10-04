# Lightweight CLI

Use Python 3.8 or later. The included tools require only the standard library and work without build scripts.

```bash
python3 tools/fh.py skills list
python3 tools/fh.py agents list
python3 tools/fh.py workflows show empirical-analysis
python3 tools/fh.py presets show panel-implement
python3 tools/fh.py exemplars did --limit 3
python3 tools/fh.py recipe aer_110_5_5 --specs
python3 tools/fh.py status
```

These commands read source guides under `harness/` and research material under `examples/` without rebuilding them.

`sync-adapters` copies source roles and skills into project host configuration. Use `--host claude` or `--host codex` to select a host, or `--output-dir <directory>` to inspect copies elsewhere.

```bash
python3 tools/fh.py sync-adapters
```

`search` is optional and requires an existing local corpus index. Supply its location with `--index <path>`; the default is `local/fh_index.sqlite`. A fresh clone does not include that database. A missing index is reported without creating or rebuilding one.
