- ⏳ **Rule-4 review queued (tier: Fable; pass type: code cold pass) — the
  floor-render batch (third render state + the PS5 pathscan promotion +
  the C1F3 floorfleet strip).** *Delta:* `tools/floor.py` +
  `tools/floorfleet.py` + their two test files (suite 1178 → 1200) +
  `.github/workflows/ci.yml` (bespoke pathscan step retired) +
  `.atelier-floor.json` (the pathscan scope) + the reworded 2026-07-19
  line in `docs/decisions/README.md` + the CHANGELOG entry (landed
  2026-08-06, this commit). *Intent record:* the 2026-08-04 rulings on
  the render item and D1/PS5 (Track C / Track D) + the C1F3 finding, all
  harvested with their items to [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
  § *The floor-render batch*.
  - [ ] 🎯 **Cycle CLOSED 2026-08-09 (0 MAJOR); FR1–FR6 + FR2a await Mike's
        ruling round.** The rule-4 Fable cold pass (taker: a Mike-spawned
        session, claimed 0815 UTC) returned PASS-WITH-FINDINGS — 0 MAJOR /
        3 MODERATE / 1 minor / 2 note; all re-runs reproduced (1178 → 1200
        exact at the landing commits, HEAD suites green, all three render
        states provoked live, the retired pathscan CI step's cover
        byte-equivalent under the registry), and all three rulings verified
        applied as ruled →
        [`reviews/2026-08-09-0823-floor-render-batch-cold.md`](../../reviews/2026-08-09-0823-floor-render-batch-cold.md).
        The MODERATEs: FR1 — pathscan absent from the `tools/README.md`
        catalogue though it now reaches every child (genuinely new); FR2 —
        the child default scope aims pathscan at the records tree the
        batch's own rationale calls un-gateable (reconcile reframed it as
        counsel against a ruled choice, severity unchanged; FR2a notes the
        record rules that default in nine words while carrying full grounds
        for the opposite scoping on atelier itself); FR3 — the C0-only strip
        passes C1 controls (U+009B probed) and bidi overrides, narrower than
        the spoofing threat the ruling answers (genuinely new).
      `[~]` **RULED 2026-08-23** — the live ruling round ran by structured
      asks; dispositions in the verdict file (§ *Rulings — 2026-08-23*).
      FR2: records-excluding default for children. Application in flight
      on wt: ruling-round-0823.
