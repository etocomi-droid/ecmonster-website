## HTTP API Query

For programmatic access from external systems (not Workers - see gotchas.md).

```bash
curl -X POST https://api.cloudflare.com/client/v4/accounts/{account_id}/r2/sql/query \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "warehouse": "my-bucket",
    "query": "SELECT * FROM default.my_table WHERE status = 200 LIMIT 100"
  }'
```

Response:
```json
{
  "success": true,
  "result": [{"user_id": "user_123", "timestamp": "2025-01-15T10:30:00Z", "status": 200}],
  "errors": []
}
```

