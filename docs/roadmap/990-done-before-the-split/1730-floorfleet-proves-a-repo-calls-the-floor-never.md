- [x] **`floorfleet` proves a repo CALLS the floor, never that its floor is
  GREEN.** (B2.) `--status` now reads each repo's latest floor run and reports
  it as a separate claim from wiring — `passing`, `failing`, `behind`,
  `actions-off`, `no-runs`, `unregistered`, `running`, `no-result`, `unknown`.
  Only `passing` is green; `unknown` is a red, so a board that could not read
  an answer never renders one.
