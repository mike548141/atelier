# Cold review — REVIEW rule 4 (cold spawn for self-authored doctrine)

**Scope:** the doctrine hunks of commit `9fef4d4` (2026-07-15): (1) REVIEW.md
**rule 4** (*Self-authored doctrine earns a cold spawn, not just a cold
context*); (2) the rules lead-in rewrite ("rules 3–4 whenever the work is
self-authored doctrine — rule 3 however the review was commissioned, rule 4
governing who may commission it"); (3) the inline-review bullet's carve-out
("self-authored doctrine cannot take this path at all"); (4) MODEL-ECONOMICS'
sub-agent-section pointer clause ("Self-authored doctrine goes further: there
the spawn itself must be cold — a non-author starts the review"). Review both
edited docs at HEAD, whole, plus the delta. The record/ROADMAP/verdict-file
hunks in the same commit are bookkeeping, in scope only for consistency with
the doctrine text.

**Commissioning note (rule 4's own terms):** the rule under review is
agent-drafted doctrine, so its review could not be warm-spawned. This brief is
written by a **non-author** — a neutral session the principal opened and
pointed at the queued item; the author session neither started nor instructed
it. The independence rules still bind in full: commit your own attack surface
to your draft first; treat this brief's framing, including its account of the
delta, as attackable; open no prior verdict text until your own findings are
committed.

**Intent source, sequenced:** rule 4's wording was drafted from the
principal's stated intent (tiered ruling, highest-stakes category explicit).
**After** your findings are committed, open
`2026-07-15-0910-model-economics-triple-delta.md` § *Decision* → *F1 ruling
RESOLVED* and check **fidelity to intent**: does the drafted text encode the
ruling faithfully — nothing added the principal didn't rule, nothing ruled
that the text drops? Fidelity gaps are findings.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (REVIEW rule 3) — recommend, apply nothing.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict below the second `---` divider.

---

## Deferred — commissioner's questions (open only after your attack surface is committed)

- Q1. Is "a neutral session the author neither started nor instructed"
  operationalisable? "The author" is defined by judgement, not commit
  metadata — across sessions of the same model, when does a later session
  *become* the author's continuation (e.g. it read the author's records and
  plans)? Can a session self-certify neutrality?
- Q2. "A scheduled batch" — if the *author* queues the brief into the batch,
  the brief still carries the author's framing and the schedule was
  author-instructed. Does the rule's spawn test catch that, or is the batch a
  laundering channel?
- Q3. The three named spawners (principal / batch / neutral session) — is
  that list exhaustive by design, and does it compose with CONCURRENCY's
  claiming rules and the ROADMAP `⏳ Mike triggers it` convention without a
  seam?
- Q4. Does the rule state what the *author* still owes when it finishes
  doctrine work it cannot spawn review for — write the brief? queue the
  pointer? — or does work now silently stall between "authored" and
  "reviewed"?

---

## Verdict — cold pass 2026-07-15

**Reviewer provenance & process disclosure.** This pass was spawned by the
principal via a neutral commissioning session (the brief is that session's
uncommitted work; the author session's last act, 9fef4d4, queued the ROADMAP
pointer and stopped — consistent with rule 4's own terms, though not
independently provable from metadata; see F5). One sequencing breach to
disclose per the apex: the file read of this brief returned it whole, so the
deferred questions were visible before my attack surface was drafted. The
attack surface below was built from the doctrine at HEAD and the doctrine-only
delta of 9fef4d4, and committed to a durable draft before the ruling record
was opened; where it overlaps Q1–Q4 I claim convergence, not independence.
Both triple-delta verdict files stayed unopened until after that commit;
only 0910's finding-F1 text, author's counsel, and §Decision were then read
(fidelity source), not its verdict body beyond that.

**Scope covered.** REVIEW.md and MODEL-ECONOMICS.md at HEAD, whole; the
doctrine hunks of 9fef4d4; ROADMAP/SESSIONS hunks for consistency; 00-APEX,
CONCURRENCY for composition. No fixes applied anywhere — self-authored
doctrine, all findings the principal's (rule 3).

### Attack surface (committed to draft first)

- A1. Spawner identity is treated as the independence locus, but the REACH
  mechanism the rules are grounded in is *framing through the ask* — and rule 4
  says nothing about who writes the brief for rule-4 work.
- A2. "A scheduled batch" sits in the non-author list with no qualifier on who
  queues or schedules it; "neither started nor instructed" grammatically
  attaches only to the neutral-session item.
- A3. No provenance/verification hook — compliance is author-side, at spawn
  time, invisible to the reviewer and the durable record unless volunteered.
- A4. The author's post-work obligations (write the brief? queue the pointer?)
  are unstated — the gap between "authored" and "reviewed".
- A5. Rule 4 restates rule 3's doctrine-by-function definition and extends it
  (behaviour-stamping template/skill) while citing "(rule 3's definition)".
- A6. Lead-in verb "commission" vs the rule's operative verb "spawn".
- A7. Companion passages unswept: MODEL-ECONOMICS §Triggering reviews; REVIEW
  §When to review heading; the "Applying decisions to doctrine" paragraph.
- A8. ROADMAP "⏳ Mike triggers it" is narrower than the rule's three paths;
  neither names the other.
- A9. Grounding: ruling-grounded and honestly attributed (legitimate under
  this repo's standard) — held, no finding.
- A10. Wording: "authored by the agent under review's own judgement".

### Fidelity to intent (0910 §Decision, *F1 ruling RESOLVED*)

The ruling's operative sentence: self-authored doctrine "earns a full ban on
warm spawns: its review must come from **a session the author neither started
nor instructed**." That is a single universal criterion.

- ✅ Tiered structure encoded: routine work keeps warm-spawn-plus-deferral;
  the ban lands only on doctrine-by-function. Faithful.
- ✅ Highest-stakes category stated plainly in the rule, as directed —
  including "behaviour-stamping template/skill", which IS in the recorded
  ruling (so the category itself is ruled, not drafted; the remaining defect
  is rule 3/rule 4 divergence — F4).
- ❌ **Fidelity gap (feeds F1):** the drafted rule renders the ruling's single
  criterion as an enumeration — "the principal, a scheduled batch, or a
  neutral session the author neither started nor instructed" — with the
  qualifier reaching only the third item. Under the ruling, an
  author-scheduled, author-briefed batch is a session the author *started and
  instructed* and is barred; under the drafted text it reads as sanctioned.
  The enumeration encodes less than the principal ruled, on the rule's
  strongest edge.
- ⚠️ Drafted-not-ruled additions, benign: the in-rule rationale (compliance
  residual, blast radius) matches the walk-through's framing; "the principal"
  as a named spawner trivially satisfies the criterion.

### Reconciliation with the commissioner's deferred questions

- **Q1** → converges with A3/F5. "Neither started nor instructed" needs a
  causation test, not an information test: a later same-model session that
  read the author's records has inherited *context*, not the authorship whose
  blind spots are in question — but the doctrine says neither this nor its
  opposite, and pure self-certification is weak. The check that actually
  works is the one this brief modelled: a commissioning note plus durable
  provenance the verdict records (F5).
- **Q2** → converges with A2/F1, and the fidelity check settles it: the
  ruling's criterion catches the author-queued batch; the drafted text does
  not. As written, the batch is a laundering channel.
- **Q3** → the list should not be exhaustive-by-enumeration at all — the
  ruling gives a criterion; the enumeration is the defect (F1). Composition
  with CONCURRENCY is clean (a reviewer session claims the `[~]` item as
  normal); the `⏳ Mike triggers it` convention is narrower than the rule and
  neither references the other (F8).
- **Q4** → converges with A4/F2. The rule states the ban, not the handoff;
  9fef4d4 improvised the right shape (ROADMAP pointer naming the delta and
  ruling record; brief written by a non-author) without doctrine requiring it.

### Findings

- **F1 — MAJOR — the batch spawner escapes the ruling's qualifier
  (laundering channel + fidelity gap).** Rule 4's enumeration lets an
  author-written brief, queued by the author into a batch the author
  scheduled, satisfy the rule's letter while the author keeps framing, timing
  and batch composition — the residual-compliance risk the rule exists to
  remove re-enters through its own example list, and the recorded ruling's
  universal qualifier ("a session the author neither started nor
  instructed") is dropped for two of the three named paths. The batched-queue
  bullet carries no rule-4 carve-out either. Direction to consider (Mike's
  call): restate the spawner test as the ruling's single criterion, with the
  named paths as examples that must each pass it.
- **F2 — MEDIUM — the author's handoff is unstated.** Rule 4 bans the spawn
  but not what the author owes on finishing rule-4 work: queue the ⏳ ROADMAP
  pointer (naming the delta and the ruling/intent record), and who writes the
  brief. Without it, work stalls silently between "authored" and "reviewed" —
  or defaults to an author-framed brief. 9fef4d4's improvised practice is the
  candidate text.
- **F3 — MEDIUM — companion passages not swept.** MODEL-ECONOMICS
  §Triggering reviews still sanctions inline background spawn unqualified
  (only §Sub-agents got the pointer — the exact single-doc-reader failure its
  own F1 flagged one cycle ago); REVIEW §When to review's heading ("the
  building model's call") is now false for one category; the "Applying
  decisions to doctrine" paragraph ("prefer an applier…", "earns a cold
  pass") is not reconciled with rule 4 — it leaves open whether an applier
  session may spawn the application review of self-authored doctrine, which
  rule 4's terms appear to bar.
- **F4 — MEDIUM — doctrine-by-function is now defined twice, divergently.**
  Rule 4's list includes "a template or skill that stamps behaviour into
  other repos" (which the ruling includes) while citing "(rule 3's
  definition)" — but rule 3's list stops at CI gate. Either rule 3's
  definition is canonical and must gain the item, or rule 4 restates what it
  claims merely to cite. Single-source it; the repo's own canonicality
  discipline says so.
- **F5 — MEDIUM — no provenance hook or neutrality test.** Nothing requires
  the spawn provenance (who commissioned, who spawned, the author's
  non-involvement) be recorded in the brief or verdict, and "neither started
  nor instructed" is undefined against artefact-mediated instruction. The
  rule's own enforcement is author compliance — the very residual it names —
  so the durable record is the only audit surface; require the commissioning
  note this brief modelled.
- **F6 — LOW — lead-in says rule 4 governs "who may commission"; the rule's
  test is who *spawns*.** A principal-commissioned, author-session-spawned
  review passes the lead-in and fails the rule. Align the verbs on "spawn".
- **F7 — LOW — wording.** "work … authored by the agent under review's own
  judgement" — clumsy possessive, and it is the work, not the agent, that is
  under review. Rule 3's "self-authored" phrasing is cleaner.
- **F8 — LOW — the `⏳ Mike triggers it` convention and rule 4 don't name
  each other.** The ROADMAP convention is narrower than the rule's three
  paths; an autonomous neutral session taking a ⏳ item is neither clearly
  licensed nor clearly barred. One sentence in either place closes it.

### Verdict

**PASS-WITH-FINDINGS — 1 MAJOR · 4 MEDIUM · 3 LOW.** The tiered ruling is
faithfully encoded in structure and category; the rule is grounded, honestly
attributed, and lands the ban where it pays. The MAJOR is a drafting gap, not
a mis-build: the enumeration of sanctioned spawners is weaker than the
criterion the principal actually ruled, and the batch path as written can be
staged end-to-end by the author. Per the close rule a MAJOR keeps this cycle
open; all findings are the principal's to decide (rule 3) — nothing has been
applied.

---

## Decision (Mike, 2026-07-15) — F1–F8 ruled as counselled; applied

Mike accepted the reviewer's suggested direction on all eight findings.
Applied same day by the commissioning session — which authored neither rule 4
nor this verdict, though it did write this brief; named per the
applier-independence preference, not hidden.

- **F1 [fixed]** — rule 4's spawner enumeration replaced by the ruling's
  single criterion as the test (**the review comes from a session the author
  neither started nor instructed**), with the principal / scheduled batch /
  neutral session recast as examples that must each pass it; the
  batched-queue bullet gains the matching carve-out (an author-queued,
  author-scheduled batch is still an author spawn).
- **F2 [fixed]** — the author's handoff written into rule 4: queue the
  ROADMAP `⏳` pointer naming the delta and the intent record, then stop;
  the non-author who takes the item writes the brief.
- **F3 [fixed]** — companions swept: MODEL-ECONOMICS §Triggering reviews
  gains the rule-4 exception and drops "the building model's call" from its
  heading, as does REVIEW §When to review (the qualifier moved into the
  lead); the "Applying decisions" paragraph now states the application
  inherits rule-4 status — the applier queues, never spawns, its own
  application review.
- **F4 [fixed]** — doctrine-by-function single-sourced in rule 3, whose list
  gains the behaviour-stamping template/skill item (in the recorded ruling
  all along); rule 4 now cites the definition without restating it.
- **F5 [fixed]** — provenance requirement written into rule 4: the brief
  states who spawned the review and the author's non-involvement, the
  verdict repeats it; no provenance trail ⇒ unauditable ⇒ non-compliant.
- **F6 [fixed]** — lead-in verbs aligned on *spawn*.
- **F7 [fixed]** — "authored by the agent under review's own judgement"
  replaced with rule 3's self-authored phrasing.
- **F8 [fixed]** — rule 4 names the `⏳` convention and licenses any
  criterion-passing spawner to take a queued item; the pass that produced
  this verdict is recorded in the rule as the worked example.

1 MAJOR at the cold pass ⇒ the close rule does not close the cycle on this
ruled application: the applied batch earns its own cold pass. Per rule 4 as
now written the applier cannot spawn that pass — it is queued on the ROADMAP
(`⏳`) for a non-author to take; the delta for that pass is the application
commit.
