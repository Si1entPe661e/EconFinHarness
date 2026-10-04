# Inference option-to-call trace

One form per reported table or panel. A cluster option appearing in a script is not evidence that the reported table used it. Every link below needs a file path and a line range. If any link is missing, the trace status is `unverified`.

- table id:
- specification ids in this table:
- traced at (UTC):
- traced by (role, instance):

| link | question | file path | lines | value found | status |
|---|---|---|---|---|---|
| 1 | Which script writes the table file? | | | | |
| 2 | Which estimation call produced the stored estimates the table reads? | | | | |
| 3 | What is written as the cluster / vcov argument in that call? | | | | |
| 4 | If the argument is a macro, local, wrapper argument, or default, what does it resolve to at the point of the call? | | | | |
| 5 | Is the macro reassigned between the call and any earlier definition? | | | | |
| 6 | Does the exported table read those stored estimates, or a different set? | | | | |
| 7 | Do stars, p-values, and confidence intervals in the table come from the same variance estimator? | | | | |
| 8 | Which package and version executed the call? | | | | |

Trace status: `verified` | `unverified`

Missing link (if unverified):

Design-implied minimum cluster level, derived independently of the code:

Match between design-implied level and resolved cluster variable: `match` | `finer_than_design` | `coarser_than_design` | `unknown`

Finding category: `confirmed_error` | `methodological_risk` | `needs_information`
