## Pipelines Integration

Stream data to Iceberg tables via Pipelines, then query with R2 SQL.

```bash
# Setup pipeline (select Data Catalog Table destination)
npx wrangler pipelines setup

# Key settings:
# - Destination: Data Catalog Table
# - Compression: zstd (recommended)
# - Roll file time: 300+ sec (production), 10 sec (dev)

# Send data to pipeline
curl -X POST https://{stream-id}.ingest.cloudflare.com \
  -H "Content-Type: application/json" \
  -d '[{"user_id": "user_123", "event_type": "purchase", "timestamp": "2025-01-15T10:30:00Z", "amount": 29.99}]'

# Query ingested data (wait for roll interval)
npx wrangler r2 sql query "my-bucket" "
  SELECT event_type, COUNT(*), SUM(amount)
  FROM default.events
  WHERE timestamp >= '2025-01-15T00:00:00Z'
  GROUP BY event_type
"
```

See [pipelines/patterns.md](../pipelines/patterns.md) for detailed setup.

