## Critical: @cloudflare/ai is DEPRECATED

```typescript
// ❌ WRONG - Don't install @cloudflare/ai
import Ai from '@cloudflare/ai';

// ✅ CORRECT - Use native binding
export default {
  async fetch(request: Request, env: Env) {
    await env.AI.run('@cf/meta/llama-3.1-8b-instruct', { messages: [...] });
  }
}
```

