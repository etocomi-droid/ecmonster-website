## Workers AI Binding

```toml
# wrangler.toml
[ai]
binding = "AI"
[[ai.gateway]]
id = "my-gateway"
```

```typescript
await env.AI.run('@cf/meta/llama-3-8b-instruct', 
  { messages: [...] },
  { gateway: { id: 'my-gateway', metadata: { userId: '123' } } }
);
```

