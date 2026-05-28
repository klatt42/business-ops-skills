# CLAUDE.md

Guidance for working on this repo. `klatt42/business-ops-skills` is a personal Claude Code plugin marketplace assembled from Anthropic's open-source plugins. Most work here is curating which plugins to extract, keeping `marketplace.json` in sync, and tuning the per-plugin practice profiles.

## What this repo is

A curated extraction of Anthropic's knowledge-work plugins for use across multiple Claude Code sessions and machines. The original `anthropics/knowledge-work-plugins` marketplace is registerable directly, but this fork exists to:

1. Pin a specific snapshot (immune to upstream churn).
2. Allow per-plugin practice-profile customization (see below).
3. Add operator-specific tooling (extra skills, custom plugins) without forking the upstream.

The marketplace is **public** and installable on any machine:

```bash
claude plugins marketplace add klatt42/business-ops-skills
claude plugins install <plugin>@business-ops-skills
```

## Layout

```
.claude-plugin/marketplace.json   # marketplace manifest — one entry per plugin
.githooks/pre-commit              # auto-bumps plugin.json version on staged changes
plugins/
  agent-plugins/                  # named workflow agents (empty — populated in Tier 3 if needed)
  vertical-plugins/               # 16 first-party plugins by vertical/function
    <plugin>/
      .claude-plugin/plugin.json  # plugin manifest (name, version, description, author)
      .mcp.json                   # MCP servers the plugin connects to (some plugins)
      CONNECTORS.md               # which connectors this plugin expects (some plugins)
      CLAUDE.md                   # practice-profile (small-business only so far)
      skills/<skill>/SKILL.md     # individual skills with YAML frontmatter + instructions
  partner-built/                  # 5 partner-contributed sub-plugins (each registered separately
                                  # in marketplace.json: apollo, brand-voice, common-room, slack, zoom)
skills/                           # 9 standalone Anthropic office skills
  <skill>/SKILL.md                # brand-guidelines, canvas-design, internal-comms, schedule,
                                  # theme-factory, docx, xlsx, pdf, pptx
scripts/
  check.py                        # validate marketplace.json, plugin.json, SKILL.md manifests;
                                  # also self-installs the git pre-commit hook
  version_bump.py                 # auto-patch-bumps plugin version on staged changes
LICENSE                           # Apache-2.0
NOTICE                            # attribution to Anthropic
README.md
```

Layout mirrors `anthropics/financial-services`: `agent-plugins` for named bundles, `vertical-plugins` for skill+command bundles, `partner-built` for vendor plugins.

## Plugins

The 17 plugins cover SMB ops, knowledge-work verticals (legal, finance, HR, sales, etc.), tech work (engineering, data, design), and 5 partner integrations (apollo, brand-voice, common-room, slack, zoom). See `marketplace.json` for the full list.

Explicitly excluded: `bio-research` (not relevant to the operator's customer base).

## Practice profile pattern

Anthropic's `claude-for-legal` and `financial-services` repos use a per-plugin `CLAUDE.md` that captures the operator's specific playbook (industry, tools, tone, approval gates). Every skill in the plugin reads this profile before doing substantive work, which customizes generic outputs to the operator's reality.

This repo applies the pattern selectively. Currently populated:

- `plugins/small-business/CLAUDE.md` — restoration services SMB profile (Prism Specialties DMV).

Future per-plugin profiles can be added as needed. The profile is read by Claude when invoking any skill in that plugin.

## Updating the repo

When extracting more plugins or refreshing existing ones from upstream:

```bash
# 1. Clone the source
git clone https://github.com/anthropics/knowledge-work-plugins /tmp/kwp

# 2. Copy first-party plugin into plugins/vertical-plugins/
#    (partner-built goes in plugins/partner-built/; named bundles in plugins/agent-plugins/)
cp -R /tmp/kwp/<plugin-name> plugins/vertical-plugins/<plugin-name>

# 3. Update marketplace.json if adding a new plugin
#    (jq filter: append to .plugins[] with name/displayName/source/description)
#    Source path: "./plugins/vertical-plugins/<name>" or "./plugins/partner-built/<name>"

# 4. Validate (also installs the pre-commit hook on first run)
python3 scripts/check.py

# 5. Stage by specific paths (NEVER git add -A on this repo from WSL —
#    drvfs creates ~70 false-positive "modified" files due to CRLF noise)
git add plugins/vertical-plugins/<plugin-name> .claude-plugin/marketplace.json
git commit && git push
# (pre-commit hook auto-bumps the plugin's version on staged changes)
```

## Drvfs gotcha (Windows / WSL)

This repo lives in Claude Desktop's Cowork output folder on the Windows filesystem:
`/mnt/c/Users/RonKlatt_3qsjg34/AppData/Roaming/Claude/local-agent-mode-sessions/<ids>/outputs/klatt42-business-ops-skills/`

When operating on it from WSL, the drvfs mount reports ~70 files as "modified" due to CRLF line-ending differences. These are NOT real changes. **Never `git add -A` on this working tree** — always stage specific paths. The original committed history is correct; only the working-tree view is noisy.

## Licensing

Everything in this repo is Apache-2.0. The root `LICENSE` and `NOTICE` attribute Anthropic for the upstream plugins. Per-plugin `LICENSE.txt` files inside `skills/<name>/` and `plugins/<name>/` are preserved from upstream. Operator-authored additions (e.g., per-plugin `CLAUDE.md` profiles) are also Apache-2.0 unless noted.
