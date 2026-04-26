## Runtime vs Build-Time Types

| Type Source | When Generated | Use Case |
|-------------|----------------|----------|
| `@cloudflare/workers-types` | npm install | Base Workers APIs (Request, Response, etc.) |
| `wrangler types` | After config change | Your specific bindings (Env interface) |

**Install both:**
```bash
npm install -D @cloudflare/workers-types
npx wrangler types
```

