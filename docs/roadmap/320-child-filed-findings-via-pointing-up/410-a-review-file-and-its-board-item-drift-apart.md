- [ ] 🔎 **A review file's follow-up list and the board item that points at it
      drift apart — and one time in five, measured, they disagree about the
      live state** `[M][tooling]` — filed by a private child 2026-09-26 via
      § *Pointing up*, on its principal's instruction to file. A tooling
      proposal for `reviewscan`, not a doctrine defect: the house already owns
      the close-out rule (`REVIEW.md` step 5); what it lacks is the half a
      machine can check.

      ## The measurement (the child's, class-only)

      A read-only sweep compared every review file in the child against the
      board item that cites it: **63 (review file, board item) pairs, 12
      disagree about the live state — about one in five — 46 consistent, 5
      pointer-only.** Five of the twelve and both edge cases below were
      re-verified first-hand against the code before recording.

      - **Ten of the twelve run one way: the REVIEW FILE goes stale after the
        fix lands.** Two sub-shapes — a frozen `Status:` header ("nothing has
        been built") that was true on verdict day; and a "follow-ups owed"
        list whose every item has since landed.
      - ⚠️ **CORRECTED the same day by the filer — this bullet is FALSE as
        filed; kept visible rather than deleted.** A re-measure against the
        child's board found the per-item record *did* restate the fix, in its
        own words, from the day it landed. The stale text was in a review file
        and in a section *narrative* file — a secondary log — not in the
        authoritative item. So the "only record" claim does not hold; what
        holds is the weaker shape: stale summaries can sit beside a correct
        item, and a reader who stops at the summary is misled. The original
        wording follows:
        ~~**The drift can be one-sided.** In one case the only record of a
        fixed HIGH-severity security finding is a stale review file that still
        says *owed* — no board item ever restated it. The record says the
        opposite of the artefact and nothing contradicts it.~~
        *The 12-of-63 count is being re-measured in the child as part of the
        record corrections; if it moves, the filer appends the new figure
        here rather than editing the one above.*
      - 🚩 **Two records can agree and both be wrong.** A review file and a
        section narrative both said a seam was "still owed" while the module
        existed and a later verdict had settled it. So *cross-check the other
        record* is not a remedy — only the artefact is.
      - **69 of 126 review files have no board item citing them** — 68 by
        design (cited from archive/spec/session records), and **one only
        because its citation wraps a filename across a line break**, which no
        basename grep can see.

      ## The class

      A record that **restates** another record's state has no mechanism to
      learn it was superseded. The child found five instances of that shape in
      one run before it ran the sweep. It is the house's class, not the
      child's: any repo with review files and a board has it.

      ## The proposal — recommend, not decide (atelier's to consider)

      Only the half a machine can see, as an extension of `reviewscan`:

      1. **One home for live state.** Every review file carries a `board:`
         back-pointer to its item file — or `board: none — <grounds>` — in a
         fixed position; `reviewscan` reds a review file without one. One
         regex. It also kills the wrapped-citation blind spot, because the
         pointer lives in the review file, not in someone else's prose.
      2. **A `Status:` line carries an ISO date.** Mechanical, and it turns
         *"nothing has been built"* into *"nothing had been built on
         2026-07-19"*, which stays true forever.
      3. **Do NOT add the inverse** (a board item stating which revision of the
         review it read). That is a second restatement and rots the same way.
      4. The *"follow-ups all landed"* sub-shape has no mechanical answer —
         only the code knows. Its remedy is `REVIEW.md` step 5's close-out plus
         the back-pointer, so a reader who finds an owed list knows where the
         live ledger is.

      **Cost, as the child estimates it (unmeasured):** ~40 lines plus tests in
      `tools/reviewscan.py`, with a boundary date so existing files are not
      red on day one (the same shape as its existing `BOUNDARY`). Children
      would pick it up by call, with no local tool.

      **What this does not claim.** That the one-in-five figure holds
      estate-wide — it is one child's measurement. That a back-pointer
      prevents staleness — it doesn't; it tells a reader where to look.
      Remediation is the parent's; the reporting session stops here.

      *review: the child's proposal was itself the output of a cold review
      pass in the child; whether atelier's change needs one is atelier's
      call.*
