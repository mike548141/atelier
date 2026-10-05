- [x] 🔎 **Two blocking guards never scan a staged file whose path git quotes**
      `[S][tools]`. Found 2026-10-05 by the worker that fixed `260/120`.
      `conflictscan` and `leakscan` read the staged plane from
      `git diff --cached --unified=0`, taking each file name from lines that
      start `+++ b/`. For a path with a non-ASCII byte, git's default
      `core.quotePath` writes `+++ "b/caf\303\251/x"`, which does not
      start `+++ b/`. So that file's added lines are never scanned, for
      conflict markers or for personal data: a silent miss at the hook.
      `secretscan` already passes `-c core.quotePath=false`. That covers
      non-ASCII, but a path containing a tab or a quote is still quoted.
      `board.py` and `harvestscan.py` split `ls-files`/`ls-tree` output on
      lines, so a quoted path is mis-parsed. That costs index and
      harvest-count correctness, not a publish gate.
      **The work:** read every staged-plane path unquoted in the guards that
      parse git's path output: `-z`, or `core.quotePath=false` plus correct
      unquoting for the diff headers. Test each with a quoted path, and
      prove the output byte-identical on a tree without one.

      ✅ **Fixed and merged 2026-10-05** (queue run, a Sonnet 5.5 worker;
      `4dfaf8d`, after a first attempt stalled with nothing committed).
      `report.py` gains three shared readers: `unquote_c` (git's C-quoting),
      `diff_header_path` (accepts only `+++ b/…` and `+++ "b/…"`, and strips
      the trailing tab git adds to a name with a space), and `nul_paths`.
      `conflictscan` and `leakscan` now pass `-c core.quotePath=false` and
      read headers through the shared reader. `secretscan` uses it too, so a
      name with a tab, quote or backslash is reported clean. `board.py`'s
      staged `ls-files` and `harvestscan`'s `ls-files`/`ls-tree` read `-z`.
      **Evidence:** output was byte-identical on atelier's tree (10 of 10
      commands), on a scratch clone's staged plane with real board and harvest
      output (5 of 5), and in all 29 sibling repos (0 changed, 0 newly
      failing). There are 9 helper tests plus a quoted-path test per guard;
      they fail on the old code (27 subtests) and pass now. The full suite
      passed (1,837) and Node 411. The orchestrator re-ran the touched modules
      on the merged tree (193 OK). One deliberate side effect: a spaced path's
      findings in `conflictscan`/`leakscan` now print without git's trailing
      tab, as `secretscan`'s already did. Code pass queued at `160/760`. A
      related header-parsing hole is filed as `280`.
