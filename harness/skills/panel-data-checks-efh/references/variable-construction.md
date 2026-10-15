# Constructing variables from several sources

Read this when a concept can be measured more than one way: several survey waves, several informants (spouses, parents and children, managers and firms), administrative records merged with survey items, or a paper that defines one variable in its text, footnotes and table notes.

## Candidate measurements

Before building a derived rule, search the labels, notes and instruments of every authorized file for each concept and record the coverage of each candidate:

- an item that measures the concept directly, such as a question asking one informant to compare two people;
- later confirmations of time-invariant facts, such as birth year, education completed before assignment or a fixed location;
- each informant's report of the same quantity.

A direct item usually dominates a rule assembled from several indirect items. A derived rule needs a reason the direct item cannot serve.

## Reporter rule

Declare whose report each variable uses: the row's own report, one designated informant for every unit, or a fallback order. When the paper names a source, use it for all units rather than mixing sources by availability, because a mixed rule changes what the variable measures across subsamples. Fill a missing value from another measurement of the same concept before any constant fill, and record how many values each fallback supplies.

## Register

Keep one row per consequential concept:

| Column | Content |
|---|---|
| concept | the paper's term |
| mentions | every page, footnote, table note and legend that defines or uses it |
| candidates | files and columns, with nonmissing counts |
| primary | the rule used for the main reproduction and why |
| alternatives | declared before the first estimate |
| discriminating evidence | a statistic sensitive to the choice, such as a descriptive mean or count |
| status | open, resolved by inspection, or departure |

## Identifying a descriptive variable

Comparing a descriptive statistic with its published value to identify a variable is inspection, not estimation. A retained, exhaustive search over a declared candidate family (which categories enter, which sources and which missing rule) is admissible. Report the family, its size and the number of matches. When the match and the text differ only in units or scaling (for example the log of a variable against the log of the variable divided by 1000, which changes means but not differences or slopes), use the matching definition and report the text as a likely documentation error. When they differ in which categories, observations or sources enter, the match is reported as a departure and the text-faithful rule stays primary. A claim that no candidate matches is verified only by the retained enumeration. This exception covers variable identity in descriptive or balance tables. It does not license searching treatment-effect specifications for agreement with published estimates.
