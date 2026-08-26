# Project Agent Context

Keep this file factual and concise. Link to authoritative project files instead of duplicating information that already exists. Remove optional sections that do not apply and never fill unknowns with guesses.

## Required context

- Purpose and audience, or authoritative reference:
- Wedge — the concrete problem that makes the project useful:
- General contract — the interface or behavior that defines broader applicability:
- Primary supported behavior, or authoritative reference:
- Important non-goals and limitations, or authoritative reference:
- Sensitive data, privileged operations, and destructive boundaries:

## Local verification

- Bootstrap:
- Fast checks:
- Full checks:
- Build/package:
- Integration or smoke tests:
- Documentation checks:
- Security checks:

State prerequisites and identify checks that require network access, credentials, paid services, special hardware, production-like data, or destructive fixtures.

## Publication and support

- Publication boundary:
- Supported versions or authoritative reference:
- Contribution and support policy:
- Contribution intake and maintainer-review policy:
- Agent-assisted public contribution policy:
- Private security reporting route:
- External actions that require maintainer authorization:

## Repository and release process

- Default branch and merge policy:
- Generated files and sensitive or persistent paths:
- Version source:
- Release workflow or authoritative reference:
- Artifact integrity policy:
- Deployment boundary and rollback path:

## Playbook profiles

Record availability and selection separately. For `Available profiles`, list profile IDs
that actually exist under `.agent/oss-playbook/profiles/` in the pinned revision; ignore
`_template/`. For `Enabled profiles`, list only available profiles selected by this
project. Use `none` when a list is empty. Inventory directory names without loading every
profile body.

Call an absent profile unavailable, never disabled or not enabled. Report an enabled but
unavailable profile as a context error. Enabling permits task-activated profile guidance;
it does not authorize changes or external actions.

- Available profiles: `none`
- Enabled profiles: `none`

## Project-specific decisions

Record deliberate deviations from playbook defaults, accepted risks, owners, and review dates. Do not restate universal rules or place credentials and private user data here.

## Pinned playbook

- Upstream: `https://github.com/segfault-stack/oss-agent-playbook`
- Immutable ref:
- Resolved commit:
- Import method: `git subtree --squash`, `git submodule`, or `vendored snapshot`
- Imported or last reviewed:
