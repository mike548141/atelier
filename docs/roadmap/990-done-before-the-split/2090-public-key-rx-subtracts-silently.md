- [x] **`PUBLIC_KEY_RX` subtracts silently** (found at the E6b build,
      reported not fixed there): the public-key line suppression predates
      the GUARDS allowance model's counted-suppression rule — lines it
      writes off appear in no tally, the one subtraction in the scanner a
      reader cannot see growing. Small alignment; rides the next
      secretscan touch.
