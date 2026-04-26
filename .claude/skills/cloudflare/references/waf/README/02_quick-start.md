## Quick Start

### Deploy Cloudflare Managed Ruleset
```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({ apiToken: process.env.CF_API_TOKEN });

// Deploy managed ruleset to zone
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_request_firewall_managed',
  name: 'Deploy Cloudflare Managed Ruleset',
  rules: [{
    action: 'execute',
    action_parameters: {
      id: 'efb7b8c949ac4650a09736fc376e9aee', // Cloudflare Managed Ruleset
    },
    expression: 'true',
    enabled: true,
  }],
});
```

### Create Custom Rule
```typescript
// Block requests with attack score >= 40
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_request_firewall_custom',
  name: 'Custom WAF Rules',
  rules: [{
    action: 'block',
    expression: 'cf.waf.score gt 40',
    description: 'Block high attack scores',
    enabled: true,
  }],
});
```

### Create Rate Limit
```typescript
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_ratelimit',
  name: 'API Rate Limits',
  rules: [{
    action: 'block',
    expression: 'http.request.uri.path eq "/api/login"',
    action_parameters: {
      ratelimit: {
        characteristics: ['cf.colo.id', 'ip.src'],
        period: 60,
        requests_per_period: 10,
        mitigation_timeout: 600,
      },
    },
    enabled: true,
  }],
});
```

