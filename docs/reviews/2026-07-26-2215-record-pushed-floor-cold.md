# Cold review (rule 4) — RECORD.md: the close all-clear carries the pushed floor run's result

**Subject (refs only):** the sub-point added to `docs/method/RECORD.md`'s
all-clear evidence rule in commit `97b4fd2` (2026-07-23): when a close pushes,
the evidence is the floor at head, not the local scan. Establish the exact
hunk with `git show 97b4fd2 -- docs/method/RECORD.md` and review it at HEAD,
in the context of the whole close rule and its siblings.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub. Nothing evaluative from
either appears above the divider.

**The reviewer's first acts:** establish what the sub-point claims and why
from the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). The heavy lenses: 1 — is pushed-floor-at-head the
right evidence bar, and is the rule *followable* from where it binds (what
does a session do when the head run has not reported yet — does the rule
define an honest waiting state, and is that state usable in practice); 2/3 —
coherence with the rest of RECORD.md's close rule, CONCURRENCY's close
discipline, and any sibling that still teaches local-scan-as-all-clear. A rule
about close hygiene is only as good as its observability at close time —
attack that.

**Re-run obligations:** `python3 tools/floor.py --plane ci` (whole-tree floor
at HEAD) · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js` — and note what the *pushed* floor for
this worktree's branch can and cannot show you, since that boundary is the
rule's own subject. Lens 4: a landed markdown doctrine delta —
`/security-review` reaches only pending diffs and excludes markdown, so
discharge it in one explicit line with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**RF1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored doctrine: REVIEW.md rules 3–4 govern — findings are the
principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* the capture rode the queue pointer itself rather than a
separate record. Its stated grounding: commit `165c40f` — a 00:47 close had
pushed a 🎯-closed item and left the floor red (reviewscan red since 00:06
plus an un-harvested `[x]`), and the next session inherited the debt to
restore green. `git show 165c40f` is the deferred material.
