# Governance

This project accepts public participation while keeping acceptance and publication
authority with a small, accountable maintainer group.

## Roles

### Contributors

Anyone may report a problem, propose a change, review public work, or submit a pull request
under [the contribution guide](CONTRIBUTING.md). Contribution does not grant authority to
accept scope, merge changes, publish releases, change settings, or speak for the project.

### Maintainers

Maintainers are equal peers responsible for the repository's overall quality and public
boundary. They may accept proposal scope, review and merge changes, moderate community
surfaces, publish releases, and administer repository settings under the documented rules.

Current maintainers:

- [@suremule56-boop](https://github.com/suremule56-boop)

Maintainer access requires two-factor authentication and reliable recovery access. Agents
may prepare or mechanically apply authorized work, but they are never maintainers and
cannot supply human approval.

## Decisions and review

An ordinary change requires passing checks, resolved review conversations, and one
maintainer approval. A consequential change to authority, security boundaries, adoption
defaults, repository-wide architecture, or maintainer memory also requires an accepted
proposal, a decision record when specified by `AGENTS.md`, and:

- affirmative acceptance from two maintainers when at least two active maintainers exist;
  a maintainer author's proposal counts as one, but at least one non-author approving
  review is required; and
- no unresolved maintainer objection.

While only one maintainer exists, that maintainer may self-review and use the documented
administrator bypass. Substantive self-authored work still goes through a public pull
request so checks, reasoning, and the bypass remain visible. Direct pushes are reserved for
narrow corrections and urgent recovery.

Passing automation is evidence, not acceptance. Maintainers may decline a technically
valid contribution when it is out of scope, duplicates existing guidance, lacks durable
ownership, or costs more to review and maintain than its cross-project value justifies.

## Adding and removing maintainers

Maintainer access is granted by a pull request updating this file and `.github/CODEOWNERS`;
repository permissions change only after that pull request is accepted. Existing
maintainers consider sustained useful participation, review judgment, understanding of
project boundaries, respectful collaboration, security hygiene, and willingness to own
long-term maintenance. No contribution count or agent-generated nomination grants access
automatically.

When several maintainers are active, adding or involuntarily removing a maintainer requires
approval from every other active maintainer and no unresolved objection. A maintainer may
step down immediately by request. Access may be suspended promptly when an account or the
repository is at credible security risk, with the reason documented publicly when doing so
is safe.

Inactive maintainers should move out of the active list through an ordinary reviewed
change. Inactivity alone is not misconduct and does not erase contribution history.

## Delegation

If issue volume later justifies help, a trusted contributor may receive GitHub's `Triage`
role to label, assign, and close issues without repository write access. Triage does not
grant proposal-acceptance, merge, release, or settings authority. Do not create additional
roles until real workload requires them.

## Reconsidering governance

Change this model through a public proposal and a new decision record. Keep governance
proportional to actual participation rather than copying committee structures from larger
projects.
