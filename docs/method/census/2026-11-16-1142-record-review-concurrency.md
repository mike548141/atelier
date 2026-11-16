# Enforcement census — RECORD, REVIEW, CONCURRENCY

Board item `020/220`, slice 1 of the census. Run 2026-11-16 (UTC) by a worker
of queue run 78ca. This is a measurement record, not doctrine: it changes no
rule, and it builds no guard.

## What this asks

For each rule in three governing documents: if it is broken, what sees it? Each
rule gets one state.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook) and whether it **blocks** or **warns**. *partial* means the
  check covers some of the rule and the rest is unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it (`ccclose`,
  `coldsweep`, `tools/worktree.py`), the row says *instrument* and the state
  stays directive-only: nothing invokes those tools, so nothing sees the
  breach unless the breaker looks.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), and the reason is stated. Accepted as of
  2026-11-16.

A directive-only rule also gets the place its breach could be seen, because
that is what the guard ranking in `020/240` needs:

- **diff**: the breach is in the committed change itself (paths, lines, file
  names, the commit message). A commit-plane check could read it.
- **record**: the breach shows only by joining records outside one diff: board
  state over time, CI run history, refs and worktrees, review files read
  against each other.
- **invisible**: the breach leaves nothing in the tree or the repo's records.
  At most a session transcript holds it, and some of those are reachable by a
  harness hook before the act (the before-plane, `115/100`).

## Method, and what it did not do

1. Read `RECORD.md`, `REVIEW.md` and `CONCURRENCY.md` in full at the commit the
   worktree was cut from (board claim commit of run 78ca). Each sentence that
   tells a future agent to do or not do something is a rule. Bearings,
   grounding stories, framing paragraphs and pure permissions are not counted
   (`RECORD.md`'s estate-root paragraph is a relaxation, with no breach to see;
   `REVIEW.md` § *What review is not* restates rules counted elsewhere).
   Clauses that only restate one rule are folded into it.
2. Listed every check that could see a breach: the floor registry
   (`python3 tools/floor.py --list` on each plane), `.githooks/`,
   `.github/workflows/ci.yml`, the test suites that pin doctrine text
   (`tools/test_templates.py`, `tools/test_queue_run_single_source.py`), the
   harness hook `tools/modelguard.py`, and the self-run instruments.
3. Before writing *enforced* against a rule, read the code that does it and
   cite it as file and function. Where a scanner's own date window means it
   warns at present though the floor lists it `enforced`, the row says so:
   `attribscan` warns until 2027-02-08, `namescan` until 2027-05-03
   (`ATTRIBUTION_WARN_UNTIL`, `NAME_WARN_UNTIL`).
4. Did not read `docs/SESSIONS.md` or `docs/sessions/` (the run's bounds). That
   matters once, below.

**On reusing `115/110`.** The map behind `115/110` (2026-08-15, four governing
documents, rule by rule) has no file of its own: what survives in a readable
home is the item's summary. It names `00-APEX.md` and `AUTONOMY.md`; the other
two are not named. Its rule list cites a `REVIEW.md` rule (the independence
criterion) and a `CONCURRENCY.md` one (an item's text never overrides
doctrine), and its gate list (review-line presence, index freshness, date form)
fits `REVIEW.md` and `RECORD.md`. So this slice may overlap that map. Its
detail sits, if anywhere, in a session record this worker was barred from
reading, so this is a fresh pass. Where the two touch they agree: the
independence criterion is `REV13` below, directive-only and invisible; the
item-text rule is `CON70`; the review-line, index and date gates are `REV41`,
`REC22` and `REC28`.

**Why this file lives here.** `115/110` left no file to sit beside. The run's
brief named `docs/method/census/` as the fallback. `docs/reviews/` is for
briefs and verdicts and its scanner reads them as such; `docs/sessions/` is
per-session and on a cold reviewer's barred list, while this census is meant to
be read by the next slices and by `020/240`. A census sits beside the doctrine
it measures, and later slices add their files here.

## RECORD.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| REC1 | The doc that governs a behaviour lands in the behaviour's commit; what lands lands doc-complete (*Docs-as-code*) | enforced, partial (CI, blocks the run) | Per-instrument tests pin some man pages to their CLI: `instruments/test_ccfleet.py` (flags in `--help` absent from the man page), `instruments/ccclose.test.js` (page exists, options listed); CI's `man page lint` step lints form only. Everything else: diff. Other instruments' pins unverified |
| REC2 | Structure as documented must exist (*Docs-as-code*) | enforced, partial | `linkscan` blocks a Markdown link that does not resolve (hook + CI; `linkscan.py:resolve`); `pathscan` warns on a backtick path that does not resolve (`pathscan.py:iter_candidates`); `indexscan` warns on a file an opted-in index never lists (`indexscan.py:scan_paths`). Prose naming a path without either form: unseen |
| REC3 | Stub honestly: what is not built is labelled a stub (*Docs-as-code*) | directive-only | diff, judgement |
| REC4 | Comments and commit bodies say why, not what (*The why lives at the site*) | directive-only | diff, judgement |
| REC5 | The session index is append-only: an entry is never edited or reordered; rotation moves old entries verbatim to an archive store, and the rotating session says so (*The session log*) | directive-only | diff: a change or removal of a non-tail line of the index that does not reappear verbatim in the archive |
| REC6 | The index stays one line per entry with detail in a file; nothing reads it for that shape (the doc says so) | directive-only | diff |
| REC7 | A detail record is named `<date>-<HHMM>-<slug>` in UTC under the session-record directory | directive-only | diff: file-name shape (the UTC half is `REC30`'s class) |
| REC8 | A pointer to an addendum names the index entry, not the earlier detail file | directive-only | diff, judgement |
| REC9 | A detail record and the closing message end with the identifiers block, read fresh; an extended record replaces or dates it | directive-only | diff for the detail record (block presence); invisible for the message. Instrument: `ccclose --identifiers` prints the block, checks nothing |
| REC10 | Declare the close only at the end of a sequence, with the tidy-up done and a clear all-done message | directive-only | invisible. Instrument: `ccclose` (fourteen checks, exit 0 when none fails; nothing invokes it) |
| REC11 | The all-clear carries its evidence; a loose end makes the close "not ready until you decide", put through the decision device | directive-only | invisible. Instrument: `ccclose:checkScratch` warns on files left in scratch |
| REC12 | The close names every agent launched and how each ended, read from the agent list | directive-only | record (transcript and subagent files). Instrument: `ccclose:checkSubagents` |
| REC13 | A close that pushes carries the pushed floor run's result, or names it pending | directive-only | record (CI runs). Instrument: `ccclose:checkFloor` |
| REC14 | Before a push of doctrine, a skill or a test to `main`, run the full suite | directive-only | record: CI's tool test suite reds after the push on the consequence, not on the skipped run |
| REC15 | A cancelled run is not a result; re-run on your own SHA once the group is quiet | directive-only | record (CI runs). Instrument: `ccclose:checkFloor` fails a cancelled run on the session's last SHA |
| REC16 | A session with no repo: thin person-level onramp, move to the repo before recording, hand on by a route, privacy line travels with the output (*A session with no repo*) | unenforceable, accepted | There is no tree, so no plane exists until the output lands; on landing, the entry half is the receiving repo's floor (`leakscan`, `pdlistscan`) |
| REC17 | Write an ADR when forgetting the reasoning risks re-litigation (*Decisions*) | directive-only | invisible: an omission leaves nothing |
| REC18 | An ADR draft is accepted only by the principal, informed, in plain language | directive-only | diff: a status flip to accepted with no citation of him. `attribscan` sees a different form (an attribution word such as *ruled*), not acceptance |
| REC19 | An accepted ADR is immutable; change comes only by dated addendum, revoked or superseded | directive-only | diff: a change to an accepted ADR above its last addendum. `reviewscan`'s docstring states the append-only premise and checks nothing about it |
| REC20 | Revoked and superseded take their status-line form and back-pointer | directive-only | diff |
| REC21 | Reservations on an approval are recorded verbatim beside it, and each becomes a check the build answers (*An approval is not the whole ruling*) | directive-only | record: only against the transcript |
| REC22 | The board is per-item files; the index is generated and never hand-edited (*The roadmap*) | enforced (blocks, hook + CI) | `board` floor check, `board.py:_run_check` (`--staged` at the hook reads the git index on both sides; `--check` on CI); item-number collisions too (`board.py:number_collisions`) |
| REC23 | A finished item flips `[x]` in its own file in the commit that finishes the work | directive-only | record. On a monolithic board `REC25` gates the hot path; on a split board the index renders done items as ✅, so nothing reads the flip |
| REC24 | Bulk deletion from a record store is shown to the principal first, whoever made the mess | enforced, partial (warns) | `harvestscan` warns when a removed roadmap item survives nowhere (`harvestscan.py:survivors`, `net_line_loss`; hook + CI, warn-only). Deletions from session records, ADRs and review files: diff, unguarded. The showing itself: invisible |
| REC25 | No completed `[x]` item on a monolithic board's hot path; on such a board the harvest happens at the close | enforced (blocks, hook + CI) | `sizescan --check`, `sizescan.py:cold_item_count`; applies to `ROADMAP.md` only, so to monolithic boards |
| REC26 | Resolved narrative stays off the hot path | unenforceable, accepted | A machine cannot name prose-shaped cold content without guessing (`sizescan.py` docstring; `160/850` SZ2). The doc says so |
| REC27 | An archive store holds no live state marker | enforced (blocks, hook + CI) | `sizescan --check`, `sizescan.py:live_item_count` over `*-DONE.md` and `*-ARCHIVE.md` wherever they live |
| REC28 | Every dated thing states an absolute ISO date, never relative time (*Absolute dating*) | enforced, partial (blocks, hook + CI) | `datescan.py:scan_text` (relative-time terms, the word for the current day only beside a dating cue, non-ISO and impossible ISO dates) over `docs/**` Markdown, added lines at the hook. Commit messages and other files: unread. That word with no cue beside it passes, by design |
| REC29 | The absolute date is the UTC date | unenforceable, accepted | A local date and a UTC date have the same shape; the licensing fact (the clock when it was written) is outside every window. Partly reachable where a record also carries its own UTC identifier to compare against: unbuilt |
| REC30 | Describe, don't quote, the shapes the floor hunts | enforced, partial (blocks) | The shape scanners block the quote (`secretscan`, `leakscan`, `licenscan` and siblings). What passes is a quote plus a reasoned allow-marker (`allowmarker`, `115/230`). Diff: new markers in record stores are countable |
| REC31 | A public record never joins a private repo's name to its sensitive posture (*The record is public*) | unenforceable, accepted | The doc says no scanner can hold it: the join is meaning, not shape. Adjacent: `namescan` (branch names and commit titles; warns until 2027-05-03) and `leakscan`'s machine-local term list on the hook |
| REC32 | A private repo's state is described by type only | directive-only | diff. Whether `leakscan`'s term list holds private repo names is unverified (the list is machine-local); if it does, it flags every mention, which this rule allows |

## REVIEW.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| REV1 | The reviewer is a separate agent with fresh context, at the capability the stakes need (*Why review*) | directive-only | record (the verdict's provenance) |
| REV2 | An author-framed review of doctrine or structural work earns an un-briefed re-run | directive-only | record |
| REV3 | Rule 1: seeded questions sit in a sibling `.deferred.md`, never a section of the brief | enforced, partial (blocks, hook + CI) | `reviewscan.py:scan_brief` reds a brief with a deferred or seeded heading and no verdict beneath. Keyed on heading words; a section named otherwise escapes (the doc says so) |
| REV4 | The reviewer names the load-bearing assumptions itself, first, and treats the brief's framing as attackable | directive-only | record (the verdict) |
| REV5 | Rule-4 passes run under an orchestrator use the context partition: deferred bytes reach the reviewer only after its findings are written | directive-only | invisible |
| REV6 | At the verdict the deferred sibling is folded below it and deleted | directive-only | diff: a sibling still present beside a closed review. `reviewscan` declines this on purpose (a fold-back lint would fire at the prescribed moment) |
| REV7 | Rule 2: no prior verdict is opened before the reviewer's own findings are committed | directive-only | invisible. Instrument: `coldsweep` excludes the barred set by default |
| REV8 | A new brief points at a prior verdict, never quotes or summarises it | directive-only | diff: verdict text reappearing in a brief |
| REV9 | Sweep the tree with `coldsweep`; a wide sweep is disclosed | directive-only | invisible (the banner prints to the sweeper) |
| REV10 | Read a landing commit with `coldsweep --commit`, never plain `git show` | directive-only | invisible |
| REV11 | A cold reviewer skips the session-log step, and discloses anything it met | directive-only | invisible |
| REV12 | Rule 3: findings on self-authored doctrine are the principal's to decide, informed; the author applies nothing alone; an earlier answer is named; a floor stop is re-briefed before the act | directive-only | diff: a doctrine review's findings tagged decided with no citation of him. `attribscan` (warns until 2027-02-08) sees only an attribution word without evidence |
| REV13 | Rule 4: the review comes from a session the author neither started nor instructed; an author-scheduled batch or inline spawn fails it | directive-only | invisible to the tree: who started whom lives in the harness. Also `115/110`'s finding |
| REV14 | A queued pointer is refs only, no evaluative account | enforced (warns) | `pointerscan.py:grammar_findings` (hook + CI, warn-only) |
| REV15 | Landing is queuing: the pointer goes in the commit that completes the work | directive-only | diff: a commit touching doctrine paths with no pointer line added. Instrument: `ccclose:checkReviews` warns over the session window, not the commit |
| REV16 | A moving bound in a pointer is pinned to a fixed SHA by the taker, in the claim and the verdict's scope | directive-only | diff |
| REV17 | Tier is checked at selection: cold passes run on the tier the principal names; a session that cannot honour it stops | directive-only | record (the transcript's model id). `tools/modelguard.py` makes every spawn name a model; it does not check which, and its wiring is user-level, unverified here |
| REV18 | An off-tier orchestrator forms no finding and is disclosed in the claim, the pointer and the verdict; the reviewer records the spawn prompt, barred set and release message | directive-only | diff for the disclosures' presence; invisible for whether it formed a finding |
| REV19 | The brief states its spawn provenance and the verdict repeats it (checklist V7, which the doc calls not mechanised) | directive-only | diff: a review file with no provenance field |
| REV20 | Contact between an author and its review chain is disclosed, recorded by the receiver | directive-only | invisible |
| REV21 | Scope is the whole commitment; non-goals are the only narrowing, and themselves reviewable | directive-only | record (the verdict) |
| REV22 | The review-brief skill names every lens the doctrine lists | enforced (CI test, blocks the run) | `tools/test_templates.py`, `ReviewBriefSkillTest.test_skill_names_every_canonical_lens`. Pins the delivery copy, not the review |
| REV23 | Every review runs all four lenses | directive-only | record (the verdict) |
| REV24 | The security lens: threats enumerated before building; `/security-review` where it reaches, never over a dirty brief; otherwise discharged with grounds | directive-only | record |
| REV25 | A confirmed security finding carries a severity and a recurrence-prevention step, and routes to `SECURITY.md` for shipped tooling | directive-only | diff, judgement on what counts as security |
| REV26 | Re-run every live-proven claim in scope; the brief-writer runs every re-run line once first | directive-only | record |
| REV27 | The seven standing checks V1 to V7 run on every review, each discharged with grounds where idle | directive-only | diff: a verdict with no line for one of them |
| REV28 | A brief is written to the review directory under a `<date>-<HHMM>-<slug>` name in UTC, with a board pointer | directive-only | diff: `reviewscan`'s name pattern selects files, it refuses none |
| REV29 | Findings carry stable ids | directive-only | diff |
| REV30 | The verdict is appended to the brief's own file below a divider | directive-only | diff |
| REV31 | Every finding is tagged fixed, backlog or rejected with grounds; none is dropped | directive-only | diff: a closed verdict with an untagged finding |
| REV32 | A finding closes only when its fix is verified, with a live proof where one exists | directive-only | record |
| REV33 | A review file keeps a dated `Status:` line and a `board:` line | enforced (warns, hook + CI) | `reviewscan.py:header_warnings` (check 3), for files dated from 2026-11-10; warn-only with no blocking date |
| REV34 | A verdict carries its method record: what was examined, every check's command and result, evidence per finding | directive-only | diff for the record's presence; record for whether a third party could re-run it |
| REV35 | Applying decisions to doctrine earns a cold pass; the applier queues the pointer in the application commit; the cycle closes on a pass with no MAJOR, and stops to ask when MAJORs are not falling | directive-only | record |
| REV36 | A pass not accepted is withdrawn, never deleted: preserved verbatim under a banner, quarantined, never handed to the redo, its findings dying with it | directive-only | diff: a deleted review file. `harvestscan` watches roadmap items only |
| REV37 | A verdict accepted in part says so, and the deferred half gets its own pointer | directive-only | record |
| REV38 | A degraded pass is topped up, not silently accepted; the top-up names its anchoring, its scope and whether a re-run is owed; its builder may not orchestrate it | directive-only | record |
| REV39 | Whether work earns a review is judged on commitment, not artefact | directive-only | invisible: an omission. Instrument: `ccclose:checkReviews` warns when doctrine or tool paths changed and no pointer landed |
| REV40 | Budget decides how many reviews run, never how one runs; at an empty allowance pause and record | directive-only | invisible: a thinner brief looks like a brief. The doc says the guards are unbuilt (`430/010`) |
| REV41 | A durable design record carries a review line: decision records | enforced, partial (blocks, hook + CI) | `reviewscan.py:scan_record` (check 1), dated decision records from 2026-07-21; numbered records skipped; presence only |
| REV42 | The same review line on roadmap sections | unenforceable, accepted | Rejected as a lint because it fires on prose and gets trained away (decision record of 2026-07-18-0820; `reviewscan.py` docstring). A recorded decision not to build, rather than a missing window |

## CONCURRENCY.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| CON1 | One worktree per line of work; never parallel work in one tree (*The substrate*) | directive-only | invisible. Instrument: `tools/worktree.py start` |
| CON2 | Worktrees live outside iCloud | directive-only | invisible. Instrument: `worktree.py` refuses an iCloud path, only when used |
| CON3 | Each parallel session's log entry names its worktree and branch | directive-only | diff |
| CON4 | Assume another session is live; write-heavy or multi-commit work takes a worktree by default; a light write syncs first (*The trigger*) | directive-only | invisible |
| CON5 | A session opened as known-second works in a worktree from its first act | directive-only | invisible |
| CON6 | Dirty-tree backstop: changes you did not make send you to a worktree; never absorb them | enforced, partial (warns, hook only) | `sweepscan.py:judge` warns on a whole-index commit where sibling worktrees exist; skipped on CI by design (`floor.py` `HOOK_ONLY`). Absorption by a pathspec commit is unseen |
| CON7 | Read the whole staged diff before every commit; stage explicit paths, never `-A`; commit by pathspec | enforced, partial (warns, hook only) | `sweepscan.py:judge` (the commit form, from the index file's name); warn-only with no blocking date, on a measured 88% fire rate. The read itself: invisible |
| CON8 | After a refused commit in a shared checkout, unstage your own paths | directive-only | invisible |
| CON9 | In a rebase left in progress, verify each peer commit is reachable and back any autostash out to a file before aborting | directive-only | invisible |
| CON10 | Back out of a shared file by reverse edit, never `checkout`, `restore` or `stash` | directive-only | invisible (a before-plane hook could read the command) |
| CON11 | Solo is concluded from positive evidence, never from a clean tree (*The solo default*) | directive-only | invisible |
| CON12 | Agents for breadth within a task; worktrees for parallel tasks | directive-only | invisible |
| CON13 | Serialise and announce actions that touch the live world (*The safety rail*) | directive-only | invisible to the repo |
| CON14 | Run `cclive` at open (*Beyond the repo*) | directive-only | invisible |
| CON15 | Name what you launch on a shared host with an owner marker | directive-only | invisible to the repo; visible on the host |
| CON16 | The open announcement names hosts, long jobs, shared remote files and live services | directive-only | invisible |
| CON17 | A rate-limited failure is checked against peers before it is treated as a credential fault | directive-only | invisible |
| CON18 | Opening sync: read `git status` first; anything not yours is a stop and a move, never an autostash; no bare pull without an upstream (*Integration hygiene*) | directive-only | invisible |
| CON19 | After the stop: fetch, base the worktree on `origin/main`, claim after a fast-forward | directive-only | invisible |
| CON20 | Verify the act by its own effect, never by the absence of an error | directive-only | invisible |
| CON21 | Read the check before the act, in a separate command | directive-only | invisible to the tree. `EVIDENCE.md` §17 records it as having no guard because "nothing inspects a session's shell invocations"; `tools/modelguard.py` is a harness hook that reads Bash command text, so that ground is contested and the census does not count it accepted |
| CON22 | Concurrent appends conflict; keep both entries in order | enforced, partial (blocks, hook + CI) | `conflictscan.py:scan_text` blocks an unresolved conflict marker; whether both entries were kept: diff, unguarded |
| CON23 | Record series use `<date>-<HHMM>-<slug>` in UTC; files under retired schemes are never renamed | directive-only | diff: a new record file of another shape, or a rename in a record directory |
| CON24 | Re-verify every shared value against the integration branch after a rebase; allocate, push, then check | directive-only | invisible |
| CON25 | Rebase small and often; a worktree diverged for days is a hazard | directive-only | record. Instrument: `worktree.py list` flags divergence |
| CON26 | Remove a worktree when its branch lands and its agent has stopped | directive-only | record. Instrument: `ccclose:checkWorktrees` fails on worktrees made in the window that remain |
| CON27 | Two lines needing one live resource are sequenced, never locked | directive-only | invisible |
| CON28 | Claim at selection: edit the item's own state line in place, commit and push to `main` from the primary checkout before any work, including in a queue run (*Claiming work*) | directive-only | record: claim time against the first work commit; a claim made on a branch. Instrument: `ccclose:checkClaims` checks only that the session's own claims are released at close |
| CON29 | A claim is paired with a file-set announcement; a dispatcher gives each worker a worktree or forbids `-A` | directive-only | invisible |
| CON30 | A split-board claim commit carries the regenerated index (from the index plane at a dirty checkout); an index conflict is resolved by regenerating | enforced (blocks, hook + CI) | `board.py:_run_check` (`--staged` at the hook) |
| CON31 | At a dirty primary checkout, stop only for the same item's file; something staged not yours means wait | enforced, partial (blocks) | The hook refuses a pathspec commit carrying a peer's baked index line without its item (`board.py` docstring, residual 1, read with `_run_check --staged`). The stop on the item's own file: invisible |
| CON32 | A same-item collision yields to whoever pushed first; adjacent different items keep both | directive-only | invisible (git surfaces the conflict; the yield is behaviour) |
| CON33 | A live claim outranks a standing instruction to take that item | directive-only | invisible |
| CON34 | A claim mutates the item in place, never appends to a claims list | directive-only | diff |
| CON35 | A themed line is split into per-leaf lines before fan-out | directive-only | invisible |
| CON36 | An abandoned claim is reverted to open as a real step of put-away | directive-only | record: a claim whose worktree and branch are gone |
| CON37 | An orphan claim is reclaimed on evidence (branch gone, commits stopped), never on a timer | directive-only | record |
| CON38 | A queue outside git uses its tracker's own claim primitive | directive-only | invisible to the repo |
| CON39 | Law 1: a message is awareness, an artefact is authority; what must survive goes in the artefact (*The channel*) | directive-only | invisible |
| CON40 | Law 2: the closing check runs after the push | directive-only | invisible |
| CON41 | Law 3: a repair's tie-break is deterministic (fewer inbound references moves) and announced; a burned identifier stays burned | directive-only | invisible for the tie-break; diff for a reused identifier, read against history |
| CON42 | Talk first: ask the owner of work you meet; talk to decide, write to hold; a message never hands over a claim | directive-only | invisible |
| CON43 | The channel carries hello, holdings, minting, stricter-gate notices, rulings relayed verbatim, findings with measurement apart from diagnosis, and farewell | directive-only | invisible |
| CON44 | A relayed ruling never overrides the principal's direct order; the conflict is put to him quoting both | directive-only | invisible |
| CON45 | A message states what it has not done, hands disposition to the receiver, and makes an offer once | directive-only | invisible |
| CON46 | A peer's claim is a hypothesis: re-run, don't reason | directive-only | invisible |
| CON47 | Abridge on the way into the record and say so; a primary source is committed, not relayed | directive-only | diff, partly: the shape scanners see literal shapes, not an unstated abridgement |
| CON48 | Stay in your lane: no claimed item, no in-flight tree, no other repo's open work, no unrelated fixes in passing (*Stay in your lane*) | directive-only | invisible; scope creep is diff-visible only by judgement |
| CON49 | Work lands in the repo it changes: queue, never deliver | directive-only | record (which session wrote which repo lives in transcripts) |
| CON50 | With no queue in the target, queue in the estate root's board and tell the principal | directive-only | record |
| CON51 | The target's visibility governs what queued evidence may carry | directive-only | diff, partly: the shape scanners in a public target |
| CON52 | A finder that declines the lane parks its list in its own repo and says it is open | directive-only | record |
| CON53 | Every branch ends put away: landed then deleted (delete-on-merge on); abandoned then salvaged, archive-tagged, deleted, recorded, claim reverted (*Every branch ends put away*) | directive-only | record (remote branches, host setting). Instrument: `ccclose:checkBranches` |
| CON54 | Commit messages a resumer can follow, never a bare "wip" (*Surviving an interrupted session*) | directive-only | diff: the commit message |
| CON55 | A genuine block extends the claim line in place with where it stopped | directive-only | record |
| CON56 | Before blocking on a decision, write the open question into the durable record | directive-only | invisible |
| CON57 | Possible interruption residue gets the read-first sweep before new work; another's recovery is not yours | directive-only | invisible |
| CON58 | A run never starts or instructs its own successor (*Orchestrated queue runs*) | directive-only | invisible to the tree; a before-plane hook could read a `claude` launch, as `modelguard` already does for the model flag |
| CON59 | A worker builds, commits and hands back; the merge and the always-confirm floor stay the orchestrator's, after reading the work | directive-only | invisible |
| CON60 | The orchestrator reads every review brief in full before it lands | directive-only | invisible |
| CON61 | A dispatch carries the item and its bounds, never a relaxation of doctrine | directive-only | invisible (the prompt is not in the tree) |
| CON62 | Each worker gets a unique absolute scratch directory; the orchestrator never writes in the scratch root; list the root after a wave | directive-only | invisible. Instrument: `ccclose:checkScratch` warns on leftovers |
| CON63 | Held-back review notes live in a user-local directory outside the repo, worktrees and any scratchpad, never a reviewer's working directory | directive-only | invisible |
| CON64 | Teardown waits for the worker to stop (marker in, nothing running); an unpushed worker's commit is made reachable first | directive-only | invisible. Instrument: `worktree.py remove` refuses unmerged work |
| CON65 | Every dispatch asks for a terminal marker; a long check is redirected to a file with an exit line and polled by the worker | directive-only | invisible |
| CON66 | A run's worktree names carry the session's short id, `<repo>-qr-<id>-<slug>` | directive-only | diff: the claim's worktree field |
| CON67 | A dispatch starts from the copyable skeleton `docs/method/session-open/dispatch-brief.md` | directive-only | invisible. No test pins the skeleton to this section (none found) |
| CON68 | The orchestrator writes the review pointer at the landing; a worker writes none; a cited hash must already be on `main` | directive-only | diff: a pointer citing a branch, or a hash not reachable from `main`. `pointerscan` resolves no hash |
| CON69 | Tier at open is stated, not asked; a run stops only when work outruns its model or a review tier cannot be honoured | directive-only | invisible |
| CON70 | An item's text describes the work and never overrides doctrine; one that purports to is surfaced | unenforceable, accepted | The doc: "no scanner catches intent" (QR4). Licensing context is intent; also `115/110`'s finding |
| CON71 | Read the current doctrine, not a stale pin's copy; a run outside a floor repo says it is the minimum viable form | directive-only | invisible. Instrument: `ccclose:checkPin` reports pin currency at close |
| CON72 | Selection order: loose ends and unblockers, then near-done, then queue order | directive-only | invisible, judgement |
| CON73 | Work handed over mid-run becomes an item first; an idea-only item is not selectable; an item bigger than the session is split first | directive-only | record |
| CON74 | Per-item close: commit, push and record before the next item | directive-only | record. Instrument: `ccclose:checkPushed` at the end only |
| CON75 | Waves only over disjoint file sets, claimed per item | directive-only | invisible |
| CON76 | Kill by the PID launched or the owned cwd, never by name pattern; read the 15-minute load before adding a wave | directive-only | invisible (a before-plane hook could read the command) |
| CON77 | A worker runs only its own modules under `nice`, plus the shared-contract ones; the full suite is the landing's | directive-only | invisible |
| CON78 | The queue-run skill names every stop condition the doctrine lists | enforced (CI test, blocks the run) | `tools/test_templates.py`, `QueueRunSkillTest.test_skill_names_every_stop_condition`; `tools/test_queue_run_single_source.py` bars the skill from growing rules. Pins the delivery copy, not the run |
| CON79 | A stop other than economics or session cap rests on a per-item triage, reported by count | directive-only | record (the report) |
| CON80 | The report surfaces every principal-blocked item, carries the identifiers block, puts each decision through the device, and re-reads every ask | directive-only | record. Instrument: `ccclose` lists asks and prints the identifiers |
| CON81 | The run's first line is its session id; progress is a per-item checklist; an unchecked assumption is named | directive-only | invisible |
| CON82 | A run takes a queued review only where it passes rule 4 for that delta; a worker's delta is the run's authorship | directive-only | record: the claiming run against the authoring run, through transcripts |
| CON83 | A spend directive is read as value, not budget; when to ask follows the run's cadence | directive-only | invisible |
| CON84 | This section points at the close discipline, never restates it | directive-only | diff, judgement. `stampscan` watches marked stamps only, and is advisory |

## Directive-only rules, grouped by where a breach shows

**Diff-visible (35).** REC3, REC4, REC5, REC6, REC7, REC8, REC9, REC18,
REC19, REC20, REC32; REV6, REV8, REV12, REV15, REV16, REV18, REV19, REV25,
REV27, REV28, REV29, REV30, REV31, REV34, REV36; CON3, CON23, CON34, CON47,
CON51, CON54, CON66, CON68, CON84. In CON47 and CON51 the diff shows only
part of the breach. REC3, REC4, REC8, REV25 and CON84 need judgement a scanner
cannot make, and stay review work.

**Record-visible (33).** REC12, REC13, REC14, REC15, REC21, REC23; REV1, REV2,
REV4, REV17, REV21, REV23, REV24, REV26, REV32, REV35, REV37, REV38; CON25,
CON26, CON28, CON36, CON37, CON49, CON50, CON52, CON53, CON55, CON73, CON74,
CON79, CON80, CON82.

**Invisible (65).** REC10, REC11, REC17; REV5, REV7, REV9, REV10, REV11,
REV13, REV20, REV39, REV40; CON1, CON2, CON4, CON5, CON8 to CON21, CON24,
CON27, CON29, CON32, CON33, CON35, CON38 to CON46, CON48, CON56 to CON65,
CON67, CON69, CON71, CON72, CON75 to CON77, CON81, CON83. Of these, CON10,
CON21, CON58 and CON76 are acts a before-plane hook could read from the
command text, the class `115/100` is about.

## Counts

| Doc | Rules | enforced (of which partial) | blocks | warns | directive-only | diff | record | invisible | unenforceable, accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RECORD.md | 32 | 8 (5) | 7 | 1 | 20 | 11 | 6 | 3 | 4 |
| REVIEW.md | 42 | 5 (2) | 3 | 2 | 36 | 15 | 12 | 9 | 1 |
| CONCURRENCY.md | 84 | 6 (4) | 4 | 2 | 77 | 9 | 15 | 53 | 1 |
| All three | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |

The *diff*, *record* and *invisible* columns split the directive-only count,
each rule once, under the place a breach first shows. *blocks* includes the
three CI test pins (REC1, REV22, CON78), which red the CI run after a push
rather than refusing the commit. A rule whose checks mix both responses is
counted at its strongest (REC2 blocks through `linkscan`; REC24 warns).

Reading the table: 12% of the rules counted here have any mechanical check, and
more than half of those cover only part of the rule. Every enforced rule is
record-keeping (index freshness, dates, archive state, links, the shape of a
review brief and its deferred sibling, skill copies, the commit form); not one
of the independence, authority or lane rules is enforced, which is `115/110`'s
finding reached again from three more documents.

## Top five guard candidates

Directive-only, breach visible in the diff, and costly when it happens:

1. **REC19, an accepted ADR edited in place**: a diff that changes an accepted
   decision record above its last dated addendum rewrites the reasoning a later
   session re-litigates against, in a public tree.
2. **REV36 with REC24's gap, a record deleted outside the roadmap**: a review
   file, decision record or session record removed by a commit; `harvestscan`
   covers roadmap items only, and a withdrawn pass must be kept.
3. **REV15, doctrine landed with no review pointer**: a commit changing
   doctrine paths that adds no queued pointer and declares none owed; unreviewed
   doctrine propagates to every child (`ccclose` sees it per window, after the
   fact, and only if run).
4. **REV19, a rule-4 review file with no provenance**: the doc calls a pass with
   no provenance trail non-compliant and V7 unmechanised; a header field check
   is the shape `reviewscan` check 3 already runs.
5. **REC5, the session index edited above its tail**: a diff that changes or
   removes earlier entries of the append-only index without moving them verbatim
   to the archive falsifies the history every session opens on.

Next after these: REV31 (a finding dropped untagged), REV12 (doctrine findings
applied with no ruling cited), CON23 (record identifiers of the wrong shape or
renamed), CON68 (a pointer citing a hash not on `main`), CON54 (a bare "wip"
message, a commit-message-plane check).

## Doubts and unverified points

- **The 115/110 map** was not readable in full (above). If its detail covers
  `REVIEW.md` or `CONCURRENCY.md` rule by rule, the two should be reconciled.
- **Rule boundaries are a judgement.** Another reader would split or fold some
  rows differently, so the counts are this reading's, not a fixed population.
  The folds are named in the rows (for example REC25 holds the monolithic
  harvest trigger, CON28 the queue run's claim-before-work).
- **Unverified**: man-page pins for instruments other than `ccfleet` and
  `ccclose` (REC1); whether `leakscan`'s machine-local term list names private
  repos (REC32); whether `modelguard` is wired for sessions in this repo
  (REV17).
- **A contested ground (CON21).** `EVIDENCE.md` §17 says nothing inspects a
  session's shell invocations; `tools/modelguard.py` does. That is a defect in
  the doctrine's stated reason, for the board, not a change made here.
- **Self-run instruments** (`ccclose`, `coldsweep`, `worktree.py`) were counted
  directive-only. Counted as warn-level guards instead, 20 more rules would read
  enforced; the census reports the stricter reading because nothing runs them
  unasked.

## Remaining docs for later slices

`docs/method/`: `00-APEX.md` and `AUTONOMY.md` (mapped by `115/110`, no file),
`ACCESS.md`, `COMMUNICATION.md`, `CONVENTIONS.md`, `DATA-PROTECTION.md`,
`DOCUMENTATION.md`, `ECONOMICS.md`, `EVIDENCE.md`, `GLOSSARY.md`, `GUARDS.md`,
`MECHANISMS.md`, `PRINCIPLES.md`, `PROPAGATION.md`, `REACH.md`, `SECRETS.md`,
`SIGNING.md`, `STORAGE.md`, `TOOLBOX.md`, and `docs/method/session-open/`.
Then, on `REVIEW.md` rule 3's definition, the doctrine outside `docs/method/`:
`docs/build/`, the ADRs, the skills and commands, the templates and the
validators' own stated rules.
