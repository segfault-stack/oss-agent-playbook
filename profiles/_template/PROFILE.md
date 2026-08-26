# Technology Profile: NAME

Delete prompts when drafting. Add sections only when this schema cannot express an
accepted requirement.

## Metadata

- **ID:** `descriptive-kebab-case-name` matching the profile directory; never numeric
- **Status:** draft
- **Supported versions:** explicit range or rule for determining support
- **Last reviewed:** `YYYY-MM-DD`
- **Primary sources:** official sources supporting the profile's material technical claims

## Scope

- **Owns:** exact repository artifacts or interfaces
- **Protects:** the property set that bounds decisions in this profile
- **Specializes:** links to owning core rules
- **Does not own:** only boundaries a reasonable reader would otherwise confuse with this profile

## Applicability and detection

Apply this profile only when both are true:

- an observable repository signal exists or the task explicitly introduces the owned boundary; and
- the current task can affect a protected property at that boundary.

State strong signals, incidental or ambiguous lookalikes, exclusions, and the required
action when applicability cannot be established. Do not apply profile defaults from a
technology mention alone.

## Decisions

Create one subsection per decision. Each decision must state:

- the observable condition that makes it apply; and
- the required outcome and protected property.

State a default only when the profile can choose safely. State alternatives and material
tradeoffs only when more than one outcome is valid. Add prohibited patterns or migration
only when omitting them would leave the accepted problem unresolved or the required
outcome unsafe.

Map every decision to an exact verification target and observable result, either beside
the decision or in the verification recipe. Link each material factual technical claim to
an official primary source; a shared source list is acceptable only when the mapping is
unambiguous. Keep profile defaults and tradeoffs distinguishable from source-owned facts.

## Verification recipe

Order the minimum commands or observable checks needed to cover the decisions above. State
each target and expected result plus material repository-controlled execution, network or
credential needs, external effects, created state, and targeted cleanup. Baseline
verification must not publish or perform broad cleanup.

## Composition

List only concrete handoffs or conflicts. For each one, distinguish what this profile owns,
the interface it requires, and the core rule, profile, or project context that owns the
other side.

## Evidence and maintenance

State what was actually checked, known gaps, untested variants, evidence still needed for
the next lifecycle status, and events that require technical re-review. Project examples
may validate applicability, composition, or verification; they do not establish normative
guidance.
