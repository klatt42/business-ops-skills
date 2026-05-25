#!/usr/bin/env bash
# push-to-github.sh
# Run this from bash/zsh/git-bash in the klatt42-business-ops-skills folder.
# Prereq: `gh auth status` shows you're logged in as klatt42.
set -euo pipefail

if [ ! -f README.md ]; then
  echo "Run this from inside the klatt42-business-ops-skills folder." >&2
  exit 1
fi

# The sandbox left a partial .git directory — wipe and start clean
if [ -d .git ]; then
  echo "Removing stale .git directory..."
  rm -rf .git
fi

git init -b main
git config user.email "klatt42@gmail.com"
git config user.name  "Ron Klatt"

git add -A
if ! git diff --cached --quiet; then
  git commit -m "Initial commit: extract Cowork business-ops skills and marketing plugin

- Marketing plugin (8 skills, Apache-2.0)
- Standalone Anthropic skills (Apache-2.0): brand-guidelines, canvas-design,
  internal-comms, schedule, theme-factory, docx, xlsx, pdf, pptx
- Catalog entries for small-business, operations, customer-support plugins"
fi

# Change --public to --private if you'd rather keep it private.
gh repo create klatt42/business-ops-skills \
  --public \
  --source=. \
  --remote=origin \
  --description "Cowork business-ops skills and plugins (marketing, internal comms, scheduling, brand, design) extracted for personal use and customization. Apache-2.0." \
  --push

gh repo view klatt42/business-ops-skills --web
