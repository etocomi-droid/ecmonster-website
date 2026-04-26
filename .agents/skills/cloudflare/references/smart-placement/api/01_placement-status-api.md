## Placement Status API

Query Worker placement status via Cloudflare API:

```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/workers/services/{WORKER_NAME}" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json"
```

Response includes `placement_status` field:

```typescript
type PlacementStatus = 
  | undefined  // Not yet analyzed
  | 'SUCCESS'  // Successfully optimized
  | 'INSUFFICIENT_INVOCATIONS'  // Not enough traffic
  | 'UNSUPPORTED_APPLICATION';  // Made Worker slower (reverted)
```

