## Critical Issues

### ReadableStream Single-Use

```typescript
// ❌ WRONG: Stream consumed twice
const email = await PostalMime.parse(await new Response(message.raw).arrayBuffer());
const rawText = await new Response(message.raw).text(); // EMPTY!

// ✅ CORRECT: Buffer first
const buffer = await new Response(message.raw).arrayBuffer();
const email = await PostalMime.parse(buffer);
const rawText = new TextDecoder().decode(buffer);
```

### ctx.waitUntil() Errors Silent

```typescript
// ❌ Errors dropped silently
ctx.waitUntil(fetch(webhookUrl, { method: 'POST', body: data }));

// ✅ Catch and log
ctx.waitUntil(
  fetch(webhookUrl, { method: 'POST', body: data })
    .catch(err => env.ERROR_LOG.put(`error:${Date.now()}`, err.message))
);
```

