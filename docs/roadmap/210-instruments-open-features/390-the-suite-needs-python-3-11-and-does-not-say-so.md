- [x] 🔎 **The Python test suite needs 3.11 or later and does not say so.**
      Routed from the `160/970` cold pass (PQ2) by queue run 722ac2e2 on
      2026-11-09. `tools/README.md` and the test modules do not state the
      floor, so a run on an older interpreter fails in ways that read as
      defects. **Shape:** one README line plus a `sys.version_info` guard
      that says what is wrong.
      - [x] ✅ **Closed 2026-11-09.** `tools/test_floor.py`, `tools/test_floorfleet.py` and
            `tools/test_precommit.py` raise a plain `ImportError` naming the 3.11 floor
            and the interpreter found, before any 3.10-only syntax or call is reached. A
            raise, not a skip: a skipped module would read as green on 3.9. The README
            line already existed (`tools/README.md`, "tests need 3.11 or later").
            Checked under the system 3.9: each module errors with that message.
