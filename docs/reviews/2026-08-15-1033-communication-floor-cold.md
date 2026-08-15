# Cold pass — the communication floor (COMMUNICATION.md's enforcement clause, plainscan, the reply gate, and the repo-plane rescope)

**Pass type:** combined doctrine + code cold pass (REVIEW.md rule 4 — the
enforcement clause was rewritten by the session that built the mechanism it
now points at; the rescope's doctrine and code came from one session too).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

**Two queue pointers, one brief.** The board carries two rule-4 pointers on
this surface: the COMMUNICATION.md enforcement-clause rewrite (landed
2026-08-09) and the plainscan repo-plane rescope (landed 2026-08-10). Both
name the same doctrine section as their delta and the second builds on the
first's mechanism, so one reviewer reads the surface once. Both pointers are
closed by this pass's verdict.

## Spawn provenance

- **Author of the work under review:** the session that landed the first
  delta on 2026-08-09 and the session that landed the second on 2026-08-10
  (wt: `plainscan-rescope-0810`); see *What the work is*.
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of either delta, was neither started nor instructed by either authoring
  session, wrote this brief from the deltas and the queue pointers only (it
  did not open the intent records), and **stopped** — it did not run the
  review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with the two
  authoring sessions and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1033-communication-floor-cold.deferred.md` (rule 1's split):
  the intent-record references, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.
- **A note on hashes.** The first pointer names `753adb6` and `e61adc4`;
  those commits were rebased before landing and sit on `main` as `c374959`
  and `beaf240`. The pointer's refs are the pre-rebase objects. Recorded here
  so the taker does not chase a dangling hash.

## What the work is

Landed on `main` as `c374959` (the floor under COMMUNICATION.md, 2026-08-09),
`beaf240` (recitation cap), `b879b02` (P5 built and rejected; the hook's
state-file fix), `171862b` (the reply gate switched on — records and the
tools catalogue), and `e390382` (the repo-plane rescope, 2026-08-10, ruled).
Reviewed at HEAD:

1. [`docs/method/COMMUNICATION.md`](../method/COMMUNICATION.md) § *The
   meta-rules that make it work* — the enforcement clause as rewritten twice:
   the 2026-08-09 correction of the "write-time discipline is the only
   control" claim, and the 2026-08-10 *each plane is scoped to its reader*
   paragraph.
2. [`tools/plainscan.py`](../../tools/plainscan.py) — the engine: rules
   P1–P4 with their stated grounds, the two planes, `RECORDS_GLOBS` and
   `--include-records`, the recitation cap. [`tools/test_plainscan.py`](../../tools/test_plainscan.py)
   — 47 → 51 tests across the deltas.
3. [`tools/hooks/plain-reply.py`](../../tools/hooks/plain-reply.py) — the
   `Stop` hook that lints the agent's own reply and blocks it for rewrite;
   fails open by stated design; the anti-deadlock guard and its state file.
   Its installation is machine-local (`~/.claude/settings.json`) and outside
   the repo — the *shape* of the installation is documented in the tools
   catalogue and is reviewable; the live setting is not in the tree.
4. [`tools/floor.py`](../../tools/floor.py) — the `plainscan` registry entry
   (warn-first via flag, both planes) and the rescope's wiring.
5. [`tools/README.md`](../../tools/README.md) — the plainscan and hook rows.
6. `CHANGELOG.md` — no entry mentions plainscan, the hook, or the
   communication floor at HEAD (grep at brief-writing: zero matches). Stated
   as a fact about the delta's surfaces, for the reviewer to weigh.

The board records that the reply-plane numbers (45 words / 60 characters) were
the principal's ruling and that the repo-plane numbers remain unruled; that
P5 was built, measured and deleted the same day; and that a test in this
module's Stop-hook suite is flaky under the full-suite run. All three are
in-scope facts about the delta, stated here as facts, not as findings.

## Scope

Widest the work admits: the measurement the correction rests on and whether
the doctrine now says what the mechanism does; the four rules and the grounds
each claims; the two-plane design and the fail-open choice; the hook's
behaviour live; the rescope's exclusion list and its ruling; the tests; and
the doctrine as it will bind every repo where the hook is installed. **Non-goals
— one, and it does not fence the risk:** the reviewer does not decide any
finding. Doctrine here is self-authored; findings are the principal's to rule
on (rule 3). Counsel may be recorded, labelled as such. The reply-plane
numbers are ruled and are not re-litigated; whether the mechanism honours the
ruling is in scope.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is a Stop hook that blocks the reply the right control for the
   trust failure it answers? Is "records are written for the next agent, not
   the principal" true of the three excluded paths — and only of them? Is
   fail-open the right posture for a gate on the principal's own reading
   surface?
2. **Correctness & quality** — run the suites; run `plainscan` on both
   planes; drive the hook by hand with a clean payload, a rule-breaking one,
   a malformed one, and a repeated session id (the anti-deadlock path); check
   what `RECORDS_GLOBS` actually matches against what the doctrine says it
   excludes. Reproduce the flake if it reproduces.
3. **Completeness / harvest** — the doctrine says four things are checkable
   and names what stays judgement; test the boundary in both directions. Do
   the rules' stated grounds hold (a published standard, dated house
   doctrine, a house call)? What does the correction leave in the person-level
   layer that the doctrine still says is unreachable?
4. **Security & privacy** — mandatory. The hook reads every reply the agent
   writes in every repo and keeps a state file; the engine's output recites
   the offending text. Where does recited text go on each plane, what does
   the state file hold, and does anything cross from a private repo's reply
   into a public tree's record? atelier is PUBLIC — verify nothing in the
   delta or your verdict joins a private repo's name to its posture. The
   house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the full suites (house invocations live in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift them, do not
guess); the test-count claims at the landing commits; the advisory tally the
rescope claims (7,817 → 4,440 on this repo — measure at the landing tree and
at HEAD, and say which you measured); the hook driven live through its stated
paths; and the floor on both planes at HEAD. The 6,704-reply measurement
behind the correction reads a private transcript corpus and cannot be re-run
from the repo — say so, and review the *method* as recorded rather than
treating the number as verified.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent records for both
deltas. The sibling `.deferred.md` holds those references and the
brief-writer's seeded questions; open it after your findings are committed.
Reconcile after, never anchor before. A taker whose own session onramp has
already read the `SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CF`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update both queue pointers
(`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/300-generalise-the-finding-don-t-just-fix-this-doc.md`
and the rescope pointer inside
`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/README.md`) and
rebuild the index in the same commit.

---

# Verdict — cold pass on the communication floor (COMMUNICATION.md's enforcement clause, plainscan, the reply gate, the repo-plane rescope)

**Provenance, repeated.** Reviewer: a cold rule-4 reviewer on the Fable tier, spawned by this pass's orchestrator — a Fable session Mike opened on 2026-08-15 at about 1120 UTC under his standing cold-session instruction (do any review work, any Fable-dependent work, write briefs for reviews that need them; a brief-writer never runs its own brief) and pointed at the review queue. The orchestrator authored no part of this delta and was neither started nor instructed by the authoring session or by the brief-writing session (a separate cold session earlier on 2026-08-15); the reviewer likewise. The `.deferred.md` sibling was withheld under the orchestrator's context partition — moved out of the worktree before this reviewer was spawned — so nothing below this line was written with it, the intent record, or any prior verdict in hand. Orchestrator's disclosure: its own session onramp read the tail of `docs/SESSIONS.md`, whose index entries summarise these deltas; the reviewer did not, and received only the brief and this preamble.

Reviewer's own disclosures, in full. **Finding prefix:** the brief asked for `CF`; the orchestrator changed it to `CMF` because `CF1`–`CF7` already exist in `docs/reviews/2026-07-20-1355-concurrency-flip-cold.md` and IDs must be unique across the directory. **What I read beyond the brief and the delta:** REVIEW.md whole; the five delta commits' messages and diffs; the six surfaces at `e390382` and at HEAD; Claude Code's hooks reference (`code.claude.com/docs/en/hooks.md`, fetched 2026-08-15 — the reviewer's own evidence for lens 1); the two queue pointers (`docs/roadmap/020-…/300-…md` and the rescope pointer in `docs/roadmap/020-…/README.md` lines 300–380, which is also the board's § *COMMUNICATION.md enforced* narrative and names itself as the rescope's intent record — so that intent record was read, by the orchestrator's explicit leave, and says so here); board item `docs/roadmap/120-test-plainscan-stophook-is-flaky-and-ci/` (the flake report, opened to check whether the delta closed it); `docs/method/RECORD.md` §§ on record stores; `docs/build/REPO-STANDARD.md` § CHANGELOG. I did not open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, or any other file under `docs/reviews/`. **Three exposures I did not choose, stated so the reader can weigh what follows:** (1) the session's auto-memory index, present in my context from the start, carries a one-line entry saying the reply gate is unwired because "a Stop hook cannot un-print"; (2) the initial git status showed the merge subject "the reply gate comes out"; (3) at about 1140 UTC I invoked `/security-review` aimed at my scratch clone (delta re-applied as a pending diff, per the preamble's sanctioned shape), and the skill instead read the *worktree's* pending diff — which at that moment was the orchestrator's in-flight brief and deferred sibling for the *reply-gate-unwiring* pass (`2026-08-15-1126-reply-gate-unwired-cold.*`) — and printed both into my context, including that later commit's mechanism claim and its transcript-window figures. That is exactly the SL2 hazard REVIEW.md names, reproduced. What I had formed before (3): my lens-1 judgement on the Stop-hook control, from the hook contract and the docs — held in reasoning, not yet written. I wrote it to a timestamped scratch note at 1144 UTC and only then opened `cd6232b`'s message and diff at 1156 UTC; lens 1 below is that note, edited for length only. The RG deferred sibling's seeded questions were also in that exposure; I have not used them to shape any finding here, and the RG pass is not mine. **Interruption:** the orchestrator reports this reviewer's run was cut by an API session limit at about 1200 UTC on 2026-08-15 and resumed at about 1352 UTC once the limit reset; the scratch clone, drive logs, suite logs and the timestamped lens-1 note all survived, and no re-run below was repeated blind — each was either already logged or re-executed after resumption.

**The delta reviewed.** `c374959` (floor under COMMUNICATION.md, 2026-08-09), `beaf240` (recitation cap), `b879b02` (P5 built/rejected; state-file fix), `171862b` (reply gate switched on — records + catalogue), `e390382` (repo-plane rescope, 2026-08-10) — reviewed at the landing tree `e390382` in a scratch clone (`git checkout e390382`) and at HEAD. HEAD moved under me during the pass (`3d0df11` at spawn → `fe4908b` → `b4fe720` at verdict-writing, all in this worktree's branch; the primary's `main` was `738afd9`); the six surfaces are byte-identical between `738afd9` and `b4fe720` (`git diff --stat` empty), so HEAD measurements are valid for either. **Moved after landing, out of scope:** `cd6232b` (2026-08-15, merged `433dc1f`) rewrote `COMMUNICATION.md` § *Some of it is enforceable*, `tools/README.md` § plainscan, and the hook's docstring; it is under its own queued pass (`docs/roadmap/160-…/180-…`). Where its text supersedes this delta's I say so; its claims are treated as a later author's, attackable, not settled. Its session record was not opened. Board pointers were not edited.

## Load-bearing assumptions, named first

1. **A `Stop`-hook block makes the flawed reply go away** — the reply is "rewritten before the principal ever reads it" (hook docstring, README, COMMUNICATION.md, commit `c374959`). **Did not hold** — see lens 1; the hook contract fires after the response is complete and delivered, and a block only continues the turn. MAJOR (CMF1).
2. **The give-up path lets the reply through with a note the principal sees.** **Did not hold** — `additionalContext` is Claude-facing, not shown as a chat message, and on `Stop` continues the conversation like a block. (CMF2)
3. **The four rules are machine-decidable "without judgement".** Held for P3 (a count) and P4 (a length in a bracket); **held only in shape** for P1 and P2 — the shape rule fires on product identifiers (`S3`, `SHA256`, `M2`) and misses dictionary-word acronyms. (CMF5)
4. **The measurement supports the doctrine's numbers as written.** Held for the direction (a real gap, plausibly measured), **did not hold for the figures the doctrine states** — the range omits one rule, one threshold differs from the shipped one, one rule had no prior doctrine to be "written down". Corpus cannot be re-run from the repo. (CMF3)
5. **"Records" = the three excluded paths, and only they.** Held as code; **did not hold as the ruling's own argument** — other verbatim-preserved stores exist and 74% of the post-rescope tally is closed review text. (CMF4)
6. **Fail-open is safe because the cost of a miss is one clumsy reply.** Held for wedging; **did not hold for silence** — loss of the gate is undetectable by design, and the same install shape gives a branch-tracking working tree machine-wide execution. (CMF6)
7. **7,817 → 4,440 and 47 → 51 tests are true at the landing tree.** **Held** — reproduced exactly.
8. **The Stop-hook suite flake is fixed by `PLAIN_REPLY_STATE`.** **Held on the evidence available** — 5/5 full-suite runs and 11/11 module runs green; the board item reporting it stays open (CMF7).

## Lens 1 — approach & assumptions

*Formed from the hook contract before reading `cd6232b`; disclosed above.*

**Is a `Stop` hook that blocks the reply the right control?** No — not for the aim this delta states, and the miss is a category error about *where the hook sits in the turn*, not a tuning error. The Claude Code hooks reference (fetched 2026-08-15) says `Stop` runs when Claude finishes responding and hands the hook `last_assistant_message` — "the text content of Claude's final response"; `decision: "block"` "prevents Claude from stopping; Claude continues the conversation", with `reason` delivered to Claude as its next instruction. Nothing in the contract retracts, hides or replaces the response already produced: in the terminal it has streamed, in `stream-json`/SDK mode it has been emitted, in the transcript it is a message. So on the principal's reading surface a block yields the flawed reply, a hook line, and then the rewrite — the reader pays for both. For a doctrine whose purpose is lowering the reader's consumption cost, that is a control that raises it on every fire and lowers it only for a later reader of the transcript, if at all. The event that would satisfy "rewrite before read" — intercepting assistant text before display — is not one the harness offers (PreToolUse gates tools; UserPromptSubmit gates the prompt; there is no pre-reply event). What a `Stop` hook *can* honestly do here is measure (a per-session ledger, no block), advise (`systemMessage`, shown to the user, turn ends), or steer the next turn (`additionalContext`); the delta chose the one output whose cost lands on the reader. `cd6232b`, read afterwards, reaches the same mechanism conclusion and unwired the hook; my finding is independent of it and adds CMF2, CMF5 and CMF6, which that commit does not carry.

**Is "records are written for the next agent, not the principal" true of the three excluded paths — and only of them?** True of the three, in the sense the ruling meant (append-only, unrewritable, read by onramps). Not *only* of them: `docs/reviews/withdrawn/` is preserved verbatim by doctrine (REVIEW.md § *A pass that is not accepted is withdrawn*); RECORD.md names `SESSIONS-ARCHIVE.md` as a growth store of the same class and it is not in `RECORDS_GLOBS`; a closed verdict is history once ruled, and `docs/reviews/` holds 3,392 of HEAD's 4,598 remaining findings; and a blockquoted principal ruling inside doctrine is prose nobody may rewrite, yet P3 fires on it. The ruling's premise (audience + rewritability) is a *class*; the code encodes three literal paths. Conversely, the doctrine's claim that the repo plane "covers only the prose the principal reads — doctrine, ruling asks, review briefs, the live roadmap" overstates the other way: the scope is `docs/`, so root `README.md`, `CLAUDE.md`, `AUTONOMY.md` — prose the principal certainly reads — are not scanned at all. Neither direction is wrong to build; the doctrine should say what the code does. (CMF4)

**Is fail-open the right posture for a gate on the principal's own reading surface?** Fail-open, yes — a linter that can wedge a session is worse than the miss, and every path was verified to exit 0 (malformed JSON, empty stdin, wrong-typed field, engine unreachable). Fail-open *and silent*, no: `systemMessage` would have made "the gate is gone" visible without wedging anything, and the delta's own later commit (`e390382`) notes that removing the engine "would silently kill the reply gate … the wall would vanish without a sound" — that is a property of this design, not of fail-open. A gate whose absence is indistinguishable from its success is the "written down, therefore assumed working" shape the scanner was built to end. (CMF6)

**Two premises the brief did not name and I attacked anyway.** *Threat enumeration at design time* (REVIEW.md lens 4's build-time obligation): none is recorded for a hook that runs machine-wide on every reply and imports engine code from a working tree — CMF6. *The measurement's rules vs the shipped rules*: the doctrine's "37% to 67%" was measured with a 25-character aside threshold and against a sentence cap that had no prior doctrine; the shipped repo plane is 35/40 and the reply plane 45/60 — CMF3.

## Lens 2 — correctness & quality (everything re-run, nothing read)

All commands ran from the scratch clone (`…/scratchpad/cmf-clone`) at `e390382`, or from this worktree at HEAD read-only, as marked. `date -u` at verdict-writing: 2026-08-15, about 1400 UTC.

| Claim (where) | Command | Observed |
|---|---|---|
| Module tests 47 at `c374959`, `b879b02`; 51 at `e390382` (`e390382` message, board) | `python3 -m unittest tools.test_plainscan` at each commit | **47 / 47 / 51, all OK** ✅ |
| Advisory tally 7,817 → 4,440 at the landing tree (`e390382`, COMMUNICATION.md, floor.py) | `python3 tools/plainscan.py --root . docs --warn` and `… --include-records`, at `e390382` | **4,440** (P1 518 · P2 215 · P3 2,153 · P4 1,554) and **7,817** (P1 1,194 · P2 428 · P3 3,471 · P4 2,724) — records carried 3,377 ✅ exact |
| Same at HEAD (`b4fe720`; surfaces identical to `738afd9`) | same, in the worktree | **4,598** default / **8,028** with records; heaviest at HEAD `docs/method/REVIEW.md ×89`, `CONCURRENCY.md ×81`, one 2026-07-19 verdict ×70 |
| "first run" tally: 7,940 (floor.py comment) · ~7,900 (README, `c374959` msg) · 7,379 (`render_human` docstring, `beaf240`) · 7,817 (rescope baseline) | — | four figures for one fact, undated; the only reproducible one is 7,817 (CMF3) |
| Full python suite green at the landing tree; the Stop-hook flake fixed (`b879b02`: "8 consecutive clean runs"; board item 120 reports 2 tests red about 1 run in 2 in the full run) | `python3 -m unittest discover -s tools -p 'test_*.py'` ×5 at `e390382`; module ×6 at `e390382`, ×5 at HEAD | **1,298 tests, 5/5 OK** (140–157 s each); module **11/11 OK**; at clone `main` full suite **1,321 tests, 2/2 OK**. The flake did **not** reproduce ✅ |
| Instrument tests exit 0 | `node --test instruments/*.test.js` at HEAD | 235 pass, 0 fail ✅ |
| Floor on both planes at HEAD; plainscan warn-only, exit 0 | `python3 tools/floor.py --plane hook --root . --tools ./tools`; `--plane ci --root .`; `--selftest` | hook **exit 0**, ci **exit 0**, selftest ok (15 scanners); plainscan line `👁️ warn-only`, 4,598 findings printed as tally + 6 ✅ |
| `plainscan --selftest` OK | at `e390382` | `selftest OK`, exit 0 ✅ |
| Hook: clean passes, bad blocks, malformed fails open, repeated id gives up after 2 (README, docstring, tests) | `cmf-hook-drive.py` — 20 payloads piped to `/usr/bin/python3 tools/hooks/plain-reply.py` with `PLAIN_REPLY_STATE` pointed into the scratchpad | clean → no output, exit 0; bad → `decision: block` naming P1/P3/P4 at the chat limits (45/60); `not json`, empty stdin, JSON array, non-string message, missing field → exit 0, no output, state untouched; same id ×3 → block, block, then `hookSpecificOutput.additionalContext` and the entry popped; 4th → block again at count 1; engine unreachable (hook copied out of tree, `ATELIER_TOOLS` and `HOME` pointed at an empty dir) → exit 0, silent; entry older than 6 h dropped on load ✅ shape as claimed — semantics not (CMF2) |
| Hook: "gives up after two blocked rewrites of **one turn**" (docstring, README) | drive: bad → short ack (<200 chars) → bad → bad, one id | the short reply did **not** reset the count: block, (silent), block, give-up — the streak is per session-until-a-clean-long-reply, not per turn ❌ (CMF2) |
| Hook honours `stop_hook_active` | payload with `stop_hook_active: true` | ignored — blocked normally ❌ (CMF2) |
| Missing `session_id` | three id-less bad payloads | all share the `"unknown"` bucket → the third gives up (CMF8) |
| Live install (brief §3; README install form) | `~/.claude/settings.json` read for shape only | **no `hooks` key at all** — Stop and SubagentStop stanzas: 0; `plain-reply` not mentioned. The gate is **not wired** on this machine at review time. A 233-byte `~/.claude/.plain-reply-state.json` remains (session-id keys, a 16-hex hash prefix, a count, a timestamp — no reply text; not opened beyond its size) |
| `RECORDS_GLOBS` matches what the doctrine says | `iter_markdown` read + selftest + `--include-records` delta | exactly `docs/SESSIONS.md`, `docs/sessions/**`, `docs/ROADMAP-DONE.md`, only when a directory is expanded; `docs/ROADMAP.md` not swept (test pinned) ✅ — see CMF4 for what the same argument also covers |
| Repo without `docs/` | `plainscan --warn --root . docs` in an empty dir; floor.py L1719–1729 | plainscan exits 2 ("path does not exist"); floor skips docs-scoped checks visibly ("skipped … no docs tree") — no child breakage ✅ |
| Rule edge probes (`cmf-probe.py`, engine at `e390382`) | 29 specimens | P1 fires on `SHA256`, `MD5`, `UTF8`, `S3`, `EC2`, `M2`, `P3`, `ABC123` (a plate-shaped token); passes `HTTP2` only because it is 4 letters; comma apposition ("F1, the missing stamp, is closed") flagged; en-dash/paren/`=` glosses cleared; P2 silent on `SWIFT` (dictionary word ≥4 letters ⇒ "shouted"); P4 misses a buried aside containing a nested bracket, and never looks at square brackets; a blockquoted 45-word sentence flagged; te reo macrons counted correctly (CMF5) |
| P1/P2 ground quote (digital.govt.nz "expand … the first time you use them") | `curl`, headless Chromium and Firefox fetch, Wayback | site bot-walled (Incapsula), archive rate-limited — **could not verify** at review time (CMF9) |
| Doctrine's "37% to 67%" | `c374959` message vs COMMUNICATION.md | message: 67.2 / 55.5 / 36.8 / **17.4** — the doctrine's range drops the 17.4 (P1); the 67.2 was measured at a **25-char** aside threshold while the shipped defaults are 40 (repo) / 60 (reply); the pre-delta doctrine (`c374959^`) has a bracket-aside rule dated 2026-07-15 and "define or drop the jargon" — **no sentence-length rule and no reference-code rule** existed to be "written down and not followed" (CMF3) |
| The 6,704-reply measurement | — | **not re-runnable** from the repo (private transcript corpus); reviewed as method only: rules, thresholds, denominator (replies ≥200 chars) and window are stated; the thresholds used were not all the shipped ones, and "reference-code density rose" measures density, not bare first use, so it is confounded by workload (August was review-heavy) — direction plausible, figures as printed in doctrine not supportable (CMF3) |
| Hook code at HEAD = code at landing | `md5` of both files from `from __future__` down | identical (`d0c70c9f…`); `plainscan.py`, `test_plainscan.py` unchanged since `e390382`; `floor.py` gained only the `board` entry ✅ |
| README/docstring at HEAD still say the give-up path is visible | `grep -n 'visible note\|visibly' tools/hooks/plain-reply.py tools/README.md` | hook L65 "findings appended as a visible note. The principal sees the mess AND sees that the wall fired"; README L852 "saying so visibly in the transcript" — both stand at HEAD, not corrected by `cd6232b` (CMF2) |

Honesty of the record otherwise: `c374959` said "NOT INSTALLED" and `171862b` corrected it the same day; the P5 build/measure/reject is stated as such; the flake fix names its own defect. Those are the apex working. `cd6232b`'s "Detection was sound throughout" (HEAD COMMUNICATION.md L108) is contradicted by its own "triggers were near-misses and board item identifiers" and by the probes above; it belongs to the RG pass and is only cross-referenced here (CMF5).

## Lens 3 — completeness / harvest

- **The checkable/judgement boundary.** The doctrine's "checkable" list is exactly P1–P4 and the "stays judgement" list is honest. Two boundary cases the delta did not test: (i) checkable-in-principle but *unfixable-in-place* prose — a verbatim principal quote, a withdrawn verdict — where a finding is noise by the ruling's own logic (CMF4); (ii) shape-checkable but *not* judgement-free — P1's shape rule cannot tell a finding ID from a product name (CMF5). The person-level layer (the calibration itself) is correctly left as unreachable.
- **Grounds.** P4 — dated house doctrine, verified in `c374959^` ✅. P3 — house call, honestly labelled; "two authorities checked" is unverifiable as recorded (no URLs, no dates). P1/P2 — "published" is an acronym clause applied by analogy to reference codes; defensible, but not the same as published (CMF9).
- **Landing = queuing.** Pointer 300 discloses it was queued one commit late; the rescope pointer landed in `959502d`, three minutes after `e390382`, in a records-only commit — the TA9 shape, meeting the intent while the grammar names no commit (CMF7). Board item 120 (the flake) is still `[ ]` although `b879b02` fixed it and the item asks to be closed if a fix landed (CMF7). `CHANGELOG.md` at HEAD has **no** entry for plainscan, the hook, the rescope, or (later) the unwiring, while sibling scanners have 32 lines (CMF7).
- **Duplication.** None found: the engine is single-sourced and both planes call `scan_text` (verified by import path); no vendored copy of the rules elsewhere in `tools/` (`grep -rn 'SENTENCE_LIMIT\|RE_REFID' tools` → plainscan.py, its test, the hook only).
- **What the correction leaves in the person-level layer.** Ordering, dosage, icon aptness, survey-vs-recommendation — the doctrine names them; nothing else was found hiding behind "checkable".

## Lens 4 — security & privacy

**Reach case for `/security-review`.** Landed-delta review with code, so I aimed the scanner at a scratch clone (`…/scratchpad/cmf-sec`) with the delta re-applied as a pending diff — the sanctioned shape. The skill's harness ignored the aim and read this **worktree's** pending diff instead, which was records/briefs (markdown only) — definitionally empty for the scanner *and* the SL2 exposure disclosed above. So the mechanical floor was delivered by a general-purpose subagent given the same objective and exclusions over the scratch clone's diff, code paths only. Its result: **no finding at ≥8/10 confidence**; two sub-threshold observations, both folded into CMF6/CMF8: O1 (medium impact, 5/10) — a machine-wide Stop hook that imports engine code from a branch-tracking working tree of a public repo, silently on error; O2 (low, 4/10) — `rglob` follows symlinked `*.md` files, same as the `wrapscan`/`leakscan` precedent, no new capability. Its explicit answers: engine shadowing needs write access to a trusted path (env, atelier `tools/`, `~/.pets/atelier/tools`), never cwd; the state file holds no reply text (session id → 16-hex hash prefix, count, epoch); the block reason quotes excerpts of the same session's reply back into that session only; the CLI recites ≤70-char excerpts only from files it scans (ignored/records files are never opened); `errors="replace"` and `re.escape` leave no injection surface.

**Design altitude, my own.** (1) No threat enumeration is recorded anywhere in the delta for a hook that runs on every reply in every repo on the machine — REVIEW.md lens 4 says absent enumeration is the finding. (2) Where recited text goes: reply plane — back into the same session's context (no cross-session path; the state file carries hashes only); repo plane — excerpts into pre-commit output and CI logs, which for a public repo are public but so is the prose excerpted; `--json` carries excerpts too. No path found by which a private repo's reply reaches a public tree. (3) The state file at `~/.claude/` holds session ids from every repo — coordination data, not secret; TTL 6 h; a stale 233-byte file remains after unwiring. (4) atelier is PUBLIC: nothing in the delta joins a private repo's name to its posture; the transcript-corpus figures are counts. This verdict names no private repo and quotes no transcript. (5) `/usr/bin/python3` pin and exec form are sound choices; `timeout: 15` bounds a hung engine. (CMF6)

## Findings

**CMF1 (MAJOR)** — The reply plane's premise is false by the hook contract: a `Stop`-hook block cannot make the flawed reply unread.
*What/where.* `c374959` message ("rewritten before Mike ever reads it"); hook docstring L10–11 and README L823–824 at `e390382`; COMMUNICATION.md L97–98 at `e390382`. *Evidence.* Claude Code hooks reference (2026-08-15): `Stop` receives "the text content of Claude's final response"; `block` "prevents Claude from stopping; Claude continues the conversation"; nothing retracts output. Formed before reading `cd6232b`; `cd6232b` reaches the same conclusion from transcripts and unwired the hook, and its rewrite of the three surfaces stands at HEAD. *Why it matters.* The one plane the delta calls "the point" was built on an unchecked claim about the harness, and the doctrine carried that claim as fact for six days across every repo the hook ran in. *Counsel* (the principal decides): the doctrine correction at HEAD is the right shape; what this pass would have asked for had `cd6232b` not — a class rule, "prove the enforcement point can deliver the remedy" — `cd6232b` states, and the RG pass will test it. Nothing further to apply from this pass on CMF1 beyond the CMF2 residue.

**CMF2 (MODERATE)** — The give-up path is neither a give-up nor visible, and the anti-deadlock guard is per session, not per turn — the tests pin the shape, not the semantics.
*What/where.* `plain-reply.py` L185–197 returns `hookSpecificOutput.additionalContext`; docstring L39–46 (HEAD L60–67) and README L831–832 (HEAD L851–852) say the reply is let through "with the findings appended as a visible note … the principal sees the mess AND sees that the wall fired". *Evidence.* Docs: `additionalContext` "doesn't appear as a chat message in the interface" and on `Stop` "keeps the conversation going through the same loop protections as `decision: "block"`"; the user-visible field is `systemMessage`. Live: a short reply between two bad ones does not reset the count; `stop_hook_active` (the documented input for exactly this) is ignored; `sig` is written and never read, so "remembers the last text it blocked" is not implemented. `test_gives_up_rather_than_wedging_the_session` asserts the JSON shape only. *Why it matters.* Under the documented behaviour the "cap" was another continuation, so a stubborn turn could run to the harness's own 8-block ceiling — up to nine copies, not three; and the wording stands at HEAD after `cd6232b`. *Counsel:* if the hook is ever repurposed, the give-up branch should emit `systemMessage` (visible, turn ends) and honour `stop_hook_active`; if destroyed, delete the two sentences with it. Either way, correct L60–67 and README L851–852 now, since a reader at HEAD is told to believe the docstring.

**CMF3 (MODERATE)** — The doctrine's measurement claims misstate the measurement.
*What/where.* COMMUNICATION.md L112–120 at `e390382` (unchanged at HEAD): "broken in 37% to 67% of replies depending on the rule … the rate did not fall after they were written down". *Evidence.* `c374959`'s own table: 67.2 / 55.5 / 36.8 / **17.4** — the range omits P1; the 67.2 was measured at a 25-char aside threshold while the shipped defaults are 40/60 (at 45/60 the reply gate "would have fired on 30.6%", `171862b`); the pre-delta doctrine had no sentence cap and no reference-code rule, so for P3 and P1 there was nothing written down to fail to fall; "reference-code density rose" is a density, not the bare-first-use rate the rule is about, and is confounded by a review-heavy month. Four different "first run" tallies across floor.py / README / `render_human` / rescope, undated. Corpus not re-runnable. *Why it matters.* Doctrine cites these figures as the reason the correction "was owed rather than optional"; a public doctrine's numbers should survive a reader checking them against the same repo's commit messages. *Counsel:* restate as "17% to 67% at the thresholds measured (25-char aside; 35-word sentence), of which two rules pre-existed as doctrine", or drop the range and keep the one robust claim (86% of first uses bare); date and single-source the first-run tally.

**CMF4 (MODERATE)** — The rescope's argument is a class; its code is three paths — and the doctrine overstates the plane's coverage in both directions.
*What/where.* `RECORDS_GLOBS` (plainscan.py L450); COMMUNICATION.md L100–110 ("covers only the prose the principal reads — doctrine, ruling asks, review briefs, the live roadmap"). *Evidence.* HEAD tallies: `docs/reviews/` 3,392 of 4,598 (74%), of which `withdrawn/` 77 — verbatim-preserved by REVIEW.md; RECORD.md names `SESSIONS-ARCHIVE.md` as a record store, not in the globs; a blockquoted 45-word principal quote fires P3 with no honest fix. Root `README.md` / `CLAUDE.md` / `AUTONOMY.md` are outside the `docs` scope and unscanned. *Why it matters.* The principal's opening position (board narrative) was that most repo prose is agent-facing; the accepted counter was "keep the floor where the human reads". What shipped keeps 74% of the remaining tally on closed review text and misses the root files he reads most. Not wrong to build; wrong to describe as done. *Counsel:* either state the scoping as "three paths, by name" in doctrine, or scope by class (open briefs, live roadmap, doctrine, ADRs, root prose) and let `--include-records` mean the rest; the reply-plane sentence is moot at HEAD.

**CMF5 (MODERATE)** — P1's shape rule cannot tell a reference code from a product name, and on the reply plane that blocked.
*What/where.* `RE_REFID` (plainscan.py L120), `BLOCKING_RULES` (hook L62). *Evidence.* Probes: `SHA256`, `MD5`, `UTF8`, `S3`, `EC2`, `M2`, `ABC123` (a plate-shaped token) all fire P1; comma apposition unrecognised as a gloss; P2 blind to dictionary-word acronyms (`SWIFT`); P4 misses nested-bracket asides and never sees square brackets. `cd6232b` itself: "triggers were near-misses and board item identifiers" — yet its HEAD text says "detection was sound throughout" (RG-pass territory; cross-referenced). *Why it matters.* On the repo plane it inflates an advisory tally the doctrine calls a backlog; on the reply plane it produced false blocks with real reader cost (CMF1). The doctrine's "checkable without judgement" is true of the count, not of the classification. *Counsel:* an allow-list of product shapes is the wrong fix (the H1–H6 argument in the tests is right); the honest fix is to state that P1 is a *shape heuristic* and keep it advisory on every plane; recognise the comma-apposition gloss.

**CMF6 (MODERATE)** — No threat enumeration for a machine-wide hook that runs branch-tracking code from a public repo, fail-open and silent.
*What/where.* README install form (hook path `<atelier>/tools/hooks/plain-reply.py`, user-level settings); `_engine()` L84–99; fail-open L143–147, L153–155, L164–165, L206–210. *Evidence.* Security subagent O1 (5/10): every Stop in every session on the machine executes whatever `plainscan.py` is checked out in atelier's tree — a `gh pr checkout` of a fork PR on this PUBLIC repo changes machine-wide hook code until the branch is switched back — and any exception is swallowed. Engine-missing drive: exit 0, no output. No design-time threat list anywhere in the delta. *Why it matters.* REVIEW.md lens 4 makes enumeration a build step; the two threats that bear on this class (supply chain via the working tree; silent loss of the control) were both live and unnamed. Mitigated at HEAD only because the hook is unwired; the install form is kept "for the record". *Counsel:* if reinstated in any form, run from an immutable copy or a pinned `ATELIER_TOOLS`, and emit `systemMessage` on engine-import failure so absence is visible; record the threat list in the file that carries the install form.

**CMF7 (minor)** — Bookkeeping the delta owed and did not close.
*Evidence.* Rescope pointer queued in `959502d`, three minutes after `e390382` (TA9 shape); pointer 300 self-discloses one commit late; board item 120 (the flake) still open though `b879b02` fixed it and 5/5 + 11/11 runs confirm; `CHANGELOG.md` silent on plainscan/hook/rescope while sibling scanners have 32 lines. *Counsel:* close 120 with the run counts above; one CHANGELOG entry covering `c374959`…`e390382` (and the unwiring, if the RG pass agrees).

**CMF8 (minor)** — Small hook defects, none security: `sig` unused; id-less payloads share an `"unknown"` bucket; non-atomic read-modify-write of the state file across concurrent sessions (a torn write parses as `{}` and fails open); `test_malformed_input_fails_open` runs without `PLAIN_REPLY_STATE` (harmless — it exits before touching state — but the isolation `b879b02` promised is not total). *Counsel:* fold into whatever CMF2's ruling does with the file.

**CMF9 (note)** — P1/P2's "published ground" is an acronym clause applied by analogy to reference codes, and the quoted digital.govt.nz sentence could not be verified at review time (site bot-walled to three fetch methods; archive rate-limited); P3's "two authorities checked" carries no URL or date. Not a defect in the rule; a gap in the grounding trail a public doctrine should let a reader follow.

**CMF10 (note)** — Verified true, recorded so nobody re-chases: 47/47/51 tests at the three landing commits; 7,817 → 4,440 exact at `e390382`; the flake did not reproduce in 5 full-suite and 11 module runs; floor exit 0 on both planes at HEAD; hook fail-open on every malformed path; live install absent at review time.

## Overall

**FAIL — 1 MAJOR / 5 MODERATE / 2 minor / 2 note.** The repo plane and its rescope are sound work with overstated doctrine around them; the reply plane — which the delta itself calls "the point" — rested on an unchecked claim about the harness and is already unwired on that ground. An author must: (CMF2) correct the give-up-path wording at HEAD in the hook docstring and README, and record whether `stop_hook_active`/`systemMessage` are used if the file is repurposed; (CMF3) restate the doctrine's measurement figures to match the commit's own table and thresholds, or drop the range; (CMF4) make the doctrine say what `RECORDS_GLOBS` and the `docs` scope actually cover, or widen the class; (CMF5) label P1 a shape heuristic; (CMF6) write the threat list beside the install form and pin the engine path if anything is reinstated; (CMF7) close item 120 and add the CHANGELOG entry. Findings on doctrine are the principal's to rule (rule 3); counsel above is labelled as such.

## Follow-up checklist

- [ ] **CMF1** — no further apply beyond CMF2; tested by the RG pass's reconcile confirming the HEAD correction says what the harness does (docs citation, or one live block observed on a terminal).
- [ ] **CMF2** — hook L60–67 and README L851–852 corrected; if repurposed, the give-up emits `systemMessage` and reads `stop_hook_active`; tested by a drive where a short reply between blocks changes nothing and the give-up JSON carries `systemMessage`, plus a unit test asserting the field.
- [ ] **CMF3** — COMMUNICATION.md L112–120 restated; tested by reading the paragraph beside `c374959`'s table and finding every figure and threshold in both.
- [ ] **CMF4** — doctrine says "three named paths" or code scopes by class; tested by `plainscan --root . docs --warn` heaviest-three no longer being closed review text, or by the doctrine sentence naming the paths.
- [ ] **CMF5** — P1 labelled a shape heuristic in README/plainscan docstring; comma-apposition gloss added with a test ("F1, the missing stamp, is closed" → no P1).
- [ ] **CMF6** — threat list recorded beside the install form; `_engine()` prefers a pinned path if reinstated; tested by a drive with the tree switched to a foreign branch showing the pinned engine still runs.
- [ ] **CMF7** — item 120 closed `[x]` with run counts; CHANGELOG entry present; tested by `board.py rebuild` and `grep -n plainscan CHANGELOG.md`.
- [ ] **CMF8** — folded into CMF2's ruling; tested by the same drive.
- [ ] **CMF9** — grounding trail: URL + fetch date for the digital.govt.nz clause and the two P3 authorities; tested by a reader following the links.
- [ ] **CMF10** — nothing to do.
