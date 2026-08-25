# 0001 — Use Git-native maintainer memory with human-owned acceptance

- Status: Accepted
- Date: 2026-08-25
- Supersedes: None

## Context

This repository is maintained through file-aware agents, should remain usable by Codex,
Claude Code, and other runtimes, and is intended to be easy to clone and inspect. Durable
maintenance lessons need to survive across agent sessions and machines without becoming a
hidden product-specific state store.

Codex and Claude Code both distinguish human-authored repository instructions from local
agent-generated memory. Their native memories are useful personal recall layers, but they
are machine-local, product-specific, and unsuitable as the only shared source for a public
repository.

The repository currently has low write volume and one human maintainer. Future maintainers
may form a small equal group, but consequential changes should continue to be read by an
accountable human rather than accepted automatically from agent output.

## Decision

Use Git-tracked Markdown as the shared maintainer-memory and decision system:

- `AGENTS.md` and `CLAUDE.md` remain the instruction plane.
- `PROJECT_AGENT_CONTEXT.md` remains the current verified project-state plane.
- `MAINTAINER_MEMORY.md` is a concise public index of accepted durable lessons.
- `docs/decisions/` is an append-oriented history of consequential choices.
- GitHub Issues remain the backlog and proposal surface; GitHub Releases remain release
  history.
- Vendor-native memory may supplement this system locally but is never authoritative or
  required for repository continuity.

Agents may prepare or edit memory and decision files within an explicitly authorized
repository change. They must surface those diffs, and a human maintainer must read
consequential memory, decision, or instruction changes before acceptance. Learned memory
cannot silently promote itself into instructions.

Accepted decisions are substantively immutable. A later reversal creates a new decision
file that names the earlier record in `Supersedes`; the earlier record then links forward
and changes status to `Superseded`.

## Consequences

### Benefits

- Every file-aware agent can inspect the same accepted context.
- Ordinary clones, source archives, subtree imports, and initialized submodules preserve
  the shared records.
- Pull requests and commits provide readable review, attribution, rollback, and conflict
  handling.
- The architecture introduces no runtime service or third-party dependency.
- Human approval remains distinct from automated validation.

### Costs and limitations

- Git-tracked memory must contain only public-safe information.
- Git is not a high-frequency concurrent memory database.
- Native personal preferences remain separate and may differ across machines.
- Removing tracked sensitive data from the current tree would not erase it from history,
  clones, or forks.
- Maintainers must keep the memory index concise and prevent duplication with current
  source-of-truth documents.

## Boundaries

- Do not store raw conversations, chain-of-thought, credentials, private messages, local
  machine paths, customer data, or unresolved security-report content.
- Do not use maintainer memory for open tasks, release notes, or transient session state.
- Do not grant an agent merge or approval authority merely because validation passes.
- Do not write consumer-project memory inside a vendored playbook subtree or submodule.
- Do not introduce a database, generation-pointer store, or remote service without a
  demonstrated concurrency, scale, privacy, or multi-host requirement and a new decision.

## Instruction evolution

When a learned lesson appears to require a permanent rule:

1. Identify the repeated failure and evidence.
2. Propose the smallest instruction change in the closest applicable file.
3. Search for duplicate or conflicting rules.
4. Review the exact diff and run applicable checks.
5. Accept the change through the normal human-owned Git workflow.
6. Start a new agent session when reliable rediscovery of changed startup instructions is
   required.
7. Link the memory entry to the authoritative rule or decision instead of retaining a
   competing paraphrase.

## Reconsideration triggers

Revisit this decision if one or more of the following becomes real rather than
hypothetical:

- several background agents write memory concurrently;
- memory volume makes a bounded Markdown index and on-demand files ineffective;
- multiple hosts require coordinated private state outside Git;
- structured queries, TTL processing, or automated consolidation become core behavior;
- public Git history cannot satisfy the required privacy or deletion model.

At that point, compare an immutable generation store, SQLite for single-host transactional
state, and a controlled remote service for multi-host writers. Preserve the same separation
between instructions, verified project state, learned memory, and human acceptance.

## Evidence reviewed

- OpenAI documents checked-in `AGENTS.md` as the durable project-guidance layer and local
  memories as a separate recall layer: [Codex memories](https://learn.chatgpt.com/docs/customization/memories)
  and [custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- Anthropic documents `CLAUDE.md` as human-written instructions and auto memory as
  machine-local agent-written learnings: [How Claude remembers your project](https://code.claude.com/docs/en/memory).
- The broader storage and backend comparison that led to this decision also reviewed
  [POSIX rename](https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html),
  [SQLite atomic commit](https://sqlite.org/atomiccommit.html), and
  [Git update-ref](https://git-scm.com/docs/git-update-ref.html).
