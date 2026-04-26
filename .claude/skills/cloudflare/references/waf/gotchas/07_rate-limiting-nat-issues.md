## Rate Limiting NAT Issues

**Problem:** Users behind NAT hit rate limits too quickly
**Cause:** Multiple users sharing single IP
**Solution:**

Add more characteristics: User-Agent, session cookie, or authorization header
```typescript
{
  action: 'block',
  expression: 'http.request.uri.path starts_with "/api"',
  action_parameters: {
    ratelimit: {
      characteristics: ['cf.colo.id', 'ip.src', 'http.request.cookies["session"][0]'],
      period: 60,
      requests_per_period: 100,
    },
  },
}
```

