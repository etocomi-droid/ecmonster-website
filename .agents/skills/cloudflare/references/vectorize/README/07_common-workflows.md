## Common Workflows

### Semantic Search

```typescript
// 1. Generate embedding
const result = await env.AI.run("@cf/baai/bge-base-en-v1.5", { text: [query] });

// 2. Query Vectorize
const matches = await env.VECTORIZE.query(result.data[0], {
  topK: 5,
  returnMetadata: "indexed"
});
```

### RAG Pattern

```typescript
// 1. Generate query embedding
const embedding = await env.AI.run("@cf/baai/bge-base-en-v1.5", { text: [query] });

// 2. Search Vectorize
const matches = await env.VECTORIZE.query(embedding.data[0], { topK: 5 });

// 3. Fetch full documents from R2/D1/KV
const docs = await Promise.all(matches.matches.map(m => 
  env.R2.get(m.metadata.key).then(obj => obj?.text())
));

// 4. Generate LLM response with context
const answer = await env.AI.run("@cf/meta/llama-3-8b-instruct", {
  prompt: `Context: ${docs.join("\n\n")}\n\nQuestion: ${query}\n\nAnswer:`
});
```

