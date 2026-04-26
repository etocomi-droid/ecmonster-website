## Pulumi Configuration

```typescript
import * as cloudflare from '@pulumi/cloudflare';

const zoneId = 'zone_id';

// Custom rules
const wafCustom = new cloudflare.Ruleset('waf-custom', {
  zoneId,
  phase: 'http_request_firewall_custom',
  rules: [
    { action: 'block', expression: 'cf.waf.score gt 50', enabled: true },
    { action: 'challenge', expression: 'http.request.uri.path eq "/admin"', enabled: true },
  ],
});

// Managed ruleset
const wafManaged = new cloudflare.Ruleset('waf-managed', {
  zoneId,
  phase: 'http_request_firewall_managed',
  rules: [{
    action: 'execute',
    actionParameters: { id: 'efb7b8c949ac4650a09736fc376e9aee' },
    expression: 'true',
  }],
});

// Rate limiting
const rateLimiting = new cloudflare.Ruleset('rate-limiting', {
  zoneId,
  phase: 'http_ratelimit',
  rules: [{
    action: 'block',
    expression: 'http.request.uri.path starts_with "/api"',
    ratelimit: {
      characteristics: ['cf.colo.id', 'ip.src'],
      period: 60,
      requestsPerPeriod: 100,
      mitigationTimeout: 600,
    },
  }],
});
```

