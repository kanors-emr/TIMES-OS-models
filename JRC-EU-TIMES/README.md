# JRC-EU-TIMES

Source: [KanORS-E4SMA/EU_TIMES_Veda2.0](https://github.com/KanORS-E4SMA/EU_TIMES_Veda2.0) @ `f6cddee` (model files; `db64778` adds the licence)

Licence: CC BY 4.0 (`LICENSE`).

## Attribution

JRC-EU-TIMES, Joint Research Centre of the European Commission, (c) European Union 1995-2019, CC BY 4.0, https://data.jrc.ec.europa.eu/collection/id-00287; adapted for Veda 2.0 by KanORS-EMR and E4SMA.

## The case folders

The DD files and run files were written by Veda 2.0 from the repository (cases `JRC_BAU` and `JRC_NetZero`).

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| JRC_BAU | 31 | 5,020,690 | 6,906,431 | 32,573,112 | 47007789.70698354 | 47007789.01267955 (1.5e-8) | not attempted (over 1 M rows) | `python TIMES.py run JRC-EU-TIMES/JRC_BAU --lp cplex` |
| JRC_NetZero | 31 | 6,726,874 | 9,268,646 | 46,052,173 | 54575398.051270396 | 54575422.85990532 (4.5e-7) | not attempted (over 1 M rows) | `python TIMES.py run JRC-EU-TIMES/JRC_NetZero --lp cplex` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
