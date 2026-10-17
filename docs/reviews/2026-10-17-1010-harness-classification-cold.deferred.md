# Sibling to the harness-classification cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-1010-harness-classification-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (name only, never opened): `210/250` (cctranscript counts
  harness text as prompts), filed by the merge that landed ccclose. Neighbouring item
  filed by this delta's merge: `210/260` (notification records read two ways).
- The landing commit's message body (read by the brief-writer), in summary:
  `readTurns` treated every non-tool-result user record as the principal's, so task
  notifications, `isMeta` records and slash-command output echoes took role "you", and
  a prepended browser-instruction block showed as part of a real prompt; "on the 12
  most recent sessions of one repo that read 181 'you' turns where 56 are the
  principal's". One shared classifier now serves `readTurns`, the `--list` label and
  ccclose "so they cannot disagree"; harness text keeps its exchange number so quoted
  refs do not move, and "last-exchange numbers match old and new on all 12 sessions
  checked". Trailer: a Sonnet model.
- The merge's body: read by the orchestrator before the merge; "one NZ-local date
  corrected"; closes 210/250, files 210/260, queues 160/880.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md` — the search surface
- `docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md` — the `--list` first-prompt
  label this delta changes (`firstPromptInLines`)
- `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` — names ccclose

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/870 (ccclose's build) shares `instruments/ccclose`, its tests, the design note and
  the README. This delta rewrote ccclose's own classification twenty minutes after that
  one merged. The 160/870 brief tells its runner to leave this delta's hunks here.
- The first-prompt-prefix pass (2026-10-16) reviewed the `--list` label code before this
  delta changed its record test.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The comment above `HARNESS_TAGS` dates its census 2026-10-17 and counts 40 sessions;
   the commit was made 2026-10-16 16:43 UTC and its body counts 12. Is the comment's date
   NZ-local at rest, and which census grounds the tag list?
2. The header's first chip is `${turns.length} turns`. Does that total now include
   harness turns while the `you` chip excludes them, and does the README's account of
   the header still read true?
3. Only `browser_instruction` is removed from a real prompt. A `system-reminder` joined
   to a real prompt stays in the text cctranscript shows as the principal's, while
   ccclose strips it for the asks. Is that the disagreement the shared classifier was
   meant to end?
4. `isMeta` records are harness "whatever they contain". Does any principal action (a
   slash command's expansion, a skill invoked by the principal) log as `isMeta` and so
   lose its authorship?
5. 210/260's title says notification records are read two ways. Do task notifications
   ever arrive as `queued_command` attachments, where `isHumanQueuedCommand` and not this
   classifier decides, so the two shapes disagree?
6. A transcript whose only user records are harness text: what does `--list` label it,
   and what does ccclose number?
7. Prompt-share figures computed before this change have been quoted in records and
   memory. Does anything flag that counts from the old reader are not comparable with
   counts from the new?
8. `stripElements` builds a fresh lazy-match regex per call over the whole record text.
   With kilobyte-scale notifications and an unclosed tag, what is its cost?
