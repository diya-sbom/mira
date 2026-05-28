# Contribution Flow

## Purpose

This repository uses protected-branch enforcement.

Changes to `main` must go through pull requests.

## Required Flow

1. Create a branch
2. Commit changes on the branch
3. Push branch to GitHub
4. Open pull request into `main`
5. Wait for required checks
6. Wait for required review
7. Merge only after protections pass

## Required Checks

The protected branch requires:

- MIRA Output Verification
- adversarial verifier tests
- adversarial corpus execution

## Blocked Behavior

Direct pushes to `main` are not allowed.

Failed verification must block merge.

Missing review must block merge.

## Invariant

No unchecked change may enter protected `main`.
