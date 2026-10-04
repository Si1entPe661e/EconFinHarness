# Code annotation references

Repository guidance is in `AGENTS.md`, `harness/skill-composition.md` and `harness/workflows/annotate-code.md`. Comments should explain research meaning while preserving executable behavior. Use a derived copy, patch or sidecar for original corpus code.

The language references below are unverified here. Consult the documentation for the version in use when a proposed comment may affect parsing or runtime behavior.

| Language | Relevant rules |
|---|---|
| Stata | Comments, line continuation and `#delimit`: `*`, `//`, `///`, `/* */` |
| R | Comments, expressions and pipe chains |
| Python | Comments, docstrings, `__doc__` and doctest |
| MATLAB | `%`, `%%`, `%{ %}` and `...` |
| Julia | `#`, `#= =#` and docstrings |
| SAS | Statement comments ending at `;` and `/* */` |
