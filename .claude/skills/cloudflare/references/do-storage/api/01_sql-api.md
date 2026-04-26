## SQL API

```typescript
const cursor = this.sql.exec('SELECT * FROM users WHERE email = ?', email);
for (let row of cursor) {} // Objects: { id, name, email }
cursor.toArray(); cursor.one(); // Single row (throws if != 1)
for (let row of cursor.raw()) {} // Arrays: [1, "Alice", "..."]

// Manual iteration
const iter = cursor[Symbol.iterator]();
const first = iter.next(); // { value: {...}, done: false }

cursor.columnNames; // ["id", "name", "email"]
cursor.rowsRead; cursor.rowsWritten; // Billing

type User = { id: number; name: string; email: string };
const user = this.sql.exec<User>('...', userId).one();
```

