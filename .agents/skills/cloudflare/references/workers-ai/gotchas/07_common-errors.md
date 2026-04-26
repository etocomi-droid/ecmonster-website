## Common Errors

### 7502: Model not found
Check exact model name at developers.cloudflare.com/workers-ai/models/

### 7504: Input validation failed
```typescript
// Text gen requires messages array
await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
  messages: [{ role: 'user', content: 'Hello' }]  // ✅
});

// Embeddings require text
await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: 'Hello' });  // ✅
```

