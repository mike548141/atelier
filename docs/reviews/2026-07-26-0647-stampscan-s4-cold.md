# Cold review — stampscan (S4), first-of-kind (rule-4 pass)

**Brief written by the reviewer (the taker), not the author** — REVIEW.md rule 4.

## Spawn provenance

- **Spawned by**: Mike, fresh session, *"Please do any review work, there are
  parallel sessions so take precautions"*. No author in the loop.
- **Author's involvement**: none. This session did not build `tools/stampscan.py`
  or its tests (queue run 0959, `2fe97f3`), did not add the marker convention to
  `PROPAGATION.md` / `templates/CLAUDE.md`, and did not start or instruct the
  session that did.
- **Rule 4's criterion** passes.
- **Claim**: `docs/ROADMAP.md`, 2026-07-26 0647 UTC, wt `atelier-review-0647-take`.

## 🚩 Same rule-1 exposure as the sibling item

This item's ROADMAP `⏳` pointer carries the author's full reviewer agenda inline
— the wiring blocker, the marker-convention ratification question, the
stamp-end placement compromise, and the unexercised residuals — against
ROADMAP's own *"refs only, no evaluative account"* ceiling and rule 1's
deferred-section requirement. A taker reads all of it while **selecting** the
item.

Mitigation, same as the sibling: the attack surface below was written from the
source and the live tree, committed before any run, and where it lands on the
same ground as the author's agenda the verdict says so instead of banking the
overlap as independent confirmation. Filed once as a queue-convention finding,
not twice as a scanner finding.

## Scope

The scanner, its tests, the marker convention it introduces into `PROPAGATION.md`
and `docs/build/templates/CLAUDE.md`, the one live stamp pair, the wiring
question, and live behaviour — re-run, not read.

**Non-goals**: the S4 mining decision that stamp-drift is a real invariant (three
grounded prior findings; not re-litigated); `test_templates.py`'s own design,
except where stampscan's markers collided with it.

## What the work is (established from the source and HEAD)

A scanner for **stamp-drift**: where a child file inlines a floor or pull-quote
of canonical doctrine, the inlined block must equal the parent's canonical text,
or be a *declared* narrowing of it. The child wraps its block in
`<!-- stamp:begin source=… region=… [narrow=…] -->` / `<!-- stamp:end -->`; the
parent brackets the canonical text with `<!-- <region>:begin/end -->`. The
scanner extracts both, trims blank boundaries, strips a presentational fence
around the canonical region, and compares: equal → clean; an ordered subsequence
with `narrow=` → clean-with-note; the same subsequence *without* `narrow=` →
red; anything else → red. Malformed markers and unresolvable source/region are
exit-2 config errors that `--warn` never downgrades.

## Attack surface (the reviewer's own, committed before any live run)

**T1 — `narrow=` is not a scanner feature; it is a new doctrine obligation, and
the scanner may not be the thing that creates it.** It imposes a duty on every
child that inlines a floor (declare your narrowing) and simultaneously mints the
escape that discharges it. Attack the substance, not just the ratification
process: does `PROPAGATION.md` already say how an inlined floor may differ from
its canonical text? If the existing doctrine says the block is copied whole, then
`narrow=` **contradicts** its parent rather than mechanising it — and a validator
that invents an escape its own doctrine does not grant is the sharpest possible
version of "encoding a policy as code does not keep the escape" (rule 3).

**T2 — Does the narrow escape have a floor?** `_is_ordered_subsequence` is a
greedy two-pointer test, and every list is a subsequence of any list when the
child side is empty. So a stamped block emptied to nothing, with `narrow=`
declared, may report as a legitimate narrow. Attack the degenerate end of the
range: a narrowing that keeps 0 of N lines is a total silent drop wearing the
declaration that was supposed to prevent exactly that.

**T3 — The wiring blocker, verified rather than accepted.** The marker parser
reads every line with no fence or code-span awareness, and `stamp:end` is matched
by `search`, not anchored. So a doc that merely *documents* the syntax — in a
fenced example or a backtick span — is parsed as a real marker, and a stray one
is a config error `--warn` does not suppress. Reproduce it, then attack the
proposed precondition itself: is "strip fenced/inline code, as every sibling
does" *sufficient*, or does the `search`-not-`match` choice for `stamp:end` leave
a hole even after stripping?

**T4 — The `search`-not-`match` asymmetry was bought to satisfy a frozen test.**
`stamp:end` is deliberately unanchored so the live pair can close on the same
line as a `---` divider, because `test_templates.py` slices that span verbatim.
That is a test constraining the *design of a marker convention*. Attack whether
the compromise is paid in the right place — the alternative named (teach
`template_block()` to strip markers) moves the cost to the test, where it
belongs.

**T5 — The canonical side has the same blindness as the child side.**
`extract_region` scans the whole source with no fence awareness, so a canonical
`<!-- floor:begin -->` shown inside a fenced illustration resolves as the real
region. Combined with first-match-wins for duplicate region names, attack what
happens when a doc documents its own region markers.

**T6 — Fence-stripping in `extract_region` is a first/last-line convention, and
the module says so.** Attack the degenerate cases the honest note does not cover:
a one-line region that looks like a fence, and a region whose real content
legitimately begins with a fence line.

**T7 — Re-run every live claim.** The pointer records 46 tests and *"live pair
CLEAN (byte-identical)"*. Re-run both, and check the pair is still clean at this
HEAD rather than at the commit that recorded it.

**T8 — What does an unwired scanner actually protect?** The three grounded
findings (`create-repo C3`, `method-layer P1`, `foundation Q2`) are the corpus
this was built for. Only one pair is stamped. Attack the coverage claim: how many
inlined floors exist in the tree today, how many carry markers, and does an
unstamped inlined floor read as clean — which would make a green stampscan run a
statement about almost nothing.

**T9 — Security/privacy lens.** `source=` is a repo-relative path read from
document text and joined to `--root`. Attack traversal (`source=../../secrets`),
symlink following, and whether a stamped block can cause the scanner to read and
echo file content from outside the scan root into its output.

**T10 — The exit-code contract under composition.** Config errors always exit 2,
even with `--warn`. In `floor.py`'s registry, an advisory scanner's non-zero exit
is *not* a failure — so attack what state an advisory-wired stampscan would
actually be in, and whether the exit-2-always rule survives the wiring the item
is asking about.

---

# Verdict — PASS-WITH-FINDINGS (3 MAJOR · 1 minor · 3 LOW · 1 nit) · **NOT gate-ready, and not wireable as built**

**Spawn provenance repeated**: a Mike-spawned session that authored neither
`stampscan.py`, its tests, nor the marker convention, and neither started nor
instructed the session that did.

**The invariant is real and the engine is competently built** — the parser's
malformed-marker handling is genuinely fail-safe, the exemption ladder matches
its siblings, the residuals are honestly stated, and 46 tests cover the
comparison logic properly. The problem is one level up: **the rule the scanner
enforces is not the rule its own canonical parent states**, and its escape hatch
has no floor. Both were found by reading `PROPAGATION.md` against the
comparison logic, and both reproduce.

## Live proofs re-run

| Claim | Result at this HEAD |
|---|---|
| 46 tests | ✅ `Ran 46 tests … OK` |
| Live pair CLEAN, byte-identical | ✅ `docs/build/templates/CLAUDE.md:18 [identical] matches canonical region 'floor' (52 lines)` |
| `--selftest` proves the engine | ✅ OK |
| Config errors are never downgraded by `--warn` | ✅ true standalone — `docs/` exits **2** with and without `--warn`. ❌ **defeated by advisory registry wiring** — see ST9 |
| BUILT BUT NOT WIRED | ✅ true — absent from `ci.yml`, `floor.py`, the hook |

## Findings

### ST1 — MAJOR (lens 1 — the load-bearing assumption is false) · The scanner's verdicts are inverted relative to `PROPAGATION.md`, the source of its one live region

`PROPAGATION.md:155` — immediately below the `floor:end` marker stampscan reads
from — states the rule for that exact block:

> *"The inlined floor is a **narrowing-free restatement** of the apex + AUTONOMY
> floor … each may **compress** but must not contradict its source."*

So the canonical doctrine **permits compression** and **forbids narrowing**.
stampscan does precisely the opposite. Reproduced on a fixture:

```
child compresses a line ("never mint new access" → "never mint access")
   → ✗ DRIFT, RED
child declares narrow= and drops lines
   → ✓ clean, reported as "legitimate narrow"
```

A compressed restatement is not byte-equal and is not an ordered subsequence, so
it fails both gates; a dropped line is a pure deletion, so it passes the
subsequence gate. The mechanics are sound — the **mapping from mechanics to
verdicts is backwards** against the doctrine being enforced.

**The terminology makes it worse, because the word is already taken.**
`PROPAGATION.md`'s layer-override rule defines *narrow* precisely:

> *"A child may **narrow** (make a rule stricter …)"* … *"A child rule that is
> **looser** or opposite to a house rule is a **defect to surface**, not a quiet
> local win."*

Dropping a line from a safety floor makes the child **looser**. So stampscan's
`narrow=` attribute grants a green verdict, under the parent's own word for
*stricter*, to the act the parent explicitly designates a defect. A child author
declaring `narrow=` will reasonably believe they are doing the sanctioned thing.

This is rule 3's category exactly: a validator is doctrine by function, and this
one **invents an escape its parent doctrine does not grant** while re-using the
parent's vocabulary for the opposite meaning. It is not a naming nit; the
attribute's whole legitimising force comes from that word.

**Fix shape** — three options, and the choice is a doctrine decision, not a code
one:
1. **Honour the doctrine as written**: drop `narrow=` entirely for the floor
   region (narrowing-free means narrowing-free), and make the comparison
   tolerant of compression instead — which is hard mechanically and is the real
   reason the build went the other way.
2. **Change the doctrine deliberately**: if a declared narrowing genuinely should
   be legitimate, that is an amendment to `PROPAGATION.md`, ruled by Mike, and
   the attribute is renamed to something that does not collide (`omits=`,
   `subset=`) — because `narrow` already means stricter.
3. **Keep the mechanics, drop the legitimacy claim**: report a declared subset as
   a *noted* difference that still reds, so the declaration buys visibility
   rather than a pass.

Whichever, the current state — scanner and doctrine asserting opposite rules,
with the scanner's word borrowed from the doctrine — cannot ship.

### ST2 — MAJOR · The narrow escape has no floor: a fully deleted floor block reports clean

`_is_ordered_subsequence` is a greedy two-pointer test, and the empty list is a
subsequence of everything. So a stamped block emptied to nothing, carrying any
non-empty `narrow=` token, passes. Reproduced, in isolation:

```
<!-- stamp:begin source=docs/canon.md region=floor narrow=we-only-need-nothing -->
<!-- stamp:end -->

  → ✓ stampscan clean — 1 stamped block(s) verified.
      [narrow] legitimate narrow — 0 of 3 canonical lines kept, in order
  → EXIT 0
```

A child can delete its **entire inlined safety floor**, declare any reason, and
the scanner built to catch silent drops calls it clean and exits 0.

The three findings that motivated this scanner (`create-repo C3`,
`method-layer P1` — *an inlined floor silently dropped "new trust surfaces"* —
`foundation Q2` — *a pull-quote listed 4 of 6 floor items*) are all **partial**
drops. This escape covers the total one. That is the wrong asymmetry for a
first-of-kind guard whose whole subject is dropped content.

**Recurrence prevention** (this is a security-class finding — the region under
guard is a safety floor): the escape needs a floor of its own regardless of which
ST1 option is chosen — reject an empty payload outright, and treat a declared
subset below some proportion of the canonical region as a config error rather
than a note. "Declared" must not be able to mean "all of it".

### ST3 — MAJOR (the wiring blocker) · Confirmed live, and the recorded precondition is both inaccurate and insufficient

The blocker reproduces without any effort to reproduce it — **this review's own
brief triggered it**:

```
$ python3 tools/stampscan.py --root . docs
✗ stampscan: 1 config error(s) (fail-safe).
  docs/reviews/2026-07-26-0647-stampscan-s4-cold.md:46  [malformed]
      stray stamp:end with no matching stamp:begin
$ echo $?
2                    # and 2 again with --warn
```

Line 46 is ordinary prose describing the convention, with the marker inside a
single-backtick span. Writing *about* stampscan reds the floor. That is the
recorded blocker, standing.

Two corrections to the precondition as recorded in the ROADMAP —
*"strip fenced/inline code before marker-hunting, as every sibling scanner
does"*:

1. **The sibling claim is not accurate.** The siblings differ on exactly this
   point: `pathscan` deliberately does **not** strip single-backtick spans,
   because backtick-wrapping a path is this house's normal way of naming one in
   prose. "As every sibling does" papers over a real divergence, and the
   divergence matters here — stampscan needs backtick spans stripped, and its
   nearest sibling needs them kept.
2. **Stripping alone does not close it.** `_STAMP_BEGIN_RX` is anchored with
   `.match()` at line start; `_STAMP_END_RX` is an unanchored `.search()`. After
   stripping code, any prose line that quotes the end marker in plain text still
   fires — and the asymmetry means the *begin* marker is safe while the *end*
   marker is not, so the failure is always the confusing "stray end" shape.

**The robust fix is to anchor `stamp:end` the way `stamp:begin` is anchored**,
*and* strip fenced/inline code. Anchoring is blocked by ST4, which is why the two
must be decided together.

### ST4 — minor · A frozen test is constraining the design of a convention that stamps behaviour into every child

`stamp:end` is unanchored so the live pair can close on the same physical line as
a pre-existing `---` divider (`---<!-- stamp:end -->`), because
`test_templates.py`'s `template_block()` slices that span verbatim and a new line
inside it would break the test.

The tail wags the dog: a marker convention that will be stamped into every child
repo took a permanent robustness cost (ST3) to avoid touching one test's slice
logic. The alternative the build itself names — teach `template_block()` to strip
markers — pays the cost where it belongs and unblocks the anchoring fix.
REVIEW.md is explicit that tests are reviewable on the same footing as the code
they exercise; here the test is the binding constraint.

### ST5 — LOW (lens 4) · `source=` resolves outside the scan root

`source=` is read from document text and joined to `--root` with no containment
check. Reproduced: `source=../s4outside/canon.md` was resolved, opened and
parsed — the scanner reported on the *region* inside a file outside the repo.

Content echo into output is possible but narrow: the drift hint's positional
branch prints `canonical=<line>`, though the more common branch prints the child
line instead, so a contrived overlap is needed to surface external content.

Bounded, but it is the same class as the sibling scanner's finding (`pathscan`
PS4) and takes the same one-line fix: resolve, then require the result to sit
under the scan root, else raise a config error. Worth fixing in both at once so
the class closes rather than the instance.

### ST6 — LOW · The canonical side is as fence-blind as the child side

`extract_region` scans the source with no fence awareness, and takes the **first**
matching begin/end pair. A doc that documents its own region markers inside an
illustration would resolve the illustration as the canonical region. Same root
cause as ST3, on the other side of the comparison, and it needs the same fix
applied in both places — fixing only the child side would leave a subtler version
of the same bug.

### ST7 — nit · A single-line region that looks like a fence extracts as empty

`extract_region`'s fence strip tests `payload[0]` and `payload[-1]`; when the
region is one line long those are the same line, so a region consisting of a
lone fence-shaped line strips to `[]`. Degenerate, no live instance, named so it
is not rediscovered.

### ST8 — minor (coverage) · One stamped pair exists, so a green run is a statement about almost nothing

The whole tree carries exactly **one** stamp pair —
`docs/build/templates/CLAUDE.md:18` against `PROPAGATION.md#floor`. An inlined
floor with no markers reads as clean, because the scanner only compares what is
stamped.

So the motivating corpus is not covered: the three grounded findings are a
`create-repo` stamped block, an inlined floor in the method layer, and a
pull-quote listing 4 of 6 items — none of which carry markers today. A clean
stampscan run currently verifies one template and is silent on every other
restatement in the estate, including the shapes it was built for.

That is not a defect in the engine; it is the honest statement of what wiring
this would buy, and it belongs in the gate decision. The same shape as
`pathscan` PS1: the tool does not yet reach its own motivating cases.

### ST9 — LOW (composition, new since the build) · Advisory registry wiring silently defeats the exit-2 contract

The module's fail-safe contract is *"a CONFIG ERROR always exits 2, `--warn` or
not."* Verified standalone. But ADR 0008's registry decides failure as
`state == "enforced" and rc != 0` — an **advisory** scanner's return code is not
consulted at all. So the moment stampscan is wired advisory through `floor.py`,
its deliberately-undowngradable exit 2 is ignored exactly like an ordinary
finding.

The registry post-dates the build, so this is not a build defect — but it means
"wire it advisory" does not do what the module's contract promises, and the
wiring decision should either accept that or give the registry a way to surface
a scanner's config errors regardless of state.

## 🎯 Decisions are Mike's

The marker convention is doctrine by function — it imposes an obligation on every
child that inlines a floor and mints the escape that discharges it. REVIEW.md
rule 3 reserves these to the principal. Nothing has been applied.

| # | What it is | Why it matters | If accepted |
|---|---|---|---|
| ST1 | The scanner reds the change the doctrine allows, and greens the change it forbids | A child following the scanner is breaking the rule; `narrow=` borrows the doctrine's word for the opposite meaning | Pick one of three routes — honour the doctrine, amend it deliberately, or keep the mechanics without the legitimacy claim |
| ST2 | Declaring a narrowing lets a child delete the *whole* safety floor and pass green | The guard's entire subject is dropped content | Refuse an empty payload; bound how much a declaration may drop |
| ST3 | Writing *about* the markers reds the build, and `--warn` can't suppress it | It is why the tool is unwired; the recorded fix is inaccurate and insufficient | Strip fenced + inline code **and** anchor the end marker |
| ST4 | One test's frozen slice forced the fragile marker design | The cost is being paid by every child repo instead of by one test | Teach `template_block()` to strip markers, then anchor |
| ST5 | A stamp can point at a file outside the repo | Same class as the sibling scanner's; fix both together | Constrain resolution to the scan root |
| ST6 | The canonical side has the same blindness | Fixing only one side leaves a subtler bug | Apply the strip to both sides |
| ST7 | A one-line fence-shaped region extracts empty | Degenerate | Optional |
| ST8 | Only one block in the estate is stamped | A green run says almost nothing yet | Decide the adoption sweep alongside the gate |
| ST9 | Advisory wiring ignores the "always exit 2" contract | "Wire it advisory" would not behave as documented | Accept, or teach the registry to surface config errors |

**Recommendation**: **do not wire, in any state, until ST1 is ruled.** ST3 is the
blocker everyone can see, but ST1 is the one that matters — wiring a gate that
enforces the inverse of its own doctrine would propagate the contradiction to
every child that adopts it, which is precisely the blast radius rule 4 exists to
protect. Sequence: rule ST1 → fix ST2/ST3/ST4 → stamp the motivating corpus
(ST8) → re-baseline → then decide advisory wiring with ST9 understood.

**3 MAJOR**, so this cycle does not close on this pass; the application earns a
further cold pass and queues its own `⏳` per rule 4.

---

## Reconciliation — deferred material

Opened after the findings above were durably written:
`sessions/2026-07-22-1036-invariant-candidates.md` § S4, and the build's own
reviewer agenda carried in the ROADMAP pointer.

**The build's agenda and this pass agree on three items and diverge on the one
that matters.** Agreed: the wiring blocker is real (ST3), the marker convention
needs ratification (ST1's process half), and the `---<!-- stamp:end -->`
placement is a compromise worth undoing (ST4). The divergence: the agenda frames
ratification as *"the marker convention borders on a doctrine act … needs
explicit ratification"* — a **process** ask. The substantive finding is that the
convention, as built, **contradicts the doctrine it points at** and re-uses that
doctrine's own word for the opposite meaning. Ratifying it as-is would enact the
contradiction rather than resolve it. ST2 is not in the agenda at all.

That divergence is the strongest evidence in this batch for rule 1's deferral:
the agenda was read at selection time (the exposure named in the brief), and the
findings that carry the pass were nevertheless produced by reading
`PROPAGATION.md` against the comparison logic — the one place the agenda did not
point.

**The intent record does not change a finding.** S4's mined rule — *"the inlined
block must EQUAL the parent's canonical text, or legitimately NARROW it"* — is
where `narrow=` comes from, and it is faithfully implemented. The finding is that
the mined phrasing was never reconciled against `PROPAGATION.md`'s
narrowing-free clause; the build inherited a wording collision from the mining
session and mechanised it. That is a lens-3 harvest gap, and it is the reason
ST1 lands on the convention rather than on the code.

**Note for anyone re-running this file**: this review is itself a live
reproduction of ST3 — the marker text quoted in its prose will red a stampscan
run over `docs/` until the strip/anchor fix lands.
