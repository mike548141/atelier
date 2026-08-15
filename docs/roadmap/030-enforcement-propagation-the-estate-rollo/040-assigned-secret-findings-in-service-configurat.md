- [ ] **`assigned-secret` findings in service configuration.** Self-hosted
      service configs with credential-shaped assignments. Same tree; the usual
      right answer is a secret-store or env reference, plus rotation if the value
      was ever real.
