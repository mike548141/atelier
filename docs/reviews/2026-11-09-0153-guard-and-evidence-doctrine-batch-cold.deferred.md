# Deferred reading for `2026-11-09-0153-guard-and-evidence-doctrine-batch-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether any addition restates a rule already homed elsewhere; whether escaping in `strip_controls`
reaches every surface that prints a child's config.

## The brief-writer's questions

1. Which printing surfaces of `floor.py` and `floorfleet.py` carry child-sourced text and do not
pass through `strip_controls`?
2. §16–§18 as read by a child: what would a child's first honest compliance step be, and does the
rule say so?

## What the brief-writer held back

- The changelog carries a measured claim about the fleet (byte-identical report); it is in the
  re-run list.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`test_floor`: 187 tests, OK, exit 0. `floor.py --plane ci`: exit 0, with 28 `secretscan` advisories
reported and not blocking. `--plane hook`: exit 0. Full suite under `python3` 3.14: 2,643 tests, OK,
exit 0, 1,228 s at a load of about 20. `floorfleet --json`: exit 0; 23 rows, 1 parent, 21 wired
children, 1 absent. Children whose `.atelier-floor.json` carries a bidi override or isolate
character: 0 of 21. The before-and-after comparison of the fleet report was not run.

