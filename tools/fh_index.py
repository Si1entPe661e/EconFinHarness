"""Read-only search over the existing article, code-signal and card index."""
import argparse
import json
import pathlib
import re
import sqlite3
import sys

import fh_common as C

def _connect(index_path=None):
    database = pathlib.Path(index_path).expanduser() if index_path else C.LOCAL_INDEX
    if not database.is_file():
        sys.exit("Local search index unavailable; it is not included in the public repository. Use skills, exemplars and recipe for included material, or read Paper/<Journal>/metadata/articles.csv if a local corpus is available.")
    con = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def search(query=None, method=None, journal=None, lang=None, signal=None, has_code=None, year_from=None, year_to=None, limit=25, as_json=False, index_path=None):
    con = _connect(index_path)
    cur = con.cursor()
    fts = bool(cur.execute("SELECT name FROM sqlite_master WHERE name='articles_fts'").fetchone())
    hits = {}  # artid -> {kinds}
    text_hits = {}
    if query:
        if fts:
            q = " ".join(f'"{t}"' for t in re.findall(r"[A-Za-z0-9_\-']+", query))
            try:
                for r in cur.execute("SELECT artid, bm25(articles_fts) AS rank FROM articles_fts WHERE articles_fts MATCH ? ORDER BY rank LIMIT ?", (q, limit * 20)):
                    text_hits[r["artid"]] = r["rank"]
            except sqlite3.OperationalError:
                fts = False
        if not fts:
            like = f"%{query}%"
            for r in cur.execute("SELECT artid FROM articles WHERE title LIKE ? OR abstract LIKE ? LIMIT ?", (like, like, limit * 20)):
                text_hits[r["artid"]] = 0
        for a in text_hits:
            hits.setdefault(a, set()).add("text")
    sig_hits = {}
    if signal:
        for r in cur.execute("SELECT artid, hits FROM signals WHERE signal=?", (signal,)):
            sig_hits[r["artid"]] = r["hits"]; hits.setdefault(r["artid"], set()).add("signal")
    card_hits = {}
    if method:
        for r in cur.execute("SELECT artid, methods, commands, coverage FROM cards WHERE (';'||methods||';') LIKE ?", (f"%;{method};%",)):
            card_hits[r["artid"]] = dict(r); hits.setdefault(r["artid"], set()).add("card")
    if not (query or signal or method):
        for r in cur.execute("SELECT artid FROM articles LIMIT ?", (limit * 20,)):
            hits.setdefault(r["artid"], set())
    rows = []
    for artid, kinds in hits.items():
        a = cur.execute("SELECT * FROM articles WHERE artid=?", (artid,)).fetchone()
        if a is None:
            continue
        if journal and a["journal"] != journal:
            continue
        if has_code and not a["has_local_code"]:
            continue
        if year_from and (a["year"] or 0) < year_from:
            continue
        if year_to and (a["year"] or 9999) > year_to:
            continue
        if lang and not (a["languages"] or "").lower().startswith(lang.lower()) and f"{lang.lower()}:" not in (a["languages"] or "").lower():
            continue
        sigs = {r["signal"]: r["hits"] for r in cur.execute("SELECT signal, hits FROM signals WHERE artid=?", (artid,))}
        card = cur.execute("SELECT methods, commands, coverage, variants FROM cards WHERE artid=?", (artid,)).fetchone()
        score = (3 if "card" in kinds else 0) + (2 if "signal" in kinds else 0) + (1 if "text" in kinds else 0) + (0.5 if a["has_local_code"] else 0)
        rows.append({"artid": artid, "journal": a["journal"], "year": a["year"], "title": (a["title"] or "")[:110], "doi": a["doi"],
                     "has_local_code": bool(a["has_local_code"]), "languages": a["languages"], "evidence": {
                         "text_match": bool("text" in kinds), "code_signals": {k: v for k, v in sigs.items() if not signal or k == signal},
                         "card": {"methods": card["methods"], "variants": card["variants"], "commands": card["commands"], "coverage": card["coverage"]} if card else None},
                     "score": score})
    rows.sort(key=lambda r: (-r["score"], -(r["year"] or 0), r["artid"]))
    rows = rows[:limit]
    if as_json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
    else:
        for r in rows:
            ev = []
            if r["evidence"]["text_match"]: ev.append("text")
            if r["evidence"]["code_signals"]: ev.append("signals:" + ",".join(f"{k}={v}" for k, v in sorted(r["evidence"]["code_signals"].items())[:4]))
            if r["evidence"]["card"]: ev.append(f"card:{r['evidence']['card']['methods']}/{r['evidence']['card']['coverage']}")
            print(f"{r['artid']:<32} {r['journal']:<12} {r['year']} code={'y' if r['has_local_code'] else 'n'} {r['title'][:70]:<70} | {' '.join(ev)}")
        print(f"# {len(rows)} results (evidence kinds kept separate: text = title/abstract keyword, signals = regex code signals, card = accepted recipe card)")
    con.close()
    return rows


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["search"]:
        args = args[1:]
    ap = argparse.ArgumentParser(prog="fh search", description=__doc__)
    ap.add_argument("query", nargs="?")
    ap.add_argument("--method")
    ap.add_argument("--journal")
    ap.add_argument("--lang")
    ap.add_argument("--signal")
    ap.add_argument("--has-code", action="store_true")
    ap.add_argument("--year-from", type=int)
    ap.add_argument("--year-to", type=int)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--index", help="Path to an existing local SQLite index; defaults to local/fh_index.sqlite")
    a = ap.parse_args(args)
    search(a.query, a.method, a.journal, a.lang, a.signal, a.has_code,
           a.year_from, a.year_to, a.limit, a.json, a.index)
    return 0

if __name__ == "__main__":
    sys.exit(main())
