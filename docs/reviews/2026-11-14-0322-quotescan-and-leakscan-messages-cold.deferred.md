# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0322-quotescan-and-leakscan-messages-cold.md`
(`REVIEW.md` rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session
`5b3a35e9`), which authored none of the delta. Open this only after act 1 is committed. Everything
here is a floor, never a fence, and none of it is a finding: the brief-writer read the code once
and probed none of these past what is recorded below.

## What the barred intent records say, in brief

- `160/900` carries the earlier pass's verdict summary (PASS-WITH-FINDINGS, QK1–QK14, one MAJOR),
  the principal's 2026-11-08 answer *"Keep edit; read committed only"*, the 2026-11-09 application
  of QK1's first counsel, and the note that QK1's second counsel "needs his word" and is "new
  machinery". It then records this build as done "on his words there" (`320/810`'s "all six"), and
  restates the claim: a double-quoted span of two or more words or a `>` line, or a reasoned
  marker; "It reads the form, never whose words they are."
- `320/810` records slice 6 with the figures the changelog states: "19 commits touch the prompt,
  8 carry a quote (42%)", 21 of 21 exit 0 with the date patched, "Tests: 14"; that the date is the
  run's choice, four weeks after `NAME_WARN_UNTIL`; and that "`quotescan` fires only on commits
  touching one file". It also records that existing clones need `tools/commit-msg.sample`
  installed for the message-plane checks to run, that until then CI's report is the only cover,
  and that `floorfleet` does not check for that hook.
- `320/550` carries the child's finding, the 2026-10-16 verification at HEAD, and the part (a)
  landing: "Measured over atelier's 2,302 messages: 4 hits in 3 messages (3 structural, 1 term)",
  "Listing them is one command; they are the principal's to weigh". Part (b) stays open. It also
  says pull-request titles and bodies are not read by anything yet.

## The brief-writer's re-run results (2026-11-14 UTC, load average about 5.5)

- `test_quotescan`: 14 tests, OK. `test_leakscan.CommitMessages`: 7 tests, OK.
  `test_floor.MsgPlaneTest`: 10 tests, OK. `quotescan --selftest`: OK, exit 0.
- `quotescan --range HEAD --warn`: **10** unquoted changes reported. `git log -- <prompt>` lists
  **19** commits (39 with `--full-history`, 21 of them merges). The landing says 19 touch and 8
  carry a quote, which would leave 11 unquoted, not 10. No commit has touched the prompt since the
  landing (last prompt commit `56e45a3b`, 2026-11-09). Unexplained by the brief-writer.
- `quotescan --range pushed --warn` outside Actions: clean, exit 0, with the note "no pushed range
  known: reading HEAD only", and the advisory line "0 finding(s)".
- `quotescan --range nosuch..HEAD --warn`: exit 2, git's error text echoed.
- `floor.py --plane msg --list`: `quotescan enforced fleet decl 1/5`.
- `leakscan --messages --json` (counts only): 2,336 messages read, 3 with findings, 4 findings
  (2 `email`, 1 `nz-address`, 1 `local-term`), `scanned_local_terms: true`, exit 0. The landing's
  "4 hits in 3 messages (3 structural, 1 term)" over 2,302 still holds over 2,336. Text mode exit 0.
- `leakscan --messages nosuch..HEAD`: exit 2.
- The fleet probe was not run by the brief-writer.

## The brief-writer's own questions

1. **Two one-word quotes.** `QUOTE_RX` is `["“][^"“”\n]*\s[^"“”\n]*["”]`. In `"x" and "y"` the span
   from the first closing quote to the second opening quote (`" and "`) matches as a two-word
   quote. So two quoted single words satisfy it, the case the selftest's "a one-word quote does
   not count" seems meant to exclude (checked once:
   `carries_quote('area: "x" and "y"')` returns True). Likewise a quoted path with a space, a quoted error message.
2. **`>` lines.** Any line starting with `>` counts, including a quoted diff hunk, a shell redirect
   at line start, or a pasted email reply. Git's default cleanup keeps such lines.
3. **Merges and silent `commit_files`.** On the CI plane, `commit_files` runs `git diff-tree`
   without `-m`/`-c`, which prints nothing for a merge commit, and returns `[]` on a git error
   rather than raising. Twenty-one merges show up under `--full-history` for the prompt. A merge
   that brings in a prompt change, or a commit git cannot diff, reads as clean, while `commits()`
   raises on a bad range. Is that asymmetry intended?
4. **No hook, no cover.** The message plane needs the `commit-msg` hook in each clone; CI is
   report-only. So before and after the flip, a clone without the hook (or `--no-verify`) can
   change the prompt with no message check at all, and the CI line says so only in a warning.
   Does the flip mean anything for the actual harm, which is an unseen prompt edit?
5. **Option injection.** Both `--range` (quotescan) and `--messages REVS` (leakscan) go straight to
   `git log` after the format argument. `git log --output=<path>` writes a file, so a spec such as
   `--output=/tmp/x` would make the "read-only" sweep write. Only a local user or a template sets
   these, and `FORBIDDEN_FLAGS` keeps a child's `flags` away, so is this a finding or a one-line
   hardening (`--end-of-options`)?
6. **`nargs="?"`.** `leakscan --messages <positional>` consumes the positional as `REVS`; a user
   who types `leakscan --messages .` gets `git log .`, which reads commits touching `.`, not every
   ref. Probe what `--messages --json` and `--messages --root .` parse as.
7. **"Same rule sets".** `320/550` asked for secret shapes too. leakscan's file mode does not cover
   secrets (that is `secretscan`), so the sizing tool may under-count a secret in a message body.
   Is that gap stated anywhere the user would read before a flip?
8. **Trailer skip.** `AUTHOR_TRAILER_RX` drops any line starting with one of five trailer names,
   anywhere in the body, whatever follows. A private address in a `Signed-off-by:` line of another
   identity would not be counted.
9. **The CI plane comment char.** `commitmsg.commits` cleans pushed messages with `#` as comment
   char, so a body line starting with `#` is dropped before the quote test. A quote that sits on a
   `#`-led line is invisible; probably harmless here, but check for the leakscan sweep, where a
   dropped line is a dropped hit.
10. **`hit` counts by `f.path`.** `report_messages` counts messages with findings as
    `len({f.path})`, where `path` is the 12-character short id. Fine unless two commits share a
    prefix; note only.
11. **The 10 vs 11 discrepancy** above: which of the 19 commits does the tool count as quoted that
    the landing count did not, or did the landing count something else?
12. **`2a6d7a41`** cites the principal's pick inside a code comment in `leakscan.py`, labelled as
    an answer. Out of scope except as a V3 mirror check.
