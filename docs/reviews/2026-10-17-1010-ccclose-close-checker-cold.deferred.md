# Sibling to the ccclose cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (name only, never opened): `020/180` (the mechanisable form
  of it). Neighbouring item filed by the merge: `210/250` (cctranscript counts harness
  text as prompts), the subject of pass 160/880.
- The landing commits' message bodies (read by the brief-writer), in summary:
  - `ef3673a`: first-of-kind, so the design landed before any code; it settles home
    (instruments/, per ADR 0006's purpose rule), streaming reuse of cctranscript's
    classifiers, the window heuristic "stated in every run", the eleven checks and why
    three can only warn.
  - `4eda680`: "a session declared its close from memory, the thing that drifts most";
    dogfooding added the live window and stripping the browser extension's injected
    instructions; "Tests: 22 … five mutations (cancelled passes, short sha, merged
    branch ok, meta prompts counted, gh-missing passes) each fail the suite".
  - `6ccbc7a` (merge): Mike answered "Build it"; "read and run by the orchestrator on
    its own live session before the merge; three NZ-local dates corrected to UTC here";
    "not installed onto the path: whether a session may add a tool to the expected
    toolbox is open, so that is Mike's"; files 210/250 and queues 160/870.
  - `09a61b4` (close commit): Mike answered "install it"; the TOOLBOX row names ccclose
    and `instruments/install` was run (symlinks only); "the toolbox edit joins 160/870's
    delta in this commit". The same commit records an unrelated answer on 115/090.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` — the only verdict whose text
  names ccclose; it was being written in the review worktree when this brief was
- `docs/reviews/2026-10-16-1510-expected-toolbox-cold.md` — the TOOLBOX install rule
- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md` — the reused module
- `docs/reviews/2026-10-16-1550-ccarchive-hardening-cold.md` — the env-seam precedent the
  design note cites
- `docs/reviews/2026-07-11-instruments-test-floor-code-review.md`

## The pointer's own lens hints

None. The pointer is refs-only; it names the TOOLBOX row as part of the delta.

## Overlap with sibling passes of this batch

- 160/880 (`cea247e`) rewrote ccclose's record classification, its wrapper list and
  design-note §6 twenty minutes after this delta merged. Its brief tells its runner to
  review ccclose's use of the shared classifier; this brief tells its runner to leave
  `cea247e`'s hunks to 160/880. Expect both verdicts to touch `readTranscript`.
- 160/500's pointer records a MAJOR, TB1, on the install grant riding on a list any
  session may extend in the same commit that uses it. The ccclose row was added to that
  list after the merge held it back on exactly that question, on Mike's answer.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `CLAIM_LINE` wants a line that begins with a list bullet and `[~]`; `CLAIM_TIME`
   matches lower-case `claimed` with no case flag. The claim lines this board carries
   at HEAD (160/500 is one) sit on a continuation line, with the marker inside a code
   span and the word in capitals. Does check 7 see any real claim on this repo, and did
   the fixtures use the board's real form?
2. The row went into the toolbox list after the merge said adding it was an open
   question for Mike, and TB1 questions that list's grant. Is the row's authority (an
   answer, not a ruling) recorded where the row sits?
3. The design says listed items are capped at 25 "with the number not shown". Does the
   text form say a list was cut, and is that consistent with the house rule that a
   report's fields stay comparable run to run?
4. `GREEN` holds `skipped` and `neutral`. Is a skipped floor workflow a pass under
   `RECORD.md`'s floor-at-head rule? `gh run list --limit 50` per sha: can the latest run
   of a workflow fall outside the window?
5. Window membership compares committer time to the transcript; the `--since` pre-filter
   subtracts a day. A cherry-pick or rebase keeps its author date. Which date does each
   check use, and does a peer's rebase onto this session's window get credited here?
6. `boardTool` prefers the checked repo's own `tools/board.py` and runs it with
   `python3`. Is that read-only (byte-code caches), and is executing a checked repo's
   code consistent with "read-only by contract"?
7. The asks heuristic lists a sentence for a cue plus an object; the cue set includes
   bare "close", "record", "log" and "update", the object set "board", "reviews" and
   "memory", and the strong set "clean up". How many lines would a normal long session
   list, and does a high count train sessions to skim it?
8. Three checks can never fail. A dirty tree at close is ⚠️ because a peer may have
   made it. Is there any input under which ccclose prints ✅ overall while the session
   itself left uncommitted work?
9. `CCCLOSE_GH` is honoured outside tests. Is an env var choosing which binary runs the
   same seam shape as ccarchive's simulate flag, which only changes what is believed?
10. The asks list quotes the principal's prompts into output the design says "gets
    pasted into records". Some of those records are in public repos.
