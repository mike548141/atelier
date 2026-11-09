# Deferred reading for `2026-11-09-0153-review-notes-date-kind-and-visibility-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether a reviewer can still reach held-back notes; whether an unlabelled date read as a mandate
strands a child; whether the cross-check can pass while a repo is public.

## The brief-writer's questions

1. Outside Actions, what does the visibility check do, and is the "detects" claim bounded to CI in
every surface?
2. Where does the `.deferred.md` sibling actually sit in the brief-writer flow, and does the rule's
named location cover a headless brief-writer?
3. How does `floor.py`'s hook-plane comparison against HEAD behave at a repo's first commit or a
shallow clone?

## What the brief-writer held back

- The principal's answer on `260/050` says public repos get the stricter checks; the changelog names
  what a public declaration tightens as not built.
- The principal's answer on `160/450` says existing dates get labelled; the changelog says none is
  labelled by this change, each repo's own edit, and which kind needs the principal.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`test_floor`: 187 tests, OK, exit 0. `test_floorfleet`: 119 tests, OK, exit 0. `test_coldsweep`: 37
tests, OK, exit 0, under `/usr/bin/python3` 3.9, and again inside the full suite under 3.14.
`floor.py --plane ci`: exit 0, with 28 `secretscan` advisories reported and not blocking. `--plane
hook`: exit 0. Full suite under `python3` 3.14: 2,643 tests, OK, exit 0, 1,228 s at a load of about
20. `gh repo view --json visibility`: PUBLIC, exit 0. `floorfleet --json`: exit 0; 23 rows, 1
parent, 21 wired children, 1 absent. `advisory_kind` set on 0 of 23 rows; `visibility` declared by 0
of 20 wired children with a config, 1 with no config.

