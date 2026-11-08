- [x] 🎯 **Rule-4 cold pass queued: the shared allow-marker grammar and ignore
      loader (`115/080` part 2).** The run authored this itself (its
      dispatched workers' output counts as the run's authorship). It was
      queued at landing, and the run neither takes it nor spawns a reviewer
      for it. *Tier:* Fable, the principal-named review tier, checked at
      selection. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/allowmarker.py` and
      `tools/test_allowmarker.py` (both new), and the marker and ignore-file
      code in `tools/{blockscan,conflictscan,datescan,leakscan,licenscan,`
      `linkscan,pathscan,pointerscan,reviewscan,secretscan,sizescan,`
      `spellscan,stampscan,wrapscan}.py`. It landed on `main` on 2026-10-03,
      in merge `5d087ec`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-03 0357 UTC for the review run** (wt:
      `atelier-review-430`, branch `review-430-1003`; brief
      `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`)
      by a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta and was
      not started or instructed by the authoring run. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree
      and outside the harness scratchpad; a fresh Fable subagent it spawns forms
      every finding and severity. Disclosed exposure: the authoring run told
      this session, over the cross-session channel, that the pointer existed
      and named its subject in a phrase; nothing else from it was read. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and
      exposure go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-10-03 and the cycle CLOSES on it (0 MAJOR);
            AM1–AM13 await Mike's ruling round.** The rule-4 Fable cold pass
            (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 4 minor · 4 note →
            [`2026-10-03-0357-shared-allow-marker-grammar-cold.md`](../../reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md)
            (sibling folded in). The extraction itself is clean: patterns
            byte-identical, loaders identical, a fixture drive across the
            scanners identical parent against HEAD, full suite exit 0. AM2
            (MODERATE; severity handed up): a malformed scoped marker backs off
            and exempts the whole line in all seven scoped scanners, both
            boundary guards included — LK1's unruled defect, now carried by one
            shared function to every child. AM1: reviewscan's deferral check
            matches a raw substring with no reason, a fifteenth marker site the
            extraction missed. AM3: an inline-code or prose mention of the
            syntax exempts the line in thirteen scanners. AM4: licenscan parses
            a scope and ignores it. AM5: the scoped grammar is documented on no
            user-facing surface. The staged-diff parser (RC1) was left for
            part 3. The review worktree lacked the delta at spawn (AM11);
            recovered and disclosed. Findings are the principal's to decide
            (rule 3); nothing was applied.
      💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered; an
        answer, not a ruling):** *"Strict, with a warning period"* — the offered option read: count broken markers across every repo first; a malformed marker then warns for a set period (about 30 days) while items are queued in the affected repos, and after that it exempts nothing (AM2). The rest of AM1–AM13 on the reviewer's counsel. Also answers `160/110`'s LK1.
      ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet worker, read
      by the orchestrator before landing), per his answer: AM2 — a malformed marker
      warns until 2026-12-09 and then exempts nothing; the count first found none
      live across 22 repos; AM1, AM3–AM13 as counselled (AM6 by the narrower
      option). Cold pass `160/1190`.
