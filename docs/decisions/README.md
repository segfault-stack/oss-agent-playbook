# Maintainer Decision Log

This directory records consequential choices about maintaining and evolving the OSS Agent
Playbook. Decisions explain why the current structure exists; they do not replace current
instructions or project facts.

## When a decision is required

Create a decision when a change materially affects:

- agent authority or human approval boundaries;
- security, privacy, licensing, or destructive-action policy;
- playbook adoption, compatibility, or distribution defaults;
- source-of-truth ownership or repository-wide architecture;
- maintainer memory, instruction evolution, or enforcement strategy.

Routine corrections, narrow clarifications, dependency refreshes, and ordinary content
improvements do not need a decision record.

## File and status rules

- Name files `NNNN-short-kebab-case-title.md` using the next unused four-digit number.
- Use one H1 and the metadata fields `Status`, `Date`, and `Supersedes`.
- Allowed statuses are `Proposed`, `Accepted`, `Superseded`, and `Rejected`.
- Use an ISO `YYYY-MM-DD` date.
- Use `None` when the decision supersedes nothing; otherwise link every replaced decision.
- Keep accepted records substantively immutable. Fixing a typo or broken link is allowed,
  but reversing the decision requires a new record that supersedes it.
- Link affected current documentation instead of copying whole policies into the record.
- Never include credentials, private deliberations, personal data, or sensitive reports.

## Lifecycle

1. Record the context and the concrete decision.
2. Describe consequences, boundaries, and alternatives considered.
3. Obtain human maintainer review for consequential changes.
4. Update current instructions, context, memory indexes, and checks in the same focused
   change when the decision is accepted.
5. When reversing it later, add a new decision and mark the old record `Superseded` with a
   link to the replacement.

## Index

- [0001 — Use Git-native maintainer memory with human-owned acceptance](0001-git-native-maintainer-memory.md) — Accepted
- [0002 — Use human-gated contribution governance](0002-human-gated-contribution-governance.md) — Accepted
