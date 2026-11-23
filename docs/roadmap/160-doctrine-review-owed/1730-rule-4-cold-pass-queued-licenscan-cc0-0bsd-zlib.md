- [ ] ⏳ **Rule-4 cold pass queued: `licenscan` reads CC0-1.0, tells 0BSD
      from ISC, and reads Zlib (`320/890`).** A guard's recognition table
      changed, and a wrong signature is a silent misread (a licence named
      as another), so the change earns its own pass. The authoring session
      (c7a1e36e, Opus 5.5, a principal-opened queue run, 2026-11-23 UTC,
      which wrote the change inline) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/licenscan.py`,
      `tools/test_licenscan.py`: the commit that closes `320/890`, on
      `main`.
      *Intent record:*
      [`../320-child-filed-findings-via-pointing-up/890-licenscan-cannot-read-a-cc0-licence.md`](../320-child-filed-findings-via-pointing-up/890-licenscan-cannot-read-a-cc0-licence.md).
      *What to test hardest:* signature order and overlap across every
      entry, not only the three touched (a body that carries two families'
      phrases, a licence quoted inside another's text); whether a
      single-phrase CC0 signature can fire on a file that merely mentions
      CC0; that a 0BSD body can no longer pass an `--expect ISC`.
      *Approval:* none yet; owed to the principal before the pass runs.
      💬 **Answered 2026-11-23 ~12:35 UTC (session c7a1e36e, AskUserQuestion), his pick:** *"Next drain (Recommended)"*, for this pass and
      the widened `160/1710` and `160/1680`: they wait for his next weekly
      drain.
