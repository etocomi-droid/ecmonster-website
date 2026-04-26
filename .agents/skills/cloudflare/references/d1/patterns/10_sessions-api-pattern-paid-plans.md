## Sessions API Pattern (Paid Plans)

```typescript
// Migration with long-running session (up to 15 min)
async function runMigration(env: Env) {
  const session = env.DB.withSession({ timeout: 600 }); // 10 min
  try {
    await session.prepare('CREATE INDEX idx_users_email ON users(email)').run();
    await session.prepare('CREATE INDEX idx_posts_user ON posts(user_id)').run();
    await session.prepare('ANALYZE').run();
  } finally {
    session.close(); // Always close to prevent leaks
  }
}

// Bulk transformation with batching
async function transformLargeDataset(env: Env) {
  const session = env.DB.withSession({ timeout: 900 }); // 15 min max
  try {
    const BATCH_SIZE = 1000;
    let offset = 0;
    while (true) {
      const rows = await session.prepare('SELECT id, data FROM legacy LIMIT ? OFFSET ?').bind(BATCH_SIZE, offset).all();
      if (rows.results.length === 0) break;
      const updates = rows.results.map(row => 
        session.prepare('UPDATE legacy SET new_data = ? WHERE id = ?').bind(transform(row.data), row.id)
      );
      await session.batch(updates);
      offset += BATCH_SIZE;
    }
  } finally { session.close(); }
}
```

