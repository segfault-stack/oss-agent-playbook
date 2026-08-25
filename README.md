# OSS Agent Playbook

Reusable, technology-neutral instructions for AI agents that publish and maintain trustworthy open-source repositories.

[![Documentation](https://github.com/segfault-stack/oss-agent-playbook/actions/workflows/docs.yml/badge.svg)](https://github.com/segfault-stack/oss-agent-playbook/actions/workflows/docs.yml)
[![Release](https://img.shields.io/github/v/release/segfault-stack/oss-agent-playbook)](https://github.com/segfault-stack/oss-agent-playbook/releases)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)

**Status:** pre-1.0 and evolving. Pin an exact release or commit when adopting it. Until `1.0.0`, minor releases may revise guidance or integration files incompatibly.

## Why this exists

Coding agents can edit a repository, but they do not automatically share a reliable standard for publication boundaries, honest positioning, secret handling, documentation, CI, releases, or external communication. Project instructions often become a mixture of local commands and copied generic advice that drifts across repositories.

This playbook separates those layers:

- a reusable core defines safety boundaries and repository-maintenance workflow;
- project context records facts, commands, risks, and deliberate decisions;
- optional technology profiles specialize the core for ecosystems such as Python, Go, and Docker;
- thin adapters route Codex, Claude Code, and other file-aware agents without loading every document into every prompt.

The contract is intentionally simple: any agent that can read repository Markdown and project-local instructions can apply the playbook. It does not require a particular model, programming language, forge, CI provider, or deployment platform.

## What it covers

- read-only audit and risk-based prioritization;
- repository positioning, metadata, README authoring, and public surfaces;
- secrets, privacy, licensing, dependencies, and reproducibility;
- proportional quality gates, CI, branch policy, releases, and operations;
- authorization boundaries for pushes, releases, deployments, and external communication;
- adoption templates and composable technology profiles.

It does not create support promises, choose a license for a consumer project, or authorize an agent to mutate external state.

## Quick start

### One-off audit

Give an agent local access to this repository and the target repository, then ask it to follow [`docs/agent-workflow.md`](docs/agent-workflow.md). Name both paths explicitly so the audit does not depend on a remote fetch.

### Continuous use

Import an immutable release into the target repository. A squashed subtree is the easiest public default:

```bash
git subtree add \
  --prefix=.agent/oss-playbook \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  v0.2.0 \
  --squash
```

Then merge the provided adapters into the project root:

- [`templates/AGENTS.consumer.md`](templates/AGENTS.consumer.md) for Codex and vendor-neutral routing;
- [`templates/CLAUDE.consumer.md`](templates/CLAUDE.consumer.md) for Claude Code;
- [`templates/PROJECT_AGENT_CONTEXT.md`](templates/PROJECT_AGENT_CONTEXT.md) for project facts and enabled profiles.

Git submodule is also fully supported for maintainers who initialize it in every local, cloud, and CI checkout. See the [adoption guide](ADOPTION.md) for add, update, verification, and rollback procedures for both modes.

## Playbook map

- [Principles](docs/principles.md) — scope, positioning, evidence, and restraint.
- [Audit and priorities](docs/audit-and-priorities.md) — how to inspect a repository and order work.
- [Public interface](docs/public-interface.md) — metadata, documentation, and community surfaces.
- [README authoring](docs/readme-authoring.md) — reader journey, quick start, and claims.
- [README presentation](docs/readme-presentation.md) — prose, tables, visuals, badges, and rendering.
- [Security and reproducibility](docs/security-and-reproducibility.md) — secrets, privacy, dependencies, builds, and supply chain.
- [Engineering and releases](docs/engineering-and-releases.md) — quality gates, CI, branches, operations, and releases.
- [Agent workflow](docs/agent-workflow.md) — authorization, execution, verification, and handoff.
- [Checklists](docs/checklists.md) — publication and maintenance review.
- [Technology profiles](profiles/README.md) — optional stack-specific overlays.

The playbook separates hard safety and authorization boundaries from recommended defaults and optional maturity practices. Project-specific decisions may specialize defaults, but they must not silently conceal security, privacy, legal, or data-loss risk.

## Contributing and support

Issues and pull requests are welcome when they make agent decisions clearer or safer. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change. Use [SUPPORT.md](SUPPORT.md) to choose the right help channel and [SECURITY.md](SECURITY.md) for sensitive reports.

Run the dependency-free documentation check locally:

```bash
python3 scripts/check_docs.py
```

## Versioning

Tags use semantic versioning. Before `1.0.0`, minor releases may contain breaking policy or integration changes. After `1.0.0`, moving or renaming a routed document, changing adapter behavior, or materially reversing a normative default requires a major release. Consumer repositories should review updates like dependency changes rather than tracking a mutable branch.

## License

The playbook, templates, profiles, and supporting scripts are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). They may be copied, modified, and redistributed without attribution to the extent allowed by law.
