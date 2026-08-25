# README Presentation

Presentation should make information easier to scan and trust. It should not compensate for unclear purpose, missing evidence, or an unsafe setup path.

## Use compact, specific prose

- Prefer user behavior and outcomes to internal component descriptions.
- Keep each paragraph focused on one idea.
- Define uncommon terms on first use and keep terminology consistent.
- Replace generic adjectives with observable behavior.
- Remove repeated taglines, promotional filler, and dependency inventories from the overview.
- Use headings that tell a scanning reader what question the section answers.

Create rhythm with short paragraphs, meaningful headings, compact lists, occasional tables, command blocks, warnings, and whitespace. Do not alternate formats mechanically or decorate an otherwise flat hierarchy.

## Use structures for the information they fit

Use a table for concise comparisons, exact mappings, compatibility, command variants, or configuration properties. Avoid it for long prose, nested procedures, feature-marketing cards, or content that becomes unreadable on a narrow screen.

Use a diagram when several components, ownership boundaries, state transitions, or branches are materially clearer visually. Prefer the smallest useful flow, sequence, tree, or topology. Remove diagrams that merely repeat a paragraph, require zooming, expose premature implementation detail, or are expensive to keep current.

Use collapsible details for optional, independent material that would interrupt the main path. The summary must say exactly what is inside. Never hide required setup, critical limitations, security warnings, or destructive effects in a collapsed block.

## Keep badges meaningful

A small badge set may communicate live CI status, license, a published release, or a genuinely important runtime requirement. Each badge should represent current public state and link to evidence accessible without authentication.

Remove stale, decorative, duplicate, or unpublished badges. A badge does not prove quality, security, or compatibility by itself.

## Use visuals deliberately

A README may use one primary hero or none. A useful hero is compact, legible at normal repository width, proportional, locally stored, and supplied with meaningful alternative text. It should reinforce identity without competing with the project explanation.

Avoid multiple competing logos, light/dark variants without a demonstrated need, tiny labels in oversized artwork, fake user interfaces, stale screenshots, excessive empty space, and illustrations added only to fill space. Never create or replace visual assets unless the maintainer has authorized that work.

Inspect screenshots and binaries for credentials, conversations, personal identifiers, private endpoints, filenames, timestamps, and other production-derived data.

## Research patterns, not content

When references are useful, inspect several actively maintained repositories from different categories. Study section order, density, navigation, optional-detail handling, and image placement. Do not copy claims, sections, branding, or functionality into a project where they do not apply. Popularity is evidence of exposure, not proof that a design choice fits.

## Verify the target rendering

An editor preview is insufficient. On the actual hosting renderer, check:

- heading anchors and navigation;
- relative links and unauthenticated access to external targets;
- image paths, alternative text, dimensions, and scaling;
- table width and narrow-screen readability;
- details blocks, callouts, and supported Markdown or HTML syntax;
- code-fence language tags and copyability;
- badge loading and destinations;
- light and dark theme behavior;
- desktop and narrow layouts without zooming.

Use only syntax the target platform supports. Consult its current official documentation when rendering behavior is consequential or uncertain.

## Review in focused passes

1. **Accuracy:** match claims, commands, paths, versions, features, and limitations to reality.
2. **Security:** inspect prose, examples, images, and links for sensitive or production data.
3. **Structure:** verify that purpose precedes setup and deep details do not interrupt the primary path.
4. **Language:** shorten prose, remove repetition, and normalize terminology.
5. **Visual:** justify every table, diagram, details block, badge, and image.
6. **Rendered:** exercise links, anchors, assets, code blocks, themes, and narrow layouts on the target platform.

Record anything that could not be rendered or verified. Do not claim completion based only on source-level inspection.
