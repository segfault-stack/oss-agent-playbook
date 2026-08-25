# Principles

## Publish reality, not an image of maturity

Describe what the project does today. Separate supported, experimental, planned, and removed behavior. Do not invent compatibility, testimonials, metrics, support capacity, security audits, or stability guarantees.

Every public file and enabled repository feature creates a maintenance expectation. Add it only when somebody owns it and it solves a current need. Empty discussions, generic roadmaps, stale changelogs, and ceremonial templates reduce trust.

## Define the publication boundary

Before preparing a repository, identify what it is intended to provide, for example:

- inspectable source;
- enough documentation to understand and evaluate it;
- reproducible build and verification instructions;
- safe configuration examples;
- installable, versioned artifacts;
- a contribution path.

These are independent choices. Public source does not automatically imply hosted support, compatibility guarantees, a contributor program, a roadmap, or one-command deployment.

## Pair a concrete entry point with a general contract

Position a project using both:

- the **wedge**: the concrete problem or scenario that makes the project easy to find and understand;
- the **contract**: the broader capability and boundaries that determine where else it applies.

A useful formulation is: “The project was created for problem X and works for consumers that satisfy contract Y.” Keep this positioning consistent across repository metadata, README, examples, releases, and external materials.

Do not reduce a general tool to its first use case. Do not describe it only through abstract architecture or implementation technologies either.

## Require evidence for claims

A significant claim should be supported by a test, a verified example, a reproducible artifact, or clearly labeled evidence. Architecture that could theoretically support an integration is not proof that the integration is supported.

Reveal mandatory manual stages. Do not call a workflow automatic when normal operation still depends on an undocumented intervention.

## Prefer proportional controls

Apply stronger controls where failure could expose secrets, lose data, break public interfaces, or compromise distributed artifacts. A small documentation-only project and a privileged network service do not need identical process.

Security and honesty outrank discoverability and polish. Fix dangerous installation instructions, exposed credentials, license conflicts, severe vulnerabilities, and false claims before promotion.

## Preserve maintainer intent and user work

Understand the product before reorganizing it. Do not infer purpose from the language, manifest, or directory names alone. Preserve unrelated worktree changes and avoid mixing independent work in one change.

Do not rename or reorganize files merely to resemble another repository. Conventional entry points are useful; internal structure should follow the project.
