# PET-VTT

Source: [vttresearch/petvtt](https://github.com/vttresearch/petvtt) @ `349b664` (PET-VTT v1.0, [doi:10.5281/zenodo.18183015](https://doi.org/10.5281/zenodo.18183015))

Licence: CC BY 4.0 (`LICENSE`). `LICENSE` is the CC BY 4.0 legal code, the licence the repository's `license.txt` names.

## Attribution

PET-VTT v1.0, VTT Technical Research Centre of Finland Ltd, CC BY 4.0, based on JRC-EU-TIMES (c) European Union 1995-2019, CC BY 4.0. Citation: Mehnert J, Lehtilä A, Kellomäki J, Koponen K, Rämä M, Lindroos T, Koljonen T. Pan-European TIMES-VTT Energy system model. Release PET-VTT v1.0, https://doi.org/10.5281/zenodo.18183015

## The case folders

The DD files and run file were written by Veda 2.0 from the repository (case `EUnetzero`, 37 regions).

Each case folder holds the run file, the DD files it reads, the solver option files, and `expected.json`: the result of TIMES v4.9.8 in GAMS that TIMES-OS compares with, and the evidence (the matrix check, both CPLEX objectives, HiGHS), and the reports of TIMES-OS's two runs: `report_<case>_matrix.txt`, the matrix compared with that of TIMES in GAMS entry by entry, and `report_<case>.txt`, the run against `expected.json` without TIMES in GAMS (solved by HiGHS, or by CPLEX where the command has `--lp cplex`).

## Changes

None: the files are as the source gives them.

## Cases

| Case | Regions | Rows | Columns | Non-zeros | TIMES in GAMS (CPLEX) | TIMES-OS (CPLEX) | HiGHS | Command |
|---|--:|--:|--:|--:|--:|--:|---|---|
| EUnetzero | 31 | 5,507,746 | 7,137,957 | 36,603,806 | 1680687191.3365524 | 1680689228.5738263 (1.2e-6) | not attempted (over 1 M rows) | `python TIMES.py run PET-VTT/EUnetzero --lp cplex --tolerance 2e-6` |

Relative differences in brackets are from the objective of TIMES in GAMS. The matrix is the same as that of TIMES in GAMS on every case (the rule: see the root README; each case's `report_<case>_matrix.txt` gives the comparison by equation).
