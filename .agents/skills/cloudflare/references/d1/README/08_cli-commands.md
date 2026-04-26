## CLI Commands

```bash
# Database management
wrangler d1 create <db-name>
wrangler d1 list
wrangler d1 delete <db-name>

# Migrations
wrangler d1 migrations create <db-name> <migration-name>    # Create new migration file
wrangler d1 migrations apply <db-name> --remote             # Apply pending migrations
wrangler d1 migrations apply <db-name> --local              # Apply locally
wrangler d1 migrations list <db-name> --remote              # Show applied migrations

# Direct SQL execution
wrangler d1 execute <db-name> --remote --command="SELECT * FROM users"
wrangler d1 execute <db-name> --local --file=./schema.sql

# Backups & Import/Export
wrangler d1 export <db-name> --remote --output=./backup.sql  # Full export with schema
wrangler d1 export <db-name> --remote --no-schema --output=./data.sql  # Data only
wrangler d1 time-travel restore <db-name> --timestamp="2024-01-15T14:30:00Z"  # Point-in-time recovery

# Development
wrangler dev --persist-to=./.wrangler/state
```

