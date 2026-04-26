## Handler Parameters

**`controller: ScheduledController`**
- Access cron expression and scheduled time

**`env: Env`**
- All bindings: KV, R2, D1, secrets, service bindings

**`ctx: ExecutionContext`**
- `ctx.waitUntil(promise)` - Extend execution for async tasks (logging, cleanup, external APIs)
- First `waitUntil` failure recorded in Cron Events

