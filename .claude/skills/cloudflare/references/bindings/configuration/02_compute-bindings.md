## Compute Bindings

```jsonc
{
  "services": [{ 
    "binding": "MY_SERVICE", 
    "service": "other-worker",
    "environment": "production"  // Optional: target specific env
  }],
  "ai": { "binding": "AI" },
  "browser": { "binding": "BROWSER" },
  "workflows": [{ "binding": "MY_WORKFLOW", "name": "my-workflow" }]
}
```

**Create workflows:**
```bash
npx wrangler workflows create my-workflow
```

