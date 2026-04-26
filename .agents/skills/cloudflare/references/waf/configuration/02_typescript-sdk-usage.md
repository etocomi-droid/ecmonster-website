## TypeScript SDK Usage

```bash
npm install cloudflare
```

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({ apiToken: process.env.CF_API_TOKEN });

// Custom rules
await client.rulesets.create({
  zone_id: process.env.ZONE_ID,
  kind: 'zone',
  phase: 'http_request_firewall_custom',
  name: 'Custom WAF',
  rules: [
    { action: 'block', expression: 'cf.waf.score gt 50', enabled: true },
    { action: 'challenge', expression: 'http.request.uri.path eq "/admin"', enabled: true },
  ],
});

// Managed ruleset
await client.rulesets.create({
  zone_id: process.env.ZONE_ID,
  phase: 'http_request_firewall_managed',
  rules: [{
    action: 'execute',
    action_parameters: { id: 'efb7b8c949ac4650a09736fc376e9aee' },
    expression: 'true',
  }],
});

// Rate limiting
await client.rulesets.create({
  zone_id: process.env.ZONE_ID,
  phase: 'http_ratelimit',
  rules: [{
    action: 'block',
    expression: 'http.request.uri.path starts_with "/api"',
    action_parameters: {
      ratelimit: {
        characteristics: ['cf.colo.id', 'ip.src'],
        period: 60,
        requests_per_period: 100,
        mitigation_timeout: 600,
      },
    },
  }],
});
```

