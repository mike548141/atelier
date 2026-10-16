# Deferred sibling — the pre-flip gate and publishscan --history (160/740)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-pre-flip-gate-history-cold.md` are committed.** A
floor, never a fence: these questions were seeded by a brief-writer who read the
landing diffs and commit body, so they carry that reading's framing. Reconcile
against them; do not let them narrow what you found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

- `docs/reviews/2026-08-02-2313-publishscan-cold.md`
- `docs/reviews/2026-08-03-0649-publishscan-application-cold.md`
- `docs/reviews/2026-08-02-2210-publish-surface-delta-cold.md`
- `docs/reviews/2026-08-03-0653-publish-surface-application-cold.md`
- `docs/reviews/2026-10-03-0357-publishscan-round-2-cold.md`
- `docs/reviews/2026-07-28-1216-estate-root-widening-cold.md` (names the
  pre-flip moment)

## The queue pointer's own lens hints

None. The pointer is refs-only, plus the orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diffs)

1. `run_history` prints a pass and exits 0 for "not a git repository". The gate
   is run on the one repo about to be published; is a gate pointed at the wrong
   directory meant to pass?
2. The docstring says refs, not `--all`, because "the stash is never pushed". Is
   the converse covered — a ref the host holds that the local clone does not
   (pruned branches, pull-request refs, commits reachable only by hash after a
   force-push)? Does the doctrine tell the gate runner to fetch them first?
3. The bullet says the gate "runs `publishscan --history`", but the mode is
   opt-in and nothing in the floor runs it. What makes the doctrine's "runs"
   true at the moment of a flip?
4. "The scrub runs last … and include[s] those records" — if the scrub finds
   something in the gate's own record and that record is then edited, has the
   scrub still run last?
5. The changelog says no repo went red because no sibling tracked `*.egg-info/`
   at its tip, while "one repo's history held it". Is that repo now a known
   `--history` finding, and is anything recording that it is owed before its own
   flip — in a private place, not here?
6. The CHANGELOG entry carries a line longer than the column budget. Is it inside
   a guard's reach, and was the wrap guard's exemption for that file deliberate?
