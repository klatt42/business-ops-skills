# small-business plugin

**Marketplace:** `knowledge-work-plugins/small-business`
**Status in this repo:** cataloged only — not yet installed locally, so source files have not been extracted yet.

## Description

Pre-built small business workflows (payroll planning, month-end close, weekly briefs, growth campaigns) wired up to QuickBooks, PayPal, HubSpot, Docusign, Gsuite, O365, Canva, and other common SMB tools. Every step that touches money or customers requires owner approval.

## Install in Cowork / Claude Code

```bash
claude plugins add knowledge-work-plugins/small-business
```

After installation, the plugin files appear under your local Cowork plugins directory. To extract into this repo:

```bash
# Replace <plugin_id> with the actual id (find via `claude plugins list`)
cp -R ~/AppData/Roaming/Claude/.../remote-plugins/<plugin_id> ./plugins/small-business
```

## Skills (30+)

### Daily briefs & dashboards
- `monday-brief` — One-page Monday morning briefing: cash, sales, pipeline, week ahead, top three to-dos
- `friday-brief` — End-of-week pulse: revenue vs prior week, top sellers, wins and watches
- `business-pulse` — One-page cross-functional snapshot for SMB owners (cash from QB, sales from PayPal/Square, pipeline)
- `month-heads-up` — Runs on the 25th; 30-day cash-flow outlook, flags pre-month-end issues
- `quarterly-review` — Full QBR narrative (revenue/margin trends, customer health, opportunities/risks) as PDF or PPTX
- `smb-router` — The front door: routes vague or specific requests to the right SMB skill
- `smb-onboard` — Walks an SMB owner through connecting first two tools and running one recipe

### Cash flow & finance
- `cash-flow-snapshot` — Reads AR/AP, historical cash timing, fixed costs from QB/PayPal/Stripe/Square (or CSV) → 30-day outlook
- `plan-payroll` — Forecasts cash, ranks overdue invoices, stages PayPal reminders so owner can run payroll
- `invoice-chase` — Drafts overdue-invoice reminders matched to each customer's payment history and tone
- `month-end-prep` — Pre-close checklist: reconciles QB vs payment processors, flags uncategorized transactions
- `close-month` — Closes the month: reconciles QB vs processors, P&L narrative, exports close packet
- `tax-prep` — Quarterly estimated tax calc OR year-end 1099 prep → accountant handoff packet
- `tax-season-organizer` — Prepares tax-season materials framed as deliverables for the accountant (not tax advice)

### Sales & pricing
- `sales-brief` — Top/bottom sellers, seasonality patterns, 2-week content brief to push winners
- `price-check` — Margin-by-product table + three pricing scenarios for owner to see full financial picture
- `margin-analyzer` — Unit economics by product/service using PayPal merchant insights + QB cost data
- `call-list` — Top-5 leads worth calling today, talking points from email history, blocks calendar time
- `lead-triage` — Scores HubSpot leads by engagement, fit, urgency → ranked outreach list

### Marketing & content
- `content-strategy` — Analyzes sales data, layers in seasonality, produces 30-day prioritized content plan
- `run-campaign` — End-to-end marketing campaign: sales analysis → content brief → Canva assets → HubSpot send
- `canva-creator` — Takes an approved content brief, builds posting calendar + Canva designs for social

### Customer ops
- `customer-pulse` — PayPal disputes + HubSpot feedback + email sentiment + reviews → themes report
- `customer-pulse-check` — Synthesizes themes into top-3 fixable issues with drafted response templates
- `handle-complaint` — Pulls context, drafts response, suggests an operational fix
- `ticket-deflector` — Reads forwarded customer email, pulls order/refund status from PayPal, drafts response

### CRM
- `crm-maintenance` — Keeps HubSpot current from email/calendar context — contacts, deals, notes, follow-ups
- `crm-cleanup` — Scans HubSpot for stale deals, duplicate contacts, missing fields; fixes with owner approval

### Hiring & contracts
- `job-post-builder` — Full hiring packet: job post + structured interview guide with rubric + offer letter template
- `review-contract` — Plain-English contract review, severity-rated red flags, marked-up docx/PDF with redlines
- `contract-review` — Lightweight NDA/MSA/vendor review for SMBs without in-house legal
