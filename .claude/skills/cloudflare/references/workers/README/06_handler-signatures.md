## Handler Signatures

```typescript
// HTTP requests
async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response>

// Cron triggers
async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void>

// Queue consumer
async queue(batch: MessageBatch, env: Env, ctx: ExecutionContext): Promise<void>

// Tail consumer
async tail(events: TraceItem[], env: Env, ctx: ExecutionContext): Promise<void>
```

