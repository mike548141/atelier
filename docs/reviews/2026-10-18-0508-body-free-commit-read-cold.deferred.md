# Sibling to the body-free-commit-read cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Facts held back

1. **Intent record:** `130/030` (the item whose path the brief bars) — **not opened by the
   brief-writer**. Neither commit's message body was read either, so this sibling carries no
   account of the author's reasons beyond what the tool's docstring states; read both at
   reconcile.
2. **The neighbouring pass.** `adf75a4`'s new *side doors* paragraph in `REVIEW.md` rule 1 ends
   "The commit-message door is `130/030`'s", so it treats this delta as the fix for one of its
   doors. That paragraph is queued at `160/910`, briefed in the same sitting by this same
   brief-writer. The two passes share a brief-writer's framing; neither was told what the other
   found.
3. **Prior verdicts on this surface** (named by filename only, not opened, not exhaustive): the
   pass behind the 2026-08-17 coldsweep ruling is the nearest; find it with
   `ls docs/reviews | grep -iE 'coldsweep|cold-sweep|sweep'` at reconcile.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **`%s` is not the first line.** The tool prints `git log --format=%h %s`. Git's `%s` is the
   first *paragraph* of the message, joined onto one line. A message with no blank line after its
   first line prints its whole first paragraph as the "subject". Does the docstring's "cannot be
   printed" survive that, and does any test cover it?
2. **The intent record is in the diff.** Landing commits here routinely edit their own intent
   record and queue pointer (`adf75a4` and `30aa8dc` both do), and neither is in the default
   barred set. The skill tells a brief-writer to cite `--commit <sha> [--path <p>]`, with
   `--path` optional and no mention of `--also-exclude`. Does a literal follower print the
   author's account through the hunk the tool was built to avoid, under a closing line saying the
   body was not read?
3. **The closing line's claim.** "message body not read" is printed after any successful run. Is
   it a statement about what the tool printed (true by construction of the `log` call), or a
   wider claim a reviewer will read as "nothing of the author's account reached me"?
4. **The stamped copy extends its parent.** The skill's header says it may compress
   `REVIEW.md`, never contradict it. As far as a grep of `REVIEW.md` shows, the parent names
   neither `--commit` nor a duty on the brief-writer to run re-run lines; both hunks may be
   content the parent does not hold, which inverts the stamped-copy direction (one fact, one
   home).
5. **"Plain `git show` is barred."** The skill says plain `git show` prints the body before the
   diff. That is true of its default format; `git show --format=%s` or `--no-patch` variants do
   not. Is "barred" the right word for a command whose default leaks, and does the parent bar it?
6. **Test portability and strength.** The fixture's `PATH` is hard-coded to four directories and
   `HOME` to the temp dir. Does that run on CI's image and on a machine with git elsewhere? And is
   there a test that would fail if `--format=%h %s` became `--format=%h %B`?
7. **The re-run duty's reach.** Item 5 now says the brief-writer runs every re-run line once
   before writing it down. Rule 4 says the brief is written by the non-author who takes the
   item; under the 2026-10-16 practice a separate Opus brief-writer writes it instead. Does the
   duty assume a brief-writer with the reviewer's tools and machine, and does rule 4 or `REVIEW.md`
   § *Re-run every "live-proven" claim* say the same?
