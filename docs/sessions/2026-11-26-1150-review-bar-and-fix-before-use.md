# 2026-11-26 11:50 UTC — the review bar, and when a finding is fixed before use (`460/020`)

**Session:** `4ccec293` (messaging name `atelier-56`), Claude Opus 5.5, principal-opened by
`/atelier:work run` with `460/020` as its brief. Worktree `atelier-460-020`. One other live
session (`a2aeebc8`, on the primary checkout, `450/010` step D); this one stayed in its worktree.
No Fable model and no review-tier subagent ran.

## What was asked

His brief, verbatim: *"Build board 460/020: write the bar into the review rules, including when
a finding is fixed before use and when fixes earn a re-check, from my words quoted on the item.
Doctrine, so its own Fable review is queued for my approval, not run."*

## What was done

- **Claim** `b459dd7e`.
- **`REVIEW.md`**: § *Whether work earns a review at all* gains the bar (three questions,
  answered in the intent record; no answer to the third, no pass), a never-on-its-own list,
  rule 3 as who rules rather than whether, one open pass per subject, and his order outranking
  the test. A new section, *When a finding is fixed before use, and when fixes earn a re-check*:
  an issue (failure shown happening) is fixed before next use; a risk goes to the board at low
  priority until evidenced, except a first occurrence that is itself irreversible and a silent
  failure (the repo's reading, marked so); a re-check is owed only after a pass with a MAJOR,
  and the chain stops at the first pass with none. Rules 3 and 4, lifecycle step 4, the stop
  paragraph and the review line point at both.
- **Copies:** `ECONOMICS.md`, `skills/review/brief.md`, `CONCURRENCY.md`'s landing step, the
  dispatch skeleton (a worker answers the three questions in its report).
- **Board:** `460/020` closed with its own review grounds; `460/030` and `460/040` unblocked,
  with the design fact the gate needs (answers live in the intent record, since pointers stay
  refs only). Pointer `160/1880` queued in the landing commit, a pass of its own as he ordered,
  not folded into the open `160/1830` on the same files.

## Found

- **His "Haven't I ruled on this in the past?":** partly. The 2026-07-13 stop (a cycle closes at
  the first pass with no MAJOR; a MAJOR count not falling means stop and ask him) was written for
  applying findings to doctrine only. The drain code's chain never met it: under it, the chain
  closes at `RK` (0 MAJOR, 2026-11-25); `DV`, `PK` and `DP` ran after, all 0 MAJOR, and
  `160/1870` is queued.
- **The bar applied to this change** passes it: no test reads what doctrine means, and a bar too
  loose fails silent.

## Left open, for the principal

- Two readings beyond his words, asked at the close: carrying the 2026-07-13 stop from doctrine
  to code fixes, and fixing the two kinds of risk (irreversible first occurrence, silent failure)
  before use without evidence.
- `160/1880`'s Fable pass: his to approve.
