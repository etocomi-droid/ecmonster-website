## Pattern 3: Workers AI Binding

For Cloudflare Workers using Workers AI.

```typescript
export default {
  async fetch(request, env, ctx) {
    const response = await env.AI.run(
      '@cf/meta/llama-3-8b-instruct',
      { messages: [{ role: 'user', content: 'Hello!' }] },
      { 
        gateway: { 
          id: 'my-gateway',
          metadata: { userId: '123', team: 'engineering' }
        } 
      }
    );
    
    return Response.json(response);
  }
};
```

