# Deferred sibling — marker kinds and finding IDs (160/750)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.md` are committed.**
A floor, never a fence: these questions were seeded by a brief-writer who read the
landing diffs and commit bodies, so they carry that reading's framing. Reconcile
against them; do not let them narrow what you found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md` (the shared
  grammar; its AM4 is the defect `db1aa4d` cites)
- `docs/reviews/2026-10-04-2215-exception-register-design-cold.md`
- `docs/reviews/2026-10-04-2215-linear-line-reader-cold.md`
- `docs/reviews/2026-10-03-0357-publishscan-round-2-cold.md`

## The queue pointer's own lens hints

None. The pointer is refs-only, plus the orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diffs)

1. `covers` keeps "any other scope exempts every kind". A marker with a typo in
   its kind therefore exempts everything — and the printed ID now invites readers
   to type kinds by hand. Does the new hatch make the old widening more likely to
   be hit, not less?
2. sizescan's `_kinds` lists three kinds; the `--json` comment and the commit say
   "up to two". Which is true, and after `72a68cc` removed one kind, does a live
   marker or a stored ID now name a kind that no longer exists?
3. spellscan's ID uses the word lower-cased. Does the marker grammar compare
   scopes case-insensitively, so a capitalised finding's ID still round-trips?
4. `ded8d32` says conflictscan, wrapscan and indexscan get no ID because their
   marker takes no scope. `1c24781` later gave indexscan a scoped kind. Is the
   ID set now stale for indexscan, and does anything pin the rule "a guard with a
   scoped marker prints an ID"?
5. The back-compat evidence for both commits ran the scanners over 28–29 sibling
   repos on the machine. Did any of that output — repo names, paths, findings —
   land in this public repo's records or tests?
6. leakscan's ID is the rule name. For a machine-local term hit, is the "rule"
   a generic label or something derived from the term itself?
