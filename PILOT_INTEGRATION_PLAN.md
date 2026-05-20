# Pilot Integration Plan

## Objective

Integrate Veridian into one real workflow so that execution and state persistence fail closed when verification does not pass.

## Candidate Pilot Workflows

- Compliance review
- Contract review
- Audit evidence verification
- Policy approval
- Agent memory control

## Integration Requirements

- Python 3
- Access to the Veridian API
- Canonical tests passing
- Stable verification contract (v1.0.0)

## Integration Steps

1. Install Veridian.
2. Configure the adapter.
3. Route actions and memory writes through Sentinel.
4. Verify decisions with MIRA and Diya.
5. Block execution if verification fails.
6. Confirm successful operation when verification passes.

## Success Criteria

- Removing Veridian causes the workflow to fail.
- Verification denial blocks execution.
- Accepted operations generate receipts.
- Canonical tests remain green.

## Expected Pilot Deliverables

- Integration code
- Execution logs
- Sample receipts
- PASS/FAIL examples
- Operational notes

## Business Outcome

Demonstrate that an independent workflow can depend on Veridian as a mandatory verification layer.

## Strategic Significance

This is the transition from internal demonstrations to genuine enterprise adoption.
