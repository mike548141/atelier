# Review — the signing doctrine (SIGNING.md + ADR 0007)

**Scope:** `docs/method/SIGNING.md` and `docs/decisions/0007-ssh-commit-signing.md`
(commit `1588fda`, 2026-07-11, session 39). Review-owed with the standing
doctrine debt. The standard is **decided but dormant** (activation gated on the
principal registering a signing key), which makes this review cheap to act on —
nothing is wired yet, so a design defect found now costs a text edit, not a
fleet retrofit. That is also the risk: nothing has been *driven*, so every
technical claim in the doc is currently model-memory, not proof. Ground the
claims — `man ssh-keygen` / git docs / GitHub docs / a scratch-repo live drive —
don't take them.

**The three lenses, instantiated:**

1. *Approach & assumptions* — is SSH-native commit signing the right layer-1,
   and is the allowed_signers-in-atelier design sound for a fleet where children
   verify in CI?
2. *Correctness & quality* — are the mechanics as written actually how git/ssh/
   GitHub behave? Every config line, every claimed failure-mode property.
3. *Completeness / harvest* — what the activation ladder omits that will bite
   at step 2–5 time.

**Specific assumptions to attack:**

- **S1 — server-side commits are unaddressed.** GitHub itself creates commits:
  merge commits from the merge button / `gh pr merge`, squash commits, web-UI
  edits — signed by GitHub's own web-flow GPG key, not the machine SSH key
  (atelier's own PR #3 merge commit `a0ef731` is a live specimen — check it).
  A CI step verifying "every commit after the adoption boundary" against
  `allowed_signers` would fail on every such commit. Does the doctrine's CI
  verification design survive contact with its own repo's history? What's the
  honest fix — verify authored commits only, first-parent exceptions, GPG-key
  allowlisting, or stating the boundary differently?
- **S2 — `allowed_signers` semantics.** `valid-after`/`valid-before` are
  claimed to make the file append-only-with-bounded-retirement and to keep old
  signatures "verifiable forever". Verify against `ssh-keygen -Y` reality: does
  `git verify-commit` pass the commit's timestamp as the verify-time, or does
  bounding a retired key un-verify its old signatures? What principal string
  must entries carry, and does the doc say?
- **S3 — key custody vs the vault claim.** The key is called "person-level,
  personal vault" — but signing runs on every commit, on every machine the
  agent commits from, so the private key (or an agent socket) must be live on
  the machine. Is the custody claim stated at its true strength, or does
  "vault" over-claim?
- **S4 — the adoption boundary is hand-waved.** "CI verification from each
  repo's adoption boundary; record each boundary" — recorded *where*, read by
  CI *how*? Is step 5 actually executable as specified, or a stub written in
  the present tense (RECORD's stub-honestly rule)?
- **S5 — `user.signingkey <path>.pub`** — confirm the private-key-discovery
  behaviour (same-dir private key vs ssh-agent), and that pointing at the
  `.pub` is correct rather than the literal key string. What breaks on a
  machine where the key lives only in an agent?
- **S6 — the badge claims.** "Remove the key and history shows unverified
  again" and vigilant-mode behaviour — verify against current GitHub docs;
  these drive the "durable plane vs UI sugar" argument.
- **S7 — child CI fetches `allowed_signers` alongside atelier's tools** —
  floats `atelier@main` like the scanner floor. Does the floating-trust-list
  argument hold for a *trust* artifact the way it held for scanners (N1–N3
  case), or is a pinned trust list the honest default here?
- **S8 — rejected-alternatives fairness.** Especially "GPG: no capability SSH
  signing lacks in this estate" — is that true for the server-side-commit
  problem in S1 (GitHub's web-flow key is GPG)?

**Reviewer:** cold fresh-context agent (2026-07-12), read-only in the repo (a
scratch repo elsewhere for live drives is encouraged); fixes applied by the
coordinating session after the verdict. Review deep, not fast. Verdict below
the divider, findings with stable IDs (G1, G2, …).

---

**VERDICT: PASS-WITH-FINDINGS**

Cold fresh-context review, 2026-07-12, read-only in the repo. Method: every
mechanical claim was live-driven in a throwaway scratch repo (git 2.50.1,
OpenSSH 10.2p1) with generated ed25519 keys — sign, verify, backdate, bound,
retire, break — plus inspection of atelier's own history
(`git cat-file commit a0ef731`), a live `gh api` probe, `man ssh-keygen` on
this machine, and current GitHub docs via fetch/search with corroboration.
Scratch repos deleted after the drive. The layer-1 design core survives
contact: the five-line config block works verbatim (T1), `.pub` in
`user.signingkey` is the right choice (T8a–c: agent or adjacent-file
discovery, fails closed otherwise), and the crown-jewel claim — bounded
retirement keeps old signatures verifiable — is **true and now proven**,
because git passes the commit's committer timestamp as `ssh-keygen`'s
verify-time (T6's error message states it outright: "verify time 2025-01-15 <
valid-after 2025-02-01"; T7 retired a key and both eras verified). But three
claims the doctrine states as fact are false or break on this estate's own
machines, and the CI design fails on atelier's own history. All are
text-edit-cheap now, exactly as the brief predicted.

**S1 — server-side commits: confirmed, the sharpest finding.** atelier's
`main` already holds two commits committed by `GitHub <noreply@github.com>` <!-- leakscan:allow: GitHub's public web-flow committer address, not personal data -->
(`a0ef731`, `4b2cf6f` — both PR merges), GPG-signed by GitHub's web-flow key.
The doctrine's CI step ("verify signatures over commits after the adoption
boundary" against `allowed_signers`) fails on every such commit:
`git verify-commit` on them requires gpg plus the web-flow public key in a
keyring; on the estate's own machine even `git log --format=%G?` errors
("cannot run gpg: No such file or directory"). Since the house PR flow itself
mints these, the design as written red-flags its own repo on first
activation. The honest fix is two-plane: local SSH verification for commits
not committed by GitHub; for `committer == GitHub <noreply@github.com>`, <!-- leakscan:allow: GitHub's public web-flow committer address, not personal data -->
assert `gh api repos/<repo>/commits/<sha> --jq .commit.verification.verified`
is true — live-proven against `a0ef731` (`verified: true, reason: valid`). A
committer-string exemption *alone* is spoofable (anyone can set that
committer); the API check is what closes it, and `gh` is already the house
tool, so zero-dep survives.

**S2 — `allowed_signers` semantics: core claim true, two traps found.** "Old
signatures stay verifiable forever" holds (T6/T7, above). Traps: (a) the
*unquoted* `valid-after=20250101` format — the man page's own format — fails
to parse on this machine's ssh-keygen ("bad options: missing start quote"),
and a parse failure fails verification of that entry entirely ("No principal
matched"); quoted values (`valid-after="20250101"`) parse and verify on the
same binary and sit within documented syntax (G3). (b) git does **not** bind
key to committer identity: an entry whose principal is `other@example.com` <!-- leakscan:allow: RFC-2606 example-domain address from the review's live drive -->
happily verifies a commit by `tester@example.com`, exit 0 (T4). The file's <!-- leakscan:allow: RFC-2606 example-domain address from the review's live drive -->
principal strings are labels git reports, not bindings it enforces — and the
doc never says what principal entries must carry (G4).

**S3 — custody: over-claimed.** "Lives in the operator's personal vault"
cannot be the whole truth when signing runs on every commit: a working
private key (or an agent holding it) must be resident on every committing
machine, readable by the agent process. The doc's own "what a signature
honestly claims" section states the true strength (machine custody); the Key
handling section is not aligned with it (G5).

**S4 — the boundary: yes, a stub in the present tense.** "Record each
boundary" names no home and no read mechanism, and the sketched CI step has
an executable gap the ladder doesn't mention: `actions/checkout` fetches
depth-1 by default (the house's own `floor.yml` template uses the default),
so a from-the-boundary sweep sees no history at all without `fetch-depth: 0`
(G6). Step 5 is not executable as specified.

**S5 — `user.signingkey <path>.pub`: correct as written.** Live-proven: with
the `.pub` configured, git/ssh-keygen uses the agent if it holds the key,
else falls back to the same-basename private file (T8b — the live agent did
*not* hold the throwaway key, and signing still worked); with neither, the
commit fails closed with a clear error (T8a). A literal `key::ssh-ed25519 …`
value is agent-only (T8c). Agent-only machines work provided the key is
`ssh-add`ed; the failure mode is loud, not silent. No change needed.

**S6 — badge claims: inverted; the doctrine states the opposite of current
GitHub behaviour.** GitHub keeps a persistent verification record: "GitHub
will not re-verify previously signed commits or retroactively adjust their
verification status in response to changes in the key's state" — removing
the key does **not** un-verify history. Corroborated across GitHub's own
docs and secondary sources; SSH signing keys additionally have no revocation
semantics at all. Both SIGNING.md ("remove the key and history shows
unverified again") and ADR 0007's consequences ("removing a key from GitHub
un-verifies its history there") are false (G2). The durable-plane
*conclusion* survives on better grounds — the badge is GitHub-controlled and
unauditable, `allowed_signers` is self-hosted — but the exposure playbook
inherits a real consequence: attacker-signed commits pushed before key
removal stay Verified on GitHub forever; only the local plane's bounds catch
them, and see G10 on backdating.

**S7 — floating trust list: the scanner argument does not carry.** Floating
the scanners distributes *fixes* (the N1–N3 case — a bug fix reaching every
child is the win, and a broken scanner fails loud). Floating
`allowed_signers` distributes *trust*: anyone with write access to atelier
`main` — e.g. a leaked auth token, precisely the compromise the doctrine says
the signing plane must burn independently of — appends a key and every child
CI trusts it immediately, silently, with no trace in any child. That defeats
the doc's own blast-radius separation argument. The honest default is
verifying against `allowed_signers` at the child's *existing* atelier pin
(ADR 0002 — the mechanism is already there), accepting that a new key fails
child CI until a visible, reviewed pin bump — which is the correct behaviour
for a trust root. Residual to state either way: signature CI cannot defend
against full repo-write compromise of the repo hosting the trust list
(attacker adds key + commits in one push, self-attesting); branch protection
is the compensating control, and saying so is the apex applied (G7).

**S8 — GPG rejection: decision right, sentence over-claims.** "No capability
SSH signing lacks in this estate" is falsified by this estate's own `main`:
verifying its two server-side commits requires GPG (or the API plane), and
GPG has revocation/expiry semantics SSH signing lacks — which G2 shows
actually matters on the badge plane. Neither fact changes the decision
(adopting GPG wouldn't make web-flow commits verify against *our* key
either, and the keyring cost stands), so reword the rejection to its true
strength rather than reverse it (G8).

**Findings**

- **G1 [Blocking]** — CI verification as specified fails on GitHub
  server-side commits; two already exist in atelier `main` and the house PR
  flow keeps minting them. *Fix:* two-plane verification in SIGNING.md's
  Verification section and the eventual floor step — local
  `git verify-commit` for non-GitHub committers;
  `gh api …/commits/<sha> --jq .commit.verification.verified` for
  `GitHub <noreply@github.com>` commits (spoof-safe: a spoofed committer <!-- leakscan:allow: GitHub's public web-flow committer address, not personal data -->
  fails the API check). Live-proven both halves.
- **G2 [Blocking]** — "Remove the key and history shows unverified"
  (SIGNING.md) and "un-verifies its history there" (ADR 0007) are false:
  GitHub verification is persistent and non-retroactive; SSH signing keys
  have no revocation. *Fix:* correct both texts (ADR via addendum, house
  style); restate the durable-plane argument on its real grounds
  (self-hosted + audited vs GitHub-controlled); add the exposure
  consequence — pre-removal attacker signatures keep their badge, so the
  local plane is the only recourse.
- **G3 [Blocking]** — the man-page (unquoted) `valid-after=`/`valid-before=`
  syntax fails to parse on the estate's primary machine (OpenSSH 10.2p1:
  "bad options: missing start quote"), which fails verification of every
  bounded entry — and the doctrine mandates `valid-after` on every entry, so
  step 2 breaks on day one. Quoted values work on the same binary and are
  within documented syntax. *Fix:* mandate quoted timestamps in the
  doctrine's entry format, and add a parse selftest (verify a known-signed
  fixture) to the hook/CI so a syntax regression goes red, not silent.
- **G4 [Minor]** — git enforces key *membership*, not key↔identity binding:
  any listed key verifies any committer (T4), and the doc doesn't say what
  principal entries carry. *Fix:* state the convention (principal =
  committer email), state honestly that the assurance is machine-level
  unless CI additionally compares the reported principal to the committer
  email, and decide whether CI does.
- **G5 [Minor]** — "lives in the operator's personal vault" over-claims
  custody. *Fix:* align Key handling with the doc's own honest-claim
  section — vault holds the durable copy; every committing machine holds a
  working copy as a standing machine credential (SECRETS' tracked-debt
  framing; passphrase-in-agent as the mitigation).
- **G6 [Minor]** — ladder steps 4–5 are stubs in the present tense: boundary
  recorded nowhere named, read by nothing named, and the CI sweep needs
  `fetch-depth: 0`, which the floor template doesn't set. *Fix:* name the
  home (e.g. a boundary SHA env/file in the child's `floor.yml`), the read
  (`git rev-list <boundary>..HEAD`), and the checkout depth; until then mark
  the steps as stubs per RECORD.
- **G7 [Minor]** — child CI fetching `allowed_signers` from floating `main`
  makes the trust root silently mutable by exactly the auth-plane compromise
  signing is meant to survive. *Fix:* verify against the file at the child's
  existing atelier pin (ADR 0002); document the residual (repo-write
  compromise self-attests; branch protection compensates).
- **G8 [Minor]** — ADR 0007's GPG rejection ("no capability SSH signing
  lacks in this estate") is over-stated: GPG verification is needed for the
  history's own server-side commits, and GPG revocation semantics exist
  where SSH's don't. *Fix:* reword to "no capability we need for signing our
  own commits"; point at the G1 mechanism for the rest.
- **G9 [Low]** — badge activation conditions omitted from ladder step 1: the
  key must be uploaded as a *signing* key (doc has this) **and** the
  committer email must be a verified email on the account (doc omits this).
  *Fix:* one line in step 1. Vigilant-mode description checked out as
  written.
- **G10 [Low]** — `valid-before` bounding trusts the commit's own committer
  timestamp (T6), which a signer controls: an attacker holding a retired key
  can backdate into its validity window and verify locally. GitHub's plane
  is the complement (it checks key registration at push time), so the two
  planes cover each other — but the exposure playbook should say bounding is
  retirement hygiene, not revocation. *Fix:* one honest sentence in Key
  handling.

**Close.** The decision itself is right and now stands on live proof rather
than model memory: SSH-native signing is the correct zero-dep layer 1, the
config block is verbatim-correct, and the append-only-with-bounded-retirement
design does what it promises — the review's deepest drive (backdate, bound,
retire, re-verify) came back green for the doctrine. What failed review is
the perimeter: two stated facts that are the reverse of current GitHub
behaviour (G2), a CI design that its own repo's history already falsifies
(G1), and an entry syntax that breaks on the estate's own ssh-keygen (G3).
Every blocking item is a text edit today because nothing is wired — which is
precisely the outcome the review-before-activation sequencing was for. Fix
G1–G3 before step 1 moves; fold G4–G10 in with them or as a named follow-up
slice.

---

## Disposition — 2026-07-12, coordinating session

All ten findings addressed same day, one commit; **the decision stands, the
text now matches reality**:

- **G1 [fixed]** — SIGNING.md Verification section rewritten two-plane
  (machine-key commits via `git verify-commit`; GitHub server-side commits
  via the `gh api` verification check, spoof-closed), with the estate's own
  `a0ef731`/`4b2cf6f` named as the grounding specimens.
- **G2 [fixed]** — badge persistence corrected in SIGNING.md; ADR 0007
  corrected by **addendum** (no-edit rule); durable-plane argument restated
  on its real grounds; the pre-removal-attacker-badge consequence added to
  the exposure playbook.
- **G3 [fixed]** — quoted `valid-after="…"` timestamps mandated in the entry
  format with the parse-failure trap stated; known-signed-fixture selftest
  baked into the ladder's step-5 spec.
- **G4 [fixed]** — principal convention stated (committer email);
  membership-not-binding honesty stated; the CI principal-comparison
  decision explicitly deferred to step 5 (stated, not silent).
- **G5 [fixed]** — custody restated at true strength: vault holds the
  durable copy; every committing machine holds a working copy as a standing
  machine credential.
- **G6 [fixed]** — steps 4–5 now marked **stub** per RECORD, with the
  working-candidate mechanics named (boundary SHA in the child's `floor.yml`,
  `git rev-list <boundary>..HEAD`, `fetch-depth: 0`).
- **G7 [fixed]** — trust list resolved at the child's existing atelier pin,
  never floating `main`; the visible-pin-bump behaviour and the
  repo-write-compromise residual both stated.
- **G8 [fixed]** — ADR 0007 addendum rewords the GPG rejection to its true
  strength.
- **G9 [fixed]** — verified-committer-email condition added to ladder step 1.
- **G10 [fixed]** — bounding-is-retirement-hygiene-not-revocation stated in
  the exposure playbook, with the two-plane complement.

The doctrine remains **decided-but-dormant**; activation still gates on the
principal registering a key (his act). These fixes are doctrine text
implementing this verdict's own findings — judged covered by this review,
not fresh unreviewed doctrine.
