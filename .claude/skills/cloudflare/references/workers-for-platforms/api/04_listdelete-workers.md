## List/Delete Workers

```bash
# List
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE/scripts" \
  -H "Authorization: Bearer $API_TOKEN"

# Delete by name
curl -X DELETE ".../scripts/$SCRIPT_NAME" -H "Authorization: Bearer $API_TOKEN"

# Delete by tag
curl -X DELETE ".../scripts?tags=customer-123%3Ayes" -H "Authorization: Bearer $API_TOKEN"
```

**Pagination:** SDK supports async iteration. Manual: add `?per_page=100&page=1` query params.

