# Deferred sibling — the shared exit and reporting contract (160/730)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-shared-report-contract-cold.md` are committed.** A
floor, never a fence: these questions were seeded by a brief-writer who read the
landing diff and commit body, so they carry that reading's framing. Reconcile
against them; do not let them narrow what you found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

No prior verdict names `report.py`. Verdicts that name the `115/080`
consolidation, for the reconcile:

- `docs/reviews/2026-09-25-0715-0918-registry-code-cold.md`
- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`
- `docs/reviews/2026-09-25-0715-single-sourced-file-walk-cold.md`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`

## The queue pointer's own lens hints

None. The pointer is refs-only, plus the orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diff)

1. `guarded_main` converts only the listed exception classes to exit 2. Any
   other exception escapes, Python prints a traceback and exits 1 — the
   "findings" code, not "broken". Was that already true before the delta, and
   either way, does the contract this module claims to own say a crash is exit 2?
2. `exit_code(blocking, warn=...)` returns 0 under `--warn` for any `blocking`.
   Is there a guard whose call site now routes an exit-2 condition through
   `exit_code` instead of `broken`, so `--warn` swallows it?
3. The commit body says the byte-identity check covered "four synthetic fixture
   trees plus error cases". Were the cases chosen from what the old scanners
   printed, or from what the helpers were written to print?
4. `resolve_targets` and `refuse_missing_paths` treat a broken symlink as
   missing (exit 2) and a symlink out of the root as present. Is either a change
   from any guard's old behaviour?
5. The module docstring says a scanner whose line "genuinely differs" keeps its
   own spelling. Who decides "genuinely", and is there a test that fails if a
   later edit routes one of those through a shared helper?
