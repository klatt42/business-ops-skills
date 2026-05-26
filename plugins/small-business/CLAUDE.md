# Small Business Practice Profile — Prism Specialties DMV

*This file is the practice profile for the `small-business` plugin. Every skill in this plugin should read it before doing substantive work and tailor outputs to this operator's reality — tools, tone, customer base, and approval rules — rather than producing generic SMB output.*

*Edit this file directly to change behavior across all small-business skills. Each section below is consumed by specific skills (noted in parentheses).*

---

## Who we are

**Operator:** Ron Klatt (`klatt42@gmail.com`)

**Primary business:** Prism Specialties DMV — a restoration-services franchise covering the DC / Maryland / Virginia region. Three vertical service lines: art restoration (ART), electronics restoration (ERS), and textile restoration (TEX). Each vertical has its own skills inventory, chemicals catalog, and pricing structure, but shares the same backbone (jobs, items, customer pipeline).

**Adjacent ventures owned by the same operator** (these may appear in the same financial reporting / tooling and should be recognized as separate-but-related entities):
- BizCopilot — internal SMB ops tool, deployed at biz-copilot.prismrestorationhub.com
- residential-restoration.com — Netlify-hosted lead-gen site, scheduled for Next.js cutover
- ROK ecosystem (Cockpit, Brain, Claw, Copilot) — internal AI infrastructure, not customer-facing

**Team size:** ~5 staff. Brand-President-level stakeholder for major demos and decisions. Operator is hands-on across finance, marketing, and ops.

**Customer base:** primarily B2B restoration jobs originating from insurance claims (carrier-driven) plus a smaller direct-to-consumer / property-owner line. Insurance reimbursement cycles drive AR aging and cash-flow patterns. Land-and-expand SMB pricing ($99–$5K/mo for the BizCopilot side; restoration jobs vary by claim).

---

## Available tools and integrations

*(Used by every skill that touches data. If a tool listed here is offline, fall back to CSV/PDF upload and tell the operator.)*

| Tool | Status | Used by | Notes |
|---|---|---|---|
| **QuickBooks Online (QBO)** | ✓ direct API | cash-flow-snapshot, plan-payroll, close-month, tax-prep, variance-analysis, margin-analyzer | Single source of truth for ledger. Direct API, NOT a generic accounting connector. |
| **HubSpot** | ✓ | crm-cleanup, crm-maintenance, lead-triage, call-list, customer-pulse-check, run-campaign | CRM for B2B insurance carrier pipeline + direct leads |
| **PayPal** | ✓ | cash-flow-snapshot, plan-payroll, invoice-chase, sales-brief | Payment processor for direct-to-consumer side |
| **GoHighLevel (GHL)** | ✓ | run-campaign, content-strategy, customer-pulse-check | Marketing automation + email delivery (Mailgun on `notify.` subdomain only) |
| **Canva** | ✓ via canva-creator | run-campaign, content-strategy, canva-creator | Social-post assets only (Instagram, Facebook, X, LinkedIn) — email content is drafted as plain text |
| **Tracking** (franchise system) | ⚠ cloud-only, no API | none directly | Franchise-mandated jobs system; **NOT a system of record for Workshop** — used as audit-trail input via PDF/Excel exports only |
| **iCat** (franchise inventory) | ⚠ cloud-only, no API | none directly | Deprioritized; warehouse-only |
| **Square** | ✗ not used | — | — |
| **Stripe** | ✗ not used | — | — |

**Insurance carrier integrations** are manual — claims arrive via email and are processed into HubSpot. No direct carrier API access.

---

## Tone and audience

*(Used by every skill that drafts customer-facing or internal communication.)*

- **Default voice:** professional, terse, no marketing fluff. Restoration-industry vernacular is fine (e.g., "ART claim", "TEX deductible", "carrier adjuster"). Avoid SaaS-startup language.
- **Customer-facing communications** (invoice reminders, complaint responses, KB articles): warm but professional, never apologetic about pricing, always reference the specific job/claim number when known.
- **Internal communications** (Monday brief, Friday pulse, status reports): bullet-heavy, KPI-forward, no preamble.
- **Stakeholder communications** (Brand President, quarterly reviews): narrative-driven with named risks and wins, no hedge language.
- **Never** use emoji unless the operator explicitly asks. Never start a draft with "I hope this finds you well" or equivalent.

---

## Approval and guardrails

*(Used by every skill that takes action or touches money/customers.)*

**Hard rule:** every step that touches money OR customers requires explicit operator approval before execution. Skills should:

1. **Stage the action, don't execute it.** Draft the invoice reminder, but don't send. Generate the journal entry, but don't post. Create the Canva asset, but don't publish.
2. **Show the impact.** If sending 12 invoice reminders, list all 12 recipients and amounts before asking for go/no-go.
3. **Flag jurisdictional or compliance risk.** DMV has DC + MD + VA = three jurisdictions. Wage/hour, sales tax, and contractor licensing differ across them. Surface jurisdiction before recommending action.
4. **Default conservative on cash and customer-trust decisions.** When in doubt about pricing, refund eligibility, or tone, ask before drafting.

**No-touch zones:**
- Direct posting to QBO ledger (operator posts after review)
- Sending customer emails from GHL (operator sends after review)
- Publishing Canva assets to social (operator publishes after review)
- Anything touching the franchise-mandated systems (Tracking, iCat) — these are decision-support inputs only, never write targets

---

## Reporting cadence

*(Used by monday-brief, friday-brief, month-heads-up, quarterly-review, business-pulse.)*

- **Monday brief:** delivered before 8am EST. Cash position, prior-week revenue vs. plan, top 3 to-dos for the week, pipeline movement.
- **Friday pulse:** delivered before 5pm EST. Revenue vs. prior week, top sellers, wins/watches, any cash-flow flags.
- **25th-of-month heads-up:** 30-day cash forecast + month-end prep checklist.
- **Monthly close:** by the 5th of the following month. Reconciliation + P&L narrative + close packet.
- **Quarterly review:** by the 15th of the month following quarter-end. Full narrative for Brand President.

---

## Common metrics and definitions

*(Used by analysis skills to ensure consistent terminology.)*

- **Cash runway:** weeks of operating expenses covered by current cash + 30-day AR (insurance-adjusted at 70% expected collection within 60 days).
- **Job cycle time:** from job-open in Tracking to invoice-sent in QBO. Target by vertical: ART <30d, ERS <14d, TEX <21d.
- **AR aging buckets:** 0-30, 31-60, 61-90, 90+. Insurance-claim AR is treated separately from direct-consumer AR (different collection patterns).
- **Pipeline stages (HubSpot):** Lead → Qualified → Estimate Sent → Job Open → Job Complete → Invoiced → Paid. "Active pipeline" = Qualified through Job Open.
- **Profitability metric:** gross margin by vertical (revenue – direct chemicals – direct labor) — NOT contribution margin (operator does that separately).

---

## What's explicitly out of scope

- **Investment, legal, or tax advice.** Tax-prep skill produces an accountant handoff packet; it does not file taxes or give tax positions.
- **HR / employment decisions.** Hiring, firing, comp adjustments — operator decides; skills can draft offer letters, but never recommend termination.
- **Pricing changes.** Margin-analyzer and price-check produce scenario data; the operator sets prices.
- **Franchise-system writes.** Tracking and iCat are read-only from this plugin's perspective.

---

*Last updated: 2026-05-26. Update this file directly when tooling, customer base, or tone preferences change. No skill in this plugin should silently fall back to generic SMB defaults if this file is present.*
