# Fail-Closed Proof

## Purpose

This proof demonstrates that an invalid canonical receipt cannot pass the protected verification path.

## Test Performed

A temporary branch was created:

`fail-closed-proof`

The canonical receipt hash was intentionally changed to:

`broken-hash`

## Result

Running the verifier produced:

`HASH_MISMATCH`

GitHub Actions then failed the required check:

`MIRA Output Verification / verify-output`

## Enforcement Result

The protected branch could not proceed because the required verification check failed.

## Conclusion

Tampered receipt
→ verifier fails
→ CI fails
→ protected branch blocks merge

This proves fail-closed receipt verification.
