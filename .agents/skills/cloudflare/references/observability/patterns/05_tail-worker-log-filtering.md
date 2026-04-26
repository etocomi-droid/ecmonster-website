## Tail Worker Log Filtering

```typescript
export default {
  async tail(events, env, ctx) {
    const critical = events.filter(e => 
      e.exceptions.length > 0 || e.event.wallTime > 1000000
    );
    if (critical.length === 0) return;
    
    ctx.waitUntil(
      fetch('https://logging.example.com/ingest', {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${env.API_KEY}` },
        body: JSON.stringify(critical.map(e => ({
          outcome: e.event.outcome,
          cpu_ms: e.event.cpuTime / 1000,
          errors: e.exceptions
        })))
      })
    );
  }
};
```

