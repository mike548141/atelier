- [x] **floorfleet's remaining child-authored text surfaces.** The C1F3
      strip covered the `.atelier-floor.json` seam as ruled; `classify`/
      `_live_yaml` still read child `floor.yml` text and the caller `ref`
      reaches the board detail line unstripped. A separate, narrower
      question — same class, smaller surface; rides the next floorfleet
      touch.

      ✅ **FIXED 2026-09-18** (`1c4a5e2`, merged from
      `floorfleet-pathscan-0918`): the `ref` a child's `floor.yml` pins is
      passed through `floor.strip_controls` at extraction, and `_live_yaml()`
      strips per line (stripping the whole document first erased the newlines
      it splits on — the module's own selftest caught that draft). Tests carry
      an escape-sequence payload through `classify()` and end-to-end through
      `render()`.
