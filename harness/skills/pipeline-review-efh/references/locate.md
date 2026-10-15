# Locate candidates

Search, then read each hit in context: a hit is a candidate, not a finding. Read whole commands, because a guard often sits on a continuation line (Stata `///`, an open bracket in R, Python or MATLAB). Ignore matches inside comments, and inside strings except for typed numbers. Exclude inspection folders and bundled third-party code. Search for the file of published values by its name; do not open it.

| Look for | Stata | R | Python | MATLAB |
|---|---|---|---|---|
| Reads of published values | `use`, `import delimited` or `merge` naming the file | `read.csv`, `readr::read_csv` or `jsonlite::fromJSON` naming the file | `pd.read_csv` or `json.load` naming the file | `readtable` or `jsondecode` naming the file |
| Assertions and key checks | `assert`, `isid`, `confirm`, `merge ..., assert()` | `stopifnot`, joins with `relationship =` or `unmatched =` | `assert`, `merge(..., validate=)` | `assert`, `validateattributes`, `mustBe*` |
| Handlers and forced options | `capture`, `cap`, `force` | `try(`, `tryCatch(`, `suppressWarnings(`, `options(warn = -1)` | `except`, `errors="coerce"` or `"ignore"`, `warnings.filterwarnings` | `try`/`catch`, `warning('off'` |
| Existence branches | `confirm file`, `confirm variable`, `_rc` | `file.exists(`, `exists(`, `%in% names(` | `os.path.exists`, `hasattr(`, `in df.columns` | `exist(`, `isfile(`, `isfield(` |
| Deletion | `erase`, `rmdir`, `shell rm` | `unlink(`, `file.remove(` | `os.remove`, `shutil.rmtree`, `Path.unlink` | `delete(` of a file, `rmdir` |
| Numbers typed into exhibits | `text()`, `note()`, `title()` or `addtext()` with a literal decimal or N | `annotate(`, `labs(` or `geom_text(` with a literal decimal | `ax.text(`, `ax.annotate(` or `set_title(` with a literal decimal | `text(` or `title(` with a literal decimal |
| Totals by group | `egen total()` or `collapse (sum)` after a `bysort g: egen` copy | `group_by()` then `summarise(sum())` | `groupby().sum()`, `transform("sum")` | `groupsummary`, `splitapply(@sum, ...)` |
| Identifier literals | `replace`, `drop` or `keep` with `if id == 123` | assignments or filters with `d$id == 123` | `d.loc[d["id"] == 123]` | indexing with `T.id == 123` |
| Variants | loops over specification names; `alt`, `variant` or `robust` names in exhibit scripts | same | same | same |

A few `rg` passes cover most rows; replace `targets.csv` with the file's name:

```bash
rg -n -F 'targets.csv' --glob '!**/inspect/**'
rg -n '^\s*(cap(ture)?|try)\b|tryCatch|suppressWarnings|except\b|errors *= *"(coerce|ignore)"|\bforce\b'
rg -n '\b(erase|rmdir|unlink|file\.remove|rmtree|os\.remove)\b'
rg -n '(text|note|title|annotate|labs)\(.*[0-9]\.[0-9]{2}'
```

## Join guards by language

- **Stata.** `merge 1:1`, `m:1` and `1:m` stop when the side declared unique has repeated keys; `m:m`, `joinby` and the old `merge varlist using` syntax declare nothing. `assert(match)` or `assert(master match)` states which rows must match. `keep()` without `assert()` drops rows without notice, `force` merges variables of different types, and `duplicates drop, force` discards conflicting rows.
- **R.** dplyr 1.1 joins accept `relationship = "one-to-one"` or `"many-to-one"` and `unmatched = "error"`. Base `merge()` and data.table joins declare nothing.
- **Python.** pandas `merge` and `join` accept `validate="1:1"` or `"m:1"`, and `indicator=True` marks unmatched rows for inspection. polars `join` accepts `validate`.
- **MATLAB.** `join` requires unique keys in the right table and a match for every left row; `innerjoin` and `outerjoin` declare nothing.

Where a join declares nothing, count unmatched and repeated keys in the inspection script ([idioms](../../panel-data-checks-efh/code-examples.md)). Add a guard where the program relies on a cardinality, such as attaching assignment or design variables to units.
