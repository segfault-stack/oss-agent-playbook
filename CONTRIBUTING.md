# Contributing

Contributions are welcome when they make the playbook clearer, safer, more accurate, or easier to adopt across projects.

## Before proposing a change

1. Read `AGENTS.md` and the source-of-truth document for the rule you want to change.
2. Search existing issues and text for prior discussion, duplicates, and contradictions.
3. For technology-specific guidance, also follow `profiles/AGENTS.md` and start from the profile template.
4. Open an issue first when a proposal changes authorization boundaries, reverses a normative default, introduces a public promise, or affects several documents.

Small corrections, broken links, and unambiguous clarifications may go directly to a pull request.

## Change requirements

- Keep universal guidance independent of language, forge, CI vendor, and deployment platform.
- Put a rule in one source-of-truth document and link to it elsewhere.
- Support time-sensitive technical guidance with primary official sources.
- Separate verified behavior from assumptions, compatibility by contract, and roadmap ideas.
- Do not include credentials, private data, proprietary material, or production-derived examples.
- Keep changes focused and explain their effect on agents or maintainers.

By contributing, you agree that your contribution is dedicated under the repository's [CC0 1.0 Universal](LICENSE) terms.

## Verification

Run:

```bash
python3 scripts/check_docs.py
```

Then inspect the complete diff, rendered Markdown, and any changed external links. State checks that were not run or could not be reproduced.

## Pull requests

Describe the cross-project problem, the chosen rule or structure, evidence used, compatibility impact, and residual limitations. A pull request should not mix unrelated guidance or silently rewrite project policy.
