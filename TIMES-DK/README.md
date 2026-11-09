# TIMES-DK

Source: [energy-modelling-club/TIMES-DK_COMETS](https://github.com/energy-modelling-club/TIMES-DK_COMETS) @ `a73b903`

Licence: GPL-3.0 (`LICENSE`).

## Attribution

TIMES-DK, the version of the COMETS project (energy-modelling-club/TIMES-DK_COMETS), licensed under the GNU General Public License v3.0.

## The case folders

Each run file is the repository's `SCENARIO.RUN` with the DD files that `scenarios/<case>.sc` lists, as `runmodel.gms --comets_scenario=<case>` puts it together; the DD files are those of `model/`, unchanged. `cplex.opt` is the repository's.

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

- The run files `TIMES-DK_COMETS_<case>.run` are assembled as above (the repository builds them at run time).

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| Frozen_policy_scenarie | 2 | 866,874 | 1,030,869 | 4,739,595 | 2268102.0846363986 | 2268102.0888631083 (1.9e-9) | Optimal, IPX + crossover, 2268102.0897291396 (2.2e-9) | `python TIMES.py run TIMES-DK/Frozen_policy_scenarie --solver ipx --highs-option run_crossover=on` |
| CB_20 | 2 | 866,875 | 1,030,870 | 4,827,622 | 2065814.349626841 | 2065814.3483820618 (6.0e-10) | Optimal, IPX + crossover, 2065814.3498800097 (1.2e-10) | `python TIMES.py run TIMES-DK/CB_20 --solver ipx --highs-option run_crossover=on` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
