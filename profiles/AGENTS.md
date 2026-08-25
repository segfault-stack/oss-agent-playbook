# Instructions for technology profiles

These instructions apply to `profiles/` in addition to the repository root `AGENTS.md`.

## Before adding or changing a profile

1. Read `profiles/README.md`, `profiles/_template/PROFILE.md`, and the core documents the profile specializes.
2. Confirm that the guidance is ecosystem-specific and useful across multiple real projects.
3. Verify current behavior against primary official documentation.
4. Identify interactions with existing profiles.

## Content rules

- Keep `PROFILE.md` as the profile entry point.
- Record status, supported versions, and an ISO `YYYY-MM-DD` review date.
- Prefer stable ecosystem capabilities over fashionable tools.
- Describe a decision and its tradeoffs before naming a default tool.
- Offer alternatives when the ecosystem has multiple established approaches.
- Do not turn a tool preference into a universal safety requirement.
- Do not copy universal authorization, security, README, CI, or release prose into a profile; link to it.
- Do not claim support based only on documentation. State what was tested and how.
- Use commands that are safe, non-interactive by default, and explicit about prerequisites.

## Verification

Check links, version claims, commands, platform assumptions, and composition with adjacent profiles. Update the review date only after substantive re-verification, not for editorial changes.
