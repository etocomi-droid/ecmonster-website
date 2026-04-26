## Sessions API (Paid Plans)

Long-running sessions for operations exceeding 30s timeout (up to 15 min).

```typescript
const session = env.DB.withSession({ timeout: 600 }); // 10 min (1-900s)
try {
  await session.prepare('CREATE INDEX idx_large ON big_table(column)').run();
  await session.prepare('ANALYZE').run();
} finally {
  session.close(); // CRITICAL: always close to prevent leaks
}
```

**Use cases**: Migrations, ANALYZE, large index creation, bulk transformations

