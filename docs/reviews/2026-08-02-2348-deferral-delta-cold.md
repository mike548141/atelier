# Cold pass — the deferral delta (`3acf7d2`)

- **Subject** — the rewrite of the review-deferral mechanism: `method/REVIEW.md`
  rules 1–2 and lifecycle steps 1/3 (deferred material moves from a
  below-the-divider section to a sibling `.deferred.md`, folded back at
  verdict), `skills/review-brief/SKILL.md`, the reviews template README,
  `tools/reviewscan.py` + `tools/test_reviewscan.py` (the mechanical half),
  and the registry `why` in `tools/floor.py`. Landed `3acf7d2`, 2026-07-29,
  by the 1418 session (Opus 5). Built, shipped, floor-wired.
- **Type** — self-authored doctrine plus its enforcing validator: rule-4
  class at its purest — this delta rewrites the very rules that govern how
  this review is being run.
- **Scope** — the `3acf7d2` diff and the six surfaces at HEAD; the doctrine
  argument itself (is the atomic-reading diagnosis right, is the sibling-file
  cure sound); the validator's actual bite; the fold-back lifecycle.
- **Spawn provenance** — rule 4: brief written by the taker, a Fable session
  Mike started 2026-08-02 and pointed at the queue; the author session
  neither started nor instructed it. Cold from the refs-only pointer; the
  shared intent record stays unopened until all four verdicts are committed.
  Caveat as disclosed in the two sibling verdicts: a sweep surfaced the
  author's `SESSIONS.md` index entry mid-pass-1, which includes an account of
  this delta (the unfollowable-rule diagnosis, the SL2 side-channel history,
  the deliberate no-lint-on-fold-back choice, "verified against all 76
  briefs", "driven live red-then-green"). Each exposed claim is treated as an
  assertion to attack. One structural advantage: this session has *operated
  under* the delta all day — the brief/verdict cycle now running is a live
  exercise of the rule under review.
- **Load-bearing assumptions to challenge**
  1. The diagnosis: the old below-the-divider deferral was *unfollowable*
     (reading is atomic), not merely unfollowed — and the sibling-file cure
     actually changes that, rather than moving the temptation one `ls` away.
  2. The honesty boundary: the doctrine claims the split makes early exposure
     "a deliberate act that leaves a trace" and only a context partition is
     structural — is that stated everywhere the mechanism is described, or
     does any surface still overclaim?
  3. The validator bites on the author at write time: a brief with a deferred
     section and no verdict below it reds; correct behaviour (fold-back after
     verdict; a verdict-bearing brief) stays green; the claimed
     red-then-green proof reproduces at HEAD.
  4. The no-lint-on-fold-back choice (reviewscan does not police that the
     sibling was folded in) does not leave a silent hole: an unfolded
     `.deferred.md` orphan after close would violate the one-file-at-rest
     rule with nothing watching.
  5. The six surfaces agree — no seventh surface still teaches the
     below-the-divider form.
- **Grounding to re-run** — reviewscan selftest + suite; a hand-built brief
  driven red (deferred section, no verdict) then green; the orphan case; the
  76-brief corpus claim re-swept at HEAD.
- **Non-goals** — the recurrence-ladder PROPAGATION sections (own pass);
  publishscan (own pass); rule 4's spawn criterion itself (predates this
  delta; in scope only where the delta's edits touched its wording).
- **Security scanner** — `/security-review` cannot reach a landed
  markdown+python delta with no pending diff; discharged on those grounds.
  The security lens runs manually — this delta's surface *is* an
  information-flow control (what a reviewer may read when), so lens 4 runs at
  design altitude on the flow itself, plus code altitude on the validator.

---

## Verdict — PASS-WITH-FINDINGS (0 MAJOR / 1 minor / 3 notes)

Reviewer: the taking session (Fable; spawn provenance and the partial
exposure caveat in the brief). This pass carries one unusual piece of
evidence: the reviewer *operated* the delta all session — four briefs and
verdicts run under its rules — and its failure mode fired live once (a
records-sweeping grep fed author-account bytes to this reviewer pre-findings,
disclosed in the pass-1 verdict). That incident is confirmatory, not
damning: it is precisely the residual the delta itself names — the split
makes early exposure deliberate-or-accidental-but-traceable, and only a
context partition is structural. The doctrine predicted its own leak class
honestly.

### Findings

- **DF1 — minor (overclaim of the mechanical half's reach).** The guard is
  vocabulary-anchored and the doctrine does not say so. `DEFERRED_HEADING`
  fires only on headings *beginning* "Deferred". Probes at HEAD: `## Seeded
  questions — open only after findings` GREEN; `## Author's deferred
  questions` GREEN (the word present, not the prefix); `## Questions to
  defer` GREEN. Yet REVIEW.md rule 1, the SKILL, and the template README all
  state flatly "`reviewscan` reds a brief carrying a deferred section with
  no verdict" — no vocabulary caveat. The population the net exists to catch
  (an author on old habits, not using the SKILL's canonical shape) is the
  population least likely to write the canonical heading. The module
  docstring's "the one mechanically-reliable shape" gestures at the
  narrowing but never names it. *Counsel:* either widen the trigger
  (`\bdeferred\b|\bseeded\b` anywhere in a heading — re-testing the honest
  disclosure headings stay green), or add one sentence to the three doctrine
  surfaces naming the canonical-vocabulary anchor. The choice is the
  principal's (rule 3); this reviewer leans widen-plus-caveat: cheap, and
  the false-red risk is bounded by the fence and prose exclusions already
  tested.
- **DF2 — note (test fixture vs name).** `test_deferred_section_below_a_
  verdict_passes` writes the deferred section *above* the verdict heading;
  the check is order-blind, so it passes, and order-blindness is actually
  correct (once any verdict exists, the exposure window is over) — but the
  fixture demonstrates the opposite of its name. Rename or reorder the
  fixture so the suite documents the intended at-rest shape.
- **DF3 — note (one marker, two checks).** `reviewscan:allow:` anywhere in a
  brief exempts it from check 2 as well as check 1 — a marker placed for a
  review-line reason silently waives the deferral guard too. Scoped markers
  (`reviewscan:allow:deferral:`) would keep the waivers separable; note
  only, since briefs rarely carry the marker.
- **DF4 — note (the "trace" is thinner than it reads).** Rule 1's "a
  deliberate act that leaves a trace" — the trace is the *session
  transcript*, not the durable record; nothing in git records an early
  opening unless the reviewer discloses it (as this session did). For an
  adopter reviewing by hand there is no trace at all. One clause naming
  where the trace lives would keep the claim exact.

### Lens results

1. **Approach & assumptions** — the diagnosis is right and crisply argued:
   reading is atomic, so a below-the-divider deferral is consumed by the act
   it must survive; "unfollowable, not merely unfollowed" is the correct
   category, and the cure moves bytes rather than words. Assumption 1 holds.
   Assumption 2 (honesty boundary) holds on all six surfaces — the
   what-the-split-does-not-buy paragraph is exactly the overclaim-refusal
   the apex demands — with DF4's clause as the one soft spot. Assumption 4
   (no fold-back lint) survives attack: any lint on the orphan window fires
   on prescribed behaviour between the verdict commit and the fold commit;
   the residual (a permanently unfolded orphan is invisible) is real,
   accepted, and named in the module docstring.
2. **Correctness & quality** — check-2 logic verified by probe and suite:
   canonical shape reds the exit code, fenced examples and prose disclosures
   stay green, README/siblings/templates correctly out of scope, verdict
   spellings matched generously (the right asymmetry — false reds punish
   finished records). DF1 is the reach gap; DF2 the fixture mislabel.
3. **Completeness / harvest** — six surfaces swept at HEAD; no seventh
   surface teaches the old form (all surviving "below a divider" text is
   negation or the verdict-placement rule, which is distinct and correct).
   The corpus claim re-run: 79 briefs green at HEAD (76 at the delta, plus
   this session's three).
4. **Security & privacy** — the delta *is* an information-flow control, and
   at design altitude it is an improvement with its limits stated (partition
   named as the only structural form). Code altitude: pure-stdlib text
   scanning, no execution of scanned content, fence handling prevents
   example-triggered reds. This session's live leak (pass 1) demonstrates
   the stated residual, not a new defect. `/security-review` discharged in
   the brief.

### Grounding re-run

`python3 -m unittest discover -s tools -p test_reviewscan.py` OK;
red-then-green re-driven via `scan_brief` probes (canonical red, folded
green); full-corpus run green at HEAD; the registry `why` renders in the
floor output of every commit this session made.

Rule 3: counsel labelled; decisions the principal's. No MAJOR — under the
close rule this pass alone would let the cycle close at its application;
the *batch* stays open on the two MAJORs in the sibling passes.

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

- **DF1 [fixed]** — ruled *widen + caveat*: the trigger matches
  `deferred`/`seeded` anywhere in a heading (verdict wins on dual-word
  headings); REVIEW.md, the SKILL and the template README name the
  vocabulary anchor.
- **DF2 [fixed]** — fixture reordered to the at-rest shape; order-blindness
  kept and documented as deliberate in its own test.
- **DF3 [fixed]** — check 2's exemption scoped to
  `reviewscan:allow:deferral:`; an unscoped marker no longer waives it
  (suite-proven both legs).
- **DF4 [fixed]** — the trace claim names where the trace lives.

No MAJOR ⇒ this application is terminal: **cycle CLOSED** at this
application (REVIEW.md close rule).
