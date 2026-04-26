## Skip Rules

```typescript
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_request_firewall_custom',
  name: 'Skip Rules',
  rules: [
    // Skip static assets (current ruleset only)
    {
      action: 'skip',
      action_parameters: { ruleset: 'current' },
      expression: 'http.request.uri.path matches "\\.(jpg|css|js|woff2?)$"',
    },
    
    // Skip all WAF phases for trusted IPs
    {
      action: 'skip',
      action_parameters: {
        phases: ['http_request_firewall_managed', 'http_ratelimit'],
      },
      expression: 'ip.src in {192.0.2.0/24}',
    },
  ],
});
```

