## Indexing Strategy

```sql
-- Index frequently queried columns
CREATE INDEX idx_users_email ON users(email);

-- Composite indexes for multi-column queries
CREATE INDEX idx_posts_user_published ON posts(user_id, published);

-- Covering indexes (include queried columns)
CREATE INDEX idx_users_email_name ON users(email, name);

-- Partial indexes for filtered queries
CREATE INDEX idx_active_users ON users(email) WHERE active = 1;

-- Check if query uses index
EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?;
```

