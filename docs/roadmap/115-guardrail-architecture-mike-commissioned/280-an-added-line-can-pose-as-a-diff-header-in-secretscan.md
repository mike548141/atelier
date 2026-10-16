- [x] 🔎 **An added line can pose as a diff header in secretscan's staged
      plane** `[S][tools]`. Found 2026-10-05 by the `260` worker and not
      fixed there, because it is old behaviour outside that item.
      `secretscan` treats any line starting `+++ ` in
      `git diff --cached --unified=0` as a file header. An added line whose
      content begins `++ ` arrives as `+++ …`, and it changes which file the
      following added lines are attributed to. If the posed name is a path
      the ignore file skips, or a fixture the guard exempts, the real lines
      after it are silently excluded: a crafted or accidental line hides
      what follows it on a blocking guard. `conflictscan` and `leakscan`
      now use `report.diff_header_path`, which accepts only `+++ b/…` and
      `+++ "b/…"`. **The work:** parse the hunk structure, so a header
      can only follow a `diff --git` / `---` pair and never appears inside
      a hunk. Then use the shared reader, and add a test that a posed header
      inside a hunk does not move attribution. Check whether the shared
      reader has the same hole inside a hunk.

      ✅ **Fixed 2026-10-16** (`39a74b9`, merged `ef75803`. A Sonnet 5.5
      worker re-dispatched fresh after the 07:35 UTC crash). **The shared
      reader had the same hole.** In `conflictscan` and `leakscan`, an added
      `++ b/x` was taken as a header, and the line itself was dropped. Now
      one reader, `report.staged_added`, serves all three guards. It follows
      `diff --git`, the `+++` header and each hunk's `@@` counts, so a header
      is never recognised inside a hunk. It fails closed (exit 2) on a diff
      it cannot fit. It splits on the newline byte only, and it pins the
      diff prefixes. Evidence: the new tests fail on the old modules. The
      staged output is byte-identical on a realistic scratch change set, and
      the whole-tree output is identical. 1,859 Python and 411 Node tests
      pass. The orchestrator reproduced the hole on its own probe: the old
      `conflictscan` was clean over a hidden marker, and the new one blocks.
      This merge commit was the first real run of the new readers. The probe
      also showed that two guards report the wrong line number on the staged
      plane, which is older behaviour and is filed as `300`. Review queued at
      `160/800`.
