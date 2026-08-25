# Audit and Priorities

Begin with a read-only audit. If the request is only to review or recommend, do not modify files, remote settings, issues, releases, or external services.

## Establish context

Identify:

- the problem, audience, wedge, and general contract;
- verified use cases and only-theoretical ones;
- non-goals, limitations, and likely alternatives;
- the intended publication and support boundary;
- project-specific risk: privileges, sensitive data, network exposure, persistence, and update path.

Record uncertainty instead of converting assumptions into claims.

## Inspect the technical reality

Review the structure, primary flows, configuration, installation, build, tests, and automation. Check dependency and lock state, generated artifacts, containers or packages, tags and releases, and agreement between documentation and behavior.

Also inspect the current branch, remotes, worktree changes, ignored and untracked files, and—when relevant—repository rules and merge settings. Never overwrite unrelated work.

## Inspect the public interface

Review:

- name, description, topics, homepage, and owner profile;
- README, license, contribution and security guidance;
- issue forms, pull/merge request template, support policy, and code of conduct;
- changelog, release notes, assets, and social preview when present;
- enabled discussions, wiki, projects, and other public surfaces;
- stale names, links, screenshots, examples, or promises.

## Inspect trust and safety

Look specifically for:

- credentials, personal data, internal identifiers, and sensitive logs;
- dangerous, destructive, or non-working instructions;
- mutable installation sources presented as stable;
- unsupported security or stability claims;
- severe exploitable vulnerabilities;
- missing or incompatible licensing and third-party notices;
- release artifacts that cannot be traced to their source revision;
- hidden manual steps and machine-specific dependencies.

## Prioritize findings

### P0 — safety, legality, and truth

Address secret exposure, data-loss paths, critical exploitable vulnerabilities, dangerous installation, license blockers, artifact/source mismatch, and materially false claims. Rotate exposed credentials; deleting them from the latest tree is insufficient.

### P1 — comprehension and first success

Clarify positioning, README entry path, a verified quick start, a minimal example, configuration, supported versus experimental behavior, limitations, non-goals, and common diagnostics.

### P2 — repeatability and maintenance

Add proportional tests and analysis, dependency controls, contributor and security paths, stable CI, branch protection, and versioned reproducible releases.

### P3 — discovery and growth

Improve topics, demos, owner profile, catalogs, community materials, and external promotion only after the important P0–P2 gaps are understood.

Within a priority, rank work by impact, likelihood, and reversibility. Do not hide unresolved higher-priority debt behind cosmetic work.
