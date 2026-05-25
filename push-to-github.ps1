# push-to-github.ps1
# Run this from PowerShell in the klatt42-business-ops-skills folder.
# Prereq: `gh auth status` shows you're logged in as klatt42.

$ErrorActionPreference = "Stop"

# Sanity check
if (-not (Test-Path "README.md")) {
    Write-Host "Run this from inside the klatt42-business-ops-skills folder." -ForegroundColor Red
    exit 1
}

# The sandbox left a partial .git directory — wipe and start clean
if (Test-Path ".git") {
    Write-Host "Removing stale .git directory..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force ".git"
}

git init -b main
git config user.email "klatt42@gmail.com"
git config user.name  "Ron Klatt"

# Stage + commit
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Initial commit: extract Cowork business-ops skills and marketing plugin

- Marketing plugin (8 skills, Apache-2.0)
- Standalone Anthropic skills (Apache-2.0): brand-guidelines, canvas-design,
  internal-comms, schedule, theme-factory, docx, xlsx, pdf, pptx
- Catalog entries for small-business, operations, customer-support plugins"
}

# Create the GH repo + push (public by default — change --public to --private if you prefer)
gh repo create klatt42/business-ops-skills `
    --public `
    --source=. `
    --remote=origin `
    --description "Cowork business-ops skills and plugins (marketing, internal comms, scheduling, brand, design) extracted for personal use and customization. Apache-2.0." `
    --push

# Show the URL
gh repo view klatt42/business-ops-skills --web
