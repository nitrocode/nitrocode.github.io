# nitrocode.github.io

Personal portfolio site for [nitrocode](https://nitrocode.github.io), Full Stack Engineer.

## Site structure

| Path | Description |
|------|-------------|
| `/` | Landing page: hero, five-pillar skills grid, AI angle |
| `/about/` | Background and career arc |
| `/blog/` | Case studies and engineering deep-dives (auto-generated from `_posts/`) |
| `/blog/opentofu-registry/` | Case study: emulating the Terraform release registry for OpenTofu |
| `/blog/how-this-blog-is-built/` | Meta post: the full stack behind this site |
| `/projects/` | Notable projects and open-source contributions |
| `/resume/` | Print-friendly résumé |
| `/opentofu/` | Legacy: static OpenTofu version registry emulation |

## Tech

[Jekyll](https://jekyllrb.com) + [Tailwind CSS CDN](https://tailwindcss.com/docs/installation/play-cdn), hosted on GitHub Pages. No build pipeline. GitHub Pages runs Jekyll natively on push to `main`.

- **Layouts**: `_layouts/` (default, post, resume)
- **Includes**: `_includes/nav.html`, `_includes/footer.html`
- **Posts**: `_posts/*.md` with YAML front matter

## Adding a new blog post

Create `_posts/YYYY-MM-DD-post-slug.md` with front matter:

```yaml
---
layout: post
title: "Post Title"
description: "One-sentence summary shown in post cards."
date: YYYY-MM-DD
tags: [Tag One, Tag Two]
permalink: /blog/post-slug/
---
```

Write the post body in Markdown below the front matter. Commit and push. Done.

## OpenTofu registry

The `opentofu/` directory is a generated static emulation of the Terraform version registry,
created to demonstrate that the format was simple enough to replicate for the OpenTofu community.
The generator script is at [`opentofu/main.py`](opentofu/main.py).
