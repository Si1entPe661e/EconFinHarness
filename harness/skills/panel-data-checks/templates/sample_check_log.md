# Sample check log

- sample id:
- analysis plan / specification ids covered:
- build script (path):
- estimation script (path):
- mode: `data_available` | `static_read_only`
- run at (UTC):
- run by (role, instance):

## Claimed sample

- unit of observation:
- key variables:
- claimed restrictions, in order:

## Check results

`status` is one of `pass`, `fail`, `unknown`, `not_applicable`. `unknown` requires a reason.

| check | status | observed value | expected value | location | note |
|---|---|---|---|---|---|
| key uniqueness | | | | | |
| duplicate classification | | | | | |
| singleton groups | | | | | |
| panel balance | | | | | |
| time index and gaps | | | | | |
| treatment timing consistency | | | | | |
| merge audit (see below) | | | | | |
| reported N reproduced | | | | | |
| missingness by variable | | | | | |
| differential missingness | | | | | |
| weights | | | | | |
| variable ranges and units | | | | | |
| winsorization / trimming | | | | | |
| lookahead / leakage | | | | | |

## Merge audit

| merge id | left | right | keys | expected cardinality | realised cardinality | rows before | rows after | matched | unmatched left | unmatched right | disposition of unmatched | pattern in unmatched |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

## Blocking findings

| id | finding | affected specification ids | why it blocks | owner role | status |
|---|---|---|---|---|---|
| | | | | | |

## Open items (unknown or conflict)

| id | item | value (`unknown` / `conflict`) | what would resolve it | owner role |
|---|---|---|---|---|
| | | | | |
