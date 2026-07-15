# 2026-07-15 · 1327 UTC · CONVENTIONS.md + UTC-at-rest ADR — the default-frame doctrine

*(Identifier `1327` is UTC — the first record named under the rule this session
set. The authoring machine's local clock already read 2026-07-16.)*

## What prompted it

Mike: "we have date and time scattered around in the repo's file names and
content. Do we say anywhere what timezone we are using?" We didn't. The search
found timezone stated in exactly one place — SIGNING's `Z`-anchoring of
`allowed_signers` `valid-after`, born from the CI dogfood bug — and only for
machine timestamps that cross the CI boundary. Every human-facing stamp (session
and ADR `HHMM` identifiers, prose dates) was implicitly the author machine's
local NZ time, with nothing saying so, hence un-anchorable to a reader in another
zone.

## How the doctrine sharpened, over four Mike refinements

1. **"Not an instruction to append NZT to everything."** The rule is *state the
   frame once at the boundary*, not tattoo it on every value — over-labelling is
   its own failure (noise costs a reread). His currency analogy set the spec: NZD
   named once in the UX, not prefixed to each `$`.
2. **The ELT point is a precedence, not an exception.** External data we don't
   own is kept as-is because "preserve the data" *outranks* "normalise to UTC" —
   integrity/verifiability over normalisation. The kept data then re-enters the
   label rule as a labelled deviation, its zone stored as metadata. So it's not a
   carve-out; it falls out of the same rule plus one precedence.
3. **"A human reasonably assumes their local frame unless signed otherwise."**
   This corrected "the label is what makes it safe": the real rule is *a shared
   default carries silently; label only a deviation or a collision*. Watch face =
   silent; wall of clocks = each labelled; foreign country = you stepped outside
   the shared default. The bug is a *silent deviation from an assumed-but-not-
   shared default* — the assumption in "the mother of all …".
4. **"Never per value" is too strong.** ~99% "declare once", but risk/context can
   justify per-value labelling as the deliberate exception. Codified as a rule of
   thumb, not an absolute.

Also settled: the word is **convention**, not practice (practice is already the
loaded term in TOOLBOX's practice/instance split); identifiers go **UTC forward**
(a key belongs in the canonical zone); **two artifacts** — the ADR *decides time*,
the method doc *states the general rule* so the next unlabelled-value case has a
home instead of becoming ADR number eight.

## Built

- **`method/CONVENTIONS.md`** — names the anti-pattern (an unlabelled frame) once;
  the three-clause rule (declare-once-and-silent · label-deviation-or-collision ·
  precedence-on-conflict); worked examples (sticker / border / clock wall); a
  declared-defaults table (UTC at rest · NZD · ISO 8601 · UTF-8 · NZ English + te
  reo), roles-not-instances so an adopter substitutes their own.
- **ADR `2026-07-15-1327`** — time's worked instance: UTC at rest, local+labelled
  on presentation, identifiers UTC-forward (existing files keep their names,
  boundary at this ADR), foreign-data precedence (ELT not ETL). Its own UTC `1327`
  identifier against a local 07-16 clock is the rule dogfooding itself.
- Both indexes wired (method/README read-order item 14, decisions/README).

## Delivery notes

- Written before a session-limit pause + a macOS-update reboot. Recovered clean:
  all four changes survived staged, no other session had touched the tree, floor
  re-run green (leak · link · size · licen).
- **Reboot cleared the ssh-agent** → the signed commit failed (key not loaded,
  passphrase is Mike's and never reaches the agent). Mike ran
  `ssh-add --apple-use-keychain`; commit `67e8582` then signed + pushed.
- **Config drift caught in passing:** `~/.gitconfig`'s
  `gpg.ssh.allowedSignersFile` still pointed at the dead iCloud path from the
  2026-07-14 STORAGE move, so local `git verify-commit` couldn't reach the trust
  list. Repointed to `~/.pets/atelier/allowed_signers`; HEAD now verifies as a
  good signature against the trust list. Machine-local fix, not committed.

## Audit against the feedback (post-commit)

Mike asked for a pass over every prompt from the opening timezone question
forward, to confirm the commit takes all of it into account. 9 of 10 points
were faithfully captured (convention-not-practice · four declared defaults ·
~99%/exception softening of "never" · ELT precedence · no-retro-rewrite ·
UTC-forward identifiers · sticker/watch/clocks/border examples · ISO 8601 named
· two artifacts). Two fidelity gaps found and fixed in `198cf32`: CONVENTIONS.md
claimed the onramp pointed to it when CLAUDE.md didn't (fixed — the claim is now
true, and readers reach the canonical doc); and clause 3 carried only one of
Mike's two stated ELT reasons (added the second — no transform cost on data we
didn't author).

## Owed

- **Cold review ⏳ queued** (ROADMAP, review-owed): self-authored doctrine, so its
  author can't warm-spawn the pass (rule 4) — a non-author takes it and writes the
  brief. Seeds in the ROADMAP item.
