# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-private-state-type-only-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

## The queue pointer's questions (author-written, verbatim)

> whether the condition/act line is drawable by a session at write time; whether the drafter's two
readings follow from the posture.

## The brief-writer's own questions

1. The table allows "Session ran in `widget-api` to land item X". The Decision lists "the work in
flight inside it" as type-only. Do they agree?
2. "Landed a fix for X" is an act that discloses a prior condition. Which side of the line is it?
3. A type read beside a roster published in the same record: when does "a private child" stop being
type-only, and does the "a type only one repo fits" reading reach the join across sentences?
4. The draft's Consequences said a B-or-C outcome would state the rule at the point of use, in the
session-record and review-brief templates, per this repo's rule-grammar finding. The accepted
Consequences state it only in `RECORD.md`. Silent scope-cut, or a decision? Check the templates
(V3).
5. `RECORD.md` says "Ruled 2026-11-08" and, in the same line, "not his own words". Does the house's
vocabulary allow that?
6. "Worked examples in doctrine keep their names": check against the later `9c8cb7e7` commit's rule.
7. The landing commit and the pointer commit are separate (`38536e4c`, then `7ad98503`).

## What the brief-writer ran, and what it got

- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).
