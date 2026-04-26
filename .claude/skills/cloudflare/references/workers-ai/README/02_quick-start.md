## Quick Start

```typescript
interface Env {
  AI: Ai;
}

export default {
  async fetch(request: Request, env: Env) {
    const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{ role: 'user', content: 'What is Cloudflare?' }]
    });
    return Response.json(response);
  }
};
```

```bash
# Setup - add binding to wrangler.jsonc
wrangler dev --remote  # Must use --remote for AI
wrangler deploy
```

