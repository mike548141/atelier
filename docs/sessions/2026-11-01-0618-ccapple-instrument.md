# 2026-11-01 · 0618 UTC — `ccapple`, a read-only reader for the Apple apps' stores

**Session:** worker, Claude Sonnet 5.5, in the worktree `atelier-ccapple` (branch
`ccapple-instrument`, from `origin/main`). The primary checkout held another session's
uncommitted work and was not touched.

**The brief.** The principal approved admitting a read-only search tool for the Apple
apps' local stores as a new instrument. Build it to atelier's conventions, public-grade,
with tests, a man page and the index entries; open a PR; do not merge.

## What was done

- **The instrument:** `instruments/ccapple` (stdlib Python), `instruments/test_ccapple.py`
  (119 `unittest` cases on synthetic stores), `instruments/man/ccapple.1` (lints clean
  under `mandoc -T lint`).
- **Safety properties kept and re-pinned:** read-only immutable opens through one function
  with `query_only`, a required filter plus a cap on every search, locked notes never read,
  and the Home reader's column allowlist with the sentinel-value and no-wildcard tests.
  Two new process-level tests run the script under an empty `HOME`, so no real store can be
  reached by the suite. Another asserts that every flag any `--help` prints is in the page.
- **Changed from the tool as first written** (to match the layer): the command and its
  messages are `ccapple`; `--since`/`--until` also take `YYYYMMDD`, the spelling `ccrepo`
  and `cctranscript` use; the top-level `--help` points at `man ccapple`; every example,
  fixture and comment is generic and fictional.
- **Wiring:** a row and a flag-table column in `instruments/README.md`, the indexscan
  `maps` directive taught to skip `test_*.py`, a CI step for the Python tests, an addendum
  to ADR 0006, a CHANGELOG entry. `instruments/install` needed no entry: it links every
  executable file and every `man/*.1` page by glob, and the test file is not executable.
- **Board:** `210/340`, a small defect found while testing (a no-filter run on a Mac that
  lacks the store exits 1, not 2). Not fixed in this change.

## Left for the next session

- Review of the PR; nothing here has had a cold pass.
- `210/340`.
- The tool was exercised on Python 3.9 and 3.14 only; the 3.8 floor it states is by reading
  the syntax it uses, not by a run.
