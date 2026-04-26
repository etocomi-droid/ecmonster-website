## Multiple Schedules

```typescript
export default {
  async scheduled(controller, env, ctx) {
    switch (controller.cron) {
      case "*/3 * * * *": ctx.waitUntil(updateRecentData(env)); break;
      case "0 * * * *": ctx.waitUntil(processHourlyAggregation(env)); break;
      case "0 2 * * *": ctx.waitUntil(performDailyMaintenance(env)); break;
      default: console.warn(`Unhandled: ${controller.cron}`);
    }
  },
};
```

