## Workers Binding

**wrangler.jsonc:**
```jsonc
{
  "kv_namespaces": [
    {
      "binding": "MY_KV",
      "id": "abc123xyz789"
    },
    // Optional: Different namespace for preview/development
    {
      "binding": "MY_KV",
      "preview_id": "preview-abc123"
    }
  ]
}
```

