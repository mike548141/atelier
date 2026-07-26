# ccarchive — encryption at rest, secure by default

Status: **design pass, not built** (2026-07-26). Nothing below is implemented.
Direction set by Mike (2026-07-25): the archive is stored **encrypted by
default**, with an **explicit, loud opt-out** to store plaintext; `ccrepo` and
`cctranscript` gain **live-decrypt** the same way they already live-decompress.
This document designs within that direction — it does not relitigate it. One
question is left open as the principal's call (§5); everything else is either
decided on measured evidence or stubbed and named as a gap (§13).

Numbers below were measured on 2026-07-26 on the machine these instruments run
on (Node v24.18.0, macOS, LibreSSL 3.3.6, the live archive at ≈1,300 archived
files / ≈270 MB). Where a claim is not measured, it says so.

## 1. What changes, in one line

Each mirror goes from `<rel>.gz` to `<rel>.gz.age` — **compress, then encrypt to
a public recipient** — so the daily background writer never touches a secret,
while the three readers unwrap the file key with an identity that lives in the
person-level credential home and never in this repo.

## 2. Why this is not redundant with ADP

The 2026-07-23 ruling treated the encryption concern as answered by iCloud's
Advanced Data Protection end-to-end layer. That ruling was correct about the
carrier it was scoped to, and this raises the bar rather than overturning it:

| | ADP (account setting) | Tool-native encryption (construction) |
|---|---|---|
| Protects | the iCloud copy in transit + at rest on Apple's servers | the bytes themselves, on every carrier |
| Local disk copy | ❌ plaintext `.gz` on the Mac | ✅ ciphertext |
| Time Machine / a disk clone / a cloud backup of the home dir | ❌ | ✅ |
| The deferred NAS second leg | ❌ (out of ADP's scope entirely) | ✅ |
| A second sync channel, ever | ❌ per-carrier | ✅ carrier-agnostic |
| File names, sizes, mtimes on the carrier | ✅ covered by ADP | ❌ deliberately left in clear (§6) |
| Holds by | configuration — a toggle, with product-defined exclusions | construction — the file cannot be read without the key |

The two are **complementary, and each covers the other's residual.** ADP covers
the archive's structural metadata, which per-file encryption deliberately leaves
readable; tool-native encryption covers every carrier ADP does not. The
person-context portability design already made the general form of this argument
against depending on an account setting: a design that inherits its
confidentiality from a toggle "holds T2 by configuration, not by construction".

**The honest limit.** Claude Code owns `~/.claude/projects/` and writes it in
plaintext. ccarchive cannot change that. So this protects **copies of the
record, not its origin** — an attacker with the live machine has the plaintext
source regardless. What it buys is that every *derived* copy — the one that
syncs, the one that gets backed up, the one that lands on a NAS — is
confidential without depending on where it went.

## 3. What the measurements say

The roadmap's framing was that the overhead is key-*access*, not decrypt CPU.
Measured, that holds, and it is stronger than expected in one direction and
weaker in another.

| Measurement | Result | Bearing |
|---|---|---|
| AES-256-GCM, in-process (`node:crypto`) | 323 MB/s | encrypt CPU is a rounding error |
| ChaCha20-Poly1305, in-process | 291 MB/s | age's payload cipher, same order |
| gzip of realistic JSONL | 114 MB/s | the archive **already** pays 3× this per byte |
| encrypt-after-gzip, 15.8 MB of JSONL | +2.7% on the gzip already run | write-path cost is noise |
| decrypt (3.37 ms) vs gunzip (58.4 ms), same payload | **6%** of the decompression already on the read path | read-path cost is noise |
| `age -d` CLI, per file, 50 runs | **20.7 ms** | ✋ per-file process spawn is the real cost |
| the same decrypt in-process in Node | **0.50 ms** | 41× cheaper, no spawn |
| `security find-generic-password`, unlocked login keychain | 40–50 ms per call | key access is one-off per process, not per file |
| age file header, one X25519 recipient | 248 bytes/file (≈320 KB across the archive) | storage overhead is negligible |
| `openssl enc -aes-256-gcm` on LibreSSL 3.3.6 | **exits 1, no usable ciphertext** | see §5 option D |

**The finding that matters most**: at ≈1,300 files, a per-file subprocess costs
≈27 seconds on any operation that reads the whole archive, against ≈0.6 seconds
in-process. `ccrepo --from-archive` and `cctranscript --list` both sweep every
file. The crypto is free; **the process boundary is not**.

**The second finding**: the key-access cost lands once per process (40–50 ms to
fetch a key from an already-unlocked login keychain), and — see §4 — the write
path can be built to need no secret at all. So encrypted-by-default is
realistic, and the opt-out is a backstop rather than the expected path, exactly
as the roadmap anticipated.

## 4. Key management — the crux

### 4a. The move that makes it work: asymmetric, so the writer holds no secret

ccarchive runs daily under launchd. Its own source already records why the
signing key is a 0600 file rather than a keychain item: it "runs from a
launchd/cron context where Keychain access prompts or fails". Any design that
makes the *write* path unlock a secret inherits that problem.

**Encrypting to a public recipient dissolves it.** With X25519 recipients (age's
model), the write path needs only the recipient's public half, which is not a
secret and can sit in ccarchive's own config, in the archive root, and in this
repo's documentation if it were useful. The daily background job therefore:

- needs no unlock, prompts nothing, and cannot fail on a locked keychain;
- **cannot read the archive it writes** — a compromise of the scheduled context
  yields an append-only writer, not a reader. That is a security gain over a
  symmetric design, not merely a convenience.

Decryption is the interactive path — a human running `cctranscript`, `ccrepo
--from-archive`, or `ccarchive --restore` — where a login keychain is already
unlocked and a 40 ms fetch, memoised per process, is invisible.

### 4b. Where the identity lives

| Artefact | Home | Never |
|---|---|---|
| Recipient (public) | ccarchive config + a plaintext `RECIPIENTS` file in the archive root | — (it is not a secret) |
| Identity (private) | the person-level credential home — a 0600 age identity file beside the existing signing key, or a keychain item | **atelier**, the archive volume, any repo, any synced tree |
| Identity backup | the person-level credential home per the person-context design's **D5** ruling | any machine the archive can reach |

This is SECRETS.md's right-plane rule applied unchanged: the value lives in
exactly one place, everything else holds a reference. It also sits squarely in
SECRETS.md's **named honest boundary** — the store's own master key is
re-mintable for *exposure* but not for *loss*, and is "kept survivable by
copies, not by minting". Person-level credentials are explicitly outside the
cheap-burn doctrine's scope, which is precisely where this key belongs.

**Recommended default: a 0600 identity file**, matching the existing signing-key
precedent, with the keychain as an option once §13's headless-unlock question is
measured. The counter-argument — "a private key in plaintext on disk defeats
encryption at rest" — does not bite here, because the same disk holds the
plaintext live logs anyway (§2's honest limit). The identity's job is to keep
the *travelling copies* unreadable, and it never travels with them.

### 4c. Key loss is total data loss — say it plainly

Without an identity, `ccarchive --restore` cannot run and the archive is ≈270 MB
of noise. There is no recovery path, by construction: that is what encryption
means. The controls, all of which must exist before encrypted-by-default is
switched on:

1. **Multiple recipients.** age encrypts to N recipients natively. Encrypt to a
   per-machine identity *plus* a break-glass identity held offline in the
   person-level credential home. Losing one machine then costs nothing.
2. **The backup is a named obligation, not a nicety** (SECRETS.md), landing in
   the D5 home already ruled for the capsule's key.
3. **Rehearse the restore**, per DATA-PROTECTION's a-backup-isn't-a-backup-
   until-a-restore-is-verified. A restore drill using *only* the break-glass
   identity is a DONE condition (§12), not a follow-up.

**Adding a recipient later is not free.** age wraps a per-file key in each
file's header, so adding a recipient is *in principle* a header-only rewrite —
but the `age` CLI exposes no rewrap command, so in practice it is a full
decrypt-and-re-encrypt of ≈1,300 files, on the same cost profile as §11's
migration. ⚠️ This is asserted from the age v1 format's shape, **not measured** —
verify before relying on it. The practical consequence is decided regardless:
**choose the recipient set before the first encrypted run**, because widening it
afterwards costs a full pass.

### 4d. Solve-once: what is shared with the person-context capsule, and what is not

The capsule design (rulings D1–D5, 2026-07-23) wants an age capsule with
per-machine identities for crown-jewels. Concretely:

**Shared — solve once:**
- The **format and the primitive**: age v1, X25519 recipients, per-machine
  identities, `age-keygen` provisioning.
- The **key-custody pattern**: identities in the person home, backup in the D5
  credential home, per-device identities so device revocation is clean.
- The **doctrine seam**: whatever SECRETS.md/STORAGE.md gains about "encrypt at
  rest, keys in the person home" is written once and cited by both.
- The **recipient set itself**, plausibly — one per-machine identity per device
  can serve both the capsule and the archive. ⚠️ *Not recommended without a
  ruling*: a shared identity couples the blast radius of two stores with very
  different threat profiles, against SECRETS.md's revocation-independence
  reasoning. Cheaper and cleaner: separate identities, same provisioning
  mechanism.

**Not shared:**
- **Carrier.** The capsule rides the private estate repo (D1); the archive rides
  iCloud Drive and, later, a NAS.
- **Granularity and access shape.** The capsule is a few files decrypted on
  demand into a session; the archive is thousands of files swept whole (§6).
- **The unlock model.** The capsule is decrypt-on-need with a human present; the
  archive's *writer* is a background job that must never prompt (§4a).
- **Code.** The capsule's tooling is a separate build. What crosses is the
  format decision, the key custody, and the doctrine — not an implementation.

## 5. 🎯 The one decision for Mike — where the crypto comes from

⚠️ **This is the principal's call, not the agent's.** AEAD encryption needs a
crypto implementation, and the house's zero-dependency tool pattern is exactly
the constraint that *deferred* release-artifact signing and SBOM (ADR 0007). The
same tension applies here, but the evidence changes the shape of it.

**The framing in the roadmap needs one correction.** It says AEAD "isn't in
Python stdlib" — true, and it governs anything in `tools/`. But ccarchive,
ccrepo and cctranscript are **Node**, and `node:crypto` on Node 24 ships every
primitive age v1 needs, verified on 2026-07-26: `aes-256-gcm`,
`chacha20-poly1305`, X25519 key agreement, `hkdfSync`, `scryptSync`, HMAC. So
"zero-dep" and "real AEAD" are **not** in conflict for the instruments layer.
What is genuinely in tension is zero-dep versus **using a standard, audited file
format** rather than a house-defined one.

| | **A · shell out to `age`** | **B · `node:crypto`, house format** | **C · `node:crypto`, age-format compatible** | **C′ · write with `age`, read in Node** ⭐ | **D · `openssl enc`** |
|---|---|---|---|---|---|
| Dependency | `age` binary, on every reading machine | none | none | `age` binary, on the *archiving* machine only | none (system openssl) |
| Full-archive read cost | ≈27 s (spawn-bound) | ≈0.6 s | ≈0.6 s | ≈0.6 s | n/a |
| Readable without our tools | ✅ any `age`/`rage` build, forever | ❌ our code is the only reader | ✅ | ✅ | ✅ |
| Crypto we author | none | container framing over an OpenSSL primitive | full age header + STREAM, both directions | **decrypt only** | none |
| Failure mode of a bug | — | silent weak ciphertext possible | silent weak ciphertext possible | **fails closed** — we never mint ciphertext | — |
| Reuses the capsule's block | ✅ | ❌ | ✅ | ✅ | ❌ |

**Option D is dead on measurement, not reputation.** macOS's bundled LibreSSL
3.3.6 `openssl enc -aes-256-gcm` exits 1 with `bad decrypt` and produces no
usable ciphertext — `enc` does not support AEAD modes. It is not a footgun to be
handled carefully; it is not a capability. Discard it.

### Recommendation — C′, and it is a recommendation, not a decision

**Write with the `age` binary; decrypt in-process with `node:crypto`.** The
asymmetry of the two paths is what makes this fit:

- The **write path is incremental** — a normal run archives a handful of new
  files, so 20.7 ms × a few is invisible, and the dependency lands only on the
  machine that archives.
- The **read path is a full sweep** — every file, interactively — so it must be
  in-process, and 0.5 ms per file makes live-decrypt genuinely as cheap as the
  live-decompress it sits beside.
- **We never author ciphertext.** `age` produces every file; our code only
  consumes. A bug in a decrypt implementation fails loudly and locally; a bug in
  an *encrypt* implementation can silently produce weak files you discover years
  later. For an archive whose whole purpose is to outlive things, that asymmetry
  is worth more than the effort it saves.
- **The format outlives the tool.** An archive readable only by ccarchive is a
  format risk on a decades horizon. `age -d` works today, on any machine, with
  no code of ours. Ship a plaintext `HOW-TO-DECRYPT.txt` in the archive root
  stating the format and the exact command — it costs nothing and it is the
  difference between an archive and a hostage.

**Honest cost of C′:** the decrypt half is still most of the format work —
header parse, X25519 unwrap, HKDF, ChaCha20-Poly1305 STREAM chunking. It saves
*risk*, not effort. Mitigation, and a DONE condition: a **differential test**
that encrypts with the real `age` binary and decrypts with ours, over fixtures
including multi-chunk payloads (>64 KiB), multiple recipients, and a
deliberately corrupted tag.

> 🎯 **Mike's call, in plain language.** Every option here gives you a
> confidential archive. The choice is what you are willing to owe:
>
> - **A** — simplest to build, and your archive is readable by a standard tool
>   forever. Cost: `age` must be installed on any machine that reads the
>   archive, and whole-archive reads get ~27 seconds slower.
> - **B** — nothing to install, fastest to build, fastest to run. Cost: your
>   archive is readable *only* by our code, forever. If the code is lost or
>   broken, the archive is gone.
> - **C** — nothing to install, fast, standard format. Cost: we write the
>   trickiest code in the estate, in both directions.
> - **C′ (recommended)** — `age` needed only on the machine that archives; the
>   reading tools stay dependency-free and fast; the format stays standard; and
>   we only ever write the half where mistakes fail loudly instead of quietly.
>   Cost: still a few hundred lines of format code, and a real test suite
>   proving it against the real `age`.

## 6. Granularity — per-file, decisively

Per-file, not a whole-archive container. The measurement is not close, and the
reasons are structural rather than performance:

- **Incremental sync.** ccarchive exists to be cheap to run often and light on a
  synced dest. A container re-writes ≈270 MB on every run, so iCloud re-uploads
  the entire history daily. Per-file keeps "only new/updated files upload".
- **Eviction.** The dataless/`--materialise` design is per-file by nature (§9).
  A container is one enormous file: it is evicted whole and faulted back whole.
- **cctranscript resolves one session.** A container forces reading everything
  to read anything.
- **Append-only by contract.** ccarchive never deletes. A container is rewritten
  in place on every run, which is deletion wearing a hat.
- **Blast radius.** One corrupted archived file loses one session. One corrupted
  container loses the archive.

**The residual, stated rather than hidden: per-file encryption leaves the
archive's *structure* in the clear.** File names carry session UUIDs and
Claude Code's dash-mangled project directory names — which are absolute repo
paths — and sizes and mtimes are visible, as is `manifest.json`, which lists
every path. An observer with the archive volume learns *which* repos were worked
on, *when*, and *how much*, without reading a word. This is inherent: the
incremental design needs readable paths to know what to sync.

Not fixed here, and named as a limit: obfuscating names would break restore
mapping, the incremental freshness check, and human navigability of the archive
all at once. On the iCloud leg this residual is covered by ADP (§2). On a future
NAS leg it would not be — flag it when that leg is designed.

## 7. The read path — `readLogText` and the three tools

`readLogText` is the shared choke-point that already hides gzip from every
parser, in identical duplicated form in both `ccrepo` and `cctranscript`:

```js
const raw = fs.readFileSync(file);
return file.endsWith('.gz') ? zlib.gunzipSync(raw).toString('utf8') : raw.toString('utf8');
```

Decrypt slots in exactly there — `.age` → decrypt → gunzip → text — with the key
resolved **lazily and memoised per process**, so a run that touches no archived
file never asks for a key, and a run that touches 1,300 asks once.

But the seam is wider than that one function, and a build must touch all of it:

| Site | Today | Under encryption |
|---|---|---|
| `ccrepo` / `cctranscript` `readLogText` | gunzip on `.gz` | + decrypt on `.age` |
| `ccrepo` `LOG_EXT` | `'.jsonl.gz'` when `--from-archive` | suffix becomes posture-dependent |
| `cctranscript` `cwdFromLog` | 64 KB partial read (plain) / full gunzip (`.gz`) | full decrypt — no regression on the archive path, which already gunzips whole |
| `ccarchive` `sha256Gz` | gunzip, hash raw bytes | needs the key, or a keyless ciphertext hash (§8) |
| `ccarchive` `listArchivedRels` | strips a 3-char `.gz` | must be suffix-aware |
| `ccarchive` restore / audit | `rel + '.gz'` constructed in several places | one `archiveSuffix()` helper, used everywhere |

⚠️ **A structural sub-decision falls out of this.** `readLogText`, `isDataless`,
`statFlags` and `defaultArchiveDest` are already *triplicated* across the three
instruments by deliberate copy ("ported from ccarchive"). Duplicating **crypto**
is a different proposition from duplicating a five-line gunzip: three copies of
a decrypt path is three places for a security-relevant divergence, and it
contradicts the solve-once principle at exactly the point where it matters most.

Recommendation: introduce a single shared module for the crypto seam only —
`instruments/lib/`, required by all three — and leave the existing duplication
alone rather than opening a refactor. This is a change to the instruments
layer's shape that ADR 0006 does not currently contemplate, so it is named here
as a design consequence rather than assumed. The alternative (triplicate the
decrypt code) is cheaper today and is the current house pattern; it is not
recommended.

## 8. Integrity and confidentiality both stay

Encryption does **not** subsume the sha256 manifest or its HMAC signature, and
the reason is sharper than "integrity ≠ confidentiality":

- **AEAD protects a file's bytes.** A tampered ciphertext fails its auth tag on
  decrypt. That is per-file, under the key.
- **The signed manifest protects the *inventory*.** AEAD says nothing about a
  file being **deleted**, or **replaced with an older but perfectly valid
  encrypted file** of the same name, or a session being **added**. Only a signed
  list of what should be there catches those — and rollback of an archive is a
  realistic attack on a synced volume in a way that byte-flipping is not.

So: keep both. Concretely, the manifest gains one field so `--verify` does not
regress:

| Field | Meaning | Checkable without the key? |
|---|---|---|
| `sha256` (existing) | hash of the **raw source bytes** — the end-to-end anchor | ❌ needs decrypt |
| `cipherSha256` (new) | hash of the stored `.gz.age` bytes as written | ✅ |

`--verify` then runs **keyless by default** on `cipherSha256` — same cost
profile as today, no key prompt, safe under launchd — and gains a
`--verify --deep` that decrypts and checks `sha256` end-to-end. Without this,
encryption would silently turn every verify into a key-requiring operation,
which would break the scheduled integrity check.

The signing key and the encryption identity stay **separate credentials**: one
guards tamper-evidence, the other confidentiality; they have different exposure
consequences and different rotation stories (the signing key is freely
re-mintable, the identity is not — SECRETS.md's honest boundary). Merging them
would drag the cheaply-rollable one down to the irreplaceable one's care level.

## 9. Dataless / iCloud eviction — unchanged, if the suffix is threaded through

The eviction machinery is `stat`-based and metadata-only: it never reads a file,
so it is untouched by encryption. Two conditions preserve that:

- Every eviction check must run against the **encrypted path** (`<rel>.gz.age`),
  which follows from the `archiveSuffix()` helper in §7. A check against a
  now-nonexistent `.gz` would silently return "not evicted" and defeat the skip.
- **A normal archive run must still never read the archive.** It stats for
  mtime and writes; that must not change. In particular the manifest-backfill
  path, which reads an archived file when its source is already gone, will now
  need the key — so it must remain dataless-skipping *and* must degrade
  gracefully when no identity is present, rather than failing the run.

`manifest.json`, `manifest.json.sig` and the new `RECIPIENTS` /
`HOW-TO-DECRYPT.txt` stay **plaintext**: they are the inventory and the recovery
instructions, and encrypting them would make the archive undiagnosable exactly
when you most need to diagnose it. The manifest's metadata exposure is the §6
residual, already named.

## 10. The opt-out, and how it stays loud

Secure-by-default means the opt-out must be an act, not a setting that drifts:

- **A flag, never an environment variable.** `--plaintext` on the command line.
  An env var is a quiet default — precisely what "loud opt-out" excludes.
- **The archive records its own posture.** The manifest carries
  `policy: { encryption: "age" | "none", recipients: [...] }`. A run whose flags
  contradict the recorded posture **refuses** rather than silently producing a
  half-encrypted archive.
- **Every plaintext run says so**, on stderr, every time — not once at setup.
- **`--verify` reports the posture** in its first line, beside the signature
  verdict, so the trust anchor and the confidentiality posture are read
  together.
- **Mixed archives are legal but visible.** A migration (§11) can be partial;
  `--verify` states the split (`N encrypted, M plaintext`) rather than rounding
  it to green.

## 11. Migration — explicit, expensive, reversible

An existing plaintext archive does not become encrypted by accident.

**The operation**: for each `<rel>.gz`, encrypt to `<rel>.gz.age`, record
`cipherSha256`, then **delete the `.gz`**. That deletion is the point — an
archive with the plaintext still beside it is not encrypted — and it is a
deliberate, stated exception to ccarchive's append-only contract. So migration
is its own explicit command (`--encrypt-archive`), never a side effect of a
normal run, and it should be resumable file-by-file so an interruption leaves a
legal mixed archive rather than a corrupt one.

**The costs, all real:**
- **Every file changes**, so the synced dest re-uploads the whole archive
  (≈270 MB) once.
- **Every evicted file faults back**, which is exactly the bulk-download the
  rest of the design works to avoid. Migration must therefore require
  `--materialise` explicitly and state the download it is about to cause.
- Wall-clock is spawn-bound under options A/C′: ≈1,300 × ~21 ms ≈ 27 s of
  encryption, dwarfed by the sync.

**Reversible?** Yes, with the identity: `--decrypt-archive` reverses it exactly,
because the raw-bytes `sha256` in the manifest proves the round trip. Without
the identity, no — which is §4c restated.

**The default recommendation is not to migrate immediately.** Turn encryption on
for new files, verify the readers work over a mixed archive, run the restore
drill, and only then migrate history. The mixed state is designed to be legal
precisely so this sequencing is available.

## 12. What DONE looks like — testable conditions

Not a checklist of intentions; each line is a test that can fail.

1. **No plaintext at rest.** A fixture archive run with no opt-out contains zero
   occurrences of a known fixture string anywhere under the dest tree.
2. **The scheduled writer needs no secret.** A full archive run completes with
   the identity file unreadable and no keychain access — only the recipient
   present. Failing this fails the whole design.
3. **Reader parity.** `ccrepo --from-archive` and `cctranscript` over an
   encrypted fixture archive produce **byte-identical** output to the same
   commands over the plaintext equivalent.
4. **Verify stays keyless.** `--verify` runs green with no identity present,
   detects a single flipped ciphertext byte, and `--verify --deep` additionally
   detects a file whose plaintext was altered and re-encrypted by a valid
   recipient.
5. **Rollback is caught.** Replacing an archived file with an older, validly
   encrypted version of itself fails `--verify` on the manifest, proving §8's
   claim that AEAD does not subsume the signed inventory.
6. **Dataless behaviour unchanged.** With `CCARCHIVE_SIMULATE_DATALESS` set, the
   evicted/skipped counts over an encrypted archive equal those over a plaintext
   one.
7. **Differential crypto test** (if C/C′): every fixture encrypted by the real
   `age` binary decrypts identically in-process, including a >64 KiB multi-chunk
   payload, a multi-recipient file, and a corrupted-tag file that must fail.
8. **Migration round-trips.** `--encrypt-archive` then `--decrypt-archive`
   reproduces the manifest's `sha256` for every entry.
9. **The restore drill passes** on a scratch dest using **only** the break-glass
   identity — the backup proven by restore, not by existing.
10. **The opt-out is loud.** A `--plaintext` run emits the warning on stderr; a
    run whose flags contradict the recorded posture exits non-zero.
11. Man page gains an ENCRYPTION section; `--help` states the posture; the floor
    is green.

## 13. Stubbed — evidence not available at design time

Named rather than guessed, per the house's stub-don't-fabricate rule:

- **Whether a keychain read from a launchd context prompts or fails.** Asserted
  in ccarchive's own source comments; **not re-measured here**, because testing
  it means writing an item into the operator's personal keychain. §4a's design
  makes the answer non-blocking (the writer needs no secret either way), but it
  must be measured before any keychain-held identity is chosen over a file.
- **Whether age's per-file header can be rewrapped to add a recipient without
  re-encrypting the payload** (§4c) — argued from the format's shape, not
  tested. Affects only how expensive it is to widen the recipient set later.
- **Compression-ratio effects.** Encrypt-after-compress is assumed correct
  (ciphertext does not compress); the ordering is not in doubt, but the archive-
  wide size delta was not measured beyond the per-file 248-byte header.
- **NAS-leg behaviour.** The second leg is deferred and undesigned; §6's
  metadata residual is uncovered there and is flagged, not solved.
- **Multi-machine reality.** Whether more than one machine reads this archive
  today is unknown to this pass, and it changes the recipient-set sizing in §4c.
  Ask before choosing the recipient set — it is the one decision that is
  expensive to revise.
- **Doctrine placement.** Whether this warrants an ADR, a SECRETS.md clause, or
  a STORAGE.md storage class is deliberately not decided here. Review is
  WARRANTED when this moves from design to build, per the roadmap.

## 14. Deferred / out of scope

Encrypting the live `~/.claude/projects/` store (Claude Code owns it) · name
obfuscation and metadata hiding (§6) · encrypting `manifest.json` (§9) ·
passphrase-only identities without a key file · hardware-backed identities ·
key rotation on a cadence for the encryption identity (SECRETS.md's cadence
argument applies to cheaply-rollable secrets; this one is not) · any change to
the manifest signing key's own design.
