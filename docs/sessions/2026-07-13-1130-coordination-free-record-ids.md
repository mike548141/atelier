# 2026-07-13 · 11:30 — record identifiers go coordination-free (Fable)

The same conversation as session 52, reopened minutes after it closed: Mike
challenged the counter-keeping carve-out in the fix just landed ("keep a
counter only where the running number itself carries meaning") — the running
number carries no meaning to him beyond chronology, which the date already
gives — endorsed coordination-free identifiers, and mid-turn extended the
ruling past session logs: "solve this for things like ADRs and any other
similar situations as well".

## The reframe

Session 52's fix kept the shared counters and added a discipline to manage
them (allocate late, provisional until pushed, first landed wins). This ruling
removes the shared resource instead: identifiers are built from facts the
session already owns — **date + slug**, plus start time (`HHMM`) where
same-day order matters (session logs) — so there is nothing to coordinate.
The silent-collision class is structurally gone: the worst case becomes two
sessions wanting the same *filename*, a visible trivial git conflict — the
append-tail case CONCURRENCY already handles. Supporting evidence was already
in the repo: `docs/reviews/` had drifted to date+slug naming in practice, with
zero incidents.

## Codified (`93e3e85`)

- **ADR `2026-07-13-coordination-free-record-identifiers`** — the deliberation
  (rejected: counters+discipline as the standing rule; NNNN-for-ADRs-only;
  locking). The first record named under the scheme it decides.
- **`method/CONCURRENCY.md`** — the session-52 bullet rewritten: the
  record-identifier rule leads; the three counter rules demote to interim
  discipline for repos still on legacy numbering; ros bearing kept.
- **`method/RECORD.md`** — session detail spec is now
  `<date>-<HHMM>-<slug>.md` (start time, 24-hour).
- **`method/PROPAGATION.md` + stamped template** — child block's Concurrency
  line recast (name records coordination-free; legacy counters allocate at
  landing), canonical + template together; drift test green.
- **`build/REPO-STANDARD.md`, decisions/reviews READMEs (repo + templates),
  ADR template** — `NNNN-slug` specs replaced with `<YYYY-MM-DD>-<slug>`;
  template renamed `0000-template.md` → `template.md` in both copies.
- **Never renumber history:** ADR 0001–0007 and session files through 52 keep
  their names and citations; old `ADR NNNN` references still resolve.

## Owed

- Children adopt at their next deliberate pin bump (ros's incident, ros's
  next bump).
- New/changed doctrine ⇒ the usual cold-review sweep covers it.

This file is the first session record named under the new scheme.
