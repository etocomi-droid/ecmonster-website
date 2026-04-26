## Security Issues

### SSRF Vulnerability

**Problem:** User-controlled destinations allow access to internal services

**Solution:** Validate against strict allowlist:

```typescript
const ALLOWED = ['api1.internal.net', 'api2.internal.net'];
const host = new URL(req.url).searchParams.get('host');
if (!host || !ALLOWED.includes(host)) return new Response('Forbidden', { status: 403 });
```

