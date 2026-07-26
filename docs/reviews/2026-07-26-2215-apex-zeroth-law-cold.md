# Cold review (rule 4) — apex: Asimov's Zeroth Law above the Three Laws

**Subject (refs only):** the Zeroth Law added to `docs/method/00-APEX.md`
§ "Then the Laws", reached across two commits — `572dddd` then `672e838`,
the second restructuring the first — plus the matching sweeps of `README.md`
and `docs/method/README.md`. Establish both hunks with `git show 572dddd
672e838` and review the result at HEAD; the two-commit shape is itself part of
the subject.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer — which
carries the decision history and one open micro-choice, deferred below — and
SESSIONS index one-liners. Nothing evaluative from either appears above the
divider. Reviewer caution: the two commits' history encodes a principal's
decision sequence; findings that would relitigate a ruled choice should be
framed as such at the reconcile, not silently dropped.

**The reviewer's first acts:** establish what the delta does and why from the
two commits and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). This is **apex text** — the widest blast radius in
the operating model. The heavy lenses: 1 — does an unnumbered Zeroth above
numbered 1–3 carry precedence unambiguously, and does the borrowed Asimov
wording ("may not harm humanity or, through inaction, allow humanity to come
to harm") bind sensibly on a repo-operating agent, or does it import
obligations no session can discharge ("through inaction" is doing load-bearing
work — attack it); 2/3 — internal consistency of every Laws restatement at
HEAD (`00-APEX.md`, both READMEs, `PROPAGATION.md`, the child template's floor
block — does any surface still claim a count, a numbering, or an ordering the
delta changed); 4 — a public repo whose apex quotes a well-known copyrighted
formulation: is attribution handled honestly.

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 -m unittest discover -s tools` · `node --test instruments/*.test.js`
(the template tests pin the child floor block — relevant here). Lens 4's
scanner: landed markdown — discharge `/security-review` in one explicit line
with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commits named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**ZL1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored apex doctrine encoding the principal's instruction: REVIEW.md
rules 3–4 govern — findings are the principal's to decide; nothing is applied
in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* no separate record — the queue pointer carries the decision
history: the principal first ruled *renumber* (move the three down one) via a
decision prompt, applied as `572dddd`, then changed his mind to the unnumbered
Zeroth-above-the-three form, applied as `672e838` — so numbers 1/2/3 keep
their historical meaning and the earlier off-by-one-against-past-records
concern is void. The original three keep their wording: no Zeroth
subordination clause was added to them — precedence is carried by position
plus the section prose. The one open micro-choice, flagged to the principal
and not yet ruled: whether to add Asimov's explicit "unless this conflicts
with the Zeroth Law" clauses to the three. The caveat's ordering line reads
Zeroth → individual harm → obedience → self-preservation; the
`PROPAGATION.md` + child-template floor-ordering summary keeps generic "the
Laws" wording with no count claim.

---

## Reviewer's attack surface (cold pass, 2026-07-26, Fable)

Named as my own before findings, from `git show 572dddd 672e838` and HEAD
(`9aef298`) only. The delta's load-bearing assumptions as I read them:

1. **Position + prose carry precedence.** The unnumbered Zeroth outranks 1–3
   via section prose ("read first and outranks them") and the caveat's
   ordering line — with no renumbering and no subordination clauses in the
   three's own text.
2. **The caveat absorbs "through inaction".** "Hold their ordering … as the
   ethic, not as a literal rule engine" is assumed to defuse the
   undischargeable positive duty a literal humanity-scale inaction clause
   imports.
3. **The sweep was complete.** README, `method/README`, `PROPAGATION.md`
   floor, and the child template were assumed to be *every* Laws restatement
   surface at HEAD.
4. **The floor summary survives the restructure.** "avoid harm to humanity →
   avoid harm to a person → obey → self-preserve" is count-free and so stays
   accurate under either numbering form.
5. **Naming Asimov is honest attribution** for a borrowed formulation in a
   public Apache-2.0 repo.
6. **The two-commit shape is legible** — a ruling then a reversal, each
   recorded in its commit message, not a confusing half-state.

Attack lines: (A1) literal cross-references — Law 2 excepts only First-Law
conflicts, Law 3 only First/Second; does an order conflicting *only* with the
Zeroth bind? (A2) the inaction clause — does the caveat defuse the
*obligation* or only the *epistemics* (standing to judge)? (A3) hunt
restatements beyond the four swept files — skills, commands, plugin-bundled
surfaces, tests. (A4) every count/numbering/ordering claim at HEAD. (A5)
attribution honesty and licence interaction. (A6) does the prose
characterising the three ("about the individual and the principal") actually
describe Law 3?

---

## Verdict (cold pass, 2026-07-26, Fable, worktree at 9aef298)

### Re-run obligations — all green

- `python3 tools/floor.py --plane ci` — exit 0, all nine scanners enforced and
  clean; sizescan raises only its never-failing size advisory on
  `docs/ROADMAP.md`.
- `python3 -m unittest discover -s tools` — exit 0, selftest OK.
- `node --test instruments/*.test.js` — 207/207 pass, 0 fail. The template
  tests that pin the child floor block pass: `PROPAGATION.md`'s floor region
  and `docs/build/templates/CLAUDE.md` are byte-identical, including the new
  "avoid harm to humanity → avoid harm to a person → obey your principal →
  self-preserve" ordering.
- Lens 4 scanner: `/security-review` **not run — discharged with grounds**:
  the delta is landed prose in four markdown doctrine files with no code,
  configuration, credential, or executable surface the scanner can read
  (REVIEW.md's landed-delta case); the floor's secretscan/leakscan ran above
  and are clean.

### Findings

**ZL1 — the stale-claim sweep missed a known Laws-restatement surface
(major).**
*Claim:* `skills/session-onramp/SKILL.md:33–35` still teaches the pre-Zeroth
three-element Laws — "**Then the Laws, in order:** (1) avoid harm — including
through inaction; (2) obey your principal, except where that conflicts with
the First Law; (3) protect your own operation, last" — with no humanity-scale
law, contradicting `00-APEX.md:202–210` and the floor block
(`docs/method/PROPAGATION.md:110–112`, `docs/build/templates/CLAUDE.md:29–31`)
at HEAD.
*Evidence:* the surface was a *known* restatement home before the delta —
commit `31b2ed0` (2026-07-23, "apex: sweep in-repo restatements to the
three-element floor") touched exactly this block; the delta's own PRINCIPLES §6
sweep (both commits, 2026-07-24) covered README, `method/README`,
`PROPAGATION.md`, and the template but not the skill. The onramp skill is the
surface that *binds the apex at session start* for adopting repos ("the two
things below bind from the start", SKILL.md:14–15) — so the one place designed
to load the Laws first now loads them without the Zeroth.
*Counsel:* extend the sweep to the skill's apex block in the fix commit, and
add the plugin-bundled surfaces (skills/, commands/) to whatever checklist the
§6 sweep works from — this is the second sweep to treat "in-repo restatements"
as `docs/` only.

**ZL2 — precedence is not self-contained in the Laws' own text (minor; input
to the open micro-choice, not relitigation).**
*Claim:* an order conflicting *only* with the Zeroth is not excepted by Law
2's own wording — `00-APEX.md:207–208` excepts only First-Law conflicts, and
`:209–210` only First/Second — so precedence rides entirely on section prose
(`:199` "read first and outranks them") and the caveat's ordering line
(`:215–217`). Read whole-section it is unambiguous; quoted as the numbered
list alone — the likeliest excerpt shape — it exports the wrong precedence.
*Evidence:* file:lines above; `672e838`'s commit message names this the "one
open micro-choice for Mike" (originals kept verbatim, no Zeroth-subordination
clause).
*Counsel:* this is the principal's pending ruling and this finding is framed
as input to it: either the Asimov-faithful "unless this would conflict with
the Zeroth Law" clauses, or one line directly above the list ("each of the
three binds only within the Zeroth"), closes the excerpt risk. Until ruled,
the caveat mitigates but does not remove it.

**ZL3 — the caveat defuses the Zeroth's epistemics, not its obligation
(minor).**
*Claim:* "through inaction, allow humanity to come to harm"
(`00-APEX.md:202–203`) read literally places every session in permanent
breach — some humanity-scale harm is always proceeding un-prevented, so the
clause imports a positive duty no repo-operating agent can discharge. The
caveat addresses *standing to judge* ("rarely has the standing to judge
species-wide harm", `:214–215`) — the epistemic half — and leans on "ethic,
not a literal rule engine" (`:217–218`) for the rest, which is defence by
disclaimer rather than a scoped duty.
*Evidence:* file:lines above; contrast the First Law's identical inaction
clause, whose scope self-limits to the human beings actually in the work's
blast radius — the Zeroth's subject ("humanity") has no such natural limit.
*Counsel:* the Law's wording is the principal's Asimov-faithful ruling and is
not the target; one scoping sentence in the caveat — the inaction duty binds
on harms within the agent's sight and reach from its seat, it is not a
mandate to go hunting for species-scale harm — would make the Zeroth
dischargeable rather than aspirational.

**ZL4 — "about the individual and the principal" mischaracterises Law 3
(trivial).**
*Claim:* `00-APEX.md:198` says the three are "about the individual and the
principal"; Law 3 (`:209–210`) is about the agent's own existence — neither.
*Counsel:* "about the individual, the principal, and the agent itself" (or
similar) if the caveat area is edited anyway.

**ZL5 — ragged rewrap in the caveat (trivial).**
*Claim:* `672e838`'s rewrap left short mid-paragraph lines at
`00-APEX.md:216–219` ("… not as a / literal rule engine. A genuine /
dilemma …"). Renders fine; wrapscan is width-only so it passes; cosmetic
against the house's otherwise even prose wrap.
*Counsel:* rewrap in the next touch of the section; not worth its own commit.

### What held

- **Precedence at whole-section read** — the Zeroth's outranking is stated
  plainly in prose and repeated in the caveat's ordering line; within
  `00-APEX.md` there is no reading on which the Zeroth is subordinate.
- **Both READMEs at HEAD** — `README.md:57–59` and
  `docs/method/README.md:8–10` say "Three Laws, with Asimov's Zeroth Law read
  above them": count, numbering, and ordering all true of the section as
  landed.
- **The floor summary** — deliberately count-free ("the Laws, in order: …"),
  four elements in the correct order, accurate under the unnumbered-Zeroth
  form; byte-identical across `PROPAGATION.md` and the child template, pinned
  by passing tests.
- **Attribution (lens 4)** — Asimov is named twice (`00-APEX.md:193,196–197`),
  the text is declared "Mike's adaptation", and the divergences from the
  original ("The agent" for "A robot"; "through inaction" carried into the
  Zeroth) are consistent adaptation, never a misquote presented as verbatim.
  Short, attributed use of a famous formulation in commentary/adaptation
  context in an Apache-2.0 repo: honest and proportionate. No finding.
- **The two-commit shape** — a ruling (`572dddd`, renumber) then a recorded
  reversal (`672e838`, unnumbered Zeroth), each commit message carrying the
  decision and its cost accounting ("off-by-one … now void"). The history is
  legible as a principal's decision sequence, not a half-state.

### Verdict: **PASS-WITH-FINDINGS** — 0 blocking · 1 major (ZL1) · 2 minor (ZL2, ZL3) · 2 trivial (ZL4, ZL5)

The landed apex text is coherent and honestly attributed; the one substantive
defect is outside the four swept files (ZL1). Findings are counsel — the
principal decides; nothing was applied in this pass.

**Discipline deviations, owned:** one repo-wide grep for Laws keywords used a
path filter (`^./…`) that grep's output format did not carry, so its output
included matching *lines* from `docs/ROADMAP.md`, `docs/SESSIONS.md`, two
`docs/sessions/**` files, two other `docs/reviews/*` briefs, and — because the
brief file itself matched — roughly five lines of this brief's own deferred
section (decision-history phrases also present in the delta's commit
messages, my legitimate source). None of those files was opened; nothing
under `docs/reviews/withdrawn/` matched; no finding above rests on the leaked
lines. The exposure is why ZL2 is framed against the *commit message's*
statement of the open micro-choice, which I hold independently of the leak.

---

## Reconciliation (against the deferred decision history, 2026-07-26)

The deferred section adds nothing beyond what the two commit messages already
record — the renumber ruling, the reversal, the void off-by-one cost, the
open subordination-clause micro-choice, and the count-free floor wording. My
findings were built on those commit messages, so the reconcile changes
little:

- **ZL1 (sweep miss, major) — held unchanged.** The decision history is
  silent on the skill surface; nothing ruled excuses the miss. Stands as the
  pass's one substantive finding.
- **ZL2 (precedence not self-contained, minor) — held, framing confirmed.**
  The deferred section confirms the subordination-clause question is flagged
  and **not yet ruled** — so ZL2 is input to a live decision, not
  relitigation of a settled one, exactly as framed. No change.
- **ZL3 (inaction obligation, minor) — held, framing sharpened.** The
  decision history shows the principal ruled on *numbering and form*, not on
  the caveat's treatment of the inaction duty — so ZL3's counsel (a scoping
  sentence in the caveat, wording of the Law untouched) sits outside every
  ruled choice. Stands.
- **ZL4, ZL5 (trivial) — held unchanged.** Prose precision and rewrap;
  no interaction with any ruling.
- **Added: none. Withdrawn: none.**
- One note for the record: the deferred section states the floor summary
  "keeps generic 'the Laws' wording with no count claim" — my what-held list
  verified that independently at HEAD (byte-identical, test-pinned), so the
  claim is confirmed, not merely inherited.

Verdict unchanged: **PASS-WITH-FINDINGS** — 0 blocking · 1 major · 2 minor ·
2 trivial.
