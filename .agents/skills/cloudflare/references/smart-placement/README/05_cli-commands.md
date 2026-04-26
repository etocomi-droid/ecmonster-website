## CLI Commands

```bash
# Deploy with Smart Placement
wrangler deploy

# Check placement status
curl -H "Authorization: Bearer $TOKEN" \
  https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/services/$WORKER_NAME \
  | jq .result.placement_status

# Monitor
wrangler tail your-worker-name --header cf-placement
```

