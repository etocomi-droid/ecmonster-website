## Rate Limiting

```typescript
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_ratelimit',
  name: 'Rate Limits',
  rules: [
    // Per-IP global limit
    {
      action: 'block',
      expression: 'true',
      action_parameters: {
        ratelimit: {
          characteristics: ['cf.colo.id', 'ip.src'],
          period: 60,
          requests_per_period: 100,
          mitigation_timeout: 600,
        },
      },
    },
    
    // Login endpoint (stricter)
    {
      action: 'block',
      expression: 'http.request.uri.path eq "/api/login"',
      action_parameters: {
        ratelimit: {
          characteristics: ['ip.src'],
          period: 60,
          requests_per_period: 5,
          mitigation_timeout: 600,
        },
      },
    },
    
    // API writes only (using counting_expression)
    {
      action: 'block',
      expression: 'http.request.uri.path starts_with "/api"',
      action_parameters: {
        ratelimit: {
          characteristics: ['cf.colo.id', 'ip.src'],
          period: 60,
          requests_per_period: 50,
          counting_expression: 'http.request.method ne "GET"',
        },
      },
    },
  ],
});
```

