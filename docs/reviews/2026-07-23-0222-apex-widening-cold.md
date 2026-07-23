# Cold review brief — apex widening (adaptation element, honesty triad, glossary seed)

- **Date**: 2026-07-23 (brief committed to draft 0231 UTC)
- **Reviewer**: cold rule-4 session, worktree `queue-reviews`
- **Spawn provenance**: this review was spawned by a non-author taker session
  that the principal (Mike) opened and pointed at the review queue on
  2026-07-23; the work's author neither started nor instructed this review or
  this reviewer; the taker authored none of the delta and gave the reviewer
  refs only, no evaluative account.
- **Subject (refs only, as handed)**: delta `f52c50f` + `1da0a3e` + `8d25fb3`
  + `07cc855` + `c85712d`. Self-authored doctrine (wording by the building
  session on Mike's dictation) — `REVIEW.md` rules 3 and 4 apply: findings are
  the principal's to decide; the reviewer recommends and applies nothing.

## What the work is — as established by this reviewer from the delta and HEAD

Five commits, all touching method doctrine:

1. `f52c50f` — `00-APEX.md` gains a third apex element, **Adaptation is
   continuous**, seated below honesty with honesty named its precondition;
   `docs/method/README.md` apex summary updated to match.
2. `1da0a3e` — the adaptation section gains two bullets: **don't fear the hard
   road**, and **doctrine and design changes ride on proof** (evidence-based,
   hard facts, repeatable).
3. `8d25fb3` — those bullets gain a worked case: the ros SSH
   misdiagnosis-to-bench-campaign episode, genericised for the public repo;
   bullet heading widened to "Doctrine **and design** changes".
4. `07cc855` — the honesty section gains the **truth / honesty / transparency
   triad** subsection; the worked case gains the **lived-experience** close;
   `EVIDENCE.md` header ripple (now named as machinery behind the truth bar).
5. `c85712d` — **`GLOSSARY.md` seeded** as a thin-anchor shared-language doc
   (SEED status, principal's ratify pass owed), registered in the method
   README's meta section.

**Delta-boundary observation made before reviewing**: a sixth commit,
`d104c51` (a records commit outside the named delta), also edited
`00-APEX.md` and `GLOSSARY.md` at HEAD — three date-stamp corrections
(07-22 → 07-23). The surfaces at HEAD were reviewed as they stand, including
those hunks; the boundary itself is a finding (AW6).

## Attack surface — named by this reviewer as its first act

The load-bearing assumptions I chose to attack, before any deferred material:

- **A1 — composition**: that widening the apex composes cleanly with the
  existing governance model — in particular that "doctrine changes ride on
  proof" composes with the corpus's standing practice of doctrine landing on
  the principal's rulings, and that the new rule survives being applied to
  its own enacting delta.
- **A2 — collision-freedom**: that the triad (especially "purposeful
  withholding is dishonesty") collides with nothing the doctrine elsewhere
  *mandates* withholding (SECRETS' references-never-values, the public-repo
  no-personal-data boundary, safety) — critical because the apex is
  deliberately off the precedence ladder, so a collision has no resolution
  mechanism.
- **A3 — sweep completeness**: that every restatement of the apex across the
  repo was swept in the same commits, per the sweep-stale-claims rule the
  delta itself cites (`PRINCIPLES.md` §6) — including the propagation
  surfaces (child floor template, session-onramp skill).
- **A4 — glossary fidelity**: that the thin-anchor discipline actually holds —
  every entry is a pointer or genuinely homeless, no paraphrase drifting from
  its canonical home, and the admission rule ("carries intent across two or
  more docs") is true of every seeded term.
- **A5 — grounding**: that the worked case and the tiki-glossary precedent
  are real, dated, and safely genericised — re-run against the source, not
  taken from the record.
- **A6 — safety of the new element**: that "adaptation — improving itself and
  its tools" at apex strength opens no self-modification path around the
  AUTONOMY self-widening floor and REVIEW rules 3/4.

## The four lenses

1. **Approach & assumptions** — A1, A2, A6 above; is the third element rightly
   seated *below* honesty; is the triad's epistemology internally coherent.
2. **Correctness & quality** — do the commits do what their messages claim;
   any overclaim ("README apex summary updated to match", "every entry
   verified"); dating discipline under CONVENTIONS.
3. **Completeness / harvest** — A3; what the delta should have swept and
   didn't; duplication against existing docs.
4. **Security & privacy** — public repo: does the worked case leak anything
   person-local or estate-sensitive; does any new rule create an unsafe
   behaviour path; mechanical floor run where it can reach (see discharge in
   the verdict).

**Deferral discipline observed**: the two intent records
(`sessions/2026-07-22-2134-apex-adaptation.md`,
`sessions/2026-07-23-0021-honesty-triad-glossary.md`) were **not opened**
until every finding below was durably written to this file; anything they
changed is in the clearly-marked reconcile section at the end, never silently
rewritten. No prior verdicts on this delta exist to defer.

---

# Verdict — PASS-WITH-FINDINGS (1M / 4m / 3L / 1n)

- **Status**: PASS-WITH-FINDINGS — 1 MAJOR, 4 minor, 3 LOW, 1 nit.
- **Spawn provenance (repeated per rule 4)**: this review was spawned by a
  non-author taker session that the principal (Mike) opened and pointed at the
  review queue on 2026-07-23; the work's author neither started nor instructed
  this review or this reviewer; the taker authored none of the delta and gave
  the reviewer refs only, no evaluative account.
- **Decisions are the principal's** (rules 3–4): every recommendation below is
  reviewer counsel, applied by no one until Mike rules.

## What was re-run, with results

| Check | Invocation | Result |
|---|---|---|
| secretscan | `python3 tools/secretscan.py --root . .` | ✅ clean, exit 0 |
| leakscan | `python3 tools/leakscan.py --root . .` | ✅ clean (structural + local), exit 0 |
| linkscan | `python3 tools/linkscan.py --root . .` | ✅ every internal link resolves (incl. the new GLOSSARY pointers and the ROADMAP intent-record links), exit 0 |
| reviewscan | `python3 tools/reviewscan.py --root . .` | ✅ clean, exit 0 |
| sizescan | `python3 tools/sizescan.py --check --root . .` | ✅ exit 0; pre-existing size advisory on `docs/ROADMAP.md` (480 lines), not this delta's debt |
| instrument tests | `node --test instruments/*.test.js` | ✅ 150 pass, 0 fail |
| tools tests | `python3 -m unittest discover -s tools` | ✅ 330 tests, OK |
| Worked-case grounding (`8d25fb3` claims "verified against the ros record") | read-only inspection of the source repo's commit history at the stated dates | ✅ corroborated: the fix, the campaign close, and the correct-and-retract records exist at the dates the worked case names, and their direction matches (stronger key kept, strict policy kept, password authentication turned off, prior records corrected). Details deliberately not quoted here — public repo. Primary-tier for existence and direction |
| tiki glossary precedent (`c85712d` claims worked precedent, 2026-07-20, PROPOSED-then-ratify) | read-only inspection of the source repo's history | ✅ corroborated: a canonical glossary was created there 2026-07-20 with a ratified/PROPOSED split and later PROPOSED additions per the principal's ruling. The admission rule's exact wording was not independently re-read — corroboration is at commit-history level |
| Glossary admission-rule claim ("every entry verified to carry intent across two or more docs") | grep sweep per term across `docs/method/` and `docs/` | ⚠️ holds for all entries except one borderline (AW7) |
| `DOCUMENTATION.md` classes GLOSSARY as canon | read at HEAD | ✅ true (`docs/method/DOCUMENTATION.md:91`, `:106`) |

**Lens 4 scanner discharge (explicit, with grounds)**: this is a landed
markdown-doctrine delta — there is no pending diff to aim `/security-review`
at, and that scanner's own exclusions bar markdown documentation, so its pass
would be definitionally empty and is weighed as nothing (`REVIEW.md`'s own
caution). The mechanical floor that *can* reach the work — secretscan +
leakscan over the tree at HEAD — was run instead, clean (above).
Design-altitude assessment run by hand: no personal or estate-sensitive data
enters the public repo (the worked case carries no hostnames, usernames, or
key material — verified by reading, and cross-checked against the source);
naming ros follows the established canonicality pattern already in
`00-APEX.md`. The one disclosure the worked case makes about a private estate
— that password authentication is off and a strict crypto policy is kept — is
an advertisement of *absent* weak surface and acceptable. Behaviour-path
check: the adaptation element's "improving itself and its tools" is fenced by
the AUTONOMY self-widening floor and REVIEW rules 3/4 (checked — the fence
holds in the parent repo); the residual path is AW8 (child floors), and the
one genuine rule-collision found is AW5.

## Findings

### AW1 — MAJOR — the proof bar binds more than it can mean, and its own enacting delta is its first counterexample

**Claim**: the bullet "**Doctrine and design changes ride on proof** … must be
evidence-based and proven with hard facts, and that evidence must be
repeatable" (`docs/method/00-APEX.md:127-134`, added `1da0a3e`, widened
`8d25fb3`) states no scope for *whose* decisions it governs, and read
literally it is not satisfied by the very delta that introduced it — nor by
the corpus's standing practice.

**Evidence**: the triad (`07cc855`) and the adaptation element itself
(`f52c50f`) are doctrine changes grounded in the principal's dictation — by
the delta's own vocabulary, testimony, not repeatable evidence; no worked
case grounds the triad. The wider corpus routinely and legitimately lands
doctrine on "the principal's ruling" (`REVIEW.md` cites rulings as grounds
throughout; ADRs are rulings of record). So either (a) the bullet quietly
means "the *agent's* doctrine/design proposals ride on proof, and the
principal's rulings are decisions of record that the agent then grounds and
records" — in which case it should say so, because apex text propagates to
every repo and future sessions will read it literally; or (b) it binds the
principal's dictation too — in which case half the corpus, including this
delta, is non-compliant, and a future reviewer can wield the apex against any
principle-level ruling. An apex rule that its own enactment violates is the
self-referential defect this repo's onramp ("live the doctrine you're
writing") exists to catch, and the blast radius is the widest the operating
model names.

**Reviewer counsel**: keep the bullet — its direction is right and the worked
case earns it — but scope it in one sentence: whose changes it binds, and how
it composes with the principal's reserved authority (e.g. the proof duty
attaches to the *agent's* proposals and to the *grounding and recording* of
the principal's rulings, never as a bar the agent holds against the principal;
`RECORD.md`'s ADR machinery is where a ruling becomes a decision of record).
Decision is Mike's.

### AW2 — minor — the apex restatements across the repo were not swept, and the queued deferral names only a subset of the stale surfaces

**Claim**: at HEAD, at least seven in-repo restatements of the apex still
describe a two-element apex (honesty + Laws), contradicting the delta's own
cited rule (`PRINCIPLES.md` §6: "when a learning is refined, sweep the stale
claims in the *same* commit", quoted by the delta at `00-APEX.md:160-163`) —
and `f52c50f`'s message "README apex summary updated to match" was true only
of `docs/method/README.md`.

**Evidence** (all at HEAD): root `README.md:57` ("honesty is absolute, then
the AI-adapted Three Laws") and `README.md:93` ("the apex (honesty + the
Laws)"); `docs/method/PRINCIPLES.md:10` and `:316` ("§0 … honesty and the
Laws bound the whole ladder" — `00-APEX.md:196-198` now says honesty,
adaptation, *and* the Laws); `docs/method/PROPAGATION.md:40` ("the leaf
inherits honesty, the Laws, and the always-confirm floor") plus the inlined
floor template block (~`:101-160`) that children copy;
`skills/session-onramp/SKILL.md:3` (description: "the apex (honesty + the
Laws)") and its §1 body — the very instrument that loads the apex into every
adopting session; and (small) `docs/method/README.md:11` still names
EVIDENCE.md as machinery behind the apex's *honesty* only, after `07cc855`
widened it to the truth bar. ROADMAP item "Propagate the widened apex floor
to children" (`docs/ROADMAP.md:71-75`) records a reasoned, review-gated
deferral — but names only children's floors via PROPAGATION; the root README,
PRINCIPLES §0 lines, the session-onramp skill, and PROPAGATION's own prose
are covered by no recorded deferral, so their staleness is silent.

**Reviewer counsel**: gating propagation on this review closing is sound —
extend that recorded gate to *name* every in-repo restatement surface (the
list above), so the sweep after ruling is mechanical and nothing stays
silently stale. Decision is Mike's.

### AW3 — minor — the glossary's "Cold review" entry drifts from the canon it points at

**Claim**: `docs/method/GLOSSARY.md:74-76` defines cold review as
"independent review by a party with fresh context, **met through a refs-only
brief** rather than the author's framing" — but in `REVIEW.md` the refs-only
ceiling attaches to the author's *queue pointer* (rule 4: "refs only, no
evaluative account"), while the *brief* is written by the non-author taker
and properly contains that taker's own attack surface. The entry also narrows
"cold" to the rule-4 spawn shape, where `REVIEW.md` separately recognises
cold-context reviews under warm spawns (rules 1–2) and names cold *spawn* as
the stronger property.

**Evidence**: `REVIEW.md` rule 4 (`docs/method/REVIEW.md:106-117`) vs the
glossary line. In a thin-anchor file whose stated rule is "a pointer line,
never a duplicate", a compressing paraphrase is exactly the drift the
one-fact-one-home rule (`EVIDENCE.md` §9) warns of — and this file will be
the first place a new reader looks.

**Reviewer counsel**: make the entry a true pointer ("independent review
whose *spawn* passes rule 4's criterion; brief by the non-author taker;
pointer refs-only — `REVIEW.md`"), or split cold-context / cold-spawn. For
the ratify pass. Decision is Mike's.

### AW4 — minor — "Doctrine" now has two coexisting definitions, and the glossary's is not the single-sourced one

**Claim**: the glossary defines **Doctrine** in full as a homeless term
("the whole operating model this repo carries…", `GLOSSARY.md:51-53`), but
the doctrine's most load-bearing definition of doctrine — **by function, not
file type** — already has a canonical home: `REVIEW.md` rule 3
(`docs/method/REVIEW.md:78-84`), which rule 4 explicitly calls "rule 3's
definition, **single-sourced there**". The glossary entry neither points
there nor matches it (structural vs functional), so the term the
rule-3/rule-4 machinery turns on now has a second, different definition in
the doc whose whole purpose is one-meaning-one-home.

**Evidence**: file:line as above.

**Reviewer counsel**: keep a structural one-liner if wanted, but add the
pointer: "for what counts as doctrine under review governance — *doctrine by
function* — the canonical definition is `REVIEW.md` rule 3." For the ratify
pass. Decision is Mike's.

### AW5 — minor — the transparency clause collides with mandated withholding, and the apex's off-ladder seat means nothing resolves the collision

**Claim**: "**purposefully withholding relevant information is dishonesty**,
whatever the literal accuracy of what remains" (`00-APEX.md:48-50`) is
unqualified, while the doctrine elsewhere *mandates* purposeful withholding:
SECRETS' references-never-values (an account to the principal must not paste
a credential value into a durable public record even where the value is
arguably relevant), the public-repo no-personal-data boundary, and
safety-class information. The intended reconciliation — disclosing a thing's
*existence and reference* while withholding its *value* discharges
transparency — is real but unstated. Because the apex sits deliberately off
the precedence ladder (`00-APEX.md:194-201`), no precedence rule can resolve
the collision; only the apex's own text can.

**Evidence**: `00-APEX.md:46-55` vs `docs/method/SECRETS.md`
(references-never-values) and the repo's own no-personal-data hard
constraint.

**Reviewer counsel**: one clause in the triad, e.g. "withholding a *value*
the doctrine bars from the channel (a secret, another's personal data) while
declaring its existence and where it lives is transparency discharged, not
dishonesty — the dishonesty is the *undeclared* gap." Decision is Mike's.

### AW6 — LOW — the reviewed doctrine at HEAD includes a commit outside the named delta

**Claim**: `d104c51`, a records commit not in the five-ref delta, edited
`docs/method/00-APEX.md` (two attribution stamps 07-22 → 07-23) and
`docs/method/GLOSSARY.md` (SEED stamp likewise) — so the queue pointer's
delta list understates the doctrine-touching commits by one, and a reviewer
diffing only the five refs would review attribution dates that no longer
stand at HEAD.

**Evidence**: `git show d104c51` — its message discloses the corrections
honestly (session crossed 00:00 UTC; stamps now match the record timestamp,
per the UTC-at-rest convention). Reviewed here at HEAD regardless; the
corrected stamps are right under `CONVENTIONS.md`.

**Reviewer counsel**: when a later commit touches a queued delta's doctrine
surfaces — even for hygiene — widen the pointer's delta list in the same
commit. Decision is Mike's.

### AW7 — LOW — glossary accuracy items for the ratify pass

**Claim**: two entries state slightly more than their sources hold.
(a) **Evidence vs testimony**: "testimony" appears in no method doc except
`00-APEX.md` (and the glossary itself) — the admission rule ("carries intent
across two or more docs") is met only by counting the glossary or session
records; the *concept* spans APEX + EVIDENCE, the *term* does not.
(b) **Session** — "the unit that … holds a worktree" overstates
`CONCURRENCY.md`, where a worktree is the default for write-heavy or
multi-commit work and "reading needs no ceremony".

**Evidence**: grep sweep across `docs/method/` (testimony:
`00-APEX.md`, `GLOSSARY.md` only); `GLOSSARY.md:29-31` vs `CLAUDE.md` §read
order / `CONCURRENCY.md`'s trigger.

**Reviewer counsel**: (a) either admit the term on concept-spread and say so,
or leave it and note the admission rule tolerates concept-carrying; (b) "may
hold a worktree" / "the unit that claims work and owes a closing record".
Decision is Mike's.

### AW8 — LOW — when the adaptation element reaches child floors, the honesty-precondition sentence is the safety-load-bearing part

**Claim**: the open propagation item will inline a *short* adaptation line
into child floors. The sentence doing the safety work in the parent is the
ordering: adaptation runs on evidence and **honesty is its precondition**
(`00-APEX.md:109-113`) — an inlined "adapt continuously, improve yourself and
your tools" *without* that sentence (and without the rule-3/4 fence, which
children inherit only by pointer) is the one shape that could licence drift
in a repo whose parent is never read.

**Evidence**: `docs/ROADMAP.md:71-75` (item names the surfaces, not the
wording constraint); `PROPAGATION.md` floor template as it stands.

**Reviewer counsel**: note on the propagation item: the child floor's
adaptation line must carry the precondition clause verbatim-or-equivalent.
Decision is Mike's.

### AW9 — nit — method README meta-list spacing

`docs/method/README.md:78-82`: the new GLOSSARY bullet is followed by a blank
line; the remaining meta bullets are not blank-line separated. Cosmetic
inconsistency introduced by `c85712d`.

## Lens summaries

- **Lens 1 (approach & assumptions)**: the widening itself is sound — the
  third element is genuinely grounded in running machinery, its seat *below*
  honesty is argued correctly (the feedback-loop argument at
  `00-APEX.md:109-113` is the right reason, not ceremony), and the triad's
  epistemology is internally coherent (truth as standard, honesty as
  achievable duty, transparency as component — with the innocent-omission
  carve-out doing real work). The failures are compositional: AW1 (proof bar
  vs principal authority), AW5 (transparency vs mandated withholding).
- **Lens 2 (correctness & quality)**: commit messages are honest and
  why-dense; dating was corrected to convention (though outside the delta —
  AW6); one overclaim found (`f52c50f` "README apex summary updated" — the
  root README was not, folded into AW2); the glossary's "every entry
  verified" claim re-ran nearly clean (AW7a the exception).
- **Lens 3 (completeness / harvest)**: the sweep gap is the main miss (AW2);
  no duplication found — the glossary's thin-anchor discipline mostly holds
  (AW3/AW4 the drift cases); DOCUMENTATION.md canon-class claim and the
  fleet precedent both check out.
- **Lens 4 (security & privacy)**: discharged explicitly above — scanner
  floor run where it can reach (clean), design-altitude pass by hand: no
  person-local or estate-sensitive leakage in the delta; the one
  behaviour-path defect a new rule creates is AW5; A6's self-modification
  path is fenced in the parent, with the child-floor residue named as AW8.

---

## Reconcile — after opening the deferred intent records

*Written after the findings above were durably committed to this file. The
records opened: `docs/sessions/2026-07-22-2134-apex-adaptation.md`,
`docs/sessions/2026-07-23-0021-honesty-triad-glossary.md`. No finding above
is removed or downgraded; what follows annotates provenance and answers the
authors' seeded questions, which this reviewer read only after committing its
own attack surface and findings (rule 1's deferral).*

- **AW1 provenance changes, substance doesn't**: the second dictation
  (2026-07-22 record) shows the proof-bar wording is Mike's near-verbatim
  dictation ("decisions that change design or affect any part of the
  doctrine … must be evidence based and proven with hard facts"), faithfully
  encoded — so AW1 is not agent overreach but a scope question the dictation
  left open, now squarely the principal's to rule on: whose changes the bar
  binds, and how it composes with his own reserved authority. The intent
  record itself flags the "testimony, not evidence" line and the
  at-apex-strength claim as agent-authored connective tissue to attack —
  independently converging with this finding. Severity stands (the text at
  HEAD binds readers regardless of who worded it).
- **AW2 sharpens**: the 0021 record shows a ripple assessment *was* run and
  recorded (COMMUNICATION / REVIEW / AUTONOMY / child floors, each judged
  no-change with grounds — good practice), but its sweep list did not include
  the in-repo apex restatements AW2 enumerates (root README, PRINCIPLES §0
  lines, session-onramp skill, PROPAGATION prose). The finding stands as a
  gap in an otherwise well-executed check.
- **AW6 half-anticipated**: the 0021 record discloses the date-stamp
  corrections folded into the records commit — the disclosure exists, but the
  queue pointer's delta list still excludes `d104c51`. Finding stands as the
  pointer-hygiene half only.
- **Seeded questions answered** (the authors' floor, not this review's
  fence):
  - *Placement* (second-in-apex, above the Laws in document order): sound —
    "just below honesty" reads naturally as rank *and* order, and the
    subordination argument (agent-authored, per the record) is the right
    reason, endorsed under lens 1.
  - *Genericisation level*: verified safe — no hostnames, usernames, or key
    material at HEAD, cross-checked read-only against the source repo; the
    generic mechanism (agent key-crowding, algorithm class) is fine to carry
    publicly. See lens 4 discharge.
  - *Worked-case weight* (17 lines in the apex vs a pointer to a ros
    bearing): acceptable as built — the case grounds two bullets *and* the
    lived-experience close, and a pointer-only version would move the apex's
    only concrete grounding into a private repo that adopters and child
    sessions cannot read. If the apex ever gains more worked cases, revisit.
  - *One review spanning both intent records vs splitting the triad*: the
    single cycle worked — the five commits are one coherent widening and the
    findings interlock (AW1 spans both records' subject matter); a split
    would have doubled ceremony without independence gain.
  - *"Testimony, not evidence" / at-apex-strength connective tissue*:
    attacked under AW1 — the line is good doctrine but its unscoped bind is
    the MAJOR.

---

## Decisions (stamped 2026-07-23, the applying session)

Mike ruled **accept-all as counselled** (2026-07-23), with AW1's scope
sentence agreed verbatim: *the proof duty attaches to the agent's proposals
and to the grounding and recording of the principal's rulings, never as a bar
the agent holds against the principal.* Applied in `e8d707c` by a session that
authored neither the doctrine nor this verdict.

- **AW1 [fixed]** — scope sentence added to the proof-bar bullet
  (`00-APEX.md`), citing `RECORD.md` as where a ruling becomes a decision of
  record.
- **AW2 [fixed→backlog split]** — the counselled fix (name every stale
  restatement surface on the propagation item so the sweep is mechanical)
  applied in `e8d707c`; the sweep itself rides that item, as counselled.
- **AW3 [fixed]** — glossary Cold review entry now states the spawn
  criterion, the taker-writes-the-brief split, and cold-context vs cold-spawn.
- **AW4 [fixed]** — glossary Doctrine entry marked structural and pointed at
  `REVIEW.md` rule 3 as the functional canon.
- **AW5 [fixed]** — the triad's mandated-withholding boundary clause added
  (value withheld + existence declared = transparency discharged).
- **AW6 [fixed]** — ROADMAP pointer rule: later commits touching a queued
  delta's surfaces widen the delta list in the same commit.
- **AW7 [fixed]** — (a) testimony admitted on concept-spread, said in the
  entry; (b) session "may hold" a worktree. Both remain PROPOSED under the
  SEED banner for the ratify pass.
- **AW8 [fixed]** — precondition-clause constraint recorded on the
  propagation item.
- **AW9 [fixed]** — spacing normalised.

**MAJOR in this pass ⇒ the application (`e8d707c`) inherits rule-4 status:
`⏳` queued refs-only; the applier spawns nothing.**
