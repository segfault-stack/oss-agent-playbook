# Maintainer Memory

This is the public, Git-tracked index of durable lessons accepted while maintaining the
OSS Agent Playbook. It is advisory context, not an instruction source and not a backlog.

Read it before substantive changes, then follow links to the relevant decision or
source-of-truth document. Do not load every linked document without a task-specific reason.

## Authority and scope

- `AGENTS.md`, applicable directory instructions, and the current user request govern work.
- `PROJECT_AGENT_CONTEXT.md` owns current repository facts and commands.
- [`docs/decisions/`](docs/decisions/) records why consequential maintenance choices were
  made and how later decisions supersede them.
- This file only indexes accepted lessons that are useful across future maintenance tasks.
- GitHub Issues own proposed work. Releases own release history. Neither belongs here.

All content must be safe for a permanent public repository. Never record credentials,
private communications, personal preferences, local paths, customer data, or sensitive
security-report details.

## Accepted lessons

### MM-001 — Separate learned memory from instructions

Agent-generated observations remain advisory. They may support a proposed instruction
change, but they never silently promote themselves into `AGENTS.md`, `CLAUDE.md`, or other
policy. Apply instruction changes only as explicit, reviewable diffs within the authorized
task. See [Decision 0001](docs/decisions/0001-git-native-maintainer-memory.md).

### MM-002 — Use Git as the shared publication and history layer

For this low-write, documentation-first repository, reviewed files and commits provide a
more portable and inspectable shared history than a custom database. Use new decision
files for consequential choices and normal focused edits for the current memory index.
Reconsider a transactional store only if real concurrent background writers or high-volume
records appear. See [Decision 0001](docs/decisions/0001-git-native-maintainer-memory.md).

### MM-003 — Keep acceptance human-owned

Agents may prepare memory, decisions, and policy diffs during authorized repository work,
but a human maintainer must read consequential changes before they are accepted. Passing
automation is evidence, not approval. If the maintainer group grows, keep acceptance
limited to a small, accountable reviewer set rather than granting agents merge authority.
See [Decision 0001](docs/decisions/0001-git-native-maintainer-memory.md).

### MM-004 — Validate indexes against their sources

When a human-readable index repeats filenames or status metadata owned by underlying
documents, validate the index against those sources. This prevents missing entries and
stale status labels from surviving otherwise successful documentation checks. The
[documentation checker](scripts/check_docs.py) applies this rule to the decision log.

## Updating this index

Add or revise an entry only when the lesson is:

- durable across future tasks;
- supported by a verified repository source, accepted decision, or explicit maintainer
  correction;
- concise, public-safe, and not already owned by another current-context document;
- useful enough to justify always being discoverable.

An agent may update this file as part of an already authorized repository change and must
surface the exact diff in its handoff. Background or self-triggered memory promotion is not
allowed. A change to agent authority, security boundaries, publication defaults, or the
memory model requires a new decision file and human review.

When a lesson becomes obsolete, keep its stable ID, mark it superseded, and link to the
replacement decision or current source. Do not preserve raw session transcripts or a
chronological activity log here.
