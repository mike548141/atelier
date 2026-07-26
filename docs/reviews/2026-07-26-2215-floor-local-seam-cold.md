# Cold review (rule 4) — the repo-local floor seam

**Subject (refs only):** commits `f526dea` and `76f4acc` at HEAD (plus the
records-pointer commit `92bc0cb` that queued this review). Touched surfaces:
`tools/floor.py` (the `local` block, `_load_local`, the `is_local` path
through plan/run/render, `_interpreter`), `tools/floorfleet.py` (the `➕`
board line), `tools/test_floor.py`, `tools/test_floorfleet.py`,
`docs/build/REPO-STANDARD.md`, `docs/build/templates/CONTRIBUTING.md`,
`docs/build/templates/workflows/floor.yml`, `CHANGELOG.md`.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and the
SESSIONS index one-liner for this work before writing this stub. Nothing
evaluative from either appears above the divider.

**The reviewer's first acts:** establish what the seam is and why it exists
from the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). This extends a *security floor's* configuration
surface with repo-owned executable checks — what a malicious or careless child
config can now make the floor do is lens-4 territory at both altitudes,
checked against open catalogues, not recalled. Re-run every claim the two
commit messages and the CHANGELOG entry make — test counts, fail-closed legs,
visibility surfaces — and probe the seam with crafted configs of your own
design (colliding names, out-of-repo `run` paths, missing scripts, permission
edge cases, softening vocabulary).

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 tools/floor.py --selftest` · `python3 -m unittest tools.test_floor
tools.test_floorfleet` · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js` · your own probe configs in a scratch
repo. `/security-review` reaches only pending diffs — on a landed delta
discharge it in one explicit line with grounds; the manual pass above stands
regardless.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/` (quarantined). Do not grep git
history for review commits; confine git archaeology to the delta commits
named above. Open the deferred section below — and the intent record it
names — only after your findings are durably written to this file; then
append the reconcile, named as such.

Findings carry stable IDs (**LS1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts. The
seam edits `REPO-STANDARD.md` and adds a surface every child may declare
against — self-authored doctrine by function: REVIEW.md rules 3–4 govern —
findings are the principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-26-1120-floor-local-seam.md`](../sessions/2026-07-26-1120-floor-local-seam.md)
