# Sibling to the close-covers-subagents cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record:
  `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/420-the-close-declaration-does-not-cover-subagents.md`
  — **not opened by the brief-writer**.
- The identifiers widening (AW6, by the same session): commissioning item
  `docs/roadmap/210-instruments-open-features/280-ccclose-prints-the-identifiers-block.md`
  — **not opened**. The second widening, `bdb1aba`, closes
  `docs/roadmap/210-instruments-open-features/300-plain-ccclose-ends-with-the-identifiers-block.md`
  (filed and claimed in `0631204`, whose subject marks it as the principal's ask) —
  **not opened**. Follow-on item
  `docs/roadmap/210-instruments-open-features/290-ccclose-identifiers-over-credits-overlapping-sessions.md`,
  in flight while this brief was written — **not opened**; its commits are outside
  this delta and carry their own queued pass.
- The landing commits' message bodies — **not read by the brief-writer**; read them now
  as the author's account.

## Prior verdicts on these surfaces (named by filename, not opened, not exhaustive)

- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` — the earlier cold pass
  on ccclose (pointer 160/870). The brief-writer read its brief section and its folded
  sibling for shape, and saw its heading outline, which lists its findings' titles; it
  did not read their bodies. Reconcile this pass's findings against it: a defect it
  found that check 12 or the identifiers form repeats, or one this delta fixed.
- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md` — the transcript module
  ccclose reuses (named by filename only).

## Overlap with sibling passes

- 160/900 holds the doctrine text the identifiers form implements (`1adf398`,
  `46320f8`, `6810b64`, and `140a190` on `CONCURRENCY.md`). Expect both verdicts to
  touch the field list; this pass owns the code's fidelity, 160/900 the text.
- The authoring run's close commits (`ea073c8`, `3d5fe35`; subjects only read) filed
  210/290 against the identifiers form, so a known defect in it was open before this
  brief was written. Its subject is in that item's filename, listed above.

## The pointer's own lens hints

None. The pointer is refs-only; it names the AW6 widening as part of the delta.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `tildePath` tests `p.startsWith(h + path.sep)`. Does a path whose prefix only
   resembles the home directory, a symlinked home, or a home with a trailing separator
   behave as intended? And does any other field (PR URLs, agent descriptions, branch
   names, board ids) carry an account name or a private repo name into a public record?
2. Agent descriptions are read from `agent-<id>.meta.json`, written from whatever the
   launching session typed. The identifiers block prints them uncapped. Is a block
   that quotes the orchestrator's own dispatch wording safe to paste into a public
   record, and does the doctrine tell the session to look before pasting?
3. A live session's own still-running agents show ❌, by design. At the moment a
   session runs ccclose to decide "ready to close", it may itself be a subagent or
   have a background reviewer open. Is there an input where the session cannot get a
   ✅ even when it is genuinely done, and does that push sessions to discount the line?
4. "Finished" rests on `stop_reason: "end_turn"` in the last assistant record. Does a
   `SendMessage` resume, a compaction, a max-tokens stop or an error stop leave a last
   record the code misreads either way?
5. The doctrine bullet's grounding says a read of 30 sessions found eleven agents
   "cut by a host crash" that survived only because their sessions were resumed. Is
   that read reproducible from the intent record, and does it support "every close
   made with no agent still running"?
6. `CONCURRENCY.md` now lists "the live agent list" beside `git status`. Is that a
   harness feature every session has (Claude Code, cloud, the SDK), and is the
   `ccclose` check the only durable way to read it?
7. The identifiers form "runs none of the twelve checks" and exits 0 always. A
   session that pastes the block may treat its presence as the close's evidence. Is
   the distinction between record and verdict stated where the block is pasted?
8. The commit-range rule prints `first^..last` only when each commit's parent is the
   previous one. With a series rebased onto `main` between sessions, as `4142efb` and
   `8b30ee6` were (one committer second), which form prints, and is it the truth?
9. `bdb1aba` changes the plain run's output and its `--stat` names no change to
   `instruments/ccclose.design.md` or `instruments/README.md`. Do the design note's
   §10 output contract and §15 ("runs none of the twelve checks") and the README's
   description still match what a plain run prints?
10. A plain run now appends a block that includes agent descriptions and paths to
    output a session may paste whole into a record. Did the move from opt-in to
    default change what reaches public records without anyone choosing it?
