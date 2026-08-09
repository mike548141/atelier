# 2026-08-09 · 0813 UTC · Five build lanes from the unclaimed queue (Opus orchestrating, four Opus workers)

Mike's ask: *"Carry on with any work in queue that's not claimed and you are
capable of until the economics suggest a new session"*, with a standing
instruction to challenge his framing and to claim before working. Three sessions
ran in parallel for most of it, which is a large part of what this record is
about.

## The selection, and the challenge that shaped it

The board carries 113 open items. A subagent inventory of the whole file put
**~28 of them behind Mike's ruling rather than behind capacity**, plus seven
`⏳` cold passes waiting to be taken.

The obvious move was to take the cold passes. **It was declined, and the reason
is recorded because it is a judgement Mike may want to overrule:** the queue is
*ruling-starved, not review-starved*. Seven more verdicts would have added
findings to the pile already scheduled for a dedicated residue sitting, while
subtracting nothing from it. So the session took five funded, ruling-free build
items across four file-disjoint lanes instead. Raised with Mike as a concern, not
a decision taken over his head — and it turned out to matter for a second reason:
a parallel session took the review lane two minutes after this one claimed.

Claimed on `main` at 0813 UTC before any work, per `CONCURRENCY.md` § *Claiming
work*. Seven items, one claim commit, then the worktree.

## What landed

Five lanes, four run by Opus workers on one shared worktree with no git of their
own; the orchestrator verified every claim independently before committing. Each
number below was re-read from the tree, not lifted from a worker's report.

**`secretscan` — the last invisible subtraction.** `PUBLIC_KEY_RX` skips a
line's entropy pass, and predated the counted-suppression model, so what it wrote
off appeared in no tally. **The crux was whether the finding was still true**: the
clean line already ends `1 public-key fingerprint(s)`, which reads like the same
thing and is a *different* subtraction (E3's carve-out, counted inside the entropy
loop). Settled by probe — the same 68-char body naming `ssh-ed25519` went clean
with every tally at zero, while the bare control returned a blocking finding. A
blocking finding vanished and no number moved. On this tree it was hiding **two**
real suppressions. Tests 122 → 134.

**`ccarchive` — the subagent `.meta.json` capture class**, funded by Mike
2026-07-28. Scoped to `subagents/` rather than name-matched at any depth, with the
cost of the narrow reading stated rather than buried. Two of the item's five build
notes needed **no code** — restore mapping and manifest/integrity fall out of
keying on `<rel>.gz` — and were proved rather than reasoned. The shrink guard
turned out **inert** on this class (0 of 545 sidecars rewritten more than a second
after creation), so nothing was carved into a working guard for an event never
observed. Tests 95 → 99.

**`worktree.py` — both recorded bugs.** Repo identity now comes from
`git worktree list --porcelain`, and `remove`'s merged-guard asks
`origin/<main>` before local `<main>`. Tests 12 → 27 on the module.

**`cctranscript --search`** — Mike's 2026-07-26 ask, designed 2026-07-27, built
here. Gate-first, UTF-8, `/i` case-folding, no index; latin1 rejected outright
because it corrupts macrons. Tests 38 → 62. It also closed the design's named
doctrinal loose end: `instruments/README.md`'s `--materialise` note argued the
flag's *absence* was principled because cctranscript never read every file, and
`--search` **is** the bulk read.

**The board's own honesty.** Two `[ ]` items the tree had already closed came off
the hot path — the spellscan reason class and the floor-local-seam verdict
pointer. Both verified against live code first: 14 regex sites across 12 scanners
re-enumerated at HEAD rather than trusted to a commit message, and all five LS
fixes traced to running code. The second had **diagnosed itself** as residue in
its own text and still sat there as `[ ] 🎯`, inflating the count of rulings Mike
was said to owe. Naming residue is not clearing it.

**The parent stopped being exempt.** `.atelier-floor.json`'s `scope` block
migrated to the reasoned spelling, reasons **lifted** from the WS1 and 2026-07-23
rulings and PS4's ground — never invented — with each declaration also stating
what cover it gives up. This clears the atelier-side precondition C1b phase 2
names.

## Three of the fixes corrected the items that commissioned them

This is the most transferable result of the session.

- **`worktree.py`'s heading named the wrong cause.** It said the *branch* was
  resolved from the cwd. The branch was always per-worktree and always right — the
  entry half-admitted it by noting `git branch --show-current` agreed. What came
  from the cwd was **repo identity**. And the ahead/behind counts were never
  dropped, only *suppressed* by a wrongly-true `is_main`.
- **Every figure in the ccarchive item was stale**, all larger: 425 → 545
  sidecars, 66 KB → 85.8 KB, 418 → 521 archived logs, and 538 → 545 *inside one
  session* because agents were spawning while it was counted. The census *shape*
  held exactly.
- **The search design's "the refs are free" was wrong at file grain.** An `N.M`
  ref counts every preceding turn, so parse-only-the-survivors and exact
  gate-invariant refs are mutually exclusive. Correctness was chosen and **DONE
  condition 13 is recorded as PARTIALLY met** — 1.22–1.32× a bare read for a
  selective term, 3.7× for one present in every session.

An item that misnames its own mechanism sends the next reader to the wrong
function; a figure that is stale in the safe direction still cannot be quoted.

## Concurrency: three live sessions, and one incident that was mine

Two other sessions ran alongside this one. A **Fable review session** claimed the
seven `⏳` cold passes at 0815 UTC — two minutes after this session's claim — and
landed four verdicts, every cycle CLOSED at 0 MAJOR. A **third session** built a
new `plainscan` scanner directly on `main`. Neither lane overlapped this one's
files.

**The incident, stated first.** The review session wrote its seven briefs into the
primary checkout while this session had uncommitted roadmap edits there. On
finding them, this session reverted `docs/ROADMAP.md` **wholesale** to get its own
edits out of another session's tree — and that revert discarded 21 lines of the
reviewer's in-flight pointer edits. Nothing was lost: it had already committed
identical content to its own worktree branch, verified byte-identical afterwards,
and its 21 lines were stripped back out of this branch so its branch kept
authorship.

The rule inverted is `CONCURRENCY.md`'s own, and the gap is worth naming:
**CF3 covers the tree you arrive at dirty** — "stage and commit your own hunk
alone, nothing else" — and says nothing about the tree that turns dirty **under
you**, which the flipped prior makes the commoner case. A file-level `git checkout
--` silently ignores the distinction.

**One thing deliberately not done:** the reviewer was not messaged. A courtesy
note mid-rule-4-cold-pass contaminates exactly the independence the rule exists
for; the session record is the channel that costs the reviewer nothing.

**A false liveness read, also worth carrying.** This session twice inferred a
worker's liveness from file mtimes read in the *wrong tree* — the shell's working
directory had silently reverted to the primary checkout, whose copies of those
files were a month old. The commits were unaffected (verified afterwards by
reading the committed blobs back), but the inference was worthless. Absolute
paths, never a persistent cwd.

## A flaky test found on the way past, and a hypothesis the control killed

Rebasing onto `main` brought in the third session's `plainscan`, and the full tool
suite went red on two `StopHook` tests. **Four full runs on byte-identical
content: red, green, red, green.** The module alone passes 47/47 every time. So
they are flaky, and because the tool suite gates the pre-commit hook and CI, a
50% flake fails commits at random — landing on whoever commits next rather than on
the author. `main`'s CI is green on those commits, but that is a coin landing
heads.

**The false lead is recorded because it is the more instructive half.** The first
hypothesis was a `GITHUB_ACTIONS`/`CI` env gate, since a run with those set came
back green — the repo's own memory records the *opposite* direction as a known
trap, so it fitted. The control falsified it: a plain re-run also came back green.
The variable is run-to-run, not environmental. Queued, not diagnosed further and
not fixed — it is another session's live lane.

## Findings queued rather than taken

Eight, none of them in a claimed lane:

- **`ccarchive` exits 1 on every scheduled run** — a live red nobody had
  recorded, predating this work. Two legitimately-condensed whole-document files
  trip the suspect-shrink guard, so the daily job carries a non-zero exit and
  those two mirrors are frozen at pre-condensation bytes. Verified independently
  read-only. Not fixed at discovery on purpose: the real question is the *class*
  (the guard assumes append-only growth, false of any whole document), and carving
  an exception into a working guard for an unruled event pattern is fitting the
  limit to the measurement. The two paths are unnamed here — they identify a
  personal project and a private repo, and this repo is public.
- **Five pre-existing `worktree.py` defects**, one of which must not be taken
  quietly: `list`'s ↑/↓ carries the same stale-local-`main` referent `remove` just
  lost, and fixing it changes what "behind" *means* on a widely-read board.
- **Archive-mode pool construction dominates every `--from-archive` run** —
  pre-existing; `--search` only made it visible.
- **The flaky `StopHook` tests** above.

## What was checked and NOT recorded

`floorfleet` renders a `scope` narrowing's paths but not its `why`, which looked
like it half-defeated the migration above. Checked against the artefact before
recording anything: `_scope_paths`' own docstring says the omission is **decided
design** — "the 🔎 line's job is to say where a check looks, and a repo that
narrowed a boundary check is already the thing being pointed at". Not a defect,
not queued. The standing rule that a blocker reasoned from how a mechanism works
must meet the real artefact once before it becomes a record earned its keep.

## Evidence

Floor exit 0 on the rebased tree, all thirteen checks; the only ⚠ is
`ROADMAP.md`'s pre-existing size advisory, which never gates. Instruments
235/235. Tool suite 1284 — **with the flake above, so a single green run is not
proof**; the lanes' own modules are deterministic (secretscan 134, worktree 27,
plainscan 47 alone). Pushed floor runs came back `conclusion=success`, read as a
conclusion rather than as "the run finished", on both intermediate pushes.

One rebase conflict, in `docs/ROADMAP.md` § *Doctrine — review-owed*, resolved
keep-both: the reviewer's closed child-membership cycle is newer truth, and this
session's new `⏳` pointer sits above it.

## Close — two rulings, and what they did NOT settle

Mike reviewed the state after all three parallel sessions closed, and ruled twice.

**AP1: a ruleset with owner bypass, plus a machine-check.** Applied the same day
as ruleset `20603641` — `deletion`, `non_fast_forward`, `required_signatures`,
active on the default branch. The three were chosen so that none can block an
ordinary signed fast-forward push: the standing direct-push grant is untouched,
and a parallel session was mid-work when it landed and was unaffected. Proven
rather than assumed, in both directions — the endpoint AP1 read as `[]` now
returns all three rules, and a real push succeeded afterwards.

**What the record deliberately does not claim.** AP1 stays OPEN. The machine-check
Mike also ruled does not exist, so nothing would notice if the ruleset were
deleted — which is the state AP1 condemned, one layer up. The admin bypass is a
real limit and was disclosed before he chose it: the control guards against
accident and third-party push, never against compromise of his own token. And the
registry-review leg is still post-hoc. ADR 0008's clause is therefore closer to
true and still not true; re-wording it is a doctrine edit owed its own `⏳`, and it
was kept out of the platform commit so the record never carries an ADR revision
with no review behind it.

**The residue round runs in a fresh session.** Offered four approaches — triage
first, sit as-is, split by severity, or delegate a defined class to the agent —
Mike took none and scoped the work out of the session that raised it. What the
next session inherits is now written on the board as measured figures rather than
recollection, together with the standing expectation that the number shrinks on
contact: two items closed today had rulings already made, applied and verified.

**Economics.** The session stopped here on Mike's instruction rather than on
capacity. Five build lanes, nine findings queued, two rulings recorded, and the
one platform change that closes a live security gap — with the gap honestly
described as narrowed rather than closed.
