# Cold review (rule 4) — ADR 0008: enforcement is called, not copied

**Subject (refs only):** ADR
[`0008-enforcement-is-called-not-copied.md`](../decisions/0008-enforcement-is-called-not-copied.md)
and the surfaces it governs at HEAD: `tools/floor.py`, `tools/floorfleet.py`,
`tools/pre-commit.sample`, `.githooks/`, `.github/workflows/floor.yml`,
`docs/build/templates/workflows/floor.yml`, the two 2026-07-25 sections of
`docs/method/PROPAGATION.md` (enforcement propagates by call; enumeration not
assumption), `.atelier-floor.json`, and their test files. Establish the
enacting commit set yourself with `git log --oneline --since=2026-07-25
--until=2026-07-26 -- <those paths>` (the first is `40c7a22`); the same-day
follow-on hardening commits on `tools/secretscan.py` / `tools/leakscan.py`
(absolute-path refusal in `--staged`) and the create-repo CONTRIBUTING
template are in scope.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub, and a git-log grep
incidentally surfaced the *subject lines* of a withdrawn earlier pass on this
item (quarantined under `docs/reviews/withdrawn/`, wrong tier, not accepted —
its findings are dead and are not reading for this redo). Nothing evaluative
from any of those sources appears above the divider; the seeded question from
the queue pointer sits below it, deferred.

**The reviewer's first acts:** establish what the work is from the ADR, the
delta, and HEAD yourself; name the load-bearing assumptions and attack surface
as your own before anything else; run all four lenses at the widest scope the
work admits (`docs/method/REVIEW.md` — the lenses organise scope, never bound
it; the ADR's decision and its stated alternatives are as reviewable as the
code). Re-run every "live-proven" claim the delta's commit messages, the ADR,
and the CHANGELOG entries make; a proof that no longer reproduces is a finding.

**Re-run obligations:** `python3 tools/floor.py --plane ci` (whole-tree floor
at HEAD) · `python3 tools/floor.py --selftest` · `python3 -m unittest discover
-s tools` · `node --test instruments/*.test.js` ·
`python3 tools/floorfleet.py --check` (and `--remote --check` if `gh` is
available — read-only) · the planted-secret / fail-open regression tests in
`tools/test_precommit.py` and `tools/test_floor.py`. Lens 4 runs at both
altitudes: this is a security floor — supply-chain posture of the call-not-copy
mechanism is in scope, checked against open catalogues, not recalled.
`/security-review` reaches only pending diffs; on a landed delta discharge it
in one explicit line with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/` (quarantined). Do not grep git
history for review commits; confine git archaeology to the delta surfaces
named above. Open the deferred section below the divider — and the intent
record it names — only after your findings are durably written to this file;
then append the reconcile, named as such.

Findings carry stable IDs (**EP1…**), each with claim / evidence / counsel;
close with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts
(MAJOR/minor/LOW/nit). This is self-authored doctrine by function (an ADR plus
policy-as-code that governs every repo): REVIEW.md rules 3–4 govern — every
finding is counsel, the decisions are the principal's, and nothing is applied
in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-25-1311-policy-propagation.md`](../sessions/2026-07-25-1311-policy-propagation.md)

*The queue pointer's seeded question (a floor, never a fence):* aim at the one
real trade — moving every repo onto a floating `@main` caller swaps a slow
silent failure (vendored copies drifting stale) for a fast loud estate-wide
one (a bad push to atelier breaking every child's floor at once). Is that the
right trade for a *security* floor?
