# Deferred sibling — indexscan cold pass (160/700)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-indexscan-guard-cold.md` are committed.** It is a
floor, never a fence: these questions were seeded by a brief-writer who read the
landing diffs and commit bodies, so they carry that reading's framing. Reconcile
against them; do not let them narrow what you already found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

No prior verdict names `indexscan`. Two verdicts own the open findings that
`tools/README.md` lines 4–5 allow-mark against (FW2, AM5):

- `docs/reviews/2026-09-25-0715-single-sourced-file-walk-cold.md`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`

## The queue pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type), plus the
orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diffs)

1. The ten `indexscan:allow` lines in `docs/SESSIONS.md` arrived in the merge
   commit `5600b0e`, not in `8d10487`. The commit body says the session index
   "reports 10 unlisted detail files, left for the records owner". Was leaving
   them for the owner and then silencing all ten in an unreviewed merge the same
   decision? Who ruled each reason, and is a blanket allow of a whole class of
   records what the guard's rule-(b) "fail noisy, then subtract" means?
2. The listed test is "any link or code span anywhere outside a fence". Does a
   passing mention in prose — say `` `ROADMAP.md` `` in a sentence of the tools
   catalogue — satisfy it for a file that has no catalogue entry? If so, how much
   of the "unlisted" class can the check actually see in a prose-heavy index?
3. Code spans resolve against three bases (mapped dir, index dir, `--root`). Can
   a span naming a same-named file elsewhere in the tree list an entry it does not
   describe?
4. The floor entry runs the guard whole-tree on the hook plane. Is that cost
   bounded on a large child, and does its exit-2 path (a malformed declaration in
   any file) block every commit in a child that never adopted the guard but
   happens to carry a line beginning `<!-- indexscan:maps`?
5. The docstring says `dir=` "must stay inside --root". Is that checked after
   symlink resolution, or only lexically?
6. `instruments/README.md` maps `match=*` with an exclude list. Does a new kind of
   file in `instruments/` (a lock file, a dot-file, a cache directory) show as
   unlisted, and is that the behaviour the declaration intends?
