## Best Practices

- **Design**: Use `idFromName()` for coordination, `newUniqueId()` for sharding, minimize constructor work
- **Storage**: Prefer SQLite, batch with transactions, set alarms for cleanup, use PITR before risky ops
- **Performance**: ~1K req/s per DO max - shard for more, cache in memory, use alarms for deferred work
- **Reliability**: Handle 503 with retry+backoff, design for cold starts, test migrations with `--dry-run`
- **Security**: Validate inputs in Workers, rate limit DO creation, use jurisdiction for compliance

