## Hostname Routing

### Wildcard Route (Recommended)
Configure `*/*` route on SaaS domain → dispatch Worker

**Benefits:**
- Supports subdomains + custom vanity domains
- No per-route limits (regular Workers limited to 100 routes)
- Programmatic control
- Works with any DNS proxy settings

**Setup:**
1. Cloudflare for SaaS custom hostnames
2. Fallback origin (dummy `A 192.0.2.0` if Worker is origin)
3. DNS CNAME to SaaS domain
4. `*/*` route → dispatch Worker
5. Routing logic in dispatch Worker

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const hostname = new URL(request.url).hostname;
    const hostnameData = await env.ROUTING_KV.get(`hostname:${hostname}`, { type: "json" });
    
    if (!hostnameData?.workerName) {
      return new Response("Hostname not configured", { status: 404 });
    }
    
    const userWorker = env.DISPATCHER.get(hostnameData.workerName);
    return await userWorker.fetch(request);
  },
};
```

### Subdomain-Only
1. Wildcard DNS: `*.saas.com` → origin
2. Route: `*.saas.com/*` → dispatch Worker
3. Extract subdomain for routing

### Orange-to-Orange (O2O) Behavior

When customers use Cloudflare and CNAME to your Workers domain:

| Scenario | Behavior | Route Pattern |
|----------|----------|---------------|
| Customer not on Cloudflare | Standard routing | `*/*` or `*.domain.com/*` |
| Customer on Cloudflare (proxied CNAME) | Invokes Worker at edge | `*/*` required |
| Customer on Cloudflare (DNS-only CNAME) | Standard routing | Any route works |

**Recommendation:** Always use `*/*` wildcard for consistent O2O behavior.

### Custom Metadata Routing

For Cloudflare for SaaS: Store worker name in custom hostname `custom_metadata`, retrieve in dispatch worker to route requests. Requires custom hostnames as subdomains of your domain.

