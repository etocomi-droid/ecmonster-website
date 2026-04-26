## Cost Optimization

| Task | Model | Neurons |
|------|-------|---------|
| Classify | `@cf/mistral/mistral-7b-instruct-v0.1` | ~50 |
| Chat | `@cf/meta/llama-3.1-8b-instruct` | ~200 |
| Complex | `@cf/meta/llama-3.1-70b-instruct` | ~2000 |
| Embed | `@cf/baai/bge-base-en-v1.5` | ~10 |

```typescript
// Batch embeddings
const response = await env.AI.run('@cf/baai/bge-base-en-v1.5', {
  text: textsArray // Process multiple at once
});
```
