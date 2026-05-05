---
layout: post
title: "Emulating the Terraform Release Registry for OpenTofu"
description: "After the HashiCorp fork, Go and other language SDKs that depended on the Terraform version registry had no migration path. A minimal static emulation proved it was achievable and unblocked the community."
date: 2023-11-01
tags: [Open Source, Infrastructure, SDK / API, Go]
permalink: /blog/opentofu-registry/
---

## Background: the fork and the registry problem

In August 2023, HashiCorp relicensed Terraform from the Mozilla Public License to the
Business Source License (BSL). Shortly after, the OpenTofu project forked Terraform
under the Linux Foundation to maintain an open-source path forward.

Switching the binary was the easy part. The harder problem was the surrounding
**ecosystem of SDKs and tooling** that had grown up around Terraform's
release infrastructure. Clients written in Go, Python, and other languages often relied
on a predictable registry URL structure to:

- List available versions
- Resolve the latest stable / beta / alpha release
- Construct download URLs for the correct platform and architecture
- Verify checksums before installation

When a Go SDK (or a Terragrunt wrapper, or a custom installer) pointed at
`releases.hashicorp.com/terraform/...`, that URL wasn't going anywhere, but
OpenTofu releases were landing on GitHub Releases, not on a Terraform-compatible
registry. The two formats were different enough to break SDK integrations.

## The question the community needed answered

> "How hard is it to replicate the Terraform release index format for OpenTofu?
> Is it something the community can realistically maintain?"

My goal was to answer that question concretely, not theoretically. The fastest way to
do that was to build it.

## What the Terraform registry format looks like

The HashiCorp release registry is deceptively simple. At its core it is a set of
static HTML pages, a root index and per-version child pages, with a predictable
URL structure:

```
releases.hashicorp.com/terraform/
├── index.html           # lists all versions
├── 1.6.0/
│   └── index.html       # lists all artifacts for that version
├── 1.5.7/
│   └── index.html
└── ...
```

Each child page links to the actual build artifacts: zip files, checksums, and
signature files hosted separately. The SDKs parse these pages (or a JSON variant)
to resolve which URL to fetch for a given OS and architecture.

No API authentication, no dynamic server, no database. A glorified directory listing.

## The implementation

I wrote a small Python script that hit the GitHub Releases API for the
`opentofu/opentofu` repo, iterated every release, and generated the
equivalent static HTML structure. The output was a root `index.html` plus
one directory per version, each containing an `index.html` linking to
the corresponding GitHub Release assets.

The generated site was hosted on GitHub Pages under this domain, making it a live,
inspectable proof-of-concept that anyone could examine and fork.

Key observations from the exercise:

- The Terraform registry format requires **no dynamic infrastructure**.
  A static site generator or a simple script is sufficient.
- GitHub Releases already provides everything needed: version names, asset file names,
  checksums (`SHA256SUMS`), and signatures. The registry is just a
  structured index on top of those.
- The main compatibility risk is SDKs that hard-code the file naming convention
  (`terraform_X.Y.Z_os_arch.zip` vs `tofu_X.Y.Z_os_arch.zip`).
  The registry can paper over the URL structure but the binary name change still
  requires SDK-level changes.

## Impact

The working emulation gave SDK authors and community contributors something concrete
to point to: a live URL demonstrating the registry format was reproducible and
maintainable without any HashiCorp infrastructure. It lowered the perceived barrier
to migration and provided a reference implementation to adapt.

OpenTofu has since grown a proper release infrastructure of its own. This proof of
concept served its purpose, unblocking early adopters while the upstream ecosystem
caught up.

## Takeaways

- **Concrete beats theoretical.** The community didn't need a design doc. It needed a
  URL to click on. Build the thing.
- **Understand your dependencies' dependencies.** The issue wasn't
  "OpenTofu vs Terraform". It was: what does the SDK use to find the binary?
  Tracing that dependency chain is often where the real work is.
- **Static is underrated.** A surprising amount of "infrastructure"
  that looks like it needs a server is really just a structured set of files.

---

The original generated registry is still live at [/opentofu/](/opentofu/) if you want
to browse the structure. The generator script is at
[opentofu/main.py](https://github.com/nitrocode/nitrocode.github.io/blob/main/opentofu/main.py).
