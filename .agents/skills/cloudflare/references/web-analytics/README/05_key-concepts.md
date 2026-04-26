## Key Concepts

### Proxied vs Non-Proxied Sites

| Type | Description | Beacon Injection | Limit |
|------|-------------|------------------|-------|
| **Proxied** | DNS through Cloudflare (orange cloud) | Automatic or manual | Unlimited |
| **Non-proxied** | External hosting, manual beacon | Manual only | 10 sites max |

### SPA Mode

**Critical for modern frameworks:**
```json
{"token": "YOUR_TOKEN", "spa": true}
```

Without `spa: true`, client-side navigation (React Router, Vue Router, Next.js routing) will NOT be tracked. Only initial page loads will register.

### CSP Requirements

If using Content Security Policy, allow both domains:
```
script-src https://static.cloudflareinsights.com https://cloudflareinsights.com;
```

