# README Authoring

A README is the shortest reliable route from “what is this?” to an informed first success. It should help an unfamiliar reader recognize the problem, decide whether the project fits, act safely, and find deeper documentation. It is neither a dump of internal notes nor complete reference documentation.

## Establish facts before writing

Inspect the implementation, current README, examples, configuration, CI, releases, and project-local instructions. Write down:

- audience, concrete wedge, and general contract;
- primary tested scenario and observable outcome;
- supported, compatible, experimental, planned, and out-of-scope behavior;
- prerequisites, recommended installation path, and operating environments;
- sensitive data, trust boundaries, manual stages, and operator duties;
- maturity, known limitations, and support boundary.

Do not resolve unknowns with polished prose. Label them, verify them, or omit the claim.

## Design the first screen

Before a long scroll, a reader should understand:

- what the project is and who it serves;
- the concrete problem and resulting benefit;
- where it operates when environment matters;
- the broader contract beyond the initial scenario;
- current maturity or stability.

Lead with the outcome, then the mechanism. A value statement can follow either pattern:

> [Result] for [audience or context] without [the main manual or operational barrier].

> A [project category] that [specific result] through [the defining contract].

Do not open with languages, frameworks, component inventories, or abstract claims such as “seamless orchestration.” Keep badges and navigation subordinate to the explanation.

## Build a reader-oriented path

Adapt the order to the project; remove sections that do not answer a real reader question. A common path is:

1. name and concise value statement;
2. problem, audience, and primary scenario;
3. general contract and important boundaries;
4. a compact flow when relationships need explanation;
5. prerequisites and verified quick start;
6. minimal working use case and expected result;
7. capabilities and compatibility levels;
8. lifecycle or failure flow when operationally important;
9. configuration and deployment;
10. security, privacy, limitations, and non-goals;
11. status, troubleshooting, and recovery entry points;
12. development, contribution, release policy, license, and documentation index.

Do not force all of these into every README. Libraries, deployed services, specifications, templates, and documentation repositories have different primary paths.

## Explain the scenario and contract

Describe the real situation before the architecture: what exists where, what fails or consumes manual effort, and which part the project changes. Then identify the stable format, API, protocol, interface, or behavior that defines broader applicability.

Do not imply that a project is coupled to its first consumer when the contract is more general. Conversely, do not present theoretical contract compatibility as a tested integration.

Use explicit compatibility language:

| Level | Meaning |
| --- | --- |
| Primary / tested | The main scenario is exercised by project verification |
| Supported | Maintainers intentionally support and maintain it |
| Compatible by contract | It satisfies a documented boundary, but this integration may not be tested |
| Experimental | Available with limited implementation or evidence |
| Planned | Not implemented yet |
| Out of scope | Intentionally excluded from the current model |

Keep separate dimensions separate. Provider availability, consumer compatibility, deployment maturity, and support lifetime should not collapse into one “supported” mark.

## Write a trustworthy quick start

The quick start is the shortest safe route to the primary observable result. It should:

- state prerequisites and the expected working directory;
- distinguish machines, terminals, identities, or environments when needed;
- use the recommended path and only essential configuration;
- use obviously non-production placeholders;
- pin downloadable executable input to an immutable version;
- explain any destructive, privileged, networked, or long-running action;
- show what success looks like and the next verification command;
- link to detailed setup and troubleshooting.

Do not make a mutable `curl | shell` pipeline the only installation path. Prefer download, inspect, verify, and execute steps. If several machines are involved, name them explicitly; never make readers guess what `localhost` refers to.

After setup, give one minimal, copyable example that demonstrates the wedge through the real contract. Explain its effect and then briefly state how compatible consumers can substitute for the primary one.

## Make automation and lifecycle boundaries visible

For distributed, stateful, security-sensitive, or human-in-the-loop systems, explain the important lifecycle:

1. what detects or initiates the event;
2. where a decision is made;
3. whether and where a person participates;
4. what state or artifact changes;
5. how the consumer receives the result;
6. how failure becomes visible and recoverable.

Use “automatic” only for the part of the cycle that closes without an undocumented human action. Intentional approval or interactive authentication can be a safety boundary; describe it rather than hiding it.

## Cover trust and fit

Security text should identify sensitive data, safe defaults, exposure boundaries, operator responsibilities, important excluded threats, and the private reporting route. Put a full threat model in dedicated documentation.

Keep decisive limitations near the relevant capability and summarize major ones in a visible limitations section. Include required external accounts, unsupported environments, manual steps, resource-heavy behavior, external-service assumptions, and meaningful failure modes.

Avoid absolute adjectives such as secure, hardened, production-ready, fully automatic, or universal unless the conditions and evidence are explicit.

## Keep reference material elsewhere

Move exhaustive API reference, every configuration key, internal design history, full threat models, long troubleshooting catalogs, changelogs, and speculative roadmaps into maintained documents. The README should link to them without breaking the primary journey.

For related projects, state whether each is required, bundled, or optional and who owns its lifecycle and configuration. Link instead of duplicating another project's README or promising its behavior.

## Authoring sequence for agents

1. Audit the project and current README without editing.
2. Write one sentence each for the wedge, contract, audience, and primary result.
3. Classify capability and compatibility claims by evidence level.
4. Verify the recommended installation and main use case.
5. Rewrite the first screen before optimizing later sections.
6. Build the shortest safe quick start and minimal example.
7. Explain lifecycle, manual stages, trust boundaries, and limitations.
8. Move deep reference material out while preserving navigation.
9. Apply the rules in [README presentation](readme-presentation.md).
10. Check commands, versions, paths, claims, links, and actual rendering.

A README is ready when a stranger can assess fit and risk, reproduce the primary scenario without private context, recognize an expected success, and find the next appropriate document.
