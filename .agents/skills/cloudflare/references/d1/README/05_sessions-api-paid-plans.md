## Sessions API (Paid Plans)

```typescript
// Create long-running session for analytics/migrations (up to 15 minutes)
const session = env.DB.withSession();
try {
  await session.prepare('CREATE INDEX idx_heavy ON large_table(column)').run();
  await session.prepare('ANALYZE').run();
} finally {
  session.close(); // Always close to release resources
}
```

