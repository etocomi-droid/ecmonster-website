## Embeddings

```typescript
const result = await env.AI.run('@cf/baai/bge-base-en-v1.5', {
  text: ['Query', 'Doc 1', 'Doc 2'] // Batch for efficiency
});
const [queryEmbed, doc1Embed, doc2Embed] = result.data; // 768-dim vectors
```

