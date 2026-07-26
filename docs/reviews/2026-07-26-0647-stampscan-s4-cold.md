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
