## Quick Start Decision Tree

```
Is your site proxied through Cloudflare?
├─ YES → Use automatic injection (configuration.md)
│   ├─ Enable auto-injection in dashboard
│   └─ No code changes needed (unless Cache-Control: no-transform)
│
└─ NO → Use manual beacon integration (integration.md)
    ├─ Add JS snippet to HTML
    ├─ Use spa: true for React/Vue/Next.js
    └─ Configure CSP if needed
```

