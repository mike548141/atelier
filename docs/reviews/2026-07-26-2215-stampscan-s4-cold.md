# Cold review (rule 4) — stampscan (S4), first-of-kind scanner review

**Subject (refs only):** `tools/stampscan.py` + `tools/test_stampscan.py` at
HEAD; the stamp-marker convention added to `docs/method/PROPAGATION.md` and
`docs/build/templates/CLAUDE.md`; the build commit `2fe97f3` and the
subsequent unwiring commit `4f637b0` — the scanner is currently **built but
wired into no plane**, and both that state and the commit that produced it are
part of the subject. Establish the full delta with `git log --oneline --
tools/stampscan.py docs/method/PROPAGATION.md .github/workflows/ci.yml`.
This is the scanner's **first-of-kind review**: whether and under what
precondition it may be wired at all is the review's call to recommend — the
decision is the principal's.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer (which
carries the author's scrutiny list — deferred below) and SESSIONS index
one-liners, and a git-log grep incidentally surfaced the *subject line* of a
withdrawn earlier pass on this item (quarantined under
`docs/reviews/withdrawn/`, wrong tier, not accepted — its findings are dead
and are not reading for this redo). Nothing evaluative from any of those
sources appears above the divider.

**The reviewer's first acts:** establish what the scanner is, what invariant
it enforces, and why it is unwired from the code, tests, and the two commits
yourself; name the load-bearing assumptions and attack surface as your own;
run all four lenses at the widest scope (`docs/method/REVIEW.md`). The marker
convention written into PROPAGATION.md and the child template is doctrine text
on the same footing as the code. Re-run every claim the commits and CHANGELOG
make — test counts, the live template-pair comparison, and the stated reason
for `4f637b0` (reproduce the failure mode it describes before trusting it).
Probe with crafted inputs of your own design, including documents that merely
*describe* the marker syntax.

**Re-run obligations:** `python3 -m unittest tools.test_stampscan` · run the
scanner over the live tree and over probes you construct ·
`python3 tools/floor.py --plane ci` · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js`. Lens 4: `/security-review` reaches only
pending diffs — on a landed delta discharge it in one explicit line with
grounds; the manual code-altitude pass (input handling, exit-code contract,
what a crafted document can make the floor do) is in scope regardless.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/` (quarantined). Do not grep git
history for review commits. Open the deferred section below — and the intent
record it names — only after your findings are durably written to this file;
then append the reconcile, named as such.

Findings carry stable IDs (**ST1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL**, severity counts, and an
explicit wiring recommendation with its precondition(s). The scanner and its
marker convention encode policy (doctrine by function): REVIEW.md rules 3–4
govern — findings are the principal's to decide; nothing is applied in this
pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-22-1036-invariant-candidates.md`](../sessions/2026-07-22-1036-invariant-candidates.md) § S4.

*The author's scrutiny list from the queue pointer (a floor, never a fence):*
**(0) the wiring blocker, found in-run:** the marker parser recognises stamp
markers anywhere it scans — including prose and code spans that only
*document* the syntax — and treats a stray/unpaired marker as a hard config
error (exit 2) that `--warn` does NOT suppress, so even advisory wiring lets
ordinary docs about stampscan block the floor (a ROADMAP pointer describing
the markers reddened the floor mid-run; the CI step was reverted). Stated
precondition to wire: strip fenced/inline code before marker-hunting, as every
sibling scanner does. **(1)** the marker convention borders on a doctrine act —
`narrow=<reason>` declares a legitimate narrowing vs a silent drop
(mechanically identical subsequences) and needs explicit ratification.
**(2)** the stamp-end marker is appended inline to the `---` divider rather
than its own line — a placement compromise forced by a collision with
pre-existing `test_templates.py` slice logic (a cleaner fix teaches
`template_block()` to strip markers).
