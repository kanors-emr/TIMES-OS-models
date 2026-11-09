# TIMES_Demo

Source: [etsap-TIMES/TIMES_Demo](https://github.com/etsap-TIMES/TIMES_Demo) @ `962db86`

Licence: CC BY 4.0 (`LICENSE`).

## Attribution

TIMES_Demo, (c) 2000-2023 IEA Energy Technology Systems Analysis Programme (ETSAP), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

## The case folders

`demo12` is the repository's `model/` folder; `demo12Base` and the two MLF cases are from `model-ge/`. Each case folder holds the DD files its run file reads.

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

- `demo12MLF-BaseRep/` and `demo12MLF-PolicyEx/`: added `com_bprice.gdx`, the base prices of `demo12Base` written by TIMES v4.9.8 in GAMS (CPLEX), which the MLF cases read, and `conopt.opt` with `Tol_Optimality 1.e-12` (see the notes of the root README).

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| demo12 | 2 | 3,233 | 4,485 | 18,375 | 23960685.737007417 | 23960685.737007767 (1.5e-14) | Optimal, simplex, 23960685.737007905 (2.0e-14) | `python TIMES.py run TIMES_Demo/demo12` |
| demo12Base | 2 | 3,714 | 4,324 | 19,662 | 24004967.443633266 | 24004967.443633262 (1.6e-16) | Optimal, simplex, 24004967.443633273 (3.1e-16) | `python TIMES.py run TIMES_Demo/demo12Base` |
| demo12MLF-BaseRep | 2 | 4,256 | 44,796 | 142,117 | 27,263.0598 (CONOPT) | - | Optimal, simplex, 27263.059793677756 (2.3e-10) | `python TIMES.py run TIMES_Demo/demo12MLF-BaseRep --points TIMES_Demo/demo12Base` |
| demo12MLF-PolicyEx | 2 | 4,270 | 44,808 | 142,213 | 27,198.5703 (CONOPT) | - | Optimal, simplex, 27198.57031263454 (4.6e-10) | `python TIMES.py run TIMES_Demo/demo12MLF-PolicyEx --points TIMES_Demo/demo12Base` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).

The MLF cases read the base prices of a reference run (`TIMESED YES`): run `demo12Base` first; TIMES-OS writes its base prices (`com_bprice.parquet`) into that folder, and `--points TIMES_Demo/demo12Base` tells the MLF case where they are.
