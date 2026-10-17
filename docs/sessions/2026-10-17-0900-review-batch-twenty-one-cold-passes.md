# 2026-10-17 · 0900 UTC · Review batch: the twenty-one briefed cold passes, and twelve briefs for the rest

**Model:** Claude Fable 5.1 orchestrating; twenty-one fresh Fable 5.1 reviewers (one per
pass); three Opus 5.5 brief-writers. **Worktree:** `atelier-review-1017`, branch
`review-1017`, fast-forwarded onto `main` and pushed after every close.
**Mike's ask, verbatim:** *"I want you to do all reviews and fable dependent work"*; mid-run,
*"I ran out of claude budget but that is resolved now. Pick up where you left off"*, then three
times that he was being asked to approve "endless amounts of file edits and commands", and at
the end *"We hit a budget limit. Pick up where you left off"*.

## What the run was

The 2026-10-16 run had written briefs for all 21 queued rule-4 passes (`160/500`–`760`) and
run none. This session, a Mike-opened Fable session that authored none of the deltas and none
of the briefs, took the whole queue in one sitting under the reviewer-plus-orchestrator shape
(`REVIEW.md` rule 4): one fresh Fable subagent per pass formed every finding and severity; the
orchestrator held each `.deferred.md` sibling outside the worktree and outside the harness
scratchpad, committed phase 1 before releasing the sibling by message, and formed no finding.
Every pointer was claimed in one commit on `main` (`8acfff1`) before any pass ran.

## Results — 21 passes, all verdicted on `main`

Twelve passes returned a MAJOR and stay open for Mike's ruling; nine returned none, so their
cycles close. Totals across the batch: **12 MAJOR · 52 MODERATE · 77 minor · 64 note**. Each
pointer carries its own counts and verdict link; the headline finding per pass:

| Item | Pass | Headline |
|---|---|---|
| `160/500` | TB · 🛑 | The install grant rides on a list any session may extend in the commit that uses it |
| `160/520` | SY · 🎯 | Step 2's stop-and-move leaves the run no sync path, so step 4's claim cannot land |
| `160/530` | RM · 🛑 | A profile's public visibility reaches `repo create --public` with no floor stop |
| `160/540` | HM · 🛑 | The session-open prompt's delta is reverted at HEAD by the stale-base restore (`320/670`) |
| `160/550` | WV · 🛑 | A worktree pointed at the primary's venv runs the primary tree's code, tests green |
| `160/560` | TC · 🎯 | The third cue ends in knowledge, not the action a firing cue is defined by |
| `160/570` | BR · 🎯 | A third stale `DATA-PROTECTION.md` citation survives the phrase-keyed sweep |
| `160/580` | RB · 🛑 | The skill's rule-4 paraphrase drops the neither-started-nor-instructed criterion |
| `160/590` | TT · 🎯 | The template still conditions review on "a more capable model" |
| `160/610` | TG · 🛑 | The trigger list is restated in a file whose header forbids it; ADR 0100 d3 reversed |
| `160/620` | FM · 🛑 | AUTONOMY's deploy-on-push floor member has been absent from every copy since July |
| `160/670` | HD · 🎯 | A rolled-back manifest-and-signature pair verifies; the ccarchive cycle closes |
| `160/680` | FP · 🎯 | A corrupt-but-decodable prefix lists wrong text where the old read threw |
| `160/690` | PO · 🛑 | The legend admits three queue counts; every live pointer wears the unnamed shape |
| `160/700` | IX · 🛑 | Code-span catalogues have no guard when an entry's file is deleted |
| `160/710` | CK · 🎯 | `EVIDENCE.md` § 15 contradicts § 2's tier rule and bypasses § 13's ladder |
| `160/720` | GT · 🎯 | Three pre-existing quadratic regexes stay reachable; a blocking hook can stall |
| `160/730` | RT · 🎯 | The shared unreadable-file exit path is dead in five of nine guards |
| `160/740` | PF · 🛑 | `--history` walks the clone's refs while the flip publishes the host's |
| `160/750` | MK · 🛑 | "Any other scope exempts every kind" is kept against the delta's own survey |
| `160/760` | QP · 🛑 | Unpinned diff config let two staged guards scan nothing at the landing commit |

Nothing was applied. The HD pass is the re-review that `160/460` and `160/510` were waiting on;
it returned no MAJOR, so that cycle closes with them. Several passes re-found open findings
from earlier verdicts (RR1/RR8/AK2 under FM, CH2/CH7 under TC, FW8/FW4/AM13 under RT,
LK1/AM2/AM4 under MK, PL5 under PF); each reconcile names the pairing so one ruling can close
both.

## Briefs written, none run

Three Opus brief-writers, each authoring none of the deltas, wrote a refs-only brief and a
sibling for the twelve unbriefed pointers `160/780`–`890` (prefixes EC HX SX DM BY RN LA SZ
AV CL HC MA, each checked unused). They were staged user-locally and landed in one commit
(`b42f305`) after the last reviewer's phase-1 sweep, so no new sibling sat in the tree while a
reviewer swept it. This session instructed the writers, so it does not run those passes.

## Also landed

- Nine child hand-up PRs (#108–#116), cherry-picked as-is with the board index rebuilt; two
  number collisions renumbered (`320/650`→`680`, `320/690`→`700`). PR #108 changes `ccmail`
  (30/30 tests at HEAD) and queued its own rule-4 pointer in the landing commit (`160/890`).
- `130/030`: the brief bars the landing commit's message body but names no command that avoids
  it; five of 21 reviewers disclosed the same slip. Filed with evidence and a proposed fix.
- Mike's permission settings: `bypassPermissions` user-level and in every repo's local file,
  on his instruction; the live session's mode is his to switch in the UI.

## Recorded against itself

- **The Fable weekly cap landed inside the first wave.** Three reviewers died with a 429 within
  a minute of spawning; the Opus brief-writer kept going. On Mike's word that the budget was
  resolved, each reviewer was resumed by message to its own transcript and disclosed the
  interruption; one had already written its full phase-1 verdict.
- **Machine load reached 170** (15-minute 135, the figure of the 2026-10-16 SIGTERM) from
  another repo's test fan-out, not this batch. The run held at two agents through it, pushed
  after every commit, and warned the session watching the queue runs, which throttled the
  source. A machine-wide `pkill -f "pytest -q"` from that side touched nothing here.
- **The session was cut twice**: once by the weekly cap, once at the end by a session limit
  followed by a machine restart at 02:41 local. The PF reviewer's phase 2 resumed from its own
  transcript on the next day; a stuck commit (signing agent empty after the restart) was killed
  and retried once the keys were reloaded.
- **Prompts.** Mike was asked to approve tool calls throughout, despite the settings fix,
  because a live session's permission mode is read at launch and every subagent inherits it.
  Two replies reported the settings edit as the fix before the third said what only he could do.
- **Five reviewers leaked a barred commit body** by the obvious `git show`; filed as `130/030`.
- **Subagents at close:** 21 reviewers and 3 brief-writers, all finished; none still working
  (`020/420`'s check, done by hand because `ccclose` does not yet read the agent list).

## Next

Mike's ruling round now holds the nine MAJOR passes from 2026-09-26 and the twelve from this
batch; the twelve briefed pointers `160/780`–`890` wait for a further cold Fable session.
