# Cold review (rule 4) — PRINCIPLES §1: "Design the way out before the way in"

**Subject (refs only):** the bullet added to `docs/method/PRINCIPLES.md` §1 in
commit `e29c49a` (2026-07-24). Establish the exact hunk with
`git show e29c49a` and review it at HEAD, in the context of the whole
principles set.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub. Nothing evaluative from
either appears above the divider.

**The reviewer's first acts:** establish what the bullet claims and why from
the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). The heavy lenses: 1 — is adopt-only-once-the-exit-
exists the right rule stated at the right strength (absolute vs default), and
does it hold against the repo's own practice (the dependencies atelier and its
tooling actually carry — check them against the rule rather than trusting the
bullet's own grounding claims); 3 — coherence with its named twin ("Build the
way back before the way forward") and with REACH's escalate-cheapest-first /
never-mint-what-you-can't-withdraw language — genuine pairing or duplicated
rule with drift potential; 2 — any overclaim in the bullet's grounding.

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 -m unittest discover -s tools` · `node --test instruments/*.test.js`.
Lens 4: a landed one-bullet markdown delta — discharge `/security-review` in
one explicit line with grounds; note that the bullet itself is *about*
dependency risk, so lens 4's design-altitude reading of it (does following it
reduce or create exposure) is in scope.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**WO1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored doctrine at the principal's instruction: REVIEW.md rules 3–4
govern — findings are the principal's to decide; nothing is applied in this
pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* no separate record — the queue pointer states the intent: a
new resilience principle paired with "Build the way back before the way
forward" — before adopting an external dependency, first establish how you
keep working without it (fallback / export path / swappable seam / degraded
mode); adopt only once the exit exists. Grounded, per the pointer, in
atelier's zero-dependency tooling as the limit case and browser-fetch as the
documented dependency exception, and cross-linked to REACH.
