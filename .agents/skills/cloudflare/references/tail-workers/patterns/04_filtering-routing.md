## Filtering & Routing

Filter by route, outcome, or other criteria:

```typescript
export default {
  async tail(events, env, ctx) {
    // Route filtering
    const apiEvents = events.filter(e => 
      e.event?.request?.url?.includes('/api/')
    );
    
    // Multi-destination routing
    const errors = events.filter(e => e.outcome === 'exception');
    const success = events.filter(e => e.outcome === 'ok');
    
    const tasks = [];
    if (errors.length > 0) {
      tasks.push(fetch(env.ERROR_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(errors),
      }));
    }
    if (success.length > 0) {
      tasks.push(fetch(env.SUCCESS_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(success),
      }));
    }
    
    ctx.waitUntil(Promise.all(tasks));
  }
};
```

