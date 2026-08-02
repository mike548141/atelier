# Cold pass — the recurrence-ladder delta (`4015e06`)

- **Subject** — `method/PROPAGATION.md`'s two new sections: *When a rule keeps
  breaking — climb, never restate* (the three-rung ladder) and *One statement,
  stamped copies — never three originals* (the DRY-for-doctrine rule). Landed
  `4015e06`, 2026-07-29, by the 1418 session (Opus 5), in the commit that also
  queued the four review pointers.
- **Type** — self-authored doctrine, prose only; rule-4 class. Meta-doctrine:
  rules about how rules are maintained, so a defect propagates through every
  future rule edit.
- **Scope** — the two sections at HEAD; their grounding citations re-checked
  against the artefacts they cite; their self-application (does the delta obey
  the rules it states); the landing commit's records hunk.
- **Spawn provenance** — rule 4: brief written by the taker, a Fable session
  Mike started 2026-08-02 and pointed at the queue; the author session neither
  started nor instructed it. Cold from the refs-only pointer; the shared
  intent record unopened until all four verdicts are committed. Exposure
  caveat as disclosed in the sibling verdicts (the `SESSIONS.md` index entry).
  Process disclosure for this pass: two consistency probes (the promotion
  threshold, the pointer count) ran before this brief was written; the brief
  names the full intended attack surface, not only what the probes found.
- **Load-bearing assumptions to challenge**
  1. Every grounding citation resolves: the 2026-07-19 framing correction,
     the private-repo × posture join ("all three occurrences, one trigger"),
     the reviewscan worked example ("stopped recurring"), stampscan's shelf
     (D2), the stamped surfaces it names.
  2. The ladder is operable: "stop at the first that fits" carries a usable
     fitness test — its own worked example shows rungs can "have answers"
     that would not have worked.
  3. The delta obeys its own DRY rule: no unmarked second original of either
     section's content exists elsewhere in the corpus.
  4. The recurrence thresholds in live practice agree with the ladder's
     trigger, or the difference is named.
  5. Honesty: what is owed and not done (the R1 count, the R2 survey) is
     said, not fudged.
- **Grounding to re-run** — citation checks against REVIEW.md, ROADMAP D2,
  the stamped headers in the SKILL and template; corpus sweeps for competing
  statements and thresholds.
- **Non-goals** — the deferral delta itself (rung 3's worked example has its
  own pass); R1/R2 execution (queued work, reviewable as pointers only);
  `stampscan`'s parser defect (shelved under D2 with its own verdict).
- **Security scanner** — `/security-review` cannot reach a landed
  markdown-only delta; discharged. Lens 4 runs at design altitude only —
  the delta has no code or data surface; its security relevance is indirect
  (rules governing how guard rules are maintained).

---

## Verdict — PASS-WITH-FINDINGS (0 MAJOR / 3 minor / 1 note)

Reviewer: the taking session (Fable; provenance and exposure caveats in the
brief). The two sections are well grounded and unusually honest about their
own gaps (the uncountable trigger, the unrun survey, the shelved stampscan).
The findings are all self-application seams — which is the correct standard
for meta-doctrine: rules about maintaining rules get judged by whether they
survive being aimed at themselves.

### Findings

- **RL1 — minor (the stop rule lacks its own fitness test).** "Three rungs,
  cheapest first — stop at the first that fits." Rung 1 *always* fits in the
  weak sense: a framing rewrite is always available, always feels like
  progress, and the section's own opening says wording changes "reliably"
  are not progress. The ladder's worked example (rung 3) makes the point
  itself: rungs 1 and 2 "both had answers — and both would have failed."
  So "fits" must mean *would have made this failure impossible or visible*,
  not *produces an edit* — the test the example applied but the rule never
  states. *Counsel:* one clause: "fits = would have prevented the recorded
  occurrences; test the rung against the incidents before stopping on it."
- **RL2 — minor (an unmarked second original of rung 1).** REVIEW.md's
  framing-trap paragraph states the full rung-1 rule in its own words
  ("When a written rule keeps being broken, suspect its framing before its
  enforcement… findable from where the reader stood — Mike, 2026-07-19")
  with no stamp and no pointer to the ladder; PROPAGATION's rung 1 cites the
  incident but not the fact that the rule is also *stated* there. Under this
  delta's own one-statement rule that is two independent originals, one
  edit away from drift. REVIEW.md's copy predates the ladder — the delta
  consolidated the rule upward without stamping the older statement.
  *Counsel:* mark the REVIEW.md paragraph as the grounded instance pointing
  at PROPAGATION as canonical (or trim it to the incident + pointer). Rule 3:
  Mike's call which file owns it; the reviewer's view is PROPAGATION owns
  the rule, REVIEW.md keeps the incident.
- **RL3 — minor (two recurrence thresholds, unreconciled).** The ladder's
  interim trigger is "treat a second occurrence you *happen* to notice as
  the trigger"; live practice operates the ">2 promotion rule" — the
  ROADMAP is holding a queued item "for a third instance, per the
  reviewer's counsel and the >2 promotion rule" (Track A, TAA3). The acts
  differ (climbing the ladder vs promoting a pattern into doctrine), but
  both answer "how many occurrences before acting", and a reader holding
  that question finds two numbers in two files with neither naming the
  other. The countable-trigger paragraph is the natural home for one
  reconciling sentence. *Counsel:* state both thresholds and their
  different acts in that paragraph, or unify deliberately.
- **RL4 — note (the landing commit's own counts disagree).** The ROADMAP
  hunk in `4015e06` writes "Three rule-4 pointers, refs only" above four
  `⏳` bullets, while the same commit's message correctly says "Four rule-4
  pointers queued here." The count-slip class is on the record five times
  over; this instance landed inside a doctrine delta about recurrence.
  Records fix, not doctrine — corrected at this batch's close (Three →
  Four), tagged there.

### Lens results

1. **Approach & assumptions** — the ladder's shape is right (system before
   wording; recurrence, not severity, earns a check) and rung 3 is a real
   addition with a sharp finding question ("what would have to stop being
   true"). The DRY section's distinction — independent originals are the
   defect, stamped copies are the mechanism — is the correct cut, and its
   grounds (drift caught twice, 2026-07-19 F3) re-verified. Assumption 2
   failed in part → RL1. Assumption 3 failed in part → RL2. Assumption 4
   failed in part → RL3.
2. **Correctness & quality** — every citation resolves at HEAD: the
   2026-07-19 framing correction (REVIEW.md carries it), stampscan shelved
   on a parser defect (ROADMAP D2, with its own S4 verdict), the three
   stamped surfaces all genuinely carry stamp headers (child CLAUDE.md
   template `stamp:begin`, the SKILL's "STAMPED COPY", the template
   README's "STAMPED POINTER"). "Landing = queuing" honoured: the pointers
   landed in the commit completing the series.
3. **Completeness / harvest** — what is owed is said (R1 cadence, R2
   survey, the unwatched stamp convention); the corpus sweep found no
   further unmarked original of either section beyond RL2 (the ROADMAP's
   restatements are records of incidents, not rule statements).
4. **Security & privacy** — no code or data surface; design-altitude note
   only: the DRY rule strengthens guard integrity long-term (drifted guard
   copies are how enforcement quietly diverges), and the honesty about
   stampscan's shelf keeps the convention's unwatched status visible.
   `/security-review` discharged in the brief.

### Grounding re-run

Citations re-checked against REVIEW.md, ROADMAP (D2, TAA3), and the three
stamped surfaces at HEAD, as listed above; thresholds and second-original
sweeps run over `docs/method/` and the ROADMAP.

Rule 3: counsel labelled; decisions the principal's. No MAJOR — this pass
alone would close at its application; the batch stays open on the sibling
MAJORs.

### Reconcile addendum (intent record opened after all four verdicts)

The shared intent record
(`sessions/2026-07-29-1418-publish-surface-and-deferral.md`) was opened only
after all four queued verdicts were committed in this worktree, per rule 1's
sequence. Reconciliation changed no finding. Batch-level notes: the record's
"four places" framing matches PS1's diagnosis — the delta amended all four
*files* but missed the second mandate-site inside REPO-STANDARD; the record's
twelve-repos and the publishscan commit's eleven-children counts are
consistent (atelier untracked itself in between); the record's § Owed says
"three cold passes queued" while four pointers landed — the RL4 count slip
originates in the record and is left standing there as history, with the
live ROADMAP header corrected at this batch's close. The record's honest
notes (the split is not structural; the denylist limits; the no-git catch)
agree with, and partly pre-state, DF4 and the pass-2/pass-3 lens results.

### Decisions (Mike, 2026-08-02, in-session walk-through)

- **RL1 [fixed]** — ruled *apply*: "fits" defined as would-have-prevented-
  the-recorded-occurrences, tested against the incidents.
- **RL2 [fixed]** — ruled *apply*: REVIEW.md's framing-trap paragraph
  stamped as the grounded instance; PROPAGATION canonical.
- **RL3 [fixed]** — ruled *apply*: two thresholds, two acts, both named in
  the countable-trigger paragraph.
- **RL4 [fixed]** — records count corrected at the review batch's close
  (Three → Four).

No MAJOR ⇒ this application is terminal: **cycle CLOSED** at this
application.
