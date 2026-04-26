## Quick Start

**1. Create AI Search instance in dashboard:**
- Go to Cloudflare Dashboard → AI Search → Create
- Choose data source (R2 or website)
- Configure instance name and settings

**2. Configure Worker:**

```jsonc
// wrangler.jsonc
{
  "ai": {
    "binding": "AI"
  }
}
```

**3. Use in Worker:**

```typescript
export default {
  async fetch(request, env) {
    const answer = await env.AI.autorag("my-search-instance").aiSearch({
      query: "How do I configure caching?",
      model: "@cf/meta/llama-3.3-70b-instruct-fp8-fast"
    });
    
    return Response.json({ answer: answer.response });
  }
};
```

