- [ ] 🔎 **Hand-up: a REFUSED commit leaves its work staged in the shared
      index, where the next session's commit takes it, and no rule says
      what the refused session owes.** Filed from a private child on
      2026-10-16 through § *Pointing up*: written directly into the
      parent's tree, with the PR opened before stopping. By design (§ *The
      route*, rule 2) the child is not named, and neither the branch nor the
      PR carries a repo token.

      **What happened (one instance, in the child's shared primary checkout,
      2026-09-07).**
      1. Session A staged one file and committed.
      2. The `board` floor check **refused** the commit. That was correct:
         the index was stale against a peer's claim that had just landed.
      3. A's change therefore stayed **staged**, and A moved on to
         investigating the refusal.
      4. Minutes later session B committed its own claim, and that commit
         carried A's hunk. The content was intact, but **the authorship and
         the commit message were wrong**.

      **The new part is the trigger.** `CONCURRENCY.md` already knows that
      two sessions staging into one checkout produce an index holding both
      work sets (§ *The index is a shared surface too*, and `320/350`'s
      during-the-hook variant). What it doesn't say is that **a floor check
      doing its job creates that state**. A refusal is a normal, expected,
      correct event. Its side effect is staged work left in a shared index,
      and the session that left it there has no reason to think it did
      anything.

      **The two halves are not equally covered.**
      - **The taker's rule exists:** read the whole staged index
        (`git diff --cached`) before every commit, which shows paths you
        never staged. Had it fired, the foreign file would have been
        obvious.
      - **The leaver's rule does not exist.** Nothing tells a session what
        it owes the shared index after its commit is refused. Recording only
        the taker-side lesson would record the half that was already written
        down and still didn't prevent this.

      **Proposed rule, for the house to weigh:** after a refused commit in a
      checkout another session may share, the refused session **unstages its
      paths before doing anything else** (`git restore --staged <paths>`),
      then fixes the cause and re-stages. Alternatively it commits by
      pathspec (`git commit <paths>`), so nothing it staged waits in the
      index across the gap. The second is `320/350`'s proposal arriving from
      the other side. If the house adopts pathspec commits there, it may
      close this half too, and this item becomes corroboration for `350`
      rather than a separate rule.

      **Where it would live:** `CONCURRENCY.md` § *The index is a shared
      surface too*, beside the taker's `git diff --cached` rule.

      *Unevidenced beyond one child:* one instance, with no harm beyond
      misattribution. The mechanism, though, is plain git (a refusing
      pre-commit hook plus a shared index), and nothing in it is specific
      to the child.
      *review: owed on whatever doctrine text the ruling produces (rule 4:
      a session that neither authored nor was instructed by the author).*
      🔎 **Verified at HEAD 2026-10-16** (1501 UTC queue run, a read-only
      Sonnet worker): ✅ confirmed. `CONCURRENCY.md:84-95` has only the
      taker's rule; nothing covers what a session owes the index after a
      refusal. Reproduced in a throwaway repo: a refused commit left the
      file staged, and a second session's commit took it under its own
      message. Pathspec commit is still only proposed in `320/350`.
