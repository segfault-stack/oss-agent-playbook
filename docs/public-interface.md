# Public Interface

The repository root and hosting metadata are part of the product interface. They should let an unfamiliar reader decide whether the project applies, try its primary path, and understand its risks without private context.

## Metadata

The description should state what the project does, its relevant context or audience, and the barrier it removes. Lead with user value rather than implementation details.

Choose a small set of topics representing the real problem, use case, compatible format or protocol, deployment category, ecosystem, and product category. Do not add weakly related popular terms, competitor names for traffic, or unverified integrations.

Enable discussions, wiki, projects, and similar surfaces only when they have content and an owner.

## README

Treat the README as the repository's primary onboarding route, not as complete technical documentation or a marketing landing page. [README authoring](readme-authoring.md) owns its content contract, first-screen requirements, and reader path. [README presentation](readme-presentation.md) owns prose, visual, and rendering rules.

## Configuration and operations documentation

Commit a safe example that covers required settings and useful options, uses obviously non-functional secret placeholders, and stays synchronized with runtime validation. Separate configuration from credentials and state.

When the project is deployable, document external dependencies, persistent state, backup and restore expectations, migrations, health checks, network exposure, permissions, optional components, and safe log inspection. Do not present a production configuration as a reusable example.

## Community surface

Add contribution instructions, issue forms, a change template, support policy, and code of conduct according to actual contribution volume and maintainer capacity. A short accurate guide is better than a generic one.

Public forms should warn users not to include credentials, authorization headers, cookies, personal data, or raw private logs. Provide a private route for vulnerability reports and state supported versions if they are defined. Do not promise response times that cannot be maintained.

## External communication

Promotion must follow, not substitute for, safety and usability work. Target places whose audience actually has the problem, lead with the concrete outcome, and then explain the broader contract.

Preparing a draft does not authorize publication. Never post, message, submit to catalogs, open third-party pull requests, or speak for a maintainer without explicit authorization for the exact action. Before an authorized publication, recheck destination, account, final text, links, claims, and sensitive data.
