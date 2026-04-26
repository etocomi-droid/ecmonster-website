## Rate Limiting Configuration

```typescript
{
  action: 'block',
  expression: 'http.request.uri.path starts_with "/api"',
  action_parameters: {
    ratelimit: {
      // Characteristics define uniqueness: 'ip.src', 'cf.colo.id', 
      // 'http.request.headers["key"][0]', 'http.request.cookies["session"][0]'
      characteristics: ['cf.colo.id', 'ip.src'], // Recommended: per-IP per-datacenter
      period: 60,                      // Time window in seconds
      requests_per_period: 100,        // Max requests in period
      mitigation_timeout: 600,         // Block duration in seconds
      counting_expression: 'http.request.method ne "GET"', // Optional: filter counted requests
      requests_to_origin: false,       // Count all requests (not just origin hits)
    },
  },
  enabled: true,
}
```

