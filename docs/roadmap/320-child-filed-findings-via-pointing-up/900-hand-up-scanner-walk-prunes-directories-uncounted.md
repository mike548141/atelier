- [ ] 🔎 **Hand-up: outside a git work tree, `leakscan` and `secretscan`
      skip pruned directories without counting them, so a publish over a
      plain tree can read green with files unread.** Reported 2026-11-23 by
      a private child's queue run (session cc48ecd8), class only. When a
      scan root is not a git work tree, the shared file walk falls back to
      `os.walk` and prunes its skip-named directories (`.vscode`, `.idea`,
      `node_modules` and the like). It counts none of the files it prunes,
      so no tally line tells "walked everything" from "pruned three
      directories". A caller that publishes such a tree with no path
      exemptions cannot refuse on what it cannot see.
      **Evidence (re-driven by the reporting orchestrator, atelier tools at
      `07377afb`).** A throwaway non-git tree, with a synthetic OpenSSH
      private-key block in `.vscode/notes.txt` and the same bytes in
      `ctl/notes.txt`: `secretscan --root` exits 1 and names only
      `ctl/notes.txt`; every suppression count reads 0. With the `.vscode`
      file alone it exits 0 with its "scanned nothing" warning, so the miss
      is loud only when the pruned file is all there is. `leakscan --root`
      over the same tree, plus a documentation-range address in a file in
      each directory, reports "2 file(s) opened" of the 4 present, and no
      count accounts for the other 2. Git-tracked mode is unaffected
      (tracked files under those names are read).
      The child closed its own instance by refusing, in its publish step,
      any file with a path part in either scanner's `SKIP_DIR_NAMES`,
      imported from the scanners, never copied.
      **Asked:** in `os.walk` mode, have the walk count the regular files
      it prunes, and have each scanner print that count in its suppression
      tally (e.g. `N file(s) under a pruned directory`), so a caller can
      refuse on it the way it refuses on the ignore-glob count. Whether a
      non-zero count should also turn the coverage line into a warning is
      the house's call.
