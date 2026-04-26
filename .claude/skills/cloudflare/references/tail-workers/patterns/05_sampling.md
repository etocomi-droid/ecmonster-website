## Sampling

Reduce costs by processing only a percentage of events:

```typescript
export default {
  async tail(events, env, ctx) {
    if (Math.random() > 0.1) return;  // 10% sample rate
    ctx.waitUntil(fetch(env.LOG_ENDPOINT, {
      method: "POST",
      body: JSON.stringify(events),
    }));
  }
};
```

