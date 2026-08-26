# Project Agent Context

This repository dogfoods the OSS Agent Playbook directly: its root documents are the
source playbook, so no nested self-submodule or subtree is used. Its instruction, context,
memory, and decision files demonstrate this repository's maintenance model; consumer
requirements are defined separately by `ADOPTION.md` and `templates/`.

## Required context

- Purpose and audience: develop reusable guidance for agents and maintainers preparing
  existing software repositories for public open-source release and subsequent maintenance.
- Wedge: heterogeneous repositories have different facts, commands, risks, and technology
  boundaries, but recurring OSS-maintenance concerns otherwise get re-explained or copied
  differently for every repository.
- General contract: any file-aware agent can apply the technology-neutral Markdown core
  together with verified project-local context and any enabled, task-activated profiles.
- Status: pre-1.0 experiment and reference implementation; it does not claim broad adoption
  or universal-standard status.
- Primary supported behavior: read-only audit, authorized repository improvement,
  observable verification, truthful handoff, and preparation for explicitly authorized
  public or release operations. A run need not perform every behavior.
- Repeated-use model: a repository may use the playbook once or keep a pinned revision
  available for later passes as the repository and guidance change. No scheduled execution,
  automatic updating, or continuous enforcement is implemented.
- Scope boundary: the core owns technology-neutral OSS maintenance. Optional profiles own
  bounded technology-specific artifacts or interfaces and must define activation,
  outcomes, and verification; absent profiles provide no stack-specific depth.
- Acceptance boundary: automated checks provide evidence, not maintainer approval. Agents
  do not gain acceptance authority from capability, task authorization, or passing checks;
  substantive merge, release, and acceptance into maintained public state remain
  human-owned.
- Non-goals: enforcing runtime policy, replacing legal advice, prescribing a technology
  stack, or authorizing external actions.
- Sensitive and destructive boundaries: the repository contains no production data or credentials; GitHub settings, releases, pushes, messages, and third-party submissions remain external actions.

## Local verification

- Bootstrap: Python 3 with no third-party packages.
- Fast and full checks: `python3 scripts/check_docs.py`.
- CI: the `Documentation / Validate documentation` GitHub Actions job.
- Network-dependent review: verify external links and current platform-specific claims against primary official sources when they change.

## Publication and support

- Publication boundary: Markdown guidance, consumer templates, technology profiles and their scaffolding, and the documentation checker.
- Supported versions: the latest tagged pre-1.0 release; fixes land on `main` before the next release.
- Contributions and support: public GitHub issues and pull requests under `CONTRIBUTING.md` and `SUPPORT.md`.
- Sensitive reports: GitHub private vulnerability reporting as described in `SECURITY.md`.
- External actions requiring authorization: pushes, tags, releases, repository settings, announcements, and third-party submissions.

## Repository and release process

- Default branch: `main`.
- Merge policy: reviewed, focused changes with the documentation check passing.
- External contribution intake: one open non-draft pull request per user without write
  access; broad work and profiles require maintainer-accepted issue scope.
- Maintainer review: one approval for ordinary changes; when at least two active
  maintainers exist, consequential changes require affirmative acceptance from two
  maintainers, including one non-author approving review, and no unresolved objection.
- Sole-maintainer path: substantive self-authored work uses a public pull request and an
  explicit administrator bypass; direct pushes are limited to narrow corrections and
  urgent recovery.
- Version source: annotated Git tags using semantic versioning.
- Release workflow: choose the version, update versioned examples, search for stale release
  pins, verify local and remote commit identity, create an annotated tag, push branch and
  tag, then publish GitHub release notes.
- Artifacts: source tree and GitHub-generated source archives; no executable release artifacts.
- Rollback: revert the focused change; never move a published version tag silently.

## Playbook profiles

- Available profiles: `docker-container-images`
- Enabled profiles: `none`

## Project-specific decisions

- Universal guidance lives in `docs/`; artifact- and interface-specific technology guidance lives in `profiles/`.
- The repository uses its own root `AGENTS.md` and `CLAUDE.md` instead of importing itself recursively.
- Empty Discussions, Wiki, and Projects remain disabled until an owner and active use case exist.
- Shared maintainer memory is public, Git-tracked, and advisory. `MAINTAINER_MEMORY.md` indexes accepted lessons; `docs/decisions/` owns consequential decision history.
- Agents may prepare changes, but a human maintainer reads consequential instruction, memory, and decision changes before acceptance. The current maintainer group has one person; any future group is expected to remain small and accountable.
- Agent-assisted contributions do not require disclosure, but a human must read and
  understand the final diff and submission before an agent publishes it.
- A formal Code of Conduct and DCO sign-offs remain disabled until real moderation or
  provenance needs justify their operational cost.

## Playbook source

- Upstream: `https://github.com/segfault-stack/oss-agent-playbook`
- Import method: source repository; direct self-application
