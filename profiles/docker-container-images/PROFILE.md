# Technology Profile: Docker Container Images

## Metadata

- **ID:** `docker-container-images`
- **Status:** draft
- **Supported versions:** Dockerfile syntax 1.x with BuildKit; verify the minimum implementation version of every feature the project uses
- **Last reviewed:** `2026-08-26`
- **Primary sources:** [Docker build contexts](https://docs.docker.com/build/concepts/context/), [build best practices](https://docs.docker.com/build/building/best-practices/), [multi-stage builds](https://docs.docker.com/build/building/multi-stage/), [Dockerfile reference](https://docs.docker.com/reference/dockerfile/), [build inputs](https://docs.docker.com/build/policies/inputs/), [build secrets](https://docs.docker.com/build/building/secrets/), [build checks](https://docs.docker.com/reference/build-checks/), [image push](https://docs.docker.com/reference/cli/docker/image/push/), and [OCI image annotations](https://github.com/opencontainers/image-spec/blob/v1.1.1/annotations.md)

## Scope

This profile specializes the core rules for [ignore and packaging boundaries](../../docs/security-and-reproducibility.md#ignore-and-packaging-boundaries), [dependencies and third-party material](../../docs/security-and-reproducibility.md#dependencies-and-third-party-material), [reproducible and safe builds](../../docs/security-and-reproducibility.md#reproducible-and-safe-builds), and [proportional quality gates](../../docs/engineering-and-releases.md#proportional-quality-gates).

This profile covers a project-owned Dockerfile image from its selected build context through
the built image and, for publication tasks, its registry-reported digest. Its decisions
protect bounded inputs, controlled external image resolution, least final-image contents
and privilege, safe build-secret handling, verifiable image configuration, and traceable
published identity. It stops at the image boundary and does not define application behavior
or policy for running the image.

## Applicability and detection

Strong signals include:

- a `Dockerfile`, `Dockerfile.*`, or `*.Dockerfile` that builds a project-owned image;
- `.dockerignore` or Dockerfile-specific ignore files;
- committed Docker build configuration;
- CI or release configuration that builds or publishes the image.

The profile also applies when an explicit task introduces a project-owned Dockerfile image.
In every case, the task must affect its build context, Dockerfile, selected target, built
image, image-specific checks, or published identity.

A Dockerfile used only as an example, a documentation mention, or configuration that only
pulls third-party images is not enough to apply the profile. When several Dockerfiles or
targets exist, establish which one the current task affects before changing shared stages
or verification.

## Decisions

### Bound the build context

**Applies when:** a maintained Dockerfile build receives a local or named context.

**Required outcome:** the selected build receives only reviewed inputs needed by its
Dockerfile and target, protecting private-data exclusion, reviewability, and predictable
input resolution.

**Recommended default:** use the narrowest practical build context and maintain a reviewed `.dockerignore`. Treat it as a separate boundary from `.gitignore`: a Git exclusion does not stop Docker from receiving a file. When Dockerfiles need materially different inputs, use [Dockerfile-specific ignore files](https://docs.docker.com/build/concepts/context/#filename-and-location).

**Unsafe patterns:** sending credentials, local state, VCS metadata, logs, databases, downloaded artifacts, or unrelated source to the builder; assuming `.gitignore` protects the context.

**Migration:** inventory every `COPY`, `ADD`, and build-mounted input; add exclusions without hiding required inputs; then build from a clean checkout.

### Control external image inputs

**Applies when:** `FROM` or image-based `COPY --from` resolves an external image.

**Required outcome:** each external image has a reviewed origin and auditable resolved
identity while remaining maintainable for security updates.

**Recommended default:** use trusted, maintained images for external inputs such as `FROM` and image-based `COPY --from`. Pin release inputs by digest and pair each pin with a documented update path and regular rebuilds. Docker documents both the repeatability benefit and update obligation of [base-image digest pins](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions).

**Acceptable alternative:** a maintained version tag plus a fresh pull favors updates over exact repeatability. Record the resolved digest so the build remains auditable.

**Unsafe patterns:** an unexplained `latest` image in a release build or an old digest pin with no update route.

**Migration:** resolve each external image input to a reviewed digest, add an update route, rebuild, and compare behavior. Do not preserve a vulnerable input merely to keep a build repeatable.

### Separate build and runtime contents

**Applies when:** the build uses source, tests, compilers, package managers, or other
material not required by the selected final target.

**Required outcome:** the built final image contains only artifacts and runtime contents
required by its documented image contract.

**Recommended default:** use named [multi-stage builds](https://docs.docker.com/build/building/multi-stage/) when they keep compilers, package managers, source, tests, or other build-only material out of the final image. Copy explicit required artifacts into a trusted runtime base and inspect the built result.

Choose a maintained runtime base that satisfies the image's verified runtime requirements.

**Acceptable alternative:** a single stage is reasonable when it introduces no build-only material and the final image remains minimal for its documented contract.

**Unsafe patterns:** copying an entire builder filesystem; leaving build-only tools, credentials, test fixtures, or other unnecessary files in the final image; assuming multiple stages make the final stage safe without inspection.

**Migration:** identify the exact final target and its required artifacts, move build-only work into named earlier stages, then rebuild and inspect the final image.

### Set the final-image user

**Applies when:** the selected final target defines an application execution environment.

**Required outcome:** the image declares the least-privileged identity compatible with its
verified file access and application contract.

**Recommended default:** set a dedicated non-root
[`USER`](https://docs.docker.com/reference/dockerfile/#user) in the final image and make
required files usable by that identity.

**Acceptable exception:** an image may require root when the application contract proves
it. Document that requirement and test the effective identity.

**Unsafe patterns:** an unexplained root default or files the configured user cannot use.

**Migration:** fix ownership, switch to the intended user, then run the built image and
verify its identity and required file access.

### Define final-image health only when meaningful

**Applies when:** the final image is long-running or inherits a `HEALTHCHECK`.

**Required outcome:** the built image has a bounded local health signal that describes the
final image, or explicitly has no health check.

**Recommended default:** define
[`HEALTHCHECK`](https://docs.docker.com/reference/dockerfile/#healthcheck) for a long-running
image with a meaningful local signal. Replace or disable an inherited check when it does
not describe the final image.

**Acceptable alternative:** omit health configuration for a one-shot image or when no
meaningful local signal exists.

**Unsafe patterns:** health checks that expose credentials, mutate state, or depend on
unrelated external services.

**Migration:** replace or disable an inherited check, then run the image and verify the
resulting Docker health state when health is part of its contract.

### Keep build credentials out of image data

**Applies when:** the selected build requires a credential or private key.

**Required outcome:** sensitive input is absent from the build context, Dockerfile
arguments and environment, exported layers and configuration, and ordinary build logs.

**Recommended default:** pass credentials through BuildKit
[secret or SSH mounts](https://docs.docker.com/build/building/secrets/) for the shortest
required instruction. A build command can still copy or print mounted data, so inspect
outputs and logs.

**Unsafe patterns:** using `ARG` or `ENV` as a secret channel; copying a secret and deleting
it in a later layer; assuming a clean final Dockerfile section proves copied artifacts
contain no credentials.

**Migration:** remove the persistent secret channel, rotate credentials that may have been
exposed, rebuild without them, and inspect the resulting image and logs.

### Assess the intended final image

**Applies when:** the task builds or changes a maintained final image.

**Required outcome:** image-specific smoke and vulnerability checks evaluate the intended
final target, and missing project checks are visible rather than silently replaced with an
agent-selected dependency.

**Recommended default:** run the repository's credential-free image smoke check and its
configured image scanner, record the scanner data currency, and triage findings.

**Acceptable alternative:** when either check is absent, report the exact coverage gap and
require a separate project decision before introducing a new tool or external service.

**Verification:** the smoke result and scanner report identify the exact locally built
image; scanner findings have recorded dispositions rather than an unqualified pass claim.

This decision specializes the core [proportional quality-gate](../../docs/engineering-and-releases.md#proportional-quality-gates)
property; individual scanner behavior remains owned by the project's selected tool.

### Publish an identifiable image

**Applies when:** the authorized task publishes a project-owned image.

**Required outcome:** consumers can relate the source revision and human version to the
exact registry artifact that was published.

**Recommended default:** publish human-readable version tags and record the
[registry-reported digest](https://docs.docker.com/reference/cli/docker/image/push/) for
the published reference. Treat `latest` and other moving tags as pointers, not immutable
release identities.

Use applicable standard
[`org.opencontainers.image.*`](https://github.com/opencontainers/image-spec/blob/v1.1.1/annotations.md)
keys for metadata the project actually owns. Verify labels from the built image rather
than assuming Dockerfile text reached the intended target.

**Unsafe patterns:** recording only a mutable tag when exact artifact identity matters, moving a versioned release tag to unrelated content, or hard-coding stale version metadata.

**Migration:** preserve the existing human-facing tags, add applicable standard labels, and capture the registry-reported digest after publication.

## Verification recipe

Use the repository's documented equivalents when they exist; they own exact filenames, targets, and smoke commands.

Prerequisites: a local Docker environment with BuildKit support. Building and scanning may use the network. If the selected build requires credentials, external services, or special hardware, report that prerequisite. Before running a repository smoke or scanner command, identify any containers, processes, files, caches, or other state it creates and its targeted cleanup. If those effects cannot be bounded, report the gap instead of running it. The baseline performs no publication or destructive cleanup.

1. Inspect the Dockerfile, applicable ignore file, build context, and intended final target. This step is read-only.
2. Run the repository's configured static Dockerfile check. When the installed CLI supports
   [build checks](https://docs.docker.com/reference/build-checks/) and the default
   `Dockerfile` with context `.` is the documented target, run:

   ```bash
   docker build --check .
   ```

   If no applicable static check is available, report the gap instead of selecting a new
   project dependency.
3. If the default `Dockerfile` and context `.` are the documented target and need no
   additional inputs, run:

   ```bash
   docker build --tag profile-check:local .
   ```

   Otherwise, derive a local command from the repository's documented build by preserving
   its Dockerfile, context, target, and required inputs while replacing every publication
   or external output with the local-only tag. Pass any authorized build credentials only
   through the documented BuildKit secret or SSH mounts. Building executes
   repository-controlled code.
4. Inspect the built image without starting it:

   ```bash
   docker image inspect profile-check:local \
     --format '{{json .Config.User}} {{json .Config.Healthcheck}} {{json .Config.Labels}}'
   ```

   When investigating possible build-argument or deleted-secret leakage, inspect image history locally because it may expose sensitive values.
5. Run the repository's credential-free image smoke test. When health is part of the image contract, verify that the built image reaches the expected Docker health state. If no suitable test exists, report the gap.
6. Run the repository's configured scanner against `profile-check:local`, record when its vulnerability data was current, and triage findings. If no scanner is configured, report the gap instead of selecting a new project dependency outside the task scope.

These commands leave the local image and build data in place and perform no cleanup.

## Composition

This profile owns the Docker build boundary, Dockerfile decisions, final image, and
image-specific verification. For an authorized publication task, it also owns the handoff
from that built image to its registry-reported digest. Use the
[general composition rules](../README.md#precedence-and-composition) for everything else.

## Evidence and maintenance

This draft was checked against the primary Docker and OCI annotation sources listed in its metadata on `2026-08-26`. It does not claim representative-project validation or `recommended` status.

Review it when a referenced Docker feature changes, an official source is superseded, or focused project validation exposes guidance that is unsafe, unclear, or too broad. Promotion to `recommended` requires a separate change with the evidence required by the profile lifecycle.
