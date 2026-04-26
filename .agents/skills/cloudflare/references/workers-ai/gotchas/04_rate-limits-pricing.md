## Rate Limits & Pricing

| Model Type | Neurons/Request |
|------------|-----------------|
| Small text (7B) | ~50-200 |
| Large text (70B) | ~500-2000 |
| Embeddings | ~5-20 |
| Image gen | ~10,000+ |

**Free tier**: 10,000 neurons/day

```typescript
// ❌ EXPENSIVE - 70B model
await env.AI.run('@cf/meta/llama-3.1-70b-instruct', ...);
// ✅ CHEAPER - Use smallest that works
await env.AI.run('@cf/meta/llama-3.1-8b-instruct', ...);
```

