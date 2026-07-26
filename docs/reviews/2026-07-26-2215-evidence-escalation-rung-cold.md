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
