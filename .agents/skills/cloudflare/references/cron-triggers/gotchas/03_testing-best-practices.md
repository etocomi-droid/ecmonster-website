## Testing Best Practices

**Unit tests:**
- Mock `ScheduledController`, `ExecutionContext`, and bindings
- Test each cron expression separately
- Verify `noRetry()` is called when expected
- Use Vitest with `@cloudflare/vitest-pool-workers` for realistic env

**Integration tests:**
- Test via `/__scheduled` endpoint in dev environment
- Verify idempotency logic with duplicate `scheduledTime` values
- Test error handling and retry behavior

**Production:** Start with long intervals (`*/30 * * * *`), monitor Cron Events for 24h, set up alerts before reducing interval

