## Authentication

### API Token (Recommended)

Generate at: Dashboard → My Profile → API Tokens

Required permissions:
- Account → Cloudflare Images → Edit

```bash
curl -H "Authorization: Bearer {api_token}" \
  https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1
```

### API Key (Legacy)

```bash
curl -H "X-Auth-Email: {email}" \
     -H "X-Auth-Key: {api_key}" \
  https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1
```

