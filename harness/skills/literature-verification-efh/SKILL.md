---
name: literature-verification-efh
description: "Literature search and verification: search available cards, notes and optional local corpus metadata before the web, separate relevance from support for a specific claim, record verification status and local code status, and deliver a paper list with artid or DOI and gaps. Use for literature tasks. Not for writing prose or method design."
metadata:
  version: 0.1.0
  kind: task
  status: draft
---

# Corpus-first literature search and verification

## When to use

- A research question, method, or setting needs a list of related work.
- A specific claim in a draft needs a citation, or an existing citation needs verification.
- A method must be traced to its source paper before it is implemented.
- Replication code for a published method is needed and its availability must be established.
- An earlier literature list must be re-checked because a claim changed.

## When not to use

- Writing prose or building a bibliography style. Use `academic-writing-efh`.
- Deciding an identification strategy from the literature. The literature role supplies verified sources; the empirical analyst decides.
- Reading a paper's replication code in depth to produce a recipe card. That is the code engineer role and the reading protocol.
- Any task that would require bypassing a paywall, a login, or a site's terms. Those are refused, not worked around.

## Inputs required

Required:

1. The research question or the exact claim that needs support, written as one sentence.
2. Whether the task is discovery (find related work) or verification (check a specific reference or claim).
3. The scope: journals, years, methods, settings, and languages in scope.

Useful when available:

4. Candidate references already in hand, with whatever identifier exists.
5. The claim's home in the draft, with the claim id from the claims-to-evidence table.
6. Whether local replication code is needed, and for what purpose.

## Procedure

1. Distinguish discovery from verification of a particular claim; define scope and relevance before searching.
2. Search available local references and recorded practice, then authoritative public sources. An absent optional corpus does not block a public search.
3. Resolve identifiers and versions from records actually read. Verify bibliographic identity separately from whether the text supports the claim.
4. Record what was inspected, access restrictions, relevant counterevidence, code availability and unresolved support. Never guess a DOI or infer unread content.
5. Deliver useful sources, claim support and gaps; recheck support when a claim changes.

Read [search and verification details](references/search-and-verification.md) only for the selected search/check mode, status vocabulary and optional corpus/code inspection. That reference retains the existing source-access restrictions and missing-information rules. It does not authorize new collection or extraction.

For the optional output shapes, use `templates/paper_list.csv` or `templates/search_log.md`. A short citation check can remain inline.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Use the relevant method to focus literature/code searches on the actual claim or implementation question. Feed useful verified material to research design without initiating new estimates or rebuilding the corpus.

## Research records

Read [research records](references/research-records.md) only when recorded practice or corpus evidence is relevant. These records are distinct from methodological recommendations.

## Templates

- `templates/paper_list.csv`: the deliverable row format, one row per paper, with identifier, relevance, support per claim, source, verification status, and local code status.
- `templates/search_log.md`: queries run, sources consulted, restrictions encountered, and the gaps section.

Templates are drafts. They are not tested and carry no execution environment.
