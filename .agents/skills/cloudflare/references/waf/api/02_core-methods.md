## Core Methods

```typescript
// List rulesets
await client.rulesets.list({ zone_id: 'zone_id', phase: 'http_request_firewall_managed' });

// Get ruleset
await client.rulesets.get({ zone_id: 'zone_id', ruleset_id: 'ruleset_id' });

// Create ruleset
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_request_firewall_custom',
  name: 'Custom WAF Rules',
  rules: [{ action: 'block', expression: 'cf.waf.score gt 40', enabled: true }],
});

// Update ruleset (include rule id to keep existing, omit id for new rules)
await client.rulesets.update({
  zone_id: 'zone_id',
  ruleset_id: 'ruleset_id',
  rules: [
    { id: 'rule_id', action: 'block', expression: 'cf.waf.score gt 40', enabled: true },
    { action: 'challenge', expression: 'http.request.uri.path contains "/admin"', enabled: true },
  ],
});

// Delete ruleset
await client.rulesets.delete({ zone_id: 'zone_id', ruleset_id: 'ruleset_id' });
```

