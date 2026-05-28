# Fail-Closed Proof

## Purpose

This document records the first protected-branch fail-closed proof for MIRA.

## Proof Scenario

A branch intentionally weakened adversarial corpus expectations.

Branch:

`fail-test`

Pull request:

`Intentional fail-closed enforcement test`

## Expected Behavior

The protected verification workflow must fail.

The pull request must not be mergeable into `main`.

## Observed Behavior

- GitHub Actions executed automatically
- MIRA output verification failed
- protected branch checks blocked progression
- merge into `main` was not allowed

## Protected Invariant

No invalid or weakened integrity expectation may advance into protected state.

## Meaning

MIRA is not only validating receipts.

MIRA is acting as a fail-closed dependency gate for protected state transitions.
