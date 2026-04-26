## Time Travel & Backups

```bash
wrangler d1 time-travel restore <db-name> --timestamp="2024-01-15T14:30:00Z"  # Point-in-time
wrangler d1 time-travel info <db-name>  # List restore points (7 days free, 30 days paid)
wrangler d1 export <db-name> --remote --output=./backup.sql  # Full export
wrangler d1 export <db-name> --remote --no-schema --output=./data.sql  # Data only
wrangler d1 execute <db-name> --remote --file=./backup.sql  # Import
```
