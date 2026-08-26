# Technology Profiles

Profiles are optional overlays for technology-specific repository artifacts and interfaces.
They turn universal properties into detectable decisions without making the core playbook
depend on a technology.

The following technology profile is available:

- [`docker-container-images`](docker-container-images/PROFILE.md) — draft guidance for Dockerfile-based application images.

Use [`_template/PROFILE.md`](_template/PROFILE.md) when proposing another profile.

## Selection

Treat availability and selection as separate facts:

- **available** means the profile exists in the pinned playbook revision;
- **enabled** means the consumer selected that available profile in
  `PROJECT_AGENT_CONTEXT.md`.

Before describing profile state, inspect the pinned `profiles/` directory. Ignore
`_template/`, prose examples, and profiles from other revisions. If a profile is absent,
say it is unavailable in the pinned revision. Never call it disabled, not enabled, or
intentionally omitted; those phrases incorrectly imply that it exists.

A consumer records available and enabled profile IDs in `PROJECT_AGENT_CONTEXT.md`.
Each ID is a stable descriptive `kebab-case` name based on the owned boundary, such as
`docker-container-images`; never use a number or list position as a profile ID.
Availability is inventory, not startup context: inspect directory names and this index
without opening every `PROFILE.md`.

Use a profile in one of two modes:

- **evaluation** — when the user explicitly asks to evaluate an available but unenabled
  profile, read only that profile and use it for audit findings and recommendations; do not
  apply its defaults or make profile-driven changes;
- **enabled application** — read an enabled profile only when an existing repository signal
  or an explicit task to introduce its owned boundary activates it and the current task can
  affect that boundary.

Enabling a profile is a project-level decision. It permits the profile to guide otherwise
authorized local work; it does not authorize edits, expand the current task, permit an
external action, or turn a default into a verified project fact. An agent must not enable a
profile silently.

Technology detection alone may justify recommending a profile by ID from this index. Do
not open or apply an unenabled profile merely because its technology is present. If
applicability remains ambiguous under an enabled profile's stated signals, do not apply its
defaults as assumptions.

If an enabled profile is absent from the pinned revision, report the context error. Do not
invent or fetch the missing guidance.

## Precedence and composition

Each profile owns a coherent set of decisions over named repository artifacts or
interfaces and states the properties those decisions protect. The accepted profile issue
sets the maximum scope. Related ecosystem advice and generally useful best practices are
outside the profile unless they are necessary to solve that accepted problem.

Split concerns into separate profiles when they can apply independently and are changed or
verified against different primary artifacts or authority boundaries. A shared ecosystem,
vendor, file format, or command-line tool is not sufficient reason to combine them.

The core playbook owns universal safety and maintenance properties. A profile may:

- **own** a technology-specific decision and its verification;
- define the minimum **interface** needed for an owned decision to compose with another owner; or
- **reference** a core document, another profile, or project context without restating it.

Project-local instructions and verified facts choose among valid alternatives. If profiles
claim the same decision and cannot be reconciled, surface the conflict and require a
project decision. Profiles cannot grant authorization, weaken platform constraints, or
convert an unverified convention into a project fact.

Profile findings enter the core [risk and priority model](../docs/audit-and-priorities.md#prioritize-findings).
Enabling a profile does not make all of its recommendations current work or rank them above
unresolved core findings.

## Profile contract

Every profile must:

- name the artifacts or interfaces it owns and the set of properties that bounds its decisions;
- activate only when an observable repository signal exists or the task explicitly
  introduces the owned boundary, and the task can affect that boundary;
- state false positives, exclusions, and what to do when activation is ambiguous;
- limit every decision to the accepted problem and its owned boundary;
- give every decision an observable condition and a required outcome tied to a declared property;
- state a default only when the profile can choose safely, and state alternatives and
  material tradeoffs only when more than one outcome is valid;
- map every decision to an exact verification target and observable result, either beside
  the decision or in a shared recipe;
- state an explicit supported range or a rule for determining support, including minimums
  only for non-baseline features the profile recommends;
- attach an official primary source to every material factual technical claim on which a
  decision depends, while identifying defaults and tradeoffs as profile judgments;
- state material execution, network, credential, external-service, state, and cleanup
  effects for verification;
- link to core and adjacent owners instead of copying their rules;
- present project examples only as validation of applicability, composition, and
  verification, never as authority for a general rule;
- keep non-goals and composition notes only where they prevent likely ownership confusion; and
- remain useful without assuming a specific forge or cloud provider.

A section or recommendation that cannot satisfy this contract does not belong in the
profile. Calling it advanced, optional, or a best practice does not create an exception.

## Lifecycle

Use these statuses:

- **draft** — incomplete or not yet validated across representative projects;
- **recommended** — reviewed and suitable for general use within its stated version range;
- **deprecated** — retained for migration but no longer recommended.

A stale review date does not automatically invalidate a profile, but agents must verify
time-sensitive instructions before applying them. Breaking profile changes follow the
repository versioning policy.

Every new profile starts as **draft**. Documentation research may support a draft but does
not prove general suitability. Promotion to **recommended** requires a separate focused
review documenting what was actually checked across at least two representative
repositories or project types that differ in a way relevant to the protected properties.

An unenabled draft is evaluation-only. An enabled draft may guide authorized work, but the
agent must identify it as draft, state relevant known gaps or untested variants, and verify
the claims needed for the current task. Profile status never grants authorization.

Start profile work from a maintainer-accepted profile issue. The author does not
automatically become a profile owner or project maintainer.
