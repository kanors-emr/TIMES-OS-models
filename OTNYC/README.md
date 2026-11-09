# OTNYC

Source: [esma-ie/OTNYC](https://github.com/esma-ie/OTNYC) @ `bc1d276`

Licence: CC BY-SA 4.0 (`LICENSE`).

## Attribution

OTNYC, Energy Systems Modelling Analytics Ltd (ESMA), based on the original COMET-NYC model by the US EPA Office of Research and Development; licensed under CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). OTNYC is not developed, maintained, reviewed or endorsed by the US EPA; its results are not US EPA results.

## The case folders

The case folder is the repository's GAMS-ready export `dd/s1_nyc_ref/`.

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| s1_nyc_ref | 7 | 236,650 | 557,258 | 1,870,931 | 9657725.872571386 | 9657725.872571386 (0.0e0) | Optimal, IPX, 9657725.93999427 (7.0e-9) | `python TIMES.py run OTNYC/s1_nyc_ref` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
