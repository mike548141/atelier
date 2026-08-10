# 2026-08-10 · 0036 UTC · plainscan's repo plane rescoped to prose the principal reads

**Session:** Fable, wt: plainscan-rescope-0810. Mike flagged parallel sessions
mid-turn, so the lane was claimed on `main` and pushed (`a2ab913`) before the
first edit, and every stage was explicit-path only.
**Trigger:** Mike proposed removing plainscan altogether and asked for a
challenge.
**Landed:** `a2ab913` (claim), `e390382` (the scoping), plus the records commit
that carries this file.

## What Mike said

Verbatim, because the proposal frames the whole session:

> I am considering removing the plainscan guard all together. The trust review
> session we had was about what responses you give me IN THESE SESSIONS and not
> in the documentation outputs. 99% of the documentation you write is to keep a
> record, collect data, and for consumption by yourself (claude) not me as the
> principal.

## The challenge, and the ruling

Two facts stood against full removal. First, it silently kills the reply gate:
`plain-reply.py` imports `scan_text` from `plainscan.py` and fails open by
design, so deleting the engine removes the session-facing control — the one
the 2026-08-09 trust review produced and Mike ruled live — without an error
appearing anywhere. Second, the audience argument is right about records and
wrong about the rest: ruling asks, review briefs, and doctrine in a public
repo are prose Mike does read, and the ruling queue makes them the
highest-stakes prose in the estate.

Mike's ruling, verbatim: *"I accept your recommendation"* — of the three
options offered, option 1: engine and reply gate untouched; the repo plane
scoped to human-read docs by excluding records, the same shape as the
cold-pass records exclusion.

## What landed

`RECORDS_GLOBS` in `plainscan.py` — `docs/SESSIONS.md`, `docs/sessions/`,
`docs/ROADMAP-DONE.md` — applied only when a directory is expanded. Records
are append-only history for the next session's agent; rewriting them would be
dishonest, so a warning there has no possible fix and is pure noise. Edges
pinned by tests: an explicitly named records file is still scanned (explicit
selection beats default exclusion), and `ROADMAP.md` never matches the
`ROADMAP-DONE.md` glob — the live roadmap is exactly the ruling-ask prose the
plane exists for. `--include-records` restores the old scope. The floor
registry entry is unchanged; the exclusion ships to every child through
`atelier@main` with no per-repo edit.

**Measured, not estimated:** atelier's advisory tally fell 7,817 → 4,440;
records carried 3,377 findings, and the two heaviest files in every previous
run were both records. The reply plane is untouched — `scan_text()` has no
scoping, because every reply is written to the principal.

## Honest notes

- **Self-authored end to end** — the recommendation, the build, and the
  COMMUNICATION.md rewrite came from the same session, so the rule-4 `⏳` is
  queued in the roadmap entry and this session spawned no review.
- **The gate fired on its own defender.** This session's first reply — the one
  arguing plainscan has value — was blocked by the Stop hook for two bare
  reference codes and rewritten. Recorded as evidence the reply plane works,
  and it is independent of the repo-plane question Mike raised.
- **The backlog item's scope decision is now half-made.** Records are out by
  ruling; the 4,440 findings in human-read docs remain, and which slice to
  work down is still Mike's call. The repo-plane numbers (35 words / 40 chars)
  also remain unruled — the rescope does not touch that item.
- **Verification:** plainscan module tests 47 → 51, python suite 1,294 → 1,298
  green, instrument tests exit 0, selftest gains the records checks. The
  floor run on the records SHA `959502d` concluded **success** — polled to
  completion and read, not assumed, because under cancel-in-progress a
  parallel push can kill a run mid-flight.
