- [x] **ccarchive: sign the manifest (tamper-evidence)** — built 2026-07-22
  (wave-4 queue run, `2a85839`): detached HMAC-SHA256 sidecar
  (`manifest.json.sig`), key off-archive at `~/.claude` (file over Keychain
  — cron/launchd reads it promptless; the key guards tamper-evidence, not
  confidentiality), `--rekey` rotation re-signs the current manifest
  (SECRETS replaceability — a roll loses nothing), five verify states each
  honest and non-zero (tampered / key-mismatch / unsigned-legacy-migrates /
  no-key-unverifiable; verify never mints). The closed caveat proven live:
  forged `.gz` + recomputed manifest hash → signature MISMATCH, exit 1.
  Non-protections stated in the man page (key theft forges; no
  anti-rollback; evidence, not prevention). Suite 70→84 ccarchive / 132
  instruments-wide, re-proven post-merge. The two contestable defaults stay
  a live 🎯 on the ROADMAP.
