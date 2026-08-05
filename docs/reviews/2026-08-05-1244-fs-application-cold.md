# Brief — FS1–FS5 application on `floorfleet`, rule-4 cold pass

**Queue ref (refs only):** the FS1–FS5 application (the B2+B3 cycle's
application pass; the FS1 MAJOR keeps the cycle open past it). Delta:
`tools/floorfleet.py` + `tools/test_floorfleet.py` (landed 2026-08-03, merge
`10b71b6`) — the discovery-authority footer + `--json` field, the
three-outcome remote read with `unknown` rows that red `--check`, the
token-spec statement in four surfaces, the wired-denominator headline, the
archived/unreadable footer counts, the `green("")` docstring + selftest
legs, and one out-of-scope crash fix (a repo with no floor config felled
`render`).

**Pass type:** application cold pass (rule 4).

**Provenance (rule 4):** reviewed by a Fable session Mike spawned onto the
queue; the author sessions (the 2026-08-03 orchestrated run and its
workers) neither started nor instructed this session. Brief written by the
taker, cold. The FS verdict and the harvested ruling entry were **not
opened** before the findings below were committed; read at reconcile only.

**Non-goals:** the C1F3 residue on `floorfleet`'s parse seam (child-authored
reason strings printed raw) is already tracked as its own ROADMAP item and
is not re-found here; the five-red-floors work is the children's own. Board
output from the live run is held in the session scratchpad and reported
here in classes only, per the private-repo × posture join rule.

# Verdict — PASS-WITH-FINDINGS · 0 MAJOR / 2 MODERATE / 0 minor / 2 notes

**What was verified live at HEAD, not read from the delta's account:**

- Selftest 0 failures; the floorfleet unit suite passes (13 FS-referenced
  test anchors); the full repo suite is green (933).
- **The crash fix is real**: a bare repo with no `.atelier-floor.json`
  renders a board row (probed live); before the fix the account says
  `render` fell over — the fix initialises `advisory` as the C1 dict every
  reader expects, and the discovery note ("every child on this estate
  happens to carry the file, so the crash path was never walked") is the
  honest kind.
- **The fail-safe contract holds live**: a full `--remote --status --check`
  estate run rendered 16 rows (parent + 15 children), all wired, a
  minority not proven green, and exited 1 — only `passing` is green, and
  the wired-denominator headline (FS2) reads over wired rows only, with
  the not-wired count fenced in its own line so the denominator can never
  read as the whole estate.
- **`green("")` is pinned both directions** (FS5): the selftest carries
  the sentinel legs (no `--status` collapses to `ok`, wired and unwired),
  plus every non-passing run state proven not-green, and
  unwired-but-passing proven not-green.
- **The three-outcome read exists and is used where it matters** (FS1(b)):
  discovery calls `_read_remote_slug_result`, only a 404 is `missing`,
  everything else is `failed`, and a failed read becomes an `unknown` row
  that reds `--check` (pinned in the selftest). The content reads keep the
  two-outcome helper with the reason documented (absent and unreadable
  both classify not-wired).
- **The discovery-authority footer and `--json` field** (FS1(a)): listings
  reported per endpoint with counts, archived and unreadable counts print
  at zero (known zeros, stable field set), `private_blind` warns when the
  private-capable listing returns nothing, and the JSON carries
  `discovery_authority` for the scheduled consumer.
- **The token-grant statement stands on four surfaces**: the module
  docstring's blind-spot section, the `--from-github` help text, the
  `discover_github` docstring, and the empty-estate failure message.
- **FS4**: `read_run` returns (state, detail, authority) on every path and
  the annotation now says so.

## Findings

**FF1 (MODERATE) — a missing `gh` binary crashes the remote plane, against
the tool's own documented contract.** `_read_remote_slug_result`'s
docstring names "no HTTP status at all (network, no `gh`, not
authenticated)" as a read-we-could-not-make, mapping to `failed` — but a
missing binary raises `FileNotFoundError` out of `subprocess.run` before
any outcome exists, and none of the three `gh` call sites (`_gh_json`,
`_gh_list`, `_read_remote_slug_result`) catches `OSError`. Probed live:
`--remote` with `gh` off PATH dies with a traceback, exit 1 — which under
`--check` aliases the legitimate "estate unguarded" red, and without
`--check` is an exit code the contract does not define. The failure
direction is safe (loud, never a false green), so this is not a MAJOR;
but the B1 scheduled consumer inherits a traceback path where the design
promises a diagnostic one, and the exit-code contract (0 / 1-with-check /
2-environment) says a missing tool is exactly the 2 case. Fix shape: a
small wrapper catching `OSError` at the three call sites, returning the
documented failure values — no behaviour change when `gh` exists.

**FF2 (note) — the `unknown`-state detail wording predates the
three-outcome read.** `classify`'s `unknown` covers "floor.yml present but
neither a caller nor a copy", while a discovery-level failed read produces
its own row wording. Both render under the same ⚠️ state name on the
board; a reader has the detail sentence to tell them apart. Cosmetic;
recorded because the state vocabulary now carries two different kinds of
not-knowing.

**FF3 (note) — the local hook column under `--remote` still reads this
machine's clone.** Documented correctly in the docstring's residual (and
`--from-github` reports `n/a`), so this is not a defect — recorded because
the mixed-plane row (remote shim, local hook) is the one place a reader
must hold two planes in one line, and the board's wording carries it.

**FF4 (MODERATE, found at reconcile) — the prior FS verdict carries the
private-repo × posture join, on public main, and has since 2026-07-29.**
The B2+B3 verdict's *Re-run and verified* section
(`reviews/2026-07-29-1251-b2b3-floorfleet-status-cold.md:121`) names four
children beside their not-proven-green run state; all four verified
private (visibility read live, detail in the session scratchpad only).
This is the exact join `ROADMAP.md` § *Candidate invariant* records as
breached three times and deliberately avoids ("naming which private repo
holds …" — the classes-only rule this verdict follows), and it recurred at
the recorded trigger moment: summarising fleet scan state into an atelier
record. Not this delta's defect — the verdict predates the application —
but the pass's scope is the whole commitment, and a standing instance in
the same cycle's own record store is in it. Counsel: rewrite that
section's line to the classes-only form (count, not names) at HEAD —
history keeps the old text as it keeps everything — and count this as the
invariant item's **fourth instance**, which is further evidence for
mechanising the join check it already proposes. The names are not
restated here; the file:line ref is the pointer.

## Faithfulness to the FS rulings (written at reconcile)

- **FS1(a) — faithful.** Discovery-authority footer with per-listing
  endpoint + count, archived and unreadable counts printed at zero, the
  private-blind warning, and the `discovery_authority` JSON block; the
  empty-estate failure path prints the listing counts too.
- **FS1(b) — faithful.** The three-outcome read; only HTTP 404 is
  `missing`; a failed read renders an `unknown` row that is neither ok nor
  green (selftest-pinned) and reds `--check`. The old outsider conflation
  is gone from discovery; the content reads keep the two-outcome helper
  with the reason stated.
- **FS1 token spec — faithful on every surface atelier carries** (module
  docstring, `--from-github` help, `discover_github` docstring,
  empty-estate message). The consuming workflow's comment in the
  estate-root repo is the remaining surface and is already tracked as its
  own ROADMAP item — not re-found here.
- **FS2 — faithful.** `unproven` filters on `i.ok`; the not-wired count is
  fenced in its own line so the denominator cannot read as the estate.
- **FS3 — faithful.** The archived count prints, at zero too.
- **FS4 — faithful.** The 3-tuple annotation matches every return.
- **FS5 — faithful.** The sentinel is named in `green()`'s docstring as
  the compatibility contract and pinned both directions in the selftest.

## Reconcile (intent records opened after the findings above were committed)

Opened after the findings commit: the FS verdict
(`2026-07-29-1251-b2b3-floorfleet-status-cold.md`, rulings FS1–FS5) and
the harvested entry (`ROADMAP-DONE.md` § *B2+B3 FS rulings applied*).

- **No contradictions; no pre-emption.** FF1 appears in neither the
  verdict nor the account: the FS pass verified the `gh`/`git` calls are
  list-argv (injection surface) but did not probe a missing binary, and
  the docstring sentence FF1 falsifies was written by this delta.
- **The account's claims reproduce:** suite growth (+22 in floorfleet's
  file — 88 collected at HEAD), the crash fix's honesty note, the live
  `--from-github` end-to-end run (this pass's own live run reproduces the
  class: all wired, a minority not proven green, exit 1 with
  `--status --check`).
- **The C1F3 floorfleet-seam residue** the account records as handed to
  Track C is confirmed present (child-authored reason strings still print
  raw through `_advisories` → `render`) and is already a ROADMAP item —
  kept a non-goal here.
- **FF4 arose from the reconcile read itself**, recorded above with the
  restatement withheld.

## Disposition — the B2+B3 cycle CLOSES (0 MAJOR); findings to Mike

This is the B2+B3 cycle's application pass; its FS1 MAJOR held the cycle
open, and this pass returns **0 MAJOR**, so per REVIEW.md's no-MAJOR rule
the cycle **closes — terminal**. FF1 (missing-`gh` crash), FF4 (the
standing join in the prior verdict) and the two notes are counsel to Mike
(rule 3): FF1 is a small wrapper fix at three call sites; FF4 is a
classes-only rewrite of one line in a landed record plus a fourth-instance
tally on the invariant item.

