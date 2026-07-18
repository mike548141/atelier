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

The cause is a **GitHub web-UI "Rebase and merge"**: GitHub re-commits server-side,
minting new SHAs, discarding the local signatures, and setting the committer to the
merging account's *display name*. Not a machine at all; a profile name.

The shed case was unrelated and mundane: two ordinary local commits at 01:41/01:45
that genuinely predate signing adoption at 03:04 the same morning. Its boundary was
simply set one commit too early.

## The finding with a future

Squash and merge-commit via the web **are** signed by GitHub's web-flow key —
signscan already defers those to the gh plane (ros carries 11 such, all handled).
**Rebase-merge is not.** It silently mints unsigned commits *inside* the verified
range, and will re-offend on the next PR merged that way.

Moving a boundary fixes the past. It does nothing about this.

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
