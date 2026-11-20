- [x] **4. Multi-key sort within a level, plus `--top`** (`ee36a91`). Built on
  Mike's **option A**: the comma stays positional per `-g` level, and multi-key
  chains additively on **`+`** (`--sort 'cost+name, time'`). The glyph was picked
  against the punctuation already in the flag — `,` means "next level" and `:`
  means direction, so `+` was the one gap. `--sort cost` still broadcasts to
  every level (a one-element chain), and an unknown key inside a chain still
  exits 2. Nothing written under v2 changed meaning.
  - **`--top <n>` truncates per level, not leaves-only** — `-g repo,model --top 5`
    keeps the top five repos *and* the top five models within each, shared by
    `treeRows`/`leafRows`/`--json`/`--csv` through one helper so every output
    shape truncates identically.
  - **TOTAL is preserved, and this was proven rather than argued.** `groupTree`
    computes every node's aggregate over the *entire* event set before any sort
    or truncation, so `--top` only slices which computed rows get listed. A
    first live check appeared to differ by two messages — that was the verifying
    session appending to its own log between runs, not truncation. Re-run over a
    **frozen** date range, the TOTAL row is byte-identical with and without
    `--top`. A footnote on the output says the total is untruncated.
