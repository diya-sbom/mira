BIL Enforcement Rule

BIL is not documentation.

BIL is generated automatically by execution.

Rules

1. Diya PASS
   → Intent Record appended

2. MIRA PASS
   → State Record appended

3. AFS PASS
   → Commit Record appended

4. Diya FAIL
   → no State Record
   → no Commit Record

5. MIRA FAIL
   → no Commit Record

6. Commit without BIL continuity
   → invalid

Continuity Chain

Intent Record
→ State Record
→ Commit Record

Missing links invalidate continuity.
