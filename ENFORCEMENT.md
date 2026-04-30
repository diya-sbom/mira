# Enforcement Rule (Phase 8)

All writes to protected_output must go through MIRA verification.

Allowed path:
guarded_write.py → MIRA → write

Not allowed:
any direct write script without verification

Future:
this will be enforced at system level (CI / runtime / adapters)
