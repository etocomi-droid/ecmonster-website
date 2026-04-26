## API Responses

### Embedding response shape varies
```typescript
// @cf/baai/bge-base-en-v1.5 returns: { data: [[0.1, 0.2, ...]] }
const embedding = response.data[0]; // Get first element
```

### Stream returns ReadableStream
```typescript
const stream = await env.AI.run(model, { messages: [...], stream: true });
for await (const chunk of stream) { console.log(chunk.response); }
```

