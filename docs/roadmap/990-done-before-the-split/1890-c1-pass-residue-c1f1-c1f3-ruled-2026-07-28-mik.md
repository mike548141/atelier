- [x] (2026-08-03: applied, terminal) **C1-pass residue — C1F1–C1F3, RULED 2026-07-28 (Mike, plain-language
      walk-through with per-option impacts).** The terminal pass
      returned 0 MAJOR / 1 minor / 2 notes
      ([verdict](../../reviews/2026-07-28-1204-c1-advisory-cold.md)); cycle
      closed, residue Mike's per rule 3.
      **C1F1** (minor) — on the floor's human line, an advisory's `why`
      displaces the "N of M scope paths missing" drift note (it survives
      only in `--json`), so a softened check with shrinking cover shows the
      reason but not the shrink → **JOIN THE NOTES**, restoring the TA3 fix
      exactly where the board is worst-informed.
      **C1F2** (note) — the record says an expired advisory shows how many
      days it has stood "on the floor and the board", but the count renders
      on the board only → **ADD THE COUNT TO THE FLOOR LINE** (chosen over
      correcting the record: it makes both true, and puts the ageing
      pressure at commit time rather than on a board someone must go and
      look at).
      **C1F3** (note) — config-authored strings (`why`, disabled reasons)
      print raw to terminals; a hostile child config could embed escape
      sequences → **STRIP C0 CONTROLS AT PARSE**, closing the pre-existing
      class as well as C1's two new fields. Scope widened by the PA4 ruling
      (Mike, 2026-08-03): `publishscan`'s two config-authored surfaces —
      ignore-file globs echoed in error messages, and finding paths in
      output — are in this fix's scope, so one change closes the class
      everywhere. Low priority while the estate is single-owner; it becomes
      real on first outside adoption.
      **Work owed: all three.**
