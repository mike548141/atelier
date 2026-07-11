# 2026-07-11 · N4 trigger follow-ups closed — atelier ci.yml + numen floor.yml (Opus)

The two follow-ups the child-CI-floor review (session 30) left standing, both
the same **N4 trigger gap**, both proven on real GitHub Actions. A deliberately
low-ceremony session: CI-trigger widenings are self-verifying (prove the gap,
watch it green) — no separate review earned, per the session-29 calibration this
session is a first live application of.

## The gap

floor.yml's N4 finding widened child CI from `push:[main]` to every push,
because on a public repo a push to *any* branch is already publication — a
feature branch that is never PR'd was previously scanned by nothing. The review
flagged two places carrying the same narrow trigger, out of its own scope:
atelier's **own** `ci.yml`, and every **workflow-file** fix baked into numen's
copied `floor.yml` (the scanner fixes N1–N3 float via `atelier@main`; the YAML
fixes N4/N5/N6 do not).

## atelier `ci.yml` — every push (`2a4b2fd`)

Trigger widened to `push:` (no branch filter) + `pull_request` +
`workflow_dispatch`, reasoning in-file: this job *is* the floor (it dogfoods the
publish-safety triad), so it gates publication, not just the merge. Double-run on
same-repo PR branches costs seconds (zero-dep stdlib) — the right side of the
trade for a safety floor.

**Proven closed, not asserted.** Floor re-run locally first (4 selftests, scan
triad + linkscan clean, both YAML files parse with the new trigger). Pushed →
main run green (`29131213386`). Then the actual claim: pushed a throwaway
`n4-trigger-proof` branch (empty commit, never PR'd) → CI fired and went green on
it (`29131233488`) — a run that could not have existed before the widening.
Branch torn down local + remote; no refs remain.

## numen `floor.yml` — re-copy (`f81f66f`)

Byte-identical re-copy of atelier's post-review template. Diff is exactly
N4/N5/N6: every-push trigger, a scanner-selftests step, and header docs for the
false-positive hatches. numen's tree re-scanned clean first with atelier's
current tools in the exact floor.yml shape (`secret/leak/link --root repo repo`,
CWD ≠ root — the N3 case). Pushed → floor green (`29131265209`); the job log
confirms the **new N5 selftests step ran**, so the re-copy is live, not merely
still-passing-old.

Incidental restated (session 28): numen's pre-commit hook is frozen pre-scaffold
(no linkscan) — on numen the CI floor is the only linkscan gate. It caught the
inherited breaks before, and the re-copy keeps it current.

## Templates pass — the session-29 sharpening propagated (`53b41db`)

Same session, related strand (both are review follow-ups). The condensed
template copy `build/templates/docs/MODEL-ECONOMICS.md` shipped **"One task per
session; start fresh"** — the exact misreadable phrase session 29 diagnosed as
driving over-application of "one thing per session," inherited by *every*
scaffolded child. Rewritten to carry the reviewed sharpening (a coherent *line*
of work, not a single checkbox; break for a genuine reason, not because one item
went green) and to name the new ceremony-to-risk bearing in the point-up pointer.

Judged **self-verifying, not fresh-review-owed** — a live application of this
session's calibration lesson turned on the deferral itself: session-29-me flagged
this "review-owed, separate," but it merely applies an *already-reviewed*
decision (session 30: PASS, no findings) to its condensed mirror. That is the
second-copy-drift class `test_templates.py` exists to catch; there is no live pin
on this file's body (the CLAUDE.md stamped block is the pinned one), so the check
is: does the copy now read consistent with the reviewed source? It does. Suite
205 OK, unchanged.

## Fleet pin bump — all three children current (bbdeece → d45a431)

With the owed follow-ups closed and HEAD green, took the deliberate fleet
maintenance `tools/pins.py` had been flagging: faves/numen/ros all pinned at
`bbdeece` since session 21, **22 commits behind**. Done per PROPAGATION, not
mechanically: read the `bbdeece..d45a431` delta first (the substantive doctrine
is the ceremony-calibration — cb37310 + this session's template sharpening
53b41db — plus the child-CI floor availability, the linkscan build/ unmasking,
and ADR 0005 public); ran **each child's stamped drift check verbatim** (C2's
lesson — `git -C "../atelier" log --oneline bbdeece..HEAD`, all three worked and
showed the 22) before touching a pin. Bumped both occurrences per child (heading
pin + drift-check SHA); post-bump each drift check runs **clean** and
`tools/pins.py` reads **all 3 current ✓**. Children functionally had the current
scanners already (floor.yml floats `atelier@main`); the bump is the
doctrine-version acknowledgment — "read and adopted up to d45a431." Commits:
faves `aaeb785`, numen `86a0f45`, ros `d85bbb9`; numen's floor re-ran green on
its bump (re-exercising the every-push trigger). Notably surfaced the
ceremony-calibration doctrine down to every child's own future sessions — the
whole point of not leaving them 22 behind.

Deliberately **not** forced as part of the bump: adopting `floor.yml` into
faves/ros (a per-repo CI call, not implied by a doctrine-read); re-syncing any
child's own condensed MODEL-ECONOMICS copy from the sharpened template (the
template governs new scaffolds, not a retro-sync mandate).

## Left open

- ros B14 estate access map — a ros session's job, as ever.
- faves/ros may adopt the child-CI `floor.yml` at their discretion (available,
  not owed).
