- [x] 🔎 **`ccfleet drive` keys "already done today" on the job's label
      alone, so a jobs file that reuses one label runs one job and skips the
      rest.** Found 2026-11-20 by session 19378351. A 17-repo jobs file gave
      every line the label `board-1120`; the first job wrote
      `results/<date>/board-1120.md`, and the driver then logged `skip …
      (result exists for 2026-11-20)` for fifteen others and exited, with no
      warning at load time. The doc's sentence ("a job whose result file for
      today already exists is skipped") is true but does not say the key is
      the label, and the skill's step 4 (`repo<TAB>label<TAB>…`) reads as if
      the label were a run name shared by the batch. Second, smaller: a second
      `drive` on the same `kit_dir` is refused (`another driver … is
      running`), which is right, but nothing in `--help` says so.
      **Shape:** key the result file on repo and label (or refuse a jobs file
      whose labels repeat, at load, before anything starts); say both rules
      in `--doc` and in `skills/fleet-sweep/SKILL.md` step 4.
      ✅ **Done 2026-11-23** (queue run c7a1e36e, with `210/470`): `ccfleet
      drive` refuses, at load and before anything starts, a jobs file whose
      labels repeat, naming the label and its lines; "one driver per
      kit_dir" is in `--help`, `--doc` and the man page; the fleet-sweep
      skill's steps 4 and 5 say both. One drive now writes one day's results
      folder (`--day` resumes a drive begun before UTC midnight). Test:
      `test_a_jobs_file_whose_labels_repeat…` in `instruments/test_ccfleet.py`.
