# agent-plugins/

Named workflow agents — self-contained plugins that bundle multiple skills into a single install for a specific job. **Empty for now**; populated as needs emerge.

## Pattern

From `anthropics/financial-services`: each agent has a job-title name (e.g., Pitch Agent, Month-End Closer, KYC Screener) and bundles the skills it uses internally, so installing the agent gives you the whole workflow in one shot — no need to figure out which 5 vertical-plugin skills to install.

## Layout (when populated)

```
agent-plugins/
  <agent-slug>/
    .claude-plugin/plugin.json    # name, version, description, author
    skills/                       # bundled copies of skills this agent uses
      <skill>/SKILL.md
    README.md                     # what this agent does, how to invoke
```

## SMB candidates (per Tier 3 plan)

- **Monday-Brief Agent** — bundles monday-brief + business-pulse + cash-flow-snapshot + call-list + smb-router
- **Month-End Closer** — bundles month-end-prep + close-month + reconciliation + plan-payroll + tax-prep
- **Customer Pulse Monitor** — bundles customer-pulse-check + handle-complaint + ticket-deflector + kb-article

The trigger to actually build one of these: when you find yourself routinely invoking the same 3-5 small-business skills in sequence. That's the signal that bundling them saves real friction.
