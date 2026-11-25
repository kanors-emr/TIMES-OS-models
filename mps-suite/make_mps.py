#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Write 15 open TIMES reference cases of TIMES-OS-models as MPS files, with TIMES-OS.

    python TIMES-OS-models/mps-suite/make_mps.py <ROOT> [--only <Model/case>,...] [--force]

<ROOT> holds TIMES-OS/ (set up: `python TIMES.py setup`) and TIMES-OS-models/ (cloned). Writes
<ROOT>/mps/<Model>__<case>.mps, one per case, and <ROOT>/mps/manifest.csv (file, rows, columns, non-zeros, reference
objective). The run folders of TIMES-OS go to <ROOT>/runs/. A case whose MPS exists is skipped unless --force.

How: TIMES-OS builds each case and hands it to HiGHS; HiGHS's own options write_model_to_file / write_model_file
write the LP it receives, before it solves; a time limit of 1 s then stops the solve, so TIMES-OS reports the case
NOT SOLVED (TIME_LIMIT): that is expected. The repository's two MACRO MLF cases (demo12MLF-*) are left out: they
solve a sequence of LPs, not one. --solve makes TIMES-OS hand the cases above 2 million rows to HiGHS as well.
"""
import csv, json, os, subprocess, sys, time

CASES = [  # model, case
    ("TIMES_Demo", "demo12"),
    ("TIMES_Demo", "demo12Base"),
    ("OTNYC", "s1_nyc_ref"),
    ("OTCGEN", "gc_ref"),
    ("TIMES-NZ", "steady-v308"),
    ("TIMES-NZ", "shift-v308"),
    ("TIMES-DK", "Frozen_policy_scenarie"),
    ("TIMES-DK", "CB_20"),
    ("OTUS9r", "reference"),
    ("OTUS9r", "tax1_wo_mou"),
    ("JRC-EU-TIMES", "JRC_BAU"),
    ("PET-VTT", "EUnetzero"),
    ("JRC-EU-TIMES", "JRC_NetZero"),
    ("ON-TIMES", "Base"),
    ("ON-TIMES", "CNN_CCS"),
]


def mps_size(path):
    """Rows (without the objective), columns and non-zeros (objective included) of a fixed or free MPS file."""
    rows, cols, nz, sec, last = 0, 0, 0, "", None
    with open(path, "r", encoding="ascii", errors="replace") as f:
        for line in f:
            if not line.strip():
                continue
            if not line[0].isspace():
                sec = line.split()[0]
                continue
            t = line.split()
            if sec == "ROWS":
                rows += t[0] != "N"
            elif sec == "COLUMNS":
                if len(t) > 1 and t[1] == "'MARKER'":
                    continue
                if t[0] != last:
                    cols, last = cols + 1, t[0]
                nz += (len(t) - 1) // 2
    return rows, cols, nz


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        sys.exit(__doc__)
    root = os.path.abspath(a[0])
    only = set(a[a.index("--only") + 1].split(",")) if "--only" in a else None
    force = "--force" in a
    tos, models = os.path.join(root, "TIMES-OS"), os.path.join(root, "TIMES-OS-models")
    out, runs = os.path.join(root, "mps"), os.path.join(root, "runs")
    for p in (os.path.join(tos, "TIMES.py"), models):
        if not os.path.exists(p):
            sys.exit(f"not found: {p}")
    os.makedirs(out, exist_ok=True)
    os.makedirs(runs, exist_ok=True)
    manifest = os.path.join(out, "manifest.csv")
    done = {}
    if os.path.exists(manifest):
        with open(manifest, newline="") as f:
            done = {r["file"]: r for r in csv.DictReader(f)}
    failed = []
    for model, case in CASES:
        key = f"{model}/{case}"
        if only and key not in only:
            continue
        name = f"{model}__{case}.mps"
        mps = os.path.join(out, name)
        ref = json.load(open(os.path.join(models, model, case, "expected.json")))["objective"]
        if os.path.exists(mps) and not force and name in done:
            print(f"{key}: {name} exists, skipped", flush=True)
            continue
        if os.path.exists(mps):
            os.remove(mps)
        cmd = [sys.executable, "TIMES.py", "run", os.path.join(models, model, case), "--out", runs, "--quiet",
               "--solve", "--time-limit", "1", "--highs-option", "write_model_to_file=true",
               "--highs-option", "write_model_file=" + mps.replace("\\", "/")]
        t0 = time.time()
        print(f"{key}: building ...", flush=True)
        with open(os.path.join(runs, f"{model}__{case}.log"), "w") as log:
            rc = subprocess.call(cmd, cwd=tos, stdout=log, stderr=subprocess.STDOUT)
        if not os.path.exists(mps) or os.path.getsize(mps) == 0:
            failed.append(key)
            print(f"{key}: NO MPS (exit code {rc}); see {os.path.join(runs, model + '__' + case + '.log')}", flush=True)
            continue
        r, c, n = mps_size(mps)
        done[name] = {"file": name, "model": model, "case": case, "rows": r, "columns": c, "nonzeros": n,
                      "reference_objective": repr(ref), "seconds": round(time.time() - t0)}
        print(f"{key}: {name}, {r:,} rows, {c:,} columns, {n:,} non-zeros, {os.path.getsize(mps) / 2**20:,.0f} MB, "
              f"{time.time() - t0:,.0f} s", flush=True)
        with open(manifest, "w", newline="") as f:
            w = csv.DictWriter(f, ["file", "model", "case", "rows", "columns", "nonzeros", "reference_objective", "seconds"])
            w.writeheader()
            for m_, c_ in CASES:
                k = f"{m_}__{c_}.mps"
                if k in done:
                    w.writerow(done[k])
    print(f"\n{len(done)} MPS files in {out}; manifest: {manifest}")
    if failed:
        print("FAILED: " + ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
