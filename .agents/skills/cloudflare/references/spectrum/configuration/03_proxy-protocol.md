## Proxy Protocol

Forwards real client IP to origin. Origin must support parsing.

| Version | Protocol | Use Case |
|---------|----------|----------|
| `off` | - | Origin doesn't need client IP |
| `v1` | TCP | Most TCP apps (SSH, databases) |
| `v2` | TCP | High-performance TCP |
| `simple` | UDP | UDP applications |

**Compatibility:**
- **v1**: HAProxy, nginx, SSH, most databases
- **v2**: HAProxy 1.5+, nginx 1.11+
- **simple**: Cloudflare-specific UDP format

**Enable:**
```typescript
const app = await client.spectrum.apps.create({
  // ...
  proxy_protocol: 'v1',  // Origin must parse PROXY header
});
```

**Origin Config (nginx):**
```nginx
stream {
    server {
        listen 22 proxy_protocol;
        proxy_pass backend:22;
    }
}
```

