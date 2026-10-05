- [~] 🔎 **`--list --from-archive` still fully gunzips every local mirror for
  its first-prompt column** (claimed 2026-10-05-1128, wt: atelier-qr-210-180) (found 2026-10-03 by the worker that fixed `050`;
  measured, not built)

  With `050`'s two causes fixed, the listing still takes about 7 s. A CPU
  profile puts zlib at about 4 s, UTF-8 slicing at about 1.7 s, and
  `firstUserPromptText` at about 1.6 s. That function decompresses each
  locally present mirror **in full** to find the first user prompt for the
  listing's column. The prefix inflate `050` added (`gunzipHead`) is the
  obvious tool. A first prompt can sit beyond any fixed prefix, though, so
  a prefix read needs a bound and a whole-file fallback, the way the cwd
  sniff has one. `--search` on the archive plane pays the same full-gunzip
  cost per mirror, and that has not been measured.
