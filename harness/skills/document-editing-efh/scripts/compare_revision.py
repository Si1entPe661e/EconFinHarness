"""Compare two revisions of a text for changed numbers, citations and evidential wording.

Usage:
    python3 -B harness/skills/document-editing-efh/scripts/compare_revision.py BEFORE AFTER [--json]

Exit status 0: nothing must be confirmed. Exit status 1: the "Must confirm" list names a removed or new
number, sign, unit, comparison operator, significance star or citation; causal, certainty or
significance wording or an attribution ("because", "due to", 由于) that the revision adds, or whose
negation it adds or removes; or association wording that falls while effect wording rises. Exit status 2: the files could not be compared.

Review items need reading but not a source: values repeated from the before text, changed labels such
as Table 4, NN3 or Q4, and changes in scope, restriction ("only", 仅), comparison, direction, hedge and
association wording. A fall in scope or restriction wording may mean a limitation was deleted rather
than moved, or a claim widened. Counts are net per word: the script cannot see a word that moves to a
different claim, Chinese numerals, or author-year citations except through their years, so changed
passages still need reading. Text inside [author: ...] or [作者：...] placeholders is ignored.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

NORMALIZE = str.maketrans({"\u2212": "-", "\uff0d": "-", "\u2010": "-", "\u2011": "-", "\u2012": "-", "\ufe63": "-", "\uff0e": ".", "\uff05": "%", "\uff1c": "<", "\uff1e": ">",
                           **{chr(0xFF10 + i): str(i) for i in range(10)}})
AUTHOR_MARKER = re.compile(r"[\[【](?:author|作者)\s*[:：](?:[^\]\[【】\n]|\n(?![ \t]*\n))*[\]】]", re.IGNORECASE)
LATEX_MINUS = re.compile(r"\$-\$|\\\(-\\\)")
EN_DASH_MINUS = re.compile(r"(?<![A-Za-z0-9.%)])\u2013(?=\.?\d)")
LIST_MARKER = re.compile(r"^[ \t]*\d+[.)][ \t]")
# References such as Table 4, Section 4.2, NN3, IA.3, Q4 or 表2 are labels, compared separately as review items.
_LABEL_NUMBER = r"\(?[A-Z]{0,3}\.?\d{1,2}(?!\d|,\d{3})(?:\.\d+)*[a-z]?\)?"
_LABEL_ITEM = r"\(?[A-Z]{0,3}\.?\d{1,2}(?![\d.]\d|,\d{3}|\d)[a-z]?\)?"
LABEL = re.compile(r"(?<![A-Za-z0-9_])(?:(?i:tables|figures|figs\.|sections|columns|cols\.|panels|appendices|equations|eqs\.|"
                   r"chapters|models)[\s~]*" + _LABEL_NUMBER + r"(?:\s*(?:[-–]|to|and|&|,(?=\s*\(?\d{1,2}\)?\s*(?:,|and|&)))\s*"
                   + _LABEL_ITEM + r")+"
                   r"|(?i:table|figure|fig\.|section|column|col\.|panel|appendix|equation|eq\.|chapter|model)[\s~]*" + _LABEL_NUMBER +
                   r"|(?!(?:USD|EUR|GBP|JPY|CNY|RMB|HKD|CHF|CAD|AUD|INR|KRW|SGD|Rs|Rp)\.?\d)[A-Z][A-Za-z]{0,3}\.?\d+(?:\.\d+)*"
                   r"|(?<![代发报列外仪试意地企构])[表图]\s*[A-Z]?\d+(?:\.\d+)*|第\s*[(（]?\d+[)）]?(?:\s*[、,，和至-]\s*[(（]?\d+[)）]?)*\s*[节章列栏])"
                   r"(?![\d.]*[   ]?(?:[%‰]|(?i:percent|per[ -]cent|percentage|pp|p\.p\.|basis|bps?|thousand|million|billion"
                   r"|trillion|mn|bn|tn|times)(?![A-Za-z])))")
# A sign follows no word, number or closing character; a number follows no lowercase letter, so citation keys
# such as smith2020 are not read; a leading-dot decimal follows no letter.
NUMBER = re.compile(r"(?:(?P<op>[<>\u2264\u2265])=?[ \t$]*)?(?P<num>(?:(?<![A-Za-z0-9_.%)])-(?=\.?\d))?"
                    r"(?:(?<![a-z0-9_.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?|(?<![A-Za-z0-9_.])\.\d+)"
                    r"(?:[eE][+-]?\d+)?)(?:[ \u00a0\u202f]?(?P<unit>[%\u2030]|万亿|千万|百万|[万亿千]|(?i:percent(?:age[ -]points?)?"
                    r"|per[ -]cent|pp|p\.p\.|basis[ -]points?|bps?|thousand|million|billion|trillion|mn|bn|tn)(?![A-Za-z])))?"
                    r"(?:(?:\$?\^\{?|\\sym\{|\\textsuperscript\{|<sup>)(?P<sup>\*{1,3})(?:\}|</sup>)?|(?P<stars>\*{1,3}))?")
UNITS = {"percent": "%", "per cent": "%", "per-cent": "%", "percentage point": "pp", "percentage points": "pp",
         "percentage-point": "pp", "percentage-points": "pp", "p.p.": "pp", "basis point": "bp", "basis points": "bp",
         "basis-point": "bp", "basis-points": "bp", "bps": "bp", "mn": "million", "bn": "billion", "tn": "trillion"}
CURRENCY, SCALES = ("$", "\u20ac", "\u00a3", "\u00a5", "\u20b9"), {"k": "thousand", "m": "million", "b": "billion"}
DOI = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
LATEX_CITE = re.compile(r"\\[A-Za-z]*[Cc]ites?[A-Za-z]*\*?((?:\s*(?:\([^)]*\)|\[[^\]]*\]))*\s*\{[^}]*\}"
                        r"(?:(?:\s*(?:\([^)]*\)|\[[^\]]*\]))*\s*\{[^}]*\})*)")
PANDOC_CITE = re.compile(r"(?<![\w@])@([A-Za-z0-9_][\w:.#$%&+?<>~/-]*)")

# English entries match whole words; Chinese entries match as substrings; entries starting with "(?"
# are regular expressions.
TERMS = {
    "causal": (["cause", "causes", "caused", "causing", "causal", "causally", "lead to", "leads to", "led to",
                "leading to", "resulted in", "resulting in", "drive", "drives", "drove", r"(?<![A-Za-z-])driving(?![A-Za-z])(?!\s+(?:distances?|times?)\b)", "driven by",
                r"(?<![A-Za-z-])results?\s+in(?![A-Za-z])(?!\s+(?:the\s+|this\s+|our\s+)?(?:main\s+|previous\s+|next\s+|"
                r"following\s+|first\s+|second\s+|last\s+)?(?:tables?|columns?|figures?|panels?|sections?|chapters?|"
                r"appendix|appendices|rows?|col\.|fig\.|tab\.|sec\.|early|mid|late|january|february|march|april|may|june|"
                r"july|august|september|october|november|december|q[1-4]|\d{4})(?![A-Za-z]))"],
               ["因果", "导致", "造成", "(?<!数据)驱动", "引起(?!.{0,4}(?:关注|注意|重视|兴趣|讨论|争议))"]),
    "certainty": (["prove", "proves", "proved", "proven", "demonstrate", "demonstrates", "demonstrated", "establish",
                   "establishes", r"(?<![A-Za-z-])established(?![A-Za-z])(?!\s+(?:firms?|companies|incumbents|banks|businesses|enterprises|institutions)\b)", r"(?<![A-Za-z-])confirm(?:s|ed)?(?![A-Za-z])(?=\s+(?:that|the\s+(?:hypothes[ie]s|predictions?|findings?|results?|mechanism|effect)|our|this|these|a\s+causal))", "clearly", "conclusively",
                   "definitively", "undoubtedly"],
                  ["证明", "证实", "毫无疑问", "无疑"]),
    "significance": (["significant", "significantly", "statistically significant", "statistically significantly",
                      "insignificant", "nonsignificant", "non-significant", "statistically insignificant",
                      "significance", "statistical significance", "statistically different",
                      "statistically distinguishable", "statistically indistinguishable", "reject the null",
                      "rejects the null", "rejected the null", "rejecting the null"], ["显著"]),
    "association": (["associated", "association", "associations", "correlate", "correlates", "correlated",
                     "correlation", "correlations"], ["相关", "关联"]),
    "scope": (["limitation", "limitations", "cannot", "external validity", "generalize", "generalizes",
               "generalizability", "beyond the scope", "only applies", "do not claim", "does not claim",
               "with caution", "does not cover", "do not cover", "compliers", "intent-to-treat",
               "partial equilibrium", "local average", "local to", "near the threshold", "near the cutoff"],
              ["局限", "无法", "不能", "有待", "外部有效性", "仅适用", "依从者", "局部平均", "意向性"]),
    "restriction": (["only", "merely", "solely", "exclusively"], ["仅仅", "仅", "只在", "只对", "只有", "仅限"]),
    "comparison": (["larger", "smaller", "outperform", "outperforms", "underperform", "underperforms", "lag", "lags",
                    "close to", "similar to", "comparable"],
                   ["更大", "更小", "偏大", "偏小", "落后", "优于", "劣于", "接近", "相近", "高于", "低于", "大于", "小于"]),
    "hedge": (["may", "might", "could", "suggest", "suggests", "suggested", "suggesting", "suggestive", "likely",
               "possibly", "potentially", "perhaps", "appears to", "appear to"],
              ["可能", "或许", "也许", "似乎", "初步", "提示"]),
    "direction": (["increase", "increases", "increased", "decrease", "decreases", "decreased", "raise", "raises",
                   "raised", "reduce", "reduces", "reduced", "higher", "lower", "positive", "positively", "negative",
                   "negatively", "rise", "rises", "rose", "fall", "falls", "fell", "affect", "affects", "impacts",
                   "effect", "effects", "impact", "impacted", "influence", "influences", "influenced",
                   "improve", "improves", "improved"],
                  ["上升", "下降", "增加", "减少", "提高", "降低", "正向", "负向", "促进", "抑制", "影响"]),
}
TERMS["attribution"] = (["because", "because of", "due to", "owing to", "attributable to", "attributed to", "explained by",
                          "explains", "reflect", "reflects", "reflected", "reflecting", "stems from"], ["由于", "源于", "归因于", "归功于", "得益于", "原因在于"])
MUST_CONFIRM_INCREASE = ("causal", "certainty", "significance", "attribution")
# A watched term after a negator counts as "not <term>"; only unnegated terms count as added claims.
NEGATED = re.compile(r"(?:(?:(?<![A-Za-z])(?:not|no|never|cannot|without|neither|nor|(?:fail(?:s|ed|ing)?|unable)\s+to|(?<![Aa]\s)little)|n['\u2019]t)"
                     r"(?:\s+(?!(?:only|just|merely|simply|surprisingly|doubts?|surprise|question|wonder|and|but|or|while|whereas"
                     r"|although|though|because|which|who)\b)[A-Za-z]+){0,5}\s+"
                     r"|(?:不会|不能|不|未必|未|没有|并非|无法|未能|并未|难以|(?<!毫)无)(?:全部|完全|全|都|均)?(?:再|一定|必然|总是|具有|具备|通过|存在|呈现|表现出|发现|观察到|得到"
                     r"|(?:能够?)?(?:证据)?(?:说明|表明|证明|显示|意味着|认为|确定)[^，。；：！？,.;:!?\s]{0,8}|[应宜](?:被)?(?:解读|理解|解释|视)为)?(?:统计上?)?)$", re.IGNORECASE)
LEMMAS = {"causes": "cause", "caused": "cause", "causing": "cause", "leads to": "lead to", "led to": "lead to",
          "leading to": "lead to", "resulted in": "result in", "resulting in": "result in", "results in": "result in",
          "drives": "drive", "drove": "drive", "driving": "drive", "proves": "prove", "proved": "prove",
          "proven": "prove", "demonstrates": "demonstrate", "demonstrated": "demonstrate",
          "establishes": "establish", "established": "establish", "confirms": "confirm", "confirmed": "confirm",
          "rejects the null": "reject the null", "rejected the null": "reject the null",
          "rejecting the null": "reject the null", "driven by": "drive", "reflect": "reflects", "reflected": "reflects",
          "reflecting": "reflects",
          **{form: base for base, forms in (("increase", "increases increased"), ("decrease", "decreases decreased"),
                                           ("raise", "raises raised"), ("reduce", "reduces reduced"), ("rise", "rises rose"),
                                           ("fall", "falls fell"), ("affect", "affects"), ("improve", "improves improved"))
             for form in forms.split()}}
NEGATIVE_FORMS = {"insignificant": "significant", "nonsignificant": "significant", "non-significant": "significant",
                  "statistically insignificant": "statistically significant",
                  "statistically indistinguishable": "statistically distinguishable"}


def term_pattern(english, chinese):
    parts = [t if t.startswith("(?") else r"(?<![A-Za-z-])" + r"\s+".join(map(re.escape, t.split())) + r"(?![A-Za-z])"
             for t in english]
    parts += [t if t.startswith("(?") else re.escape(t) for t in chinese]
    return re.compile("|".join(sorted(parts, key=len, reverse=True)), re.IGNORECASE)


PATTERNS = {name: term_pattern(*terms) for name, terms in TERMS.items()}


OPERATORS = ((re.compile(r"\\(?:leq?|leqslant)(?![A-Za-z])|&le;|<="), "\u2264"),
             (re.compile(r"\\(?:geq?|geqslant)(?![A-Za-z])|&ge;|>="), "\u2265"),
             (re.compile(r"\\textless(?![A-Za-z])(?:\{\})?|&lt;"), "<"),
             (re.compile(r"\\textgreater(?![A-Za-z])(?:\{\})?|&gt;"), ">"))
CURRENCY_PREFIX = re.compile(r"(?<![A-Za-z])(Rs|Rp)\.?(?=\d)")


def normalize(text):
    text = LATEX_MINUS.sub("-", AUTHOR_MARKER.sub(" ", text).translate(NORMALIZE)).replace("\\*", "*").replace("\\%", "%")
    for pattern, operator in OPERATORS:
        text = pattern.sub(operator, text)
    text = CURRENCY_PREFIX.sub(r"\1 ", text)
    return EN_DASH_MINUS.sub("-", text)


def strip_list_markers(text):
    lines, in_list = text.split("\n"), True
    for i, line in enumerate(lines):
        if not line.strip():
            in_list = True
        elif LIST_MARKER.match(line) and (in_list or re.match(r"[ \t]*1[.)]", line)):
            lines[i], in_list = LIST_MARKER.sub("", line), True
        else:
            in_list = False
    return "\n".join(lines)


def labels(text):
    return Counter(" ".join(re.sub(r"\s*[-\u2013]\s*", "-", re.sub(r"[()（）~]", " ", m)).lower().split())
                   for m in LABEL.findall(text))


def numbers(text):
    found = Counter()
    text = LABEL.sub("_", strip_list_markers(text))
    for m in NUMBER.finditer(text):
        stars = m["sup"] or m["stars"] or ""
        if m["stars"]:
            prefix, run = text[text.rfind("\n", 0, m.start()) + 1:m.start()], re.escape(stars)
            opened = (len(re.findall(r"(?<![\w*\\])" + run + r"(?=[^\s*])", prefix))
                      > len(re.findall(r"(?<=[^\s*\\])" + run + r"(?![\w*])", prefix)))
            if opened or text[max(0, m.start() - len(stars)):m.start()] == stars:
                stars = ""  # Markdown emphasis such as **0.3** or **grew 12%**, not significance stars.
        unit = m["unit"] or ""
        if not unit and text[m.start("num") - 1:m.start("num")] in CURRENCY and re.match(r"[kKmMbB](?![A-Za-z0-9])", text[m.end():]):
            unit = SCALES[text[m.end()].lower()]
        unit = UNITS.get(" ".join(unit.lower().split()), unit.lower() if unit.isascii() else unit)
        found[(m["op"] or "") + re.sub(r"[,\s\u00a0\u202f]", "", m["num"]) + unit + stars] += 1
    return found


def citations(text):
    found = Counter("doi:" + m.rstrip(".,;:)").lower() for m in DOI.findall(text))
    for group in LATEX_CITE.findall(text):
        for keys in re.findall(r"\{([^}]*)\}", group):
            found.update("key:" + k.strip() for k in keys.split(",") if k.strip())
    found.update("key:" + k.rstrip(":.#$%&+?<>~/-") for k in PANDOC_CITE.findall(text))
    return found


def terms(text):
    result = {}
    for name, pattern in PATTERNS.items():
        found = Counter()
        for m in pattern.finditer(text):
            token = " ".join(m.group().lower().split())
            token = LEMMAS.get(token, token)
            if token in NEGATIVE_FORMS:
                token = "not " + NEGATIVE_FORMS[token]
            elif NEGATED.search(text, max(0, m.start() - 70), m.start()):
                token = "not " + token
            found[token] += 1
        result[name] = found
    return result


def diff(before, after):
    return {"removed": dict(sorted((before - after).items())), "added": dict(sorted((after - before).items()))}


def compare(before_text, after_text):
    before_text, after_text = normalize(before_text), normalize(after_text)
    before_numbers = numbers(before_text)
    result = {"numbers": diff(before_numbers, numbers(after_text)),
              "citations": diff(citations(before_text), citations(after_text)),
              "labels": diff(labels(before_text), labels(after_text)),
              "terms": {}, "must_confirm": [], "review": []}

    def listed(items):
        return ", ".join(f"{token} x{count}" for token, count in items.items())

    added = result["numbers"]["added"]
    new = {t: n for t, n in added.items() if t not in before_numbers}
    repeated = {t: n for t, n in added.items() if t in before_numbers}
    for heading, items, target in (("numbers removed", result["numbers"]["removed"], "must_confirm"),
                                   ("numbers added", new, "must_confirm"),
                                   ("numbers repeated from before text", repeated, "review"),
                                   ("citations removed", result["citations"]["removed"], "must_confirm"),
                                   ("citations added", result["citations"]["added"], "must_confirm"),
                                   ("labels removed", result["labels"]["removed"], "review"),
                                   ("labels added", result["labels"]["added"], "review")):
        if items:
            result[target].append(f"{heading}: {listed(items)}")
    before_terms, after_terms = terms(before_text), terms(after_text)
    rose = set()
    for name in TERMS:
        b, a = before_terms[name], after_terms[name]
        changed = {t: [b[t], a[t]] for t in sorted(set(b) | set(a)) if b[t] != a[t]}
        if not changed:
            continue
        result["terms"][name] = changed
        line = f"{name} wording {sum(b.values())} -> {sum(a.values())}: " + ", ".join(
            f"{t} {x}->{y}" for t, (x, y) in changed.items())
        added_claim = any(y > x for t, (x, y) in changed.items() if not t.startswith("not "))
        removed_negation = (sum(n for t, n in a.items() if t.startswith("not "))
                            < sum(n for t, n in b.items() if t.startswith("not ")))
        if added_claim:
            rose.add(name)
        added_negation = (sum(n for t, n in a.items() if t.startswith("not "))
                          > sum(n for t, n in b.items() if t.startswith("not ")))
        unnegated_fell = (sum(n for t, n in a.items() if not t.startswith("not "))
                          < sum(n for t, n in b.items() if not t.startswith("not ")))
        # A new negated significance statement is still a significance claim; a new causal or certainty
        # negation needs a source only when it replaces an unnegated claim.
        must = name in MUST_CONFIRM_INCREASE and (
            added_claim or removed_negation or (added_negation and (name == "significance" or unnegated_fell)))
        result["must_confirm" if must else "review"].append(line)
    association = result["terms"].get("association", {})
    if "direction" in rose and sum(y for x, y in association.values()) < sum(x for x, y in association.values()):
        result["must_confirm"].append("association wording fell while effect or direction wording rose: "
                                      "check for a causal upgrade")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("--json", action="store_true", help="Print the full comparison as JSON.")
    args = parser.parse_args(argv)
    try:
        before, after = (p.read_text(encoding="utf-8-sig") for p in (args.before, args.after))
    except (OSError, UnicodeError) as exc:
        parser.error(f"cannot read input: {exc}")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    result = compare(before, after)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Revision comparison: {args.before} -> {args.after}")
        for heading, key in (("Must confirm against sources", "must_confirm"), ("Review", "review")):
            if result[key]:
                print(heading + ":")
                print("\n".join("  " + line for line in result[key]))
        if not result["must_confirm"] and not result["review"]:
            print("No listed differences." + (" The text changed; read the changed passages." if before != after else ""))
    return 1 if result["must_confirm"] else 0


if __name__ == "__main__":
    sys.exit(main())
