## Storage Integration

### KV Storage with TTL

```typescript
export default {
  async tail(events, env, ctx) {
    ctx.waitUntil(
      Promise.all(events.map(event =>
        env.LOGS_KV.put(
          `log:${event.scriptName}:${event.eventTimestamp}`,
          JSON.stringify(event),
          { expirationTtl: 86400 }  // 24 hours
        )
      ))
    );
  }
};
```

### Analytics Engine Metrics

```typescript
export default {
  async tail(events, env, ctx) {
    ctx.waitUntil(
      Promise.all(events.map(event =>
        env.ANALYTICS.writeDataPoint({
          blobs: [event.scriptName, event.outcome],
          doubles: [1, event.event?.response?.status ?? 0],
          indexes: [event.event?.request?.cf?.colo ?? 'unknown'],
        })
      ))
    );
  }
};
```

