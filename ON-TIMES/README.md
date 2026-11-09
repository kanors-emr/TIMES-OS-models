# ON-TIMES

Source: [NordicEnergyResearch/NCES2020](https://github.com/NordicEnergyResearch/NCES2020), branch `ON-TIMES` @ `5571f82` (tag `v1.final`)

Licence: ODbL 1.0 (`LICENSE`).

## Attribution

ON-TIMES v1.final, Nordic Energy Research (EML, IVL, VTT), ODbL 1.0. This folder is a derived database of ON-TIMES and is made available under the Open Database License 1.0 (share alike).

## The case folders

The DD files and run files were written by Veda 2.0 from the repository (cases `Base` and `CNN_CCS`).

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| Base | 10 | 7,115,906 | 13,730,551 | 60,410,644 | 791981747.4106092 | 791981747.410609 (3.0e-16) | not attempted (over 1 M rows) | `python TIMES.py run ON-TIMES/Base --lp cplex` |
| CNN_CCS | 10 | 8,222,634 | 15,757,960 | 72,253,471 | 792224036.7800869 | 792224036.7800869 (0.0e0) | not attempted (over 1 M rows) | `python TIMES.py run ON-TIMES/CNN_CCS --lp cplex` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
