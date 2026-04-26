## Monitoring & Observability

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const startTime = Date.now();
    const meta = { cron: controller.cron, scheduledTime: controller.scheduledTime };
    console.log("[START]", meta);
    try {
      const result = await performTask(env);
      console.log("[SUCCESS]", { ...meta, duration: Date.now() - startTime, count: result.count });
      ctx.waitUntil(env.METRICS.put(`cron:${controller.scheduledTime}`, JSON.stringify({ ...meta, status: "success" }), { expirationTtl: 2592000 }));
    } catch (error) {
      console.error("[ERROR]", { ...meta, duration: Date.now() - startTime, error: error.message });
      ctx.waitUntil(fetch(env.ALERT_WEBHOOK, { method: "POST", body: JSON.stringify({ text: `Cron failed: ${controller.cron}`, error: error.message }) }));
      throw error;
    }
  },
};
```

**View logs:** `npx wrangler tail` or Dashboard → Workers & Pages → Worker → Logs

