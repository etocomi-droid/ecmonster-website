## Deploy Managed Rulesets

```typescript
// Deploy Cloudflare Managed Ruleset (default)
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_request_firewall_managed',
  name: 'Cloudflare Managed Ruleset',
  rules: [{
    action: 'execute',
    action_parameters: {
      id: 'efb7b8c949ac4650a09736fc376e9aee', // Cloudflare Managed
      // Or: '4814384a9e5d4991b9815dcfc25d2f1f' for OWASP CRS
      // Or: 'c2e184081120413c86c3ab7e14069605' for Exposed Credentials
    },
    expression: 'true', // All requests
    // Or: 'http.request.uri.path starts_with "/api"' for specific paths
    enabled: true,
  }],
});
```

