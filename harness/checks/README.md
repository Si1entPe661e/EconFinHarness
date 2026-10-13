# Checks

Run from the repository root:

```bash
python3 -B -m unittest discover -s harness/checks -p 'test_*.py'
python3 -B harness/checks/check_paper_first.py
python3 -B harness/maintenance/sync_roles.py --config
python3 -B harness/examples/native-project/check_helpers.py
python3 -B harness/examples/war-discourse/check_runner.py
```

These checks require Python 3.9+ and its standard library and can run from a fresh clone. The War Discourse runner checks inject failures without loading research data or requiring R; the empirical R analysis has separate package and local-input requirements documented in that example.

Installer checks use actual local Git repositories, isolated user roots and file-URL downloads. They cover global/project setup, installed command execution, fast-forward updates, host collisions, skipped entries, ignored local files, local changes/commits, failed network operations and concurrent mutations. They never write into the real user installation or require network access.

Namespace checks require every published skill directory and declared name to use the `-efh` suffix, keep role/route references loadable and validate maintained documentation links. Installer migration checks distinguish owned legacy links from other projects' same-name files or links and preserve historical records under retired source directories.

The runtime checks inject actual transient/permanent failures, missing/stale artifacts, source changes during checking, duplicate dispatch, invalid tokens, evidence revision changes and unsafe retry declarations. Structure checks validate routes, links, entrypoint bounds, unchanged migrated research records, role/configuration synchronization and resumable demonstrations. These are deterministic implementation checks, not a benchmark of an LLM's domain judgment.

Native adapter checks cover durable dispatch, authorization before execution, dependency/capacity selection, fresh contexts, observed-handle binding, explicit unknown-outcome resolution, strict terminal receipts, source budgets and concurrent acceptance. CLI integration uses explicitly simulated handles. Live transport and writing judgment are exercised separately by the [real project workflow](../examples/native-project/README.md); no unit-test handle counts as a live agent.

The 750-word skill-entrypoint and 400-word role-body bounds are this repository's maintenance budgets. They do not measure provider token limits or all files an agent later opens. Do not delete essential constraints just to meet them; move conditional detail into reachable references.

`fixtures/research_record_hashes.json` records the exact bytes moved out of skill entrypoints during the progressive-loading refactor. It is a migration-preservation fixture, not audited corpus metadata. An intentional later record update must update its fixture in the same reviewed change.

The optional skill-creator validator requires PyYAML and can run in a separate validation environment. Repository checks cover the used frontmatter form, identity, links, dispatch and entrypoint size; they do not claim to implement a complete YAML validator. Runtime manifests/catalogs are JSON and have no YAML dependency.
