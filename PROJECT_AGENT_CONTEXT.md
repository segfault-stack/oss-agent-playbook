# Project Agent Context

This repository dogfoods the OSS Agent Playbook directly: its root documents are the source playbook, so no nested self-submodule or subtree is used.

## Required context

- Purpose and audience: reusable repository-maintenance guidance for AI agents and open-source maintainers.
- Wedge: agents can modify repositories but often lack consistent, safe publication and maintenance rules.
- General contract: any file-aware agent can apply the Markdown guidance together with project-local context.
- Primary supported behavior: read-only audits, in-scope repository improvements, verification, and explicit handoff within the documented authorization boundaries.
- Non-goals: enforcing runtime policy, replacing legal advice, prescribing a technology stack, or authorizing external actions.
- Sensitive and destructive boundaries: the repository contains no production data or credentials; GitHub settings, releases, pushes, messages, and third-party submissions remain external actions.

## Local verification

- Bootstrap: Python 3 with no third-party packages.
- Fast and full checks: `python3 scripts/check_docs.py`.
- CI: the `Documentation / Validate documentation` GitHub Actions job.
- Network-dependent review: verify external links and current platform-specific claims against primary official sources when they change.

## Publication and support

- Publication boundary: Markdown guidance, consumer templates, technology-profile scaffolding, and the documentation checker.
- Supported versions: the latest tagged pre-1.0 release; fixes land on `main` before the next release.
- Contributions and support: public GitHub issues and pull requests under `CONTRIBUTING.md` and `SUPPORT.md`.
- Sensitive reports: GitHub private vulnerability reporting as described in `SECURITY.md`.
- External actions requiring authorization: pushes, tags, releases, repository settings, announcements, and third-party submissions.

## Repository and release process

- Default branch: `main`.
- Merge policy: reviewed, focused changes with the documentation check passing.
- Version source: annotated Git tags using semantic versioning.
- Release workflow: verify local and remote commit identity, create an annotated tag, push branch and tag, then publish GitHub release notes.
- Artifacts: source tree and GitHub-generated source archives; no executable release artifacts.
- Rollback: revert the focused change; never move a published version tag silently.

## Enabled playbook profiles

- Enabled profiles: `none`

## Project-specific decisions

- Universal guidance lives in `docs/`; ecosystem guidance lives in `profiles/`.
- The repository uses its own root `AGENTS.md` and `CLAUDE.md` instead of importing itself recursively.
- Empty Discussions, Wiki, and Projects remain disabled until an owner and active use case exist.

## Playbook source

- Upstream: `https://github.com/segfault-stack/oss-agent-playbook`
- Import method: source repository; direct self-application
