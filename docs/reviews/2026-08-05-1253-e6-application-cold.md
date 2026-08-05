# Brief — E6 application (E6a + E6c slices), rule-4 cold pass

**Queue ref (refs only):** the E6 application, E6a + E6c slices. Delta:
`docs/method/SECRETS.md` § *The boundary's posture — over-flag, because
detection enables everything* (landed 2026-08-03, merge `75f52df`); the
E6c/SF carve-outs + canary suite in `tools/secretscan.py` +
`tools/test_secretscan.py` (landed 2026-08-03, merge `47709df`); the
specimen allow-marker in the SF verdict and the triage record's dated
correction (same merge).

**Pass type:** application cold pass (rule 4 — the E6a slice is doctrine by
function; the E6c slice is security-floor code).

**Provenance (rule 4):** reviewed by a Fable session Mike spawned onto the
queue; the author sessions neither started nor instructed this session.
Brief written by the taker, cold. The EI rulings and the SF verdict's
ruling text were not opened before the findings below were committed
(verifying the delta's own two-line and four-line record slices exposed
the diff hunks and nothing further); the full reconcile read follows the
findings commit.

# Verdict — PASS · 0 MAJOR / 0 minor / 3 notes

**What was verified live at HEAD, not read from the delta's account:**

- **The ruled six-shape probe reproduces at 6/6.** Under credential-named
  keys, all six shapes flag: hex letter-leading, hex digit-leading, hex
  uppercase, base32, and both passphrase spellings (kebab and snake).
- **Suppression precedence holds exactly as ruled**: placeholder,
  indirection (`${VAR}`), extensionless mount path, code reference
  (`admin_password`) and the three-word name (`yes-access-request`) all
  stay clean — the carve-out sits *after* the statements-of-what-a-value-
  is-for and *before* every variety-reading gate, in the code and in the
  probe.
- **The blocking set only widened — structurally, not just empirically.**
  The carve-out adds a `return True` branch; every previously-blocking
  path is untouched, and the context-free net is unreached by it (a bare
  40-char SHA in prose probes clean, unchanged).
- **The canary suite guards the gate as claimed**: 16 shapes across six
  families, every-canary-flags with a fix-the-gate-not-the-fixture failure
  message, the count pinned (≥ 16 + dedupe) so shrinking it must be
  deliberate and principal-visible.
- **E6a's doctrine text carries each ruled element**: the stated intent as
  the bar; over-flag as the fail-safe direction with the cost asymmetry
  argued; the leakscan/secretscan drift as found-and-decided; rotation-
  presupposes-detection as the grounding (and explicitly *not* a
  risk-ranking claim); coverage narrowing as the principal's decision,
  never a code comment; the advisory dial as decided-not-built with the
  named-consumer precondition; leakscan-gains-no-advisory-form as decided
  asymmetry. Grounding links resolve.
- Suite green via the canonical invocation (`unittest discover -s tools`,
  933 OK); the SF-verdict allow-marker specimen and the triage record's
  dated correction are in the merge as named.

## Findings

**EA1 (note) — the E6c comment's own example lives mostly outside the
context that serves it.** The carve-out cites "base32 TOTP seeds" as a
covered sibling, and the shape does flag under generic credential keys
(`secret=`, `api_key=`) — but the natural TOTP key spellings (`totp_seed`
and the `*_seed` family) are not in `SECRET_KEY_RX`, so the cited
habitat's most likely key name never enters assigned-secret context. Not
this delta's defect (the key list predates it) and not a carve-out gap;
recorded as ready-made counsel for the E6b/E6d pickup, where E6's own
reasoning says key-context is the nearly-free axis to widen.

**EA2 (note) — the standalone test invocation cannot import its subject.**
`python3 -m unittest tools.test_secretscan` fails on sibling import;
the canonical `discover -s tools` form works. Every sibling test file
shares the pattern, the repo's documented invocation is the discover form,
and nothing is owed — recorded so the next session's first failed run
costs a sentence, not a chase.

**EA3 (note, from reconcile) — EI4's correction sits in the item's ruling
recap, not its narrative.** The ruling asked the E6 item to name
`HIGH_ENTROPY_RX`'s mixed-class requirement as the real narrowing site
alongside `SLUG_RX`; the item now does, but only inside the EI1–EI6 recap
paragraph, while the body's narrative still tells the `SLUG_RX`-first
story. The letter is met; a reader of the narrative alone inherits the
half-story the ruling corrected. One-sentence weave if Mike wants it.

## Faithfulness to the rulings (written at reconcile)

- **EI1 — honoured by restraint.** E6b remains unbuilt; E6a's doctrine
  states the precondition ("may not be built until its design names where
  advisory findings surface durably and whether they must be
  acknowledged"). Mike's 2026-08-04 consumer naming discharges the
  precondition going forward and contradicts nothing in the delta.
- **EI2 — applied** in E6d(ii): class terms only in public trees.
- **EI3 — honoured by restraint**: E6b/E6d left unclaimed as
  bring-proposals-at-pickup, exactly as ruled.
- **EI4 — applied, minimally** (EA3 above).
- **EI5 — applied verbatim**: the posture grounds on rotation-presupposes-
  detection, with the risk ranking explicitly demoted to colour.
- **EI6 — applied, all three legs**: per-plane advisory semantics are in
  E6b's consumer text; E6a-first ordering held (E6a is landed, E6b is
  not); the leakscan asymmetry recorded as decided in E6a's closing
  paragraph.
- **SF1+SF2 (the carve-outs) — applied as ruled and generalised** under
  the E6c rule, live-probed 6/6 with precedence intact; **SF3 (canaries)
  — applied**, 16 shapes, pinned, contract stated; the SF verdict's
  specimen line carries its reasoned allow-marker.

## Reconcile (intent records opened after the findings above were committed)

Opened after the findings commit: the EI rulings
(`2026-07-29-1243-e6-intent-cold.md`), the SF verdict's ruling text
(`2026-07-28-1220-secretscan-fragment-cold.md`), and the harvested entry
(`ROADMAP-DONE.md` § *secretscan residue + E6c*).

- **No contradictions.** The account's live claims reproduced before the
  records were opened: the six-shape probe, the precedence order, the
  only-widened property, the canary contract.
- **EA1 converges with the account's own framing** — the harvested entry
  and E6's split both name key-context as the nearly-free widening axis;
  the `totp_seed` miss is a ready-made first instance for that build.
- **EA3 arose from the reconcile read**, recorded above.

## Disposition — the E6 intent cycle CLOSES (0 MAJOR); notes to Mike

This is the application pass the EI1 MAJOR held the cycle open for. It
returns **0 MAJOR**, so the E6 intent-review cycle **closes — terminal**
per the no-MAJOR rule. E6b and E6d remain open *build* items with their
own bring-proposals pickup shape and will queue their own pointers at
landing, as the roadmap already records. EA1–EA3 are counsel to Mike.
