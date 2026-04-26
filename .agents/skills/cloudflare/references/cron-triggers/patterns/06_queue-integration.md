## Queue Integration

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const batch = await env.MY_QUEUE.receive({ batchSize: 100 });
    const results = await Promise.allSettled(batch.messages.map(async (msg) => {
      await processMessage(msg.body, env);
      await msg.ack();
    }));
    console.log(`Processed ${results.filter(r => r.status === "fulfilled").length}/${batch.messages.length}`);
  },
};
```

