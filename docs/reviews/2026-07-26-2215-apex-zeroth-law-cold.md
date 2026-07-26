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
