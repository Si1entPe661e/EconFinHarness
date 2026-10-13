## Procedure

1. **Clarify the research question and what counts as relevant.** State what would make a paper count as relevant, and separately what would make a paper count as support for the claim. These are different tests. Mixing them produces a list that looks like support and is not. Keep that distinction clear while searching.

2. **Search available local material first.** Start with references and recorded practices in `harness/paradigms/`. Standalone code cards and paper-practice notes are not included in the public package; consult them if available locally. If an optional local corpus is available, match on title and abstract across `Paper/*/metadata/articles.csv`. Search the whole set of journals in scope. Use several formulations: the method name, common abbreviations, the estimator name, the setting, and the outcome. Record the queries you ran, because a later reader needs to know what was not searched. Narrow by journal or year before running a full-corpus scan, since the corpus is large.

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

See [checklist.md](../checklist.md). Every item accepts yes, no, or unknown. `unknown` is a legitimate answer and is not `no`.
