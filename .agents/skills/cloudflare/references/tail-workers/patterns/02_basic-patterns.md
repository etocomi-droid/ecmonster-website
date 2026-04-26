## Basic Patterns

### HTTP Endpoint Logging

```typescript
export default {
  async tail(events, env, ctx) {
    const payload = events.map(event => ({
      script: event.scriptName,
      timestamp: event.eventTimestamp,
      outcome: event.outcome,
      url: event.event?.request?.url,
      status: event.event?.response?.status,
      logs: event.logs,
      exceptions: event.exceptions,
    }));
    
    ctx.waitUntil(
      fetch(env.LOG_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(payload),
      })
    );
  }
};
```

### Error Tracking Only

```typescript
export default {
  async tail(events, env, ctx) {
    const errors = events.filter(e => 
      e.outcome === 'exception' || e.exceptions.length > 0
    );
    
    if (errors.length === 0) return;
    
    ctx.waitUntil(
      fetch(env.ERROR_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(errors),
      })
    );
  }
};
```

