# OTUS9r

Source: [esma-ie/OTUS9r](https://github.com/esma-ie/OTUS9r) @ `598e179`

Licence: CC BY-SA 4.0 (`LICENSE`).

## Attribution

OTUS9r, Energy Systems Modelling Analytics Ltd (ESMA), based on the original EPAUS9rT database by the US EPA Office of Research and Development; licensed under CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). OTUS9r is not developed, maintained, reviewed or endorsed by the US EPA; its results are not US EPA results.

## The case folders

The case folders are the repository's GAMS-ready export `dd/reference/` and `dd/tax1_wo_mou/`.

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| reference | 10 | 1,028,923 | 1,647,278 | 7,186,412 | 192206507156.18262 | 192206507156.18256 (3.2e-16) | not attempted (over 1 M rows) | `python TIMES.py run OTUS9r/reference --lp cplex` |
| tax1_wo_mou | 10 | 1,199,533 | 1,922,664 | 8,402,583 | 212593238099.785 | 212593237937.44806 (7.6e-10) | not attempted (over 1 M rows) | `python TIMES.py run OTUS9r/tax1_wo_mou --lp cplex` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
