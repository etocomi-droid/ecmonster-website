## RAG (Retrieval-Augmented Generation)

```typescript
// 1. Embed query
const embedding = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: query });

// 2. Search vectors
const results = await env.VECTORIZE.query(embedding.data[0], {
  topK: 5, returnMetadata: true
});

// 3. Build context
const context = results.matches.map(m => m.metadata?.text).join('\n\n');

// 4. Generate with context
const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
  messages: [
    { role: 'system', content: `Answer based on:\n\n${context}` },
    { role: 'user', content: query }
  ]
});
```

