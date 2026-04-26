## OpenTelemetry Export

```typescript
export default {
  async tail(events, env, ctx) {
    const otelSpans = events.map(e => ({
      traceId: generateId(32),
      spanId: generateId(16),
      name: e.scriptName || 'worker.request',
      attributes: [
        { key: 'worker.outcome', value: { stringValue: e.event.outcome } },
        { key: 'worker.cpu_time_us', value: { intValue: String(e.event.cpuTime) } }
      ]
    }));
    
    ctx.waitUntil(
      fetch('https://api.honeycomb.io/v1/traces', {
        method: 'POST',
        headers: { 'X-Honeycomb-Team': env.HONEYCOMB_KEY },
        body: JSON.stringify({ resourceSpans: [{ scopeSpans: [{ spans: otelSpans }] }] })
      })
    );
  }
};
```
