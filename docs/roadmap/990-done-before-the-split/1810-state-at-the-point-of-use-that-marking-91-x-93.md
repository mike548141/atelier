- [x] (2026-08-03: enacted — the two preamble clauses landed; this entry is the
      grounding) **State, at the point of use, that marking `[x]` and harvesting
      to ROADMAP-DONE are one commit — not two.** The ROADMAP preamble defines
      the `[x]` state but says nothing about *when* the harvest happens, and the
      cold-content gate fires the moment an `[x]` lands on the hot path. So
      marking three items done in one commit and harvesting in the next leaves a
      window in which the **pushed** floor is red — which is exactly what
      happened on 2026-07-26 (`d847866` red, `0485540` green). Local scans were
      green throughout, because the harvest was already done on disk before the
      first push was checked; only the pushed floor saw the window.
      **This is the same shape as a ruling already made**, which is what makes
      it a candidate rather than a one-off: AWA2 put the `⏳` pointer *in the
      commit that lands the work* so no window exists where landed doctrine sits
      unpointed. Same argument, different marker — an `[x]` and its harvest
      belong in one commit so no window exists where a completed item sits
      stranded on the hot path. Both are instances of a more general rule worth
      naming if a third case appears: **a state change and the bookkeeping the
      floor demands of it ship together.**
      **A third instance arrived the same day, from the opposite direction — and
      it names the mechanism.** A post-outage recovery sweep found one item
      still `[~]` **claimed** whose work had shipped hours earlier (`b89a306`).
      Of the three states that is the worst to leave behind: a later session
      reads `[~]` as *a live session owns this* and skips it, so delivered work
      sits looking permanently in progress. The reason it was missed is
      structural, not carelessness — **every other item that run was claimed
      with a worktree, and merging the worktree forced a return to the roadmap.
      This one was claimed `wt: none — inline on main`, so nothing ever forced
      the return.** The forcing function was the worktree, and the item that
      skipped the worktree skipped the closing step with it. So the rule wants a
      second clause aimed at exactly that case: **an inline claim is closed in
      the commit that lands its work**, because there is no merge step later to
      remember it. Same family as the `[x]`/harvest pairing above — a state
      change and its bookkeeping ship together — and the same reason it keeps
      recurring: the bookkeeping is only reliable when something *makes* you do
      it. (Moved from ROADMAP.md 2026-08-03.)
