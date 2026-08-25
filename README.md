# OSS Agent Playbook

Technology-neutral guidance for agents that publish, improve, and maintain open-source repositories.

The playbook optimizes for accuracy, safety, reproducibility, and low maintenance overhead. It is not a completeness checklist: a small honest repository is preferable to one filled with processes nobody owns.

**Status:** pre-1.0 and evolving. Pin an exact commit when adopting it. Until a `1.0.0` release, any update may revise guidance or integration files incompatibly.

## Contents

- [Principles](docs/principles.md) — scope, positioning, evidence, and restraint.
- [Audit and priorities](docs/audit-and-priorities.md) — how to inspect a repository and order work.
- [Public interface](docs/public-interface.md) — metadata, README, documentation, and community surfaces.
- [README authoring](docs/readme-authoring.md) — reader journey, content structure, quick start, and claims.
- [README presentation](docs/readme-presentation.md) — prose, tables, visuals, badges, and rendering.
- [Security and reproducibility](docs/security-and-reproducibility.md) — secrets, privacy, dependencies, builds, and supply chain.
- [Engineering and releases](docs/engineering-and-releases.md) — quality gates, CI, branches, operations, and releases.
- [Agent workflow](docs/agent-workflow.md) — authorization boundaries, execution sequence, verification, and handoff.
- [Checklists](docs/checklists.md) — publication and maintenance review.
- [Adoption guide](ADOPTION.md) — how to attach this playbook to a concrete project.
- [Technology profiles](profiles/README.md) — optional stack-specific overlays loaded only when relevant.

The playbook separates hard safety and authorization boundaries from recommended defaults and optional maturity practices. Project-specific decisions may specialize defaults, but they must not silently conceal security, privacy, legal, or data-loss risk.

## Quick use

For a one-off review, give an agent this repository plus the target repository and ask it to follow [the agent workflow](docs/agent-workflow.md).

For continuous use, import a pinned revision into the target project and add a short root `AGENTS.md` that routes agents to it. Keep project-specific facts and enabled technology profiles in a local `PROJECT_AGENT_CONTEXT.md`.

Two Git delivery modes are supported:

- a squashed subtree is the easiest public default because ordinary clones and archives remain self-contained;
- a submodule provides cleaner separation and an exact gitlink for maintainers willing to initialize it in every local, cloud, and CI checkout.

See [ADOPTION.md](ADOPTION.md) for both workflows and [`templates/`](templates/) for Codex, Claude Code, and project-context adapters.

## Scope

This playbook covers public repository preparation and maintenance. It does not prescribe a language, framework, hosting provider, branching convention, license, or community model. It also does not authorize publication, remote configuration changes, releases, or external communication on behalf of a maintainer.

## Contributing

Issues and pull requests are welcome when they make agent decisions clearer or safer. Universal guidance belongs in `docs/`; technology-specific guidance belongs in `profiles/`. Follow [AGENTS.md](AGENTS.md) when editing this repository.

Run the dependency-free documentation check before proposing a change:

```bash
python3 scripts/check_docs.py
```

## Versioning

Tags use semantic versioning. Before `1.0.0`, minor releases may contain breaking policy or integration changes. After `1.0.0`, a breaking change includes moving or renaming a routed document, changing integration-file behavior, or materially reversing a normative default. Consumer repositories should review playbook updates like dependency changes rather than tracking a mutable branch.

## License

The playbook, templates, and profiles are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). They may be copied, modified, and redistributed without attribution to the extent allowed by law.
