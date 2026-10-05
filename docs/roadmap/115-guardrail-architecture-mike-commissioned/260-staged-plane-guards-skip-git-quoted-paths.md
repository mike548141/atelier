- [~] 🔎 **Two blocking guards never scan a staged file whose path git quotes** (claimed 2026-10-05-1858, wt: atelier-qr-115-260)
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
