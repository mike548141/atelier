- [x] **CI floor restored to green — DELIVERED 2026-07-26** (`eac5581` +
  `908de1d`, inline Opus, found during a close-out check). The pushed floor had
  been **red since `6749202` (2026-07-25 13:16)** — ~19 hours, 20+ consecutive
  failing runs, across several sessions — while every session's *local* scan
  reported 9/9 green. Two stacked failures, the first masking the second.
  **(1)** `floor.py --json` violated its own documented contract (`run()`:
  *"stdout carries nothing but the JSON document"*) by printing Actions
  `::group::`/`::error::` markers to stdout unconditionally, so a caller parsing
  `--json` from inside a workflow hit `JSONDecodeError` on line 1 — that caller
  being our own `test_missing_records_tree_skips_visibly`. **The failure was
  environment-gated, not logic-gated:** `GITHUB_ACTIONS` is never set on a dev
  machine, so the suite was green locally and red only in CI, the one place
  nobody re-runs by hand. Fixed by routing the markers to `child_stdout` (stderr
  under `--json`, stdout otherwise); both workflows invoke floor.py *without*
  `--json`, so grouping still renders where it is consumed. New
  `test_json_stdout_stays_pure_inside_actions` pins `GITHUB_ACTIONS=true` for the
  subprocess so the contract is tested where it breaks; suite 660 → 661, green
  under both conditions. **(2)** With the pipeline unblocked, a never-reached
  step ran and failed: `mandoc -T lint` on an 81-byte line in `ccrepo.1`, from
  the same session's context-column work — verified locally with `man -P cat`
  (which *renders*) rather than `mandoc -T lint` (which *checks*, and isn't
  installed locally). Rewrapped. Floor at head green. **Standing gap flagged:**
  no local equivalent of the mandoc gate exists on this machine.
