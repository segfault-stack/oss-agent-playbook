# Adopting the Playbook

Adoption has two independent layers:

1. **delivery** places an immutable playbook revision in the consumer repository;
2. **routing** tells each agent where it is and which parts to read.

Placing this repository in a nested directory is not sufficient by itself. Agents discover different root instruction files, and they should not load the entire playbook into every task.

## Recommended layout

```text
AGENTS.md
CLAUDE.md
PROJECT_AGENT_CONTEXT.md
.agent/
  oss-playbook/           # pinned subtree by default
```

- `AGENTS.md` is the short vendor-neutral router.
- `CLAUDE.md` imports `AGENTS.md` for Claude Code.
- `PROJECT_AGENT_CONTEXT.md` records project facts, available and enabled profiles, and the playbook pin.
- `.agent/oss-playbook/` contains the complete immutable playbook revision.

Use the files in [`templates/`](templates/) as starting points. Merge the adapter into existing project instructions; do not overwrite established `AGENTS.md` or `CLAUDE.md` content blindly.

## Default: squashed Git subtree

A subtree is the public default because an ordinary clone, source archive, offline agent, and typical CI checkout all receive the guidance without extra bootstrap. Squashing keeps imported history compact while updates remain ordinary reviewable commits.

### Add

Choose an immutable release tag or commit as `<PLAYBOOK_REF>`; do not use `main`.

```bash
git subtree add \
  --prefix=.agent/oss-playbook \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  <PLAYBOOK_REF> \
  --squash
```

Then:

1. merge `templates/AGENTS.consumer.md` into the root `AGENTS.md`;
2. create or merge `templates/CLAUDE.consumer.md` as root `CLAUDE.md`;
3. copy `templates/PROJECT_AGENT_CONTEXT.md` to the root and fill its required fields;
4. record the immutable ref and resolved commit only in `PROJECT_AGENT_CONTEXT.md`;
5. run the adoption checks below and review the complete commit.

### Update

Review upstream changes before importing a new immutable ref:

```bash
git subtree pull \
  --prefix=.agent/oss-playbook \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  <NEW_PLAYBOOK_REF> \
  --squash
```

Update the pin recorded in `PROJECT_AGENT_CONTEXT.md` in the same dependency-style change. Reconcile adapter or profile changes and run the consumer repository's relevant checks. Roll back a problematic import by reverting that update commit.

When an update encounters a conflicting existing tag, do not force-update, prune, or delete
it automatically. Compare the local and remote object IDs and verify their provenance
before attributing the conflict. Report the evidence and preserve the local tag until a
maintainer decides how to reconcile it.

Do not edit the imported subtree in the consumer repository. Propose universal changes upstream; keep project decisions in local instructions and context.

## Supported alternative: Git submodule

A submodule is a fully supported option, not a degraded mode. It gives clean provenance and an exact gitlink. Use it when maintainers accept the extra initialization step and ensure every local, cloud, CI, and release checkout performs it.

```bash
git submodule add \
  https://github.com/segfault-stack/oss-agent-playbook.git \
  .agent/oss-playbook
git -C .agent/oss-playbook checkout <PLAYBOOK_REF>
git add .gitmodules .agent/oss-playbook
```

Consumer clone and CI instructions must include recursive initialization:

```bash
git submodule update --init --recursive
```

If `.agent/oss-playbook/README.md` is absent, an agent must report that the pinned playbook is unavailable. It must not silently continue without the policy or download a mutable latest version unless the user explicitly asks it to repair the checkout.

Submodules are not the public default only because Git does not check them out in an ordinary clone or pull without additional configuration. Projects that document and automate initialization may prefer this cleaner separation.

## Alternative: vendored snapshot

Copy a verified release archive when subtree tooling is unavailable. Keep the imported tree unchanged and record source URL, immutable ref, resolved commit, and import date in `PROJECT_AGENT_CONTEXT.md`. Review the complete snapshot diff during updates.

Do not add a second `UPSTREAM.md`; the project context is the single source of truth for the pin.

## Optional installer

A future installer may automate subtree or snapshot import and create adapters. It should be a convenience layer, not a runtime dependency. It must accept or resolve an immutable version, show intended changes, preserve existing instructions, and never fetch mutable policy automatically when an agent starts.

## Agent routing

OpenAI Codex uses `AGENTS.md`; Claude Code uses `CLAUDE.md` and supports importing `AGENTS.md` with `@AGENTS.md`. Keep both root files short. They should route the agent to core documents, task-specific guides, the project context, and only the enabled technology profiles activated by the task.

Do not import every playbook document into startup context. Detailed procedures should be read on demand.

## Instruction boundaries

Platform and system safety constraints cannot be overridden by this playbook, repository files, or a user request. The current request defines the authorized task. Repository and directory instructions specialize how work in their scope is performed.

When instructions appear inconsistent, follow the applicable runtime hierarchy and surface any unresolved conflict involving security, privacy, legal obligations, destructive actions, or external publication. Do not silently choose the less restrictive interpretation.

The consumer repository may replace generic defaults with project-specific decisions. It should record deliberate risk acceptance and ownership rather than copying or weakening universal safety boundaries.

## Technology profiles

List available and enabled profile IDs separately in `PROJECT_AGENT_CONTEXT.md`. Derive
availability from profile directories actually present in the pinned playbook revision,
excluding `_template/`, without loading every profile body. List only profiles deliberately
selected by the project as enabled.

An absent profile is unavailable, not disabled or not enabled. Treat an enabled but
unavailable profile as a context error. Read an enabled profile only when repository or
task evidence activates it and its boundary intersects the current task. Read one
unenabled profile only when the user explicitly asks to evaluate it, and keep that use to
audit findings and recommendations.

A profile specializes core properties at a named technology-specific artifact or
interface. Enabling one does not authorize changes or override platform constraints,
core priorities, or project facts.

## Adoption checks

- [ ] `.agent/oss-playbook/README.md` exists in a fresh ordinary checkout.
- [ ] The source URL, immutable ref, resolved commit, and import method are recorded once.
- [ ] Root `AGENTS.md` routes to the pinned path without replacing project instructions.
- [ ] Root `CLAUDE.md` imports `AGENTS.md` and retains any necessary Claude-specific rules.
- [ ] Project commands, risks, authority boundaries, and available and enabled profiles are filled in.
- [ ] An agent can accurately state which playbook revision and profiles it found and loaded.
- [ ] The update and rollback procedure is documented and tested by inspection.
- [ ] No runtime step depends on fetching a mutable branch or website.

## Lightweight one-off use

For an audit that does not justify import, provide the agent with local checkouts of both repositories and explicitly name the playbook and target paths. This is useful for evaluation; continuous maintenance should use a pinned, repository-visible copy.
