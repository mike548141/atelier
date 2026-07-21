<!--
  STAMPED POINTER, NOT A SECOND SOURCE. The canonical review doctrine — the
  trigger, the calibration, the lifecycle, the independence rules — lives in
  atelier's docs/method/REVIEW.md. What follows is a thin floor (enough to act
  on without opening atelier) plus a pointer up. Do NOT restate atelier's
  trigger list here: an unmarked local copy is how this file drifted from its
  parent once already (2026-07-18 — it still carried a diff-shaped trigger, and
  affirmatively exempted "a doc line" while the parent said otherwise).
  Narrowing-free: this may compress the parent, never contradict it.
-->

# Reviews

Significant or risky work gets a peer review before it's trusted, and the review
is written down here. The house practice: a **more capable model (Fable) reviews
the approach, assumptions, security & privacy, and real-world behaviour — not
just whether the code is correct** — before the work is relied on. Reviewer
scope is the whole commitment — intent, decisions, design, docs, code, tests,
behaviour (exercised live where possible); the brief's non-goals are the only
legitimate narrowing, and security & privacy is a must on every review (likely
threat vectors checked against open catalogues such as OWASP, not recalled; a
work with no such surface says so explicitly, with grounds). The builder (usually Opus) then applies
the findings. Canonical doctrine, and anything this file doesn't answer:
`<atelier-path>/docs/method/REVIEW.md`.

## When to write one

Not all work earns one. **The trigger is commitment, not artefact** — the
question is not what form the work took, but *what will come to rest on it once
it is trusted*. Ask it holding a design, a decision, or a diff; it parses the
same either way:

- a design others will build to, or a decision that forecloses alternatives —
  reviewable **before** the code exists, which is when it's cheapest to be wrong;
- behaviour a user sees (an interaction, an output, a workflow);
- bundled third-party code, added or removed;
- a load-bearing assumption worth challenging before it's trusted (e.g. "this
  API's error contract works the way we assumed").

Genuinely routine work (a typo, a config tweak, a records-only edit) doesn't need
one — CI and a real look are enough. **A doc or design record is not routine by
virtue of being prose**: doctrine, ADRs, roadmap direction and architecture notes
are exactly the class where a wrong premise propagates furthest. Calibration —
which risks earn the full ceremony versus the mechanical floor — is atelier's
call, not this file's: see *Whether work earns a review at all* in `REVIEW.md`.

## Format

One file per review, `<YYYY-MM-DD>-<HHMM>-<slug>.md` (start time, 24-hour, in
UTC — `date -u`, atelier ADR 2026-07-15; coordination-free, per atelier's
`method/CONCURRENCY.md` record-identifier rule). Keep it a brief the reviewer can
act on, not a transcript. Every field takes work that isn't built yet:

- **Subject** — what is under review, in what state (designed / built / shipped),
  by which model and date.
- **Type** — "approach + assumptions" vs "correctness only". Say so.
- **Scope** — point at the exact thing: the files or diff if it exists, the
  design record or decision if it doesn't. Point, don't paste.
- **Load-bearing assumptions to challenge** — the things that, if wrong, break
  it. This is the heart of the brief, and it is the field that has the *most* to
  bite on before anything is built.
- **Grounding** — for built work, what was actually driven (real inputs, real
  environment) and what's still owed; for a design, what would have to be true
  for it to hold, and how that could be checked cheaply. Name the concrete thing,
  not "tests pass".
- **Non-goals** — what's correctly out of scope.

Keep Fable sessions short and pre-scoped
(`<atelier-path>/docs/method/MODEL-ECONOMICS.md`): hand it the scoped subject,
ask for findings, apply fixes back on Opus.
