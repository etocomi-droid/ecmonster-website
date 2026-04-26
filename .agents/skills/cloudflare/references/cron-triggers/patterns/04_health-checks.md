## Health Checks

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const services = [{name: "API", url: "https://api.example.com/health"}, {name: "CDN", url: "https://cdn.example.com/health"}];
    const checks = await Promise.all(services.map(async (service) => {
      const start = Date.now();
      try {
        const response = await fetch(service.url, { signal: AbortSignal.timeout(5000) });
        return {name: service.name, status: response.ok ? "up" : "down", responseTime: Date.now() - start};
      } catch (error) {
        return {name: service.name, status: "down", responseTime: Date.now() - start, error: error.message};
      }
    }));
    ctx.waitUntil(env.STATUS_KV.put("health_status", JSON.stringify(checks)));
    const failures = checks.filter(c => c.status === "down");
    if (failures.length > 0) ctx.waitUntil(fetch(env.ALERT_WEBHOOK, {method: "POST", body: JSON.stringify({text: `${failures.length} service(s) down: ${failures.map(f => f.name).join(", ")}`})}));
  },
};
```

