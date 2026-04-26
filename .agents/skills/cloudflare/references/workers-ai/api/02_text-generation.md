## Text Generation

```typescript
const result = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
  messages: [
    { role: 'system', content: 'You are helpful' },
    { role: 'user', content: 'Hello' }
  ],
  temperature: 0.7,  // 0-1
  max_tokens: 100
});
console.log(result.response);
```

**Streaming:**
```typescript
const stream = await env.AI.run(model, { messages, stream: true });
return new Response(stream, { headers: { 'Content-Type': 'text/event-stream' } });
```

