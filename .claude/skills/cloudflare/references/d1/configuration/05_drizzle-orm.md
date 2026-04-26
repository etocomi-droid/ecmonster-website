## Drizzle ORM

```typescript
// drizzle.config.ts
export default {
  schema: './src/schema.ts', out: './migrations', dialect: 'sqlite', driver: 'd1-http',
  dbCredentials: { accountId: process.env.CLOUDFLARE_ACCOUNT_ID!, databaseId: process.env.D1_DATABASE_ID!, token: process.env.CLOUDFLARE_API_TOKEN! }
} satisfies Config;

// schema.ts
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';
export const users = sqliteTable('users', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  email: text('email').notNull().unique(),
  name: text('name').notNull()
});

// worker.ts
import { drizzle } from 'drizzle-orm/d1';
import { users } from './schema';
export default {
  async fetch(request: Request, env: Env) {
    const db = drizzle(env.DB);
    return Response.json(await db.select().from(users));
  }
}
```

