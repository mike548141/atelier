# Session — boundary-findings triage: the scanner was reporting the safe pattern

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 215+1 -->
- [2026-07-28 · 0430 UTC · Boundary-findings triage — the gate was reporting the safe pattern (Opus, wt: secretscan-blind-spots + main)](2026-07-28-0430-boundary-findings-triage.md) — Mike's *"resolve the boundary findings … WALK ME THROUGH IT STEP BY STEP … FIRST, MEASURE"*, with *"there is a parallel session so take precautions"* mid-turn. **Re-measuring changed the shape, not just the numbers**: only **2 of 13** children have `secretscan` hits at all, so the 2026-07-25 framing implied an estate-wide credential problem that does not exist. **The organising finding inverts the roadmap entry it came from**: the `assigned-secret` class was recorded as credential-shaped assignments wanting "a secret-store reference" — but both flagged lines already *were* secret-store references, and the live plaintext credentials beneath them were unflagged. Four defects, each confirmed by running the scanner's own functions on the exact lines: `\b` cannot see past `_` (exempting every prefixed env var); the path test demanded a file extension (so following Docker's recommended pattern is what turned a repo red); an *opening* templating marker anywhere wrote a value off as a template; a stray bracket anywhere meant "function call" — the fourth found only while fixing the third, and the reason the same key stayed exempt. **All four are one error — a rule deciding on a *fragment* instead of a whole shape** — queued as a doctrine candidate pending a fifth instance, not asserted. Fix validated by re-scanning the estate, which **caught three false positives the fix itself introduced** (minified JS, a kebab-case enum, prose in a comment); fixed and pinned rather than shipped. 747 → 759 tests; PR #14, pushed floor green. 🚩 **Three near-misses named rather than hidden.** (1) **A real credential was nearly published by the fix for credential leaks** — the natural test value is the one that broke the rule, so two live values from a private repo went verbatim into atelier's test file; the floor passed them because a scanner's own fixtures are exempt, so **no gate would have caught it**. Caught on a last look, replaced with synthetic values plus a comment saying why. (2) A child's log carried an open 2026-07-12 scanner-gap follow-up; the obvious move was to record that this fix closed it — tested against **both** the pre- and post-fix scanner first, **both catch all four shapes**, so the gap was already closed and the credit was not this session's to take. It also corrected this session's own framing: the high-entropy net already catches ≥32 chars regardless of key name, so the `\b` defect only ever mattered in the **12–31 character band** — short service passwords, not tokens. (3) Mike ruled **allow-marker** for the tracked data export; tested rather than assumed, a line-level marker is **impossible in JSON** (outside the string it breaks the file, inside it falsifies a business record) — reported back rather than silently substituted, with a correction to this session's own earlier claim that the file-scoped ignore was "strictly worse". Mike then moved the export out of the tree; **verified rather than accepted** — the blob stayed in its commit and on the remote, all 2016 records one command away — and the point put to him was that **the scanner going green is the failure mode**. Ruled **untrack-only, informed**, and the records say so plainly (`homenetwork@a6c19e3`). Per-repo detail went to the estate root, whose identity Mike confirmed this session and which is deliberately **still not named here** — `PROPAGATION.md` binds any public tree including atelier's own, so writing it to close **Track B1**'s blocker would commit the breach the blocker exists to prevent; B1 is unblocked regardless. 🎯 **Owed:** finding 2b (15 live credential assignments, one at a time in the owning repo, rotate-then-remove for the live service configs) and findings 3–5 (structural `leakscan` reds, measured but **explicitly not triaged**). Rule-4 `⏳` queued in the landing commit, not spawned by this session.


- **Date**: 2026-07-28 04:30 UTC
- **Worktree**: `secretscan-blind-spots` (scanner fix); `main` (records)
- **Subject**: triage the boundary findings queued since 2026-07-25 — the real
  credential exposure in the child repos — one finding at a time, ruled as we
  went, per Mike's standing preference for plain-language walk-throughs.
- **Rulings taken**: finding 2a → **fix all four defects**; 2b → **work the
  credentials one by one in the owning repo** (deferred); finding 1 → **untrack
  only, history deliberately retained**.

## Measure first — the stale numbers were the wrong shape, not just stale

Mike's instruction was to re-measure rather than inherit the 2026-07-25 figures,
which came out of a measurement pass rather than a triage pass. The re-measure
changed the picture: **only two of thirteen children have `secretscan` hits at
all**. The earlier framing implied an estate-wide credential problem; the
eleven other repos are clean.

The documented invocation footgun was avoided and then verified rather than
trusted: the scanners' positional path argument resolves against the working
directory, not `--root`, so a cross-repo one-liner reports confident, identical,
wrong numbers for every repo. Each scan `cd`-ed into its repo *and* passed
`--root` with no positional, and the per-repo numbers were checked to differ
before any of them were believed.

## The organising finding: a gate reporting the safe pattern

The `assigned-secret` class was recorded on the roadmap as "credential-shaped
assignments" whose usual answer is "a secret-store or env reference". The
triage inverted it. **Both flagged lines already were secret-store references**
— commented-out `/run/secrets/…` mounts — and the live plaintext credentials
directly beneath them were not flagged at all. No ignore file, no allow-marker;
the omission was the scanner's own logic.

Four defects, each confirmed by running `secretscan`'s own functions on the
exact lines rather than by reading the code and inferring:

1. **The leading `\b` cannot see past `_`.** `_` is a word character, so there
   is no boundary between a prefix and the keyword — exempting every prefixed
   environment variable, the single most common shape a credential takes in
   compose and `.env` files.
2. **`_looks_like_path` required a file extension**, so an extensionless
   secret-store mount was reported high-severity. Following the recommended
   secure pattern was what turned a repo red.
3. **`_is_placeholder` substring-matched *opening* templating markers**, so a
   random 60-character key that happened to contain two particular characters
   was written off as shell interpolation.
4. **`_looks_like_code_ref` returned true on a stray bracket anywhere** — found
   only while implementing the fix for (3), and the reason the same key stayed
   exempt once (3) was fixed.

All four are one error: **a rule deciding on a *fragment* of a value instead of
its whole shape.** That generalisation is queued as a doctrine candidate rather
than asserted, pending a fifth instance.

## The fix validated itself by finding its own false positives

Re-scanning the estate before landing caught **three false positives the fix
introduced** — vendored minified JS, a kebab-case enum, and prose in a comment
— all shapes the old stray-bracket test had been quietly absorbing. Each was
fixed and pinned rather than shipped. Final state: the eleven clean repos stay
clean, and the two with real exposure went 2 → 9 and 25 → 26, with the two
false positives among the old hits gone. 747 → 759 tests, green.

The trade is named honestly in the `⏳` brief: every widened rule was validated
by re-scanning this estate, which risks tuning a gate to one corpus. A
**pre-existing** gap — a lowercase hex secret is still exempted as
identifier-shaped — was deliberately left open and flagged for the reviewer to
rule on rather than inherit, because closing it trips every lowercase word in
the corpus.

## Named, not hidden

**A real credential was nearly published by the fix for credential leaks.**
Drafting the tests, the natural value to use is the one that broke the rule —
so two live values from a private repo went verbatim into atelier's test file.
atelier is public. The floor passed them clean, because a scanner's own test
fixtures are exempt from it: **no gate would have caught this.** Found on a
last look before committing and replaced with synthetic same-shape values,
with a comment saying why so a later session does not "helpfully" restore the
realistic ones. The usual risk from this rule is a false positive *blocking* a
commit; here it was a real leak sailing through.

**A claim about another repo's records was nearly written wrong.** A child's
log carried an open follow-up from 2026-07-12 asserting `secretscan` was blind
to two credential shapes. The obvious move was to record that this session's
fix closed it. Tested against both the pre- and post-fix scanner first: **both
catch all four shapes**, so the gap was already closed by an earlier change and
the credit was not this session's to take. It also corrected this session's own
framing — the high-entropy net already catches anything ≥32 characters
regardless of key name, so defect (1) only ever mattered for credentials in the
**12–31 character band**: short service passwords, not tokens.
*(Correction 2026-08-03, per the SF ruling: the ≥32 aside is true only for
mixed-class values — probed false for single-class values, two 32-character
probes did not flag. The E6c carve-outs now close that family in assigned
context.)*

**A ruling was executed in a form the file could not hold.** Mike ruled
allow-marker for the tracked data export. Tested rather than assumed: in a
`.json` file a line-level marker is *impossible* — appended outside the string
it breaks the JSON, inside the string it is absorbed into a data value and
falsifies a business record. Reported back rather than silently substituted,
along with a correction: this session had called the file-scoped ignore
"strictly worse" on a general argument that does not bite for a frozen one-off
export nothing writes to.

**A removal that removes nothing.** Mike then moved the export out of the
working tree. Verified rather than accepted: the blob remained in its commit
and on the remote, all 2016 records recoverable with one command. The point
put to him was that committing that deletion turns the scanner green while the
exposure is unchanged — *the scanner going green is the failure mode*. He
ruled untrack-only on that basis, informed, and the records say so plainly
rather than implying resolution.

## Where the per-repo detail went

atelier records **classes** only. The per-repo triage list — which repo, which
file, which ruling — is in the estate root, whose identity Mike confirmed this
session. That answer is deliberately **not** written here: `PROPAGATION.md`
binds any public tree including atelier's own, so recording it to close Track
B1's blocker would commit the breach the blocker exists to prevent. B1 is
unblocked by the fact existing and being written down somewhere private, not by
it being written down here.

## Verification

- 759 tests green (12 new); floor 9/9 on the hook plane; **pushed** floor green
  on both CI runs of PR #14, which is the all-clear, not the local scan.
- The `[x]` for the closed finding rode its harvest to `ROADMAP-DONE.md` in the
  same commit — no window where a completed item sits on the hot path.

## Owed

- **Finding 2b — 15 live credential assignments**, to be worked one at a time
  in the repo that owns each; the ones in live service config are
  **rotate-then-remove**, never remove first.
- **Findings 3–5 — structural `leakscan` reds, measured but NOT triaged.**
  Recorded as untriaged so the numbers are not read as resolved. The largest is
  almost certainly a scoping problem rather than content, which is a hypothesis
  this session did not test.
- **The rule-4 review** of the `secretscan` change: queued in the landing
  commit, **not spawned by this session**.
