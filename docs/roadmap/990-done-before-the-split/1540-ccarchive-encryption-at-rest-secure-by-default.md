- [x] **ccarchive: encryption at rest, secure-by-default (Mike, 2026-07-25)** —
  **design pass DELIVERED 2026-07-26** (`d913698`, merged `7701a62`) →
  [`instruments/ccarchive.encryption.design.md`](../../../instruments/ccarchive.encryption.design.md).
  Still not a build; what remains is 🎯 **one decision, Mike's**. **Two stubs
  below were answered by measurement, and both answers moved the question:**
  - ⚠️ **The zero-dep tension does not exist as framed.** AEAD isn't in
    *Python's* stdlib, which governs `tools/` — but ccarchive, ccrepo and
    cctranscript are **Node**, and `node:crypto` ships `aes-256-gcm`,
    `chacha20-poly1305`, X25519, `hkdfSync` and `scryptSync` (verified directly
    at merge, Node 24). Zero-dep and real AEAD are compatible here. The
    `openssl` fallback is **dead on capability, not reputation**: macOS
    LibreSSL 3.3.6 `openssl enc -aes-256-gcm` exits 1 with no usable ciphertext
    (reproduced at merge) — `enc` has no AEAD modes.
  - **The overhead is the process boundary, not key access.** Measured over the
    live archive: `age -d` ≈20.7 ms per file (≈27 s for a full sweep) against
    ≈0.50 ms in-process (≈0.6 s); keychain fetch 40–50 ms, once per process.
    Encryption adds ~2.7% to the gzip already run, and decrypt is ~6% of the
    gunzip already on the read path. **So encrypted-by-default is comfortably
    realistic and the plaintext opt-out really is a backstop, not the expected
    path** — which is what the direction assumed but could not yet show.
  - **The spine of the design:** compress then encrypt to a **public** X25519
    recipient (`<rel>.gz.age`), so the scheduled writer holds no secret, never
    prompts, and *cannot read what it writes*. Decrypt is the interactive path,
    where the keychain is already unlocked. Per-file, not a container — a
    container breaks incremental sync, iCloud eviction and append-only at once.
    Signing **stays**: AEAD protects a file's bytes, the signed manifest
    protects the *inventory* against deletion and rollback. `--verify` stays
    **keyless** via a new `cipherSha256`, so the scheduled integrity check
    doesn't silently become key-requiring.
  - 🎯 **The decision, in plain language: where does the crypto come from?**
    Every option gives a confidential archive; what differs is what you owe.
    **A** shell out to `age` everywhere — simplest, standard format forever, but
    `age` must be installed on every *reading* machine and full reads get ~27 s
    slower. **B** house format in `node:crypto` — nothing to install, fastest,
    but the archive is readable *only* by our code, a real durability risk for
    something meant to outlive its tools. **C** implement the age format both
    directions — no install, fast, standard, but we write the trickiest code in
    the estate twice over. **C′ (counselled)** write with the `age` binary,
    decrypt in-process — `age` needed only on the archiving machine, readers
    stay dependency-free and fast, format stays standard, and **we only author
    the half where a bug fails loudly**; an encrypt bug can mint weak files you
    discover years later. `age` is already installed on this machine. Counsel,
    not a decision.
  - **Named honestly rather than buried:** per-file encryption leaves session
    UUIDs, dash-mangled repo paths, file sizes and the whole `manifest.json` in
    the clear. ADP covers that residual on the iCloud leg; a NAS leg would not.
  - **Key loss is total data loss**, said plainly — an archive you cannot
    decrypt is not an archive.
  - Review **WARRANTED when it moves from design to build** — unchanged. The
    design pass authored no doctrine, so nothing is queued yet.
  Original brief kept below for the reasoning. **Direction (Mike):** ccarchive stores the archive
  **encrypted by default** (secure-by-default → confidential at rest), with an
  **explicit opt-out param** to store plaintext if the overheads bite (a loud
  opt-out, never a silent default); and **ccrepo + cctranscript gain live-decrypt**
  the same way they already live-decompress. **This raises the bar the 2026-07-23
  archive decision set:** that ruled the encryption concern "answered" by the
  iCloud **ADP E2E** layer — but ADP only protects the *iCloud copy*; tool-native
  encryption makes the bytes confidential *everywhere* (local disk, any copy, in
  transit, the deferred NAS leg). Complementary to ADP, not redundant.
  **Open design questions (stub — do not pre-decide):**
  - **Key management is the crux, not the crypto.** Where the key lives + how the
    consumers get it at read time. Keys → the person-level credential home
    (keychain / an age identity), **never atelier** (SECRETS right-plane).
  - **The overhead is key-*access*, not decrypt CPU** (symmetric decrypt is
    microseconds; the cost is unlocking the key per op). Lever: session-cached
    unlock / already-unlocked login keychain — then live-decrypt reuses the exact
    live-decompress read seam. So encrypted-default is realistic; the opt-out is a
    backstop, not the expected path.
  - 🔗 **Solve-once reuse:** the person-context portability design already wants an
    **age capsule with per-machine keys** for crown-jewels (rulings D1–D5). Same
    building block — "encrypt-at-rest, keys in the person-home". Solve the key
    infrastructure ONCE and reuse for both (a live instance of the *solve once,
    reuse the building block* capture above).
  - ⚠️ **Zero-dep tension (the one likely Mike-decision at the design pass):**
    AEAD encryption isn't in Python stdlib — it needs a crypto dep (`age` is the
    clean choice, already contemplated for the capsule) or shelling to `openssl`
    (footguns — not AEAD by default). This is the same tool-install-floor tension
    that *deferred* release-artifact signing/SBOM; weigh secure-by-default against
    the zero-dep house-tool pattern.
  - **Orthogonal to the existing manifest signing** (integrity ≠ confidentiality):
    keep both — sign for tamper-evidence, encrypt for confidentiality.
  Review WARRANTED when it moves from design to build (touches SECRETS.md +
  the instruments crypto surface).
