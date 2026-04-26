## Producer: Send Messages

```typescript
// Basic send
await env.MY_QUEUE.send({ url: request.url, timestamp: Date.now() });

// Options: delay (max 43200s), contentType (json|text|bytes|v8)
await env.MY_QUEUE.send(message, { delaySeconds: 600 });
await env.MY_QUEUE.send(message, { delaySeconds: 0 }); // Override queue default

// Batch (up to 100 msgs or 256 KB)
await env.MY_QUEUE.sendBatch([
  { body: 'msg1' },
  { body: 'msg2' },
  { body: 'msg3', options: { delaySeconds: 300 } }
]);

// Non-blocking with ctx.waitUntil - send continues after response
ctx.waitUntil(env.MY_QUEUE.send({ data: 'async' }));

// Background tasks in queue consumer
export default {
  async queue(batch: MessageBatch, env: Env, ctx: ExecutionContext): Promise<void> {
    for (const msg of batch.messages) {
      await processMessage(msg.body);
      
      // Fire-and-forget analytics (doesn't block ack)
      ctx.waitUntil(
        env.ANALYTICS_QUEUE.send({ messageId: msg.id, processedAt: Date.now() })
      );
      
      msg.ack();
    }
  }
};
```

