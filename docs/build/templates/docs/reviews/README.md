# Reviews

Significant or risky work gets a peer review before it's trusted, and the
review is written down here. This is the house practice: a **more capable
model (Fable) reviews the approach, assumptions and real-world behaviour —
not just whether the code is correct** — before the work is relied on. The
builder (usually Opus) then applies the findings. The full lifecycle is
atelier's `docs/method/REVIEW.md`.

## When to write one

Not every change. Write a review brief when a change:

- alters behaviour a user sees (an interaction, an output, a workflow),
- touches or removes bundled third-party code, or
- makes a load-bearing assumption worth challenging before it's trusted
  (e.g. "this API's error contract works the way we assumed").

Trivial edits (a typo, a doc line, a config tweak) don't need one — CI and
a real look are enough.

## Format

One file per review, `<YYYY-MM-DD>-<HHMM>-<slug>.md` (start time, 24-hour —
coordination-free, per atelier's `method/CONCURRENCY.md` record-identifier
rule). Keep it a brief the reviewer can act on, not a transcript:

- **Build** — what changed and by which model/date.
- **Type** — "approach + assumptions" vs "correctness only". Say so.
- **Scope** — the exact files/diff. Point, don't paste.
- **Load-bearing assumptions to challenge** — the things that, if wrong,
  break it. This is the heart of the brief.
- **Real-world check** — what was actually driven (real inputs, real
  environment) and what's still owed. Name the concrete thing exercised,
  not "tests pass".
- **Non-goals** — what's correctly out of scope.

Keep Fable sessions short and pre-scoped (see
[`../MODEL-ECONOMICS.md`](../MODEL-ECONOMICS.md)): hand it the diff, ask
for findings, apply fixes back on Opus.
