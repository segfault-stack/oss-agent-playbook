# Security and Reproducibility

## Secrets and private data

Treat a committed credential as compromised. Remove it from the public material and rotate it; deleting the current file does not invalidate copies or Git history.

Inspect the working tree, ignored and untracked files, retained history, documentation, examples, fixtures, logs, screenshots, binaries, archives, build contexts, packages, and CI artifacts as applicable. Secret scanners supplement manual review; they do not replace it.

Do not publish real environment values, tokens, passwords, keys, certificates, sessions, cookies, production dumps, user content, credential-bearing logs, private endpoints, or operator-specific data. Use unmistakably non-functional placeholders such as `replace-with-a-secret`.

Review for personal and tenant identifiers, internal domains and addresses, private repository URLs, analytics IDs, production-derived test data, and screenshots containing names, conversations, filenames, or timestamps.

## History and publication

If private history contains credentials, personal data, obsolete internal work, large artifacts, or code that cannot be redistributed, consider publishing an independently verified clean snapshot in a fresh repository. If history is retained, scan all of it and preserve required attribution.

## Ignore and packaging boundaries

Ignore rules should cover the state the project actually creates: local configuration, credentials, caches, build and test output, logs, databases, dumps, uploads, archives, editor files, and temporary data as appropriate.

Git ignore rules do not protect build contexts, images, packages, archives, caches, or CI artifacts. Define and test exclusions at each boundary.

## Dependencies and third-party material

Use the ecosystem's established lock mechanism when available. Keep manifests and locks synchronized, separate runtime and development dependencies, and pin external tools and base environments to intentional versions when reproducibility or integrity depends on them.

Review automated dependency changes like any other code change: determine exposure, inspect transitive effects, and run relevant verification. Avoid unbounded mutable dependencies unless accepting that update model is an explicit project decision.

For bundled code, assets, fonts, templates, and snippets, verify licenses, preserve notices, distinguish upstream from local work, and pin revisions when needed. Do not imply endorsement through copied branding. The repository license must be compatible with distributed material; do not guess the maintainer's licensing intent.

## Reproducible and safe builds

A clean environment should be able to resolve dependencies, build, test, and package using committed instructions. Avoid undeclared machine state and production credentials. Keep build credentials out of durable layers, caches, logs, and artifacts.

Pin third-party CI components to reviewed immutable revisions when practical. Validate that a release artifact corresponds to its tag and does not fetch executable code from a mutable default branch.

Checksums establish artifact integrity, not publisher identity. Add signatures, provenance, or a software bill of materials only when the release process can generate and verify them consistently; do not claim supply-chain guarantees from unused files or badges.
