# 2026-09-19 · Queue run — building this morning's rulings

**Session:** Opus 5 (VS Code) orchestrating, Sonnet 5 workers in isolation
worktrees · `main` for claims, records and inline doctrine · in progress; each
item closes in its own commit, so this record grows per item.

## The ask

Mike's standing queue-run brief: *"I have a long list of work queued and I want
you to deliver it — across this session and any that follow. Start here, then
use your own judgement on what's next."* Run per `CONCURRENCY.md` §
*Orchestrated queue runs*. Tier check at open: Opus 5 orchestrating, stated
and not put to Mike (`ECONOMICS.md` § *Match the model to the job*, the
2026-09-16 standing default); the `⏳` review pointers name Fable, so this run
takes none of them.

## Opening state

`main` at `f1b34e7`, clean, no stashes, one worktree. The last two commits
(the 2026-09-19 rulings on `020/370`, `020/380`, `320/300`, `115/030`,
`320/010`) came after the previous run's closing entry, but they appended to
that run's own record, so they read as its tail rather than a live peer. One
open PR, #81, a child hand-up.

## Items

### PR #81 — the tier-question hand-up (merged as `320/320`)

The child filed at `320/310`; the ruling sitting took `320/310` an hour later
on `main` for *"should `pathscan` block"*. Two new files never text-conflict,
so only the number collided. Merged `--no-ff`, renumbered to `320/320`, index
regenerated. Its substance bears on this run's own open: the role check
against the 2026-09-16 "don't ask which tier" default. This run followed the
newer default (stated the tier, did not ask); the contradiction itself stays
a decision for Mike on `320/320`.

### Wave 1 — the three items ruled this morning

Claimed together (`9847c3d`): `020/370` (bounded-memory `secretscan`),
`320/010` part 1 (declared `pathscan` resolution roots), `115/030` (the floor
copied verbatim). Three Sonnet 5 workers, disjoint files; the `115/030`
doctrine half written inline by the orchestrator, because no scanner catches
a wrong rule.

### 320/320 — the tier contradiction, ruled mid-run and swept (inline)

The session was cut overnight with the three wave-1 workers still running;
their worktrees survived, two with commits, one dirty, and all three were
resumed from their transcripts rather than re-dispatched. Mike then ruled the
hand-up merged above, mid-run: *"the cheapest model that can do a good job is
the one that should be used for every job including orchestration. Fix
everything that is causing this mess"*, and on the one question it raised —
whether that reopened the principal-named review tier — *"fable reviews remain
fable reviews"*.

The mess was a **four-link chain**, and cutting any one link would have left
the question reachable by the other three: the run brief told a session to
confirm it was on the capable tier, `CONCURRENCY.md`'s role check told it to
stop if it wasn't, `ECONOMICS.md` defined the capable tier as *the most
capable model available*, and the estate's records rank the models. All four
are cut (`c38b7da`), plus `AUTONOMY.md`'s first-of-kind bullet and the two
places review read as *most capable available* rather than *the named tier*.
The run-open check now **states the tier and proceeds**. Two stops survive,
neither about rank: work that outruns the model doing it, and a `⏳` pass whose
named tier the session cannot honour.

Worth recording because it is the pattern's own failure mode: **the prompt
Mike pastes carried the defect too** — `session-open-prompt.md` said *"confirm
you're on the capable tier … stop and say so"*, so every run he opened
re-injected the stop the doctrine was being fixed to remove. A doctrine sweep
that had only touched `docs/method/` would have read clean and changed
nothing. Rule-4 cold pass queued at `160/330`; this author may not take it.

### 115/030 — the floor is copied verbatim (worker + inline doctrine)

The scanner's verdicts were inverted against the rule they enforced: a child
that *compressed* the floor went red, while one that declared `narrow=` and
deleted lines passed clean — and the attribute that bought the pass is spelled
with the parent's own word for *stricter*. Mike ruled the doctrine rather than
the scanner: **"Floor copy verbatim"**, so the exact-copy comparison becomes
simply correct for that region.

Doctrine inline (a fourth boundary in `PROPAGATION.md`; the *may compress*
sentence disambiguated — atelier's canonical text may compress its sources, a
child's copy of that text may not), scanner by a Sonnet worker. The worker's
own judgement call is the part worth keeping: it matched the floor on the
(`source`, `region`) **pair**, not the region name, because the test fixtures
and a real scaffold both reuse "floor" as a generic region name — name-only
matching would have swept in unrelated stamps. No existing test pinned the old
passing behaviour, which is itself evidence the passing case was never
deliberate.

**Two findings fell out of it, both filed rather than folded in:**
- Read-only across the siblings: 5 carry a floor stamp, 4 already byte-equal,
  **1 declares `narrow=`** and reds from now on. Its own session restores the
  canonical text — work is delivered where it lives. `115/200`, unnamed there
  because atelier is public.
- `python3 -m unittest discover -s tools` is **red on this machine and green
  in CI**: macOS ships Python 3.9.6, three floor modules use 3.10+ `X | None`
  annotations, CI pins 3.12. The worker proved it pre-existing before carrying
  on, which is the right move; but every session here is told to run that
  suite and shown `FAILED (errors=3)` when the tree is fine. `115/210`.

Rule-4 cold pass queued at `160/340`.

### 020/370 — secretscan in bounded memory (worker)

The incident that filed this item was a ~9 GB `secretscan` process that pushed
a 16 GB machine into swap. All three suspected causes measured real, and the
worker isolated each one rather than fixing them as a bundle: the whole-tree
file list built before a byte is scanned (~1 KiB held per file), each file held
three times at once (bytes + decoded string + `splitlines` list — a clean
32 MB/400k-line file peaked the *old* code at 134 MB, 7.5× the file), and every
finding kept to the end (~700 B each; 400k findings = ~283 MB on their own).

| Shape | Before | After |
| --- | --- | --- |
| 32 MB, one line, no newline | 114 MB | 42 MB |
| 32 MB, ~400k short lines | 432 MB | 52 MB |
| 60,000 tiny files | 83 MB | 23 MB |
| 16 MB, dense findings | 304 MB | 61 MB (cap engaged, overflow reported) |

The shape of the fix matters more than the numbers: `os.walk` with in-place
pruning streams the tree, a fixed 1 MiB read feeds a 4 MiB line window with a
64 KiB overlap so a token straddling a window cut is still whole in one of the
two, and findings past a fixed 50,000 cap are **counted, never dropped** — the
exit code and the advisory total read those counters, not `len(findings)`, so
a capped run still blocks correctly. The regression test's bound is derived
from the window design (4 × window + overlap), and the worker checked it
discriminates: pre-fix code measures 2.3× over it, fixed code 10–17× under.

Verified before the merge by running the old and new scanners over this repo's
`docs/` and `tools/` trees and diffing the JSON counts — identical. `020/380`
(every other guard) now has its harness: `tools/memprobe.py`.

### 320/010 part 1 — pathscan reads declared resolution roots (worker)

A repo laid out `src/<pkg>/` can now declare that root in
`.atelier-floor.json` (`roots.pathscan`, with a mandatory `why`); it is tried
**in addition** to the three base anchors, so declaring can only drop a
finding, never invent one, and a repo that declares nothing is unchanged.
Class A was 34 of a child's 46 findings — three quarters of the noise, none of
it real. `floor.py` was checked, not assumed: it reads named keys with
`raw.get`, so the new top-level key passes through unexamined and the scanner
stays self-contained.

The part worth keeping is the **discrepancy the item flagged**: the failure
message named three resolution anchors, the module docstring four. The worker
resolved it the honest way round — the message was right, because the docs
anchor has two mutually exclusive forms and no single resolution tries both —
and corrected the docstring rather than rounding the message up to match a
miscount. The item stays **open**: Classes B and C are unruled, and its own
closing evidence is a re-measurement showing a lower count *and* a non-zero
true-positive rate, which nothing has produced yet.

Code cold pass queued at `160/350` for both scanners.

### 320/190 — a private child's name was being published by the doctrine itself

The contradiction a child filed: § *The route* rule 2 forbids a finding from a
private child to name that repo; § *Report without harming the parent* told it
to file on a branch named `report-<reporting-repo>-<subject>`. atelier is
public, so obeying the second published what the first forbids — and nothing
said which rule won.

Re-measured before putting it to Mike, rather than quoting the filing's own
evidence: no **pushed branch** carries a child name any more (the 2026-09-17
sweep removed them), but **two closed pull requests still carry a private
child's name in their head ref and title**, and a third names a child that is
in fact public — checked at the forge, not assumed. Head refs and titles
survive branch deletion, so this is a leak that can be stopped and **not
retracted**.

Mike ruled **(b): rule 2 wins, everywhere** — it governs branch names, PR
titles, commit subjects and PR bodies, and outranks any rule about how to name
one. The branch form is now `report-<subject>-<HHMM>` **uniformly**, rather
than conditional on a visibility the parent cannot see from its own tree, and
a private child names itself nowhere in the parent.

**What I deliberately did not do:** doctrine's own prose names a child repo in
two worked examples, one of them on Mike's explicit earlier ruling (PU-2,
2026-08-22, reasoning that the veil was already defeated). Extending the new
precedence to narrative would partly overturn that, so it is a decision, not a
tidy-up: filed as `320/330`. Rule-4 pass queued at `160/360`.

### Two things the workers surfaced that were not their items

- A `020/380` worker found that **parallel workers share a scratchpad path**:
  a peer's script overwrote its own mid-measurement and later invocations ran
  the peer's copy with no error. Harmless here (measurement-only, and it
  caught it), silent by construction in general — the run pattern isolates
  workers by git worktree and that isolation stops at the repo boundary.
  Filed as `020/390`.
- The full suite has **one** environment failure beyond the interpreter issue:
  a `floorfleet` test shells out to `gh`, which is not on a worker shell's
  `PATH`. Same class as `115/210` and folded into it.

### 320/300 — blockscan, and the blind spot it has on its first day

Mike's *"Build the check"*: nothing checked whether atelier's **own** child
doctrine block still matches the method docs it summarises, which is how a
reworded ask rule sat in the block — and in every child at pin bump — for
weeks after it was overturned. `blockscan` is a staged **co-change** rule: a
map ties each block bullet to its source section(s), and touching a mapped
section without moving that bullet in both `PROPAGATION.md` and the scaffold
template is a finding, clearable only by a reasoned allow marker.

**The worker went against its dispatch spec, and was right to.** The spec said
register it in the shared floor registry "the way pathscan is". It refused: the
registry is read verbatim by every child's hook and CI, and every path this
map names exists only in atelier — so a registry line would exit 2 as a config
error on every child from the moment it merged. It wired two advisory steps in
atelier's own CI instead, following `stampscan`'s precedent, and said so. That
is the hand-up working in the direction it is hardest to get: a worker
declining an orchestrator's instruction on evidence.

**Then the check was probed rather than trusted**, and the probe paid: a test
edit inside a mapped section produced the violation correctly — but running it
against *this session's own* doctrine commits reported **clean**, because the
sections I rewrote are `###` subsections and the map's extraction is
non-recursive. The check works and has a blind spot on day one; `320/340`
carries it, with the honest note that this is `370/020`'s class — a guard
reporting clean over exactly the change it exists to catch.

### 020/380 — nine guards measured, and the item's second clause earning its keep

Three waves of workers, each given `secretscan`'s landed fix as the template
rather than the requirement alone, so the guards converge on one shape instead
of inventing nine. Nine ticked: `leakscan`, `conflictscan`, `sizescan`,
`datescan`, `wrapscan`, `spellscan`, `linkscan`, `reviewscan`, `publishscan`.
Every one measured before and after; every regression test confirmed to
**fail** against the pre-fix file; every scanner's output diffed old-vs-new
over `docs/` and `tools/` and found identical.

⏱️ **The finding that outran the brief.** The requirement has two clauses —
bounded memory *and* time at most linear in the bytes read — and the second
caught two defects the first never would:

- `spellscan`'s path/URL regex backtracked catastrophically: **107 seconds on
  one 1 MB line**, timing out a 120-second harness. Tokenise first, test for
  `/` natively: under a millisecond on 200,000 characters.
- `linkscan` ran two quadratic passes — an uncached `os.listdir` per resolved
  link, and a whole-tree `rglob` per *broken* link in its suggestion fallback.
  A 20,000-file tree **did not finish in three minutes**; it takes 17 seconds
  now.

Neither appears in a peak-RSS table. Both were found because a memory probe
happened to hit a wall clock. Later batches were re-briefed to look for the
shape deliberately.

📐 Two judgement calls worth keeping: `publishscan` was left **unmodified** —
it judges paths and never reads content, so the honest outcome was a
measurement and a pinning test, not a rewrite — and window sizes were chosen
per guard (256 KiB for links and headings, 4 MiB for credentials) rather than
copied, because converging on the shape is the point and copying the numbers
is not.

### The pushed floor went red, and it was mine

`memprobe`'s own test asserted that a child allocating 50 MB measures higher
than one allocating nothing. Green on every local run, **red on the Linux
runner**: `bytearray(N)` is zero-filled, and on Linux a large zeroed
allocation is served by copy-on-write zero pages that never become resident
until written — so the child's `ru_maxrss` never moved, the baseline happened
to peak higher on interpreter startup, and the assertion inverted. The fix
touches one byte per 4 KiB page. Its sibling rss-limit case had been passing
on the same runner **by luck from the same wrong assumption**, and now touches
too: a harness every guard's memory test is about to build on does not get to
be right by accident. This is the local-green/CI-red class the estate already
knows — the all-clear is the pushed floor run, never the local one.

**The second red was the interesting one.** Touching the pages fixed the
first failure and the floor stayed red, now with three failures — including
the case written to catch a *contaminated* reading. Cause: a forked child
inherits its parent's page accounting until it `exec`s, and on Linux
`subprocess` forks (`close_fds=True` rules out `posix_spawn`), so the harness
was reading **the test process's own footprint** back as the child's —
`python3 -c pass` measured **187 MB** on the runner. macOS spawns instead,
which is why every local run was clean.

The damage is worse than a constant offset: a test that writes a large
synthetic input grows its own interpreter between the small and the large
measurement, so the inherited baseline **grows with the input size** — which
is indistinguishable from the scaling every `020/380` test exists to detect.
`test_datescan` failed exactly that way on CI while passing here. So the
harness now measures one level down, in a fresh minimal interpreter whose
footprint is small and constant whatever the caller holds, with two new cases
pinning it (200 MB of ballast in the caller must not move the reading; the
isolated and direct paths must agree on a real allocation).

🔑 Worth stating plainly, because it is the lesson rather than the bug: **nine
guards had just been declared bounded on the strength of numbers this harness
produced.** Their macOS measurements were sound — macOS never had the
contamination — but the estate came within one CI run of carrying a set of
"measured" claims whose instrument was wrong on the platform its own CI uses.
The rule that saved it is the one already written down: the all-clear is the
**pushed** floor run, never the local one.

**Three pushes to get the floor green, and the third was the same fact
again.** After isolation landed, two cases still failed — both *direct-path*
readings taken from the test process itself, which by then holds a thousand
tests' worth of footprint (`python3 -c pass` read back **254 MB** on the
runner). The bleed case has to stay on the direct path, since that is where
the bookkeeping it guards lives, so it now runs its whole scenario inside a
fresh interpreter; the direct-versus-isolated agreement case was deleted,
because it compared a sound number against a contaminated one and called the
gap a disagreement. **Floor green on the pushed run at `8426f3e`** —
confirmed on that SHA, not inferred from a local pass.

### 020/380 — batch four: two fixed, two measured, one refused

`licenscan` (whole repo's text resident at once) and `pathscan` (the
`rglob`-into-a-list defect) fixed. `board` and `pointerscan` **not** rewritten:
both are the item's own named index-growth carve-out, both measured linear in
item count (~0.4 KB and ~3.7 KB per item, steady from 500 to 10,000), and both
pinned by a test that fails if that ever goes superlinear. Measured and pinned
is a complete outcome — a rewrite there would have been motion.

The refusal is the valuable part: `harvestscan`'s vanished-item check compares
every candidate against every survivor, **quadratic in item count** — 500
items in 21 seconds, 5,000 items unfinished at 120. The worker said so plainly
instead of patching around it, and it is now `020/400`. That is the **fourth**
defect the requirement's time clause has caught and the first that no amount
of memory work would have touched.

### 020/380 — closed: the last batch, and the two costs it leaves

`stampscan` had the full pre-`020/370` shape and is now streamed, with
canonical regions cached as *regions* rather than whole source docs (+29 MB →
+0.1 MB on a many-line file). The interesting call was the other four:
`blockscan`, `pins`, `floorfleet` and `signfleet` are **not tree-walkers** —
a fixed map, or one-level `iterdir` plus a few named files per child — so a
streaming rewrite would have been ceremony. They take a **size gate** instead:
check the size, refuse loudly past a cap grounded in the file class, never
truncate in silence. The headroom was measured across the real siblings rather
than assumed — largest `CLAUDE.md` in the estate 72 KB against a 2 MiB cap,
largest `floor.yml` 10 KB — so a real file is never refused and a pathological
one always is. `signscan` needed nothing: 1,324 commits of this repo's history
move it under a megabyte.

Local suite at close: **1,519 tests, OK, 378 s.**

**Two costs recorded rather than absorbed**, because both will be someone's
problem later:
- the suite takes ~6.3 minutes locally now, up from ~3.5, since every guard
  spawns real subprocesses over multi-megabyte synthetic inputs;
- `_walk_files` exists in **ten copies**, which is `115/080`'s third and
  largest instance — and the next correction to the walk (`020/160`'s
  gitignored-worktree skip) is ten edits, which is precisely Mike's own
  upstream test.
