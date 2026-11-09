- [x] 🎯 **R1 — the recurrence count has to become mechanical, and the mining
      pass earns a cadence rather than one run.** The registry's promotion rule
      (recurrence, not severity, earns a check) never fires, because nothing
      can answer *how many times has this broken?* — recurrence is currently
      noticed by somebody's unease, which is exactly how a rule reaches its
      third occurrence unpromoted. The retrospective sweep above tells us about
      the past; the defect is continuous. Decide the cadence and what triggers
      it (a scheduled run, or a check at review close), then wire it.
  - [ ] 📎 **Corpus is narrower than Mike's own ask, named 2026-09-12.** The
        one sweep this item's parent README records ran over **review
        findings** (330 findings across 47 reviews) — never over raw session
        transcripts. His words: *"Worth reviewing all the past session
        transcripts for evidence and learnings, recurring issues, defects
        etc."* `cctranscript` already exists and reads transcripts for other
        purposes (attribution, search), so the mining pass this item wants
        should widen its source to transcripts themselves, not stay scoped to
        the findings a review happened to already write down — a defect that
        never reached a review finding is invisible to the current corpus by
        construction.
  - [ ] 🔁 **A further steer on the same idea, same day:** *"Another idea
        could be a scheduled review of all session transcripts to find
        problem, opportunities, and learnings and make adjustments."* This
        item already asks for a cadence (the line above); his phrasing adds
        two things worth keeping distinct from *recurrence-counting* — a
        transcript sweep should also surface **opportunities**, not only
        problems, and should end in **adjustments made**, not only a report.
        Whether "make adjustments" means proposing board items (safe, matches
        how this item's own corpus already gets used) or something that edits
        doctrine on its own (a materially bigger, unscoped claim) is not
        decided here and should not be assumed by whoever builds this.
  - [ ] ⚖️ **Mike, 2026-11-09, in his own words** (queue run 722ac2e2 had said he ruled out background jobs on this machine, a wrong reading of the estate root's record): *"I didnt rule out background jobs. I ruled out you creating silly little apps and adding them as login items on the mac that dont then run on a schedule but an event. For example background jobs for an active claude code session are fine. I dont' think cloud would work as it cant access things like transcripts? Following all that I approve the recommended option"*. The recommended option read: on his word, about monthly, a session reads the transcripts and files what it finds as board items; it proposes changes and does not make them.
  - [x] ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet worker, read by
      the orchestrator before landing): `PROPAGATION.md` carries the on-his-word review and `TOOLBOX.md` § *Background jobs* his words. Cold pass `160/1240`.
