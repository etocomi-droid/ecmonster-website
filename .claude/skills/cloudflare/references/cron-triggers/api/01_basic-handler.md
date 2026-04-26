## Basic Handler

```typescript
export default {
  async scheduled(controller: ScheduledController, env: Env, ctx: ExecutionContext): Promise<void> {
    console.log("Cron executed:", new Date(controller.scheduledTime));
  },
};
```

**JavaScript:** Same signature without types  
**Python:** `class Default(WorkerEntrypoint): async def scheduled(self, controller, env, ctx)`

