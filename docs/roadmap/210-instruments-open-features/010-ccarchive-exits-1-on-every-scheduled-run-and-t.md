- [ ] 🔎 **ccarchive exits 1 on every scheduled run, and the board did not know**
  (found 2026-08-09 by the sidecar build; **predates it and is not caused by
  it**). Verified independently, read-only: `--dry-run` exits **1** with
  `refusedShrink` carrying **two** entries — both per-project memory `.md`
  files, legitimately condensed, tripping the suspect-shrink guard. The paths
  are deliberately not named here: they identify a personal project and a
  private repo, and this repo is public.
  **Two consequences, both live:** the daily launchd run carries a non-zero exit
  (so any monitor keyed on exit code has been red or ignored for as long as this
  has held), and those two mirrors stay frozen at pre-condensation bytes until
  someone runs `--force`, so the archive is silently stale for them.
  ✅ **Clearing the staleness needs no ruling:** a `--force` run overwrites the
  two frozen mirrors and the scheduled run goes green again until the next
  legitimate condensation. That is a workaround, not the fix.
  🤔 **The real question is not the two files, it is the class.** The guard
  assumes append-only growth, which is true of transcripts and false of any
  whole-document class — memory `.md` as of 2026-08-09, and the `.meta.json`
  sidecar the moment Claude Code ever rewrites one. Deliberately **not** fixed at
  discovery: carving a size or class exception into a working guard to
  accommodate an event pattern nobody has decided on is fitting the limit to the
  measurement. Options are (a) exempt whole-document classes from the shrink
  guard, (b) keep the guard and give the scheduled run a way to succeed with a
  declared refusal, (c) accept the red and clear it by hand. Same shape reaches
  `--audit`, which buckets a rewritten whole document as `mutated` rather than
  `grown`.
