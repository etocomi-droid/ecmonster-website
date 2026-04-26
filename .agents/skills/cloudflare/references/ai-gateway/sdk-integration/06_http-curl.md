## HTTP / cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account}/{gateway}/openai/chat/completions \
  -H "Authorization: Bearer $OPENAI_KEY" \
  -H "cf-aig-authorization: Bearer $CF_TOKEN" \
  -H "cf-aig-metadata: {\"userId\":\"123\"}" \
  -d '{"model":"gpt-4o","messages":[...]}'
```

