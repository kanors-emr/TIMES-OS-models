# OTCGEN

Source: [esma-ie/OTCGEN](https://github.com/esma-ie/OTCGEN) @ `08af95f`

Licence: CC BY-SA 4.0 (`LICENSE`).

## Attribution

OTCGEN, Energy Systems Modelling Analytics Ltd (ESMA), based on the original Generative COMET model by the US EPA Office of Research and Development; licensed under CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). OTCGEN is not developed, maintained, reviewed or endorsed by the US EPA; its results are not US EPA results.

## The case folders

The case folder is the repository's GAMS-ready export `dd/gc_ref/`.

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| gc_ref | 2 | 512,182 | 765,953 | 5,622,500 | 756404387.8201399 | 756404387.8201396 (3.2e-16) | Optimal, IPX, 756405975.8766135 (2.1e-6) | `python TIMES.py run OTCGEN/gc_ref --tolerance 3e-6` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
