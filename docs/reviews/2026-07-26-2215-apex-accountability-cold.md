# Cold review (rule 4) — apex: the principal's authority is rooted in accountability

**Subject (refs only):** the opening grounding paragraph added to
`docs/method/00-APEX.md` § "The principal's authority is conditioned on being
informed" in commit `4af5f3b` (2026-07-24). Establish the exact hunk with
`git show 4af5f3b` and review it at HEAD, in the context of the whole apex.

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
(`docs/method/REVIEW.md`). This is **apex text** — the widest blast radius in
the operating model; every future session and every child repo inherits its
framing. The heavy lenses: 1 — is accountability the right root for the
authority claim, does the RASCI framing hold, and does grounding the
reservation in consequences create any unintended release (if a decision's
consequences somehow didn't land on the principal, would the paragraph read as
licensing the agent to take it?); 3 — coherence with the rest of the apex and
with every in-repo restatement of the informed-principal section. This is a
public, shareable repo — lens 4 includes whether the paragraph's liability
framing (privacy, copyright/IP, licence/contract) says anything an adopter
would inherit wrongly.

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 -m unittest discover -s tools` · `node --test instruments/*.test.js`.
Lens 4's scanner: a landed markdown doctrine delta — `/security-review`
reaches only pending diffs and excludes markdown, so discharge it in one
explicit line with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**AA1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored apex doctrine: REVIEW.md rules 3–4 govern — findings are the
principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* no separate record — the queue pointer states the intent as
the principal's own reading: the principal's authority is born of the
principal's accountability (RASCI *Accountable*) — he funds the work, the
world attributes the product to him, and the liabilities (privacy,
copyright/IP, licence/contract) land on him; the reserved decisions are his
*because their consequences are*. The paragraph is the author-agent's wording
of that reading, at the principal's instruction.
