- ⏳ **Rule-4 cold pass queued — the 2026-09-18 floor-registry code: a scanner
      added, one removed, two blocking nets widened.** Self-authored by the
      run (its dispatched workers count as its authorship), queued at landing;
      the run neither takes nor spawns it. *Tier:* Fable, the principal-named
      review tier — checked at selection; a session that cannot honour the bar
      stops rather than takes. *Pass type:* code cold pass, per
      `method/REVIEW.md` rule 4.
      *Delta — scoped to paths:* `tools/conflictscan.py` +
      `tools/test_conflictscan.py` (new) · `tools/floor.py` (the
      `conflictscan` and `board` entries; the `plainscan` entry removed) ·
      `tools/secretscan.py` (URL spans, `HIGH_ENTROPY_RX`, `--staged`
      parsing) · `tools/leakscan.py` (`PLURAL_SUFFIX`) · `tools/board.py`
      (argv) · `tools/floorfleet.py` (the boundary row, the control strip) ·
      their test files · the two review records' `linkscan` allow-markers.
      Landed on `main`, 2026-09-18.
      *Intent record:*
      [`../../sessions/2026-09-18-0114-queue-run-hand-up-fixes.md`](../../sessions/2026-09-18-0114-queue-run-hand-up-fixes.md).
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-0918-registry-code-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-09-26 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned FAIL — 1 MAJOR · 2 MODERATE · 6 minor · 6
            note (RC4 re-rated minor at reconcile) →
            [`2026-09-25-0715-0918-registry-code-cold.md`](../../reviews/2026-09-25-0715-0918-registry-code-cold.md)
            (sibling folded in and deleted). RC1 (MAJOR): conflictscan --staged
            and leakscan --staged parse only a literal +++ b/ header, so under
            diff.noprefix or diff.mnemonicPrefix they attribute no lines, scan
            nothing and exit 0 — live-proven green on a staged conflict marker
            and a staged email; one-line fix with --src-prefix/--dst-prefix,
            pinned by a scratch-repo test; RC2 (MODERATE): the narrowed URL
            exclusion still admits a token in userinfo, which neither version
            weighed; RC15 (note) formed at reconcile. Findings are the
            principal's to decide (rule 3); nothing was applied.
