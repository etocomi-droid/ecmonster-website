## Quick Start

1. **Add binding to wrangler.jsonc:**
```jsonc
{
  "kv_namespaces": [
    { "binding": "MY_KV", "id": "your-kv-id" }
  ]
}
```

2. **Generate types:**
```bash
npx wrangler types
```

3. **Access in Worker:**
```typescript
export default {
  async fetch(request, env, ctx) {
    await env.MY_KV.put('key', 'value');
    return new Response('OK');
  }
}
```

