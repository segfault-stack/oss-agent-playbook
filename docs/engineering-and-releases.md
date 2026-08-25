# Engineering and Releases

## Proportional quality gates

Automate the properties most likely to harm users or maintainers. Depending on the project, this can include:

- formatting and static analysis;
- unit, behavior, integration, and smoke tests;
- compilation, packaging, and configuration validation;
- dependency-lock and generated-file consistency;
- secret, dependency, artifact, and code security scanning;
- documentation and link checks;
- release artifact verification.

Keep local verification aligned with CI. Apply coverage requirements to meaningful behavior and public boundaries rather than maximizing a global number with low-value tests.

Default checks should be deterministic and should not require production credentials. Mock external systems for ordinary verification and separate network-dependent smoke tests. Schedule periodic vulnerability rescans when databases may change without a code change.

Name jobs after the property they verify and fail close to the cause. Turn checks into merge requirements only after their names and behavior have succeeded reliably.

## Main branch and changes

Once reliable CI exists, consider requiring review, stable checks, and non-destructive merge paths; preventing force-push and deletion; removing merged branches; and documenting a recovery route for a sole maintainer. Choose a merge strategy that matches the desired history.

Keep commits focused and explain user impact. Before pushing, inspect the exact diff and untracked files, run relevant verification, check for generated secrets or artifacts, and confirm the destination remote and branch. After pushing, compare local and remote revisions and inspect CI.

Repository setting changes and pushes are external mutations. Perform them only when the user's request authorizes them.

## External contribution controls

Treat contributor attention and CI capacity as bounded resources. When submission volume
justifies it, cap concurrent ready-for-review pull requests from users without write access
and maintain a narrow bypass list for proven contributors. Do not use collaborator access
only to bypass an intake limit.

Run untrusted fork changes with the minimum token permissions and without repository
secrets. Prefer the ordinary pull-request event for validation. Do not use a privileged
workflow event to check out and execute untrusted fork content. Require manual approval
before external workflows when jobs use costly infrastructure or other risk makes that
review worthwhile.

Automate deterministic intake properties such as required checks, document structure, and
changed-file consistency. Do not claim that generated-text detection, a completed template,
or a passing check proves human understanding or makes a contribution worth accepting.
Avoid bots that add repetitive failure narration or stale activity without reducing real
maintainer work.

## Releases

A release should refer to an immutable tag and communicate:

- honest stability status;
- user-visible changes;
- breaking changes and upgrade steps;
- known limitations and compatibility;
- versioned artifacts and their integrity information.

Verify that source revision, tag, remote commit, CI result, release metadata, and artifacts agree. Do not publish a stable version solely to obtain a convenient `latest` endpoint. Versioned installers must not silently execute content from a mutable branch.

## Operational changes

Before replacing a live deployment:

1. inventory services, configuration, and state;
2. create and verify a consistent backup;
3. preserve an explicit rollback path;
4. restore incompatible formats into isolated new state;
5. run migrations exactly as designed;
6. verify identity, authorization, configuration, and sessions;
7. run live smoke tests and observe health after an idle period;
8. remove temporary test data;
9. retain or delete rollback material through an explicit operator decision.

This sequence describes safety properties, not authorization. Do not touch a deployment unless the user has placed it in scope and the exact target is known.
