## Deployment

```bash
npx wrangler deploy
```

**Connect to Email Routing:**

Dashboard: Email > Email Routing > [domain] > Settings > Email Workers > Select worker

API:
```bash
curl -X PUT "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/email/routing/settings" \
  -H "Authorization: Bearer $API_TOKEN" \
  -d '{"enabled": true, "worker": "email-worker"}'
```

