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

# Verdict — PASS-WITH-FINDINGS · 0 MAJOR / 1 MODERATE / 0 minor / 2 notes

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

## Faithfulness to the FS rulings (written at reconcile)

## Reconcile (intent records opened after the findings above were committed)
