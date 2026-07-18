# 2026-07-18 · 1602 UTC · the signing warn→block gate, re-probed — and the greens were never evidence

Mike opened with "list the work", then challenged one roadmap line: *"Code-signing:
flip CI warn→block — held … Not agent-actionable yet. I think we are ready to make
the flip now, agreed?"*

The answer was no, and the reason turned out to be different from the one the
roadmap held.

## Why the standing assessment could not carry its claim

The 2026-07-12 assessment concluded the flip **"wouldn't newly-red them"**, on the
evidence that none of the three scanner-red children failed on *signing*.

That evidence never supported the claim, for two compounding reasons:

- signscan runs `--warn` **fleet-wide**, so no child's floor has ever *failed* on
  signing. A green floor was never a signing pass — it was a signing step that
  cannot fail.
- On the scanner-red children the signature steps **never execute at all**:
  secretscan/leakscan fail first and every later step skips. Those repos had never
  run the check even once.

So the fleet's greens and reds were both silent on the question. Nobody had run
signscan in the mode the flip would actually use.

## The probe

A local probe ran signscan in **blocking** mode (no `--warn`) against all 12
children, each resolved at **its own atelier pin** and **its own adoption
boundary** — replicating what each child's `floor.yml` does, rather than testing
against a floating `main`.

Result: **10 pass, 2 fail** — and both failures were children **currently green**,
neither among the scanner-red three. The flip would have newly-redded two repos
that looked clean.

Seven commits, all dated 2026-07-12 (signing-activation day), carried **no
signature header at all** — verified against the raw commit objects, with a signed
commit as control.

### Method note — the first probe was wrong, and said so

The first pass was a shell script that reported *every* child as "pin predates
signing, CI would skip signing". That was a probe bug, not a fleet finding: macOS
`sed` does not support `\s`, and the trust-list redirect swallowed its result.
Checked directly, `allowed_signers` resolves at every child pin. Rewritten in
Python, the probe returned the real picture. The 7 green children passing acted as
the control that the rewrite was faithful.

A second self-caught error: a mid-probe commit count moved 455→472 and was briefly
attributed to a concurrent session. ros's HEAD was unchanged both times; the 455
was a miscount of the author's own making. Recorded rather than quietly dropped.

## Two causes — and neither was the "second machine"

The five ros commits carried a **short committer display name**, not this machine's
usual full git identity. The obvious reading — a second machine that was not
signing — was **wrong**, and Mike said so: he uses one laptop.

The ordering was the tell. A single config change would produce *unsigned then
signed*; ros showed **8 signed → 5 unsigned → signed again**. The evidence that
settled it:

| Clue | Shows |
|---|---|
| All 5 share one identical committer timestamp, to the second | A machine replay in one operation, not typing |
| Author times spread 17:19–17:47, committer times identical | Replay preserving authorship, rewriting the commit moment |
| Reflog: checkout off `security/mgmt-plane-pinning…` → `pull --ff-only` | A branch merged remotely, then pulled back |
| **Pre-merge originals survive as dangling objects, correctly signed** | The laptop *did* sign; something downstream stripped it |

The cause is a **rebase-merge** (`gh pr merge --rebase`, or the equivalent API
call — the principal does not use the web UI; merges here are agent-run through
the CLI). GitHub performs it server-side regardless of trigger: it re-commits,
minting new SHAs, discarding the local signatures, and setting the committer to the
merging account's *display name*. Not a machine at all; a profile name.

The shed case was unrelated and mundane: two ordinary local commits at 01:41/01:45
that genuinely predate signing adoption at 03:04 the same morning. Its boundary was
simply set one commit too early.

## The finding with a future

Squash and merge-commit **are** signed by GitHub's web-flow key — signscan already
defers those to the gh plane (ros carries 11 such since its boundary, all handled,
all `Merge pull request #N` two-parent merge commits dated 2026-07-18/19).
**Rebase-merge is not.** It silently mints unsigned commits *inside* the verified
range, and will re-offend on the next PR merged that way.

Moving a boundary fixes the past. It does nothing about this.

**This is agent-facing, not principal-facing.** Merges in this estate are run by
agent sessions through `gh`, not by hand in a browser — so the recurrence risk is
a default in agent behaviour, not a human habit to break. That cuts against
complacency: an agent chose `--rebase` once already, agents merge PRs routinely
under the standing grant, and nothing has since changed to prevent it. The 11
clean merges are convention, not enforcement.

The durable control is the **repo setting** (`allow_rebase_merge: false`), which
is enforced server-side on the same endpoint the CLI and the web UI both call —
so it binds every trigger, including `gh pr merge --rebase`, rather than relying
on an instruction each session has to remember.

**Applied on the principal's call: disabled on all 13 repos**, then independently
re-read to confirm rather than trusting the write responses (13/13 `false`).
Merge-commit and squash remain enabled on every repo, so no PR becomes unmergeable.

What it costs is worth stating plainly, because the principal asked twice and the
first answers were too abstract. Rebase-merge is the only method that yields flat
history *while keeping the individual commits separate* — merge-commit keeps the
commits but adds branch structure, squash flattens but melts them into one. That
combination is what is given up. In practice it costs nearly nothing here: all 11
PRs merged in ros since its boundary already used merge commits, so the button was
buying nothing while sitting there as a hazard. And the workflow remains reachable
— `git rebase` locally produces the same linear history *and* signs each replayed
commit, because the signing key is on the machine doing the work. The one-line
form of the whole issue: **rebase locally and it is signed; rebase on GitHub and
it is not**, because GitHub has no access to the key and cannot re-sign what it
rebuilds. Fully reversible per repo
(`gh api -X PATCH repos/<owner>/<repo> -F allow_rebase_merge=true`); nothing
accumulates while it is off.

## Applied

Both boundaries corrected, on the principal's explicit agreement per case:

| Repo | Boundary | Unsigned cleared | Already-signed commits dropped from verification |
|---|---|---|---|
| shed | `5bdee55`→`414baf5` | 2 | **0** — they sit at the range head |
| ros | `26a8bb6`→`f53d645` | 5 | **8** of 459 |

ros's 8-commit cost was put to Mike explicitly rather than absorbed. It is close to
theoretical and was argued as such: the 8 were confirmed good by the probe *before*
the move, remain signed, and stay protected by the hash chain — altering them would
change every SHA after and fail the 448 commits still checked. Rewriting history to
re-sign five commits would break every pin referencing them for no security gain.

Blocking-mode probe after the change: **12/12 PASS**.

## The probe became a tool

The throwaway probe was promoted to **`tools/signfleet.py`** at the end of the
session. The reasoning for keeping it: the blind spot is *structural*, not a
one-off. As long as `signscan` runs `--warn`, no floor can fail on signing, so
the fleet will stay mute on "would the flip pass?" every time anyone asks —
and the wrong answer already survived six days once.

It reuses `pins.discover`/`read_pin` and `signscan.scan` **by import** rather
than re-implementing either, so discovery rules and verification semantics
cannot drift from the tools it mirrors. Per-child resolution — trust list at
that child's pin, boundary from that child's `floor.yml` — is exactly why it
could not be a loop over `signscan --allowed-signers allowed_signers`.

Local-only by nature (it reads sibling repos), so like `pins` it cannot run in
CI and the suite is where it is proven: **17 tests, suite 247→264**. The
load-bearing one is `test_unsigned_child_fails` — a fleet probe that has only
ever printed "pass" is not proven, so the suite builds a throwaway atelier and
child whose commits are genuinely unsigned and asserts it goes red. The skip
paths are tested too, since a silent skip is how this tool would lie by
omission. Documented in `method/SIGNING.md` beside `signscan`.

The `\s`/BSD-sed bug that broke the first probe is preserved as a comment on
the boundary regex, so the next person to "tidy" it into shorthand sees why not.

## Left open

- **The rebase-merge decision** — disable it per-repo in GitHub settings (a settings
  change, not a discipline to remember), or accept recurrence. Principal's call.
- **Scanner debt** — unchanged, 5 children red on secretscan/leakscan. The
  principal's rotations, as before.
- **"Every active machine signs"** — still formally unverified, though the drift
  that prompted the doubt is now explained and is not a machine.

## Housekeeping caught in passing

The first roadmap correction ran 24 lines and pushed `docs/ROADMAP.md` **over its
300-line sizescan budget** — which would have redded atelier's own CI. Tightened to
fit; the detail lives here, which is what the current-truth/history split is for.
