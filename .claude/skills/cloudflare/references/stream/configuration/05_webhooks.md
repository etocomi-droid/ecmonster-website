## Webhooks

**Setup webhook URL**
```bash
curl -X PUT \
  "https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/webhook" \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"notificationUrl": "https://your-worker.workers.dev/webhook"}'

# Save the returned `secret` for signature verification
```

**Store secret**
```bash
wrangler secret put WEBHOOK_SECRET
```

