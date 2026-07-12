# Review brief — the applied independence-batch edits

**Author-commissioned** (the session that applied the edits wrote this brief).
Under the rules these edits encode: this brief scopes what the work is; it
seeds no attack questions; the reviewer chooses its own attack surface, must
not let this brief's framing — including its account of what the work is —
steer or bound what it considers, and reads the prior verdicts only after its
own findings are committed (reconciling dispositions is reconcile-step work).
Findings on this work route to Mike, the principal, for disposition.

## What the work is

Commit `4c7ea9c` (2026-07-13) edited `docs/method/REVIEW.md` and one clause of
`docs/method/PROPAGATION.md`. The author's account of the change: it applies
the principal's disposition of fourteen findings from two prior cold reviews
(`reviews/2026-07-12-review-independence.md`, I1–I7;
`reviews/2026-07-13-review-doctrine-second-pass.md`, F1–F7), including one
fork the principal decided directly (whether a work's author may seed
questions for its reviewer) with a strengthening of his own wording. That
account is the author's claim, not settled scope.

## Scope

The two edited files at HEAD, as doctrine in their own right, plus whether the
edits are faithful to the recorded dispositions (reconcile step).

---

## Verdict: **PASS-WITH-FINDINGS**

**Reviewer:** fresh-context agent, 2026-07-13. **Scope:** `REVIEW.md` and `PROPAGATION.md` at HEAD as doctrine in their own right, plus fidelity of commit `4c7ea9c` to the recorded dispositions.

**Independence note.** The attack surface below is my own, chosen before weighing the brief. I treated the brief's account of the work ("applies the principal's disposition of fourteen findings… with a strengthening of his own wording") as a claim to test, not settled scope. The load-bearing assumptions I named and attacked: (a) that the rule-1 strengthening actually neutralises the influence mechanism it names; (b) that rule 3's binding condition is correctly scoped; (c) that the standing strengthen/weaken test would have fired on the very case that grounds the rule; (d) that the review-of-the-application ceremony terminates; (e) that rule 2's bar is honourable at all when the work under review *is* a disposition-application commit. Siblings checked at HEAD: 00-APEX, PROPAGATION, MODEL-ECONOMICS, EVIDENCE, AUTONOMY, PRINCIPLES, REACH.

**One honest disclosure, which is itself finding G5:** rule 2 bars prior verdicts until findings are committed, but `git show 4c7ea9c` — the delta I was directed to review — necessarily contains both prior verdicts' Disposition sections and ticked checklists. I was exposed to the principal's framing of I1–I7/F1–F7 before drafting, with no way not to be. My findings were committed to a durable draft before the two verdict files were opened in full; the reconciliation section below was written last.

The applied batch is sound work: 14/14 findings are addressed in substance, the floor-not-fence resolution is coherently threaded through rule 1, step 1, and the inline-spawn section, and one application judgement call was made *well* (F2's literal recommended wording, drafted before the fork was decided, was harmonised with the floor-not-fence disposition rather than applied verbatim — the right call, faithful to the disposition over the stale letter). I could not unseat the spine. The findings below are seams, three of them in the newly decided material itself.

## Findings

### G1 — MEDIUM (approach): the rule-1 strengthening's remedy doesn't match its own premise, and it is behavioural where the house demands structural

Rule 1 states the mechanism precisely — seeded questions influence *"by their very existence — their topic and tone suggest where 'the risk' lives"* — and then prescribes an ordering of the reviewer's attention: choose your own surface *"before weighing the author's list"*. But if existence influences, the influence lands at **read time**, before any choosing; a reviewer that has read the brief cannot un-read the questions, and reordering its subsequent attention does not undo exposure priming. The premise defeats the remedy as stated.

The doctrine already owns the structural answer and applies it one rule down: rule 2 defers *prior verdicts* to after findings-committed at the **artifact** level. Seeded questions get no equivalent, only an intent instruction — exactly what the siblings warn against (EVIDENCE §12: "intent is not a control"; AUTONOMY: "encode the policy, don't just remember it").

**Fix:** encode the sequencing structurally — the brief template puts seeded questions in a deferred section (below the divider, or a separate file) the reviewer opens only after committing its own attack surface, mirroring rule 2's shape. Or, if the exposure is accepted as residual, say so honestly: the ordering rule is a mitigation, not a cure, and the standing re-run test is the real backstop.

### G2 — MEDIUM (coherence): rule 3 is conditioned on brief authorship, where its true condition is self-authored doctrine — and step 4 contradicts it

The umbrella sentence binds all three rules *"when the brief is written by, or on the framing of, the work's author… (rules 1–2 always; rule 3 on doctrine)"*. But rule 3's trigger has nothing to do with who wrote the brief: findings on self-authored doctrine go to the principal even when the review was principal-commissioned and un-briefed — which is precisely what the 2026-07-13 second pass *was*, and its findings were correctly routed to Mike despite the umbrella's condition not holding. Step 4's carve-out is (correctly) unconditional; the rules section and the lifecycle now state two different conditions for the same rule. The applied I5 wording is faithful to that finding's recommended fix — the residue is in the recommendation's shape, so this is a fresh defect, not an unfaithful application.

**Fix:** lift rule 3 out from under the brief-authorship trigger. The parenthetical becomes "(rules 1–2 whenever the brief carries the author's framing; rule 3 whenever the work is self-authored doctrine, however the review was commissioned)".

### G3 — MEDIUM (calibration): the standing test's trigger would not have fired on the case that grounds the rule

The strengthen/weaken test: *"an author-briefed review that passes clean earns an un-briefed re-run."* Per this same document, the author-briefed REACH pass **found five findings and still missed two MAJORs** — not "clean" on any plain reading, so the trigger as worded never fires on the motivating case, and the new "What review is not" text says finding count is the wrong test in both directions. The test's condition keys on the discredited metric.

**Fix:** define the trigger by risk or by the seeded axes, not by count — e.g. "an author-framed review of doctrine or structural work earns an un-briefed re-run regardless of its finding count; a pass that is clean *on the seeded questions specifically* is the strongest trigger". Each pair remains a data point.

### G4 — MEDIUM (completeness): the doctrine-review regress has no stopping rule, and the application step itself is unencoded

Ceremony-to-risk says doctrine text earns the full ceremony. Applying dispositions produces new doctrine text (this commit); its review (this review) produces findings; applying *those* is again a doctrine edit — unbounded in principle. The practice that bounds it today lives only in the ROADMAP entry and the disposition stamp ("a cold review of the applied batch was commissioned per the ceremony-to-risk rule"), not in REVIEW.md. Also unencoded: **who may apply** the principal's dispositions to self-authored doctrine — the batch was applied by a session that authored neither the doctrine nor the verdicts (a good pattern, currently just an accident of practice).

**Fix:** one paragraph in REVIEW.md: disposition application to doctrine is itself a doctrine edit and earns a cold pass; prefer an applier that authored neither the doctrine nor the verdicts; the cycle closes when a pass returns nothing above an agreed severity (e.g. no MAJOR), with remaining findings dispositioned into the backlog rather than spawning another full cycle.

### G5 — MEDIUM (internal): rule 2 cannot be honoured when reviewing a disposition-application commit, and the doctrine doesn't say so

The delta of an application commit necessarily carries the prior verdicts' disposition stamps — it did here, so this reviewer read the principal's framing of all fourteen findings before drafting, unavoidably. This extends F5 (disposition verification is reconcile-step work) to the shape F5's fix doesn't cover: in an application review, exposure happens at diff-read time, not at a step the reviewer can defer. As the repo now routinely reviews applied batches, this shape recurs.

**Fix:** sequencing guidance in REVIEW.md or the brief template for application reviews — review the doctrine files at HEAD and commit findings before opening the verdict-file hunks of the delta — or name the exposure as an accepted residual the reconcile step absorbs.

### G6 — MINOR (overclaim): "The rules presuppose the two are *distinct*" — only rule 3 does

Rules 1–2 bind and deliver value when author and principal are the same person (a solo operator can still let the reviewer choose its surface and bar prior verdicts); the text itself narrows to "rule 3 gives nothing" one sentence later. I2's recommended fix said "the rule presupposes" (singular); the applied text pluralised it. **Fix:** "Rule 3 presupposes the two are distinct."

### G7 — MINOR (staleness): the F4 fix stopped one line short in PROPAGATION

The enforcement clause now correctly points at REVIEW.md without restating — but the same paragraph still says *"the review lifecycle owed in the ROADMAP"*. The lifecycle is delivered in full in REVIEW.md, and the ROADMAP item is ticked `[x]`. A reader of PROPAGATION alone inherits a stale "owed". **Fix:** drop the clause or point at REVIEW.md's lifecycle section. *(NOTE, pre-existing, harvest:* REVIEW.md's "Whether a change earns a review at all" and MODEL-ECONOMICS' "Match the ceremony to the risk" carry near-duplicate earns-review taxonomies — a one-fact-two-homes seam the F4 rationale leaves standing; worth a one-way pointer some day.)*

### G8 — NOTE (drift): the trigger is glossed two ways

Section: *"written by, or on the framing of, the work's author"*. Step 1: *"written by, or dictated by, the party whose work is under review"*. "On the framing of" is wider (covers a third party steeped in the author's records); "dictated by" is narrower. Pick one phrase and reuse it.

### G9 — NOTE (ambiguity): "until its own findings are committed" — committed to what?

For a background-agent reviewer there is no git commit of its own. Say "committed to its draft (durably written), before any prior verdict is opened" — this review had to interpret it exactly that way.

## Follow-up checklist

- [x] G1 — encode deferred-seeded-questions in the brief shape (or state the ordering rule as mitigation-not-cure with the re-run test as backstop)
- [x] G2 — decouple rule 3's condition from brief authorship; align with step 4
- [x] G3 — re-key the standing test's trigger off finding count (risk- or seeded-axes-keyed)
- [x] G4 — encode the application-earns-review rule, the neutral-applier preference, and a cycle-stopping rule
- [x] G5 — sequencing guidance for application reviews (delta carries dispositions)
- [x] G6 — "Rule 3 presupposes", singular
- [x] G7 — drop/repoint PROPAGATION's stale "lifecycle owed in the ROADMAP"
- [x] G8 — unify the trigger gloss
- [x] G9 — define "committed" as durably-drafted

## Reconciliation (written last, after reading both prior verdicts and their dispositions)

**Were the dispositions faithfully applied?** Yes — 14/14 in substance. I1 (floor-not-fence + the principal's strengthening, framing-attackable) ✔ rule 1 and step 1; I2 ✔ (with the G6 pluralisation wobble — the fix wording said "the rule", the text says "the rules"); I3 ✔ doctrine-by-function, policy-as-code escape closed; I4 ✔ findings-committed headline; I5 ✔ as recommended (G2's residue sits in the recommendation's own shape, carried forward faithfully); I6 ✔ "proved" → "showed"/"evidence, not proof"; I7 ✔ same-act-two-views in step 4. F1 ✔ show-your-work test with the manufacture-findings pressure named; F2 ✔ applied in harmonised form — its literal pre-fork wording ("scopes what the work is and stops") was correctly superseded by the floor-not-fence disposition, a faithful-to-the-disposition deviation worth recording as the right pattern; F3 ✔ all three confounds verbatim plus the standing test (whose trigger G3 now challenges — a defect in the recommendation, faithfully applied); F4 ✔ (G7: one adjacent stale clause unswept); F5 ✔; F6 ✔ in both rule 3 and step 4; F7 ✔ re-seated.

**Did the edits introduce new defects?** One clear candidate: the standing test's count-keyed trigger (G3) is new text at HEAD, though it transcribes F3's own recommended wording. G1 attacks the principal's strengthening itself, which postdates both reviews — neither prior pass could have reached it. G2 and G5 are pre-existing seams the batch narrowed but did not close.

**Does reading the priors change my verdict?** No. My G5 independently extends the second pass's F5 to the application-review shape; my G3 lands on the same territory F1 cleared (count is the wrong test) and shows the F3 fix reimported the metric F1 evicted — the two dispositions, both faithfully applied, are in quiet tension at HEAD, which is itself evidence the batch earned this cold pass. Both prior verdicts and this one land on the same tier for the same reason: the spine holds; the seams that remain are in the newest, least-exercised material. None of G1–G9 blocks the doctrine from operating; G1–G5 should land before the independence section is cited as standalone authority.

Per rule 3, these findings are Mike's to disposition; this reviewer applies nothing.

---

## Disposition (2026-07-13, Mike — the principal)

All nine **[fixed]**, applied same day by the batch's applier at Mike's
direction. Two rulings of Mike's own are now doctrine:

- **G1 [fixed — Mike endorsed the structural fix]:** seeded questions live in a
  deferred section below the brief's divider, opened only after the reviewer's
  own attack surface is committed — deferral by structure, not willpower.
- **G4 [fixed — extended by Mike]:** the cycle closes when a pass returns no
  MAJOR (this pass did — the cycle is closed; this application spawns no
  further ceremony), *plus his escape valve*: if the MAJOR count is not falling
  from pass to pass, stop cranking and ask the principal for direction.
- **G2, G3, G5–G9 [fixed]** as recommended: rule 3 reconditioned on
  self-authored doctrine however commissioned; the standing test re-keyed off
  finding count; application-review sequencing stated with the residual
  exposure named; "rule 3 presupposes", singular; PROPAGATION's stale
  "lifecycle owed" repointed; the trigger gloss unified; "committed" defined
  as durably-drafted.
