# Dronesim Agent Instructions

## Universal Policies

Before starting any task, read and follow:

`.agent/universal-policies/AGENTS.md`

Follow all references and required instructions in that file.

If a required policy cannot be read, stop and report the failure.

## Project Policies

Project-specific rules in this file supplement or override universal policies according to the universal override rules.

## Documentation Reconciliation

After each developer-accepted implementation step:

1. Inspect the accepted changes.
2. Compare the implementation against `docs/architecture.md`.
3. Identify completed, outdated, or unresolved items in `NEXT.md`.
4. Determine whether any accepted ADRs are affected.
5. Propose necessary documentation updates for developer review.

Do not modify documentation without an explicit grant.

Documentation updates must be independently reviewable.
Report the resulting changes and stop for review.