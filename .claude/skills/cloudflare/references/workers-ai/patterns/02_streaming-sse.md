## Streaming (SSE)

```typescript
const stream = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
  messages, stream: true
});

const { readable, writable } = new TransformStream();
const writer = writable.getWriter();

(async () => {
  for await (const chunk of stream) {
    await writer.write(new TextEncoder().encode(`data: ${JSON.stringify(chunk)}\n\n`));
  }
  await writer.write(new TextEncoder().encode('data: [DONE]\n\n'));
  await writer.close();
})();

return new Response(readable, {
  headers: { 'Content-Type': 'text/event-stream' }
});
```

