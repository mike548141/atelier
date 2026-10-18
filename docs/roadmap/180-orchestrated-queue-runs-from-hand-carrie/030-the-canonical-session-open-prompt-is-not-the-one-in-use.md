- [x] **DONE 2026-10-18** (wt: atelier-qr-180-plugin) **The canonical
      session-open prompt is not the one the principal actually uses.** Mike,
      2026-10-18, opening a queue run: *"The current version of the prompt I
      like to use is this
      "~/.pets/session-open-prompt-prior-version-2026-09-14.txt" which we
      should update into atelier too"*. That file is the 2026-09-14 text plus
      two closing lines; `docs/method/session-open/session-open-prompt.md`
      carries the later 2026-09-16 additions instead (open with the date, the
      checklist format, verify-don't-infer, bullet-list board answers, the
      fuller close confirmation) and lacks his two closing lines. Owed: bring
      the canonical file to the text in use, with git history holding what
      changes, and reconcile the prompt with doctrine it now contradicts
      (its "confirm you're on the capable tier … stop" line predates the
      2026-09-19 state-and-proceed ruling, `CONCURRENCY.md` § *Tier at open*).

  **Closed 2026-10-18** (commit `998c35f`). The canonical file is now his text,
  long closing lines rewrapped, with two lines reconciled: the tier line takes
  the 2026-09-20 wording (`320/320`) and the close list the 2026-10-03 one
  (`200/100` C3). 🔎 Both had been in this file and were **undone on
  2026-10-17** by `6a0ac93`, a "restore current content" commit that wrote
  back an older text as current — a restore that dropped two rulings with
  nothing to catch it. Dropped by his choice and kept in git history: the
  2026-09-16 additions (date at open, checklist reports, verify-don't-infer,
  bullet-list board answers, the fuller close confirmation). Whether any comes
  back is put to him at the run's close.
