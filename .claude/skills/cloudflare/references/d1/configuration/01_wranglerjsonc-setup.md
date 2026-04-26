## wrangler.jsonc Setup

```jsonc
{
  "name": "your-worker-name",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01", // Use current date for new projects
  "d1_databases": [
    {
      "binding": "DB",                    // Env variable name
      "database_name": "your-db-name",    // Human-readable name
      "database_id": "your-database-id",  // UUID from dashboard/CLI
      "migrations_dir": "migrations"      // Optional: default is "migrations"
    },
    // Read replica (paid plans only)
    {
      "binding": "DB_REPLICA",
      "database_name": "your-db-name",
      "database_id": "your-database-id"   // Same ID, different binding
    },
    // Multiple databases
    {
      "binding": "ANALYTICS_DB",
      "database_name": "analytics-db",
      "database_id": "yyy-yyy-yyy"
    }
  ]
}
```

