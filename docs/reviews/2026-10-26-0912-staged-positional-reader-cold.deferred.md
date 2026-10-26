# Sibling to the staged-positional reader cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer subagent of session `5070f22b`
named in the brief's provenance; it forms no finding and writes no severity. Fold this file in
below the reconcile and delete it at phase 2.

## Intent record

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md`
  — read in full by the brief-writer. It carries no quoted words of the principal. Lines 2–41
  are the finding as filed: the old prefix match, a scratch-clone measurement, a statement
  that the floor's hook plane was not affected, the cost (a run of commits citing a
  `.`-scoped staged scan as green), and a proposed fix with two parts. It also names a
  neighbouring finding id from a 2026-10-17 staged-diff pass (a prior verdict, not opened).
  Lines 42–54 are the author's closing account: one shared reader, what it normalises and
  refuses, that the proposed refusal of "a positional that empties a non-empty set" was
  deliberately not built and why, a scratch-clone before/after probe, a count of new tests and
  a count of the full suite green. Read it now as the author's claims to reconcile against.
- The message body of `692c04a` — not read by the brief-writer.

## Re-run results held back from the brief

Run once each by the brief-writer, 2026-10-26, from its worktree root at `2f6dbf6`, on the
principal's machine, in the foreground:

- `coldsweep --commit 692c04a`: exit 0, closing line present, no barred file in the diff.
- The four delta test files: each exit 0 — `test_conflictscan` 174 tests, `test_leakscan`
  56, `test_report` 71, `test_secretscan` 219, all OK (each also printed its scanner's
  selftest OK).
- Full suite under `nice -n 10`: exit 0, 2032 tests OK, 664 s on a heavily loaded machine
  (load average rose from about 7 to about 29 during the run; other sessions were live).
- `git log --oneline 692c04a..HEAD` over the eight delta paths: two commits, `b5a2c53` and
  `34dc0f0`, both on `tools/leakscan.py`.
- Floor at HEAD: hook plane exit 0; ci plane exit 0 (advisory warn-only lines only). Both ran
  with this brief untracked in the tree.

## Probe results held back from the brief

- **Old against new, one scanner.** `secretscan` extracted at `692c04a^` and at `692c04a`,
  one staged live-shaped key at `docs/sub/a.txt`, ten positional spellings. Six spellings
  changed from exit 0 (old) to exit 1 (new): the empty string, `.`, `./docs`,
  `docs/sub/..`, `docs/./sub`, `./docs/sub/a.txt`. One changed from exit 0 to exit 2: `..`.
  Three were unchanged: `docs` and the exact file path (1 → 1), and an out-of-scope
  directory (0 → 0). The other two guards were not probed this way.
- **Child probe, by count.** Of 29 git repos beside the principal's main atelier checkout
  (atelier excluded), 19 carry a committed floor config; 2 declare a scope for one of the
  three guards (10 scope paths in all, fleet `scope` plus `local` checks that run
  `--staged`); 0 of those paths change spelling under `normpath` once rendered by the
  floor's staged-mode render. 1 repo's committed hooks or workflows mention `--staged`
  (a grep hit only; the file was not opened, so whether it calls a guard directly with a
  positional is unknown). `floorfleet --json` over the same directory listed 22 children.

## Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. The reader normalises with `os.path.normpath`, which follows the host platform. On a
   platform whose separator is not `/`, a nested scope such as `docs/sub` normalises to a
   backslash spelling, the `/` prefix test matches no git path, and the set silently empties
   — the class the delta exists to close, reintroduced for nested scopes where the old match
   worked. Confirmed only lexically (`ntpath.normpath('docs/sub')` gives `docs\\sub`); whether
   any supported runner or adopter runs on such a platform is open.
2. The empty-string positional, and any spelling that normalises to `.`, now means "no
   restriction". That widens cover, which is the safe direction, but it is a change a caller
   passing an empty scope by accident would not see. The floor drops `.` and `""` before
   render, so the hook plane never reaches this; a hand or bespoke caller can.
3. `normpath` is lexical: `a/link/../b` collapses to `a/b` whatever `link` is. The floor
   rejects `..` in a scope path before render, but a hand caller is not so guarded. Whether a
   collapse can point a scope at a different subtree than the caller meant is open.
4. The later commit `b5a2c53` calls `scope_staged` twice more in `leakscan` and discards the
   returned code. The first call already refused on the same positionals, so the discarded
   codes may be unreachable — or may not be, if the inputs differ. Out of delta, but the
   reader's contract is now relied on by callers its own tests do not exercise.
5. The author declined the item's proposed refusal of a positional that empties a non-empty
   set, on the ground that the hook plane legitimately filters to nothing. That ground holds
   for a declared scope; it does not obviously hold for a hand invocation, where an empty
   result after a typo (`dcos`) still prints clean. Whether the guards can tell the two
   callers apart, and whether they should, is the residual silent-empty surface.
6. By grep, `.githooks/pre-commit` delegates to `floor.py` and no workflow passes
   `--staged`, so in atelier every automated positional passes two normalisers in series:
   the floor's render (`strip("/")`, dropping `.` and `""`) and then the reader's
   `normpath`. Two homes for one spelling rule is a V4 question, and the floor's comment on
   staged positionals (it names "a bare `.`" as matching nothing) may now be stale.
7. The three new test classes are near-identical copies across three files. Whether a
   mutation of the shared reader (for example, restoring the old prefix match) reds all of
   them, and whether the leakscan copy's environment patch keeps it portable to CI, is
   unprobed.

## Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- The intent record names a 2026-10-17 staged-diff pass. Its file is under `docs/reviews/`;
  the brief-writer did not search for or open it.
