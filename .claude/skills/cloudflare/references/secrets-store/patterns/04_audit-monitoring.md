## Audit & Monitoring

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const startTime = Date.now();
    try {
      const apiKey = await env.API_KEY.get();
      const resp = await fetch("https://api.example.com", {
        headers: { "Authorization": `Bearer ${apiKey}` }
      });
      
      ctx.waitUntil(
        fetch("https://log.example.com/log", {
          method: "POST",
          body: JSON.stringify({
            event: "secret_used",
            secret_name: "API_KEY",
            timestamp: new Date().toISOString(),
            duration_ms: Date.now() - startTime,
            success: resp.ok
          })
        })
      );
      return resp;
    } catch (error) {
      ctx.waitUntil(
        fetch("https://log.example.com/log", {
          method: "POST",
          body: JSON.stringify({
            event: "secret_access_failed",
            secret_name: "API_KEY",
            error: error instanceof Error ? error.message : "Unknown"
          })
        })
      );
      return new Response("Error", { status: 500 });
    }
  }
}
```

