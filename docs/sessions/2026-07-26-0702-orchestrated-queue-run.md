# 2026-07-26 · 0702 UTC · Orchestrated queue run — ccrepo v3, cctranscript agents, ccarchive encryption design

**Model:** Opus 5 orchestrator (Mike's stop-if-wrong-model check — Opus, correct).
Workers: 2 × Opus build, 1 × Opus design, 1 × Sonnet build; three items taken
inline by the orchestrator. A **review session ran in parallel** throughout and
held its own three items; no collision.

**Mike's brief:** maximise plan use, start with ccrepo then cctranscript/ccarchive,
carry on with unclaimed queue work, worktrees for parallel safety, claim before
working and never touch a claimed item. Closed early at Mike's request ("I worry
this session has got too big") with one worker still mid-flight — handed over on
breadcrumbs rather than run to exhaustion.

## What landed

| # | Item | Where |
|---|---|---|
| 1 | ccrepo **time-bounded price table** (v3 ask 1) | `7cf8163` → `70bc1ad` |
| 2 | ccrepo **`-g session`** (v3 ask 3) | `7cf8163` → `70bc1ad` |
| 3 | cctranscript **agents finished beside agents started** | `3b38f3d` → `99d43d1` |
| 4 | ccarchive **encryption-at-rest design pass** | `d913698` → `7701a62` |
| 5 | linkscan **names the fix** when the path is computable | `b89a306` |
| 6 | floorfleet **reads the tracked shim** on the remote plane | `b6d6c8b` |
| 7 | ccrepo **`--context` session-peak filter** (v3 ask 2) | `791bea6` |
| 8 | Roadmap captures: transcript search, two corrections, one doctrine candidate | several |

Floor green at head throughout except one self-inflicted window (below).
Tests: node 180 → 202; python 661 → 673.

## The five things worth carrying forward

**1. Two recorded blockers were false, and both were false the same way.**
The cctranscript agent count had been deferred because "archive mode resolves a
single file, so a directory-sourced count reads zero". It doesn't — ccarchive's
`captureClass` allows any `.jsonl` at *any depth*, so `subagents/` is mirrored;
**92 such directories exist in the live archive**, and a session renders an
identical header live and archived. Separately, the ccarchive encryption item
said AEAD "isn't in Python stdlib ⇒ needs a crypto dep" — true for `tools/`, but
the instruments are **Node**, and `node:crypto` ships `aes-256-gcm`,
`chacha20-poly1305`, X25519, `hkdfSync` and `scryptSync` (verified directly).
Both blockers were reasoned from **how a mechanism works** rather than from
**what is actually there**, and in both cases one command settled it. That is a
repeatable failure shape, not two coincidences: *a deferral justified by
inference deserves one check against the artefact before it is written down.*

**2. The pushed floor caught me, exactly where the rule says it will.**
Marking three items `[x]` and harvesting to ROADMAP-DONE in the *next* commit
left `d847866` red on the pushed floor (`0485540` green). Local scans were green
the whole time, because the harvest was already on disk before the first push was
checked. Captured as a **doctrine candidate**: an `[x]` and its harvest belong in
one commit. It is AWA2's shape with a different marker — the `⏳` pointer rides
the landing commit so no window exists — and the generalisation worth naming if a
third case appears is *a state change and the bookkeeping the floor demands of it
ship together.* **Dogfooded immediately**: the ccarchive and floorfleet items were
both marked and harvested in a single commit, and the floor never went red again.
Not enacted as doctrine here — rule 4 binds the author out of reviewing it.

**3. `finished` counts logs, not successes — found by using the feature.**
This session started six subagents and **three died** (two watchdog stalls, one
connection closed mid-response), yet its own header read `6 agents started ·
6 finished`: a crashed agent has already written its log. So the started/finished
gap catches a spawn that **never began** and is blind to one that began and
**fell over** — which is the failure an orchestrator most wants to see. The man
page is not wrong (an agent that crashed did run) and was left alone. Queued as
an open question, not a build, because what a third figure would key on is
genuinely unknown and log length alone is too crude to be honest.

**4. Verification caught one of my own errors before it became a record.**
The cctranscript worker's diff appeared to touch `docs/ROADMAP.md` — a rule it had
been explicitly given. It hadn't: the branch predated my later ROADMAP commit, so
`main..HEAD` rendered my own addition as its deletion. Diffing against the
**merge-base** showed the true four-file diff. Second catch, same session: I
spot-checked the worker's `finished > started` explanation, saw ten `spawnDepth:
1` entries and concluded the nesting claim was wrong — but `head` had truncated
the distribution, which is `{1: 10, 2: 5}`. The worker was right both times.
*Both near-misses came from reading a partial view as a complete one.*

**5. Sonnet's third-seat trial: a partial run, and it is recorded as partial.**
The Sonnet worker was given ccrepo asks 2/4/5 and **completed ask 2 only** before
the session closed (`791bea6`). That one item **passed** orchestrator verification
with no rework — the session-grain semantics are right, and a malformed *and* an
inverted range both exit 2 rather than matching everything, which is the failure
mode the ask didn't even name. Asks 4 and 5 were never started, so this is
**one clean item out of three, not a clean run**; recorded that way deliberately.
Call it **Run 5 (partial)** — it adds a data point for the well-specified-filter
class and says nothing about the other two asks.

## Infrastructure: three agent deaths, and the tier that was held

The first wave died twice over — one API connection closed mid-response, one
watchdog stall at 600s, then a second stall on retry. All three died before
touching anything (worktrees verified clean), so nothing needed salvaging.

**The tier was not dropped to route around it.** Down-tiering to dodge an
infrastructure fault is still down-tiering for a non-risk reason, so the ccrepo
pricing work — a correctness change with a silent-failure mode — was taken
**inline by the Opus orchestrator** instead. Same tier, no capability lost.

## Records and rulings

- ROADMAP harvested twice; `sizescan --check` exit 0 at close.
- The dated **`sonnet-5` ⏳ watch is retired on its own stated terms** — both
  conditions met (interval work landed well before 2026-09-01), so no action is
  owed on that date and the diary note became data.
- **One 🎯 open for Mike**: ccarchive encryption — *where does the crypto come
  from?* Four options with costs stated plainly; **C′ counselled** (write with
  the `age` binary, decrypt in-process) because it is the only one where we
  author solely the half whose bugs fail loudly. Counsel, not a decision.
- Mike queued **cctranscript transcript search** mid-session; captured grounded
  in the code, including the consequence nobody had noticed: it would be
  cctranscript's first bulk-read operation, which invalidates the documented
  reason it carries no `--materialise`.

## Open at close

- ccrepo v3 **asks 4 and 5** — `[~]` with resume breadcrumbs. Ask 4 (`--top` +
  the within-level multi-key separator, option A already decided by Mike) and
  ask 5 (sectioned `--help`) are both **untouched**. Ask 5 carries a live trap:
  the `--help` ≤40-line guard will need a **grounded** decision, never a figure
  fitted to whatever the sectioned output happens to measure.
- Branch `ccrepo-v3` and its worktree **left in place** for that continuation.
- **Nothing is uncommitted anywhere.**
