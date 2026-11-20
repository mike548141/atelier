- [x] **Repo-specific scoping preserved** — the networking child's leakscan
      tuning (shareable subtree only, IP/MAC rules off, because those shapes are
      *content* there) moved into config verbatim. Its device-config capture
      dirs went to `.secretscanignore` per Mike's ruling: scoping, not secrets.
