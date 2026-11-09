# TIMES-OS models

Public TIMES models with their inputs as [TIMES-OS](https://github.com/kanors-emr/TIMES-OS) runs them, and the result TIMES v4.9.8 in GAMS gives for each. Anyone can build every case with TIMES-OS, without TIMES in GAMS, and compare the result with the one published beside it (`expected.json`). The cases up to 1 million rows solve with HiGHS (section 2); the larger ones were solved with CPLEX (`--lp cplex`) and need a solver of that strength.

Every model is under its own licence; see its folder. The rest of the repository is under CC BY 4.0 ([LICENSE](LICENSE)).

## 1. Same matrix, same optimum, comparable speed

On every case below, TIMES-OS 1.0.0 builds **the same matrix** as TIMES v4.9.8 in GAMS (rows and columns matched by name and labels, each in both; every coefficient equal within a relative difference of 1e-9 (plus 1e-12 absolute), an explicit zero on both sides counting as equal; every right-hand side and bound equal by the same rule, a right-hand side made of constants that cancel equal within 64 machine epsilons of their size), and CPLEX finds **the same objective value** on both, within the solver's tolerance: a relative difference of at most **2e-9** where CPLEX ends with crossover, and **2e-6** where the model's own option file stops the barrier without crossover (JRC-EU-TIMES JRC_BAU, PET-VTT EUnetzero, JRC-EU-TIMES JRC_NetZero; marked †). These differences are the solver's: CPLEX receives the same linear program from both, with its rows and columns in another order, and stops within its own tolerance; they are not a difference between TIMES-OS and TIMES in GAMS, which the matrix shows to be none.

Each case folder holds the reports of both runs: `report_<case>_matrix.txt`, of the run that compared the matrix with that of TIMES in GAMS (CONVERT's jacobian) entry by entry, by equation, and `report_<case>.txt`, of the run that compares with `expected.json` without TIMES in GAMS, as anyone can repeat it (solved by HiGHS, or above 1 million rows by CPLEX, `--lp cplex`).

It builds models of up to 1 million rows in at most 33 seconds (TIMES in GAMS: up to 27 seconds) and 4.2x the peak memory of TIMES in GAMS, and larger ones in at most 1.3x the time and 3.4x the peak memory; the three largest, of 6.73, 7.12 and 8.22 million rows, in less time than TIMES in GAMS.

| Model | Case | Rows | Columns | Non-zeros | Objective value | Time P/G | Peak memory P/G |
|---|---|--:|--:|--:|--:|--:|--:|
| TIMES_Demo | demo12 | 3.23 k | 4.49 k | 18.4 k | 23,960,685.7370 | 8.3 s / 0.4 s ‡ | 799 MB ‡ |
| TIMES_Demo | demo12Base | 3.71 k | 4.32 k | 19.7 k | 24,004,967.4436 | 8.1 s / 0.3 s ‡ | 799 MB ‡ |
| TIMES_Demo | demo12MLF-BaseRep | 4.26 k | 44.8 k | 142 k | 27,263.0598 * | 11 s / 0.2 s ‡ | 1.17 GB ‡ |
| TIMES_Demo | demo12MLF-PolicyEx | 4.27 k | 44.8 k | 142 k | 27,198.5703 * | 10 s / 0.2 s ‡ | 1.17 GB ‡ |
| OTNYC | s1_nyc_ref | 237 k | 557 k | 1.87 M | 9,657,725.87257 | 20 s / 7.2 s ‡ | 3.09 |
| OTCGEN | gc_ref | 512 k | 766 k | 5.62 M | 756,404,387.820 | 32 s / 27 s ‡ | 4.18 |
| TIMES-NZ | steady-v308 | 622 k | 523 k | 3.41 M | 1,333,686.04070 | 17 s / 6.8 s ‡ | 2.85 |
| TIMES-NZ | shift-v308 | 631 k | 529 k | 3.63 M | 1,286,960.50578 | 17 s / 6.9 s ‡ | 2.73 |
| TIMES-DK | Frozen_policy_scenarie | 867 k | 1.03 M | 4.74 M | 2,268,102.08464 | 22 s / 9.2 s ‡ | 3.30 |
| TIMES-DK | CB_20 | 867 k | 1.03 M | 4.83 M | 2,065,814.34963 | 24 s / 10 s ‡ | 3.06 |
| OTUS9r | reference | 1.03 M | 1.65 M | 7.19 M | 192,206,507,156 | 1.23 | 3.35 |
| OTUS9r | tax1_wo_mou | 1.20 M | 1.92 M | 8.40 M | 212,593,238,100 | 1.19 | 3.40 |
| JRC-EU-TIMES | JRC_BAU | 5.02 M | 6.91 M | 32.6 M | 47,007,789.7070 † | 1.04 | 2.95 |
| PET-VTT | EUnetzero | 5.51 M | 7.14 M | 36.6 M | 1,680,687,191.34 † | 1.05 | 3.13 |
| JRC-EU-TIMES | JRC_NetZero | 6.73 M | 9.27 M | 46.1 M | 54,575,398.0513 † | 0.96 | 2.76 |
| ON-TIMES | Base | 7.12 M | 13.7 M | 60.4 M | 791,981,747.411 | 0.75 | 1.89 |
| ON-TIMES | CNN_CCS | 8.22 M | 15.8 M | 72.3 M | 792,224,036.780 | 0.67 | 2.06 |

The objective value is that of TIMES in GAMS solved by CPLEX, to 12 significant digits. Each case's `expected.json` holds both objectives at full precision and their relative difference.

\* MACRO MLF: TIMES in GAMS solves these with CONOPT, and its listing gives the objective to 4 decimals; TIMES-OS (HiGHS) agrees within them.

† The model's `cplex.opt` stops the barrier without crossover, so the two objectives agree to the barrier's tolerance.

P/G: TIMES-OS divided by TIMES in GAMS v4.9.8, both measured in the same run on the same machine, from the start to the matrix built. Peak memory: TIMES-OS's peak working set (its processes, sampled every 0.5 s) divided by the peak memory TIMES in GAMS reports in its listing.

‡ Where TIMES in GAMS takes under 30 s to the matrix: the two times (TIMES-OS / TIMES in GAMS) instead of their ratio, as TIMES-OS's start-up (a few seconds) dominates such short runs and a ratio would mislead; likewise the peak memory under 100 k rows is TIMES-OS's own.

## 2. With an open solver only (HiGHS)

| Model | Case | Rows | HiGHS status | Relative difference from CPLEX | Method | HiGHS solve time | CPLEX solve time | H/C |
|---|---|--:|---|--:|---|--:|--:|--:|
| TIMES_Demo | demo12 | 3.23 k | Optimal | 2.0e-14 | simplex | 0.1 s | 0.1 s | – § |
| TIMES_Demo | demo12Base | 3.71 k | Optimal | 3.1e-16 | simplex | 0.1 s | 0.1 s | – § |
| TIMES_Demo | demo12MLF-BaseRep | 4.26 k | Optimal | 2.3e-10 | simplex | 6.0 s | – (CONOPT) * | – |
| TIMES_Demo | demo12MLF-PolicyEx | 4.27 k | Optimal | 4.6e-10 | simplex | 7.3 s | – (CONOPT) * | – |
| OTNYC | s1_nyc_ref | 237 k | Optimal | 7.0e-9 | IPX | 52 s | 6.4 s | – § |
| OTCGEN | gc_ref | 512 k | Optimal | 2.1e-6 | IPX | 87 s | 24 s | – § |
| TIMES-NZ | steady-v308 | 622 k | Optimal | 9.2e-9 | IPX + crossover | 445 s | 63 s | 7.0 |
| TIMES-NZ | shift-v308 | 631 k | Optimal | 3.5e-10 | IPX + crossover | 585 s | 80 s | 7.3 |
| TIMES-DK | Frozen_policy_scenarie | 867 k | Optimal | 2.2e-9 | IPX + crossover | 767 s | 126 s | 6.1 |
| TIMES-DK | CB_20 | 867 k | Optimal | 1.2e-10 | IPX + crossover | 931 s | 145 s | 6.4 |
| OTUS9r | reference | 1.03 M | not attempted (over 1 M rows) | | | | 209 s | |
| OTUS9r | tax1_wo_mou | 1.20 M | not attempted (over 1 M rows) | | | | 542 s | |
| JRC-EU-TIMES | JRC_BAU | 5.02 M | not attempted (over 1 M rows) | | | | 460 s | |
| PET-VTT | EUnetzero | 5.51 M | not attempted (over 1 M rows) | | | | 1,291 s | |
| JRC-EU-TIMES | JRC_NetZero | 6.73 M | not attempted (over 1 M rows) | | | | 1,202 s | |
| ON-TIMES | Base | 7.12 M | not attempted (over 1 M rows) | | | | 4,348 s | |
| ON-TIMES | CNN_CCS | 8.22 M | not attempted (over 1 M rows) | | | | 10,907 s | |

H/C: HiGHS's solve time divided by CPLEX's, on the same linear program and the same machine. HiGHS: the attempt that ended optimal (the attempts before it are not counted). CPLEX 22.1.2.0, with the model's own `cplex.opt`, its solve time as TIMES v4.9.8 in GAMS reports it.

§ Where CPLEX solves in under 30 s, the two times only: a ratio of such short solves would mislead.

HiGHS 1.15.1, 24 threads, a 6-hour limit per attempt. Each case was tried with HiGHS's default first; where that did not end optimal, with HiPO, then with IPX and crossover (`--solver ipx --highs-option run_crossover=on`); the method shown is the one that did. Each case's README gives the command. Intel Core i7-13700 (16 cores, 24 threads), 64 GB, Windows 11. Times are indicative.

## 3. Check it yourself

Without TIMES in GAMS: install [TIMES-OS](https://github.com/kanors-emr/TIMES-OS#readme), then run a case folder with the command its README gives (above 1 million rows that command solves with CPLEX, `--lp cplex`, which needs GAMS with a CPLEX licence), for example

    python TIMES.py run <path to>/TIMES_Demo/demo12

TIMES-OS finds `expected.json` in the folder and compares its result with it. The first line of `runs/<case>/report_<case>.txt` is the verdict; compare its objective with the table above.

With GAMS: `--jacobian <file>.gdx` writes TIMES-OS's matrix in the format of GAMS CONVERT's jacobian file; run the same folder through TIMES in GAMS with CONVERT and compare the two with `python times_pp/tools/compare_jacobian.py <TIMES-OS file>.gdx <GAMS file>.gdx`, as the [TIMES-OS verification guide](https://github.com/kanors-emr/TIMES-OS/blob/main/docs/verification.md#comparing-with-times-in-gams-yourself) describes.

## 4. The models

| Model | Source | Licence | Cases |
|---|---|---|---|
| [TIMES_Demo](TIMES_Demo/) | [etsap-TIMES/TIMES_Demo](https://github.com/etsap-TIMES/TIMES_Demo) @ `962db86` | CC BY 4.0 | `demo12`, `demo12Base`, `demo12MLF-BaseRep`, `demo12MLF-PolicyEx` |
| [OTNYC](OTNYC/) | [esma-ie/OTNYC](https://github.com/esma-ie/OTNYC) @ `bc1d276` | CC BY-SA 4.0 | `s1_nyc_ref` |
| [OTCGEN](OTCGEN/) | [esma-ie/OTCGEN](https://github.com/esma-ie/OTCGEN) @ `08af95f` | CC BY-SA 4.0 | `gc_ref` |
| [TIMES-NZ](TIMES-NZ/) | [EECA-NZ/TIMES-NZ-Model-Files](https://github.com/EECA-NZ/TIMES-NZ-Model-Files) @ `8165e1d` (TIMES-NZ 3.0.8) | MIT | `steady-v308`, `shift-v308` |
| [TIMES-DK](TIMES-DK/) | [energy-modelling-club/TIMES-DK_COMETS](https://github.com/energy-modelling-club/TIMES-DK_COMETS) @ `a73b903` | GPL-3.0 | `Frozen_policy_scenarie`, `CB_20` |
| [OTUS9r](OTUS9r/) | [esma-ie/OTUS9r](https://github.com/esma-ie/OTUS9r) @ `598e179` | CC BY-SA 4.0 | `reference`, `tax1_wo_mou` |
| [JRC-EU-TIMES](JRC-EU-TIMES/) | [KanORS-E4SMA/EU_TIMES_Veda2.0](https://github.com/KanORS-E4SMA/EU_TIMES_Veda2.0) @ `f6cddee` (model files; `db64778` adds the licence) | CC BY 4.0 | `JRC_BAU`, `JRC_NetZero` |
| [PET-VTT](PET-VTT/) | [vttresearch/petvtt](https://github.com/vttresearch/petvtt) @ `349b664` (PET-VTT v1.0, [doi:10.5281/zenodo.18183015](https://doi.org/10.5281/zenodo.18183015)) | CC BY 4.0 | `EUnetzero` |
| [ON-TIMES](ON-TIMES/) | [NordicEnergyResearch/NCES2020](https://github.com/NordicEnergyResearch/NCES2020), branch `ON-TIMES` @ `5571f82` (tag `v1.final`) | ODbL 1.0 | `Base`, `CNN_CCS` |

Each folder holds its own LICENSE, attribution and any changes; the root [LICENSE](LICENSE) does not cover the models.

## 5. Notes

- **MACRO MLF** (`demo12MLF-BaseRep`, `demo12MLF-PolicyEx`): the case ships `conopt.opt` with `Tol_Optimality 1.e-12`, which TIMES in GAMS uses for the MLF calibration. With CONOPT's default tolerance the two matrices differ by up to 1.5e-9.
- The MLF cases read the base prices of a reference run (`TIMESED YES`), as in TIMES: run `TIMES_Demo/demo12Base` first (TIMES-OS writes its base prices into that folder), then the MLF case with `--points TIMES_Demo/demo12Base`. TIMES in GAMS reads them from `com_bprice.gdx`, which the case ships.
- Every case is solved with its own shipped option files (`cplex.opt`, `conopt.opt`), as it is published here.
- JRC-EU-TIMES JRC_BAU, PET-VTT EUnetzero, JRC-EU-TIMES JRC_NetZero: their `cplex.opt` solves by barrier without crossover, so their objectives agree to the barrier's tolerance (†).
- The cases over 1 M rows are run with `--lp cplex` (TIMES-OS's matrix solved by CPLEX through your own GAMS); HiGHS was not attempted on them.
