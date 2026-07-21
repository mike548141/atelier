# Cold pass — REVIEW.md scope mandate + security & privacy lens 4 (deltas `f9db922` + `a059e49`)

- **Date/time**: 2026-07-21 2158 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "Please do any review work" (Fable). The taker authored
  neither delta, none of the files they touch, and no record of the authoring
  session. Claim landed on `main` (`3909d76`) before review work started; this
  brief is taker-written in wt: review-scope-lens4-cold-pass. The review run
  itself is a fresh-context subagent spawned by the taker — a spawn the
  author neither started nor instructed, so the criterion holds through both
  hops.
- **Named exposure (the taker's, not the reviewer's)**: before writing this
  brief the taker read the author's intent record
  (`docs/sessions/2026-07-21-2147-review-scope-security-lens.md`) in full —
  including the author's own account of the gap audit and a framing note
  addressed to this cycle — and both delta commit bodies. That is author
  framing the taker cannot un-read. Mitigation, per rule 1's shape: the
  taker's seeded questions sit **below the divider**, the reviewer is a
  separate cold context that has read none of that material, and everything
  above the divider is refs and mechanics only. The brief's framing remains
  attackable.
- **Deferred material (reviewer opens only after its own findings are
  durably drafted)**: the seeded questions below the divider; the intent
  record named above; the commit bodies of `f9db922` and `a059e49`; prior
  verdicts in `docs/reviews/` (notably the 2026-07-15 and 2026-07-19 cycles
  the delta's text cites).

## What the work is (refs only)

Deltas `f9db922` + `a059e49` (2026-07-21), reviewed as one, at worktree HEAD:

- `docs/method/REVIEW.md` — a scope paragraph above the lens list (*What a
  review actually checks*), a fourth lens, and a sentence naming a harness
  scanner inside it.
- `docs/method/README.md` — one summary-line change.
- `docs/build/templates/docs/reviews/README.md` — the child-floor template
  carrying corresponding text.

In scope at HEAD: those files, plus every other surface that states, counts,
or relies on the lens structure or review scope — templates, skills, method
docs, ROADMAP conventions — per the delta's own scope rule. The review runs
under the doctrine as amended: all four lenses, applied to the text that
defines them.

## Why it earns a review

Self-authored doctrine by function (rule 4): these paragraphs govern every
future review in this repo and, via the child template, every repo on the
fleet floor — the widest blast radius in the operating model. Worst failure
modes: a scope or lens rule that is uncostable in practice and gets
appeased rather than followed; an instruction that cannot actually be
executed as written (a tool named where it cannot run); a narrowing escape
left open in the very text that was meant to close narrowing escapes.

## Reviewer instructions

1. Read this brief **down to the divider and stop**. Read the repo: the
   three delta files at HEAD in full, `git show f9db922 a059e49` **with
   `--format=` so the author's commit bodies stay unseen**, and whatever
   siblings your own attack surface demands.
2. Name the load-bearing assumptions yourself as your first act (lens 1);
   run all four lenses as the amended text defines them — this review is
   also the first live execution of the rules under review, and any point
   where you cannot comply as written is itself a finding.
3. Re-run every live-proven claim in scope. Where lens 4's scanner
   instruction applies, execute it or discharge it exactly as the text
   directs, and report how that went as evidence.
4. Draft findings with stable IDs (SL1, SL2, …) and severities
   (MAJOR/MEDIUM/LOW), durably written to
   `docs/reviews/drafts/2026-07-21-2158-scope-lens4-findings-draft.md`,
   **before** opening the deferred material. Then open it, reconcile —
   never anchor — and produce the verdict: per-lens answers, findings,
   follow-ups, and a repeat of the spawn provenance above.

Non-goals: the conduct of the 2026-07-21 authoring session (its record is
deferred context, not the work); re-litigating rulings Mike has already
made in prior closed cycles (attack how this delta *encodes* them, not the
rulings themselves); the reviewscan/review-line machinery closed in the
0913 cycle.

---

## Deferred — the taker's seeded questions (a floor, never a fence)

- **SQ1 — unbounded scope vs "scoped and short".** The new mandate says
  scope is the widest the work admits and non-goals are the only legitimate
  narrowing; *When to review* still requires every review to stay "scoped
  and short". Can a reviewer honour both, or does the pair train sessions to
  write sweeping non-goals to make reviews finishable? Note who writes the
  non-goals in a warm (non-rule-4) brief: the author. Is "non-goals are the
  only legitimate narrowing" an escape hatch in exactly the wrong hands?
- **SQ2 — lens 4's cost calibration.** "A must on every review" plus
  "checked, not recalled" against OWASP: what does this cost on a
  ten-minute doc review? Is the one-line discharge shape well-enough
  defined to stay honest (who judges "genuinely no surface"?), or will it
  become the reflex stamp that hollows the lens?
- **SQ3 — the scanner instruction's executability.** Claude Code's
  `/security-review` reviews *pending changes on the current branch*. A
  rule-4 cold pass reviews an already-committed delta on a clean tree; a
  design-time review has no diff at all. Does the instruction as written
  misfire in the two review shapes this repo most actually runs? What did
  it do when *you* executed it per instruction 3?
- **SQ4 — stale lens arithmetic.** The delta chose "lens 4" to keep 1–3
  references valid. Sweep the repo (and templates/skills that ship to
  children) for "three lenses", "all three", lens counts in prose, and any
  place the lens list is restated but not updated.
- **SQ5 — "where possible" as an escape.** Real-world behaviour must be
  exercised live "where doing so is possible". Is there any test or burden
  attached to a claim of impossibility, or does "wasn't possible" become
  the new "no source code"?
- **SQ6 — child-floor fidelity.** Does the template sentence actually
  compress the parent without narrowing (scope, all four lenses, the
  scanner clause), and does anything in it break for a child repo whose
  harness has no `/security-review`?

---

## Verdict — cold pass, deltas `f9db922` + `a059e49` (reviewed as one, at HEAD `a0d24d7`)

**PASS-WITH-FINDINGS — 2 MAJOR · 3 MEDIUM · 2 LOW.** The scope mandate and lens 4 are sound doctrine, correctly landed on the three delta files; the MAJORs are a missed point-of-use surface and a scanner instruction that misfires — live-proven — in the very review shape this pass ran in.

### Spawn provenance (rule 4, restated from the brief)

Taken from the ROADMAP `⏳` queue by a session Mike spawned with "Please do any review work" (Fable). The taker authored neither delta, none of the files they touch, and no record of the authoring session; the claim landed on `main` (`3909d76`) before review work started; the brief is taker-written in wt: review-scope-lens4-cold-pass. This review ran as a fresh-context subagent spawned by the taker — a spawn the author neither started nor instructed; the criterion holds through both hops.

**Deferral order: honoured in every act of the reviewer, breached once mechanically by the doctrine under review.** Reading stopped at the divider; deltas were read via `git show --format=`; assumptions were named and the surface sweep completed before any deferred material; the findings draft was durably written (`docs/reviews/drafts/2026-07-21-2158-scope-lens4-findings-draft.md`) before the deferred section, intent record, or commit bodies were opened. However, executing lens 4's scanner instruction per brief instruction 3 caused `/security-review` to inject the entire brief file — deferred section included — into this reviewer's context before drafting. That contamination is disclosed in the draft with a pre-/post-leak attribution timeline (all assumptions A1–A6 and the SL1/SL3 sweep results demonstrably predate the leak; only SL6's angle arrived with it and is attributed as seeded). The breach is itself SL2 evidence. One further disclosure: a lens-reference grep legitimately surfaced the one-line `docs/SESSIONS.md:132` index summary of the authoring session; the session record itself was not opened until the reconcile step.

### Per-lens answers

- **Lens 1 — approach & assumptions.** Right problem, right shape. The gap was re-derived independently, not taken from the record: pre-delta `REVIEW.md` contained zero security/privacy/threat/OWASP content and an enumerated-never-mandated scope — both confirmed from the diffs. The design choices are good: lens-4-as-a-number preserves every pre-existing lens-1/2/3 reference (verified by sweep); the one-line-discharge-with-grounds mirrors `review: not warranted`; the child template correctly genericises the vendor command with "e.g.". Two assumptions failed under attack: A3 (scanner runnability in the cold-pass shape — falsified live, SL2) and A4 (widest-scope vs "scoped and short" left unreconciled, SL5).
- **Lens 2 — correctness & quality.** The three delta files do what they claim at HEAD; `method/README.md` says four lenses; no overclaim in the delta text itself. One encoding escalation found at reconcile: a permissive grant became a mandate (folded into SL2). Cosmetic wrap defects (SL7).
- **Lens 3 — completeness / harvest.** The delta's own scope rule ("every surface that states, counts, or relies on the lens structure or review scope — templates, skills…") is the standard it fails: `skills/review-brief/SKILL.md` still counts three lenses (SL1), `docs/build/templates/CONTRIBUTING.md` still carries the old three-part scope sentence (SL3), and the amended template file retains a contradicting "correctness only" review type (SL4).
- **Lens 4 — security & privacy.** Executed, not recalled. Design altitude: the delta is prose in a public repo; no personal data, no over-collection; but the scanner instruction creates an information-flow defect in the review process itself — running it during a cold pass leaks the brief's deferred material into the reviewer (SL2.2). Code altitude: no code surface; the repo scanner floor re-run green at HEAD (secretscan 0 · leakscan 0 · licenscan 0/Apache-2.0 · linkscan 0 · reviewscan 0 · sizescan --check 0). The `/security-review` instruction was executed as directed: it analysed the wrong diff (the brief file — the only pending change; the in-scope deltas are landed on `main`), and its own hard exclusion 16 bars all findings in markdown files, so its "no vulnerabilities" result is a definitional no-op for this work class, weighed accordingly.

### Findings

**SL1 — MAJOR — the review-brief skill still stamps the three-lens structure.** `skills/review-brief/SKILL.md:53–59`: "**The three lenses**, run all three" — no lens 4, no security & privacy anywhere in the file, no scope mandate, no scanner clause. The file's own header (lines 6–13) declares it "narrowing-free — it may compress the parent, never contradict it" and records this exact drift class being caught once before (2026-07-19 cold-pass F3). It now contradicts the parent on the delta's two central claims, at the point of use: briefs written via the skill omit the mandatory lens. Plugin-bundled — fleet blast radius.

**SL2 — MAJOR — the scanner sentence cannot be executed as written in the doctrine's own primary review shapes, and executing it breaches the independence structure.** `docs/method/REVIEW.md:157–162`. Live evidence from this pass, the rule's first execution: (1) *wrong diff* — `/security-review` reads pending changes; a rule-4 cold pass reviews a landed delta on a clean tree, so it scanned the taker's brief, not the work; a design-time review has no diff at all; (2) *deferral breach* — the skill dumped the full brief, deferred section included, into the cold reviewer's context pre-draft: complying with lens 4 forcibly violated rules 1–2; (3) *null floor* — the skill's hard exclusion 16 excludes markdown documentation entirely, so for doctrine reviews the "mechanical floor" is definitionally empty and the text doesn't say so. Reconcile sharpened it: the `a059e49` body records a permissive grant ("If it is useful I'm happy for you to use it"); the delta's "the reviewer runs it" is the author's own escalation to a mandate — and it is the mandate that forces the misfire. Needs an execution shape per review type plus a scanner-inapplicable discharge line mirroring the lens's own, and a warning never to run it over a brief carrying deferred material before drafting.

**SL3 — MEDIUM — CONTRIBUTING template still carries the pre-delta scope sentence.** `docs/build/templates/CONTRIBUTING.md:42–44`: "reviews approach, assumptions and real-world behaviour, not just correctness" — no security & privacy, no scope mandate; the same house-practice sentence the delta amended in the reviews README. At pin bump a child's CONTRIBUTING and reviews README describe two different review scopes.

**SL4 — MEDIUM — "correctness only" survives as a legitimate review Type in the very file the delta amended.** `docs/build/templates/docs/reviews/README.md:58`: **Type** — "approach + assumptions" vs "correctness only" — a standing narrowing offer that bypasses the non-goals mechanism, contradicting the amended paragraph fourteen lines above it.

**SL5 — MEDIUM — the widest-scope mandate and "scoped and short" are unreconciled, and the sole narrowing lever sits in warm hands.** `docs/method/REVIEW.md:126–137` vs `:357`. The older economy sentence remains an available counter-cite for scope-shrinking; and in warm reviews the author writes the non-goals — the delta makes them the only legitimate narrowing without stating that a reviewer may treat a risk-fencing non-goal as itself a finding (rule 1 makes the brief's framing attackable; the scope paragraph doesn't extend that to non-goals explicitly).

**SL6 — LOW — the live-exercise impossibility claim carries no grounds burden** (seeded — SQ5, arrived via the scanner leak; attributed as such). `REVIEW.md:130–133`: the re-run fallback partially mitigates, but "wasn't possible" needs a stated ground, same shape as every other discharge the delta itself created. Attacks the encoding, not Mike's caveat.

**SL7 — LOW — wrap artefacts introduced by the delta.** `docs/build/templates/docs/reviews/README.md:24` (~90-char line in an 80-wrapped file); `docs/method/REVIEW.md:162–164` (three-word stub line "genuinely has no" left by `a059e49`).

### Reconcile — what the deferred material changed

Nothing overturned; two additions. SQ1≙A4/SL5, SQ3≙A3/SL2, SQ4≙A1→SL1 (sweep went wider, adding SL3), SQ6 covered plus SL4 beyond the seed — all in the committed draft before the deferred open, deferral order honoured on each. SQ2 was considered and deliberately closed without a standalone finding (the discharge line is a disagreeable act; the hollowing vector is SL1). SQ5 became SL6, honestly attributed as seeded. The intent record's framing note was honoured by re-deriving the gap audit from the diffs rather than taking its account; the commit bodies discharged A6 (the 2026-07-21 rulings are corroborated) and supplied SL2's permissive-grant-to-mandate escalation. Prior verdicts were not opened beyond the in-repo anchors the delta cites — the citations resolve, and the brief's non-goals bar re-litigating closed cycles.

### Follow-ups

1. SL1: bring `skills/review-brief/SKILL.md` to four lenses + scope mandate + scanner clause (and consider a mechanical parity check between the skill and `REVIEW.md`'s lens list — this drift class has now shipped twice).
2. SL2: rewrite the scanner sentence with an execution shape per review shape (pending-diff, landed-delta, design-time), a scanner-inapplicable discharge line, and the deferral-safety warning; decide mandate vs permissive to match the grant.
3. SL3 + SL4: sweep the two template surfaces; propagate at next pin bump.
4. SL5: reconcile "scoped and short" with the scope mandate; state that non-goals are attackable by the reviewer.
5. SL6, SL7: one-line fixes alongside the above.
6. All rulings are Mike's (rule 3 — self-authored doctrine); MAJORs present, so the cycle stays open after decisions land.
