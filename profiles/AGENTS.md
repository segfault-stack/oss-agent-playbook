# Instructions for technology profiles

These instructions apply to `profiles/` in addition to the repository root `AGENTS.md`.

## Before adding or changing a profile

1. Read `profiles/README.md`, `profiles/_template/PROFILE.md`, and the core documents the
   profile specializes.
2. Confirm that the linked issue has maintainer-accepted scope. Its accepted cross-project
   problem and boundary are the maximum implementation scope.
3. Apply the decision gate below to every added or materially changed recommendation.
   Focused corrections need to recheck only the decisions they affect.

## Decision gate

A recommendation may remain in a profile only when all of these are true:

- it solves the accepted cross-project problem;
- it protects a declared property at the profile's owned boundary without repeating a
  core or adjacent decision;
- repository or task evidence provides an observable activation condition;
- an observable check can verify the outcome on the owned artifact or interface; and
- an official primary source supports every material factual technical claim on which the
  recommendation depends.

Remove a recommendation that fails the gate. Link to its owner when a reference is needed,
define only the required handoff when profiles compose, or return to the issue when the
accepted boundary cannot be satisfied without expanding it. General ecosystem relevance,
popularity, and the label `optional` do not make guidance admissible.

Split or defer concerns that can apply independently and are changed or verified against
different primary artifacts or authority boundaries. A shared ecosystem, vendor, or tool
does not establish common ownership.

## Candidate checks

- Satisfy the [profile contract](README.md#profile-contract) and keep `PROFILE.md` as the
  profile entry point.
- Verify supported-version claims, claim-to-source mappings, commands, material
  prerequisites, state changes, targeted cleanup, and concrete composition handoffs.
- Treat project examples as validation of applicability, composition, and verification,
  never as technical authority.
- Update `Last reviewed` only after substantive re-verification of affected technical
  claims, not after editorial changes.

New profiles must use `draft`. Do not promote one to `recommended` until a later focused
change documents what was checked across at least two representative repositories or
project types that differ in a way relevant to the protected properties.
