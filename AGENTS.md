# Instructions for agents maintaining this playbook

## Purpose and scope

This repository is a technology-neutral playbook for agents working on public open-source repositories. Improve the guidance itself; do not turn it into rules for one language, forge, CI vendor, or deployment platform.

Instructions in this file apply to the entire repository.

## Sources of truth

- `README.md` is the short index and scope statement.
- `GOVERNANCE.md` owns maintainer roles, acceptance authority, and decision thresholds.
- `AI_CONTRIBUTIONS.md` owns the human-review boundary for agent-assisted public work.
- `PROJECT_AGENT_CONTEXT.md` records this repository's own verified commands, public boundary, and release process.
- `MAINTAINER_MEMORY.md` indexes accepted public maintenance lessons; it is advisory and does not override instructions or current project facts.
- `docs/decisions/` records consequential maintenance decisions and their supersession history.
- `docs/principles.md` owns universal scope, evidence, and restraint rules.
- `docs/audit-and-priorities.md` owns audit coverage and prioritization.
- `docs/public-interface.md` owns repository metadata and community surfaces.
- `docs/security-and-reproducibility.md` owns secrets, privacy, licensing, dependencies, and supply-chain rules.
- `docs/engineering-and-releases.md` owns quality gates, branches, releases, and operational changes.
- `docs/agent-workflow.md` owns authorization, execution, verification, and handoff behavior.
- `docs/readme-authoring.md` owns README content and reader-flow rules; `docs/readme-presentation.md` owns visual and rendering rules.
- `docs/checklists.md` summarizes other documents; it must not introduce new requirements.
- `ADOPTION.md` and `templates/` define how consumer repositories use the playbook.
- `profiles/` contains optional technology overlays and its own maintenance instructions.
- `CONTRIBUTING.md`, `SUPPORT.md`, and `SECURITY.md` own the contributor, support, and sensitive-reporting boundaries.

Put each rule in one primary document. Link to it elsewhere instead of maintaining paraphrased copies. If a summary must repeat a rule, update both locations in the same change.

## Editing rules

1. Preserve technology and hosting neutrality. Examples may name tools, but requirements must describe the property being protected.
2. Distinguish universal safety boundaries from optional maturity practices. Do not require ceremony without a demonstrated maintenance benefit.
3. Use direct, testable language. Prefer “verify the documented command in a clean environment” to vague advice such as “ensure quality.”
4. Keep authorization separate from capability. Guidance may explain an external action without granting an agent permission to perform it.
5. Never weaken secret handling, privacy, license, destructive-action, or external-communication safeguards for convenience.
6. Avoid fixed version numbers, transient product behavior, and undocumented assumptions about agent runtimes.
7. Keep project-specific commands, contacts, support promises, and compatibility claims in consumer project context, not in this repository.
8. Add a new file only when it has a distinct reader task. Prefer extending the closest existing document.
9. A profile may specialize a universal property but must link to, not restate, the core rule.
10. Use the smallest enforcement surface that closes the observed failure. Put behavioral
    guidance in its source-of-truth document and update only necessary routes or templates.
    Add automation only when it can detect the actual regression; do not use structural
    checks as a proxy for agent judgment or wording.

## Change workflow

Before editing, read `README.md`, `PROJECT_AGENT_CONTEXT.md`, the target document, and any document that links to the section being changed. Search for duplicates and contradictory wording.

For substantive changes, also read `MAINTAINER_MEMORY.md` and only the decision records relevant to the task. Do not load the full decision history mechanically.

For substantive changes:

1. State the cross-project problem the rule solves.
2. Put the normative rule in the appropriate source-of-truth document.
3. Update affected checklists, templates, links, and adoption guidance.
4. Review the result from both perspectives: an agent applying the playbook and a maintainer adopting it.
5. Keep unrelated user changes intact.

## Public contributions

- Follow `CONTRIBUTING.md`, `GOVERNANCE.md`, and `AI_CONTRIBUTIONS.md` when preparing work
  for this repository.
- Do not publish an issue, pull request, review reply, or other repository communication
  until a human contributor has read the exact final diff and submission text.
- Agents may perform authorized mechanical publication after that review, but cannot supply
  human acceptance, approval, or maintainer authority.
- Broad guidance, technology profiles, and consequential changes require a linked issue
  with maintainer-accepted scope before implementation. Narrow corrections may go directly
  to a pull request.
- Do not open or advance parallel changes to evade the one-active-contribution limit.
- Maintainers may close low-quality, misleading, bulk, or unreviewable work without asking
  an agent to generate a detailed rebuttal.

## Maintainer memory and decisions

- Keep all shared memory public-safe, concise, evidence-backed, and useful across future tasks.
- Do not store backlog items, release history, raw conversations, private preferences, local paths, credentials, personal data, or sensitive reports in maintainer memory.
- An agent may update `MAINTAINER_MEMORY.md` during authorized repository work, but must surface the exact diff in its handoff. Background or self-triggered promotion is not allowed.
- Learned memory never silently changes `AGENTS.md`, `CLAUDE.md`, or another instruction file. Instruction changes require an explicit, reviewable patch within the authorized task.
- Create a new decision file for consequential changes to authority, safety boundaries, adoption defaults, source-of-truth ownership, or repository-wide architecture.
- Keep accepted decision records substantively immutable. Reverse one with a new record that supersedes it.
- Consequential memory, decision, and instruction changes require human maintainer review. Automated checks provide evidence; they do not grant approval or merge authority.

## Verification

Before handing off a change:

- inspect the complete diff and untracked files;
- check relative Markdown links and anchors;
- search for stale filenames and duplicated requirements;
- confirm headings and lists render clearly;
- verify that examples contain no real credentials, personal data, or implied promises;
- run `python3 scripts/check_docs.py` and any other repository-provided checks.

After every agent-authored change to this playbook, stop before creating a commit or
publishing remotely and explicitly offer the human maintainer an immediate review of the
complete diff. State plainly that reviewing the exact diff is required before both commit
and remote publication. Provide the exact local review command and offer to display the
diff in the conversation. Do not proceed until the maintainer confirms that review;
advance authorization to commit or push does not replace it. A change summary, file list,
or test report is not a substitute, even when the diff is small.

If no automated documentation checks exist, say so in the handoff rather than claiming full validation.

## Writing style

Write concise English intended for agents and maintainers. Use short sections, explicit conditions, and imperative language. Define uncommon terms on first use. Avoid marketing copy, badge walls, decorative diagrams, and framework-specific tutorials.

Report state only when it affects the outcome, the next action, or a maintainer decision.
Do not present an expected intermediate state, such as a local branch being ahead after an
authorized commit, as a warning or blocker. When the user has authorized the remaining
steps and no real constraint intervenes, continue the workflow and report the completed
outcome in plain language.
