# klatt42 Business-Ops Skills

A curated, redistributable collection of Claude skills and plugins focused on **business operations for small businesses and operators** — the Cowork-native counterpart to Anthropic's public [legal](https://github.com/anthropics/skills) and [finance](https://github.com/anthropics/skills) skill repos.

Everything in this repo originates from Anthropic's `knowledge-work-plugins` marketplace inside Cowork. All included content is Apache-2.0 licensed and redistributed here with attribution preserved (see `LICENSE` and `NOTICE`).

## Why this repo exists

Cowork ships with a strong set of business-operations skills (marketing, brand, internal comms, scheduling, design, plus a deeper `small-business`, `operations`, and `customer-support` plugin family). Unlike the legal and finance plugins, these don't currently have a dedicated public source repo. This repo collects them into one place so you can:

- Browse, fork, and customize each skill outside Cowork
- Use the skills in Claude Code, the Agent SDK, or your own MCP setup
- Pin a stable copy of skills you depend on
- Add your own business-specific overrides on top

## Layout

This mirrors the [`anthropics/skills`](https://github.com/anthropics/skills) repo convention: one folder per skill at the top level, each containing a `SKILL.md` plus any supporting files.

```
klatt42-business-ops-skills/
├── skills/                       # Standalone skills (Apache-2.0)
│   ├── brand-guidelines/         # Anthropic brand colors/typography styling
│   ├── canvas-design/            # Visual poster/art creation in .png/.pdf
│   ├── internal-comms/           # Status reports, leadership updates, FAQs, etc.
│   ├── schedule/                 # Create or update scheduled tasks
│   ├── theme-factory/            # 10 pre-set themes for slides/docs/HTML
│   ├── docx/                     # Word document creation/editing
│   ├── xlsx/                     # Excel spreadsheet handling
│   ├── pdf/                      # PDF processing, forms, merge/split
│   └── pptx/                     # PowerPoint deck creation/editing
│
├── plugins/
│   └── marketing/                # Full plugin: 7 commands + 8 skills
│       ├── .claude-plugin/plugin.json
│       ├── README.md
│       ├── CONNECTORS.md
│       ├── LICENSE
│       └── skills/
│           ├── brand-review/
│           ├── campaign-plan/
│           ├── competitive-brief/
│           ├── content-creation/
│           ├── draft-content/
│           ├── email-sequence/
│           ├── performance-report/
│           └── seo-audit/
│
└── catalog/                      # Plugins not yet extracted to source
    ├── small-business.md         # 30+ skills — install to pull files locally
    ├── operations.md             # 9 skills — install to pull files locally
    └── customer-support.md       # 5 skills — install to pull files locally
```

## What's included

### Standalone skills (`/skills`)

| Skill              | Purpose                                                                       |
| ------------------ | ----------------------------------------------------------------------------- |
| `brand-guidelines` | Apply Anthropic's official brand colors and typography to any artifact        |
| `canvas-design`    | Create visual art in `.png` and `.pdf` using a design-philosophy approach     |
| `internal-comms`   | Write status reports, leadership updates, 3P updates, FAQs, incident reports  |
| `schedule`         | Create or update scheduled tasks ("every morning", "weekly", "in an hour")    |
| `theme-factory`    | Apply one of 10 curated themes (colors + fonts) to any artifact               |
| `docx`             | Create, read, and edit Word documents — reports, memos, letters, templates    |
| `xlsx`             | Create, edit, and analyze Excel spreadsheets — budgets, models, charts        |
| `pdf`              | Extract text/tables, fill forms, merge/split, OCR, watermark PDFs             |
| `pptx`             | Create and edit slide decks — pitch decks, presentations, templates           |

### Marketing plugin (`/plugins/marketing`)

A complete plugin with seven slash-commands and supporting skills:

| Command               | What it does                                                                  |
| --------------------- | ----------------------------------------------------------------------------- |
| `/draft-content`      | Blog posts, social, newsletters, landing pages, press releases, case studies  |
| `/campaign-plan`      | Full campaign brief — objectives, channels, content calendar, success metrics |
| `/brand-review`       | Review content against brand voice, style guide, and messaging pillars        |
| `/competitive-brief`  | Research competitors, generate positioning and messaging comparison           |
| `/performance-report` | Marketing performance report with KPIs, trends, optimization recommendations  |
| `/seo-audit`          | Keyword research, on-page analysis, content gaps, technical checks            |
| `/email-sequence`     | Multi-email nurture, onboarding, drip, win-back, launch sequences             |

### Cataloged but not yet extracted (`/catalog`)

These three Cowork plugins live in the `knowledge-work-plugins` marketplace but aren't installed locally yet, so the source files haven't been copied into this repo. Each catalog file documents every skill the plugin provides plus a one-line install command. Once installed in Cowork, the plugin files appear under `~/.../local-agent-mode-sessions/.../remote-plugins/<plugin_id>/` and you can copy them into `/plugins/<name>` to bring them into this repo.

| Plugin             | Skills | Focus                                                                          |
| ------------------ | -----: | ------------------------------------------------------------------------------ |
| `small-business`   |    30+ | SMB workflows: cash flow, month-end, CRM, invoice chasing, hiring, tax prep    |
| `operations`       |      9 | Vendor reviews, runbooks, RACI/SOPs, risk, compliance, capacity, status        |
| `customer-support` |      5 | Ticket triage, response drafts, KB articles, escalations, customer research    |

## Installation

### As Cowork plugins

If you just want to use these in Cowork or Claude Code, install the plugins directly from the marketplace:

```bash
claude plugins add knowledge-work-plugins/marketing
claude plugins add knowledge-work-plugins/small-business
claude plugins add knowledge-work-plugins/operations
claude plugins add knowledge-work-plugins/customer-support
```

### As standalone skills

Copy any folder from `/skills` into your Claude skills directory (e.g. `~/.claude/skills/` for Claude Code, or your project's `.claude/skills/` folder). Each `SKILL.md` has YAML frontmatter that Claude reads to know when to activate the skill.

## Adding your own business skills

This repo is set up so you can layer Klatt42-specific overrides on top of the Anthropic baseline. Common patterns:

1. **Brand voice fork** — copy `plugins/marketing/skills/brand-review` to a new folder and edit `SKILL.md` to encode your brand's voice attributes, do/don't terminology, and required disclaimers.
2. **SOP library** — add a new top-level skill folder per recurring SOP (vendor onboarding, monthly close, weekly newsletter). Use `internal-comms` and `operations:runbook` as templates.
3. **Customer-specific playbooks** — fork `customer-support:draft-response` per customer segment.

## License & attribution

All content is Apache-2.0, originally authored by Anthropic. See:

- `LICENSE` — Apache License 2.0
- `NOTICE` — required attribution
- Per-skill `LICENSE.txt` files preserved from the upstream

Modifications by Ron Klatt (klatt42) are also Apache-2.0.

## Sources

- Marketing plugin and skills: bundled with Cowork (`knowledge-work-plugins/marketing`)
- Standalone skills: shipped with Cowork at `~/AppData/Roaming/Claude/.../skills-plugin/skills/`
- Catalog entries: inventoried from the Cowork plugin registry on 2026-05-25
