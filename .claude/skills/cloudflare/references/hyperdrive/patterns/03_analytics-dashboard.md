## Analytics Dashboard

```typescript
const client = new Client({connectionString: env.HYPERDRIVE.connectionString});
await client.connect();

// Aggregate queries cached (use fixed timestamps for caching)
const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();
const dailyStats = await client.query(`
  SELECT DATE(created_at) as date, COUNT(*) as orders, SUM(amount) as revenue
  FROM orders WHERE created_at >= $1
  GROUP BY DATE(created_at) ORDER BY date DESC
`, [thirtyDaysAgo]);

const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString();
const topProducts = await client.query(`
  SELECT p.name, COUNT(oi.id) as count, SUM(oi.quantity * oi.price) as revenue
  FROM order_items oi JOIN products p ON oi.product_id = p.id
  WHERE oi.created_at >= $1
  GROUP BY p.id, p.name ORDER BY revenue DESC LIMIT 10
`, [sevenDaysAgo]);
```

**Benefits:** Expensive aggregations cached (avoid NOW() for cacheability), dashboard instant, reduced DB load.

