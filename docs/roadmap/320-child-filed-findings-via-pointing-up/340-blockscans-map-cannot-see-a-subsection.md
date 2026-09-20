- [ ] 🔎 **`blockscan` cannot see a change to a mapped section's
      SUBSECTIONS, and the session that built it walked straight into the
      gap** — found 2026-09-20 in the same sitting `320/300` landed, by
      running the new check against that sitting's own doctrine commits.
      **The mechanism.** The map ties a block bullet to a heading, and the
      section is extracted **non-recursively** — it stops at the next
      heading of *any* level. That choice is right where it was reasoned:
      `00-APEX.md`'s `## Honesty is absolute` and its own
      `### The principal's authority…` subsection answer to *different*
      bullets, and a recursive slice would make one edit fire both.
      **The cost, measured on this sitting.** The `doctrine-problems` bullet
      maps to `PROPAGATION.md` § *Pointing up*. This session rewrote
      § *The route* **rule 2** and two bullets of § *Report without harming
      the parent* — both `###` subsections of that very section, both
      doctrine changes the block's own bullet plausibly summarises — and
      `blockscan --against` reported **clean**. The check fires correctly
      when the mapped slice itself changes (verified with a probe edit); it
      simply never sees a subsection.
      **Why it is filed rather than fixed in passing:** the fix is a real
      design choice, not a typo. Candidates — map subsections explicitly as
      their own sources (most precise, most map to maintain) · give an entry
      an opt-in `recursive: true` where the bullet really does summarise the
      whole tree (cheap, and the apex case shows why it cannot be the
      default) · have `--check` report which of a doc's headings are
      **unmapped**, so the blind spot is visible even where nobody widens
      the map. The third is the one that stops this being rediscovered.
      **The class this belongs to:** `370/020` — a guard that cannot see
      what it guards. It reported clean over exactly the change it exists to
      catch, and only a deliberate probe showed the difference.
