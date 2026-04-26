## HTTP Ingest API

### Endpoint Format

```
https://{stream-id}.ingest.cloudflare.com
```

Get `{stream-id}` from: `npx wrangler pipelines streams list`

### Request Format

**CRITICAL:** Must send array, not single object

```bash
# ✅ Correct
curl -X POST https://{stream-id}.ingest.cloudflare.com \
  -H "Content-Type: application/json" \
  -d '[{"user_id": "123", "event_type": "purchase"}]'

# ❌ Wrong - will fail
curl -X POST https://{stream-id}.ingest.cloudflare.com \
  -H "Content-Type: application/json" \
  -d '{"user_id": "123", "event_type": "purchase"}'
```

### Authentication

```bash
curl -X POST https://{stream-id}.ingest.cloudflare.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '[{"event": "data"}]'
```

**Required permission:** Workers Pipeline Send

Create token: Dashboard → Workers → API tokens → Create with Pipeline Send permission

### Response Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Accepted | Success |
| 400 | Invalid format | Check JSON array, schema match |
| 401 | Auth failed | Verify token valid |
| 413 | Payload too large | Split into smaller batches (<1 MB) |
| 429 | Rate limited | Back off, retry with delay |
| 5xx | Server error | Retry with exponential backoff |

