# Cold pass — the close declaration covers subagents, and ccclose's identifiers form

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** RAN 2026-10-25 UTC — PASS-WITH-FINDINGS, 0 MAJOR · 6 MODERATE · 9 minor ·
4 note (CV1–CV19); act 1 saved 22:08 UTC, act 2 (reconcile) saved 22:32 UTC, both by a
Fable 5.1 reviewer subagent under session `52e11d15` (Opus 5.5, orchestrator only; it
forms no finding). Brief written 2026-10-18 UTC by an Opus brief-writer that neither
authored the delta nor reviewed it.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/920-rule-4-cold-pass-queued-close-covers-subagents.md`.
**Why it earns a review:** it changes what "ready to close" must carry, in doctrine
every session reads at close, and adds the check that a session will cite as proof
that no agent is still running. Its worst failure is a ✅ on *Subagents finished*
while an agent is still live: the principal closes the tab on that signal and the
agent dies silently, which is the exact loss the rule exists to prevent. The
identifiers form prints a block designed to be pasted into records, some of them in
public repos, and every plain run now ends with it.

## Spawn provenance

- **Author of the work under review:** a Mike-opened Opus 5.5 queue run, 2026-10-18,
  which dispatched the Sonnet worker that wrote the code; the pointer counts the
  worker's output as the run's authorship. The same run widened the delta to the
  identifiers form, and the pointer was widened again on `main` (to `bdb1aba`) after
  this brief-writer's worktree was made. Not opened here beyond the pointer.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on
  2026-10-18 by a different Mike-opened Opus 5.5 queue run (worktree
  `atelier-qr-briefs-1018`), which authored none of this delta. This brief-writer
  authored none of it either. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief, its sibling, and
  one other brief pair (160/940).
- ⚠️ **Channel contact, disclosed by the orchestrator** (roadmap `280/040`). The
  dispatching run was started by the principal directly; the authoring session neither
  started nor instructed it. While this brief was being written, the authoring session
  (one session throughout, `e1d4097c`) sent that run's orchestrator one cross-session
  file-set notice: `ccclose` had changed under a parallel worker, rebase before merging,
  and which commits had landed and widened two pointers. It carried no view of any
  delta. The orchestrator also read the close section of the authoring session's record
  and, before landing it, this brief and its sibling. Weigh that as you see fit.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its dispatch prompt; `skills/review-brief/SKILL.md`; `docs/method/REVIEW.md`
  lines 55–234; the queue pointers 160/920 and 160/940 in full, 160/780 in full
  (including its recorded verdict line on another surface), the head of 160/870 (the
  earlier ccclose pass) and the head of 160/900; the earlier ccclose brief
  `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` lines 1–221 and its
  folded sibling, **and that file's heading outline, which carries the titles of its
  verdict's findings on ccclose** (a prior verdict on this tool, met for shape; its
  body was not read). Of the delta: `089fcdc` whole; `a738f85`'s design-note and
  README hunks; `4142efb`'s design-note hunk; `8b30ee6` whole; `bdb1aba`'s `RECORD.md`
  and man-page hunks — all read body-free
  through `tools/coldsweep.py --commit`, and subjects and stats only for every other
  commit named here. **No delta commit's message body was read.** It ran this brief's
  re-run lines once (below). It did not open the intent record, board items 210/280 or
  210/290, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `CHANGELOG.md`. Its harness also loaded the user-level and repo instruction files and
  a memory index. What its orchestrator read is the orchestrator's to disclose; it
  passed on a dispatch prompt naming the two pointers, a prefix suggestion, the
  pointer-append shape and one scope instruction (the out-of-scope line under *What
  the work is*), then one mid-task message saying the pointer had been widened to
  `bdb1aba` (named by id and subject), and no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff them; review the paths at `main`, `bdb1aba` or later — nothing
on `main` touched the delta paths after it at the time of writing):

- `089fcdc` (2026-10-18 00:23 UTC) — record: the close declaration names every agent
  the session launched (020/420 parts 2-3). `docs/method/RECORD.md` (the agents bullet
  under *The all-clear carries its evidence*) and `docs/method/CONCURRENCY.md` (the
  close-out measurement sentence).
- `a738f85` (2026-10-18 00:27 UTC) — ccclose: add check 12, subagents finished.
  `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
  `instruments/man/ccclose.1`, `instruments/README.md`.
- `4142efb` (2026-10-18 04:10 UTC) — ccclose: add --identifiers, the paste-ready
  identifiers block. The same instrument files except the README.
- `8b30ee6` (2026-10-18 04:10 UTC) — ccclose: print worktree paths under the home
  directory as ~/ in the identifiers block. `instruments/ccclose` only.
- `bdb1aba` (2026-10-18 05:06 UTC) — ccclose: a plain run ends with the identifiers
  block (210/300). `docs/method/RECORD.md` (the identifiers block's lead sentence),
  `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/man/ccclose.1`.

Read each body-free: `python3 tools/coldsweep.py --root . --commit <sha> [--path <p>]`
prints subject, stat and diff and never the message body. Plain `git show` is barred
here because it prints the body (the author's account) before the diff, and reading is
atomic (`REVIEW.md` rule 1).

**Commits on the same doctrine files that are not this delta.** Between `a738f85` and
`4142efb`, `140a190`, `1adf398`, `46320f8` and `6810b64` changed `RECORD.md` and
`CONCURRENCY.md`; they write the identifiers block's own doctrine text and are queued
pass 160/900's delta. The identifiers form here implements that text: test the code's
fidelity to it, but where a defect sits in the doctrine text itself, say so and leave
its charge to 160/900. The one exception is `bdb1aba`'s hunk in that same section of
`RECORD.md`, which is this delta.

**Later commits are out of scope.** Commits to these same files under board item
`210/290` (in flight while this brief was written, not on `main`) are not this delta
and carry their own queued pass; do not attribute them to it.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Check 12 against its design table.** The design note's *Subagents finished (12),
  precisely* section gives five states and the rule that combines them. Drive every
  state with a synthetic `subagents/` tree, and record which the code reaches and
  whether any input produces ✅ the table does not license.
- **What "finished" is read from.** The on-disk layout, the record shapes and the
  notification shapes the design names: are they the harness's real shapes, and were
  the fixtures derived from real transcripts or from the same reading that wrote the
  code? A shape the harness emits that the code does not read is a silent miss.
- **The doctrine bullet's claims.** `RECORD.md`'s new bullet makes a behavioural claim
  about the harness and an empirical one about past sessions. Re-drive what can be
  re-driven; mark the rest unverifiable with grounds. `CONCURRENCY.md` now names "the
  live agent list" as a measurement: what is that list, and can a session read it?
- **The identifiers form against its spec.** The seven fields, their order, the
  `none` and `by hand` rules, the commit-range rule, the board-change derivation, the
  worktree and branch reads, and the agents field — against `RECORD.md` § *The session
  log* at HEAD and the design note's §15. Since `bdb1aba` a plain run prints the block
  after its verdict: drive that path too, with `--json`, with a failing check and with
  reads that time out, and check the exit-code and field-set contracts still hold.
- **What the block carries into records.** Every field's source and what it can
  contain once pasted into a public record; the home-path rewrite and its edge cases;
  what `--json` keeps that the text form drops.
- **Mirror sites.** Every place the close declaration or `ccclose`'s check count is
  restated (skills, the session-open prompt, `TOOLBOX.md`, templates, the man page and
  `--help`): swept to match, or now claiming more or less than the tool proves.

**Non-goals:** the principal's asks that the close cover subagents and that the record
end with an identifiers block, which a plain run prints (quoted in their intent
records), the identifiers block's
doctrine text (160/900), and `210/290`'s later commits. The checks chosen, their states
and every word of the delta's own text are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that the agents directory beside a transcript is complete for the
   session; that the harness's notification records are a stable interface; that a
   live session's own running agents showing ❌ is the right answer rather than noise
   that trains sessions to ignore the line; that the identifiers form belongs in the
   close checker rather than its own tool.
2. **Correctness & quality.** Read the check-12 and identifiers code and tests whole;
   diff each build commit. Build a state table: one row per check-12 state and per
   identifiers field, with the input that reaches it and what prints.
3. **Completeness / harvest.** The design note against the code at HEAD, the man page
   and README against both, the doctrine sites in *Scope*, and any test the design
   promises that does not exist.
4. **Security & privacy** — mandatory. The tool reads every agent transcript and
   meta file beside the session's transcript and prints descriptions from them; the
   identifiers block is made to be pasted into public records; `--json` keeps absolute
   paths. Weigh each against the repo's purpose-based personal-data rule
   (`docs/build/REPO-STANDARD.md`). Never quote real transcript content in the
   verdict. `/security-review` is discharged by grounds (a landed delta; the pending
   diff is not the work) — say so, and do the code-altitude read by hand against the
   OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift invocations from `.github/workflows/ci.yml` rather than
guessing. Each line below was run once by the brief-writer and ran — the first three
both from its worktree root (at `f0d6238`, before `bdb1aba`) and from a `git archive`
export of `bdb1aba` in its scratchpad; nothing about their results is offered here.

- `node --test instruments/ccclose.test.js` (about 90 s on this machine), then the
  whole instruments suite once as CI runs it (`node --test instruments/*.test.js`),
  foreground, with a long timeout
- `mandoc -T lint -W style instruments/man/ccclose.1`; `node instruments/ccclose
  --help` by path
- live runs by path, never by bare name: throwaway git repos, a fake `HOME`, synthetic
  transcripts and synthetic `subagents/` trees in your scratchpad, `gh` stubbed through
  `CCCLOSE_GH`; drive each check-12 state and each identifiers field
- one run of `--identifiers` and of the full check against your own session in a
  scratch clone of this repo, after the throwaway runs; never against the shared
  checkout or another repo, and never paste its output into the verdict unredacted
- mutation, in a scratch clone: flip one load-bearing condition per check-12 state and
  per identifiers field, and record which tests fail
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, fixtures, mutated copies and older checkouts go in a private clone under
  your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: check `uptime` first, and run the
  instruments suite at most once whole, in the foreground. Never point a scanner or
  ccclose at any other repo on the machine. Never run an installed tool by bare name
  from `PATH`; instruments are symlinked onto it from another checkout.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address, personal detail or real
  transcript text — this repo is PUBLIC; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/` (one is on this same tool),
the queue pointer, this brief's sibling
`docs/reviews/2026-10-18-0506-close-covers-subagents-cold.deferred.md`, the landing
commits' message bodies, and the intent and commissioning items:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/420-the-close-declaration-does-not-cover-subagents.md`
- the whole of `docs/roadmap/210-instruments-open-features/`, which holds the
  identifiers form's commissioning items (210/280, 210/300) and the in-flight 210/290; barred as
  a directory so that no item filename is put in front of you here

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/920-rule-4-cold-pass-queued-close-covers-subagents.md
--also-exclude docs/reviews/2026-10-18-0506-close-covers-subagents-cold.deferred.md
--also-exclude
docs/roadmap/020-policy-as-code-programme-five-tracks-mik/420-the-close-declaration-does-not-cover-subagents.md
--also-exclude docs/roadmap/210-instruments-open-features <pattern>`;
`--include-barred` only with disclosure in the verdict. The generated index
`docs/ROADMAP.md` repeats item titles; read it no further than your onramp needs, and
disclose it if you do. Reading the delta is never barred; the design note and the
doctrine hunks are part of the delta.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the state table, findings with stable IDs (prefix
`CV`: `CV1`, `CV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions, the intent records and the prior verdict on this
tool, any finding formed at reconcile marked as such, and the overall line restated.
Never revise phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on doctrine, and on a tool that encodes it, are the principal's to decide
(rule 3): record all, apply nothing; counsel per finding is welcome, labelled and kept
beneath it.

---

# Verdict — cold pass run 2026-10-25 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 6 minor · 4 note** (CV1–CV13).
Act 1 first saved 2026-10-25 22:08 UTC and extended below under *Act 1 extensions*;
nothing above that heading was revised after the first save.

## Provenance (REVIEW.md rule 4, V7)

- **Reviewer:** a Claude Fable 5.1 subagent (`claude-fable-5-1`), the principal-named review
  tier, checked at selection. Spawned 2026-10-25 by session `52e11d15` (Claude Opus 5.5),
  which orchestrates, holds the context partition, forms no finding and writes no severity.
  That session authored neither the delta nor this brief, and was not started or
  instructed by session `e1d4097c` (the delta's author) or `8e498ef1` (the brief-writer's
  run). It was launched under the principal's approval of Fable work for the week ending
  2026-10-25 23:00 UTC. Arrangement: reviewer-plus-orchestrator, disclosed here before the
  findings as the 2026-08-17 ruling requires.
- **Worktree:** `~/worktrees/atelier-cold-160-920`, branch `atelier-cold-160-920`
  at `06c7966` (= `origin/main` at spawn). No git command that writes was run there. All
  probes, fixtures and mutated copies ran in clones under a fresh `/private/tmp` directory:
  `clone` (HEAD), `clone-bdb` (checked out at `bdb1aba`), `clone-mut` (mutations), `live`
  (a fake `HOME`, synthetic transcripts, a throwaway repo).
- **What was read before the findings:** this brief; `docs/method/REVIEW.md` whole; the
  five delta commits body-free through `tools/coldsweep.py --commit` (`089fcdc`,
  `a738f85`, `4142efb`, `8b30ee6`, `bdb1aba`); `RECORD.md` lines 60–170 and the
  CONCURRENCY hunk at HEAD; the instrument's helper functions at `bdb1aba`; the test
  file's fixture helpers; `instruments/README.md` by grep. No commit message body, no
  prior verdict, no session record, no roadmap item file and no `.deferred.md` was opened.
- ⚠️ **Exposure, disclosed.** Two `coldsweep` sweeps for mirror sites printed lines of the
  generated index `docs/ROADMAP.md`, which repeats item titles: those of `160/870`,
  `160/960`, and `210/280`, `290`, `300`, `310`, `320`, `330`. Two of those titles (`320`,
  `330`) each name a defect in `ccclose --identifiers`. Neither defect is in this delta's
  scope (`210/290`'s later commits carry them) and neither seeded a finding below; the
  findings here rest on probes run in this pass. The orchestrator's spawn prompt said the
  deferred sibling was removed from the tree; `git status` in the worktree shows that
  deletion, which is all this reviewer knows of it.
- **Delta paths at HEAD vs `bdb1aba`.** Three later commits (`0462173`, `621d18b`,
  `e78b6f1`, board `210/290`) changed all four instrument files after `bdb1aba` (+746/−52).
  The delta was therefore reviewed and exercised at `bdb1aba`; the floor and the whole
  suite were run at HEAD. Nothing from those later commits is attributed here.

## Lens 1 — approach and assumptions, named first and attacked

Load-bearing assumptions this reviewer named before reading the design's own list:

1. **The `subagents/` directory beside the transcript holds every agent of the session,
   including agents launched by agents.** Verified on the live store: 3,084 `.meta.json`
   files, 0 nested `subagents/` directories, 0 `agent-*.jsonl` outside a `subagents/`
   directory, and 287 metas with `spawnDepth` 2 or 3 — nested agents land in the top
   session's directory. Holds.
2. **The parent transcript records the end of every agent in that directory.** Holds for
   background agents at any depth (36 of 36 finished depth-2 background agents had their
   `<task-notification>` echoed into the session transcript). **Does not hold for a nested
   foreground agent**: its `tool_result` lands in the parent *agent's* file, which the tool
   never opens (24 depth-2 foreground metas store-wide) — CV6.
3. **The harness's record shapes are a stable interface.** False on the store's own
   history: `requestShape` is absent on 1,318 of 3,084 metas and `finished` is present on
   only 382, so the meta the design describes as four fields has changed twice, and the
   code reads neither change — CV1. The three notification carriers the design names are
   the three that open with the tag in the live store (`queue-operation` enqueue 9,
   `queued_command` attachment 4, plain `user` 5 in one real session; `queue-operation`
   remove, `prompt_snapshot`, `api-request-*` also carry the text but do not open with it,
   and the code rightly ignores them).
4. **A live session's own running agents showing ❌ is the right answer.** Accepted: the
   question is "ready to close?", and an agent still running is the one case the rule
   exists for. The risk the brief names — that noise trains sessions to ignore the line —
   comes instead from ⚠️ rows the session cannot clear: an older session's foreground
   agents (CV1) and nested foreground agents (CV6) both read as "result never consumed"
   whatever the session does.
5. **The identifiers form belongs in the close checker.** Accepted with one cost: the form
   inherits the checker's `gh` seam, and so inherits its misdiagnosis of a timeout as
   absence, now written into a pasted record — CV3.
6. **The block is safe to paste into a public record.** Not fully: `8b30ee6` weighed the
   home-directory path and nothing weighed the agent descriptions, which are free text
   written by the spawning agent. 50 of 3,084 descriptions in the store carry a
   private-repo or household token (count only; none is quoted) — CV2.
7. **The design's "launched in the window holds by construction".** Holds: the window is
   the transcript's span and the directory is the session's.

The brief's account of *what the work is* checked out against the commits: five commits,
the files named, and `bdb1aba`'s `RECORD.md` hunk is indeed the one sentence in the
identifiers section that this delta owns.

## Lens 2 — correctness and quality

Code and tests read whole at `bdb1aba`; every build commit diffed. The state table is
below. Points beyond the table:

- `judgeAgent` matches its design table in every row driven (14 synthetic agents, all five
  states plus the sub-cases: resumed-and-cut, completed-but-short, unknown status,
  foreground with and without `tool_result`, no meta, no records yet, a `finished: true`
  meta over a cut transcript). No input produced a ✅ the table does not license.
- The summary count folds two different things into "finished, result never consumed":
  an agent whose notification carried a status the tool does not know (`failed` in the
  probe) and an agent with no meta. The per-agent line is right; the count's label is
  not — CV5.
- The fixtures' "cut" shape is `stop_reason: null` with a `tool_use` block; the one
  in-flight agent in the real store ends on `stop_reason: "tool_use"`. The code reads
  both as cut, so this is a fixture-fidelity note, not a defect — CV10.
- `--identifiers` exit 0, the seven fields in `RECORD.md`'s order, `none` and `by hand`
  rules, the `first^..last` range (verified as a real git range in the test and by hand),
  the board derivation, worktree and branch reads, and the agents field all behaved as
  specified at `bdb1aba`. The plain run ends with the block after the verdict and keeps
  exit 1 on a failing check; `--json` on the plain run keeps the checks alone, and
  `--identifiers --json` keeps the absolute path (as designed).
- The commit-range read is the window heuristic; its attribution weakness is `210/290`'s
  (later commits) and is not charged here.

## Lens 3 — completeness and harvest

- Design note vs code at `bdb1aba`: the §12 table, the *Subagents finished (12),
  precisely* section and §15 describe the code as built, with the two omissions in CV1
  (meta fields the harness writes that the design does not list) and CV6 (depth).
- Man page and `--help`: both say twelve checks and both document `--identifiers`;
  `mandoc -T lint -W style` is clean at `bdb1aba` and at HEAD; `--help` is 19 lines and
  the drift guard (every `--help` flag in the man page) is in the suite.
- Mirror sites swept: `instruments/README.md` (twelve; the identifiers block is mentioned
  at HEAD), `TOOLBOX.md` (lists the tool, states no count), `skills/`, `templates/`,
  `CLAUDE.md`, `docs/build/` (no restatement of the close declaration or the check count
  found). `RECORD.md` and `CONCURRENCY.md` restate the close's agent evidence in two
  phrasings — CV7.
- Tests the design promises that do not exist: none promised by name; the ones the design
  implies and the suite lacks are the `~/` rewrite (CV4) and the unknown-status row (CV5),
  both confirmed by mutation below.

## Lens 4 — security and privacy

- `/security-review` is **discharged by grounds**: the work is a landed delta and the
  pending diff in the worktree is this brief; the scanner reads the pending diff, and
  running it would have fed this brief's text back into the reviewer. Not run.
- Code-altitude read by hand against the OWASP Top 10 (2021) for this class (a local CLI
  that reads JSON lines and shells out):
  - **Injection (A03):** every subprocess is `execFile`-style with an argument array; the
    only text the tool parses from the transcript into command-shaped output is read, not
    executed (`shellWords`, `worktreeAdds`, `ghPrCommands`). Clean.
  - **Path handling:** the agents directory is derived from the transcript's own path, so a
    `--session <path>` points the tool at that file's siblings only; `resolveFrom` expands
    `~` and relative paths for *display and existence checks*, never for writes. Clean.
  - **Sensitive data exposure (A02/A04 design altitude):** the tool reads every agent
    transcript and meta beside the session and prints descriptions — CV2 (MODERATE). The
    `~/` rewrite covers the worktree path in the block but not check 1's list two screens
    above it in the same plain run — CV4.
  - **Logging/monitoring (A09):** a `gh` timeout is recorded as "gh is not installed" —
    CV3 (a claim stronger than its evidence, written into a record).
  - A07/A05/A08 (auth, misconfiguration, integrity): no network of its own; `gh` is reached
    through `CCCLOSE_GH` or `PATH`, pre-existing seam, unchanged by this delta.
- Threat enumeration at design time: the design note names the public-record paste as the
  threat for paths (`8b30ee6`) and nothing else. The missing enumeration for descriptions
  is the finding (CV2), the same shape as a missing `review:` line.
- Repo purpose-based personal-data rule (`docs/build/REPO-STANDARD.md`): the block names a
  session id, models, short shas, PR numbers, board ids, `~/`-relative paths and agent
  descriptions. Only the last carries free text from a human-adjacent source.

## Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** Bites twice: CV3 (timeout printed as
  absence) and CV8 (the doctrine bullet's empirical claim, which this pass could not
  re-drive in act 1 because its source is barred).
- **V2 — re-run every live-proven claim.** Done; ledger below. All reproduced.
- **V3 — swept to every mirror site.** Swept; one restatement issue, CV7.
- **V4 — one fact, one home.** CV7 (two phrasings of "the agent list").
- **V5 — no internal contradiction.** `RECORD.md` says the plain run prints the block;
  the man page adds that `--json` keeps the checks alone. Not a contradiction (`--json` is
  not the plain run) — noted, no finding. The design's "three ways" and the store's
  fourth signal (`meta.finished`) are CV1.
- **V6 — security and privacy.** Lens 4 above; CV2, CV3, CV4.
- **V7 — spawn provenance stated.** In the brief (lines 19–43) and above.

## State table

Check 12, one row per state, driven at `bdb1aba` in the `live` world (14 agents):

| State | Input that reached it | Printed |
|---|---|---|
| ✅ reported | finished, `completed` via enqueue / attachment / user | `reported (completed notification)` |
| ✅ reported (fg) | foreground, finished, `tool_result` on launch | `reported (tool_result on the launch)` |
| ✅ stopped | cut transcript, `killed` via user record | `stopped on purpose (killed notification)` |
| ⚠️ unconsumed | finished, no notification | `finished, but the parent has no notification …` |
| ⚠️ unconsumed | foreground, finished, no `tool_result` | `… the parent has no tool_result …` |
| ⚠️ unconsumed | `completed` note, transcript short, no later records | `a completed notification, but … short of end_turn` |
| ⚠️ unconsumed | note with status `failed` | `notified with status "failed", which ccclose does not know` |
| ⚠️ unconsumed | no `.meta.json` | as the first ⚠️ row, `(no description)` |
| ⚠️ unconsumed | note text prefixed by a banner | as the first ⚠️ row (the note is not seen) — CV9 |
| ❌ cut | last assistant `stop_reason: "tool_use"`, no note | `cut mid-flight: last turn is a tool_use …` |
| ❌ cut | `completed` note, records after it, ends short | `resumed after its completed notification and cut …` |
| ❌ cut | empty agent file | `cut mid-flight: no assistant turn yet` |
| ❌ cut | `finished: true` in meta, transcript cut | as the first ❌ row (the flag is unread) — CV1 |
| ➖ | no transcript / no `subagents/` | tested in the suite; counts `null` / known zeros |

Identifiers fields, one row each, at `bdb1aba`:

| Field | Input | Printed |
|---|---|---|
| Session | id, one model, window | `sess-live · Opus 5.5 · <from> to <to> UTC` |
| Commits | one commit in window | `(1): <short>`; three unbroken → `· unbroken, a^..c` (suite) |
| Pull requests | no GitHub remote | `none (no GitHub remote, so states are unknown)` |
| Pull requests | `gh` sleeping 25 s | `none (gh is not installed, …)` after 20.4 s — CV3 |
| Board | no board | `by hand — this repo has no board` |
| Worktrees | `git worktree add` under the fake home | `~/wt-under-home (branch …) — worktree still present; branch kept, merged` |
| Agents | the 14 above | counts line, then every agent, uncapped, problems first |
| Other repos | — | `not read by ccclose — fill in by hand` |

## Findings

- **CV1 — MODERATE. The meta and notification shapes are read as if fixed; the store's own
  history shows them moving, and the code has no guard or fourth signal.** Evidence:
  3,084 metas; `requestShape` absent on 1,318 (so every foreground agent of an older
  session reads as "finished, result never consumed" because `foreground` is false and the
  `tool_result` is discounted); `finished` (a harness-written boolean) present on 382 and
  on 7 of the 8 agents of the live session that spawned this reviewer, absent exactly on
  the one still running; `spawnDepth`, `agentType`, `requestNonInteractive`, `isBuiltIn`
  also present. The design note lists four meta fields and "three ways" the parent records
  an end. Rows affected: the ❌/⚠️ split for any agent where `finished` and `stop_reason`
  disagree (one synthetic case driven: `finished: true` over a cut transcript prints ❌).
  *Counsel:* read `meta.finished` as a signal and say when it disagrees with the
  transcript; treat a missing `requestShape` as "shape unknown" and say so rather than
  defaulting to background; add one fixture per observed meta shape, derived from a
  field-allowlisted census of the real store, so the next shape change fails a test.
- **CV2 — MODERATE. Agent descriptions are printed into a block designed to be pasted into
  public records, and nothing weighed them.** Evidence: 50 of 3,084 descriptions in the
  store carry a private-repo or household token (8 distinct tokens; count only, nothing
  quoted); the probe's description naming a person printed verbatim in the plain run and
  in the block. The delta's own privacy step (`8b30ee6`) covers the home path only.
  *Counsel:* print short id and end in the text block by default and the description only
  under a flag (or clipped to the first three words); say in `RECORD.md`'s *record is
  public* section that the agents list is reviewed like any other free text before paste.
- **CV3 — MODERATE. A `gh` that does not answer within 20 s is written into the record as
  "gh is not installed".** Evidence: a stub that sleeps 25 s produced `none (gh is not
  installed, so states and open PRs are unknown)` in the identifiers block and `unknown —
  gh is not installed` in check 4, both after 20.4 s. `ghReady` predates this delta (its
  wording belongs to the earlier pass's scope), but the identifiers form is new and is the
  surface that pastes the false statement into a durable record. *Counsel:* distinguish
  `status === null` with `ETIMEDOUT` from a missing binary (`ENOENT`) and print "gh did
  not answer in 20 s"; the identifiers note should never assert absence it did not see.
- **CV4 — minor. The `~/` rewrite has no test and covers one of the two places the same
  path prints.** Evidence: mutation M10 (rewrite disabled) is pending in the ledger below;
  in the plain run check 1 printed the absolute path under the fake home while the block,
  two screens later, printed `~/…`. *Counsel:* a test with a worktree under the fake
  `HOME`; apply the rewrite to check 1's items or state in the man page that only the
  block is paste-safe.
- **CV5 — minor. The summary count labels an unknown-status agent and a meta-less agent as
  "finished, result never consumed".** The per-agent lines are right. No test drives the
  unknown-status row of the design table (mutation M15 pending). *Counsel:* a fifth count
  ("other"), or the word "or unknown" in the label; one test with a `failed` status.
- **CV6 — minor. A nested foreground agent's end is read from the wrong file.** The
  `tool_result` on a depth-2 agent's launch lands in its parent agent's transcript, which
  the tool does not open; 24 such metas exist store-wide; background nested agents are
  fine (36 of 36 echoed to the session transcript). The design does not mention depth.
  *Counsel:* when `spawnDepth > 1`, also scan the sibling agent files for the launch's
  `tool_result`, or print "nested — end read from the session transcript only".
- **CV7 — minor (doctrine; the principal's to decide, rule 3). "The live agent list" is
  named as a close-out measurement in `CONCURRENCY.md` without saying what it is.**
  `RECORD.md` says "the agent list at that moment" and names `ccclose`'s check as its
  reader; `CONCURRENCY.md` names neither. There is no harness command that lists live
  agents; the only reader is the on-disk store via `ccclose`. V4: one fact, two phrasings.
  *Counsel:* `CONCURRENCY.md` says "the agent list (`ccclose`, check 12)".
- **CV8 — note (doctrine). The `RECORD.md` bullet's empirical claim (30 sessions read;
  every close made with no agent running; eleven agents cut by a host crash) was not
  re-driven in act 1**: its source is the intent record, barred until act 2. What was
  re-driven: the behavioural half is consistent with the store (the one agent still running
  has no `finished` flag and no notification, which is exactly the state a closed tab would
  freeze). Extended below if act 1's time allows; otherwise carried to the reconcile.
- **CV9 — note. The carrier test is an exact prefix (`startsWith('<task-notification>')`
  after `trimStart`).** Every real carrier in the live session's transcript opens with the
  tag (5 of 5 user records, 9 enqueues, 4 attachments), so nothing is missed today; a
  harness that prepends a banner to the stored text (the in-context shape a subagent
  receives already carries one) would turn every background agent into ⚠️ silently.
  Fragility, not a defect; worth one line in the design note.
- **CV10 — note. Fixture fidelity.** The fixtures are synthetic, written from the same
  reading that wrote the code; their three carriers match the store, their "cut" shape
  (`stop_reason: null`) does not match the store's in-flight shape (`"tool_use"`), and
  they omit the meta fields in CV1. The code's behaviour is the same on both cut shapes.
- **CV11 — minor. `requestShape` absent is treated as background without saying so.**
  The sub-case of CV1 that produces a wrong ⚠️ on 1,318 metas' worth of older sessions;
  listed apart because its fix is one line (`shape unknown` in the end text).
- **CV12 — minor. The design's "An empty directory is a known zero and passes" is right,
  but the `--identifiers` agents field prints `0 · none launched` for both an empty
  directory and no directory**, which are different facts (the check distinguishes them
  as ✅ and ➖). Mutation M23 pending. *Counsel:* `0 · no agents directory` for the latter.
- **CV13 — note. Non-goals reviewed.** The brief fences off the principal's two asks, the
  identifiers doctrine text (`160/900`) and `210/290`. None fences a risk this delta
  carries: CV2 and CV3 sit squarely inside the delta's own code. The narrowing is sound.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (CV1, CV2, CV3) · 6 minor (CV4, CV5, CV6,
CV7, CV11, CV12) · 4 note (CV8, CV9, CV10, CV13).** The worst failure the brief names — a
✅ on *Subagents finished* with an agent still live — was not reproducible: every cut or
in-flight shape driven printed ❌. The findings are about ⚠️ rows a session cannot clear,
a false statement a record can carry, and free text pasted into public records.

## Re-run ledger (act 1, first save)

| Claim / command | Where | Result |
|---|---|---|
| `node --test instruments/ccclose.test.js` | `clone-bdb` at `bdb1aba` | 52 pass · 0 fail · 56.5 s |
| `mandoc -T lint -W style instruments/man/ccclose.1` | `bdb1aba` and HEAD | clean, exit 0, both |
| `node instruments/ccclose --help` by path | `bdb1aba` and HEAD | 19 lines; points at `man ccclose` |
| Every check-12 state, synthetic `subagents/` tree | `live` world, `bdb1aba` | 14 agents; table above; exit 1 |
| Plain run, `--json`, `--identifiers`, `--identifiers --json` | `live`, `bdb1aba` | field sets stable; exits 1/1/0/0 |
| `gh` timing out (stub sleeps 25 s) | `live`, `bdb1aba` | 20.4 s; printed "not installed" (CV3) |
| Worktree under the fake `HOME` | `live`, `bdb1aba` | `~/` in the block; absolute in check 1 (CV4) |
| Store census (keys/types only, no content) | real store, read-only | figures in CV1, CV2, CV6 |
| Whole instruments suite as CI runs it | HEAD | pending — see extensions |
| `tools/floor.py --plane ci --root .` and the hook plane | HEAD | pending — see extensions |
| Mutations (22), one condition per state/field | `clone-mut` at `bdb1aba` | running; ledger in extensions |
| `ccclose` against this reviewer's own session | scratch clone | pending — see extensions |

## Follow-up checklist

- [ ] CV1 — read `meta.finished`; treat missing `requestShape` as unknown; shape fixtures
      from a censused store.
- [ ] CV2 — descriptions out of the default text block, or clipped; a line in `RECORD.md`.
- [ ] CV3 — `gh` timeout named as a timeout, never as absence.
- [ ] CV4 — a `~/` test; one rule for both places the path prints.
- [ ] CV5 — an "other/unknown" count and a `failed`-status test.
- [ ] CV6 — nested foreground agents: read the parent agent's file or say it was not read.
- [ ] CV7 — `CONCURRENCY.md` names the reader of "the live agent list" (principal's call).
- [ ] CV8 — re-drive the 30-session claim at reconcile.
- [ ] CV12 — distinguish "no directory" from "empty" in the agents field.

## Act 1 extensions (written after the 22:08 UTC save; nothing above revised)

### Extension 1 — the harness's status vocabulary (saved 22:11 UTC)

A store-wide census of `<status>` values inside `<task-notification>` blocks (6.6 GB,
read-only, values only): `completed` 33,697 · `failed` 1,385 · `killed` 315 · `stopped`
63 · `running` 26 · one stray `Up` (tool output, not a notification). Those counts include
background shell tasks, so the follow-up asked which are keyed to an *agent* id (a
`<task-id>` matching an `agent-<id>.jsonl` beside that session's transcript):

- `running`: **never** keyed to an agent. It is a shell-task status. The MAJOR this
  reviewer was testing for — a live agent whose `running` note makes check 12 ⚠️ and the
  run exit 0 — does not occur in the store. Cleared.
- `failed`: keyed to an agent **205 times** in session transcripts (95 `queue-operation`
  enqueues, 68 plain `user` records, 42 `queued_command` attachments), plus 25 removes and
  43 request blobs the code rightly ignores. So `failed` is a status the harness emits for
  agents, often, and the design table lists only `completed`, `killed` and `stopped`.

**CV5 is raised from minor to MODERATE on this evidence**, and its statement widens: the
design's status vocabulary omits `failed`, which the harness emits for agents; the code's
"which ccclose does not know" branch is the only thing that keeps a failed agent from
reading as finished, and the summary count then files it under "finished, result never
consumed". The ⚠️ is right for the close question (a failed agent is not running), the
label and the design are wrong, and no test drives the row. *Counsel:* add `failed` to the
known set as its own state ("failed — the parent was told; the result is an error, not
a report"), count it apart, and keep the unknown-status branch for whatever comes next.

**CV14 — minor (new). The suite never drives the store's real cut shape.** Mutation M2
(`finished` = any non-null `stop_reason`) passed all 52 tests, because every "cut" fixture
ends on `stop_reason: null`; the real in-flight agent ends on `"tool_use"`. The shipped
code is right (`=== 'end_turn'`); a regression toward "anything non-null is finished"
would turn a live agent into ⚠️ and the suite would not notice. This is CV10 given teeth.
*Counsel:* one cut fixture with `stop_reason: "tool_use"`, one with `"max_tokens"`.

**Tally after extension 1: 0 MAJOR · 4 MODERATE (CV1, CV2, CV3, CV5) · 6 minor (CV4,
CV6, CV7, CV11, CV12, CV14) · 4 note (CV8, CV9, CV10, CV13).**

### Extension 2 — mutation ledger and the floor (saved 22:24 UTC)

Twenty-two mutations, one load-bearing condition each, applied to a scratch copy of
`instruments/ccclose` at `bdb1aba`, the full test file run after each (49–61 s a run,
one at a time). **18 caught, 4 survived.**

| Mutation | Caught by |
|---|---|
| M1 `STOP_STATUS` drops `killed` | 1 test (every agent reported or stopped) |
| M2 finished = any non-null `stop_reason` | **none** — CV14 |
| M3 every agent treated as foreground | 1 test (state sort; `f6666666`) |
| M4 resume comparison inverted | 1 test (resumed and cut again) |
| M5 a cut agent only warns | 2 tests |
| M6 `queue-operation` carrier dropped | 3 tests |
| M7 opens-with-tag guard dropped | 1 test (`taskNotifications`) |
| M8 commit range loses the `^` | 1 test (`first^..last`) |
| M9 claimed lists released claims | 1 test (board groups) |
| M10 `~/` rewrite disabled | **none** — CV4 confirmed |
| M11 `--identifiers` exits 1 | 2 tests |
| M12 failed commands count | 2 tests (worktrees; PRs) |
| M13 identifiers agents capped | 1 test |
| M14 block printed before the verdict | 1 test (210/300) |
| M15 unknown status passes as reported | **none** — CV5 confirmed |
| M17 `⏳` not counted | 1 test |
| M18 `EnterWorktree` ignored | 1 test |
| M19 other-repo PR count dropped | 1 test |
| M20 `tool_result` user records count as carriers | 1 test |
| M22 completed counted when already `[x]` | **none** — CV15 below |
| M23 empty `subagents/` reported not applicable | 1 test (the check); the identifiers field's `0 · none launched` for both cases stays untested — CV12 |
| M24 problems not sorted first | 2 tests |

**CV15 — minor (new). A board item already `[x]` before the window whose first line is
rewritten (still `[x]`) inside it would be counted as *completed* by the session.** Mutation
M22 passed every test because `boardWorld()` never re-touches a closed item. The shipped
code checks `before !== 'x'`, so the behaviour is right; the guard is unprotected.
*Counsel:* one fixture commit that edits a closed item's first line in the window.

**Floor at HEAD (`06c7966`), scratch clone:** `tools/floor.py --plane ci --root .` exit 0,
every enforced scanner ✅ (leakscan 🟡 "cover not guaranteed", the ci plane's standing
note); `--plane hook --root . --tools ./tools`, as `.githooks/pre-commit` invokes it, exit
0. Both reproduce the delta's standing claim that the floor is green.

**This reviewer's own session, HEAD clone, `--root` the clone:** check 12 ❌ with 8
agents · 7 reported · 1 cut (the cut one is this reviewer, still running), exit 1; the
identifiers block printed 7 fields, no absolute home path, three `~/` paths. The correct
answer to "ready to close?" for a session with a live reviewer. Output not pasted.

**Tally after extension 2: 0 MAJOR · 4 MODERATE (CV1, CV2, CV3, CV5) · 7 minor (CV4,
CV6, CV7, CV11, CV12, CV14, CV15) · 4 note (CV8, CV9, CV10, CV13).** Still pending in
act 1: the whole instruments suite at HEAD (running) and a re-drive of CV8's population.

### Extension 3 — the whole suite, and CV8 re-driven (saved 22:27 UTC)

**Whole instruments suite at HEAD, as CI runs it** (`node --test instruments/*.test.js`,
foreground in the scratch clone, once): 492 tests · 492 pass · 0 fail · 86.2 s.

**CV8 re-driven as far as the store allows** (every `agent-*.meta.json` and `.jsonl` under
351 sessions, keys only; "noted" = the session transcript holds a `<task-notification>`
with the agent's id):

| Transcript ends | `finished` flag | Noted in parent | Agents |
|---|---|---|---|
| `end_turn` | absent | yes | 2,372 |
| `end_turn` | `true` | yes | 298 |
| short of `end_turn` | absent | yes | 197 |
| `end_turn` | absent | no | 113 |
| `end_turn` | `true` | no | 64 |
| short of `end_turn` | `true` | yes | 23 |
| short of `end_turn` | absent | no | 11 (one is this reviewer, live) |
| short of `end_turn` | `true` | no | 6 |

- The bullet's shape reproduces: agents cut and later *told to the parent* (197) are
  common and are what a resumed session sees; agents cut and never told (10 historical,
  in 9 sessions) are rare. Whether those 9 sessions were closed on a declaration or died
  with the host the store cannot say, so "every close made with no agent still running"
  is neither confirmed nor refuted here; the exact 30-session and eleven-agent figures
  are the intent record's and wait for act 2. CV8 stays a note.
- **CV1 gains evidence:** 29 agents (23 noted, 6 unnoted) carry `finished: true` while
  their transcript ends short of `end_turn`. For the 6 unnoted ones the tool prints ❌
  *cut mid-flight* for an agent the harness itself marked finished; for the 23 it prints
  ⚠️. The flag and the transcript disagree in the store today, and the tool reads only
  one of them. Severity unchanged (MODERATE); the counsel to read the flag and *say when
  the two disagree* is now grounded in 29 cases rather than one synthetic one.

**Final act-1 tally: PASS-WITH-FINDINGS — 0 MAJOR · 4 MODERATE (CV1, CV2, CV3, CV5) ·
7 minor (CV4, CV6, CV7, CV11, CV12, CV14, CV15) · 4 note (CV8, CV9, CV10, CV13).**

**Re-run ledger, closed for act 1** (the four rows left pending at 22:08):

| Claim / command | Where | Result |
|---|---|---|
| Whole instruments suite as CI runs it | HEAD, scratch clone | 492 pass · 0 fail · 86 s |
| `floor.py --plane ci` and `--plane hook … --tools` | HEAD, scratch clone | exit 0 and exit 0 |
| Mutations (22) | `bdb1aba`, scratch copy | 18 caught · 4 survived (M2, M10, M15, M22) |
| `ccclose` and `--identifiers` on this reviewer's own session | HEAD clone | ❌ 1 cut (the live reviewer); block clean of home paths |
| CV8 population | real store, keys only | table above |

Scratch state left behind, all under one fresh `/private/tmp` directory and none of it in
the worktree: three clones, the `live` world, the ledger and census text files. No file
other than this brief was written in the worktree; no git command that writes was run
there. Act 1 ends here; `### Reconcile` follows once the sibling is handed over.

*One edit to phase-1 text after the 22:08 save, disclosed: the worktree path in
*Provenance* was redacted from its absolute form to `~/…` at 22:27 UTC, because this
repo is public and the absolute form names an account — the same rule `8b30ee6` applies
to the block. No finding, severity or other word above was changed.*

---

# Act 2 — Reconcile (opened 2026-10-25 22:27 UTC, on the orchestrator's release)

The sibling was read from the orchestrator's held copy after act 1 was saved and
reported; the fold-in is the orchestrator's. Also opened in this act, as rule 2 permits
once findings are durable: the intent record `020/420`, the commissioning items `210/280`
and `210/300`, the five landing commits' message bodies, and the prior verdict on this
tool, `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` (its findings CL1–CL24
and Overall; it carries no `[fixed]`/`[backlog]`/`[rejected]` tag, so every CL stands
undecided). `210/290` and the cctranscript-search verdict were not opened. Nothing in
act 1 was revised; every change to an act-1 finding is stated here beside it.

## The seeded questions, one by one

1. **`tildePath` edge cases; other fields carrying names.** Probed at `bdb1aba`: with
   `HOME` carrying a trailing separator the block printed the absolute path; with `HOME`
   a symlink to the real home it printed the absolute (realpath) form too. Both defeat
   the rewrite silently. **CV4 widens** to these two cases (severity unchanged, minor; the
   fix is `path.resolve`/`realpath` on both sides). Other fields: PR numbers, board ids
   and short shas carry nothing; branch names are free text and print as typed; agent
   descriptions are CV2; the `Session` line prints model names only.
2. **Descriptions pasted whole; does doctrine say look first?** CV2 stands and
   strengthens. `RECORD.md` lines 118–123 record that the *Agents* field was the agent's
   recommendation, not the principal's ask, and `bdb1aba` then moved the block into every
   plain run (the principal's ask was for the block, not its contents). `RECORD.md` § *The
   record is public* regulates the name-to-posture join for private repos; it says
   nothing about free text copied from a tool's output, so no, doctrine does not tell the
   session to look before pasting. Counsel unchanged, with that sentence added.
3. **Can a genuinely done session get ✅?** Not always. Inputs that deny it: run from
   inside its own worktree (prior CL21, check 1); any nested foreground agent (CV6); any
   foreground agent on an older-shaped meta (CV11); any agent whose last record is a
   streamed partial despite a `completed` notice (CV16, below, 118 real cases); a
   subagent running the check sees the parent's session and itself as cut. The design's
   "that is the intended answer" covers the live-agent case only. The push to discount
   the line is real and is why CV16 is rated as it is.
4. **Resume, compaction, max-tokens, error stops.** Store census of agents whose last
   assistant record is not `end_turn` (values only): `null` + text 129 · `stop_sequence`
   52 · `tool_use` 33 · `null` + `tool_use` 14 · `null` + thinking 7 · `refusal` 1. Cross
   with the parent's notice: **118 of the `null`+text agents were notified `completed`**
   — the tool prints ⚠️ *a completed notification, but its own transcript stops short of
   `end_turn`* for every one; 44 of the 52 `stop_sequence` agents were notified `failed`
   (CV5). A `SendMessage` resume is handled (last record governs; tested). Compaction
   left no shape this census could separate. **CV16 below.**
5. **The 30-session read.** The intent record holds the figures (30 sessions, 21 closed,
   240 agents, about 35 close claims, 11 agents in 4 sessions cut by the host crash of
   2026-10-16 07:35 UTC, each seen only because the session was resumed, and one
   `TaskStop` case). Act 1's store-wide re-drive is consistent in shape: 197 agents cut
   and later told to a resumed parent, 10 historical agents cut and never told. The exact
   24-hour slice was not re-counted. **CV8 closes as consistent** (remains a note; its
   open half is now answered). The record supports "every close made with no agent still
   running" for that slice; the store cannot extend it to every close since.
6. **"The live agent list" across harnesses.** Claude Code writes the store this tool
   reads; the prior pass (CL23) saw a store on a cloud host too; the SDK was not checked.
   `ccclose` is the only durable reader found. CV7 stands; the counsel now says the
   doctrine should name the reader, and say "where the store exists".
7. **Record vs verdict where the block is pasted.** The man page says `--identifiers`
   "is a record, not a verdict" and exits 0; `RECORD.md` says only that `ccclose` prints
   the block after its checks. A session pasting the block is not told that the block is
   not the close's evidence. **CV18 below** (doctrine, the principal's).
8. **The commit range on a rebased series.** The delta's own chain: `4142efb` (parent
   `6810b64`, a doctrine commit), `8b30ee6` (committer time ten minutes after its author
   time, rebased), `bdb1aba` (parent `12e6d9b`). The chain test is on parents, not dates,
   so a rebased linear series still prints `first^..last`, and the range is a true git
   range over those commits. The truth risk is a rebase by a *later* session moving the
   committer time into that session's window — `210/290`'s territory, not charged. But
   the probe for this question surfaced **CV19 below**.
9. **`bdb1aba`'s mirrors.** Design §10 at `bdb1aba` and at HEAD still ends the output at
   "one verdict line"; §15 still says `--identifiers` runs none of the checks (true, but
   silent on the plain run). The README at `bdb1aba` described twelve checks, asks and a
   verdict and no block; HEAD's README mentions the block, by a `210/290` commit. **CV17
   below.** This corrects act 1's lens 3, which said the design describes the code "as
   built": it does for check 12 and §15, not for §10.
10. **Opt-in to default.** Yes: `bdb1aba` put agent descriptions and worktree paths into
    every plain run's output without a choice about their content; the only privacy step
    in the delta (`8b30ee6`) predates that move and covers one field. Folded into CV2.

## Against the intent record and the commissioning items

- The intent record specifies the layout, the four meta fields, the three carriers, the
  foreground `tool_result` and the states exactly as built; the code is faithful to its
  spec. The shapes came from the author's read of real transcripts (the 30-session
  census), so **CV10 is corrected**: the fixtures derive from a real read, not from
  invention; the finding narrows to "the cut fixture's shape (`null` stop) is one of the
  real shapes but not the in-flight one, and the suite proves neither" (CV14).
- The record's close note says: the `finished` field some real metas carry **is ignored
  by judgement**, because the item defines "finished" from the agent's own transcript.
  **CV1 is reframed, severity unchanged (MODERATE):** the field is not unknown to the
  author; the judgement is recorded in the board item and nowhere a reader of the tool
  or its design note meets it, and the store now shows 29 agents where that judgement
  and the harness disagree, plus 118 (CV16) where the transcript-only definition
  mislabels a completed agent. The judgement was a reasonable default on 2026-10-18;
  the evidence here is what tests it, and it should be carried into the design note
  with the disagreement surfaced per agent.
- `210/280` says the home-path rewrite lets the block "go into a public record"; act 1
  (CV2, CV4) and question 1 show that claim covers one field under one `HOME` shape.
- `210/300` records that the plain-run change was the principal's ask and that "the
  accuracy defect is still open at `210/290`" — consistent with this pass's scoping.

## Against the prior verdict on this tool (CL1–CL24, all undecided)

- **CL1 (MAJOR, `--since` stops the walk) is inherited by the identifiers form.**
  `windowCommits` and `boardChanges` both call `sinceArg(w)` at `bdb1aba`. Reproduced on a
  throwaway repo: commits *in-window A*, *back-dated B*, *in-window C* on one branch; the
  `Commits` field printed `(1)` and named only C. The record field whose doctrine text is
  "every commit the session landed" silently omitted one. **CV19 below.** (At HEAD the
  same repo printed `(0): none`, because `210/290` now credits commits only on transcript
  evidence; that is a different behaviour and is not assessed here.)
- **CL8 (home path and principal's words in pasted output)** — partly answered by
  `8b30ee6` (the block's worktree paths only). The Transcript and Repo rows, check 1's
  list and the asks still print as CL8 found. CV4 reconciles to "CL8's remainder".
- **CL9 (no doctrine site tells a closing session to run it)** — partly answered by this
  delta: `089fcdc` names the check in `RECORD.md`'s all-clear bullet and `bdb1aba` names
  the command. `CONCURRENCY.md` still does not (CV7).
- **CL15 (design §10's example mismatch)** — still open, and §10 is now also silent on
  the block (CV17).
- **CL18 (test gaps by mutation)** — the pattern continues in the new code: four guards
  unprotected (CV4, CV5, CV14, CV15) against CL18's six.
- **CL21 (run from inside its own worktree, check 1 fails)** — bears on question 3; not
  this delta's, unchanged.
- **CL22 (a timed-out `gh auth status` reads as "not installed", note)** — the same
  mechanism as **CV3**. The prior pass rated it a note ("twenty seconds is generous, so
  rare"); this pass rates it MODERATE because the identifiers form now writes the
  misdiagnosis into a durable record and the plain run prints the block every time. CV3
  stands; CL22 is its origin.
- **CL23 (the transcript-store assumption)** — act 1's lens 1 item 1 answers it with
  the census (the store is complete for a session, nesting included).
- No prior finding was contradicted by this pass.

## Findings formed at reconcile (marked as such)

- **CV16 — MODERATE (formed at reconcile; seeded question 4). A completed agent whose
  last assistant record is a streamed partial reads as ⚠️, and the store holds 118 of
  them.** Evidence: 118 agents whose parent was notified `completed` end on an
  `assistant` record with `stop_reason: null` and a text block; the tool's rule ("the
  last assistant record has `end_turn`") prints ⚠️ *stops short of `end_turn`* for each.
  Beside CV1's 29 disagreements, that is a population a session cannot clear and will
  learn to read past — the brief's named risk. The `completed` notice is the harness's
  own word, and the design treats it as weaker than the file's last line. *Counsel:*
  when the parent holds a `completed` notice (or `meta.finished` is true) and the file's
  records all pre-date it, treat the agent as reported and say "by notification"; keep
  ❌ for records after the notice. One fixture with the `null`+text tail.
- **CV17 — minor (formed at reconcile; question 9). Design §10 was not swept when the
  plain run gained the block.** `bdb1aba`'s stat names no design or README change; §10
  still ends the output at the verdict line at `bdb1aba` and at HEAD; the README lagged
  at `bdb1aba` and was corrected later by another item's commit. V3. *Counsel:* one
  sentence in §10; the prior CL15 fix in the same edit.
- **CV18 — minor (doctrine; formed at reconcile; question 7). `RECORD.md` does not say
  the identifiers block is a record and not the close's evidence.** The man page does.
  A session that pastes the block under its all-clear can present it as proof the checks
  passed; the block prints whatever the verdict. The principal's to decide (rule 3).
  *Counsel:* one clause at `RECORD.md` line 98: "the block records; the twelve check
  lines are the evidence".
- **CV19 — MODERATE (formed at reconcile; prior CL1 inherited). The identifiers
  `Commits` and `Board` fields are built on the truncated `--since` walk the prior pass
  rated MAJOR, with no guard and no note.** Reproduced at `bdb1aba` (above): one of two
  in-window commits omitted, no hint printed. The root defect is CL1's and stays MAJOR
  under `160/870`, undecided; this delta's own defect is that a new record field — whose
  purpose is to name *every* commit — was laid on it twelve hours after CL1 was written,
  with the brief-writer and the author both able to see the prior verdict's heading. If
  the principal judges the root this delta's to own, this finding is a MAJOR and the
  overall line below becomes FAIL; this reviewer charges it MODERATE because the
  mechanism is already open at MAJOR on the same tool and a second MAJOR for the same
  cause would double the record without adding a fix. *Counsel:* fix CL1 once (walk
  without `--since`, or `--since` with `--topo-order` and a full range) and the field
  heals with it; until then the `Commits` line should say "walk may be truncated".

## Overall, restated

**PASS-WITH-FINDINGS — 0 MAJOR · 6 MODERATE (CV1, CV2, CV3, CV5, CV16, CV19) · 9 minor
(CV4, CV6, CV7, CV11, CV12, CV14, CV15, CV17, CV18) · 4 note (CV8, CV9, CV10, CV13).**
Changes from act 1, all stated above: CV1 reframed (same severity); CV2 strengthened;
CV3 traced to CL22; CV4 widened; CV8 answered (stays a note); CV10 corrected and
narrowed; CV16–CV19 new. The verdict holds on the brief's own test — no input produced
✅ with an agent live — and the conditional on CV19 is stated plainly for the principal.
All findings on the doctrine hunks (CV7, CV18) and on the tool that encodes them are the
principal's to decide; counsel sits beneath each and nothing was applied.

## Follow-up checklist, act 2 additions

- [ ] CV16 — honour the `completed` notice over a trailing partial; fixture with the
      `null`+text tail.
- [ ] CV17 — design §10 names the block; CL15's example fixed with it.
- [ ] CV18 — `RECORD.md`: the block records, the checks evidence (principal's call).
- [ ] CV19 — fix CL1 once; until then the `Commits` line says the walk may be truncated.
- [ ] CV4 (widened) — `realpath` both sides; trailing-separator `HOME`.

---

## Deferred sibling, folded below the verdict (orchestrator, 2026-10-25)

*Released to the reviewer only after its act-1 findings were saved; folded here verbatim and
the sibling file deleted, per the brief. The orchestrator (session `52e11d15`, Claude Opus 5.5)
formed no finding and wrote no severity.*

### Sibling to the close-covers-subagents cold pass — held under rule 1's split

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
