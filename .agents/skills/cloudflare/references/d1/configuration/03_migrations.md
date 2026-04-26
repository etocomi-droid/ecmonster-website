## Migrations

File structure: `migrations/0001_initial_schema.sql`, `0002_add_posts.sql`, etc.

### Example Migration

```sql
-- migrations/0001_initial_schema.sql
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);

CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  content TEXT,
  published BOOLEAN DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_published ON posts(published);
```

### Running Migrations

```bash
# Create new migration file
wrangler d1 migrations create <db-name> add_users_table
# Creates: migrations/0001_add_users_table.sql

# Apply migrations
wrangler d1 migrations apply <db-name> --local     # Apply to local DB
wrangler d1 migrations apply <db-name> --remote    # Apply to production DB

# List applied migrations
wrangler d1 migrations list <db-name> --remote

# Direct SQL execution (bypasses migration tracking)
wrangler d1 execute <db-name> --remote --command="SELECT * FROM users"
wrangler d1 execute <db-name> --local --file=./schema.sql
```

**Migration tracking**: Wrangler creates `d1_migrations` table automatically to track applied migrations

