---
title: Service status and incidents
description: Public Alpha maintenance, status, and incident communication commitments.
sidebar:
  order: 3
---

The public [TerraScale status page](https://status.terrascale.tech) reports shared incidents by product and region. Public Alpha publishes observed availability but makes no uptime percentage or SLA commitment.

The Dashboard links each Project's service-status view to the public status page for shared incidents. A project-specific authorization or usage problem may appear only in the authenticated Project view.

## Maintenance

TerraScale gives at least 24 hours notice before planned maintenance. Emergency maintenance may begin without advance notice when waiting would increase customer or service risk. The status page states affected products and regions when known.

## Customer-impacting incidents

After TerraScale confirms a customer-impacting incident, it posts an initial public notice within 30 minutes. While impact continues, TerraScale updates the notice at least hourly. Each update states current impact, affected products and regions, mitigation progress, and the next expected update time when known.

The incident closes only after recovery checks pass. A major incident receives a short public review after recovery. The review covers customer impact, the observed period, what changed, and follow-up work without exposing customer data or useful attack details.

## Security notification

Public status updates and customer security notices have different audiences. After a confirmed security incident, TerraScale emails affected Organization Owners with the known affected period and data categories, mitigations, and required customer actions. TerraScale follows applicable legal deadlines and does not wait for every root-cause detail before sending a required notice.

Customer organizations remain responsible for notifying their own application users when their role or applicable law requires it.

## External verification

Local checks validate the wording and the checked-in `security.txt` file only. They do not prove that the status page, policy URL, security contact, or Organization Owner notification delivery is reachable. Before registration opens, an authorized release check must verify those external routes and exercise the notification path.
