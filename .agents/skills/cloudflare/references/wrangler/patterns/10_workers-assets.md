## Workers Assets

```jsonc
{ "assets": { "directory": "./dist", "binding": "ASSETS" } }
```

```typescript
export default {
  async fetch(request, env) {
    // API routes first
    if (new URL(request.url).pathname.startsWith("/api/")) {
      return Response.json({ data: "from API" });
    }
    return env.ASSETS.fetch(request);  // Static assets
  }
}
```

