"""Build a source-linked report from numerical exports, with no author code access."""
import csv
import html
import json
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "outputs/war-discourse-reproduction"
LABELS = {"lms": "HXZ long-short", "single": "HXZ single sorts", "cz_decile": "CZ single sorts",
          "tree": "Tree portfolios", "anomalies": "Own anomalies", "nonlinear": "Own nonlinear"}


def read_rows(name):
    with (OUT / name).open(newline="") as stream:
        return list(csv.DictReader(stream))


def number(x, digits=2):
    return f"{float(x):,.{digits}f}"


def table(headers, rows):
    def cell(x):
        return html.escape(str(x))
    return '<div class="scroll"><table><thead><tr>' + ''.join(f'<th>{cell(h)}</th>' for h in headers) + \
        '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{cell(v)}</td>' for v in row) + '</tr>'
                                      for row in rows) + '</tbody></table></div>'


def comparisons(data, control, loadings, industries, targets):
    result = []

    def add(tab, asset, model, metric, actual, target, decimals, variant, pages):
        tolerance = 0 if decimals is None else 0.5 * 10 ** -decimals
        actual = float(actual)
        result.append(dict(table=tab, assets=asset, model=model, metric=metric, variant=variant,
                           reproduced=actual, published=target, difference=actual-target,
                           tolerance=tolerance, matched=abs(actual-target) <= tolerance + 1e-10,
                           source_pdf_pages=pages))

    lookup = {(r["table"], r["assets"], r["model"], r["variant"], r["term"]): r for r in data + control}
    for variant in ("published_series", "supplied_factor_control"):
        for asset, target in targets["table_II"].items():
            for i, model in enumerate(targets["models"]):
                r = lookup[("II", asset, model, variant, "Intercept")]
                for key, metric, scale, decimals in (
                    ("estimate", "intercept", 100, 2), ("t", "intercept_t", 1, 2),
                    ("r2", "r2", 100, 0), ("adjusted_r2", "adjusted_r2", 100, 0),
                    ("mape", "mape", 100, 2)):
                    target_key = "r2" if metric == "adjusted_r2" else metric
                    add("II", asset, model, metric, float(r[key])*scale, target[target_key][i], decimals,
                        variant, target["pages"])
                for key in ("N", "T"):
                    add("II", asset, model, key, r[key], target[key], None, variant, target["pages"])
            for i, model in enumerate(targets["war_models"]):
                r = lookup[("II", asset, model, variant, "WarFac")]
                add("II", asset, model, "war_lambda", float(r["estimate"])*100, target["war_lambda"][i],
                    2, variant, target["pages"])
                add("II", asset, model, "war_t", r["t"], target["war_t"][i], 2, variant, target["pages"])
    for i, asset in enumerate(targets["table_I_war"]["assets"]):
        target = targets["table_I_war"]
        r = next(r for r in loadings if r["assets"] == asset and r["factor"] == "WarFac" and
                 r["variant"] == "published_series")
        for key, scale, decimals in (("lambda", 100, 2), ("t", 1, 2),
                                      ("average_abs_beta_t", 1, 2), ("significant_betas", 1, None)):
            add("I", asset, "War", key, float(r[key])*scale, target[key][i], decimals,
                "published_series", target["pages"])
    target = targets["table_IV_all"]
    for i, asset in enumerate(target["assets"]):
        r = lookup[("IV", asset, "All", "published_series", "WarFac")]
        for key, source, scale, decimals in (("lambda", "estimate", 100, 2), ("t", "t", 1, 2)):
            add("IV", asset, "All", key, float(r[source])*scale, target[key][i], decimals,
                "published_series", target["pages"])
        add("IV", asset, "All", "T", r["T"], target["T"], None, "published_series", target["pages"])
    for target in targets["table_V"]:
        r = next(r for r in industries if r["assets"] == target["assets"] and
                 r["model"] == target["model"] and r["variant"] == "published_series" and
                 r["term"] == "WarFac" and r["hac_lag"] == "6")
        for key, source, scale in (("lambda", "estimate", 100), ("t", "t", 1)):
            add("V", target["assets"], target["model"], key, float(r[source])*scale, target[key], 2,
                "published_series", "37-38")
    return result


def main():
    summary = json.loads((OUT / "run_summary.json").read_text())
    checks = json.loads((OUT / "checks/hard_checks.json").read_text())
    if summary["status"] != "succeeded" or not all(c["passed"] for c in checks):
        raise RuntimeError("A completed checked analysis is required before report generation.")
    targets = json.loads((HERE / "published_targets.json").read_text())
    data = read_rows("tables/two_pass_results.csv")
    control = read_rows("tables/supplied_factor_control.csv")
    loadings = read_rows("tables/table_I_loadings.csv")
    industries = read_rows("tables/table_V_industries.csv")
    compared = comparisons(data, control, loadings, industries, targets)
    with (OUT / "tables/publication_comparison.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(compared[0]))
        writer.writeheader()
        writer.writerows(compared)
    grouped = defaultdict(list)
    for r in compared:
        grouped[(r["table"], r["variant"], r["metric"])].append(r)
    comparison_summary = [dict(table=tab, variant=variant, metric=metric,
                               matched=sum(r["matched"] for r in rows), total=len(rows),
                               max_absolute_difference=max(abs(r["difference"]) for r in rows))
                          for (tab, variant, metric), rows in grouped.items()]
    (OUT / "comparison_summary.json").write_text(json.dumps(comparison_summary, indent=2))

    headlines = []
    for i, asset in enumerate(targets["table_I_war"]["assets"]):
        values = []
        for variant in ("calendar", "observed", "published_series"):
            r = next(r for r in data if r["table"] == "II" and r["model"] == "War" and
                     r["term"] == "WarFac" and r["assets"] == asset and r["variant"] == variant)
            values.append(f'{number(100*float(r["estimate"]))} ({number(r["t"])})')
        target = targets["table_I_war"]
        headlines.append([LABELS[asset]] + values + [f'{target["lambda"][i]:.2f} ({target["t"][i]:.2f})',
                                                    r["N"], r["T"]])
    result_table = table(["Test assets", "War_base / calendar", "War_base / observed",
                          "War_main / observed (post hoc)", "Published", "N", "T (observed)"], headlines)
    agreement = table(["Table", "Track", "Metric", "Within published rounding", "Largest difference"],
                      [[r["table"], r["variant"], r["metric"], f'{r["matched"]}/{r["total"]}',
                        number(r["max_absolute_difference"], 4)] for r in comparison_summary])
    unmatched = [r for r in compared if not r["matched"]]
    difference_table = table(["Table", "Assets", "Model", "Track", "Metric", "Reproduced", "Published", "Difference"],
                             [[r["table"], r["assets"], r["model"], r["variant"], r["metric"],
                               number(r["reproduced"], 5), r["published"], number(r["difference"], 5)] for r in unmatched])
    flow = read_rows("tables/sample_flow.csv")
    flow_table = table(["Assets", "Candidate columns", "Retained", "Excluded", "Observed input months"],
                       [[LABELS[r["assets"]], r["candidates"], r["retained"], r["excluded"],
                         r["months_before_factor_matching"]] for r in flow])
    beta_diagnostics = read_rows("tables/first_pass_inference_diagnostics.csv")
    beta_table = table(["Assets", "Diagnostic covariance", "Average |beta t|", "|beta t| > 1.65", "Published average / count"],
                       [[LABELS[r["assets"]], r["inference"], number(r["average_abs_beta_t"]),
                         r["significant_betas"],
                         f'{targets["table_I_war"]["average_abs_beta_t"][targets["table_I_war"]["assets"].index(r["assets"])]:.2f} / '
                         f'{targets["table_I_war"]["significant_betas"][targets["table_I_war"]["assets"].index(r["assets"])]}']
                        for r in beta_diagnostics])
    industry_table = table(["Industries", "Controls", "Index / lag track", "War premium (pp)", "t (HAC 6)", "T", "N range"],
                           [[r["assets"], r["model"], r["variant"], number(100*float(r["estimate"])), number(r["t"]),
                             r["T"], r["N_min"] + "–" + r["N_max"]] for r in industries if
                            r["term"] == "WarFac" and r["hac_lag"] == "6"])
    appendix_counts = defaultdict(set)
    for r in data:
        appendix_counts[r["table"]].add((r["assets"], r["model"], r["variant"]))
    coverage = [
        ["Main Tables I–II", "Independent downstream reproduction", "Full-sample OLS betas; cross-sectional OLS; explicit Shanken covariance. All six supplied test-asset sets. Published comparisons cover War in I and four main sets in II."],
        ["Main Table III / Appendix C", "Estimated with supplied portfolio inputs", "Tree-based cross-sectional WMP; mean, Sharpe and HAC spanning; time-series WMP alternatives. Full-sample weights are retrospective."],
        ["Main Table IV", "Estimated on a common comparison sample", "War / NVIX / GPR and joint model; every column shares factor availability through March 2016."],
        ["Main Table V", "Independent implementation; discrepancies retained", "60-month lagged betas, crisis-beta quintiles, monthly cross sections and HAC lags 0/3/6/12; asset-specific eligibility."],
        ["Appendix D / E", "Selected available comparisons", "Tail-beta portfolio controls, alternative narrative factors, topic controls, sample/AR starts, positive/negative innovations and supplied index variants. ARMA robustness is not implemented."],
        ["Appendix F", "Decomposition diagnostic", "Campbell-style VAR identity checked for 11 explicit predictor specifications; missing precise predictor mapping prevents a claim of exact published reconstruction."],
        ["Appendix H.2", "Conditional downstream calculation", "WMP with supplied MKT/MOM selection. H.1 screening / complete three-pass inference are not reproduced."],
        ["Seeded LDA, stock-level sorts, Appendix G", "Blocked upstream stages", "Full news corpus, stock characteristics/capitalizations/delistings and article-level topic weights are absent. Supplied levels/returns remain inputs."],
    ]
    coverage_table = table(["Stage", "Status", "Scope"], coverage)
    crosswalk = [
        ["paper.pdf", "11", "War topic average 9.71%; source-level mapping"],
        ["paper.pdf", "14–15, equations 1–4", "Full-sample two-pass pricing and AR innovation construction"],
        ["paper.pdf", "20–29", "Table I loadings and Table II published targets"],
        ["paper.pdf", "30–36", "Competing traded-factor and uncertainty-factor comparisons"],
        ["paper.pdf", "37–38, equations 5–6", "Industry rolling-beta Fama–MacBeth"],
        ["paper.pdf", "39–41, equations 7–9", "Cross-sectional and time-series WMP; FF30 uses its available long history"],
        ["appendix.pdf", "Sections A, C–F, H, J", "Text construction details and selected robustness / factor-selection tests"],
    ]
    with (OUT / "tables/source_crosswalk.csv").open("w", newline="") as stream:
        writer = csv.writer(stream); writer.writerow(["source", "pdf_page_or_section", "use"]); writer.writerows(crosswalk)
    source_table = table(["Source", "PDF pages / section", "Implementation link"], crosswalk)
    # Generated links are relative so the report can be moved with its output directory.
    paper = quote('../../examples/war-discourse/The Journal of Finance - 2025 - HIRSHLEIFER - War Discourse and the Cross Section of Expected Stock Returns.pdf')
    appendix = quote('../../examples/war-discourse/War_Discourse_CS_IA.pdf')
    file_links = ''.join(f'<li><a href="{quote(path)}">{html.escape(label)}</a></li>' for path, label in [
        ("tables/two_pass_results.csv", "All independent two-pass estimates"),
        ("tables/publication_comparison.csv", "Every manually transcribed target and numerical comparison"),
        ("tables/table_V_industries.csv", "Industry results and HAC sensitivities"),
        ("tables/first_pass_inference_diagnostics.csv", "First-pass covariance diagnostics"),
        ("tables/supplied_factor_control.csv", "Supplied-factor control, explicitly separate"),
        ("tables/appendix_F_VAR.csv", "VAR decomposition diagnostics"),
        ("checks/hard_checks.json", "Hard output checks"),
        ("checks/data_comparison.csv", "Input membership and innovation comparisons"),
        ("checks/raw_input_hashes.csv", "Original input fingerprints"),
        ("checks/source_hashes.json", "Analysis source fingerprints"),
        ("session_info.txt", "Runtime and package versions"),
        ("run.log", "Estimation and synthetic-check log"),
        ("diagnostics.log", "Post-implementation diagnostic log"),
        ("input_access.txt", "Data-only access log"),
        ("fitted_results.rds", "Fitted numerical objects"),
        ("industry_monthly_slopes.rds", "Actual industry cross-sectional slope paths"),
        ("figures/war_premia.eps", "Vector figure (EPS)"),
    ])
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>War discourse | Independent reproduction</title><style>
:root{{--ink:#173641;--muted:#55717b;--line:#d5e1e4;--paper:#fff;--accent:#14556b}}
*{{box-sizing:border-box}}body{{margin:0;background:#eef3f2;color:var(--ink);font:16px/1.65 system-ui,sans-serif}}
main{{max-width:1200px;margin:36px auto;padding:44px;background:var(--paper);border-top:6px solid var(--accent)}}
h1{{font-size:36px;line-height:1.2;margin:8px 0 16px}}h2{{margin-top:38px;font-size:23px}}p{{max-width:1000px}}
.eyebrow{{color:var(--muted);font-size:13px;letter-spacing:.12em;text-transform:uppercase}}
.note{{background:#edf4f5;padding:16px 20px;border-left:4px solid var(--accent)}}
.stats{{display:flex;flex-wrap:wrap;gap:14px;margin:24px 0}}.stat{{background:#f3f6f5;padding:14px 22px;min-width:200px}}
.stat strong{{display:block;font-size:25px}}.stat span{{color:var(--muted);font-size:13px}}
.scroll{{overflow-x:auto;margin:18px 0}}table{{border-collapse:collapse;width:100%;font-size:13px;line-height:1.45}}
th,td{{text-align:left;padding:10px;border-bottom:1px solid var(--line);vertical-align:top}}th{{background:#edf3f3;white-space:nowrap}}
tr:nth-child(even) td{{background:#fafcfc}}a{{color:#12647b}}img{{max-width:100%;height:auto}}code{{font-size:13px;background:#edf3f3;padding:3px 6px}}
details{{border:1px solid var(--line);padding:14px;margin:18px 0}}summary{{cursor:pointer;font-weight:600}}li{{margin:7px 0}}
.muted{{color:var(--muted);font-size:14px}}@media(max-width:700px){{main{{margin:0;padding:22px}}h1{{font-size:29px}}}}
</style></head><body><main>
<div class="eyebrow">FinEconHarness · Paper-first empirical example</div>
<h1>War discourse and expected returns</h1>
<p>Hirshleifer, Mai and Pukthuanthong (2025), <em>The Journal of Finance</em>.
<a href="https://doi.org/10.1111/jofi.13482">DOI 10.1111/jofi.13482</a>.</p>
<div class="note"><strong>Result:</strong> independently reconstructed AR innovations and two-pass estimators recover negative War premia in all six supplied test-asset sets. The War_main / observed-lag track is closest to the published pricing estimates. Index identity, first-pass inference and industry implementation retain unresolved differences.</div>
<div class="stats"><div class="stat"><strong>{summary['two_pass_models']:,}</strong><span>independent two-pass fitted models</span></div>
<div class="stat"><strong>{summary['numerical_rows']:,}</strong><span>exported coefficient rows</span></div>
<div class="stat"><strong>{len(checks)} passed</strong><span>hard output / integrity checks</span></div></div>
<p class="muted">These counts describe calculation coverage; they do not establish publication agreement. The example is a complete runnable downstream task, not a reproduction of every page of the paper and appendix.</p>
<h2>Source boundary and independent choices</h2>
<p>The paper and appendix supplied the econometric logic. Author programs, .Rhistory and author output workbooks were not read. The runner permits only named data files inside the input directory, including post-implementation intermediate-factor diagnostics. The access log enforces the runner boundary; it cannot prove an agent's entire browsing history.</p>
<p>War_base was chosen before pricing estimation because its 1871–2019 mean is 9.7101%, matching the paper's reported 9.71%; War_main averages 8.7233%. A predeclared all-index sensitivity later identified closer published numerical correspondence for War_main. That post hoc track is labelled separately throughout. Filename and numerical correspondence do not establish seed-word provenance.</p>
<p>The expanding AR(1) begins in January 1926, uses at least 12 eligible pairs and parameters estimated through the current month. Both lag and response must fall inside the start window. Expanding length, minimum history and initialization are implementation assumptions because the text does not fully specify them. A prior-month-parameters sensitivity is also exported. Full-sample betas and a constant enter the cross-sectional OLS. Shanken inference includes the factor-covariance term, uses T divisors and normal reference probabilities.</p>
<h2>Main War premium</h2><p>Monthly percentage points; t statistics in parentheses. All observed-lag tracks use 532 months. Calendar matching uses 531. Confidence intervals below are pointwise 95% Shanken intervals.</p>
{result_table}<img src="figures/war_premia.png" alt="War premium estimates under three explicit index and date conventions">
<h2>Sample reconstruction and input dependencies</h2>
<p>The calendar span July 1972–December 2016 contains 534 months. The supplied original portfolio panels already omit September and October 1978, leaving 532 observed months. The news index has the same gap. A calendar lag also loses November 1978; an observed-row lag bridges the gap. Return columns were screened for complete coverage before factor matching, independently recovering the supplied retained membership.</p>
{flow_table}
<p>Portfolio returns, factor returns and topic-index levels are supplied inputs. The full 6.8-million-article corpus and stock characteristics, market capitalizations and delisting data are absent. Seeded LDA and stock-level portfolio formation therefore cannot be rebuilt here. Supplied returns keep their original decimal units; generic column names do not establish excess-return provenance, and no second risk-free subtraction is imposed.</p>
<h2>Published agreement and retained differences</h2>
<p>Targets were manually transcribed from the paper after implementation. A cell matches if its absolute difference is within half its last displayed unit; N and T must match exactly. No mismatch is automatically classified as a program bug. Raw and adjusted R² are compared separately against the paper's single R² row. The supplied-factor control substitutes supplied War_main_AR1 only after the independent estimates and is a diagnostic of upstream versus estimator differences.</p>
<p>The reported Table II R² values generally correspond more closely to adjusted R² than to the raw fit definition. Table I beta-significance summaries differ under ordinary OLS; the supplied-factor Newey–West lag-6 diagnostic rounds to all six published average |t| values and five of six significant-beta counts. This correspondence is evidence about a possible inference convention, not proof of the author's setting. HC0 and Newey–West alternatives remain diagnostics. Industry estimates are sensitive to beta timing, missing-month windows, eligibility, rank ties and HAC bandwidth; all chosen conventions remain explicit.</p>
<details open><summary>Agreement counts by metric</summary>{agreement}</details>
<details><summary>All {len(unmatched)} cells outside published rounding</summary>{difference_table}</details>
<details><summary>First-pass inference diagnostics (supplied-factor control only)</summary>{beta_table}</details>
<details><summary>Industry premiums; HAC lag 6 shown, other bandwidths in CSV</summary>{industry_table}</details>
<h2>Coverage and limits</h2>{coverage_table}
<p>Full-sample cross-sectional and time-series mimicking weights use information from the evaluation period. These are retrospective pricing exercises. The available H.2 calculation does not validate H.1 factor screening or a complete three-pass standard-error procedure. The VAR output verifies the decomposition identity under explicitly chosen supplied predictors; it is not labelled an exact Appendix F table match.</p>
<h2>Harness changes driven by this run</h2>
<ul><li>Added a paper-first workflow and data-only boundary before code-reading instructions; preserved an explicit distinction between independent implementation and author-code audit.</li>
<li>Added a two-pass pricing guide separating full-sample Shanken tests from rolling-beta Fama–MacBeth. Raw and adjusted R², actual N/T and return units remain in exports.</li>
<li>Added provenance, calendar gaps, intermediate-input dependency and generated-factor timing guidance to sample checks.</li>
<li>Specified HAC prewhitening, finite-sample adjustment and lag units; calendar gaps use zero estimating scores on absent dates, not imputed zero returns.</li>
<li>Fixed per-asset rolling-window eligibility, pre-start AR lag leakage, inconsistent Table IV comparison samples, access-log whitespace that invalidated hashes and stale success status. Targeted synthetic and end-to-end checks cover these fixes.</li>
<li>Used installed base R QR/OLS, sandwich, testthat and ggplot2. Tested the actual PNG/EPS export path after SVG capability detection proved insufficient.</li></ul>
<h2>Reuse from the local repository collection</h2>
<p>The supplied repository-review workbook guided a narrow review of cran__sandwich and yhoriuchi__replication-package-guide. The useful patterns were an established covariance backend, explicit Newey–West options, one entry point, an immutable input directory, execution logs and session metadata. No third-party source was vendored. Broader repository reading was unnecessary for this estimator.</p>
<p>Shanken inference reference: <a href="https://doi.org/10.1093/rfs/5.1.1">Shanken (1992)</a>. The unconditional additive factor-covariance convention is also discussed in <a href="https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/08-16.Schwarz2.pdf">the Appendix C.2 research treatment</a>. The chosen covariance formula and dense-matrix synthetic equivalence check are saved in the implementation.</p>
<h2>Sources and reproducibility</h2>
<p><a href="{paper}">Original paper PDF</a> · <a href="{appendix}">Internet appendix PDF</a>. Pointers below use PDF pages, not printed journal page numbers.</p>{source_table}
<p>From the repository root: <code>python3 harness/examples/war-discourse/run_all.py</code>. Requires Rscript and sandwich, jsonlite, ggplot2, testthat; Python uses its standard library. The entry point reruns estimation, diagnostics, checks and this report, then marks task success. A failed run clears prior success; retained files must be interpreted with task_status.json.</p>
<ul>{file_links}</ul><p class="muted">Original data hashes were verified unchanged. Source hashes and package/session versions identify this run. Research example only; all result claims are conditional on the supplied input data.</p>
</main></body></html>'''
    (OUT / "report.html").write_text(document)
    print(f"Wrote report and {len(compared)} publication comparisons ({len(unmatched)} outside rounding).")


if __name__ == "__main__":
    main()
