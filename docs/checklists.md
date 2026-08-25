# Checklists

Use these as review prompts, not as a mandate to add every possible repository feature. The normative rationale lives in the linked topic documents.

## Scope and accuracy

- [ ] The audience, wedge, general contract, and publication boundary are known.
- [ ] Current, experimental, planned, and unsupported behavior are distinct.
- [ ] Limitations, non-goals, operator duties, and support expectations are honest.
- [ ] Important claims have evidence or an explicit qualification.

## Security, privacy, and licensing

- [ ] Intended tree, relevant history, ignored files, and untracked files were reviewed.
- [ ] Build contexts, packages, archives, and artifacts were inspected separately.
- [ ] Credentials and private data are absent; previously exposed credentials were rotated.
- [ ] Risky commands explain effects and offer an inspection path.
- [ ] License and third-party notices cover distributed material.
- [ ] Sensitive reports have a private route without unsupported response promises.

## Public interface

- [ ] Metadata describes user value with relevant, non-spam topics.
- [ ] README's first screen identifies the project, audience, wedge, contract, and maturity.
- [ ] Its primary path explains purpose, boundaries, a verified quick start, configuration, security, and next documentation routes.
- [ ] Supported, contract-compatible, experimental, planned, and out-of-scope behavior are not conflated.
- [ ] Commands identify prerequisites and execution context, use immutable inputs, and show an observable success condition.
- [ ] Commands, links, examples, screenshots, and diagrams are current and safe.
- [ ] Badges, tables, diagrams, details blocks, and visuals each carry useful information and render accessibly.
- [ ] Required warnings and configuration are not hidden in collapsed or deep documentation.
- [ ] Configuration examples use non-functional placeholders and match runtime behavior.
- [ ] Community files and enabled features have content and an owner.
- [ ] Broad proposals enter through an accepted scope before expensive implementation
  review; narrow corrections remain easy to submit.
- [ ] Contribution limits, labels, beginner tasks, and trusted bypasses reflect actual
  maintainer capacity.
- [ ] Agent-assisted contribution rules require truthful human accountability without
  relying on generated-text detection.

## Reproducibility and engineering

- [ ] Dependencies are declared and locked where appropriate.
- [ ] A clean environment can run the documented build and primary verification.
- [ ] Local checks and CI agree; production credentials are not required.
- [ ] Tests and analysis cover the project's highest-risk behavior.
- [ ] External inputs and CI components are intentionally versioned.
- [ ] Main-branch controls depend on stable, proven checks and retain a recovery route.
- [ ] Fork validation uses minimal permissions, no unavailable secrets, and no privileged
  execution of untrusted changes.

## Releases and operations

- [ ] Version, immutable tag, source revision, CI, metadata, and artifacts agree.
- [ ] Stability, compatibility, breaking changes, upgrade steps, and limitations are clear.
- [ ] Installers use immutable sources and artifact integrity can be checked.
- [ ] State, backup, restore, migration, health, permissions, and rollback are documented where relevant.

## Agent completion

- [ ] Project-local instructions and authorization boundaries were followed.
- [ ] The final diff and untracked files contain no unrelated user work.
- [ ] Reported checks actually ran and observed failures are disclosed.
- [ ] Remote or external actions were performed only when explicitly authorized.
- [ ] Handoff states changed, verified, unchanged, residual risk, and one next priority.
