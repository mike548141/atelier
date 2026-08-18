- [ ] 🎯 **Queue the block-trim finding in `cbom` — AFTER this cycle's
      review closes** `[S][docs]` — Mike's sequencing, 2026-08-18, in his own
      words: *"once thats ready (incl reviews etc) queue it in cbom repo so
      that a cbom session can revert the changes cbom has made to
      claude.md."* Blocked on `050`; do not file it early.
      **Why it is queued there and not done from here.** Work lands in the repo
      it changes (`PROPAGATION.md` § *Who is a child*, `CONCURRENCY.md` §
      *Stay in your lane*). Mike was offered the faster route — this session
      reverting `cbom/CLAUDE.md` directly as a recorded exception — and ruled
      for the queue. A `cbom` session does the edit.
      **What the finding must carry**, so the taker is not re-deriving it:
      - **Nothing was owed upstream.** Both authored rules are already in
        atelier's `CONCURRENCY.md` — the claiming rule verbatim in § *Claiming
        work*, the index rule's substance in § *The trigger*. Verified
        2026-08-18 against the parent's own text.
      - **The cause was reading its own block instead of the parent**, whose
        compression (*read the staged hunk headers*) reads as covering only
        what you staged. The parent's rule runs `git diff --cached` over the
        whole index and always covered that case. Corrected at the source this
        commit.
      - **The act owed** is to cut the locally-authored rule text out of the
        floor block, restore the bullet to the corrected canonical wording, and
        take the pin bump that delivers it — one act, not two.
      - **The incident stays** in `cbom`'s session record. It is evidence, and
        evidence belongs where it happened (`PROPAGATION.md` § *Pointing up*,
        step 4).
      **One thing the taker must check rather than assume:** whether anything
      else in that block is locally authored rather than stamped. This finding
      is scoped to the rules identified above; a wider trim is a wider judgement
      and is not pre-approved here.
