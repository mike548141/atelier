# 0006 — Teammate instruments live in atelier, in their own `instruments/` layer

**Status**: accepted • **Date**: 2026-07-11

## Context

Two small CLIs were built to support working with Claude: `ccrepo` (per-repo
token/cost totals — a DevFinOps view of what the collaboration costs) and
`cctranscript` (a timestamped transcript of a session — observability of when
Claude or the principal did something). They were first dropped into the private
`homenetwork` infra repo next to unrelated machine config, because that's where
an earlier one-off (`ccrepo`) had landed.

That placement was expedient, not reasoned. The real question surfaced: do these
belong in atelier? atelier's stated purpose is *the operating model for working
with Claude as a teammate*. Both instruments have **no value outside that
relationship** — they read Claude Code's own session logs to cost and observe the
work. By purpose they are atelier material, not home-infra material.

The counter-objection was that atelier is doctrine-only and adding runnable tools
expands its scope. But atelier already ships executable tools (`tools/` — the
Python control-scanners) and a skill (`create-repo`). It is already a repo that
ships instruments, not only prose. So the scope objection doesn't hold; what's
needed is to draw the boundary deliberately.

## Decision

Move both instruments into atelier, in a **new top-level `instruments/` layer**
distinct from `tools/`:

- **`tools/` enforces** — Python, zero-dep, hook/CI-wired checks that gate a
  commit (leakscan, secretscan, licenscan, linkscan, worktree, pins).
- **`instruments/` observes** — Node, user-invoked CLIs that cost and observe the
  collaboration itself (ccrepo = DevFinOps, cctranscript = observability).

The membership rule is **purpose, not runtime**: an instrument belongs here only
if its value *is* the Claude teammateship — costing it, observing it, steering it.
General machine/infra utilities (macOS, TrueNAS, networking) that the principal or
Claude merely *use* stay with the estate they serve (`homenetwork` et al.).

Install stays as it already worked: a per-tool symlink into `~/.local/bin` via an
idempotent `instruments/install`, not the folder on `PATH`.

## Rejected

- **Leave them in `homenetwork`:** keeps the pair together and private, but files
  them by accident of where the first one landed, not by what they are. Their
  whole reason to exist is the Claude relationship — the operating-model repo is
  their honest home. Private-vs-public isn't the deciding axis: the code carries
  no personal data (paths are derived at runtime), so publishing them is safe.
- **Put them inside `tools/`:** one dir, matches "atelier already has a tools
  folder". Rejected because `tools/`'s charter is explicit — *"Doctrine informs; a
  check enforces. These are the checks."* These aren't checks and aren't Python;
  folding them in blurs a sharp, load-bearing framing (the enforcement floor) with
  a different species (interactive observability). A clean second layer keeps both
  honest.
- **A dedicated public micro-repo (`cc-tools`):** over-fragments for two scripts
  and re-poses the same "where does this belong" question. atelier is the answer.

## Consequences

- atelier now has a first-class `instruments/` layer; the README structure table
  and this ADR record the tools/instruments split. Future teammate-support tools <!-- pathscan:allow: a prose slash naming the tools-vs-instruments split, not a path -->
  land here by the purpose rule; infra tools are explicitly out.
- atelier gains a **Node** runtime dependency for this layer (the `tools/` layer
  stays pure-`python3`). Stated, not silent.
- Publishing: the instruments enter the public repo. Verified clean of personal
  data before the move (no hardcoded paths/names; logs read at runtime). The
  leakscan/secretscan pre-commit gate covers every commit as usual.
- They leave `homenetwork` entirely — no duplicate, no stale copy. The
  `~/.local/bin` symlinks re-point to atelier; `homenetwork/bin/` is removed.
- The instruments are currently untested (unlike the `tools/` scanners). Test
  coverage for them is a future item if they grow beyond throwaway.

## Addendum (2026-07-12) — the layer admits *capability* tools, not only observers

**Decision (Mike):** `instruments/` widens to admit **capability tools** — ones
that extend what the teammate can *do* — where their value is wholly the
working-together relationship. The membership rule is unchanged (purpose, not
runtime); what widens is the *kind* of value that counts: not just **observing**
the collaboration (ccrepo, cctranscript) but **extending its reach**.

Prompted by adopting **`browser-fetch`** (Mike, 2026-07-12): an MCP server that
drives Chrome so the teammate can get through when `WebFetch`/curl are blocked
(and so the operator can help clear a captcha the agent can't). It passes the
purpose test squarely — it exists only for the teammateship — but it breaks
every prior *sub-norm* of the layer, and those norms are now understood as
descriptive of the first two instruments, not constitutive of the layer:

- **acts, not observes** — the layer is now three verbs: `tools/` enforce,
  observer instruments (ccrepo/cctranscript) observe, capability instruments
  (browser-fetch) extend reach.
- **Python + dependencies, not zero-dep Node** — a browser tool cannot be
  zero-dep. The zero-dep ethos holds where it can (`tools/`) but **flexes for
  capability tools whose value requires deps**; the price is paid honestly —
  deps pinned (`requirements.txt`) and constrained (`constraints.txt`), the
  runtime a regenerable venv outside the repo, the code versioned in-repo.
- **an MCP server, not a `~/.local/bin` CLI** — it installs via its own `setup`
  (build the venv, print the `~/.claude.json` registration), not the shared
  symlink `install`.

**Boundary still holds:** a *general* browser-automation utility Claude merely
uses would be estate/infra, not an instrument. browser-fetch qualifies because
it is built for, and only makes sense within, the Claude teammateship.

**Consequences:** the `instruments/` charter is "value is the teammateship",
observing **or** extending it. CI does not unit-test a browser (disproportionate);
the floor scanners still cover its source, and it is verified by live use — the
same honest-scope stance the scanners take. Pre-public scrub done (the
`Mike`/machine specifics and pre-SDK history removed before the code entered the
public repo).

## Addendum (2026-07-17) — a *preserving* verb, and the first instrument that writes

**Decision (Mike):** admit **`ccarchive`** — it durably mirrors every raw session
`.jsonl` into a compressed, append-only archive so the transcripts survive Claude
Code's `cleanupPeriodDays` deletion. Its value is wholly the teammateship (keeping
the record of the work), so it passes the purpose rule squarely and lands as the
ADR anticipated — "future teammate-support tools land here by the purpose rule".
It sits beside the observers as a zero-dep Node CLI, unit-tested like
`cctranscript`.

It stretches one prior *sub-norm*, recorded here for honesty (the norms are
descriptive of the first instruments, not constitutive): the observers "read the
logs **read-only**, write nothing". `ccarchive` **writes** — that's its job. Two
guards keep the boundary clean:

- **No personal data in the code.** The dest defaults to the operator's iCloud
  Drive but is derived at runtime from `$HOME` (`--dest`/`CCARCHIVE_DEST` to
  override); nothing personal is committed. The leakscan/secretscan gate covers it
  as usual.
- **The write target is a personal store, outside any repo.** The transcripts span
  every repo and carry personal data, so the archive itself must never be atelier
  (public) — it lands in the operator's own storage, and the *schedule* (a
  `launchd`/`cron` job) is machine-local too. Only the generic, data-free tool
  lives here.

So the layer is now four verbs: `tools/` **enforce**; observer instruments
**observe** (ccrepo, cctranscript); capability instruments **extend** reach
(browser-fetch); and `ccarchive` **preserves**. The boundary is unchanged —
value is the teammateship — the kinds of value it admits widen again.

## Addendum (2026-09-09) — the first instrument that holds a credential

**Decision (Mike):** admit **`ccmail`** — it fetches Gmail attachments to disk,
because the mailbox connector Claude Code speaks to lists an attachment's
filename and id but has **no call that returns its bytes**. The observable
failure is a session reporting, accurately and uselessly, that a message carries
a valuation PDF and that it cannot open it. `ccmail` adds no new verb: it is a
capability instrument under the 2026-07-12 addendum, and the purpose rule is
passed about as squarely as it can be — the *operator* has no use for it at all,
because the operator opens their own mail in a mail client. It exists solely so
the teammate can read what the operator is already looking at.

What is **new** is that it is the first instrument to **hold a credential to a
third-party account**. Every instrument before it either read local files
(ccrepo, cctranscript, ccarchive) or drove a local program that already held its
own sessions (browser-fetch drives the operator's Chrome). `ccmail` authenticates
as the operator to an external service, so the layer now has a secrets surface it
did not have. That is recorded here rather than left implicit, with the controls
that make it acceptable:

- **One scope, read-only** — `gmail.readonly`, on the operator's own mailbox. It
  cannot send, reply, label, delete, or reach another mailbox. The tempting
  alternative for a Workspace **administrator** — a service account with
  domain-wide delegation — was considered and **rejected**: it needs no browser
  consent and never expires, but it can be pointed at any mailbox in the domain
  and its key is a file. Convenience bought with blast radius, against
  `SECRETS.md`'s *least* leg. Mike ruled for the narrow personal grant.
- **The secret never touches a repo** — macOS Keychain by default, a 0600 file
  (`CCMAIL_CREDENTIALS`) as the documented fallback. Re-mintable in one command
  (`--auth`) and revocable from the operator's Google account page, which is the
  cheap-to-burn property `SECRETS.md` asks for.
- **The data it fetches never touches a repo either** — attachments are other
  people's data, so `ccmail` refuses a destination inside a git work tree, the
  same guard `ccarchive` carries on its archive dest and for the same reason.
- **Nothing personal in the shipped code** — the account, the client and every
  path are resolved at runtime, so the file publishes safely, as ADR 0005
  requires of everything here.

**Consequences:** the layer's charter is unchanged (value is the teammateship,
observing or extending it), but the *review surface* widens — a future instrument
holding a credential inherits these four controls as the precedent to meet or to
argue against explicitly. `ccmail` also carries the layer's first
**human-in-the-loop install step**: `./instruments/install` puts it on `PATH`, but
`ccmail --auth` needs a terminal and a browser once per machine, and no agent
session can perform it. That is a stated limit, not a defect — a credential an
agent could mint unattended would be the wrong design.

**Amended the same day, on the principal's re-ruling.** The choice above was put
to Mike as personal-grant *versus* domain-wide, and the case against domain-wide
included "its key is a file on your Mac". That was **false of this estate**: its
Workspace identity is deliberately **keyless**, reached by impersonation, built
that way *because* a key file had gone wrong there before. Re-briefed on the
correct facts he ruled for **both, delegation first** — and added a standing
constraint: *secrets belong in a secret store (Keychain, SOPS+age, OpenBao),
never loose in a file.*

Three things follow, and they sharpen the addendum rather than replace it:

- **The preferred route stores nothing at all.** Where the delegation is
  available it adds no credential, so the "first instrument to hold a
  credential" framing is now conditional: it holds one only when it falls back.
- **The plaintext-file fallback is removed, not deprioritised.** A fallback that
  lowers the bar is reached exactly when something else has already gone wrong.
  Off macOS `ccmail` refuses to store and names the estate's real stores.
- **A fallback is still owed.** The delegation depends on a cloud login that
  lapses, and an instrument promising "any session, any repo" cannot be dark for
  a day. Preferring the route that stores nothing is not the same as pretending
  the other is unnecessary.

**A correction worth keeping as method, not just as a fact:** the wrong option
was nearly chosen because the *brief* was wrong, not because the ruling was. The
facts that overturned it were already written down in the estate's own registry
and would have been found by reading it first. "Check what already exists before
offering to build" is the cheap lesson; "an approval extracted on a wrong fact
stands as the principal's word and is challenged by re-briefing, never voided
quietly" is the load-bearing one.

## Addendum (2026-09-09, third) — an instrument installed under another tool's name

**Decision (Mike, implicitly by commission — the attachment gap was not closed
until this landed):** admit **`ccpdf`**, a PDF page renderer built on macOS's own
PDFKit and installed as **`pdftoppm`**.

It exists because `ccmail` fetching a PDF turned out **not to be enough**. Claude
Code's file reader renders PDF pages by shelling out to poppler's `pdftoppm`, and
the machine has no package manager and so no poppler — so every PDF read failed
with an install instruction. An attachment successfully downloaded and still
unopenable is the *same* gap one step further along.

What it stretches, recorded in the layer's own practice of naming each stretch:

- **It is the first instrument that does not carry its own name.** Every other
  one is `cc*` or its own directory; this installs as `pdftoppm` because the
  reader looks up exactly that binary, and a renderer answering to any other
  name closes nothing. The mitigation is that `setup` **refuses to shadow a real
  poppler**, and prints its own one-line uninstall.
- **It is the first compiled instrument.** Swift, built by `swiftc` against a
  system framework — so it adds no runtime dependency at all, but it does add a
  *build-time* one (Xcode or the Command Line Tools), stated rather than silent.
- **It is arguably a general utility**, which ADR 0006's boundary sends to the
  estate. It passes on purpose all the same, by the same test `browser-fetch`
  passes: the operator opens PDFs in Preview and has no use for this whatsoever.
  It exists solely so the teammate can read a document it otherwise cannot.
