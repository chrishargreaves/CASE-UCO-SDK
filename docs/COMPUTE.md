# Compute and Platform Support

This document is the SDK source of truth for deployment sizing and CPU
architecture support. Downstream deployment catalogs should copy these values
rather than infer requirements from developer CI runners.

## Compute baseline

| Resource | Minimum | Recommended |
| --- | ---: | ---: |
| CPU | 4 cores | 8 or more cores for concurrent generation and validation |
| RAM | 8 GB | 16 GB; 32–64 GB for large in-memory graphs |
| GPU | Not required | Not required |
| VRAM | Not applicable | Not applicable |
| Application/database disk | 20 GB | 40 GB or more for build caches and generated artifacts |
| Evidence storage | Not included | Size separately for retention and replication requirements |

The application/database figure covers the SDK, language toolchains, package
caches, temporary validation data, and generated artifacts. It does **not**
cover source evidence, forensic images, exports, backups, or replicas. Those
must use separately governed storage sized for the deployment's evidence
volume and retention policy.

Installers and deployment catalogs that list the SDK should keep their
compute entry synchronized with this baseline.

## CPU architecture matrix

| Package | Linux `x86_64` | Linux `aarch64` | Architecture-sensitive components |
| --- | --- | --- | --- |
| Python | Supported and CI-tested | CI-tested on GitHub `ubuntu-24.04-arm` | The SDK wheel is pure Python. `rdflib`, `jinja2`, and SDK code are architecture-neutral; CI installs `case-utils==0.18.0` on the arm64 runner. |
| C# | Supported and CI-tested on .NET 8 | CI-tested on GitHub `ubuntu-24.04-arm` with the .NET 8 `linux-arm64` SDK | `CaseUco` is managed IL and ships no native library. |
| Java | Supported and CI-tested on JDK 11+ | CI-tested on GitHub `ubuntu-24.04-arm` with Temurin 17 | The SDK JAR is architecture-neutral and contains no JNI library. |
| Rust | Supported and CI-tested | CI-tested on GitHub `ubuntu-24.04-arm` | Rust produces a native binary/library for the selected target. |

The repository does not currently publish container images and has no CUDA or
GPU runtime dependency. NVIDIA hardware does not accelerate ontology loading,
code generation, or SHACL validation unless a downstream application adds its
own GPU workload.

GitHub-hosted `ubuntu-24.04-arm` is the recorded Linux `aarch64` CI
evidence.
NVIDIA Spark remains unvalidated on this repository: this environment has
no Spark host, and NVIDIA hardware does not change ontology loading or
SHACL validation. Do not describe NVIDIA Spark as a release platform
until a completed host checklist from this document is recorded for it.

## Native validation checklist

Run from a recursive clone on the target host:

```bash
uname -m
python3 --version
dotnet --info
java -version
rustc -vV
make init
make generate
make test
make lint
make smoke
```

Record the host architecture, operating-system release, toolchain versions,
commands, test counts, failures, and any packages compiled from source. The
validation record must not contain case data or evidence; use only repository
T0 synthetic fixtures.
