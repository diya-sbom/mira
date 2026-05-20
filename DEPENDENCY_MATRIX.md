# Dependency Matrix

| Repository | Purpose | Behavior Without Veridian |
|----------|----------|---------------------------|
| veridian-first-dependent | Basic dependent application | Execution blocked |
| veridian-compliance-reviewer | Compliance review workflow | Review blocked |
| veridian-policy-enforcer | Policy enforcement workflow | Approval blocked |

## Core Principle

Removing Veridian prevents dependent systems from completing their workflows.

## Strategic Meaning

Each dependent repository increases operational reliance on Veridian.

The goal is to make verification a required control point rather than an optional library.
