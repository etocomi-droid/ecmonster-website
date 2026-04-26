## Finding Your Zone and Account IDs

- **Zone ID**: Dashboard > select zone > Overview (right sidebar), or via API
- **Account ID**: Dashboard > Account Home URL, or via API

```bash
curl -s https://api.cloudflare.com/client/v4/zones -H "Authorization: Bearer $CF_API_TOKEN" | jq '.result[] | {name, id}'
curl -s https://api.cloudflare.com/client/v4/accounts -H "Authorization: Bearer $CF_API_TOKEN" | jq '.result[] | {name, id}'
```

