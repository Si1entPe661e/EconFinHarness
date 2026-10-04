---
name: literature-verification
description: "Literature search and verification: search available cards, notes and optional local corpus metadata before the web, separate relevance from support for a specific claim, record verification status and local code status, and deliver a paper list with artid or DOI and gaps. Use for literature tasks. Not for writing prose or method design."
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

- Writing prose or building a bibliography style. Use `academic-writing`.
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

1. **Clarify the research question and what counts as relevant.** State what would make a paper count as relevant, and separately what would make a paper count as support for the claim. These are different tests. Mixing them produces a list that looks like support and is not. Keep that distinction clear while searching.

2. **Search available local material first.** The public package contains code cards and paper-practice notes under `examples/`. Search their DOI/artid and recorded observations. If an optional local corpus is available, match on title and abstract across `Paper/*/metadata/articles.csv`. Search the whole set of journals in scope. Use several formulations: the method name, common abbreviations, the estimator name, the setting, and the outcome. Record the queries you ran, because a later reader needs to know what was not searched. Narrow by journal or year before running a full-corpus scan, since the corpus is large.

3. **Inspect available code and source pointers.** Original replication source trees are not included in the public package. When a local corpus exists, for each candidate check `Paper/<Journal>/articles/<artid>/`. Record what is present: `code/` contents and languages, `docs/`, and `paper/source.json`. The corpus holds source code and metadata. It does not hold paper PDFs, and it does not hold datasets. Do not attempt to obtain either.

4. **Record the local code status honestly.** Use one of: `code_present` with languages and a rough file count; `code_absent`; `link_only` when a repository link exists in metadata but nothing was collected; `no_code_link` when the collector recorded the source as having no code. Never infer that code exists because the journal has a data policy.

5. **Extend to the web after searching the available local material.** If the optional corpus is absent, continue with public sources without requiring an index or collection step. Use Crossref, then OpenAlex, then Semantic Scholar. Search by title, by DOI, and by author plus year. Prefer the publisher's record of authority for the version of record. Record which service returned the record and what it returned.

6. **Resolve every reference to a stable identifier.** A DOI, or an artid when the paper is in the corpus. A reference without an identifier is not usable in a research output and is recorded as `unverified` with a note on what is missing. Do not construct a DOI from a pattern. Do not report a DOI you did not read from a source.

7. **Check the version.** Working paper, accepted version, and version of record can differ in results, sample, and even in the sign of a coefficient. Record which version was checked and where it came from. If a claim depends on a specific number in a paper, that number must come from the version cited, not from a different version and not from memory.

8. **Separate relevance from support, explicitly, per claim.** Relevance means the paper is about the same method, setting, or question. Support means the paper contains a finding that establishes the specific claim being made. A paper can be highly relevant and give no support at all. For every claim, record the support judgement separately from the relevance judgement, and record what was actually read to reach it (abstract only, the specific section, the specific table). "Support" asserted from an abstract alone is recorded as such.

9. **Assign a verification status from a fixed vocabulary.**
   - `verified_corpus`: the record was found in `Paper/*/metadata/articles.csv` or a per-article directory, with an artid, and the metadata fields used were read from that record.
   - `verified_online`: the record was resolved through Crossref, OpenAlex, Semantic Scholar, or the publisher's own record, with a DOI, and the fields used were read from that response.
   - `unverified`: the reference comes from memory or from an unverified secondary source, or the identifier could not be resolved. It is labelled `unverified` everywhere it appears, including in any draft.
   Verification of the record's existence is not verification of a claim about its content. Keep the two fields separate.

10. **Respect access rules absolutely.** Do not bypass a paywall, a login, a rate limit, a robots directive, or a human verification page. When a source is restricted, record the link, the restriction encountered, and the reason, and move on. Note that publisher article pages for several journals in scope refuse scripted access; that is a recorded restriction, not a problem to solve. Keep request rates low and single-threaded against repository APIs.

11. **Do not download prohibited material.** No paper PDFs, no datasets, no full replication archives. This applies to every source, including open access ones. If a link would supply them, record the link only.

12. **Record the gaps.** List what was searched and found nothing, what could not be accessed and why, which claims still have no support, and which candidate references remain unresolved. A literature deliverable without a gaps section overstates its own coverage.

13. **Deliver the useful references and gaps.** Include identifiers, relevance, claim support, sources, verification status and actual code availability. Use `templates/paper_list.csv` or `templates/search_log.md` when their format helps.

14. **Re-verify when a claim changes.** A verification is a statement about a specific claim and a specific version. If the claim text changes, the support judgement is stale until re-checked.

### When information is missing

- If a reference cannot be resolved to an identifier, deliver it as `unverified` with the searches attempted. Do not drop it silently and do not guess an identifier.
- If a paper's content cannot be read because the source is restricted, record `needs_information` for the support judgement. Do not infer content from the title or the abstract and present it as read.
- If the corpus has no code for a paper whose code is needed, record `code_absent` or `link_only` and say what would be required to obtain it under the project policy.
- If the scope was not specified, propose a scope, state it in the deliverable, and record it as an assumption to be confirmed.

## Missing information

| situation | value | what to record |
|---|---|---|
| Identifier not resolvable | `unverified` | the reference as known, every search attempted, and which service was used |
| Source restricted | `restricted` | the link, the restriction encountered, and the date |
| Content not read, only metadata | `needs_information` | what was read (title, abstract) and what would be needed |
| Relevant but does not support the claim | `relevant_not_supporting` | one sentence on what the paper does establish |
| Local code expected but absent | `code_absent` or `link_only` | the metadata link if one exists, and the collector's status |
| Scope not specified by the requester | `assumed_scope` | the assumed journals, years, and methods |

## Checklist

See [checklist.md](checklist.md). Every item accepts yes, no, or unknown. `unknown` is a legitimate answer and is not `no`.

## Skill composition

For compound tasks, consult harness/skill-composition.md and read only relevant skills. Use the relevant method to focus literature/code searches on the actual claim or implementation question. Feed useful verified material to research design without initiating new estimates or rebuilding the corpus.

## Evidence

This is a task skill. It carries no corpus counts. It does not state how many papers in `Paper/` use any method, and it must not be cited as evidence of prevalence. Counts about the corpus come from the corpus metadata and audit files at the time they are computed.

Method-specific observed practice, with denominators and explicit unknown counts, is in `harness/paradigms/<method>/observed.md` (for example `harness/paradigms/rdd/observed.md`). Recommendations are separate and live in `harness/paradigms/<method>/recommendations.md`.

The corpus under `Paper/` is read-only. Metadata files under `Paper/*/metadata/` are audited artifacts and are not modified by this skill.

<!-- reported-practice:begin -->
### Reported practice (paper texts; generated by `fhb papers skill-evidence`, 2026-09-09)

From 91 paper-practice notes (all methods; `harness/paradigms/_all/reported.md`, note hashes there). Counts are papers whose note carries the tag; an absent tag means the reader did not record it. Pointers are artid p.pages locator.

- **data_access** (papers with the category: 91/91): `administrative` 66 (e.g. aer_107_1_5 p.14 Section II.B; author note); `data_restricted` 38 (e.g. aer_107_1_5 p.14 Section II.B; author note); `public_use` 34 (e.g. aer_110_10_1 p.25 Sec. IIIA, Evidence from the Arab Barome); `linked_records` 29 (e.g. aer_107_1_5 p.26 Section III.B, Measurement Error)

- **replication_statement** (papers with the category: 89/91): `replication_package_cited` 88 (e.g. aer_107_1_5 p.14 footnote; References); `code_public` 56 (e.g. aer_107_5_51 p.1 introduction, para 1); `data_public` 43 (e.g. aer_110_10_1 p.32 References); `software_named` 31 (e.g. aer_107_1_5 p.20 Section III.A)
<!-- reported-practice:end -->

## Templates

- `templates/paper_list.csv`: the deliverable row format, one row per paper, with identifier, relevance, support per claim, source, verification status, and local code status.
- `templates/search_log.md`: queries run, sources consulted, restrictions encountered, and the gaps section.

Templates are drafts. They are not tested and carry no execution environment.
