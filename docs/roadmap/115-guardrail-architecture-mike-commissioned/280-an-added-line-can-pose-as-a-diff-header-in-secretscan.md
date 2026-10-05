- [ ] 🔎 **An added line can pose as a diff header in secretscan's staged
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
