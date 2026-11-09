# TIMES-NZ

Source: [EECA-NZ/TIMES-NZ-Model-Files](https://github.com/EECA-NZ/TIMES-NZ-Model-Files) @ `8165e1d` (TIMES-NZ 3.0.8)

Licence: MIT (`LICENSE`).

## Attribution

TIMES-NZ 3.0.8, Energy Efficiency and Conservation Authority (EECA), BusinessNZ Energy Council and Paul Scherrer Institut; Copyright (c) 2024 Energy Efficiency and Conservation Authority, MIT licence.

## The case folders

The DD files and run files were written by Veda 2.0 from the repository's model files (scenarios `steady` and `shift` of version 3.0.8).

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| steady-v308 | 2 | 622,043 | 523,095 | 3,414,768 | 1333686.0406999006 | 1333686.0404737373 (1.7e-10) | Optimal, IPX + crossover, 1333686.0529837294 (9.2e-9) | `python TIMES.py run TIMES-NZ/steady-v308 --solver ipx --highs-option run_crossover=on` |
| shift-v308 | 2 | 630,987 | 529,483 | 3,631,870 | 1286960.5057784112 | 1286960.5061724158 (3.1e-10) | Optimal, IPX + crossover, 1286960.506233816 (3.5e-10) | `python TIMES.py run TIMES-NZ/shift-v308 --solver ipx --highs-option run_crossover=on` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
