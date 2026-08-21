# Cold review — doctrine "Pointing up: the child-to-parent route, and the two canonical-block fixes"

**Status: BRIEF ONLY — the review has NOT run.** Written 2026-08-21 by a
Mike-opened `claude-fable-5` session pointed at "any reviews and fable
dependent work"; it authored neither the delta (an atelier session,
2026-08-18) nor this section's items. Per Mike's rule for such sessions
(2026-08-15), *the session that writes a brief does not run its review* — so
this waits for a **further** cold Fable session that neither the delta's
author nor this brief's writer started or instructed; tier checked at
selection (REVIEW.md rule 4). The reviewer appends its verdict below the
`---` and states its own spawn provenance there.

**Brief-writer's exposure, disclosed:** this writer read the delta commit's
message and the seven `method/` diffs (as pin-bump catch-up work for two
child repos, earlier the same session, before taking this item) and applied
the corrected concurrency wording in those two children's floor blocks. The
**intent records were left unopened** — the section README (which carries
Mike's 2026-08-18 ruling), `docs/sessions/2026-08-18-0746-…`, and the
`SESSIONS.md` entry — so this brief is written from the delta and the queue
pointer only, and carries no account of the author session's reasoning
beyond what the delta text itself asserts.

- **Subject**: the delta of `f9eda42` (2026-08-18), whole — **doctrine by
  function** (REVIEW.md rule 3), so rules 3 and 4 bind:
  - `docs/method/PROPAGATION.md` — new § *Pointing up — when a child earns a
    house rule* (~150 lines: the check-the-parent-first rule, the
    whose-rule-is-it test, the four-step route, the closing-the-loop rule,
    § The instance), and the reworked concurrency bullet of § *The standard
    child doctrine block*.
  - `docs/build/templates/CLAUDE.md` — the same bullet, which the scaffold
    stamps into every new child.
  - `docs/method/CONCURRENCY.md` — § *The trigger* gains the whole-index
    clause and a *Bearing* recording the 2026-08-18 incident.
  - `docs/method/GUARDS.md` — § *A rule with no home is not a rule* gains
    the cross-repo paragraph routing house-shaped rules to § Pointing up.
  - This section's items (`010`–`050` as landed) and the CHANGELOG entry.
- **Type**: doctrine cold pass — a rule that governs every future child
  session's behaviour at the child/parent seam, stamped into the fleet at
  pin bumps.
- **Scope** (point, don't paste):
  - The four delta surfaces above, at HEAD — including whether the four
    files tell one consistent story of where the index rule lives.
  - The queue pointer
    ([`050-…`](../roadmap/310-pointing-up-the-child-to-parent-route/050-rule-4-cold-pass-queued-pointing-up.md))
    and the sibling items `010`–`040` as the delta's own account of itself.
  - Intent record: the section
    [`README.md`](../roadmap/310-pointing-up-the-child-to-parent-route/README.md)
    (Mike's commission and his 2026-08-18 ruling on the child-side
    allowance) and the session record
    [`2026-08-18-0746-…`](../sessions/2026-08-18-0746-pointing-up-the-child-to-parent-route.md)
    — under the reviewer's own deferral discipline.
  - Neighbours it must not contradict: PROPAGATION § *The layer-override
    rule*, § *Who is a child*, § *One statement, stamped copies*, § *When a
    rule keeps breaking*; CONCURRENCY § *Claiming work* and § *Stay in your
    lane* (the route asserts that filing a finding in the parent's board
    *is* the lane — test that against the rule as written); GUARDS' three
    axes and the fourth requirement; the public-repo constraint (this repo
    is public; the instance describes a private child).
- **Load-bearing claims the record rests on** (extracted from the delta
  text, not evaluated — the reviewer decides which are load-bearing and
  adds its own):
  1. The house had no gap: `git diff --cached` at CONCURRENCY § The trigger
     always covered unstaged paths, and the child's second rule sits
     verbatim at § Claiming work.
  2. The 2026-08-18 incident is as described: a session staged two paths
     explicitly, committed, and destroyed a sibling's session-log entry
     that predated its arrival in the shared index.
  3. The old block phrase ("read the staged hunk headers") and its pointer
     (§ The channel) were both defective, and both are fixed in the
     canonical block and the template by this commit.
  4. Ten children carry the defective block and each clears it at its next
     pin bump (item `030`'s count).
  5. The whose-rule test — *would this rule be true in a repo that shares
     none of this repo's stack?* — partitions child rules from house rules,
     with the learned-on-a-stack seam stated.
  6. A pending-upstream line is a **narrowing** under § The layer-override
     rule, and being dated, addressed and self-removing is what separates
     it from a second original.
  7. Mike ruled the child-side allowance on 2026-08-18, in preference to
     leaving the child unprotected in the window.
  8. GUARDS § A rule with no home and this route are complementary, not in
     tension: evidence stays in the child's record, the rule travels to
     where it governs.
  9. Nothing enumerates upward debt; the section is honestly rung 1 until
     the queued instrument (item `020`) exists.
  10. The instance carries the class and never the private child's
      specifics, as the public-repo constraint requires.
- **Grounding — what the reviewer can run or read**:
  - Re-run claim 1 against HEAD: read CONCURRENCY § The trigger and
    § Claiming work and check the delta's account of them is byte-honest.
  - Diff the canonical block against `docs/build/templates/CLAUDE.md` —
    the two stamped statements of the same bullet must match.
  - Re-derive claim 4's count from the fleet enumeration the repo ships
    (`tools/floorfleet.py`, read-only) or the pins list — and note that
    child bumps after 2026-08-18 (two landed 2026-08-21) change the live
    count without changing the item's truth at its date.
  - `tools/board.py`-rendered index lines for this section's items;
    `pointerscan` behaviour on the `050` pointer.
  - The public commit log: does the instance's detail (two staged paths, a
    sibling's session-log entry, the date) let a public reader identify the
    private child? The class/specifics line is testable, not assumable.
- **Non-goals**: re-ruling Mike's 2026-08-18 allowance (the review may test
  the *grounds* the text records for it); designing the upward-debt
  enumerator (item `020`, queued); repairing the child repo's own records
  (its lane); the 2026-08-17 ruling round (separately reviewed and queued).
- **Prior verdicts to open only after your findings are durably written**
  (rule 2): none address this delta. Nearest relatives, pointed at not
  summarised: `2026-08-17-1000-channel-doctrine-cold.md` (the neighbouring
  CONCURRENCY §) and `2026-08-17-1321-bs1-wording-cold.md` (the claim
  mechanics the reworked bullet sits beside).
- **Deferred material**: the brief-writer's own attack angles are in the
  sibling `2026-08-21-0820-pointing-up-cold.deferred.md`. Open it as a
  deliberate second act, after your own findings are written; then fold it
  below the verdict and delete it (REVIEW.md rule 1).

---
