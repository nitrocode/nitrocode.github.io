---
layout: post
title: "How This Blog Is Built"
description: "The full stack behind nitrocode.github.io: plain HTML, Tailwind CSS CDN, GitHub Pages, and now Jekyll for Markdown-based blog posts. No complex build pipeline needed."
date: 2026-05-05
tags: [Meta, Frontend, GitHub Pages, Jekyll]
permalink: /blog/how-this-blog-is-built/
---

## The stack at a glance

| Layer | Choice | Why |
|-------|--------|-----|
| Hosting | GitHub Pages | Free, zero ops, auto-deploys on push to `main` |
| CSS | Tailwind CSS CDN | No build step; utility classes directly in HTML |
| Fonts | Google Fonts (Inter) | One `<link>` tag, no local assets |
| JavaScript | None (Tailwind config inline only) | No interactivity needed |
| Templates | Jekyll layouts + includes | Native GitHub Pages support, no CI workflow needed |
| Posts | Markdown (`_posts/*.md`) | Write content, push, done |

## Why no heavy framework

A personal portfolio has maybe six pages and changes a few times a year.
The overhead of a bundler, a dependency tree, a build command, and a deploy workflow
exists to solve problems this site does not have.

Plain HTML with Tailwind CDN means:

- Open any file in a browser directly from disk. No server needed to preview.
- Edit a line, commit, push. The site is live in under a minute.
- Zero supply chain surface. No `node_modules`, no lockfile drift, no CVEs in dev dependencies.
- The file you read is the file the browser receives. No source maps, no transpilation.

The tradeoff is duplication. The nav and footer are repeated across every page.
For six pages, that is a manageable cost. For blog posts, writing raw HTML for prose
is friction. That is where Jekyll helps.

## Tailwind CSS via CDN

Tailwind ships a CDN script that generates styles from utility classes at runtime.
It is not the production build path (that would require PostCSS and tree-shaking),
but for a low-traffic personal site with a handful of pages, the performance difference
does not matter.

The benefit is everything Tailwind offers: a consistent design system, dark-mode
utilities, responsive prefixes, and hover states, all without a config file or build step.

## GitHub Pages + Jekyll

Push to `main`. Done. GitHub Pages runs Jekyll natively, so no GitHub Actions workflow
is needed. The site builds on GitHub's servers and deploys automatically.

Jekyll adds two things:

1. **Layouts and includes**: Nav and footer live in `_includes/`. All pages share them
   via `{% raw %}{% include nav.html %}{% endraw %}`. No more copy-paste.
2. **Markdown posts**: Blog posts live in `_posts/*.md` with YAML front matter.
   Jekyll renders them through `_layouts/post.html`, which applies the Tailwind
   prose styles and page structure automatically.

Adding a new post is now just: create a `.md` file with front matter, commit, push.

## File structure

```
nitrocode.github.io/
├── _config.yml             # Jekyll site config
├── _includes/
│   ├── nav.html            # shared nav
│   └── footer.html         # shared footer
├── _layouts/
│   ├── default.html        # base HTML doc wrapper
│   ├── post.html           # blog post wrapper (extends default)
│   └── resume.html         # resume wrapper with print CSS (extends default)
├── _posts/
│   ├── 2023-11-01-opentofu-registry.md
│   └── 2026-05-05-how-this-blog-is-built.md
├── index.html              # / (front matter + body sections)
├── about/index.html        # /about/
├── blog/index.html         # /blog/ (auto-generates post cards via site.posts loop)
├── projects/index.html     # /projects/
├── resume/index.html       # /resume/
└── opentofu/               # static registry emulation (untouched)
```

## Lessons

- **Match the tool to the problem.** Six pages updated a few times a year
  do not justify a framework. But repeated nav copy-paste across every file
  justifies a template system.
- **Static is underrated.** No server, no database, no ops. A directory
  of files is a surprisingly capable publishing platform.
- **GitHub Pages runs Jekyll natively.** No CI workflow needed. Write a `.md` file,
  push, and the page is live. The "no build step" philosophy is preserved.

---

Source for this site is at
[github.com/nitrocode/nitrocode.github.io](https://github.com/nitrocode/nitrocode.github.io).
