# Technology Profile: Docker Container Images

## Metadata

- **ID:** `docker-container-images`
- **Status:** draft
- **Applies to:** repositories and tasks that build, test, inspect, or publish a project-owned application image from a Dockerfile
- **Supported versions:** Dockerfile syntax 1.x with BuildKit; verify the minimum implementation version of every feature the project uses
- **Last reviewed:** `2026-08-26`
- **Primary sources:** [Docker build contexts](https://docs.docker.com/build/concepts/context/), [build best practices](https://docs.docker.com/build/building/best-practices/), [multi-stage builds](https://docs.docker.com/build/building/multi-stage/), [Dockerfile reference](https://docs.docker.com/reference/dockerfile/), [build inputs](https://docs.docker.com/build/policies/inputs/), [build secrets](https://docs.docker.com/build/building/secrets/), [build checks](https://docs.docker.com/reference/build-checks/), [image push](https://docs.docker.com/reference/cli/docker/image/push/), and [OCI image annotations](https://github.com/opencontainers/image-spec/blob/v1.1.1/annotations.md)

## Scope

This profile specializes the core rules for [ignore and packaging boundaries](../../docs/security-and-reproducibility.md#ignore-and-packaging-boundaries), [dependencies and third-party material](../../docs/security-and-reproducibility.md#dependencies-and-third-party-material), [reproducible and safe builds](../../docs/security-and-reproducibility.md#reproducible-and-safe-builds), and [proportional quality gates](../../docs/engineering-and-releases.md#proportional-quality-gates).

This profile covers a project-owned Dockerfile image from its selected build context through the built image and its published digest. It stops at the image boundary and does not define application behavior or how the image is run.

## Applicability and detection

Strong signals include:

- a `Dockerfile`, `Dockerfile.*`, or `*.Dockerfile` that builds a project-owned image;
- `.dockerignore` or Dockerfile-specific ignore files;
- committed Docker build configuration;
- CI or release configuration that builds or publishes the image.

A Dockerfile used only as an example or a configuration that only pulls third-party images is not enough to apply the profile. When several Dockerfiles or targets exist, establish which one the current task affects before changing shared stages or verification.

## Decisions

### Bound the build context

**Property protected:** private-data exclusion, reviewability, and predictable build inputs.

**Recommended default:** use the narrowest practical build context and maintain a reviewed `.dockerignore`. Treat it as a separate boundary from `.gitignore`: a Git exclusion does not stop Docker from receiving a file. When Dockerfiles need materially different inputs, use [Dockerfile-specific ignore files](https://docs.docker.com/build/concepts/context/#filename-and-location).

**Unsafe patterns:** sending credentials, local state, VCS metadata, logs, databases, downloaded artifacts, or unrelated source to the builder; assuming `.gitignore` protects the context.

**Migration:** inventory every `COPY`, `ADD`, and build-mounted input; add exclusions without hiding required inputs; then build from a clean checkout.

### Control external image inputs

**Property protected:** repeatable input resolution and controlled security updates.

**Recommended default:** use trusted, maintained images for external inputs such as `FROM` and image-based `COPY --from`. Pin release inputs by digest and pair each pin with a documented update path and regular rebuilds. Docker documents both the repeatability benefit and update obligation of [base-image digest pins](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions).

**Acceptable alternative:** a maintained version tag plus a fresh pull favors updates over exact repeatability. Record the resolved digest so the build remains auditable.

**Unsafe patterns:** an unexplained `latest` image in a release build or an old digest pin with no update route.

**Migration:** resolve each external image input to a reviewed digest, add an update route, rebuild, and compare behavior. Do not preserve a vulnerable input merely to keep a build repeatable.

### Separate build and runtime contents

**Property protected:** least functionality and a reviewable final image.

**Recommended default:** use named [multi-stage builds](https://docs.docker.com/build/building/multi-stage/) when they keep compilers, package managers, source, tests, or other build-only material out of the final image. Copy explicit required artifacts into a trusted runtime base and inspect the built result.

Choose a maintained runtime base that satisfies the image's verified runtime requirements.

**Acceptable alternative:** a single stage is reasonable when it introduces no build-only material and the final image remains minimal for its documented contract.

**Unsafe patterns:** copying an entire builder filesystem; leaving build-only tools, credentials, test fixtures, or other unnecessary files in the final image; assuming multiple stages make the final stage safe without inspection.

**Migration:** identify the exact final target and its required artifacts, move build-only work into named earlier stages, then rebuild and inspect the final image.

### Set the final-image user and health check

**Property protected:** least privilege and a usable Docker health signal.

**Recommended default:** set a dedicated non-root `USER` in the final image and make required files usable by that identity.

Define `HEALTHCHECK` only for a long-running image with a meaningful local health signal; one-shot images may omit it. Replace or disable an inherited health check when it does not describe the final image, and verify the resulting Docker health status.

**Acceptable exception:** an image may require root when the application contract proves it. Document that requirement and test the effective identity.

**Unsafe patterns:** an unexplained root default; files the configured user cannot read; health checks that expose credentials, mutate state, or depend on unrelated external services.

**Migration:** fix ownership, switch to the intended user, then run the built image and verify its identity and health behavior.

### Publish an identifiable image

**Property protected:** source traceability and exact consumer identity.

**Recommended default:** publish human-readable version tags and record the registry-reported digest for the published reference. Treat `latest` and other moving tags as pointers, not immutable release identities.

Use applicable standard `org.opencontainers.image.*` keys for metadata the project actually owns. Verify labels from the built image rather than assuming Dockerfile text reached the intended target.

**Unsafe patterns:** recording only a mutable tag when exact artifact identity matters, moving a versioned release tag to unrelated content, or hard-coding stale version metadata.

**Migration:** preserve the existing human-facing tags, add applicable standard labels, and capture the registry-reported digest after publication.

## Dependencies and reproducibility

External images are the Docker-specific dependencies governed by this profile. Apply the [core dependency rules](../../docs/security-and-reproducibility.md#dependencies-and-third-party-material) to all other build inputs.

## Project structure and configuration

Keep each maintained Dockerfile, its effective ignore file, context, and non-default final target discoverable together.

## Quality and CI

Image-specific checks should prove the final image, not only parse the Dockerfile:

1. statically check each maintained Dockerfile;
2. build the intended final target from a clean checkout;
3. inspect its configured user, health check, and labels;
4. run the repository's credential-free image smoke test;
5. scan the final image with the project's maintained vulnerability scanner and triage the result.

## Security

Follow the core rules for [secrets and private data](../../docs/security-and-reproducibility.md#secrets-and-private-data). The build context, intermediate stages, image history, logs, and exported image are separate leak surfaces.

- Pass build credentials through BuildKit [secret or SSH mounts](https://docs.docker.com/build/building/secrets/) for the shortest required instruction. A build command can still copy or print mounted data, so inspect outputs and logs.
- Never use `ARG` or `ENV` as a secret channel. Build arguments may appear in image history, and environment values may remain in the image configuration.
- Do not copy a secret and delete it in a later layer; the earlier layer still contains it.
- Review files copied from earlier stages; a clean final Dockerfile section does not prove copied artifacts contain no credentials.

## Packaging and releases

- Build the documented release target from the intended source revision.
- Record the source revision, human version, image tag, and published registry digest together.
- Verify after publication that the tag resolves to the recorded digest.

## Verification recipe

Use the repository's documented equivalents when they exist; they own exact filenames, targets, and smoke commands.

Prerequisites: a local Docker environment with BuildKit support. Building and scanning may use the network. If the selected build requires credentials, external services, or special hardware, report that prerequisite. The baseline performs no publication or destructive cleanup.

1. Inspect the Dockerfile, applicable ignore file, build context, and intended final target. This step is read-only.
2. If the default `Dockerfile` and context `.` are the documented target and it needs no additional inputs, run:

   ```bash
   docker build --check .
   docker build --tag profile-check:local .
   ```

   Otherwise, derive a local command from the repository's documented build by preserving its Dockerfile, context, target, and required inputs while replacing every publication or external output with the local-only tag. Pass any authorized build credentials only through the documented BuildKit secret or SSH mounts. Building executes repository-controlled code.
3. Inspect the built image without starting it:

   ```bash
   docker image inspect profile-check:local \
     --format '{{json .Config.User}} {{json .Config.Healthcheck}} {{json .Config.Labels}}'
   ```

   When investigating possible build-argument or deleted-secret leakage, inspect image history locally because it may expose sensitive values.
4. Run the repository's credential-free image smoke test. When health is part of the image contract, verify that the built image reaches the expected Docker health state. If no suitable test exists, report the gap.
5. Run the repository's configured scanner against `profile-check:local`, record when its vulnerability data was current, and triage findings. If no scanner is configured, report the gap instead of selecting a new project dependency outside the task scope.

These commands leave the local image and build data in place and perform no cleanup.

## Composition

This profile owns only the Docker build boundary, Dockerfile decisions, final image, and image-specific verification. Use the [general composition rules](../README.md#precedence-and-composition) for everything else.

## Evidence and maintenance

This draft was checked against the primary Docker and OCI annotation sources listed in its metadata on `2026-08-26`. It does not claim representative-project validation or `recommended` status.

Review it when a referenced Docker feature changes, an official source is superseded, or focused project validation exposes guidance that is unsafe, unclear, or too broad. Promotion to `recommended` requires a separate change with the evidence required by the profile lifecycle.
