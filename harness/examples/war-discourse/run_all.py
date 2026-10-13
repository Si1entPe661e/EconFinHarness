#!/usr/bin/env python3
"""One entry point: independent estimation, diagnostics, checks and report."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "outputs/war-discourse-reproduction"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "checks").mkdir(exist_ok=True)
    subprocess.run([sys.executable, str(HERE / "check_runner.py")], cwd=ROOT, check=True)
    source_paths = sorted(HERE.glob("*.R")) + sorted(HERE.glob("*.py")) + sorted(HERE.glob("*.json"))
    fingerprints = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
    (OUT / "checks/source_hashes.json").write_text(json.dumps(fingerprints, indent=2))
    print("Running independent estimates and synthetic checks.", flush=True)
    with (OUT / "run.log").open("w") as log:
        subprocess.run(["Rscript", str(HERE / "run.R")], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    print("Running explicitly labelled supplied-factor diagnostics.", flush=True)
    with (OUT / "diagnostics.log").open("w") as log:
        subprocess.run(["Rscript", str(HERE / "diagnostics.R")], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    subprocess.run([sys.executable, str(ROOT / "harness/checks/check_paper_first.py")], cwd=ROOT, check=True)
    from verify_outputs import verify
    checked = verify()
    print(f"Passed {len(checked)} hard output checks.", flush=True)
    subprocess.run([sys.executable, str(HERE / "build_report.py")], cwd=ROOT, check=True)
    print("Finished:", OUT / "report.html", flush=True)


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "task_status.json").write_text(json.dumps({"status": "running"}, indent=2))
    try:
        main()
    except BaseException as error:
        (OUT / "task_status.json").write_text(json.dumps({"status": "failed", "error": str(error)}, indent=2))
        raise
    else:
        (OUT / "task_status.json").write_text(json.dumps({"status": "succeeded"}, indent=2))


if __name__ == "__main__":
    run()
