"""Hard checks of actual outputs, separate from publication agreement."""
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "outputs/war-discourse-reproduction"


def rows(name):
    with (OUT / name).open(newline="") as f:
        return list(csv.DictReader(f))


def verify():
    checks = []

    def check(name, passed, detail=""):
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    summary = json.loads((OUT / "run_summary.json").read_text())
    check("analysis_run_succeeded", summary.get("status") == "succeeded")
    data = rows("tables/two_pass_results.csv")
    expected_n = {"lms": 138, "single": 1372, "cz_decile": 904, "tree": 360,
                  "anomalies": 128, "nonlinear": 2190}
    check("all_exports_have_valid_numeric_inference", all(
        float(r["se"]) > 0 and math.isfinite(float(r["estimate"])) and
        math.isclose(float(r["t"]), float(r["estimate"]) / float(r["se"]), rel_tol=1e-9, abs_tol=1e-9) and
        math.isclose(float(r["p"]), math.erfc(abs(float(r["t"])) / math.sqrt(2)), rel_tol=1e-8, abs_tol=1e-12)
        for r in data), f"{len(data)} exported coefficient rows")
    check("portfolio_counts_reconstructed_from_original_panels", all(
        int(r["N"]) == expected_n[r["assets"]] for r in data))
    check("calendar_and_observation_lags_keep_distinct_sample_sizes", all(
        int(r["T"]) == (531 if r["variant"] == "calendar" else 532)
        for r in data if r["table"] == "II"))
    # Regression for a real bug: NVIX availability originally changed only its own column.
    for asset in expected_n:
        for variant in ("calendar", "observed", "published_series"):
            sample_sizes = {int(r["T"]) for r in data if r["table"] == "IV" and
                            r["assets"] == asset and r["variant"] == variant}
            check(f"table_IV_common_sample/{asset}/{variant}", len(sample_sizes) == 1,
                  str(sorted(sample_sizes)))
    for r in rows("checks/raw_input_hashes.csv"):
        path = Path(r["path"])
        digest = hashlib.md5(path.read_bytes()).hexdigest()
        check("raw_input_unchanged/" + path.name, digest == r["md5"])
    source_hashes = json.loads((OUT / "checks/source_hashes.json").read_text())
    for name, digest in source_hashes.items():
        check("analysis_source_current/" + name, hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest)
    for name in ("figures/war_premia.png", "figures/war_premia.eps", "fitted_results.rds",
                 "industry_monthly_slopes.rds", "tables/supplied_factor_control.csv"):
        check("output_present/" + name, (OUT / name).is_file() and (OUT / name).stat().st_size > 500)
    (OUT / "checks/hard_checks.json").write_text(json.dumps(checks, indent=2))
    failed = [c["check"] for c in checks if not c["passed"]]
    if failed:
        raise AssertionError("Failed checks: " + ", ".join(failed))
    return checks


if __name__ == "__main__":
    checked = verify()
    print(f"Passed {len(checked)} hard output checks.")
