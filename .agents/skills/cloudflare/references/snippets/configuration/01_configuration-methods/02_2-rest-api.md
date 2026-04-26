### 2. REST API
**Best for**: CI/CD, automation, programmatic management

```bash
# Create/update snippet
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/snippets/$SNIPPET_NAME" \
  --request PUT \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --form "files=@example.js" \
  --form "metadata={\"main_module\": \"example.js\"}"

# Create snippet rule
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/snippets/snippet_rules" \
  --request PUT \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "rules": [
      {
        "description": "Trigger snippet on /api paths",
        "enabled": true,
        "expression": "starts_with(http.request.uri.path, \"/api/\")",
        "snippet_name": "api_snippet"
      }
    ]
  }'

# List snippets
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/snippets" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

# Delete snippet
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/snippets/$SNIPPET_NAME" \
  --request DELETE \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

