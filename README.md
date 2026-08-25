# OSS Agent Playbook

A technology-neutral maintenance playbook that helps AI agents and their human operators
audit, improve, and publish open-source repositories with explicit safety and authority
boundaries.

[![Documentation](https://github.com/segfault-stack/oss-agent-playbook/actions/workflows/docs.yml/badge.svg)](https://github.com/segfault-stack/oss-agent-playbook/actions/workflows/docs.yml)
[![Release](https://img.shields.io/github/v/release/segfault-stack/oss-agent-playbook?display_name=tag)](https://github.com/segfault-stack/oss-agent-playbook/releases/latest)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)

**Status:** pre-1.0 and evolving. Pin an exact release or commit when adopting it. Until `1.0.0`, minor releases may revise guidance or integration files incompatibly.

## Why this exists

Coding agents can edit a repository, but they do not automatically share a reliable standard for publication boundaries, honest positioning, secret handling, documentation, CI, releases, or external communication. Project instructions often become a mixture of local commands and copied generic advice that drifts across repositories.

This playbook separates those layers:

- a reusable core defines safety boundaries and repository-maintenance workflow;
- project context records facts, commands, risks, and deliberate decisions;
- an optional profile layer can specialize the core for ecosystems such as Python, Go, and Docker;
- thin adapters route Codex, Claude Code, and other file-aware agents without loading every document into every prompt.

The contract is intentionally simple: any agent that can read repository Markdown and project-local instructions can apply the playbook. It does not require a particular model, programming language, forge, CI provider, or deployment platform.

The core and profile framework are usable now. No technology profile has been published
yet. Under the profile lifecycle, each new profile starts as a draft and becomes
recommended only after representative project validation.

## What it covers

- read-only audit and risk-based prioritization;
- repository positioning, metadata, README authoring, and public surfaces;
- secrets, privacy, licensing, dependencies, and reproducibility;
- proportional quality gates, CI, branch policy, releases, and operations;
- authorization boundaries for pushes, releases, deployments, and external communication;
- adoption templates plus a schema and lifecycle for future technology profiles.

It does not create support promises, choose a license for a consumer project, or authorize an agent to mutate external state.

## Choose how to use it

| Need | Delivery mode | Main trade-off |
| --- | --- | --- |
| Inspect one repository once | Separate local checkout | No files are added to the target repository; the agent must be given both paths explicitly. |
| Keep the playbook available in every ordinary clone | Squashed Git subtree (recommended public default) | Updates produce normal reviewable commits, but upstream history is squashed. |
| Keep exact upstream provenance and a small consumer diff | Git submodule (fully supported) | Every local, cloud, and CI checkout must initialize submodules recursively. |

## Quick start

### One-off audit

From the directory containing the target repository, clone an immutable playbook release:

```bash
git clone \
  --branch v0.4.1 \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  oss-agent-playbook
```

Give the agent the local paths to both repositories and ask it to follow
`oss-agent-playbook/docs/agent-workflow.md`. Name both paths explicitly so the audit does
not depend on a later remote fetch. A read-only audit does not authorize the agent to edit,
push, publish, or change repository settings.

### Continuous use

Run the following from a clean target-repository worktree. Pin the playbook as a normal
dependency; do not track `main`.

#### Option A: squashed subtree

```bash
git subtree add \
  --prefix=.agent/oss-playbook \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  v0.4.1 \
  --squash
```

#### Option B: submodule

```bash
git submodule add \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  .agent/oss-playbook
git -C .agent/oss-playbook checkout v0.4.1
git add .gitmodules .agent/oss-playbook
```

Clone a submodule consumer recursively:

```bash
git clone --recurse-submodules <CONSUMER_REPOSITORY_URL>
```

Initialize or repair an existing checkout with:

```bash
git submodule update --init --recursive
```

#### Route agents to the pinned files

After either import, merge these templates into the target repository root:

- `.agent/oss-playbook/templates/AGENTS.consumer.md` as `AGENTS.md` for Codex and
  vendor-neutral routing;
- `.agent/oss-playbook/templates/CLAUDE.consumer.md` as `CLAUDE.md` for Claude Code;
- `.agent/oss-playbook/templates/PROJECT_AGENT_CONTEXT.md` as
  `PROJECT_AGENT_CONTEXT.md` for verified project facts and available and enabled profiles.

Copy them directly only when the corresponding root file does not exist. Otherwise merge
the routing into the established project instructions instead of overwriting them. Fill in
every required project-context field and record the immutable ref, resolved commit, and
delivery mode.

Verify the imported playbook itself:

```bash
test -f .agent/oss-playbook/README.md
python3 .agent/oss-playbook/scripts/check_docs.py
```

Success prints `Documentation checks passed` with the number of Markdown files in the
pinned release. Then give a file-aware agent a bounded first task, for example:

```text
Follow AGENTS.md and read PROJECT_AGENT_CONTEXT.md plus the pinned playbook.
Audit this repository without changing files. State the playbook ref, profiles actually
available in that pinned revision, and profiles enabled by the project. Do not describe an
absent profile as disabled or not enabled. Then report the three highest-priority findings
with evidence.
```

See the [adoption guide](ADOPTION.md) for updates, rollback, vendored snapshots, detailed
routing rules, and the complete adoption checklist.

## Playbook map

- [Adoption](ADOPTION.md) — subtree, submodule, snapshot, routing, updates, and rollback.
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

Issues and pull requests are welcome when they make agent decisions clearer or safer. Read
[Contributing](CONTRIBUTING.md), [Governance](GOVERNANCE.md), and
[AI-assisted contributions](AI_CONTRIBUTIONS.md) before proposing a change. Use
[Support](SUPPORT.md) to choose the right help channel and [Security](SECURITY.md) for
sensitive reports.

Run the dependency-free documentation check locally:

```bash
python3 scripts/check_docs.py
```

## Versioning

Tags use semantic versioning. Before `1.0.0`, minor releases may contain breaking policy or integration changes. After `1.0.0`, moving or renaming a routed document, changing adapter behavior, or materially reversing a normative default requires a major release. Consumer repositories should review updates like dependency changes rather than tracking a mutable branch.

## License

The playbook, templates, profiles, and supporting scripts are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). They may be copied, modified, and redistributed without attribution to the extent allowed by law.
