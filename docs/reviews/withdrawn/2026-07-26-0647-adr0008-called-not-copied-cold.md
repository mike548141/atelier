> # ⛔ WITHDRAWN — NOT ACCEPTED, NOT A COMPLETED REVIEW
>
> **Rejected in full by Mike on 2026-07-26, on tier grounds: cold review
> passes are Fable's, and this pass was run by Opus.** Nothing below is an
> accepted finding, an applied change, or a ruling. The item it covers —
> the ADR 0008 review — is still `⏳` in the ROADMAP
> and still awaits its first accepted review.
>
> It is kept because it happened, and this repo does not rewrite history:
> *withdrawn*, not deleted — the same state the ADR lifecycle uses for a
> record that was real and is not binding. It lives in
> `docs/reviews/withdrawn/` rather than alongside the accepted verdicts so
> that no queue pointer, no index, and no reader scanning `docs/reviews/`
> meets it by accident. See [`README.md`](README.md) in this directory.
>
> **If you are the accepted reviewer for this item: stop here.** Do not read
> past this banner until your own verdict is written and committed. Reading
> it afterwards, and comparing, is your call — reading it before is exactly
> the contamination `REVIEW.md` rule 2 exists to prevent.
>
> Provenance: merged `4252bc6`, withdrawn `625ee0e`, restored to the tree
> 2026-07-26 1007 UTC.

---

# Cold review — ADR 0008 "enforcement is called, not copied" + the estate rollout (rule-4 pass)

**Brief written by the reviewer (the taker), not the author.** REVIEW.md rule 4:
self-authored doctrine earns a cold *spawn*, not merely a cold context, and the
brief is written by the non-author who takes the `⏳` item.

## Spawn provenance

- **Spawned by**: Mike, in a fresh session, with the instruction *"Please do any
  review work, there are parallel sessions so take precautions"* — the queue was
  not pre-filtered for me and no author was in the loop.
- **Author's involvement**: none. This session did not write ADR 0008
  (`docs/decisions/0008-enforcement-is-called-not-copied.md`), `tools/floor.py`,
  `tools/floorfleet.py`, `.github/workflows/floor.yml`, `.githooks/pre-commit`,
  the `.atelier-floor.json` convention, or any of the 13 child-repo wirings; it
  did not instruct or schedule the sessions that did.
- **Rule 4's criterion** — *the review comes from a session the author neither
  started nor instructed* — passes.
- **Claim**: `docs/ROADMAP.md`, claimed 2026-07-26 0647 UTC, wt
  `atelier-review-0647-take`.

## Scope

Widest the work admits (REVIEW.md, *What a review actually checks*): the
decision itself, the design it commits to, the implementation that enacts it,
the tests, the child-facing template, and the live behaviour — re-run, not read.

**Non-goals** (and this narrowing is itself reviewable):

- The individual scanners' own detection quality (`sizescan`, `datescan`,
  `wrapscan`, `spellscan`, `reviewscan`, `leakscan`, `secretscan`, `linkscan`,
  `licenscan`). Each has, or is owed, its own first-of-kind review. What *is* in
  scope is how the registry composes and invokes them.
- The 15 pre-existing findings the rollout surfaced in four repos. They are
  those repos' work; the rollout says so.
- Private child repos' contents. atelier is public; nothing about a private
  child's internals gets written down here.

## What the work is (as this reviewer establishes it from the ADR and HEAD)

A rewrite of *how* the guard layer reaches 13 child repos. Previously each child
vendored a ~247-line `floor.yml` naming the scanners of its scaffold date, so 12
of 13 ran none of the five checks added since. Now:

1. `tools/floor.py` is the single registry, with two invocation planes — a
   pre-commit hook over the staged diff, and CI over the whole tree.
2. `.github/workflows/floor.yml` in atelier is a **reusable workflow**; each
   child's `floor.yml` is a ~30-line caller that names no scanner and resolves
   the workflow from `atelier@main` — floating, deliberately, on a
   "for a security floor, newest is safest" argument.
3. `.atelier-floor.json` per repo declares non-enforcement (`advisory` /
   `disabled`), scope, and flags — with a stated carve-out that a repo may not
   change *whether* a check blocks, and no advisory form at all for the boundary
   and integrity scanners.
4. `tools/floorfleet.py` enumerates conformance across the fleet,
   `--remote` reading GitHub's default branches.
5. `.githooks/pre-commit` + `core.hooksPath` so the hook is tracked, not
   machine-local.

The ADR's own framing — *"code was one-source; policy was vendored"*, and the
`PROPAGATION.md` thin-anchor/fat-pointer rule applied to the wrong half — is the
author's account of what the work is, and is therefore itself attackable
(rule 1).

## Attack surface (the reviewer's own, committed before any deferred material)

Named first, as lens 1 requires, and before opening the intent record, the
rollout session record, or the ADR's steer to a reviewer.

**A1 — "For a security floor, newest is safest" is the load-bearing premise, and
this repo has already ruled the opposite way once.** A floating `@main` reusable
workflow is a supply-chain dependency pointing *from* every child *into*
atelier's default branch: whoever can push there executes code in 13 repos' CI.
The ADR rejects vendoring the scanner code because it *"multiplies the
supply-chain surface"* — but floating the caller concentrates that surface into
one branch with no review lag. Sharper: the ADR's own *Rejected* list says
`signscan` must resolve its trust list from *"the child's own pin (never floating
`main` — 2026-07-12 review G7)"*. So a prior review already held that floating
`main` is unsafe for a trust-bearing check, and this decision floats the entire
floor. Either the two cases are genuinely different and the ADR must say why, or
the earlier ruling is being quietly overridden. **Is the trade named honestly,
and is the counter-evidence in the ADR's own text acknowledged?**

**A2 — Is the "may not change whether a check blocks" boundary actually
enforced, or only asserted?** `advisory` changes exactly that, for the checks
where it is allowed. So the guarantee reduces to: the carve-out list is correct,
and the code refuses what the prose refuses. Attack: which scanners have no
advisory form, is that list complete, does the code refuse mode-changing flags
as claimed, and what happens on a malformed, hostile, or absent
`.atelier-floor.json`? A declaration file that fails *open* would be the ADR's
own named defect class reproduced in the fix.

**A3 — Enumeration is only as good as its cadence, and the ADR's own Context
convicts intention-without-mechanism.** The ADR's most quotable lesson is that a
session *saw* the gap, wrote it down as a discipline to honour manually, and
watched it decay for three days. `floorfleet --check` is the answer to drift —
but if nothing *runs* it on a schedule, it is precisely an intention logged where
an edit was available. **Is floorfleet wired to anything, or is conformance
re-checked only when a human remembers?**

**A4 — Fail-open paths in the registry itself.** The ADR's Evidence section
records one fail-open caught in-build (absolute vs repo-relative paths on the
staged plane, so every boundary check silently passed). One found is a reason to
look for siblings, not a reason for confidence. Attack the exit-code and error
paths: a scanner that crashes, a scanner named in the registry but absent from
the fetched tree, a scope glob matching nothing, an empty staged diff, a
non-zero exit distinguished from a finding.

**A5 — Two children were installed with `--no-verify`, and the ADR does not say
so.** The rollout bypassed the very gate it was installing, twice, because the
gate failed on pre-existing content. That is recorded in the ROADMAP but is
absent from the decision record's Consequences. A decision record that omits the
compromise its own rollout required is incomplete for anyone reading it later
as the authority.

**A6 — Every "proven live" claim re-run.** The ROADMAP asserts *"All 13 children
call the floor; `floorfleet --remote --check` exits 0 against GitHub's default
branches"* and *"Proven live in CI, not just locally"*. Re-run both. A recorded
proof can be stale at the commit that recorded it.

**A7 — Security lens on the workflow itself** (mandatory, not a specialist
add-on). A reusable workflow inherits the caller's context: what `permissions:`
does it declare, what trigger does the child caller use, does it check out or
execute caller-supplied content, does it need or receive secrets, and does a
public reusable workflow called by a private repo leak anything about that repo
into a public surface? The `pull_request` vs `pull_request_target` distinction
is the classic hole in this exact shape.

**A8 — The parent-is-not-special claim.** Point 5 says atelier runs the floor it
ships with its own scoping declared. Verify against `.atelier-floor.json` and
`ci.yml`: does atelier actually route through the same registry, or does it keep
a second path that would let the parent's floor and the children's drift?

**A9 — Reversibility, and what happens when atelier is unreachable.** A
GitHub outage, a rename, a visibility flip, or a rate limit takes the floor out
in all 13 repos simultaneously. Does the caller fail closed (build red, work
blocked) or open (build green, unguarded)? Either is defensible; the ADR should
say which, and PRINCIPLES §1 ("design the way out before the way in") applies to
the estate's newest hard dependency.

---

# Verdict — PASS-WITH-FINDINGS (3 MAJOR · 2 minor · 2 LOW · 1 nit)

**Spawn provenance repeated** (rule 4: a pass with no provenance trail is
unauditable): reviewed by a Mike-spawned session that authored none of ADR 0008,
`floor.py`, `floorfleet.py`, the reusable workflow, the hook, or the 13 child
wirings, and that neither started nor instructed the sessions that did.

**The decision is sound and I would ratify it.** *Enforcement is called, not
copied* is the correct application of `PROPAGATION.md` to the half that had never
received it, the alternatives are fairly weighed, and the implementation is
unusually well-reasoned — the config surface fails closed on nine distinct
malformed-input classes, the planted-secret tests exist because they already
caught one fail-open, and the parent's CI genuinely runs the floor it ships.

The findings are not about the decision. They are about three places where the
*enforcement of the enforcement* has a hole the board reports as green — which is
the precise defect class the ADR's own Evidence section names: *"a check that
runs, reports success, and covers nothing."*

## Live proofs re-run (REVIEW.md — a recorded proof is a claim like any other)

| Claim | Source | Result at 2026-07-26 |
|---|---|---|
| `floorfleet --remote --check` exits 0 | ROADMAP § Enforcement propagation | ✅ true — 13/13 wired on GitHub's default branches, exit 0 |
| All 13 children call the floor | ADR 0008 / ROADMAP | ✅ true — local board 13/13 wired |
| Registry carries its own contract tests | ADR Consequences | ✅ true — 30 tests in `test_floor.py`; full suite 661 tests OK |
| `floor.py --selftest` / `floorfleet --selftest` | `ci.yml`, `floor.yml` | ✅ both ok (9 scanners, 0 failures) |
| atelier runs the floor it ships (point 5) | ADR Decision | ⚠️ **half true** — CI yes; the commit-time hook no. See AD3 |
| Softening `flags` are "declared and visible … read out estate-wide by floorfleet" | `floor.py` docstring | ❌ **false at HEAD** — see AD2 |
| leakscan's hook cover "is FULL" | `floor.py` docstring | ❌ **unbacked** — see AD4 |

Third-party actions are SHA-pinned with a readable tag comment (verified, both
`checkout` uses and `setup-python`); the reusable workflow declares
`permissions: contents: read`; the child caller passes **no** `secrets:`, so the
reusable workflow receives none. Those three were the sharpest things A1/A7 could
have found, and all three are right.

## Findings

### AD1 — MAJOR (security · fail-open) · A `scope` override naming a path that does not exist silently skips the scanner — including the two that may never be softened

`floor.py:493-498` filters declared subtrees to those that exist and, when none
do, records `Result(..., "skipped", 0, ...)`. `Result.failed` is `state ==
"enforced" and rc != 0`, so a skip never blocks and never reddens the exit code.
`Config.validate()` checks scanner *names* but never checks that a declared
`scope` path resolves, and `_str_map` rejects only the empty list.

The comment justifies the skip for a repo that keeps no records tree. That
reasoning is sound for the prose scanners' `default_scope="docs"`. It is applied
without distinction to an **explicit `scope` override on a boundary scanner** —
and the ADR's own worked case for `scope` is a repo narrowing leakscan to its
shareable subtree. Rename or mistype that subtree and the personal-data boundary
switches off, green, permanently.

**Reproduced live**, same tree, same planted AWS-shaped key pair, one character
changed in the config:

```
no .atelier-floor.json          → EXIT 1 · ❌ secretscan enforced, ❌ leakscan enforced
scope: {secretscan: ["sharable"],   ← typo of the real "shareable/"
        leakscan:  ["sharable"]}    → EXIT 0 · ⏭ secretscan skipped, ⏭ leakscan skipped
```

The floor printed `(no sharable tree in this repo)` and exited 0 with a live
credential shape sitting in the scanned tree.

**Why it is MAJOR and not minor**: the design's load-bearing promise is that
boundary and integrity checks *have no advisory form* — a repo cannot soften
them. This route softens them all the way to off, via a key the ADR
actively recommends using, with no error and no board signal (compounded by
AD2, which means the override is not visible estate-wide either).

**Recurrence prevention** (a security finding owes the class, not the instance):
a declared `scope` that resolves to nothing should be a `ConfigError` — a config
that means less than it says, which `validate()`'s own docstring already says is
the thing it refuses. The registered-default case (`docs` absent in a code-only
repo) keeps the visible skip; an *explicitly declared* path that is not there is
a config bug, and the two cases are already distinguishable in `subtrees()` by
whether `cfg.scope` supplied the answer.

### AD2 — MAJOR · The conformance board never reads `scope` or `flags`, so the two keys that actually weaken a check are the two it cannot show

`floorfleet.evaluate()` (`floorfleet.py:206-219`) reads exactly `advisory` and
`disabled` from `.atelier-floor.json`. `ChildFloor` has no field for `scope` or
`flags`, so neither reaches `render()` nor `--json`.

`floor.py`'s own docstring for `flags` says the opposite, in terms:

> *"This genuinely weakens a check, which is why it lives in a committed file
> that `floorfleet` reads out estate-wide — declared and visible, never quietly
> applied."*

It is committed. It is not read out. A repo running
`flags: {"leakscan": ["--disable", "ipv4,ipv6,mac-address"]}` — the ADR's own
worked case — shows on the board as a plain `✅ wired` with nothing beneath it.
So does a repo that has scoped a boundary scanner to one subdirectory.

This is not hypothetical and the parent demonstrates it: atelier's own
`.atelier-floor.json` scopes `wrapscan` and `spellscan` to three of its docs
subtrees, and nothing about that narrowing is visible on any board.

The design principle at stake is the ADR's headline: **"nothing is silently
absent."** Two of the four declaration keys are currently silently present.

**Fix shape**: add `scope` and `flags` to `ChildFloor` and render them under the
repo's row the way `advisory`/`disabled` already are. Small, and it makes the
docstring's claim true rather than aspirational.

### AD3 — MAJOR · The parent is in the pre-ADR-0008 state at commit time, and `floorfleet` structurally cannot report it

ADR 0008 point 5: *"The parent is not special. atelier runs the floor it
ships."* On the CI plane this is true and verified — `ci.yml` calls
`python3 tools/floor.py --plane ci --root .`. On the commit-time plane it is
false on this machine, today:

```
$ git config --get core.hooksPath          →  (unset)
$ ls .git/hooks/pre-commit                 →  6613 bytes, dated 2026-07-12
$ grep '^run_scan' .git/hooks/pre-commit   →  secretscan, leakscan, linkscan
```

atelier's primary checkout is running the **vendored, pre-ADR-0008 hook** —
three checks named in the hook file itself — where the registry's hook plane
runs nine. Six registry checks (`reviewscan`, `sizescan`, `datescan`, `wrapscan`,
`spellscan`, `licenscan`) do not run at commit time in the repo that authored the
registry. Every commit this review made showed it: three scanner lines, no
`atelier floor — hook plane` summary.

The ADR anticipated the *class* — *"One `git config core.hooksPath` per clone is
still manual. `floorfleet` reports the gap."* Two things make this a finding
rather than a known residual:

1. **The rollout converted 13 children and not the parent.** `floorfleet
   --child` proves the tooling detects it (`hook:legacy`) — nobody pointed it at
   atelier.
2. **The nominated reporter cannot see the parent.** `floorfleet` discovers via
   `pins.discover(roots, atelier)`, which enumerates *children*. The default
   board — the one an assurance claim would be read off — has no atelier row at
   all. So the single instrument the ADR names as the answer to this gap is
   blind to it precisely for the repo that hosts the instrument.

That is *"the parent is not special"* failing in the enumerator as well as in the
clone, which makes it a design finding and not only an install chore.

**Fix shape**: convert the parent's clone (`git config core.hooksPath .githooks`
— the tracked hook is already in the tree and correct), and include atelier in
`floorfleet`'s own board as a first-class row rather than as a `--child`
argument. Both cheap; the second is what stops it recurring.

### AD4 — minor · The hook plane's "FULL cover" leakscan claim is unbacked, and a test pins the gap using CI's reasoning

`floor.py`'s module docstring distinguishes the planes on exactly this axis:
*"leakscan has its machine-local term list, so its cover is FULL"* (hook) versus
*"leakscan runs STRUCTURAL-ONLY here and always will"* (CI). The registry passes
`--require-terms` on **neither** plane.

`leakscan` built that flag for this exact failure — its help text cites the
finding: *"review B5: to automation, a degraded exit-0 pass is indistinguishable
from a full one."* On a machine with no term list the hook degrades to
structural-only and exits 0. The human-readable line does say `structural only`,
so it is declared in prose — but the gate's *decision* is identical either way,
and the hook is the only place in the whole estate where full personal-data cover
is supposed to exist (CI cannot hold the list, correctly and permanently).

`test_floor.py:78` then asserts `--require-terms` is absent from **both** forms,
with a docstring reasoning entirely about CI (*"a list CI cannot and must not
hold"*). That reasoning does not transfer to the hook, which runs on a real
machine that is expected to have it. As written the test would block a future
session from closing this.

**Not a regression** — the pre-ADR-0008 hook did not pass it either. It is a
pre-existing gap carried into the new single source, which is now the one place
it can be fixed.

**Note on the fix**: a blanket `--require-terms` on the hook form would be wrong
— an external adopter with no term list would have every commit blocked. It
needs to be declarable (a `.atelier-floor.json` key, or `flags`, which already
reaches the hook form), so an estate that *expects* full cover asserts it and an
adopter that does not is unaffected. That makes it a small design call rather
than a one-line change, which is why it is filed as minor rather than fixed in
passing.

### AD5 — minor · The decision record omits that its own rollout bypassed the gate twice

Two children were bootstrapped with `--no-verify` because the gate failed on
their pre-existing content and so blocked its own installation. The ROADMAP
records this in full, with grounds, and *"once is the honest resolution; twice
would not be"* is a fair call.

ADR 0008's Consequences do not mention it. The ADR is the durable authority a
future reader consults; the ROADMAP is a queue that empties. A decision record
that omits the compromise its own rollout required is incomplete in the one
direction the apex's honesty burden cares about — and the omission is more
notable because the same ROADMAP section identifies `--no-verify` as *"the real
hole"* in the enforcement story.

One sentence in Consequences closes it.

### AD6 — LOW · The blast-radius consequence is stated as availability, never as confidentiality

Consequences says *"a bad change to the registry now breaks the whole estate at
once."* True, and honestly named. The unstated half: whoever can push to
atelier's `main` also **executes workflow steps in 13 repos' CI**, including
private children, with `contents: read` on each caller's tree.

Checked before filing, and it is why this is LOW and not higher:

- the marginal widening over the prior design is ≈ 0 — the vendored workflow
  already fetched and executed `atelier@main` scanner *code*, so arbitrary
  atelier-main code already ran in every child's runner;
- the child caller passes no `secrets:`, so the reusable workflow inherits none
  (verified in `docs/build/templates/workflows/floor.yml`);
- `permissions: contents: read` is declared at workflow level.

So this is a **recording** gap, not a new hole: the ADR reasons about the
floating-`@main` trade purely as staleness-versus-breakage, and the read-access
concentration is the part a future reader would want stated. The G7 counter-
precedent (a trust root must never float) *is* correctly distinguished in both
the ADR's Rejected list and `floor.yml`'s header — attack A1 does not land.

### AD7 — LOW · `pinned` is `ok` for `--check` with no staleness bound

`ChildFloor.ok` is `state in ("wired", "pinned")`, so `floorfleet --check` exits
0 for a child pinned at any SHA, of any age. The docstring calls pinning *"a
declared choice"*, which is fair — but ADR 0008 exists because frozen
propagation decays silently, and this is the same decay re-entering through a
declared door with a green exit beside it.

Same shape as the ROADMAP's own residual item 5 (advisory needs an expiry),
applied to a different key — worth folding into whatever ages `advisory`, rather
than solved separately.

### AD8 — nit · A string-valued `advisory` renders one board line per character

`floorfleet.py:212`: `advisory = list(cfg.get("advisory", []) or [])`. A child
writing `"advisory": "wrapscan"` gets ten `⚠️ w advisory` / `⚠️ r advisory` rows.
`floor.py`'s loader would separately reject the config at scan time, so this is
cosmetic — but the board would look broken rather than saying so.

## What was checked and found sound

- **Lens 1 (approach)** — *enforcement is called, not copied* is right, and the
  four rejected alternatives are each rejected on the correct ground. A1's
  attack (floating `@main` against the G7 never-float-a-trust-root ruling) does
  not land: the two are properly distinguished as detector versus trust root, in
  both the ADR and the workflow header, and `signscan` is deliberately kept out
  of the registry for exactly that reason.
- **Fail-closed behaviour** — verified by reading and by the contract tests:
  a missing scanner blocks with a printed remedy; an unparseable config blocks;
  an unknown scanner name, a reasonless `disable`, an `advisory` on a scanner
  with no advisory form, a contradictory advisory+disabled pair, a bare-list
  `disabled`, and a non-object config are all refused. `FORBIDDEN_FLAGS` blocks
  the sharpest smuggling route (`--warn` via `flags`). AD1 is the one input class
  that escapes this otherwise-thorough net.
- **The staged-path sharp edge** — `_render` renders repo-relative paths in
  `--staged` mode, with a comment recording the fail-open it replaced and two
  tests pinning both shapes. The scanners were additionally hardened at source
  to refuse an absolute path in `--staged`. Fixed at the class, correctly.
- **Two planes, honestly declared** — CI reading the whole tree rather than the
  diff (a rename breaks a link outside the diff that caused it) is the right
  call and is reasoned in place.
- **Supply chain** — third-party actions SHA-pinned with human-readable tag
  comments; pinning them once in the reusable workflow rather than 13 times is a
  real second win of the move, and is claimed as such.
- **`--json` stdout purity** — the Actions grouping markers route to the same
  stream as the scanners' prose, so `--json` output stays parseable inside
  Actions. Pinned by `test_json_stdout_stays_pure_inside_actions`.

**Security lens discharge** (mandatory, REVIEW.md lens 4): the harness
`/security-review` scanner reads *pending changes*, and this is a landed-delta
review with no in-scope pending diff — the only dirty content in this tree is
this brief, and REVIEW.md's SL2 caution explicitly forbids running it over a
brief. Discharged with grounds; the lens itself ran manually and produced AD1
and AD6.

## Already known — reported here as confirmations, not discoveries

The rollout's own residual list (ROADMAP § *To be considered*) already records
these, and this pass confirms each is still open rather than claiming it:
nothing schedules `floorfleet` (item 1, with four costed options and a 🎯
awaiting Mike); a repo with Actions disabled reads as wired (item 4); `advisory`
carries neither a reason nor an expiry (item 5). AD7 is item 5's shape applied to
`pinned`.

## 🎯 Decisions are Mike's, not the author's — and not this reviewer's

ADR 0008 is doctrine by function: it governs how every repo in the estate
enforces policy, and it stamps behaviour into 13 other repos. REVIEW.md rule 3
therefore reserves every one of these findings to the principal. Nothing above
has been applied.

Plain-language summary of what is being decided, per rule 3's informed-principal
requirement:

| # | What it is | Why it matters | If accepted |
|---|---|---|---|
| AD1 | A typo in a repo's `scope` setting turns a scanner off instead of erroring | The two scanners that guard secrets and personal data can be switched off silently by one wrong character | Make a declared-but-missing path an error; keep the silent skip only for the built-in default |
| AD2 | The estate board doesn't show two of the four settings a repo can use to weaken its floor | The design's promise is "nothing is silently absent"; today two settings are | Add two columns' worth of output to `floorfleet` |
| AD3 | atelier's own clone still runs the old hook, and the board can't see the parent | The repo that wrote the rule isn't following it at commit time | One `git config` on this machine, plus give the parent a row on the board |
| AD4 | The commit hook doesn't insist on the full personal-data check it claims to run | On a machine missing the local term list, the strictest check quietly runs in a weaker form | Make "I expect full cover" declarable per repo, then assert it |
| AD5 | The ADR doesn't mention the two `--no-verify` bypasses its rollout needed | Future readers take the ADR as the record; the omission reads as if it never happened | One sentence in Consequences |
| AD6 | The ADR states the risk as "breakage", not "read access to every repo" | Same risk as before the change, but the record should say it plainly | A clause in Consequences |
| AD7 | A child pinned to an old version stays green forever | Re-introduces the staleness the ADR removed, through a declared door | Fold into whatever ages `advisory` |
| AD8 | A malformed setting renders as gibberish rather than an error | Cosmetic | Two lines |

**The cycle does not close on this pass** (REVIEW.md — it closes when a pass
returns no MAJOR). Three MAJOR findings mean the application earns a further cold
pass, and per rule 4 the applier queues a `⏳` pointer in the commit that lands
the application rather than spawning that review itself.

**Reviewer's overall position**: accept the decision, fix AD1 first — it is the
only finding where the gate is currently answerable-for-nothing on the two
checks that carry the repo's hardest constraint.

---

## Reconciliation — deferred material (opened only after every finding above was durably written)

Opened after commit: `docs/sessions/2026-07-25-1311-policy-propagation.md` (the
intent record), the ADR's own steer to a reviewer, and the ROADMAP's residual
list.

**On the ADR's steer** — *"whether moving every repo onto a floating `@main`
caller trades a slow, silent failure for a fast, loud, estate-wide one, and
whether that trade is right."* Answered above as A1 and it is **the right
trade**, for a reason the steer itself does not reach: the marginal supply-chain
widening is ≈ 0 because atelier-main code already executed in every child's
runner before the change. The steer aims at the loudest question rather than the
load-bearing one — which is rule 1's mechanism working exactly as described, and
the reason the attack surface was committed before this section was opened. The
three MAJOR findings all sit outside the steer's frame.

**A rule-4 ceiling breach worth recording.** ROADMAP's own header states the
`⏳` pointer is *"refs only, no evaluative account — the account lives in the
session record, so a taker meets the work cold."* The pointers for two other
queued items (pathscan, stampscan) carry the author's seeded reviewer questions
inline in the queue, so a taker reads the author's framing while *selecting* the
item — before a brief exists to defer it below a divider. This ADR 0008 pointer
is compliant; the sibling ones are not. Filed here because it is the same
independence mechanism these rules exist to protect, and it is reported in the
briefs for those items too.

**Nothing in the intent record changes a finding.** It records the fail-open the
author caught and fixed, the rollout's `--no-verify` bypasses, and the licence
gate ruling. AD3 is not mentioned anywhere in it — the parent's own hook was
never checked after the change.
