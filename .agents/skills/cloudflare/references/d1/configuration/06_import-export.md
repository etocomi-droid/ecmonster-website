## Import & Export

```bash
# Export full database (schema + data)
wrangler d1 export <db-name> --remote --output=./backup.sql

# Export data only (no schema)
wrangler d1 export <db-name> --remote --no-schema --output=./data-only.sql

# Export with foreign key constraints preserved
# (Default: foreign keys are disabled during export for import compatibility)

# Import SQL file
wrangler d1 execute <db-name> --remote --file=./backup.sql

# Limitations
# - BLOB data may not export correctly (use R2 for binary files)
# - Very large exports (>1GB) may timeout (split into chunks)
# - Import is NOT atomic (use batch() for transactional imports in Workers)
```

