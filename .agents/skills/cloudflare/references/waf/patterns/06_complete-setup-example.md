## Complete Setup Example

Combine all three phases for comprehensive protection:

```typescript
const client = new Cloudflare({ apiToken: process.env.CF_API_TOKEN });
const zoneId = process.env.ZONE_ID;

// 1. Custom rules (execute first)
await client.rulesets.create({
  zone_id: zoneId,
  phase: 'http_request_firewall_custom',
  rules: [
    { action: 'skip', action_parameters: { phases: ['http_request_firewall_managed', 'http_ratelimit'] }, expression: 'ip.src in {192.0.2.0/24}' },
    { action: 'block', expression: 'cf.waf.score gt 50' },
    { action: 'managed_challenge', expression: 'cf.waf.score gt 20' },
  ],
});

// 2. Managed ruleset (execute second)
await client.rulesets.create({
  zone_id: zoneId,
  phase: 'http_request_firewall_managed',
  rules: [{
    action: 'execute',
    action_parameters: { id: 'efb7b8c949ac4650a09736fc376e9aee', overrides: { categories: [{ category: 'wordpress', enabled: false }] } },
    expression: 'true',
  }],
});

// 3. Rate limiting (execute third)
await client.rulesets.create({
  zone_id: zoneId,
  phase: 'http_ratelimit',
  rules: [
    { action: 'block', expression: 'true', action_parameters: { ratelimit: { characteristics: ['cf.colo.id', 'ip.src'], period: 60, requests_per_period: 100, mitigation_timeout: 600 } } },
    { action: 'block', expression: 'http.request.uri.path eq "/api/login"', action_parameters: { ratelimit: { characteristics: ['ip.src'], period: 60, requests_per_period: 5, mitigation_timeout: 600 } } },
  ],
});
```