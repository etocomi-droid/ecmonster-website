## REST API

```bash
curl https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/meta/llama-3.1-8b-instruct \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"messages":[{"role":"user","content":"Hello"}]}'
```

