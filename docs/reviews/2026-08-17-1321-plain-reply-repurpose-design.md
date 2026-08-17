# Design review — can `plain-reply.py` be usefully repurposed as a data-gathering instrument?

**Pass type:** design review (REVIEW.md § *Review the design, not only the
build*) — a build/no-build question the principal put to the Fable tier. Not a
rule-4 doctrine pass: the hook is nobody's self-authored doctrine and no rule
is under review; the decision stays the principal's.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection.
**Status:** RUNNING — taken 2026-08-17 1321 UTC (wt: `cold-run-0817-1321`).

## The commission — the principal's words, verbatim

> "Do a fable review to see if it can be usefully repurposed e.g. to gather
> data/stats on plain speak to find the root cause when its not plain.
> Otherwise we will destroy the hook per your recommendation."

(Ruled 2026-08-17, second sitting, 1045 UTC; recorded at board item
`docs/roadmap/290-ruling-round-2026-08-17-the-cold-run-find/070-cmf1-fable-repurpose-review-else-destroy.md`,
which is the commission and is **not** barred — read it whole. It restates the
context the principal was given before ruling and the two outcomes it funds.)

## Spawn provenance

- **Author of the work under review:** the session that built the reply gate
  (landed 2026-08-09, `c374959`, per `git log`) and the session that unwired it
  on the principal's 2026-08-15 ruling. Neither is this
  session.
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 at 1321
  UTC on the **Fable** tier under his standing cold-session instruction (*do
  any reviews and any Fable-dependent work; write any briefs required*). This
  brief is scope-and-process only; the question is the principal's, above, and
  the brief-writer adds no attack questions of its own. The brief-writer is the
  orchestrator of this pass; it forms no finding and writes no severity.
- ⚠️ **Disclosure.** The brief-writer read the `docs/SESSIONS.md` tail and the
  2026-08-17 0955 session record at onramp — the record that carries the
  ruling and the principal's context for it in the orchestrating session's
  words. The reviewer read none of that.
- **Who reviews:** a Fable reviewer subagent spawned by the orchestrator, which
  authored no part of the hook, `plainscan`, the CHANGELOG or the doctrine
  clause, and was not started or instructed by any authoring session.
- **Orchestration shape:** the three prior verdicts the commission names —
  the communication-floor pass (`CMF`), the reply-gate unwiring pass (`RG`) and
  the board-generator pass (for `BG14`) — live under `docs/reviews/`, which
  `tools/coldsweep.py` bars by default; they are released by the orchestrator
  after the reviewer's phase-1 verdict is durably written, for reconcile only.

## Delta under review (the principal's list)

- `tools/hooks/plain-reply.py`
- `tools/plainscan.py` § the reply plane
- `tools/README.md` § `plainscan.py` (the two-planes section and the install
  stanza)
- `docs/method/COMMUNICATION.md` § *Some of it is enforceable*

## What the review must weigh (from the commission)

1. Whether a **record-only Stop hook** — run `plainscan` over the last
   assistant message, log findings + rule + context to a machine-local store,
   never block — would produce data that finds *root causes* of unplain prose,
   or only counts of it.
2. Whether the existing **`cctranscript` instruments** already reach the same
   data from transcripts without a hook. **Run the instruments' `--help` first**
   (`instruments/cctranscript --help`, and its man page under
   `instruments/man/`), and probe them against a real local transcript if one
   is reachable, before proposing any hook.
3. The **threat surface** the earlier passes named as `CMF6` — a machine-wide,
   fail-open hook running branch-tracking code from a public repo — as it
   applies to a *logging-only* variant. Consider what a logging hook writes,
   where, and who can read it (atelier is PUBLIC; the store must be
   machine-local and never travel into a repo).
4. The **private-layout path** the earlier passes named as `BG14`: the hook
   carries a hard-coded estate-layout fallback path. Say what it is, whether
   it belongs in a public tree, and what a repurposed hook would do about it.

Also in scope, because a design review's earliest finding is the cheapest:
whether the *question itself* is well posed — is "root cause when it's not
plain" a property a per-reply hook can observe at all, or does it need the
prompt/context that only a transcript carries? And whether "usefully
repurposed" has a cheaper answer than either build or destroy (a `plainscan`
mode over `cctranscript` output; a report; nothing).

## Re-run obligation

- `python3 tools/plainscan.py --help` and `python3 tools/hooks/plain-reply.py
  --help` (or read the argparse); run `plainscan` over a method doc to see the
  finding shape the hook would log.
- `instruments/cctranscript --help`; if a local transcript directory exists
  under `~/.claude/projects/`, run the instrument's search/stat modes against
  it and say what data it already yields on prose plainness — this is the
  control the commission asks for.
- The hook's tests, if any (`tools/test_*plain*`), the full Python and node
  suites, and the floor on both planes at HEAD (invocations lifted from
  `.githooks/pre-commit` and `.github/workflows/ci.yml`).
- Confirm the current wiring state: is the hook installed anywhere the repo
  can see (`.claude/settings*.json`, `tools/README.md` install stanza)? Say
  what you found, not what the docs claim.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the prior verdicts named in the commission are held by the orchestrator under rule 1's split, released after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the `CMF`, `RG` and `BG` passes
especially, which the commission names for reconcile). Sweep the tree with
`python3 tools/coldsweep.py`; if you use `--include-barred`, disclose it. The
board item `290-…/070` is the commission and is open to you. Board items
elsewhere that discuss the hook (`grep`-able as `plain-reply`) are the
authors' framing — read them after your findings if at all, and say so.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
the load-bearing assumptions named first, the answer to each of the four
weighings, findings with stable IDs (prefix `RP` — `PR` was already taken by a 2026-08-02 pass) and severities (MAJOR /
MODERATE / minor / note) where a finding is warranted, a **verdict line —
REPURPOSE (with the design, sized) or DESTROY — with grounds**, and a
follow-up checklist naming which of the item's two funded outcomes it
triggers. Then, on release, append a reconcile section against the three
prior verdicts. The decision is the principal's; record, apply nothing.

---

## Verdict — phase 1

**Written:** 2026-08-17 13:45–14:10 UTC · **Reviewed at:** worktree
`cold-run-0817-1321`, HEAD `b7e0da5` (main + the claim commit + the
orchestrator's prefix edit to this brief; the delta files are unchanged since
`cd6232b`, the unwiring commit). Hook first landed `c374959` (2026-08-09).

### Provenance and disclosures

- **Reviewer:** a Fable-tier subagent spawned by the orchestrating session Mike
  opened 2026-08-17 at 1321 UTC under his standing cold-session instruction. I
  authored no part of the hook, `plainscan`, the CHANGELOG, the README section
  or the doctrine clause, and was neither started nor instructed by any
  authoring session. The orchestrator wrote none of the delta and none of this
  brief's questions (they are the principal's, verbatim); it forms no finding
  and writes no severity. Every finding, severity and word below is mine.
- **Barred material:** I opened none of `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, or any other file under `docs/reviews/`. All tree
  sweeps went through `tools/coldsweep.py` with the three sibling
  2026-08-17-1000 briefs additionally excluded (wrapper in the session
  scratchpad); `--include-barred` was never used. The sweep for `plain-reply`
  surfaced grep lines from four board items that carry the authors' framing
  (`020-…/310`, `020-…/README.md`, `120-…/010`, `160-…/180`); I read only the
  truncated hit lines the sweep printed, did not open those files, and no
  finding rests on them.
- **Outside the tree, read-only:** the machine-level Claude settings file
  (only its `hooks` key and a substring test for the hook's name — see the
  wiring check), the hook's leftover state file (entry count and key names
  only), and the local transcript store via `cctranscript` for the control
  probe. The probe read eight older atelier sessions (2026-07-26 to 2026-08-09)
  and computed aggregates only; one earlier shape check opened the second-most-
  recent atelier session by JSON, printed keys and role counts only, and I
  note it was likely a live sibling session. A key-only pass over ten older raw
  logs established which fields the log carries. Nothing from any transcript is
  quoted here. The listing that selected sessions showed the orchestrator's own
  session id at the top; I did not open it. One external read: the Claude Code
  hooks reference page, for the exact `Stop` payload fields.

### Lens 1 — the load-bearing assumptions, in my words

1. **That a per-reply observer sees something a transcript does not.** It is
   the only reason to prefer a hook over a batch job. I tested it directly.
2. **That "data/stats on plain speak" is what finds a root cause.** A rate is
   an effect; a cause is what the effect correlates with. Root-cause data must
   pair each unplain reply with the conditions around it — the prompt, the
   model, the effort level, the size of the context, the kind of ask.
3. **That the thing to repurpose is the hook.** The hook is 231 lines, of
   which the rule engine is an import. What is uniquely *in* the hook is the
   block/rewrite loop, the anti-deadlock state file, and three chat-plane
   constants.
4. **That "machine-local, never block" removes the earlier objections.** It
   removes one (the reprint). It leaves the fail-open, branch-tracking,
   machine-wide execution path untouched, and adds an output the blocking
   variant did not have: a written store of reply fragments.

### The control the commission asked for

`instruments/cctranscript --help` and the man page: the instrument renders or
searches Claude Code's session logs, read-only, and `--json` emits every turn
with `role`, `model`, `ref`, `timestamp` and `text`, plus the session's
context peak and agent counts. Sessions older than the live 30-day window are
reachable through `--from-archive`. It has no plainness mode of its own.

Piping its JSON into `plainscan.scan_text` — the hook's own engine, at the
hook's own settings (P1/P3/P4, 45 words / 60 chars, replies of 200+ chars) —
over eight older atelier sessions:

| Measure | Value |
|---|---|
| Sessions read | 8 of 8 |
| Replies of 200+ chars | 45 |
| Flagged under the hook's config | 25 (56%) |
| Findings by rule | P1 ×45 · P3 ×5 · P4 ×9 |
| Flagged replies whose *preceding prompt* was in the same JSON | 25 of 25 |
| Preceding-prompt length (chars) | min 2 · median 667 · max 3,131 |

Two things follow. First, the transcript route yields the hook's whole output
plus the prompt that produced each reply, today, with a 40-line script. Second,
P1 (a bare reference code) is 76% of the findings — and P1's most plausible
root cause is a code seeded by the *prompt* or the board and echoed back bare,
which is a hypothesis you can only test by reading the prompt beside the reply.

Field check on the raw logs (keys only, ten older sessions): the log records
`effort`, `permissionMode`, `gitBranch`, `cwd`, `version`, `promptId`,
per-message `model` and `timestamp`, and the tool layer. Every covariate a
root-cause analysis would want is already at rest there.

`Stop` payload per the hooks reference: `session_id`, `transcript_path`,
`cwd`, `permission_mode`, `hook_event_name`, `prompt_id`, `effort`,
`agent_id`/`agent_type` when in a subagent, `stop_hook_active`,
`last_assistant_message`. So a hook that wanted context would have to open
`transcript_path` — the same file `cctranscript` reads — and would then be a
transcript reader that runs at the worst possible moment.

### Wiring state — what I found, not what the docs say

- No `.claude/` directory exists in the worktree; no `.claude/settings*.json`
  is tracked anywhere in the repo (`git ls-files` shows only
  `.claude-plugin/{marketplace,plugin}.json`, and the plugin manifest declares
  no hooks).
- The machine-level Claude settings file has **no `hooks` key at all** and no
  mention of `plain-reply` or `plainscan`. The install stanza in
  `tools/README.md` is documentation only. **The hook is wired to nothing.**
  The docs' claim is true.
- Residue: the hook's state file (`~/.claude/.plain-reply-state.json`) still
  exists — 3 entries, `{at, count, sig}`, last written 2026-08-15. Harmless
  (the hook applies a 6-hour TTL on read), but it is the one trace of the live
  period left outside the repo.
- `python3 tools/hooks/plain-reply.py --help` prints nothing and exits 0: the
  file has no argument parser; it reads stdin, fails open on the empty payload,
  and exits. It has no CLI surface to repurpose.

### The four weighings

**1. Would a record-only Stop hook find root causes, or only counts?** Counts,
and worse counts than the transcript already holds. A per-reply hook observes
one reply at a time; a root cause is a correlation across many replies with
their conditions. The hook payload carries none of those conditions except
`effort` and `cwd`, and the transcript carries all of them (verified above).
The hook could reach the rest only by reading the transcript. And a hook logs
a *derived* value — findings under today's rule set — so a rule fix cannot
re-score history; the transcript keeps the *primary* data and re-scores on
demand. A fail-open collector also produces a dataset with unmeasured gaps: an
engine import failure logs nothing and looks like a clean session.

**2. Do the `cctranscript` instruments already reach the same data?** Yes, and
more. See the control table: every hook output plus the prompt, model, effort,
context size and repo, for every session in the live store and, via
`ccarchive`, beyond the 30-day cleanup. What does *not* exist yet is a scorer
over that JSON — a ~100-line consumer, not a hook (sized under RP8).

**3. CMF6 for a logging-only variant.** Unchanged in the parts that matter,
worse in one. Unchanged: a user-level `Stop` hook runs on every turn of every
session in every repo on the machine, executing whatever the tracked checkout
of a public repo currently holds, and fails open, so a broken or hostile
version is silent. Worse: a logger *writes*. Its natural payload is finding
excerpts (70-char windows of reply text) and, if "context" is logged, prompt
text — from every repo including private ones — into a machine-local store.
Any process running as the user can read it, and I note that the atelier
checkout's local settings grant its sessions read access over the Claude
configuration directory, which is where the hook already keeps its state file.
That is a curated, cross-repo, most-quotable-fragments file sitting inside a
public repo session's read scope. The transcripts themselves already live
there, so this is not a new class of exposure — but it is a second copy, and
the design earns nothing for taking it on.

**4. BG14 — the private-layout path.** The fallback is
`Path.home() / ".pets" / "atelier" / "tools"` (`plain-reply.py:111`). The
`~/.pets/` layout is already published in `docs/method/STORAGE.md`, so the
line discloses nothing new. It is, however, **dead code under the documented
install form** — the stanza runs the file by absolute path, so `__file__`
resolves and `tools/` is found beside it — and under any other placement it is
a silent fail-open trap: an adopter without that layout gets a hook that does
nothing and says nothing. A repurposed hook would delete the fallback and fail
loud (a logger that cannot find its engine must say so, or its data lies by
omission). Under DESTROY it goes with the file.

**Is the question well posed?** As a data question, yes: "what conditions
produce unplain replies" is answerable. As a *hook* question, no: the property
is not observable per reply, and the one place it is observable — the
transcript — is already instrumented. **The cheaper answer exists**: score
`cctranscript --json` with the engine plainscan already has.

### Findings

- **RP1 — MODERATE — The hook adds no observation the transcript lacks.**
  Evidence: `Stop` payload fields vs. raw-log keys (above); the control probe
  reached the preceding prompt for 25/25 flagged replies. Reproduce: run the
  probe script from the session scratchpad over any session ids;
  `cctranscript --repo <name> --json <id>` and score `turns[].text` for
  `role == "claude"`.
- **RP2 — MODERATE — A fail-open logger yields worse data than re-scoring the
  transcript.** Findings logged under the rules of the day cannot be re-scored
  after a rule fix; silent import failures are indistinguishable from clean
  sessions. The transcript is complete and re-runnable. Reproduce: read
  `_engine()` and `main()` in `plain-reply.py` — every failure path is
  `return 0` with no output.
- **RP3 — MODERATE — The logging variant keeps CMF6's execution surface and
  adds a written store of cross-repo reply fragments.** Evidence: the hook is
  user-level (README stanza), fails open (docstring, code), imports from a
  tracked checkout; a logger's output would sit in the Claude config directory
  the state file already uses. Not disqualifying on its own — the transcripts
  are already there — but a cost with no matching benefit.
- **RP4 — minor — BG14 confirmed: `~/.pets/atelier/tools` fallback at
  `plain-reply.py:111`.** Already-published layout, dead under the documented
  install, silent trap elsewhere. Remedy under DESTROY: file deletion. Under
  any repurpose: remove it and fail loud.
- **RP5 — minor — Wiring residue.** The hook is out of every settings file I
  can see, but its state file survives outside the repo (3 stale entries).
  Remedy: delete it in the same sweep that deletes the hook; the README's
  destroy checklist should name it so an adopter's copy goes too.
- **RP6 — note — Nothing in the hook is instrument-shaped.** No CLI, no
  output format, no store; the reusable content is three constants
  (`BLOCKING_RULES`, 45/60, the 200-char floor). "Repurpose the hook" would in
  practice mean writing a new tool and deleting this one.
- **RP7 — note — Re-run ledger green** (table below). The repo-plane
  `plainscan` tally is 5,499 findings (P1 699 · P2 253 · P3 2,665 · P4 1,882),
  identical on both planes.
- **RP8 — note — The cheaper answer, sized.** A transcript-plane report — call
  it `plainreport`, in `tools/` or as `plainscan --transcript` reading a
  `cctranscript --json` turns array on stdin. Scores `claude` turns of 200+
  chars at the chat limits; groups findings by rule × model × repo ×
  prompt-shape (does the prompt carry reference codes; prompt-length bucket)
  × context-peak bucket × reply-length bucket; prints a table and `--json`.
  Reads only the transcript store, writes nothing, needs no settings entry,
  runs on demand and over `--from-archive`. Size: ~100–150 lines Python, ~8
  tests, one README section; no doctrine change. It reuses `plainscan`'s
  engine, not `plain-reply.py`. Whether to build it is a separate call — it is
  not one of this item's two funded outcomes.

### Verdict

**DESTROY** `tools/hooks/plain-reply.py`, with these grounds: (1) a per-reply
hook observes strictly less than the transcript already at rest, and could
close the gap only by reading that transcript (RP1); (2) its data would be
derived, un-rescorable and silently gappy where the transcript's is primary
and complete (RP2); (3) the logging variant retains the machine-wide fail-open
execution surface and adds a written cross-repo store for no gain (RP3); (4)
nothing in the file is worth carrying into an instrument (RP6). The
data-gathering aim the principal named is sound and is met without a hook by
scoring `cctranscript --json` with the engine `plainscan` already exposes
(RP8) — a repurpose of the *engine*, which needs no ruling to stay, not of the
hook. Counts: 0 MAJOR · 3 MODERATE · 2 minor · 3 note. The decision is the
principal's.

### Re-run ledger

| Check | Invocation (from the worktree root) | Result |
|---|---|---|
| Hook tests | `python3 -m unittest tools.test_plainscan` | 51 tests OK (7 in `StopHook`) |
| Python suite | `python3 -m unittest discover -s tools -p 'test_*.py'` | 1,344 tests OK |
| Node suite | `node --test instruments/*.test.js` | 235 pass · 0 fail, exit 0 |
| Floor, hook plane | `python3 tools/floor.py --plane hook --root <wt> --tools <wt>/tools` | exit 0; 15 rows, none red; plainscan warn-only 5,499 |
| Floor, CI plane | `python3 tools/floor.py --plane ci --root <wt>` | exit 0; 13 rows, none red; plainscan 5,499 |
| stampscan | `python3 tools/stampscan.py --warn --root <wt> <wt>` | exit 0; 1 region identical |
| `plainscan --help` / hook `--help` | as written | exit 0 / exit 0 with no output (no argparse) |
| plainscan over a method doc | `plainscan.py --root . docs/method/COMMUNICATION.md --sentence-limit 45 --aside-limit 60 --rules P1,P3,P4` | 7 findings (P3 ×4, P4 ×3), exit 1; `--json` shape `{scanner, findings[{rule,path,line,detail,excerpt}], counts, warn}` |
| `cctranscript --help` + man page | as written | exit 0; read whole |
| Control probe | scratchpad script over 8 session ids | table above |
| Wiring | machine settings `hooks` key; `git ls-files`; plugin manifest | none / none / none |

No suite result looked like interference; nothing was re-run for that reason.

### Follow-up checklist — triggers the item's **If DESTROY** outcome

- [ ] Delete `tools/hooks/plain-reply.py`; delete the `StopHook` test class
      (7 tests) and the `HOOK` constant in `tools/test_plainscan.py`; delete
      the install stanza and retense the reply-plane paragraphs in
      `tools/README.md` § `plainscan.py` to history.
- [ ] RG2: retense the `plainscan.py` docstring's "reply — a Stop hook…"
      plane to past tense or a single-plane statement.
- [ ] `docs/method/COMMUNICATION.md` § *Some of it is enforceable*: replace
      "Destroy-or-repurpose is Mike's open ruling" with the ruling and date.
- [ ] Delete the leftover state file outside the repo (RP5) and name it in the
      destroy note so adopters do the same.
- [ ] Close RG3, CMF2, CMF6, CMF8, BG14 as moot; **CMF cycle CLOSES.** The
      flaky-StopHook-test item under `docs/roadmap/120-…` closes moot with the
      tests.
- [ ] Optional, separate call for the principal: open a small build item for
      the transcript-plane report (RP8). Not funded by this item.

### Reconcile (2026-08-17, after release)

**Written:** 2026-08-17 13:51–14:05 UTC, after phase 1 was committed
unrevised as `16da277`. Nothing above this heading is changed. There is no
deferred sibling for this pass; nothing is folded in.

**Provenance of this step.** On the orchestrator's release I opened, in this
order: (1) `docs/reviews/2026-08-15-1033-communication-floor-cold.md` — the
findings block, overall, checklist and reconcile; (2)
`docs/reviews/2026-08-15-1126-reply-gate-unwired-cold.md` — findings, overall,
checklist, and the two reconcile subsections on the documentation follow-up and
the CMF2 transcript look; (3) the BG14 finding text and the lens-answer line
that points at it in the BG verdict
(`docs/reviews/2026-08-17-0730-board-generator-child-truth-cold.md`), nothing
else in that file; (4) the four board items whose sweep
hit-lines I had seen: `020-…/310-the-reply-gate-is-unwired-destroy-it-or-repur.md`
(whole), `020-…/README.md` § *COMMUNICATION.md enforced* (the hook lines and the
rescope bullet), `120-…/010-two-tests-fail-intermittently-in-the-full-suit.md`
(whole), `160-…/180-rule-4-review-queued-tier-fable-pass-type-doc.md` (head).
Item (5), the SESSIONS.md index line, was **not opened** — no finding needed
it. One further key-only read of the same ten older raw logs, to check a
field the item's ruling made relevant (below). The orchestrator formed no
finding.

**A fact the release surfaced that phase 1 did not have.** The item's verbatim
ruling names the target as *"unusable responses to the VS code sessions … the
root cause(s)"*. Two consequences. The transcript records the client that ran
each session (`entrypoint`; every record in the ten logs checked reads
`claude-vscode`), so a transcript-side analysis can select exactly the
sessions the ruling names; the `Stop` payload carries no such field. And
"unusable" is wider than plainscan's four rules — the item's own measurement
counts reprinted verdicts as the largest unusable output — which a transcript
report can score (near-duplicate replies, reply length, position in session)
and a plainscan-only hook cannot. Both strengthen RP1; neither changes a line.

**Per finding — anticipated or new.**

- **RP1** — *new as a measured claim*; anticipated in substance by the item
  itself, which says the programme's "queued history-mining pass is the
  instrument" for the position-in-session hypothesis, and whose option-2 log
  fields (session, repo, model, reply length, position-in-session) are all in
  the transcript. Not in CMF, RG or BG.
- **RP2** — *new*, but compounded by RG1 and CMF5: RG1 says a collector built
  on "detection was sound" inherits a detector that fired mostly on
  near-misses; CMF5 says P1 cannot tell a reference code from a product name.
  A hook logs those misfires permanently; a transcript re-scores them away
  once the rule is fixed.
- **RP3** — *anticipated by CMF6* (machine-wide, branch-tracking, fail-open,
  silent; supply chain via the working tree; counsel to pin `ATELIER_TOOLS`
  and emit `systemMessage` on engine failure) and by the item's own boundary
  paragraph ("its log holds verbatim reply text from every repo … machine-local
  and never committed"). New in RP3: the read-scope observation — the atelier
  checkout's local settings let its sessions read the Claude configuration
  directory where the hook already keeps state.
- **RP4** — *anticipated by BG14 exactly.* New: the fallback is dead code under
  the documented install form, and `STORAGE.md` already publishes the layout,
  so the class BG14 names is "estate fact embedded in a tool", not a fresh
  disclosure.
- **RP5** — *anticipated by RG8 exactly* (same file, same three entries).
- **RP6** — *new*; adjacent to CMF2 and RG6, which establish that the two
  mechanisms the file does own — the give-up path and the anti-deadlock guard
  — are respectively invisible to the principal and not implemented as
  described. That is why nothing in the file is worth carrying.
- **RP7** — *matches CMF10 and RG9*: green re-runs, flake fixed and verified.
- **RP8** — *anticipated in aim* by the item's option 2 and the programme's
  history-mining pass; new in plane (transcript, not hook) and in the design.

**CMF6 as those passes described it vs. RP3.** They match. CMF6's surface is
the execution path — every `Stop` on the machine runs whatever `plainscan.py`
the tracked checkout holds, and a `gh pr checkout` of a fork branch on this
public repo changes machine-wide hook code silently. RP3 reads it the same way
and adds only that a logging variant also *writes*, so the surface gains an
output. CMF6's counsel (immutable or pinned engine; visible failure) is what
RP4's "fail loud" restates for the fallback path. Also resolved in passing:
RG's reconcile left open whether `stop_hook_active` is a documented `Stop`
input; the hooks reference I fetched for phase 1 lists it, which agrees with
the 1033 pass. Moot under DESTROY; recorded so nobody re-chases it.

**Is the item's "If DESTROY" checklist COMPLETE against what CMF/RG/BG filed?**
Not quite. It names RG2 (retense) and RG3, CMF2, CMF6, CMF8, BG14 (moot).
DESTROY also bears on these, which the item's list does not mention:

- **RG6** — the anti-deadlock docstring; moot with the file (RG's own checklist
  says "fix or delete with the ruling"). Add to the moot list.
- **RG8** — the state-file residue; not moot by deletion of the hook, needs the
  explicit removal (my RP5). Add.
- **RG9 / item `120-…/010`** — the StopHook flake and its open "guard the fix"
  ask die with the StopHook tests. Add as moot.
- **CMF7 / RG7** — CHANGELOG owes entries for the wiring and the unwiring;
  DESTROY adds a third event and closes neither. Not moot; should ride the same
  commit.
- **CMF2 and RG3 are moot only if the README's give-up sentences go too.**
  The item's list deletes "the install stanza"; CMF2 (README L851–852) and RG3
  (README L859–862) sit in the reply-plane paragraphs *above* the stanza. Phase
  1's checklist already says "retense the reply-plane paragraphs"; the item's
  should say so, or "moot" is overstated for those two.
- **RG1** — the COMMUNICATION.md clause keeps half its evidence; independent of
  DESTROY and still open, but the same clause is edited to record the ruling,
  so one edit can carry both. Not moot.
- **CMF3, CMF4, CMF5, CMF9** — repo-plane and doctrine findings; DESTROY does
  not touch them and they stay in the ruling round. "CMF cycle CLOSES" should
  be read as the review cycle closing at 0 MAJOR, not as those findings
  closing.
- The 020 README's *"Destroy-or-repurpose is Mike's open ruling"* line and the
  matching sentence in COMMUNICATION.md both retense with the ruling (the
  latter is already in phase 1's checklist).

**Severity or verdict change.** None. Phase 1: DESTROY, 0 MAJOR / 3 MODERATE /
2 minor / 3 note. After release: the same. RP1 is strengthened by the
`entrypoint` field and by the item's own concession that the transcript-mining
pass is the instrument; nothing weakens any finding.

**Counsel, labelled as counsel and one line:** if the principal wants the data
the ruling asked for, build a small transcript-plane report over
`cctranscript --json` — plainscan's engine plus reply-repetition and length
measures, filterable by `entrypoint` — and skip the hook; it is a separate,
unfunded item, and this pass recommends it without requiring it.
