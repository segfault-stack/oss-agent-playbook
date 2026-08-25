# 0002 — Use human-gated contribution governance

- Status: Accepted
- Date: 2026-08-25
- Supersedes: None

## Context

The playbook should accept guidance improvements and technology profiles from the public.
At the same time, agents make it inexpensive to generate more issues, pull requests, and
review replies than a small maintainer group can responsibly evaluate. Review attention and
long-term ownership remain human costs even when creation and syntax validation are cheap.

This repository currently has one human maintainer and expects any future maintainer group
to remain small and accountable. The project itself is developed with agents, so banning
AI-assisted work or trying to detect generated prose would contradict its purpose and
would not establish contribution quality.

## Decision

Use a staged, human-gated contribution model:

- AI-assisted and substantially agent-produced work is allowed without disclosure.
- A human contributor must read and understand the final diff and submission before an
  agent may mechanically publish it.
- Consequential, cross-document, and technology-profile work requires a maintainer-accepted
  issue before implementation; narrow corrections may go directly to a pull request.
- A user without write access may have one open non-draft pull request at a time unless a
  maintainer explicitly grants a trusted-contributor bypass.
- Initial technology profiles enter as `draft`; promotion to `recommended` requires later
  validation across at least two representative projects or project types.
- Maintainers may close work whose relevance, evidence, maintainability, or review cost
  does not justify acceptance, without supplying a detailed critique.
- Ordinary changes require one maintainer approval. Once two or more active maintainers
  exist, consequential changes require affirmative acceptance from two maintainers,
  including at least one non-author approving review, and no unresolved maintainer
  objection.
- A sole maintainer uses public pull requests for substantive self-authored work and
  documents the necessary administrator bypass. Direct pushes remain available for narrow
  corrections and urgent recovery.
- Do not adopt a formal Code of Conduct until a human owner is prepared to receive and
  enforce private reports. Do not require DCO sign-offs unless provenance risk or
  contribution volume later justifies the friction.

Current policy lives in [Governance](../../GOVERNANCE.md),
[AI-assisted contributions](../../AI_CONTRIBUTIONS.md), and the
[contribution guide](../../CONTRIBUTING.md).

## Consequences

### Benefits

- The cheapest decision—whether work belongs—happens before expensive implementation
  review.
- Contributors may use agents without ceremonial disclosure while a human remains
  accountable for public actions and claims.
- Native pull-request limits constrain ready-for-review floods without granting trusted
  contributors repository write access.
- Draft profiles can improve publicly without overstating validation.
- Maintainers retain explicit discretion over finite review and maintenance capacity.

### Costs and limitations

- Human review before publication cannot be proven automatically.
- Pull-request templates and attestations can be completed dishonestly.
- GitHub's pull-request cap excludes drafts, so documented policy and moderation still
  cover draft spam.
- Sole-maintainer review is not independent review; the public pull request records this
  limitation but cannot remove it.
- Closing low-quality work may reject some good-faith contributions, so decisions should
  target observable quality and scope rather than language fluency or assumed AI use.

## Boundaries

- Do not use a CLA, DCO, or Code of Conduct as a bot-detection obstacle without accepting
  the legal and operational duties it creates.
- Do not use automated AI-output classifiers as an acceptance gate.
- Do not grant agents approval, merge, moderation, or maintainer authority.
- Do not run untrusted fork code with secrets or writable repository tokens.
- Use temporary interaction limits only for an actual abuse event, not as the normal public
  contribution boundary.

## Reconsideration triggers

Revisit this decision if contribution volume overwhelms one-change intake, trusted
contributors need parallel work, issue spam becomes material, a real moderation owner
appears, provenance disputes occur, or several active maintainers need a different
decision rule.

## Evidence reviewed

- GitHub documents persistent per-user pull-request caps and trusted-contributor bypasses:
  [Limiting interactions](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository).
- GitHub describes repository-local agent instructions, enforced templates, CI gates, and
  maintainer discretion as practical controls for agent-heavy contribution queues:
  [Your contributors are AI-first now](https://github.blog/open-source/maintainers/your-contributors-are-ai-first-now-is-your-project/).
- The Open Home Foundation permits human-owned AI assistance while rejecting autonomous
  public submissions: [AI policy](https://github.com/home-assistant/home-assistant.io/blob/current/AI_POLICY.md).
- OpenSSF requires documented contribution and public discussion mechanisms while treating
  more elaborate governance as a later maturity step:
  [OSPS Baseline](https://baseline.openssf.org/versions/2026-02-19) and
  [Best Practices criteria](https://github.com/ossf/best-practices-badge/blob/main/docs/criteria.md).
