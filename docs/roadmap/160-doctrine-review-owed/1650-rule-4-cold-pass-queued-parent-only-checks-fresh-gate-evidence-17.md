- [ ] ⏳ **Rule-4 cold pass queued: three doctrine corrections —
      `PROPAGATION.md` on what the parent runs alone (`115/440`) and on a
      called gate being only as fresh as the parent's working tree
      (`320/040`), and `EVIDENCE.md` §17's corrected no-guard premise
      (`115/410`).** Written by a worker of queue run 08cd3b95 (Opus 5.5,
      principal-opened, 2026-11-20 UTC), which queues this and does not take
      it or brief it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `docs/method/PROPAGATION.md` (§ *Enforcement
      propagates too*, three new paragraphs) and `docs/method/EVIDENCE.md`
      (§17): the commit that closes `115/440`, `320/040` and `115/410`, on
      `main`.
      *What to test hardest:* `115/440`'s note says the item's own premise was
      half wrong (signature checks run in children through `floor.yml`):
      re-check that against both workflows. The §17 text describes what
      `modelguard` and `secretguard` inspect: test it against the code. The
      `320/040` paragraph says no occurrence is recorded and names the fix it
      does not make: test whether the worktree default really narrows it.
      *Intent records:* the three items named above.
      No brief yet: a brief-writer this run did not start writes it. **Drain
      priority: not set by the principal; this run suggests low.**
