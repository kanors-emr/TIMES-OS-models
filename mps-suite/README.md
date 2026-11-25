# MPS files of 15 cases, for solver testing

*Instructions for an AI coding agent (or a person). Input: one local folder, called `ROOT` below. Everything else is
fixed.*

These steps write 15 of the 17 cases of this repository as MPS files, one linear program per case, each with its
reference optimum. They start from cloning, with TIMES-OS and `make_mps.py` (in this folder).

Tested from a clean clone on Windows 11 (25 November 2026, TIMES-OS `60149c4`, this repository at `f164f0d`):

- The setup took 10 minutes.
- The 10 cases up to 1.2 M rows took 8.5 minutes, and every row count matched the table.
- `OTNYC__s1_nyc_ref.mps` solved with HiGHS to 9,657,725.8726, against a reference of 9,657,725.87257.
- The five large cases use the same command. Their test is still to be run.

## What you will end up with

```
ROOT/
  TIMES-OS/            the TIMES-OS model generator (https://github.com/kanors-emr/TIMES-OS), set up
  TIMES-OS-models/     17 cases of 9 open TIMES models, 15 used (https://github.com/kanors-emr/TIMES-OS-models)
  runs/                TIMES-OS's run folders and one log per case (can be deleted afterwards)
  mps/
    <Model>__<case>.mps   15 LPs, as TIMES-OS hands them to HiGHS
    manifest.csv          file, model, case, rows, columns, non-zeros, reference objective, seconds
```

Each MPS file is the linear program of one case, exactly as HiGHS receives it from TIMES-OS. HiGHS writes it with its
own `write_model_file` option. Rows and columns are unnamed (`r0`, `c0`, ...), and the objective is minimised.
TIMES-OS builds the same matrix as TIMES in GAMS for each case, coefficient by coefficient. So
`reference_objective` in the manifest, which is the optimum TIMES v4.9.8 in GAMS found with CPLEX, is the optimum of
the MPS file.

| Model | Case | Rows | Non-zeros | Reference objective |
|---|---|--:|--:|--:|
| TIMES_Demo | demo12 | 3.23 k | 18.4 k | 23,960,685.7370 |
| TIMES_Demo | demo12Base | 3.71 k | 19.7 k | 24,004,967.4436 |
| OTNYC | s1_nyc_ref | 237 k | 1.87 M | 9,657,725.87257 |
| OTCGEN | gc_ref | 512 k | 5.62 M | 756,404,387.820 |
| TIMES-NZ | steady-v308 | 622 k | 3.41 M | 1,333,686.04070 |
| TIMES-NZ | shift-v308 | 631 k | 3.63 M | 1,286,960.50578 |
| TIMES-DK | Frozen_policy_scenarie | 867 k | 4.74 M | 2,268,102.08464 |
| TIMES-DK | CB_20 | 867 k | 4.83 M | 2,065,814.34963 |
| OTUS9r | reference | 1.03 M | 7.19 M | 192,206,507,156 |
| OTUS9r | tax1_wo_mou | 1.20 M | 8.40 M | 212,593,238,100 |
| JRC-EU-TIMES | JRC_BAU | 5.02 M | 32.6 M | 47,007,789.7070 |
| PET-VTT | EUnetzero | 5.51 M | 36.6 M | 1,680,687,191.34 |
| JRC-EU-TIMES | JRC_NetZero | 6.73 M | 46.1 M | 54,575,398.0513 |
| ON-TIMES | Base | 7.12 M | 60.4 M | 791,981,747.411 |
| ON-TIMES | CNN_CCS | 8.22 M | 72.3 M | 792,224,036.780 |

The full-precision objectives are in each case's `expected.json` (key `objective`) and in the manifest. With CPLEX,
TIMES-OS's LP and the GAMS LP agree within 2e-9 relative. On JRC_BAU, EUnetzero and JRC_NetZero the model's own
`cplex.opt` stops the barrier without crossover, so for those three use 2e-6. HiGHS 1.15.1's results on the cases up to
0.9 M rows are in this repository's README, section 2.

## Requirements

- Windows 10/11 or Linux, x86-64, with `git` and **Python 3.11 or newer** on the PATH (`python --version`; on Linux
  use `python3` wherever `python` appears below). TIMES-OS's setup installs everything else, Julia included.
- Internet access for the clones and the setup.
- **Memory.** The 10 cases up to 1.2 M rows need at most 9 GB. The five large ones need 35 to 55 GB at their peak
  (JRC_BAU 34 GB, EUnetzero 41, JRC_NetZero 43, ON-TIMES Base 48, CNN_CCS 53), so a 64 GB machine that runs nothing
  else. With less memory, make the 10 smaller ones only (step 5).
- **Disk.** About 25 GB: the models clone 0.8 GB, TIMES-OS with its Julia packages a few GB, the MPS files about
  11 GB (gc_ref about 0.2 GB, OTUS9r reference 0.27 GB, ON-TIMES CNN_CCS about 2.7 GB), and the run folders.
- **Time.** The setup takes 10 to 15 minutes the first time. The cases up to 1.2 M rows take a minute or two each, and
  the five large ones several minutes each.

## Steps

Run every command from `ROOT`, unless a step says otherwise. Replace `ROOT` with the folder you were given. Create it
if it does not exist.

### 1. Clone both repositories

```
cd ROOT
git clone https://github.com/kanors-emr/TIMES-OS
git clone https://github.com/kanors-emr/TIMES-OS-models
```

The models repository is about 0.8 GB. Its `.gitattributes` keeps every file byte for byte, so do not change git's
line-ending settings for it.

### 2. Set up TIMES-OS

```
cd ROOT/TIMES-OS
python TIMES.py setup
```

This installs Julia if there is no Julia 1.11 or newer (on Windows through winget, otherwise as a portable copy). It
installs the Python packages into `TIMES-OS/.venv` and the Julia packages into `TIMES-OS/.julia_depot`, compiles the
Julia code, and solves the example model.

- **Success:** the last lines say `Setup is complete`, and the exit code is 0.
- **Failure:** read the message. It names what is missing. Do not install Julia packages by hand.

### 3. Check TIMES-OS on the smallest case

```
cd ROOT/TIMES-OS
python TIMES.py run ../TIMES-OS-models/TIMES_Demo/demo12 --out ../runs
```

The command exits with code 0. The first line of `ROOT/runs/demo12/report_demo12.txt` must read
`VERDICT  SAME OBJECTIVE`: TIMES-OS found the case's `expected.json` and its objective agrees with it.

### 4. The driver script

The script is `ROOT/TIMES-OS-models/mps-suite/make_mps.py`. It needs nothing beyond Python's standard library.

What it does, for each case, is to run

```
python TIMES.py run <case folder> --out ROOT/runs --quiet --solve
    --highs-option write_model_to_file=true --highs-option write_model_file=ROOT/mps/<Model>__<case>.mps
    --time-limit 1
```

from `ROOT/TIMES-OS`.

- HiGHS writes the LP it receives before it starts solving.
- `--time-limit 1` then stops the solve, so TIMES-OS reports each case as `NOT SOLVED: ... TIME_LIMIT` and exits
  with code 1. This is expected; only the MPS file matters.
- `--solve` makes TIMES-OS hand cases above 2 million rows to HiGHS as well (by default it only builds them).
- Every case is one LP: built, written, solved once. The models repository also has two TIMES-MACRO cases
  (`demo12MLF-BaseRep`, `demo12MLF-PolicyEx`). They solve a sequence of LPs to calibrate, so they are left out.
- The script uses the Python it is started with. TIMES-OS's runner switches to its own `.venv` by itself.

### 5. Write the MPS files

All 15 cases, which needs 64 GB of memory (see Requirements):

```
cd ROOT
python TIMES-OS-models/mps-suite/make_mps.py ROOT
```

Only the 10 cases up to 1.2 M rows:

```
python TIMES-OS-models/mps-suite/make_mps.py ROOT --only TIMES_Demo/demo12,TIMES_Demo/demo12Base,OTNYC/s1_nyc_ref,OTCGEN/gc_ref,TIMES-NZ/steady-v308,TIMES-NZ/shift-v308,TIMES-DK/Frozen_policy_scenarie,TIMES-DK/CB_20,OTUS9r/reference,OTUS9r/tax1_wo_mou
```

- The script prints one line per case: its rows, columns, non-zeros, size and seconds.
- It skips a case whose MPS is already in the manifest, so after an interruption it can simply be run again.
  `--force` rewrites them.
- It exits with code 1 and lists the cases that gave no MPS. Each case's TIMES-OS output is in
  `ROOT/runs/<Model>__<case>.log`, and its report is in `ROOT/runs/<case>/report_<case>.txt`.

### 6. Check the result

- `ROOT/mps/manifest.csv` has 15 rows (or 10).
- The rows in the manifest match the Rows column of the table above, to the three digits shown. The non-zeros can
  be a few percent lower than the table's: the table counts the matrix of TIMES in GAMS, and the MPS file leaves out
  entries HiGHS holds as zero.
- Optional: solve `TIMES_Demo__demo12.mps` with any LP solver. The optimum must be 23960685.737 (relative difference
  below 1e-9).

The run folders in `ROOT/runs` can be deleted once the manifest is complete. They are not needed to use the MPS files.

## For a test suite

- Use the MPS files as they are. Their objective is `reference_objective` in the manifest. As acceptance, a relative
  difference of at most 1e-6 is safe for all 15 cases.
- If MPS files are not to be stored, the same files can be made again at any time from the same commits of the two
  repositories. Record them with `git -C ROOT/TIMES-OS rev-parse HEAD` and `git -C ROOT/TIMES-OS-models rev-parse HEAD`.
- The models are under their own licences (CC BY 4.0, CC BY-SA 4.0, MIT, GPL-3.0, ODbL 1.0). Each model's folder in
  TIMES-OS-models gives its licence and attribution, and these apply to the MPS files made from it.
