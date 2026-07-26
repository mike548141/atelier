# Cold review (rule 4) — EVIDENCE §13: escalation is beside the ladder, not a rung

**Subject (refs only):** the paragraph added to `docs/method/EVIDENCE.md` §13
(the source-acquisition ladder) before its blocked-from-climbing clause,
landed in commit `5915e73` (2026-07-26). Establish the exact hunk with
`git show 5915e73 -- docs/method/EVIDENCE.md` and review it at HEAD, in the
context of the whole section and its siblings.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub. Nothing evaluative from
either appears above the divider.

**The reviewer's first acts:** establish what the paragraph claims and why
from the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`) — for a one-paragraph doctrine delta the heavy
lenses are 1 (is beside-the-ladder the right model, and does the paragraph
bind where a session actually faces the choice) and 3 (coherence with the rest
of §13, §14, the escalation language elsewhere in `method/` — does any sibling
still teach the rung model, and does this paragraph contradict or duplicate an
existing rule).

**Re-run obligations:** `python3 tools/floor.py --plane ci` (whole-tree floor
at HEAD) · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js`. Lens 4: a landed one-paragraph markdown
delta — `/security-review` reaches only pending diffs and excludes markdown,
so discharge it in one explicit line with grounds; state whether the paragraph
has any security/privacy surface at all.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below — and the intent record it names — only after your
findings are durably written to this file; then append the reconcile, named
as such.

Findings carry stable IDs (**EE1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored doctrine: REVIEW.md rules 3–4 govern — findings are the
principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-26-0100-ccrepo-context-column.md`](../sessions/2026-07-26-0100-ccrepo-context-column.md)
§ Addendum — the paragraph was captured after the principal's correction of an
escalation the session had handed up.

---

## Reviewer's attack surface (named before the lens work; cold, Fable)

Established the subject myself from `git show 5915e73 -- docs/method/EVIDENCE.md`
and re-read at HEAD (`docs/method/EVIDENCE.md:189-208`, inside §13, above the
blocked-from-climbing clause). Load-bearing assumptions I will attack:

1. **The model itself** — "beside the ladder" assumes climbing and escalating
   are sequential alternatives (escalate only once genuinely blocked), not a
   parallel track (ask while climbing) and not a top rung. Is that the right
   model for every stakes level, including time-critical ones?
2. **Exhaustiveness of the escalation grounds** — the opening sentence's
   trigger ("the climb is genuinely blocked") versus the enumerated grounds
   ("no authoritative source exists" / genuine contest / principal's by right):
   does the list cover *source exists but is genuinely unreachable to the
   agent* (paywalled, credential-gated, tool absent)? If not, the two halves of
   the paragraph disagree about when escalation is legitimate.
3. **Collision with the clause below it** — the pre-existing paragraph says
   blocked-from-climbing is "a gap to *state*"; the new one says blocked is
   when escalation is reached. Do they compose (state the gap AND hand up at
   stakes) or contradict?
4. **Point-of-use binding** — the failure fires at the hand-off moment, which
   other method docs may govern (communication/hand-back rules, autonomy
   floors, any fail-noisily/hand-up doctrine). Does a sibling teach "when
   unsure, ask" or a hand-up ladder without this test, so a session in that
   doc's flow never meets the rule? Does any sibling still teach the rung
   model?
5. **Duplication** — does an existing rule already say "do the lookup before
   the hand-off" (one fact, one home)?
6. **The cited ban** — the grounding example leans on "the ban on fitting a
   number to one's own measurement"; verify that ban exists in doctrine a
   reader can find from here, and that the fitting/reading distinction
   restates it rather than quietly amending it.
7. **Scope wording** — the test is phrased for "a missing value"; does that
   narrow the rule below its intended scope (any fact-lookup, not only
   numbers)?
8. **Security/privacy surface** — the paragraph quotes the principal's words
   verbatim in a public repo; check it against the no-personal-data boundary.

Re-run obligations to discharge: `python3 tools/floor.py --plane ci`,
`python3 -m unittest discover -s tools`, `node --test instruments/*.test.js`,
and the lens-4 one-line discharge for `/security-review` on a landed markdown
delta.

---

## Cold verdict (Fable, 2026-07-26)

**PASS-WITH-FINDINGS — 0 major · 3 minor · 2 nits.**

### Re-run obligations, discharged

- `python3 tools/floor.py --plane ci` — 9/9 enforced, exit 0. One sizescan
  size-advisory (`docs/ROADMAP.md` 1582 lines) — advisory class, never gates,
  pre-existing at HEAD, not attributable to the subject.
- `python3 -m unittest discover -s tools` — 694 tests, OK.
- `node --test instruments/*.test.js` — 207/207 pass, 0 fail.
- **Lens-4 discharge, one line with grounds:** `/security-review` was not run —
  it reaches only pending diffs and excludes markdown; the subject is a landed
  one-paragraph markdown delta, so its pass would be definitionally empty
  (`docs/method/REVIEW.md:180-192`), and running it here would scan this dirty
  brief, the exact SL2-grounded caution. The paragraph itself has **no security
  or privacy surface**: the quoted principal sentence is a work instruction
  about public model pricing — no personal, health, family, or financial
  detail; the public-repo boundary holds.

### Findings

**EE1 (minor) — the test's enumeration omits the trigger its own opening
establishes.** *Claim:* the escalation grounds list ("no authoritative source
exists", a genuine contest, the principal's call by right — "never on 'I don't
have the number in front of me'", `docs/method/EVIDENCE.md:199-201`) reads as
exhaustive, but omits the case the opening sentence licenses: the source
*exists* and the climb is *genuinely blocked* (paywall, credential wall, tool
absent) — `EVIDENCE.md:189-190`. *Evidence:* `REACH.md:50-51` makes exactly
this ask legitimate (rung 6, "full manual fallback", block-gated), and the
clause below at `EVIDENCE.md:210-212` handles blocked-climb as a gap to state
without saying whether the hand-up is then permitted. *Counsel:* add the
blocked-with-existing-source ground to the enumeration, phrased as a **fetch
request that states the gap** — still not a decision handed up.

**EE2 (minor) — the model's strongest justification is unstated, leaving a
surface contradiction with two sibling ladders where the human IS a rung.**
*Claim:* `REACH.md:50-51` ("6. Ask the operator") and `ECONOMICS.md:247` ("the
ladder ends at the principal") both make a human the terminal rung of their
ladders; "not a rung on this ladder" invites a fast reader to see doctrine
disagreeing with itself. The reconciliation is derivable but unwritten: §13's
rungs are ordered by **evidential strength**, and the principal's from-memory
answer is itself reported/secondary tier (`EVIDENCE.md:35-51`, `:72-81`) —
asking moves the question *sideways*, not up, whereas reach orders pipes by
cost and economics orders workers by capability, where a human rung is
coherent. `REACH.md:65-69`'s existing no-conflict note reconciles only the
*climb* maxim and predates this paragraph. *Counsel:* one bridging sentence in
the paragraph (the principal's recollection is reported-tier — asking cannot
climb this ladder) and/or extend REACH's no-conflict note to cover the beside
model.

**EE3 (minor) — the rule may not bind where the choice is faced.** *Claim:* a
lookup dressed as a judgement call reaches the principal through the hand-up
passages, and neither points here: `ECONOMICS.md:247-252` ("route the work
up... when every tier is out of its depth") and `AUTONOMY.md:117-121` (how to
shape an ask) carry no pointer to §13's one-question test, so a session in
those flows never meets it. *Evidence:* the brief's own lens-1 question; the
repo's otherwise-dense cross-pointer style. *Counsel:* a one-clause pointer in
ECONOMICS' hand-up bullet — a hand-up whose payload is a missing *fact* first
passes EVIDENCE §13's test — and optionally the same in AUTONOMY's
name-both-sources paragraph.

**EE4 (nit) — the cited ban has no locatable doctrinal home.** *Claim:*
"citing the ban on fitting a number to one's own measurement"
(`EVIDENCE.md:204`) uses the definite article for a rule that appears nowhere
in `docs/method/`; its only repo home is `tools/sizescan.py:117` (budgets
"GROUNDED in the file's *class*, never derived from the file's current
length") — an instance rule for size budgets. A shareable-doctrine reader
cannot follow the reference. *Counsel:* gloss the ban in half a clause inline,
or name where it lives; promote it to general doctrine only if that is
actually intended.

**EE5 (nit) — numeric phrasing narrows the read.** *Claim:* the test is
phrased for numbers ("a missing value", "the number in front of me",
`EVIDENCE.md:197-201`) while the failure class is any fact-lookup (a date, a
flag name, a licence term); the opening sentence is already general ("the
question"). *Counsel:* "value" → "fact" in the test sentence, or a short "any
fact, not only numbers" gloss.

### What held

- **Lens 1:** beside-the-ladder is the *right* model for this ladder — the
  rungs measure evidential strength and the principal's answer cannot climb
  that axis (it is the finding EE2 asks the text to say aloud). The paragraph
  addresses a real, grounded failure mode and sits at the ladder's canonical
  home, in the correct position (not-a-rung → test → blocked-handling composes
  cleanly with the pre-existing clause).
- **Lens 2:** the paragraph's account matches the delta commit's own narrative
  (`5915e73`); no overclaim, no silent scope-cut found. Caveat, owned: the
  verbatim principal quote could not be checked against the session record
  within the reading discipline (`docs/sessions/**` barred pre-unlock); the
  commit message corroborates the incident's substance.
- **Lens 3 sweep:** no sibling in `docs/method/` teaches principal-escalation
  as a rung of the *acquisition* ladder; no existing doctrine duplicates the
  do-the-lookup-first rule; the §11/§13 stakes interplay is untouched by the
  insertion.
- **Lens 4:** no security/privacy surface (discharged above); floor, unit, and
  instrument suites all green at HEAD.

Findings are counsel — the principal decides; nothing applied in this pass.

---

## Reconciliation (post-unlock: deferred section + intent record read)

Read after the verdict above was durable: the brief's deferred section and
`docs/sessions/2026-07-26-0100-ccrepo-context-column.md` § Addendum 0210. The
withdrawn-directory ban was honoured throughout, including this phase.

- **EE1 — sharpened, kept.** The intent record states the narrow single-trigger
  form explicitly (*"The trigger for handing up is 'no authoritative source
  exists', not 'I don't have the number in front of me'"*, sessions
  record :143-146). The enumeration's omission of the
  blocked-with-existing-source ground is therefore faithful to the recorded
  intent, not a transcription slip — the counsel stands but is now a proposed
  *widening* of the intent, for the principal to weigh as such.
- **EE2 — kept, unchanged.** The addendum reasons entirely inside EVIDENCE
  §13; nothing there addresses the REACH rung-6 / ECONOMICS
  ladder-ends-at-the-principal surface tension or states the reported-tier
  justification.
- **EE3 — kept, unchanged.** No pointer from the hand-up passages was intended
  or landed; the record adds nothing either way.
- **EE4 — kept, unchanged.** The addendum's fitting-vs-reading table
  (sessions record :138-141) is the ban's origin, but it names no doctrinal
  home either; the reference in the landed paragraph remains unfollowable from
  `docs/method/`.
- **EE5 — kept, unchanged.** The grounding incident was numeric (a price),
  which explains the phrasing; the delta commit's own framing ("a fact to
  fetch") supports the generalisation the counsel asks for.
- **EE6 — added (nit): the verbatim-marked quote silently drops two words.**
  *Claim:* the paragraph quotes the principal as *"Isn't there an API or web
  page you can reference?"* (`docs/method/EVIDENCE.md:206`) while the intent
  record has *"...you can reference from anthropic?"*
  (sessions record :129-130). One of the two is not verbatim, and the doctrine
  version marks no elision. Likely a deliberate vendor-neutral trim for
  shareable doctrine — fine, but then it should elide visibly or paraphrase.
  *Counsel:* align the two, or mark the elision (…) in the doctrine quote.
- **Lens-2 caveat discharged.** The verdict's owned caveat (quote unverifiable
  within the reading discipline) is now resolved by the unlock-phase check —
  its resolution is EE6.
- **Withdrawn: none.**

Post-reconciliation verdict unchanged in class: **PASS-WITH-FINDINGS — 0 major
· 3 minor · 3 nits** (EE6 added at nit).
