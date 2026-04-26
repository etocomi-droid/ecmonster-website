### Client IP Showing Cloudflare IP

**Problem:** Origin logs show Cloudflare IPs not real client IPs  
**Cause:** Proxy Protocol not enabled or origin not configured  
**Solution:**
```typescript
// Enable in Spectrum app
const app = await client.spectrum.apps.create({
  // ...
  proxy_protocol: 'v1',  // TCP: v1/v2; UDP: simple
});
```

**Origin config:**
- **nginx**: `listen 22 proxy_protocol;`
- **HAProxy**: `bind :22 accept-proxy`

