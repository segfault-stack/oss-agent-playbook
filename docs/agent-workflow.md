# Agent Workflow

## Authorization boundary

Start read-only and separate findings into observed, completed, recommended, blocked, and permission-dependent work.

- A request for an audit, explanation, or draft does not authorize changes.
- A request to improve a repository authorizes in-scope local edits and proportional local verification, but not unrelated work.
- Do not push, change remote settings, publish packages or releases, send messages, create external submissions, or modify deployments unless the request explicitly covers that action.
- Do not create images, logos, or social previews unless requested.
- Resolve the exact target before a destructive or difficult-to-reverse action. Prefer recoverable operations.

Project-local instructions may further restrict actions. Preserve user changes and stop when an unresolved choice would materially change scope, public promises, licensing, or external state.

## Agent-assisted public contributions

When acting as a public contributor, follow the target project's intake and AI-assistance
policy. Do not autonomously publish issues, pull requests, comments, or review replies when
the project requires human review. Never claim that a human read the final work, that a
check ran, or that a source supports a statement unless that fact was verified.

A strong default for agent-oriented projects is to allow agent-produced work while
requiring a human operator to read and understand the exact final diff and submission
before publication. The agent may then perform authorized mechanical publication. Judge
the contribution by observable scope, evidence, correctness, and maintainability rather
than attempting to infer whether its prose was generated.

An accepted issue authorizes work within its stated scope, not merge. Do not open parallel
changes, fabricate activity, or use alternate identities to evade an intake limit or
maintainer decision.

## Execution sequence

Adapt this order to the request and risk:

1. Read project-local agent instructions and context. Verify the pinned playbook revision,
   inventory profiles actually present in it, and distinguish available profiles from
   profiles the project enabled. Never describe a profile absent from the pinned revision
   as disabled, not enabled, or intentionally omitted.
2. Audit purpose, technical reality, public surface, and worktree state using [Audit and priorities](audit-and-priorities.md).
3. Resolve P0 safety, privacy, licensing, and truthfulness issues as defined there.
4. Establish the audience, limitations, non-goals, and the [wedge and general contract](principles.md#pair-a-concrete-entry-point-with-a-general-contract).
5. Repair metadata, README entry path, and verified quick start.
6. Align configuration, documentation, and troubleshooting with behavior.
7. Add proportional community, security, test, and CI controls.
8. Address dependency and supply-chain risks.
9. Establish safe branch and release mechanics when authorized.
10. Consider discoverability and external materials only after core trust gaps.
11. Review the repository as an unfamiliar reader in a clean environment.
12. Verify the exact changes and hand off residual risks.

Do not execute every step mechanically. Skip surfaces the project does not need and state important out-of-scope items.

When README work is a primary deliverable, follow the focused authoring sequence in [README authoring](readme-authoring.md) and include rendered-page checks from [README presentation](readme-presentation.md).

## Verification

Use the strongest practical evidence for changed behavior:

- inspect the final diff and untracked files;
- run documented formatting, analysis, tests, build, and packaging checks that cover the change;
- validate example configuration and generated or locked files;
- test the primary documented flow from clean state when feasible;
- check links and hosting-platform rendering for documentation changes;
- verify README headings, anchors, tables, details blocks, badges, images, and narrow-layout readability when they changed;
- inspect packages, images, and release archives independently of the source tree;
- recheck claims, secrets, private data, license notices, and mutable download sources.

Never report a check as passed unless it ran and its result was observed. Distinguish “not run,” “not available,” and “failed.”

## Handoff

Lead with the resulting user value, then report:

- **Changed:** files, behavior, settings, commits, releases, or external actions actually completed.
- **Verified:** exact checks and observed results.
- **Not changed:** important items deliberately outside scope.
- **Residual risks:** unresolved alerts, assumptions, manual steps, or unverified compatibility.
- **Next priority:** one highest-value follow-up and why it ranks first.

Do not imply that local changes were pushed, that remote checks passed, or that a release exists unless verified.

## Completion test

For a repository intended to distribute usable software, an unfamiliar reader should be able to:

1. find and understand the real problem and project boundaries;
2. select a suitable supported version;
3. install or build it from immutable, documented inputs;
4. reproduce the primary scenario;
5. assess maturity, operational duties, and known risks;
6. report ordinary and sensitive problems through appropriate paths;
7. trace distributed artifacts to their source;
8. understand whether and how contributions are accepted.

Apply only the items relevant to the project's publication boundary. Record concrete follow-up work for an unmet item instead of compensating with polish.
