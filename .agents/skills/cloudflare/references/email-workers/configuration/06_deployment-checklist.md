## Deployment Checklist

- [ ] Enable Email Routing in dashboard
- [ ] Verify destination addresses
- [ ] Configure DMARC/SPF/DKIM for sending
- [ ] Create KV/R2 resources if needed
- [ ] Update wrangler.jsonc with production IDs

```bash
npx wrangler deploy
npx wrangler deployments list
```

