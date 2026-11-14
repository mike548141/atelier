# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0158-cclive-machine-wide-live-work-cold.md` (`REVIEW.md` rule
1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `c4d93896`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

## The brief-writer's own questions

1. **The quiet footnote.** A repo whose claims are unknown because it has *no main or master ref*
   (not because it has no board) still lands on the quiet line with a `*`, and the footnote reads
   "no board, so claims are unknown". Does the footnote say something false for that repo, and can
   such a repo be quiet while a session holds a claim on another branch? (No repo on this machine
   hit that path on 2026-11-14; build one.)
2. **Worktree names are matched globally.** `markLive` builds the set of live worktree basenames
   across *every* repo, then marks a claim live when its `wt:` name is in that set. Linked worktrees
   commonly share a basename with their repo (a worktree of repo `x` checked out at
   `.../something/x`). Can a claim in one repo be marked `live` by a live worktree of the same
   basename in another repo, and then mark that repo's same-named worktrees live too (A3, A4)?
3. **Indistinguishable rows.** On 2026-11-14 four live sessions in one repo all printed `where` as
   the repo's own name and four worktree lines all read `<repo>  (no branch)  … [detached]`. The
   row shows the basename, not the path. Can a reader tell which session holds which worktree?
4. **The session id on a claim** is the first 8-hex token with a letter anywhere *after the stamp
   on the stamp line*, which can include title text: a commit SHA prefix or a hex-looking word.
   Can a claim be credited to the wrong session, or marked live by an unrelated one?
5. **The released filter** voids a stamp if the stamp line contains `released` anywhere. For an
   indented `[~]` that also drops the claim entirely. Is a held claim whose title mentions a
   release silently uncounted?
6. **Unsanitised names.** Transcript text, claim titles, branches and worktree names pass through
   `printable`/`clip`. The repo name in each repo header and in the quiet list, and root paths, do
   not. Can a directory name under a root carry a terminal escape into the output?
7. **Sessions in a removed worktree** land under *elsewhere* even when the path was a worktree of a
   scanned repo minutes ago (two did on 2026-11-14, both brief-writers whose worktrees had just
   been removed). Is that the honest reading, or does it hide that the session belonged to a repo?
8. **Exit codes.** `--root /nonexistent-dir` exits 0 when the transcript store is readable: the
   root prints UNREADABLE and nothing under it is scanned. Is exit 0 consistent with the help
   text's "2 bad usage or nothing could be read", and with a caller that reads only the exit code?
9. **A1, the idle-open session.** A session open and waiting on its operator writes nothing, so
   its worktree reads `quiet` after ten minutes. The limit is printed. Is it prominent enough for
   a session that reads `quiet` as "free to take"?

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC, foreground, load average 12.9 to 14 on 12 cores.

- `node --test instruments/cclive.test.js`: 32 tests, 32 pass, 0 fail, about 14 s.
- `nice node --test instruments/ccclose.test.js`: 111 tests, 111 pass, 0 fail, about 148 s.
- `mandoc -T lint -W style instruments/man/cclive.1`: no output, exit 0.
- `instruments/cclive`: exit 0. 30 repos scanned under the default root, 2 skipped (not git
  repos); 8 fresh transcripts; totals sessions 8, agents 0, claims 54 (4 dated, 50 undated; 9 repos
  unknown), worktrees 5; 4 repos active, 26 quiet; 2 sessions under *elsewhere*.
- `instruments/cclive --json`: exit 0. Of 30 repos, 9 had `claimsWhy` "no board" (all quiet), none
  had "no main or master ref"; 17 quiet with claims known; 4 active.
- `instruments/cclive --root /nonexistent-dir`: exit 0. `--fresh 0`: exit 2 (bad usage).
- The three `coldsweep --commit` lines in the brief: each exit 0. The sweep line with the three
  `--also-exclude` paths: exit 0.
- `merge-base --is-ancestor` on all three commits: each an ancestor of the brief's base,
  `58f612b7`.
- The installed `cclive` on `PATH` is a symlink into the principal's primary checkout, not the
  review worktree.
