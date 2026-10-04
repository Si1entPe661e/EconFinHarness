"""fh exemplars / recipe: read the accepted recipe cards shipped with the harness (harness_build/recipes/accepted/<artid>.json).

These commands read existing cards without rebuilding them or opening the corpus. Corpus search over the thirteen journal manifests
and the code-signal census lives in the build workstation (harness_build/cli/fhb.py search).
"""
import argparse, json, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fh_common as C  # noqa: E402


def load_cards():
    for p in sorted(C.RECIPES.glob("*.json")):
        try:
            c = C.read_json(p)
        except Exception:
            continue
        if c.get("schema_version") == "recipe-card-v2" and c.get("record_kind") == "corpus":
            yield c, p


def exemplars(method, lang=None, limit=10, as_json=False):
    """Rank recorded calls by coverage, evidence completeness and specification count."""
    rows = []
    for c, p in load_cards():
        dids = {d["id"]: d for d in c["designs"] if d.get("method") == method}
        if not dids or (lang and lang not in c["repository"]["languages"]):
            continue
        specs = [s for s in c["specifications"] if s.get("design_id") in dids]
        diag_obs = [x["kind"] for x in c["diagnostics"] if x["status"] == "observed"]
        known = sum(1 for s in specs for f in ("estimator", "fixed_effects", "weights", "sample") if s.get(f) is not None) + sum(1 for s in specs if s["se"].get("type"))
        score = {"full": 3, "partial": 2, "minimal": 0}[c["provenance"]["coverage"]] + min(len(specs), 6) * 0.5 + len(diag_obs) * 0.7 + known / max(len(specs), 1)
        rows.append({"artid": c["artid"], "journal": c["journal"], "year": c["year"], "coverage": c["provenance"]["coverage"], "languages": c["repository"]["languages"],
                     "variants": sorted({d["variant"] for d in dids.values() if d.get("variant")}), "score": round(score, 2),
                     "diagnostics_observed": diag_obs,
                     "specs": [{"id": s["id"], "command": s["command"], "estimator": s["estimator"], "se": s["se"]["type"], "cluster": s["se"]["cluster_level"],
                                "fe": s["fixed_effects"], "call": s["formula_or_call"],
                                "evidence": [(e["path"], e["lines"]) for e in s["evidence"] if "formula_or_call" in e.get("supports", [])][:1]} for s in specs]})
    rows.sort(key=lambda r: (-r["score"], r["artid"]))
    rows = rows[:limit]
    if as_json:
        print(json.dumps(rows, indent=1, ensure_ascii=False)); return rows
    for r in rows:
        print(f"## {r['artid']} ({r['journal']} {r['year']}, coverage {r['coverage']}, {'/'.join(r['languages'])}, variants {r['variants'] or '-'}, diagnostics {r['diagnostics_observed'] or '-'})")
        for s in r["specs"][:6]:
            loc = f"{s['evidence'][0][0]}:{s['evidence'][0][1][0]}-{s['evidence'][0][1][1]}" if s["evidence"] else "?"
            print(f"  {s['id']:<4} {s['command']:<18} est={s['estimator']} se={s['se']} cluster={s['cluster']} fe={s['fe']}  [{loc}]\n      {s['call'].replace(chr(10), chr(10) + '      ')[:400]}")
        print()
    print(f"# {len(rows)} exemplar cards for {method}. Calls are recorded from cited source lines; absolute workstation paths are redacted. Source pointers are relative to Paper/<Journal>/articles/<artid>/, which is not distributed. Adapt the specification to the research question and check the original license before copying.")
    return rows


def recipe(artid, mode="summary"):
    p = C.RECIPES / f"{artid}.json"
    if not p.exists():
        sys.exit(f"no accepted card for {artid}")
    c = C.read_json(p)
    if mode == "json":
        print(json.dumps(c, indent=1, ensure_ascii=False)); return
    methods = sorted({d["method"] for d in c["designs"] if d.get("method")})
    print(f"{artid} {c['journal']} {c['year']} doi={c['doi']} coverage={c['provenance']['coverage']}")
    print(f"methods={methods} languages={c['repository']['languages']} files_read={len(c['provenance']['files_read'])}")
    for d in c["designs"]:
        print(f"  design {d['id']} method={d['method']} variant={d['variant']} role={d['role']} basis={d['classification_basis']} treatment={d['treatment']!r}")
    for sp in c["specifications"]:
        ev = next(((e["path"], e["lines"]) for e in sp["evidence"] if "formula_or_call" in e.get("supports", [])), None)
        print(f"  spec {sp['id']} d={sp['design_id']} {sp['command']} est={sp['estimator']} fe={sp['fixed_effects']} se={sp['se']['type']}/{sp['se']['cluster_level']} w={sp['weights']} out={sp['output_ids']} [{ev[0] if ev else '?'}:{ev[1] if ev else ''}]")
        if mode == "specs":
            print("      " + sp["formula_or_call"].replace("\n", "\n      "))
    for x in c["diagnostics"]:
        print(f"  diag {x['id']} {x['kind']} {x['status']} {x['observation'] or ''} {(x['description'] or '')[:90]}")
    for r in c["robustness"]:
        print(f"  robustness {r['type']} base={r['baseline_spec_ids']} var={r['variant_spec_ids']} {r['relationship_status']}")
    print(f"  tables={len(c['outputs']['tables'])} figures={len(c['outputs']['figures'])} packages={[(k['ecosystem'], k['name'], k['usage']) for k in c['packages']][:8]}")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="fh exemplars|recipe")
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("exemplars"); e.add_argument("method"); e.add_argument("--lang"); e.add_argument("--limit", type=int, default=10); e.add_argument("--json", action="store_true")
    r = sub.add_parser("recipe"); r.add_argument("artid"); r.add_argument("--json", action="store_true"); r.add_argument("--specs", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "exemplars":
        exemplars(a.method, a.lang, a.limit, a.json)
    else:
        recipe(a.artid, "json" if a.json else "specs" if a.specs else "summary")


if __name__ == "__main__":
    main()
