## Type-Safe Handler

```typescript
interface Env {
  LOGS_KV: KVNamespace;
  ANALYTICS: AnalyticsEngineDataset;
  LOG_ENDPOINT: string;
  API_TOKEN: string;
}

export default {
  async tail(
    events: TraceItem[],
    env: Env,
    ctx: ExecutionContext
  ): Promise<void> {
    const payload = events.map(event => ({
      script: event.scriptName,
      timestamp: event.eventTimestamp,
      outcome: event.outcome,
      url: event.event?.request?.url,
      status: event.event?.response?.status,
    }));
    
    ctx.waitUntil(
      fetch(env.LOG_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      })
    );
  }
} satisfies ExportedHandler<Env>;
```

