## Query Execution Methods

```typescript
// .all() - Returns all rows
const { results, success, meta } = await env.DB.prepare('SELECT * FROM users WHERE active = ?').bind(true).all();
// results: Array of row objects; success: boolean
// meta: { duration: number, rows_read: number, rows_written: number }

// .first() - Returns first row or null
const user = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();

// .first(columnName) - Returns single column value
const email = await env.DB.prepare('SELECT email FROM users WHERE id = ?').bind(userId).first('email');
// Returns string | number | null

// .run() - For INSERT/UPDATE/DELETE (no row data returned)
const result = await env.DB.prepare('UPDATE users SET last_login = ? WHERE id = ?').bind(Date.now(), userId).run();
// result.meta: { duration, rows_read, rows_written, last_row_id, changes }

// .raw() - Returns array of arrays (efficient for large datasets)
const rawResults = await env.DB.prepare('SELECT id, name FROM users').raw();
// [[1, 'Alice'], [2, 'Bob']]
```

