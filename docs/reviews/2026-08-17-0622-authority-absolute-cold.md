# Cold pass — the apex: authority absolute, rulings conditioned

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the delta rewrites the
apex section that governs how the principal's word binds, plus its five
restatements and the child-facing floor block; self-authored doctrine by
function, in the authoring session's wording, carrying a ruling quoted from
the principal).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection: a session that cannot honour the bar stops rather than takes.
**Status:** REVIEW RUN 2026-08-17 — **PASS-WITH-FINDINGS, 0 MAJOR /
2 MODERATE / 2 minor / 4 notes (AA6–AA13)**. Verdict and reconcile below;
sibling folded in and deleted. AA6–AA13 go to the principal's ruling round
(rule 3); no MAJOR ⇒ the ruling application is terminal and the cycle closes.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `authority-absolute-0815`; Fable tier per the commit
  trailers on `38add7c` and `c782e14`).
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 for the
  fleet board-split rollout, and then asked, mid-session: *"Are there any
  briefs that need to be written?"* and *"If so please write them for a cold
  review."* That session authored no part of this delta, was neither started
  nor instructed by the authoring session, and has not edited any file this
  delta touches. It wrote this brief from the two commits and the queue
  pointer only; it did **not** open the intent record
  (`docs/sessions/2026-08-15-1129-authority-absolute.md`) or the board item
  the pointer names.
- ⚠️ **Two disclosures the taker should weigh, both about the brief-writer,
  not the delta.**
  1. **It read the `SESSIONS.md` index entry for this delta** — early in the
     session, as a range grep over recent entries, before this brief was
     commissioned. That entry summarises the ruling and the surfaces. It is
     rule-2 barred material and it was read; it is the reason the intent
     record itself was left unopened, and it is why the seeded questions in
     the sibling are deliberately thin. Treat them as a floor, not a fence.
  2. **It is not on the Fable tier** — it is Opus. Brief-writing has been done
     at Fable in this repo's prior split passes (2026-08-15, 1024 UTC). The
     tier bar in REVIEW rule 4 is stated for the *reviewer*, and this is not
     the review; but the taker should satisfy itself that a brief written off
     the named tier is acceptable, and say so either way in its verdict. If
     it judges otherwise, the correct outcome is to rewrite the brief, not to
     run the review on a brief it does not trust.
- **Who takes the review:** the next cold session meeting rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier. The taker repeats its own provenance in the verdict: how it was
  spawned, and its non-involvement with both the authoring session and this
  brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling
  `2026-08-17-0622-authority-absolute-cold.deferred.md` (rule 1's split).
  Recommended: run under an orchestrator that holds the sibling's bytes and
  releases them only after the reviewer's findings are durably written. A
  taker working by hand opens the sibling as a deliberate second act after its
  findings are committed, and says so in the verdict. Fold in and delete when
  the verdict lands.
- **Adjacent passes, not this one.** The Laws-removal cold pass
  (`2026-08-15-1031-laws-removal-apex-cold.md`) reviews the *removal* that
  emptied the apex section this delta then rewrote, and its LR findings are a
  prior verdict — barred until reconcile. The board-store pass
  (`2026-08-15-1030-…`) touches none of these surfaces.

## What the work is

Two commits on `main`, merged as `81d7d04`. Reviewed at HEAD.

**`38add7c` — the authority correction.** The apex section *The principal's
authority is conditioned on being informed* is retitled *The principal's
authority is absolute; his rulings are conditioned on being informed* and
rewritten. The removed claim: that authority is *"not exercisable
uninformed"*. The replacement: the authority is absolute and never decays, the
agent can never overrule the principal in any situation including one where it
believes him uninformed, and what being informed conditions is the **ruling** —
challengeable on the briefing, and still challengeable by an independent review
session even when informed; a challenge is raised *to* the principal by
re-briefing, never by declining to obey. Restatements aligned in the same
commit: `RECORD.md`, `AUTONOMY.md`, `CONCURRENCY.md`, `REVIEW.md` rule 3, the
child floor block in `PROPAGATION.md`, and the byte-identical
`docs/build/templates/CLAUDE.md` stamp. The sharpest single change outside the
apex is in REVIEW rule 3: *"An approval given without that account is not a
decision the doctrine recognises"* became *"stands as the principal's word but
is open to challenge — on the briefing, never on his authority."*

**`c782e14` — the dilemma line returns.** *"Surface a genuine dilemma; never
silently resolve it"* — dropped with the Laws — is restored as an in-practice
bullet under `00-APEX.md` § *Honesty is absolute*, and to the child floor block,
the templates stamp (53 lines, stampscan identical) and the session-onramp
skill, under the **honesty** bullet rather than the Laws bullet it used to ride.

The commit messages state the ruling in the principal's terms and claim
`stampscan` identity between `PROPAGATION.md`'s floor block and the template
stamp. Both are the author's claims and are in scope as such.

## Scope

Widest the work admits. This delta changes **what the agent may do when it
believes the principal is wrong**, so the reviewable question is not only
whether the words are accurate but what they license and forbid at the moment
of use. In scope: whether "absolute and never decays" and "challengeable by
re-briefing" compose into a rule an agent can actually follow under pressure,
or leave a gap where an agent that disagrees has no sanctioned action; whether
the REVIEW rule 3 softening — from *not recognised* to *stands, open to
challenge* — is what the principal ruled or the author's reading of it, and
what it now permits that it previously forbade; whether the five restatements
say the same thing as the apex or five slightly different things; whether the
always-confirm floor and the ADR-acceptance path still work under the new
wording; whether the honesty framing carries the dilemma line as well as the
removed Laws framing did, or whether something the Laws caveat was doing is
now unowned; and what a session reading only the **child floor block** — which
is all most children get — will believe about its authority to refuse.

**Non-goals, and neither fences the risk:** the reviewer does not decide any
finding — findings are the principal's to rule on (rule 3), and this delta is
his own ruling being recorded, so counsel is welcome but must be labelled.
And the *substance* of the ruling is not under review; the account of it is.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself
   first. Is the authority/ruling split a real distinction or a restatement
   that dissolves at the point of use — what, concretely, does an agent DO
   when it holds a ruling it believes uninformed and re-briefing has already
   failed once? Does "never decayed by it" bound the number of times an agent
   may re-brief, and if not, is repeated re-briefing distinguishable from
   declining to obey? Does the doctrine anywhere say what happens when the
   principal declines to be re-briefed?
2. **Correctness & quality.** Read all seven surfaces at HEAD side by side
   with both diffs. Do the apex, `RECORD`, `AUTONOMY`, `CONCURRENCY`,
   `REVIEW` rule 3, the `PROPAGATION` floor block and the templates stamp
   agree — not merely avoid contradicting? Verify the byte-identity claim by
   running `stampscan` rather than reading it. Check whether any surface still
   carries the old "not exercisable uninformed" logic under other words,
   including skills, `docs/build/`, and the ADR corpus.
3. **Completeness / harvest.** Every surface that stated the old rule, and
   every surface that *relies* on it: the always-confirm floor list, the
   ADR acceptance path, the autonomy grant, the review-independence rules,
   the session-onramp skill, `CHANGELOG.md`. Does a CHANGELOG entry exist for
   both commits? Children inherit the floor block only at their next pin bump
   — is the resulting window stated anywhere a child session would see it?
   Does the restored dilemma line duplicate anything already in the honesty
   section under another name?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The delta quotes
   the principal at length and describes a governance relationship; check that
   nothing in the seven surfaces or the queue pointer joins a private repo's
   name to its posture, or carries personal context. Consider separately
   whether *this* change alters the safety posture: the always-confirm floor
   is the mechanism that stops irreversible action, and this delta touches how
   its stops may be challenged. If the lens has no surface beyond the public
   -tree check, discharge it in one explicit line with grounds. The house
   security scanner reads the session's pending diff whatever path it is aimed
   at (board item `160-…/190`); this is a landed-delta review, so state the
   reach case that applied rather than assuming one.

## Re-run obligation

Re-run, do not read: `stampscan` at HEAD, to test the byte-identity claim
between the `PROPAGATION.md` floor block and `docs/build/templates/CLAUDE.md`
— and note that `stampscan`'s verdicts are themselves under a standing finding
(board `115/030`: its verdicts are inverted against the doctrine it enforces),
so read its output against the files, not only its exit code. Run the full
suite and the floor on both planes at HEAD; lift the invocations from
[`.githooks/pre-commit`](../../.githooks/pre-commit) and
`.github/workflows/ci.yml` rather than guessing them. Grep the tree for the
old wording and for the removed *"not a decision the doctrine recognises"*
formulation. Check at least one real child's `CLAUDE.md` for which version of
the floor block it currently carries, and say which.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the Laws-removal pass especially), the
intent record for this delta, and the board item
`160-…/200-apex-authority-absolute-rulings-conditioned.md`, which carries the
ruling verbatim and the author's account. The sibling `.deferred.md` holds
those references and the brief-writer's seeded questions; open it after your
findings are committed. Reconcile after, never anchor before. A taker whose own
session onramp has already read the `SESSIONS.md` tail discloses that in the
verdict, as this brief-writer has.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `AA`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/210-rule-4-cold-pass-queued-authority-absolute.md`)
and rebuild the index in the same commit.

---

# Phase-1 verdict — 2026-08-17

## Provenance

- **Reviewer:** a **Fable** subagent, spawned 2026-08-17 by an atelier session
  Mike opened at 0710 UTC under his standing cold-session instruction ("do any
  review work and any work that is fable dependent … write briefs too if they
  are required"). This reviewer authored no part of the delta under review, and
  was neither started nor instructed by the authoring session (2026-08-15,
  Fable, wt: `authority-absolute-0815`) nor by the brief-writing session
  (2026-08-17, Opus, wt: `board-cmd-and-briefs`).
- **Orchestration shape — a departure, stated plainly so the principal can
  reject it on sight:** the orchestrator holding the deferred sibling and
  committing these records is **Opus, not Fable** — unlike the 2026-08-15
  precedent where both orchestrator and reviewers ran on Fable. The
  orchestrator forms no finding and writes no severity; it releases the
  sibling only after this verdict is durably committed. **Reviewer's one-line
  view on the tier bar:** rule 4 prices the *pass* — the lens work, findings,
  and severities — and all of that ran on Fable, so the bar is honoured in
  substance; but the shape departs from a precedent the principal set, so
  accepting it is his call, not this pass's.
- **The off-tier brief (disclosure 2), answered as asked:** acceptable, and I
  ran the review on it. The tier bar in rule 4 is stated for the reviewer;
  the brief is scoping, not findings, it quotes no barred material, its bars
  and re-run obligations are complete, and nothing in it steered a
  conclusion. I did not rewrite it.
- **The brief-writer's SESSIONS.md exposure (disclosure 1):** noted; it
  shaped only the sibling's seeded questions, which stay unopened until
  reconcile. It did not reach this verdict.

## Barred-material exposure — this reviewer's own, disclosed

1. **`git show 38add7c` run unfiltered** printed rule-2 barred material,
   because the delta commit itself packages it: the full intent record
   (`docs/sessions/2026-08-15-1129-authority-absolute.md`, created in that
   commit — Mike's verbatim ruling, the author's judgement calls), board item
   `200-…` in full, and the `SESSIONS.md` tail hunk. See AA11 — the landing
   shape makes this exposure near-unavoidable for any reviewer told to read
   "both diffs".
2. **Two tree greps leaked summary-depth lines** — my path-exclusion regex
   assumed a `./` prefix the grep output didn't carry, so the exclusions
   silently failed: two `SESSIONS.md` entries (the 2026-07-14 informed-
   principal entry and this delta's), one `ROADMAP-DONE.md` line, and
   one-line fragments of three prior verdicts — the Laws-removal pass (its
   line naming LR2/LR5 as un-re-homed), the 2026-07-14 pass (AS3 lines), and
   a 2026-07-26 pass reference. Files not opened; exposure is
   one-line-summary depth. Effect on findings: the LR2 knowledge duplicated
   what the delta itself shows (the dilemma line restored); the LR5 fragment
   ("the frame sits within the agent's own safety values" left unowned) is
   **contaminated knowledge — not adopted as a finding here**, left for
   reconcile and the Laws-removal cycle.
3. The lane README (`160-…/README.md`, not barred) disclosed that a prior
   pass on the same file holds open findings numbered AA1–AA5 — see AA10.

## Per-lens answers

**1 · Approach & assumptions.** Load-bearing assumptions, named: (a) that
authority and ruling are separable at the point of use; (b) that re-briefing
is always an available act; (c) that challenge-by-re-briefing terminates. The
split **is** a real distinction, not a restatement: it relocates the
informed-condition from the principal's *capacity* (which made the agent the
judge of when his word counted — a quiet overrule) to the ruling's
*challengeability* (which keeps the agent obeying while disagreeing). At the
point of use it yields a defined action in every case I could construct —
obey, and re-brief — except the execution-timing seam in AA6. Repeated
re-briefing: no count bounds it, and rightly (a count is gameable), but the
bound exists in principle — re-briefing that functionally stalls the ruling
"decays the principal's ability to make an authoritative decision", which the
new text forbids in terms. The principal declining to be re-briefed **is**
covered: that is the waiver clause — once the account has been offered, he
may waive and decide on less. Answered by the text, not by charity.

**2 · Correctness & quality.** All seven surfaces read at HEAD against both
diffs. They agree — same rule, consistent condensations, no surface saying a
sixth thing: apex (full statement) · `RECORD.md` (title ref, ADR acceptance
intact) · `AUTONOMY.md` (title ref; "informed decision and not obedience
extracted" consistent) · `CONCURRENCY.md` ("his rulings are conditioned" —
the correct half for an informing-the-principal context) · `REVIEW.md` rule 3
(stands-but-challengeable, matches the apex verbatim in substance) ·
`PROPAGATION.md` floor block and templates stamp (condensed; the one nuance
dropped — informed rulings stay reviewable — is point-up material, fine for a
floor). **Byte-identity claim verified two ways:** `stampscan --warn --root . .`
at HEAD reports `[identical] … (53 lines)`, and an independent extraction and
`diff` of the two region bodies confirms 53 identical lines — the 115/030
inversion caveat discharged by reading the output against the files. No
surface still carries the old logic under other words: the only remaining
"not exercisable uninformed" / "not a decision the doctrine recognises"
occurrences on live surfaces are CHANGELOG narration and the apex's own
correction note — history, correctly kept. GLOSSARY's section reference is
title-agnostic ("§ The principal's authority") and survives. ADR corpus,
`docs/build/`, skills: clean of the old logic.

**3 · Completeness / harvest.** CHANGELOG entries exist for both commits at
HEAD, and the Laws-removal entry was honestly amended to point at the
restoration. The always-confirm floor list is unchanged and works under the
new wording; the ADR path works; AUTONOMY's "a dilemma is never silently
resolved" clause has its apex anchor back. The child pin-bump window is
stated in CHANGELOG and the board item; a child sees it only through the
source-&-drift bullet's mechanical check — and empirically the window is
already closing: **ros's `CLAUDE.md` carries the NEW floor block** (both the
never-overrule sentence and the dilemma line) at pin `atelier@eef38be`, which
contains this delta (`merge-base --is-ancestor` verified). The restored
dilemma bullet does not blind-duplicate the honesty section — it cites the
transparency clause it specialises. Gaps found: the session-onramp skill's
floor (AA9) and the challengeability clause's scope (AA8).

**4 · Security & privacy.** atelier is PUBLIC; checked as such. The delta's
quoted principal prose is governance-only — no personal, health, family, or
financial context; the principal's identity is the published worked example
(ADR 0005). Neither the seven surfaces nor the queue pointer joins any
private repo's name to its posture (the pointer names worktrees, tiers, and
times only). Floor re-run green on both planes at HEAD, including full-cover
hook-plane leakscan on this machine. **Safety-posture delta:** real, and
housed in AA7 — this change converts an unbriefed floor approval from void to
live, which is a genuine weakening of the floor's failure-case guard, traded
deliberately for ending the doctrine's quiet overrule of the principal.
**Scanner reach case, stated:** the house security scanner reads the
session's pending diff; this is a landed-delta review on a clean tree, so its
reach here is empty — it was not run, and the floor plus the manual
public-tree read above is the cover that applied.

## Findings

Numbered from **AA6** — AA1–AA5 are already taken by the still-open
2026-07-26 apex-accountability pass on the same file in the same lane (AA10);
re-using them would make the lane's ruling queue ambiguous.

- **AA6 · MODERATE (counsel — the finding is Mike's to rule on):**
  **Execution timing under a standing challenge is unstated, and the two
  readings diverge exactly at the floor.** "The challenge is raised … by
  supplying the missing account and asking again" implies pause-then-ask;
  "never by declining to obey" and "never a licence to act as if the ruling
  had not been given" can be read as execute-now-challenge-later. For
  recoverable work the difference is nil; for an unbriefed approval of an
  irreversible floor action it is the whole question. One sentence closes it
  — e.g. *"pausing to supply the account before acting is not declining to
  obey."*
- **AA7 · MODERATE (counsel):** **The void→live conversion is the author's
  derivation, and its behavioural widening deserves its own line in the
  walk-through.** Mike's ruling (as quoted in the commit message) decides
  authority vs rulings; the extracted-approval consequence — an unbriefed
  approval now *stands* where it was previously *unrecognised* — is derived,
  not quoted. The derivation is sound (voidness let the agent un-decide the
  principal's word, a quiet overrule), and the author flagged it aloud; but
  what it newly permits — acting on an approval the agent itself
  under-briefed, which the old text forbade — is the sharpest safety change
  in the delta and is safe only under AA6's pause-first reading. Name the
  widening to Mike explicitly when this verdict is walked through.
- **AA8 · minor (counsel):** **The challengeability clause covers only
  rulings the agent asked for.** "When the agent asks the principal to rule…"
  — a principal-*initiated* overrule gets the briefing duty ("acts on an
  overrule the principal initiates") but is not literally within the
  challengeable-on-informedness sentence. The asymmetry faithfully tracks the
  verbatim ruling's own scope, so this is a harmonisation question for Mike,
  not a transcription error: one clause extends the challenge path to
  overrules he initiates, if he wants it extended.
- **AA9 · minor:** **The session-onramp skill's floor carries neither the
  authority-absolute sentence nor the informed-confirmation duty.** Its §2
  lists the stops bare; a plugin-onramped session never sees "never overrule
  him" or the challenge path unless it opens `00-APEX.md`. The same delta
  *did* add the dilemma line to this skill's honesty bullet, so the skill was
  in hand and the omission reads unchosen. Add the one-sentence floor line to
  §2, or record the narrowing as deliberate.
- **AA10 · note:** **Finding-ID collision assigned by the brief.** Prefix
  `AA` was already spent by the 2026-07-26 apex-accountability pass, whose
  AA1–AA5 await the principal's ruling in the same lane, on the same file.
  Worked around here by numbering from AA6; the review-brief machinery has no
  used-prefix check.
- **AA11 · note (process, on the landing shape — not this delta's
  substance):** **The delta commit packages its own barred material.** The
  intent record, board item `200-…`, and the `SESSIONS.md` entry land in the
  same commit as the doctrine change, so any rule-4 reviewer who reads "both
  diffs" — as every brief instructs — takes rule-2 barred material in the
  same output (it happened to this pass; disclosed above). AWA2's
  landing=queuing rule forces the *pointer* into the landing commit, but not
  the record-layer narration. Splitting records into an adjacent commit
  would keep the delta diff cold-readable at zero doctrinal cost.
- **AA12 · note:** The child floor block omits the waiver clause — a
  floor-only session that re-briefs and is waved off has no floor-level line
  saying the principal may decide on less, and could loop. Point-up covers
  it; one clause if wanted.

## Re-runs executed (all at HEAD `d161f72`)

- `stampscan --warn --root . .` → clean, `[identical]` 53 lines; independent
  region extraction + `diff` → byte-identical, 53 lines. Claim **verified**.
- `floor.py --plane hook` → exit 0, all gates ✅ (full-cover leakscan).
- `floor.py --plane ci --root .` → exit 0; 🟡 secretscan 22 advisory and
  degraded-cover leakscan are the standing expected CI-plane state.
- `python3 -m unittest discover -s tools -p 'test_*.py'` → **1324 tests, OK**.
- `node --test instruments/*.test.js` → **235/235 pass**.
- Pushed floor (full-SHA `gh run list --commit`): **success** on the delta's
  merge commit `81d7d04` and on HEAD `d161f72` — conclusion read, not just
  status; neither cancelled.
- Child check: `~/.pets/ros/CLAUDE.md` carries the **new** floor block at pin
  `atelier@eef38be`, verified to contain this delta.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 2 minor · 3 notes (AA6–AA12).**
The correction is faithful to the ruling on every surface, the restatements
genuinely agree, the byte-identity claim survives independent verification,
and the two commits' own claims all check out. The MODERATEs are counsel on
what the new wording leaves open at its highest-stakes moment, not defects in
the transcription — findings are the principal's to rule on (rule 3).

## Follow-up checklist

- [ ] Walk AA6–AA8 through to Mike plain-language, with AA7's widening named
      (rule 3; no MAJOR ⇒ his ruling is terminal).
- [ ] AA9: one floor sentence into `skills/session-onramp/SKILL.md` §2, or a
      recorded deliberate narrowing.
- [ ] AA10: a used-prefix check (or register) for review-brief finding IDs.
- [ ] AA11: consider a records-in-adjacent-commit convention for rule-4
      landings (doctrine edit to REVIEW rule 4's handoff paragraph, if Mike
      wants it).
- [x] Reconcile step (phase 2, after this verdict is committed): open the
      sibling, reconcile — including the LR-cycle overlap this reviewer names
      only as contaminated knowledge — fold in, delete the sibling, close the
      queue pointer. **Done below, 2026-08-17.**

## Reconcile — post-verdict, against the released material

Opened after phase 1 was committed (`fb6897c`), on the orchestrator's
release: the sibling's bytes (handed by message — the file was held out of
the tree), the intent record
`docs/sessions/2026-08-15-1129-authority-absolute.md`, board item `200-…`
(the ruling verbatim), and the Laws-removal verdict
`2026-08-15-1031-laws-removal-apex-cold.md` (LR1–LR9). Nothing above this
heading is revised; where the released material bears on a finding, the
outcome is stated here.

### AA7 against the ruling's verbatim text — the sibling's question 1

Board item `200-…` and the intent record carry the ruling verbatim. It rules
on: authority absolute; never overrule "no matter the situation including if
claude believes the principal is uninformed"; rulings conditioned on being
informed; challengeable on that, and by a review session even informed; the
ability to decide never decayed. **It does not mention extracted approvals,
the "not a decision the doctrine recognises" clause, or REVIEW rule 3 at
all.** So the void→live conversion **is the author's derivation, and AA7
stands as written** — unrevised, severity unchanged. Two things the released
material adds, neither softening it: the derivation is *near-compelled* —
treating an unbriefed approval as void is precisely the agent overruling the
principal in the situation where it believes him uninformed, which the
ruling's own words forbid — and the author flagged the call aloud in the
intent record ("'Challengeable' is not 'void'… if Mike wants it stronger or
weaker, it is a one-paragraph edit"), which is the right shape. What remains
owed is what AA7 asks: the walk-through presents the conversion to Mike *as
a derivation to ratify*, with its behavioural widening named, not as part of
what he already ruled.

### The five seeded questions

1. **The power transfer in the approvals clause.** Answered above — the
   transfer is the author's inference from a ruling about authority, applied
   to the approvals clause; near-compelled by the ruling's
   no-matter-the-situation words; flagged aloud; Mike has not yet ratified
   it. Covered by AA7 (stands) + AA6 (what the standing approval licenses
   while challenged).
2. **The decay mechanism.** Partially answered by the text: one violating
   behaviour is named (acting as if the ruling had not been given); beyond
   it the decay class is undescribed — repeated re-briefing to exhaustion,
   option-framing, timing are all left to judgement. A rule whose violation
   cannot be described has no forcing function (the standing `020-…/220`
   concern applies). New note AA13 below; the walk-through folds it into
   AA6's sentence-sized fix.
3. **What would have caught the first error.** Honest answer: nothing in the
   process — and worse, the 2026-07-14 cold pass *endorsed* the clause this
   delta removed (its AS3: "'not a decision the doctrine recognises' has the
   right teeth" — known from the incidental grep exposure disclosed in
   phase 1; the verdict was not opened further). The error was caught by the
   principal's own reading, two months on. The new wording has no test the
   old lacked — no scanner or lens detects a condition placed on the wrong
   noun; what it has is the ruling recorded verbatim at the decision site
   (board `200-…`), which lowers the cost of the *next* re-litigation but
   detects nothing. Recorded as the answer, not a finding — it is the
   `020-…/220` class, already on the board.
4. **The ordering the Laws framing carried.** No new orphan from *this*
   delta: the dilemma line never carried the ordering (its content is
   disclosure, not precedence); honesty-vs-obedience needs no ladder because
   the authority section is the honesty absolute's own positive face; and
   honesty-vs-design-goals is owned by § Why this is level 0. The genuine
   ordering residue (harm rankings, safety-values frame) left with the Laws
   and is the Laws-removal cycle's LR5, awaiting Mike — not re-found here.
5. **Child floor vs apex on the disagreeing agent.** Compared in phase 1
   (lens 2, AA12): at the moment of disagreement both texts permit exactly
   the same actions — obey, re-brief. The floor omits the waiver clause
   (AA12) and the independent-review challenge channel — a floor-only
   session doesn't know that channel exists, which is point-up material, not
   a permission difference. The feared whole-finding difference does not
   materialise. One true shared defect: AA6's timing ambiguity reads
   identically in both texts, so the larger population inherits it too.

### The LR overlap, resolved properly

- **No AA finding duplicates an LR finding.** AA6–AA9 have no LR ancestor
  (they concern the new wording, which post-dates the LR delta). AA11 is
  novel — the LR reviewer read non-record hunks selectively and dodged the
  exposure; this pass names the packaging itself.
- **LR2 (dilemma line un-re-homed)** — this delta's `c782e14` is its fix,
  and this pass reviewed the fix: the line is present on all four surfaces
  at HEAD (apex bullet, floor block, template stamp, onramp skill — phase-1
  lens 3), stampscan identical at 53 lines. LR2's follow-up test passes;
  the close is Mike's to confirm, per the LR verdict.
- **LR7 (two open pointers overlapping on the apex surfaces)** — resolved
  in practice by this pass: the `200`-pointer pass has now reviewed
  `38add7c` + `c782e14`, absorbing the post-`b5da9e5` overlap LR7 asked
  someone to own. Saying which, as LR7 requested: **the `200` pass absorbed
  it**; `215-…`'s delta list needs no widening.
- **LR5 (safety-values sentence unowned)** — flagged in phase 1 as
  contaminated knowledge, now legitimately open: it is the Laws-removal
  cycle's finding, awaiting Mike's ruling there; this delta neither restores
  the sentence nor bears on it. Not adopted as an AA finding — a descendant
  would be double-counting an open item.
- **LR9 (the accountability cycle's AA1 cited the deleted Laws block)** —
  adjacent to AA10 only in that both concern the AA1–AA5 cycle; no overlap
  of substance.

### Falsification check, both directions

- **Nothing in the intent record falsifies a phase-1 claim.** Its stampscan
  figures (52 lines after `38add7c`, 53 after `c782e14`) agree with my
  independent 53-line byte-diff at HEAD; its account of the seven surfaces
  matches what the diffs show; its "pushed-floor reported at close" claim is
  the author's, and my own full-SHA check of the merge commit's run
  (success) covers the substance.
- **Absent from the author's account, present in this pass:** AA6 (the
  execution-timing seam), AA8 (challengeability scoped to asked-for
  rulings), AA9 (the onramp skill's floor carries no authority line), AA11
  (the records-in-the-delta-commit packaging). The record's judgement-calls
  section prices the void→live call and the floor growth — the right calls
  to say aloud — but none of the four above.
- **AA10, amended (not renumbered):** the intent record names the open
  AA1–AA5 cycle in terms ("the two cycles sit side by side"), so the prefix
  collision was knowable — but only from a record rule 2 barred the
  brief-writer from opening. The bar itself contributed to the collision,
  which strengthens the mechanical fix (a used-prefix check at
  brief-writing time) over any disciplinary reading.

### Post-reconcile additions — clearly marked

- **AA13 (note, post-reconcile)** — the never-decayed clause names exactly
  one behaviour that violates it (acting as if the ruling had not been
  given); the rest of the decay class is undescribed, so the clause guards
  by judgement, not by test — the standing `020-…/220` concern applied to
  the apex's newest sentence. Counsel: fold into AA6's one-sentence fix
  rather than legislating a list; a described *example* of decay-by-
  re-briefing would give the clause its forcing function.

**Overall after reconcile: PASS-WITH-FINDINGS — 0 MAJOR / 2 MODERATE /
2 minor / 4 notes (AA6–AA13; AA7 and all phase-1 severities unchanged; AA10
amended; AA13 added).** No MAJOR ⇒ the ruling application is terminal under
REVIEW's close rule; AA6–AA13 go to Mike's ruling round.

## Deferred material (folded in at verdict landing)

# Deferred material — authority absolute (open only after your findings are durably written)

Sibling of `2026-08-17-0622-authority-absolute-cold.md` under REVIEW.md
rule 1's split. Fold into the brief below the verdict and delete this file
when the verdict lands.

## Intent records

- `docs/sessions/2026-08-15-1129-authority-absolute.md` — the authoring
  session's account. **Not opened by the brief-writer.**
- `docs/roadmap/160-doctrine-review-owed/200-apex-authority-absolute-rulings-conditioned.md`
  — the board item, carrying the principal's ruling verbatim. **Not opened by
  the brief-writer.**
- The `docs/SESSIONS.md` index entry for the same session. ⚠️ **This one WAS
  read by the brief-writer**, incidentally and before the brief was
  commissioned — see the disclosure in the brief. It is the reason the two
  records above were left closed.

## Prior verdicts on the same surfaces

- `docs/reviews/2026-08-15-1031-laws-removal-apex-cold.md` — the pass on the
  removal that emptied the apex section this delta rewrote. LR1–LR9 await the
  principal's ruling round; reconcile against it.
- The Laws-removal board item
  (`020-…/215-rule-4-cold-pass-queued-laws-removal.md`) records that cycle's
  state.

## Brief-writer's seeded questions (a floor, never a fence — and thinner than usual)

These are deliberately few. The brief-writer had already read the
`SESSIONS.md` summary of this delta, so its questions are shaped by the
author's own framing more than a cold reader's would be. Generate your own
before reading these, and treat a question you did not think of as a prompt to
re-read the surface rather than as an agenda.

1. The old text said an approval given without an account *"is not a decision
   the doctrine recognises"*. The new text says it *"stands as the principal's
   word but is open to challenge"*. That is a real transfer of power — from the
   agent (which could previously treat such an approval as void) to the
   principal (whose word now stands until he revisits it). Is that transfer
   what the principal ruled, or is it the author's inference from a ruling
   about *authority* applied to a clause about *approvals*? The commit message
   and the board item are the evidence; the board item is barred until now.
2. "The principal's ability to make an authoritative decision must never be
   decayed by it." What is the mechanism of decay this clause guards against,
   and does the doctrine name any behaviour that would constitute it? A rule
   whose violation cannot be described is a rule with no forcing function —
   which is the standing concern on this board at `020-…/220`.
3. The correction was made because the earlier wording put the condition in
   the wrong place. Both wordings were written into the apex, the highest
   doctrine surface, and the earlier one survived a review cycle. What, if
   anything, in the review process would have caught the first error — and
   does the new wording have a test the old one lacked, or only a better
   author?
4. `c782e14` re-homes the dilemma line from a Laws bullet to an honesty
   bullet. The Laws framing carried an ordering (a ladder); honesty does not.
   Does anything the old placement did — precedence when honesty and another
   value conflict — now have no owner?
5. The child floor block is the only doctrine most children read. Compare what
   it says about authority against what the apex says. If they differ in what
   an agent is permitted to do when it disagrees, that difference is the whole
   finding, because the population that reads the weaker text is larger.
