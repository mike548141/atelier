- [x] 🔎 **publishscan's default and staged planes miss any path git quotes**
      `[S][tools]`. Found 2026-10-05 by the worker that built `--history`
      (`110`). The tip plane reads `git ls-files` and the staged plane reads
      `git diff --name-only`, both without `-z`. With git's default
      `core.quotePath`, a path with a non-ASCII byte comes back C-quoted:
      `café/.env` arrives as `"caf\303\251/.env"`, and no never-publish
      pattern matches it. Confirmed on a fixture: the default scan missed a
      tracked never-publish file under a non-ASCII directory, and
      `--history`, which reads with `-z`, found it. It is a silent miss on
      a blocking guard, the same class as `110/130`'s gate risk.
      **The work:** read both planes with `-z`, as `--history` does. Output
      changes only where a quoted path is now matched. Before landing,
      measure read-only across the sibling repos how many would newly turn
      red, counts only.

      ✅ **Fixed and merged 2026-10-05** (queue run, a Sonnet 5.5 worker;
      `c1cef10`). Both planes now read NUL-delimited (`ls-files -z`, `diff
      --cached --name-only --diff-filter=ACMR -z`) through the history plane's
      streamed reader. The file set and ordering are unchanged. **Evidence:**
      across 29 local repos, old against new, all 29 were byte-identical, 0
      changed and 0 newly failing. Two of them track git-quoted paths, none of
      which is a never-publish name. Three new tests pin
      `core.quotePath=true`: a quoted never-publish path is caught on both
      planes, and a clean quoted path stays green. The tests fail against the
      old code. The suites passed (1,773; Node green). No separate pass is
      queued; `160/740` covers `publishscan` as it now stands. **The same
      class on two blocking guards** was found by the same worker and is filed
      as `115/260`.
