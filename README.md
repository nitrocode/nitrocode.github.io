# nitrocode.github.io

Personal portfolio site for [nitrocode](https://nitrocode.github.io) — Full Stack Engineer.

## Site structure

| Path | Description |
|------|-------------|
| `/` | Landing page — hero, five-pillar skills grid, AI angle |
| `/about/` | Background and career arc |
| `/blog/` | Case studies and engineering deep-dives |
| `/blog/opentofu-registry/` | Case study: emulating the Terraform release registry for OpenTofu |
| `/projects/` | Notable projects and open-source contributions |
| `/resume/` | Print-friendly résumé |
| `/opentofu/` | Legacy: static OpenTofu version registry emulation |

## Tech

Plain HTML + [Tailwind CSS CDN](https://tailwindcss.com/docs/installation/play-cdn). No build step — hosted on GitHub Pages.

## OpenTofu registry

The `opentofu/` directory is a generated static emulation of the Terraform version registry,
created to demonstrate that the format was simple enough to replicate for the OpenTofu community.
The generator script is at [`opentofu/main.py`](opentofu/main.py).
