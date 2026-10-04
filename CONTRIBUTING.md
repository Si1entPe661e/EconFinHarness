# Contributing

Keep changes focused on research skills, methods, examples and the lightweight tools that support them. Documentation, code, comments and reusable prompts are maintained in English.

Edit source skills and roles rather than generated host copies. After changing a source skill or role, run:

```bash
python3 tools/fh.py sync-adapters
```

Check changed commands or tools in an appropriate environment. Describe what was actually checked; do not claim that a syntax check reproduces a paper's estimates.

Use Conventional Commits:

```text
<type>(<optional scope>): <description>
```

Common types are `feat`, `fix`, `docs`, `refactor`, `test` and `chore`. Use a short imperative English description, such as `fix(cli): handle a missing local search index`. Add `!` after the type or scope when a change breaks existing usage.

The public tree includes `harness/`, `tools/`, `examples/`, generated host configurations and root documentation. `.gitignore` excludes the entire local `harness_build/` directory, corpus, environments, private configuration and build artifacts. Add new public paths deliberately; do not include raw research data or original third-party replication packages.
