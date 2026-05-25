# Verification Flow

Developer
→ Creates state change
→ Generates canonical receipt
→ Receipt verified by `verify_output.py`
→ GitHub Actions runs `verify-output`
→ Protected branch checks verification result
→ Merge allowed or blocked

External systems may independently verify blessed receipts without importing the MIRA runtime.
