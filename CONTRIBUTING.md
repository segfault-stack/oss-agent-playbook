# Contributing

Contributions are welcome when they make the playbook clearer, safer, more accurate, or
easier to adopt across projects.

Read [Governance](GOVERNANCE.md) for acceptance authority and
[AI-assisted contributions](AI_CONTRIBUTIONS.md) before publishing agent-assisted work.
Open participation does not guarantee review, acceptance, mentorship, or merge.

## Before proposing a change

1. Read `AGENTS.md` and the source-of-truth document for the rule you want to change.
2. For a substantive change, read `MAINTAINER_MEMORY.md` and the relevant records under `docs/decisions/`.
3. Search existing issues and text for prior discussion, duplicates, and contradictions.
4. For technology-specific guidance, also follow `profiles/AGENTS.md` and start from the profile template.
5. Open an issue first when adding a profile or when a proposal changes authorization
   boundaries, reverses a normative default, introduces a public promise, or affects
   several documents.

Small corrections, broken links, and unambiguous clarifications may go directly to a pull request.

## Proposal lifecycle

Use the matching structured issue form. Maintainers record proposal state with a status
label and an explicit comment:

- `status: needs-info` — required evidence or scope is missing;
- `status: evaluating` — maintainers are deciding whether the problem belongs;
- `status: accepted` — implementation is welcome within the stated scope;
- `status: blocked` — accepted work is waiting on a named dependency or decision.

`status: accepted` is a scope decision, independent of whether the issue is open or closed.
When reporting it, state both facts explicitly, for example: “Issue open; scope status
accepted.” It makes an implementation eligible for review; it does not guarantee merge. If
implementation materially exceeds the accepted scope, return to the issue before continuing.

Comment before starting substantial work so maintainers and other contributors can avoid
duplicating effort. A contributor without write access may have one active contribution
under review unless a maintainer grants an explicit bypass. Do not open parallel drafts or
use alternate accounts to evade this limit.

## Change requirements

- Keep universal guidance independent of language, forge, CI vendor, and deployment platform.
- Put a rule in one source-of-truth document and link to it elsewhere.
- Support time-sensitive technical guidance with primary official sources.
- Separate verified behavior from assumptions, compatibility by contract, and roadmap ideas.
- Do not include credentials, private data, proprietary material, or production-derived examples.
- Keep changes focused and explain their effect on agents or maintainers.
- Add a new decision record when changing authority, safety boundaries, adoption defaults, source-of-truth ownership, or repository-wide architecture. Do not substantively rewrite an accepted decision to conceal a reversal.
- Treat `MAINTAINER_MEMORY.md` as a concise public index of durable lessons, not as a backlog, activity log, or instruction channel.
- Read and understand the final diff and submission text before publication. Review the
  reported evidence, checks, and limitations. Agents may publish only after this human
  review.

By contributing, you agree that your contribution is dedicated under the repository's [CC0 1.0 Universal](LICENSE) terms.

## Verification

Run:

```bash
python3 scripts/check_docs.py
```

Then inspect the complete diff, rendered Markdown, and any changed external links. State checks that were not run or could not be reproduced.

## Pull requests

Describe the cross-project problem, the chosen rule or structure, evidence used, compatibility impact, and residual limitations. Call out changes to instructions, maintainer memory, or accepted decisions explicitly. A pull request should not mix unrelated guidance or silently rewrite project policy.

Link a `status: accepted` issue for profiles, broad guidance, cross-document work, and
consequential changes. Draft pull requests are useful for early structural feedback only
after scope acceptance. Unsolicited broad changes may be closed without line-by-line
review.

Maintainers judge relevance, correctness, evidence, maintainability, compatibility, and
review cost. Passing automation is necessary evidence, not acceptance. A maintainer may
ask the contributor to explain a material choice or source; the contributor remains
responsible for accurate follow-up regardless of the tools used to prepare it.

Squash merge is the default for external contributions. A clean intentional commit series
may be rebased. Policy, profile, authority, and architecture changes are not auto-merged.

## Technology profiles

New profiles merge as `draft`. Promotion to `recommended` requires a later focused pull
request showing verification across at least two representative repositories or project
types. Profile authors do not automatically become maintainers or permanent owners.

Whole ecosystem profiles are substantial research tasks and should not be labeled
`good first issue`. Reserve that label for narrow, accepted work with explicit boundaries
and verification.

## Moderation

Maintainers may close low-quality, misleading, bulk, out-of-scope, or unreviewable work
without providing a detailed critique. Repeated autonomous submissions, spam,
misrepresentation, or attempts to evade a decision may be reported and blocked through
GitHub. Ordinary disagreement, imperfect English, and use of translation or accessibility
tools are not violations.

Participation remains subject to the
[GitHub Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines).
The project does not currently operate a separate Code of Conduct or private conduct-report
process.
