# Sharing — public since 2026-07-10 (ADR 0005)

The private-first sequence (peer-adoption → restructure → *then* public) was
consciously collapsed: the peer-of-two never became a peer-of-three, so **public
is the friction mechanism**, not a reward withheld until after it. atelier is
public as a **named worked example** (README "If you're adopting this"). What was
"before public release" is now **post-public hardening**:


Completed sharing work (public release, the plugin bundle widening, atelier's own
CI, child-CI scanner floor, linkscan build + wiring) → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

### Cold passes from the 2026-07-29 publish-surface + deferral session — RUN

Four rule-4 pointers (the header here said "Three" until 2026-08-02 — the
landing commit's own count slip, RL4, corrected at this batch's close), taken
2026-08-02 by a qualifying Fable session (started by Mike, pointed at the
queue; the author session neither started nor instructed it). All four run
cold from the refs-only pointers; the shared intent record opened only after
all four verdicts were committed. **Mike ruled all 13 findings in-session
(2026-08-02, per-finding walk-through) and the taker session applied them
the same sitting** — decisions stamped in each verdict; the two 0-MAJOR
cycles (deferral, recurrence ladder) are CLOSED at their terminal
applications; the two MAJOR cycles' applications queue their own rule-4
pointers (§ *Application reviews* below). One process incident disclosed in
every verdict: a
records-sweeping grep fed the author's `SESSIONS.md` index entry to the
reviewer pre-findings (the SL2 channel class, second live instance).

- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS 1M/2m
  — [verdict](../../reviews/2026-08-02-2210-publish-surface-delta-cold.md). **The
  publication-surface delta** (`a9ab2cf`). PS1 MAJOR: REPO-STANDARD's
  standardise step 2 still instructs the committed allowlist the ruling
  retired — a standardiser following canon re-commits the exposure. PS2: the
  identical-bytes seed template residual is real but unnamed where the cost
  is named. PS3: the seeded `settings.local.json` template publishes a
  maximal unattended grant. RULED + APPLIED 2026-08-02 (all three as
  counselled, stamped in the verdict); the MAJOR keeps the cycle open —
  the application's own review is queued below.
- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  1M/1m/2n — [verdict](../../reviews/2026-08-02-2313-publishscan-cold.md).
  **`publishscan`** (`8bdcfaa`). PB1 MAJOR: `fnmatch` globs are not
  path-aware, so most never-publish entries match at the repo root only —
  nested `.npmrc`, `.env` variants, `.mcp.json` pass green. PB2: the
  stated reason-required mitigation on `.publishscanignore` is unenforced.
  RULED + APPLIED 2026-08-02 (all four as counselled, stamped in the
  verdict); the MAJOR keeps the cycle open — the application's own review
  is queued below.
- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  0M/1m/3n — [verdict](../../reviews/2026-08-02-2348-deferral-delta-cold.md).
  **The deferral delta** (`3acf7d2`). Core diagnosis and honesty discipline
  verified sound; DF1: the deferred-heading guard is vocabulary-anchored
  (prefix-only) while three doctrine surfaces claim unqualified cover.
  RULED + APPLIED 2026-08-02; no MAJOR ⇒ terminal application — **cycle
  CLOSED**.
- 🎯 REVIEWED 2026-08-02 (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  0M/3m/1n — [verdict](../../reviews/2026-08-03-0028-recurrence-ladder-cold.md).
  **The recurrence-ladder delta** (`4015e06`). RL1: the stop-at-first-fit
  rule lacks its own fitness test. RL2: rung 1 has an unmarked second
  original in REVIEW.md. RL3: two recurrence thresholds unreconciled.
  RL4 [fixed at this close]: the Three-over-four pointer count above.
  RULED + APPLIED 2026-08-02; no MAJOR ⇒ terminal application — **cycle
  CLOSED**.

### Application reviews from the 2026-08-02 rulings application

> 📦 **Both cold passes ran 2026-08-03, both cycles CLOSED (terminal, no
>   MAJOR), all six residue findings RULED and applied the same day** →
>   [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The two application passes —
>   PA1–PA4, PSA1–PSA2*. Nothing open remains in this section.

### Publication surface — what a public repo reveals about its own defences (2026-07-29)

*`review:` this section states direction, so it carries a review judgement:
**queued** — the doctrine deltas it drives (the allowlist amendment, the
publication-surface class) each queue their own `⏳` pointer at their landing
commit; the section itself is refs + work, not doctrine.*

**Where this came from.** `rpi` flipped PUBLIC on 2026-07-29 and its post-flip
cold pass (0 MAJOR, 11 findings) found F1: the committed `.claude/settings.json`
published the exact list of commands an AI session runs **unprompted**, at the
same moment going public opened untrusted inbound (issues, PRs) into those
sessions. `rpi` fixed it locally — and by doing so **diverged from this repo's
doctrine**, which mandates committing that file in four places
([`REPO-STANDARD.md`](../../build/REPO-STANDARD.md), [`TOOLBOX.md`](../../method/TOOLBOX.md),
`templates/gitignore`, `skills/create-repo`). The child was right and the parent
was wrong, and nothing carried that upward — the resolved-upward rule
(`method/PROPAGATION.md`) working only because Mike happened to ask.

**The class this opened, and why it is bigger than one file.** The estate's
guard files are *self-describing*: a repo that publishes where its checks are
switched off, or what its agent may do without asking, hands a reader a map. It
is a **reconnaissance** exposure, not a secrets one — secretscan and leakscan
both correctly report clean on every file below, because none of them contain a
credential or a personal fact. That is the gap: **the existing floor asks "does
this file contain something private?", and never "does publishing this file
weaken the repo?"**

**P1 — the command allowlist: RULED ⓑ (untrack everywhere, uniform) and
applied 2026-07-29** — atelier + all four doctrine surfaces done, children at
their next pin bump. Full ruling, its named cost, and what it does not undo →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § Sharing.

**P2 — `publishscan` built and registry-wired blocking, 2026-07-29.** The class
is mechanical now rather than a memory: it judges the **path**, not the
contents — the one question no other scanner here asks, and the reason both
content scanners passed `rpi`'s allowlist correctly. Build detail, provenance
per pattern, and the stated residual →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § Sharing. Its cold pass is queued below.
