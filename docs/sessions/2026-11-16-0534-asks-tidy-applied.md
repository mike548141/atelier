# 2026-11-16 · 0534 UTC — Asks de-dupe tidy-ups applied

**Session:** `0f2ea343` (as `cclive` lists it), Claude Opus 5.5, headless, started by an estate
health sweep (orchestrator session `58027096`). **Worktree:** a detached worktree at
`origin/main`. No Fable used, no review run.

## What was done

The principal approved the tidy-ups of his de-duplicated asks on 2026-11-16, on the condition
that each one is rated high confidence or better, can be reversed, and says at the item where the
original is and how to revert it. Every row here was rated high by a per-row verification on
2026-11-14. Before writing, each cited line was opened and still said what the evidence quoted.

Each applied row adds **one line** under its item, starting `🔀 Tidied 2026-11-16`, and is its own
commit: no existing line, checkbox, flag or item state was changed, and the generated board index
is unchanged (it reads only an item's first line). Twelve commits, 77 lines added, 0 removed.

| Row | Item | What was added | Commit | Revert |
|---|---|---|---|---|
| C0333 | [`020/120`](../roadmap/020-policy-as-code-programme-five-tracks-mik/120-d3-signscan-cannot-fail-ci.md) | a pointer to its home, `170/010` (the same warn-to-block decision) | `2e95a91b` | `git revert 2e95a91b` |
| C0495 | [`020/010`](../roadmap/020-policy-as-code-programme-five-tracks-mik/010-the-five-red-floors-themselves-are-now-open-wo.md) | not an ask of Mike: each child repo's own call (lines 2-4) | `586a598f` | `git revert 586a598f` |
| C0497 | [`020/070`](../roadmap/020-policy-as-code-programme-five-tracks-mik/070-c1b-migrate-the-remainder-then-delete-the-lega.md) | not an ask of Mike: date settled (lines 12-15); Phase 2 is agent build work | `423365b7` | `git revert 423365b7` |
| C0499 | [`020/220`](../roadmap/020-policy-as-code-programme-five-tracks-mik/220-a-the-census-nobody-has-run-which-rules-have-a.md) | not an ask of Mike: the rule census is agent work | `74527eda` | `git revert 74527eda` |
| C0500 | [`020/230`](../roadmap/020-policy-as-code-programme-five-tracks-mik/230-b-the-half-with-no-owner-doctrine-that-reaches.md) | not an ask of Mike: a wording obligation, agent work | `a6a657d9` | `git revert a6a657d9` |
| C0544 | [`220/010`](../roadmap/220-observability-of-the-collaboration-itsel/010-doctrine-candidate-the-mechanical-instruments.md) | not an ask of Mike: a doctrine candidate to write up | `07fda494` | `git revert 07fda494` |
| C0545 | [`220/020`](../roadmap/220-observability-of-the-collaboration-itsel/020-doctrine-candidate-evidence-hygiene-a-scanner.md) | not an ask of Mike: a doctrine candidate to write up | `dcb9ead9` | `git revert dcb9ead9` |
| C0546 | [`270/050`](../roadmap/270-open-questions/050-one-task-per-session-does-the-doctrine-say-what-was-directed.md) | not an ask of Mike: "nothing is decided here" (line 28); the looking is agent work | `a9f12ca6` | `git revert a9f12ca6` |
| C0547 | [`300/030`](../roadmap/300-posture-recover-cheaply-mike-commissioned/030-what-would-this-estate-actually-notice.md) | not an ask of Mike: the census is agent work, run outside atelier (lines 10-14) | `9a9a7a21` | `git revert 9a9a7a21` |
| C0553 | [`330/010`](../roadmap/330-sha-2-or-better-for-every-hash-mike-commissioned/010-name-the-rule-and-find-where-the-house-already-br.md) | not an ask of Mike: homing the rule and the sweep are agent work | `948bc387` | `git revert 948bc387` |
| C0554 | [`340/010`](../roadmap/340-long-running-operations-need-a-way-back-mike-comm/010-the-rule-and-where-it-attaches.md) | not an ask of Mike: drafting the rule is agent work | `dc6be68d` | `git revert dc6be68d` |
| C0557 | [`430/010`](../roadmap/430-review-quality-is-never-traded-for-budget-mike-commissioned/010-reinforce-the-rule-in-doctrine-and-guard-it-in-code.md) | not an ask of Mike: the owed wording and guards are agent work | `2c931341` | `git revert 2c931341` |

To revert every row at once: `git revert 2e95a91b^..2c931341`.

## Held

| Row | Reason |
|---|---|
| C0308 | No copy of the ask is in this repo: it lives in another repo's review brief, and atelier is only cited as evidence. Nothing to apply here. |
| C0311 | No copy of the ask is in this repo: it lives in another repo's session record, and atelier is only cited as evidence. Nothing to apply here. |

## Left owed

Nothing from this run. The 🎯 flags on the eleven not-his items are left as they were (the
approval was to add lines, not change flags); a later session may lift them on the principal's
word.
