# Technology Profiles

Profiles are optional overlays for ecosystems such as Python, Go, Docker, or a hosting platform. They turn universal properties into ecosystem-specific decisions without making the core playbook depend on a technology.

No technology profiles have been published yet. Use [`_template/PROFILE.md`](_template/PROFILE.md) when adding the first one.

## Selection

A consumer lists enabled profiles in `PROJECT_AGENT_CONTEXT.md`. Several profiles may apply to the same project. An agent reads a profile only when both conditions hold:

1. the consumer explicitly enables it or the user asks to evaluate it;
2. its scope intersects the current task.

Technology detection alone may justify recommending a profile, but it must not silently add the profile or turn its defaults into project facts.

## Precedence and composition

The core playbook defines universal safety and maintenance properties. A profile explains how an ecosystem commonly satisfies those properties. Project-local instructions and verified project facts choose among valid profile alternatives.

When multiple profiles apply, combine their requirements by concern. For example, a language profile may own dependency locking while a container profile owns image construction. If two profiles claim the same decision and cannot be reconciled, surface the conflict and ask for a project decision.

Profiles cannot grant authorization, weaken platform safety constraints, or convert an unverified convention into a project fact.

## Profile contract

Every profile must:

- declare scope, applicability signals, status, supported ecosystem versions, and last review date;
- link each time-sensitive recommendation to a primary official source;
- distinguish required safety properties, recommended defaults, acceptable alternatives, and optional maturity practices;
- provide concrete local and CI verification;
- state security, dependency, packaging, and release concerns that are unique to the ecosystem;
- link to core rules instead of repeating their rationale;
- avoid starter-project boilerplate and commands that cannot be verified generically;
- document conflicts and composition with related profiles;
- remain useful without assuming a specific forge or cloud provider.

Split a profile only after one file becomes difficult to navigate. `PROFILE.md` remains its index and source-of-truth map.

## Lifecycle

Use these statuses:

- **draft** — incomplete or not yet validated across representative projects;
- **recommended** — reviewed and suitable for general use within its stated version range;
- **deprecated** — retained for migration but no longer recommended.

A stale review date does not automatically invalidate a profile, but agents must verify time-sensitive instructions before applying them. Breaking profile changes follow the repository versioning policy.

Every new profile starts as **draft**. Promotion to **recommended** requires a separate
focused review with evidence that its guidance was checked against at least two
representative repositories or project types within the declared scope. Documentation
research alone is not sufficient evidence of general suitability.

Start profile work from a maintainer-accepted profile issue. Comment with the intended
project types, primary sources, outline, and adjacent-profile interactions before opening
a broad implementation pull request. The author does not automatically become a profile
owner or project maintainer.
