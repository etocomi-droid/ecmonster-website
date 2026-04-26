## Model Fallback

```typescript
try {
  return await env.AI.run('@cf/meta/llama-3.1-70b-instruct', { messages });
} catch {
  return await env.AI.run('@cf/meta/llama-3.1-8b-instruct', { messages });
}
```

