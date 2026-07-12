# 2026-07-12 · session 41 — commit signing activated (Opus)

Mike: "Lets register a signing key — guide me through." The signing doctrine
(SIGNING.md + ADR 0007) had been decided-but-dormant since session 39 and cleared
by the session-40 cold review; the only thing owed was step 1 of the activation
ladder — the principal's act. This session walked steps 1–3 and left 4–5 for a
scoped follow-up.

## The split held: step 1 stayed Mike's, steps 2–3 the agent's

Doctrine puts key generation + GitHub registration on the principal (a new trust
surface on his identity infra, AUTONOMY floor), and it was honoured literally:
Mike ran `ssh-keygen` (passphrase set — the intended posture) and, after a
`gh auth refresh -s admin:ssh_signing_key` scope top-up, `gh ssh-key add --type
signing`. The passphrase never passed through the agent. Registered as key id
`1048805`, type `signing`.

## Step 2 — machine wired, boundary set, proven on both planes

- Canonical **`allowed_signers`** written to atelier root: one entry,
  `namespaces="git",valid-after="20260712"` (quoted — the review's G-fix against
  the "missing start quote" parse failure on macOS ssh-keygen), append-only header.
- Global git config: `gpg.format=ssh`, `user.signingkey`, `commit.gpgsign=true`,
  `tag.gpgsign=true`, `gpg.ssh.allowedSignersFile` → the atelier file.
- **Adoption boundary = atelier `958b1ea`** (the commit that landed
  `allowed_signers` itself). Verification proven on both planes the doctrine
  requires: `git verify-commit` → *Good "git" signature for mike@cxi.nz* (durable <!-- leakscan:allow: author's own git identity in a live verify-commit output quote; same case as the CLAUDE.md convention line (ADR 0005) -->
  plane, against the trust list), and `gh api …commit.verification.verified` →
  `true, reason: valid` (badge plane). Both review traps dodged live — quoted
  timestamp parsed, boundary set *forward* (no history rewrite, ADR 0002 pins
  intact).
- Two operational facts surfaced by driving it, not predicting it: (1) the
  passphrase key must be loaded — `ssh-add --apple-use-keychain` caches it in the
  login keychain so signing runs unattended (SIGNING.md's passphrase-in-agent);
  (2) leakscan blocks `allowed_signers` on its principal email — a false positive
  (the emails are the data the format holds), exempted via a narrow
  `.leakscanignore` glob, same category as the plugin-manifest exemptions.

## Step 3 — the intent baked into new repos

`create-repo`'s git-init block and REPO-STANDARD's new-repo process now both bake
repo-local `commit.gpgsign=true` (belt-and-braces so a new repo signs even where
global config drifted; signing itself stays a machine property).

## shed — the credential remembered (Mike's steer)

Mike's instinct — "shouldn't shed have a script for this?" — was half-right and
sharpened the boundary. **No script:** an SSH signing key is generated locally
and registered once, not minted from a provider root, so shed's mint pattern
(`mint_cloudflare.py`) doesn't apply and a `mint_github.py` would be ceremony.
**But a registry entry, yes:** a distinct `signing_keys` array under shed's
`github` provider now records the key's id, location, and roll story (metadata
only — validate.py green). Two house-consistent calls: the fingerprint is *not*
stored (its 40+ char base64 run trips validate.py; recompute via `gh`/`ssh-keygen`),
and the principal is *referenced* to atelier's `allowed_signers` rather than
duplicated (one-fact-one-home, and it sidesteps leakscan without a scanner hole).
The entry flags the live boundary question: this key's **secret** is person-level
(Apple Passwords), yet the whole fleet **trusts** it as estate provenance infra —
the open "where estate credential governance lives" ADR.

## Steps 4–5 taken up (Mike: "do 4 + 5 now", CI warns-first)

**Step 5 — CI verification, built as a tool not YAML.** The review's mandated
"known-signed-fixture selftest" only means something if it runs, so the logic
went into `tools/signscan.py` (a testable house tool with `--selftest`, like the
scanners), not inline workflow bash. signscan verifies `boundary..HEAD` against
a trust list, two-plane by necessity: machine-key commits locally via
ssh-keygen; GitHub web-flow merge/squash commits **deferred** to the gh-api
plane (never failed — two already sit on atelier's main). `--selftest` carries a
throwaway ed25519 signature whose quoted, `Z`-suffixed `valid-after` guards both
parse traps; a tampered-payload negative proves the check has teeth. Wired into
atelier's `ci.yml` and the child `floor.yml` template (`fetch-depth: 0`, both
planes, warn-first). Trust list read at the child's **pin** via
`git show <pin>:allowed_signers`, never floating main (review G7). 11 tests.

**The dogfood earned its keep — a timezone bug, caught before any child.** The
first CI run went `0 good, 3 bad`: bare `valid-after="20260712"` is read in the
verifier's *local* timezone, so it passed on the UTC+12 author machine and
failed in the UTC runner ("key is not yet valid" — a 02:13 NZST commit is 14:13
the *previous* UTC day, before a local-midnight window start). Fixed by
UTC-anchoring with a `Z` suffix (`"20260711Z"`) before the earliest commit's UTC
time; SIGNING.md now mandates it, the selftest fixture guards it. Running
atelier's own CI *before* touching the fleet is precisely what surfaced it — the
"proven on both planes" from step 2 was the local `verify-commit` + the GitHub
badge; the CI *sweep* is a third check, and it found the config bug the other
two couldn't.

## Step 4 — fleet retrofit (done; faves/ros deferred)

The fleet splits three ways, which changed the plan (Mike: "take your
recommendation"): **10 children carry the house `floor.yml`** — uniform retrofit;
**faves + ros run bespoke `ci.yml`** (menu-validate/SBOM, router config) and
never adopted the house floor — a pre-existing standardisation gap, so their
signing-CI was **deferred** to a separate floor-adoption pass (they still sign
every commit — only CI *verification* waits).

The 10 retrofit each: pin bumped to a signing-aware atelier SHA (picks up
`allowed_signers` + signscan), the floor signing steps rolled in (overwrite from
the proven template, `--disable` re-applied for the two network repos), and
`SIGN_BOUNDARY` set to the repo's pre-signing HEAD so its unsigned past stays
unflagged. numen piloted first — its CI resolved the trust list at its own pin
via `git show <pin>:allowed_signers` and reported `1 good, 0 bad`, proving the
*child* pattern (distinct from atelier's in-repo trust list) — then the other 9
in a batch, each signed + verified + pushed.

**Result: 7 CI-green** (numen, Baby Brain, ec2_builder, FoodTracker,
hitchbots_guide, nova, shed). **3 red on pre-existing scanner debt**, confirmed
by each repo's *prior* run being red too: they fail at the secretscan/leakscan
stage, which runs *before* the signing steps, so signing never even executes.
That debt is the owners' (one child's floor was "red by design" at adoption);
which children, and what debt, lives in their own private records — not
detailed here (public repo; the names were joined to the debt in this file
until the session-47 scrub). shed's boundary is its pre-signing HEAD `5bdee55` (it already carried
one signed commit, the registry entry).

## Honest close

Signing is **fully active, warn-first**. Ladder steps 1–5 done; SIGNING.md,
ROADMAP, CHANGELOG, and this log say so with the apex's done-vs-stubbed honesty —
including the two things NOT finished: faves/ros signing-CI (deferred) and the
warn→block flip (Mike's call once the pre-existing scanner debt clears). Vigilant
mode stays off until the fleet is fully green. The dogfood earning its keep — a
timezone bug caught on atelier before a single child was touched — is the session's
one real lesson: verify the mechanism on yourself first.

## Tail — the papercut, and two items logged

Mike flagged the passphrase-in-agent papercut ("couldn't load key") for a
findable home. Closed both ways, in atelier so they travel: a **pre-commit
signing pre-flight** (fast non-interactive test-sign → prints the `ssh-add`
remedy the moment signing looks unready; silent when ready, never blocks, only
after scanners pass) and a **SIGNING.md Operational notes** section as the
durable record. Verified silent on a real commit with the key loaded.

Two things Mike raised for the future. **Reply/reporting style — reframed out of
atelier.** First logged as a candidate `method/REPORTING.md`; Mike then clarified
the purpose is *for the agent to understand him*, not rules the agent recites —
which makes it personal context (a named person's communication preferences), and
the no-personal-data boundary keeps that in `~/.claude/`, never public atelier.
Written into `~/.claude/CLAUDE.md`'s "Working with me" (visual reader →
iconography/tables; outcome-first-then-evidence; watch volume, structure replaces
length). The honest call was *not* to build an atelier doc — the boundary decided
it. **browser-fetch** (a Python Chrome-driving MCP server) as a teammate
*capability*: **boundary decided** — `instruments/` widens to admit capability
tools whose value is the working-together relationship (ADR-0006-extending, amend
when built). Still owed before any code moves: a pre-public scrub of `server.py`
and the zero-dep-ethos-vs-deps call. Not started.
