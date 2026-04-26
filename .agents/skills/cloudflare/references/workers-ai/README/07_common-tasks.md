## Common Tasks

```typescript
// Streaming text generation
const stream = await env.AI.run(model, { messages, stream: true });
for await (const chunk of stream) {
  console.log(chunk.response);
}

// Embeddings for RAG
const { data } = await env.AI.run('@cf/baai/bge-base-en-v1.5', {
  text: ['Query text', 'Document 1', 'Document 2']
});

// Function calling
const response = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
  messages: [{ role: 'user', content: 'What is the weather?' }],
  tools: [{
    type: 'function',
    function: { name: 'getWeather', parameters: { ... } }
  }]
});
```

