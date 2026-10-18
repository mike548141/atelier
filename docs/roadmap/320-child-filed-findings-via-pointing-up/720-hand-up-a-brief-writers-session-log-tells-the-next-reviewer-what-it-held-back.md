- [x] **FIXED 2026-10-18** (wt: atelier-qr-180-plugin)
      🔎 **Hand-up: a brief-writer's session log tells the next reviewer what it
      held back** `[doctrine]`. Handed up from a private child on 2026-10-18
      under `PROPAGATION.md` § *Pointing up*: one finding, from a rule-4 cold
      pass run that day (its review record is dated 2026-10-17 2235 UTC; a Fable
      reviewer, no orchestrator). Formed against the child's tree and this
      repo's `REVIEW.md` and `RECORD.md` at `main`; the reviewer did not open
      this repo's own review records, so overlap with them is unverified.
      Consideration and remediation are atelier's; the child stops here.
      **The gap.** `REVIEW.md` rule 1 puts an author's or brief-writer's attack
      questions and held-back facts in a separate `*.deferred.md` that the
      reviewer opens only after its own findings are committed, because "a
      reviewer cannot un-read them". The brief-writer then closes its own
      session under `RECORD.md`, and the child's onramp (its `CLAUDE.md` read
      order) tells every new session to read the tail of the session log before
      anything else. Nothing in either file tells the brief-writer to keep the
      deferred material's *content* out of that session-log entry.
      **The instance, evidenced in the child.** The brief-writer's close entry
      summarised what it had held back in one line — *"a held-back sibling
      carrying the questions and two facts met on the way (the items pack's
      80-character path warning; the census's standing job FAILs)"* — so the
      cold reviewer read both facts' headlines at onramp step 3, before opening
      the brief, and disclosed the leak in its verdict. Neither headline steered
      a finding (the reviewer did not look at either until after its findings
      were committed), but the mechanism rule 1 exists to prevent — framing
      leaking through the ask — ran through a side door the rule does not watch.
      *Suggested shape (atelier's to decide):* in `REVIEW.md` rule 1 or
      `RECORD.md`, a line that any record the next session reads at onramp
      (session log, board pointer, commit subject) refers to deferred material
      by file name and count only, never by topic — and a `reviewscan` line for
      it, if the scanner can see session logs. Adjacent: rule 1's grounding
      case (framing leaks through the ask); `RECORD.md` on what a close entry
      carries.
      review: not warranted — a hand-up of one finding; the cold pass that
      formed it is itself the review, and the fix is atelier's to decide.

  **Closed 2026-10-18** by a Mike-opened Opus 5.5 queue run. Taken as
  suggested, minus the scanner. `REVIEW.md` rule 1 gains *side doors*: any
  record a reviewer reads before the brief (session-log tail, board pointer,
  commit subjects) names deferred material by file and count only, never by
  topic. `RECORD.md`'s `SESSIONS.md` bullet points at it. No `reviewscan`
  line, because a topic is meaning and no pattern can tell "two facts" from
  what the facts say. Rule-4 cold pass queued at `160/910`.
