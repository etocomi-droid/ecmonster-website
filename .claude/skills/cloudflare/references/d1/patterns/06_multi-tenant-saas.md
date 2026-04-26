## Multi-Tenant SaaS

```typescript
// Each tenant gets own database
export default {
  async fetch(request: Request, env: { [key: `TENANT_${string}`]: D1Database }) {
    const tenantId = request.headers.get('X-Tenant-ID');
    const data = await env[`TENANT_${tenantId}`].prepare('SELECT * FROM records').all();
    return Response.json(data.results);
  }
}
```

