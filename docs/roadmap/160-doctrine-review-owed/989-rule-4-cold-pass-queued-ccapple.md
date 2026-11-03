- [ ] ⏳ **Rule-4 cold pass queued: `ccapple`, a read-only search of the
      Apple apps' local stores, landed before its review on the principal's
      word.** Mike, 2026-11-03, through the decision device, of three routes
      for PR #126 (keep it open for a review, merge it now and review after,
      or close it): he chose *"Merge it now, review after"*. That is his
      answer, recorded as such. It is the first instrument whose output is
      other people's private content (ADR 0006 addendum, 2026-11-01). The
      building worker (2026-11-01) and the landing session (queue run
      4c65083c, which resolved the merge's record conflicts and wrote no
      code) both queue this and take neither.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4, with the
      privacy limits the PR states (read-only opens, required filter, capped
      output, locked notes unread, the Home reader's column allowlist) as the
      first things to break.
      *Delta, scoped to paths:* `instruments/ccapple`,
      `instruments/test_ccapple.py`, `instruments/man/ccapple.1`,
      `instruments/README.md`, `.github/workflows/ci.yml`,
      `docs/decisions/0006-instruments-in-atelier.md` (the merge of PR #126,
      on `main`, 2026-11-03).
      *Intent records:* PR #126's description, and
      [`../210-instruments-open-features/340-ccapple-checks-the-store-before-the-filter.md`](../210-instruments-open-features/340-ccapple-checks-the-store-before-the-filter.md).
