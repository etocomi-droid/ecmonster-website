## Workers Assets (Static Files)

Recommended for serving static files (replaces old `site` config).

```jsonc
{
  "assets": {
    "directory": "./public",
    "binding": "ASSETS",
    "html_handling": "auto-trailing-slash",  // or "none", "force-trailing-slash"
    "not_found_handling": "single-page-application"  // or "404-page", "none"
  }
}
```

Access in Worker:
```typescript
export default {
  async fetch(request, env) {
    // Try serving static asset first
    const asset = await env.ASSETS.fetch(request);
    if (asset.status !== 404) return asset;
    
    // Custom logic for non-assets
    return new Response("API response");
  }
}
```

