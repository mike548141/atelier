- ⏳ **Rule-4 review queued (tier: Fable; pass type: code + doctrine cold pass,
  the `ccmail` build).**
  *Delta:* `instruments/ccmail` (new) + `instruments/ccmail.test.js` (new, 25
  tests) + `instruments/man/ccmail.1` (new) + `instruments/README.md` (the
  layer table row and the `ccmail` section) +
  `docs/decisions/0006-instruments-in-atelier.md` (the 2026-09-09 addendum —
  the layer's first third-party credential) +
  `docs/roadmap/210-instruments-open-features/120-drive-binaries-have-the-same-gap-ccmail-just-closed.md`
  (the Drive finding filed beside it). **Delta widened 2026-09-09** per the
  landing-commit rule: `instruments/ccmail` again (the two-route resolver, the
  removal of the plaintext-file store) + `instruments/ccpdf/` (new: renderer,
  `setup`, `selftest`) + the 0006 amendment and third addendum + the
  `instruments/README.md` `ccpdf` section. Surfaces **outside this repo** and
  unreadable from it: the machine-local global-instructions entries routing
  sessions to `ccmail` and to the web-media method, and `~/.claude/ccmail.json`
  (identifiers only, no secret).
  *Intent record:*
  [`sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md`](../../sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md).
  *Self-authored*, so the review is not this session's to take. Two facts a
  taker needs at selection rather than after: the live Gmail round trip is now
  **proven end to end** against a real mailbox via the delegation route (the
  earlier "untestable" note is superseded), and the build's own **five** defects
  were found by reading and by an adversarial selftest, all in the layers
  between this code and something else, and none by using the tool.
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-ccmail-build-cold.md`) by a Mike-opened
      `claude-fable-5-1` session ("Please deliver all fable dependent work, and
      work that would be best delivered using fable") that authored none of the
      delta. Shape, disclosed per rule 4: reviewer-plus-orchestrator, both seats
      Fable — this session writes the refs-only brief and holds the
      `.deferred.md` sibling outside the worktree; a fresh Fable subagent it
      spawns forms every finding and severity. The sibling, the intent record
      and prior verdicts stay unopened by the reviewer until its phase-1
      findings are committed. Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-09-26 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 4 MODERATE ·
            6 minor · 2 note →
            [`2026-09-25-0715-ccmail-build-cold.md`](../../reviews/2026-09-25-0715-ccmail-build-cold.md)
            (sibling folded in and deleted). CC1 (MAJOR, rule 3): the
            delegation-first ruling omits two facts — keylessness does not
            remove the any-mailbox-in-the-domain blast radius, and
            stores-nothing is true of the tool but the route runs on the cloud
            CLI's plaintext refresh-token file, the class the same ruling
            banned; neither route's compromised-session exposure is stated
            anywhere; CC10 (MODERATE): at review time both routes were down, so
            no session could open an attachment; CC2 strengthened at reconcile
            (the 2026-09-09 test-run attachments are still in the live cache);
            CC13 (minor) formed at reconcile. Nothing from the mailbox enters
            the verdict. Findings are the principal's to decide (rule 3);
            nothing was applied.
