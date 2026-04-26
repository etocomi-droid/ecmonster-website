## Monitoring Commands

```bash
# Tail Worker logs
wrangler tail your-worker-name

# Tail with filters
wrangler tail your-worker-name --status error
wrangler tail your-worker-name --header cf-placement

# Check placement status via API
curl -H "Authorization: Bearer $TOKEN" \
  https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/services/$WORKER_NAME \
  | jq .result.placement_status
```

