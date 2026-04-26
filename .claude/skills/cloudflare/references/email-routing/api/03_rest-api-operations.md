## REST API Operations

Base URL: `https://api.cloudflare.com/client/v4`

### Authentication

```bash
curl -H "Authorization: Bearer $API_TOKEN" https://api.cloudflare.com/client/v4/...
```

### Key Endpoints

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Enable routing | POST | `/zones/{zone_id}/email/routing/enable` |
| Disable routing | POST | `/zones/{zone_id}/email/routing/disable` |
| List rules | GET | `/zones/{zone_id}/email/routing/rules` |
| Create rule | POST | `/zones/{zone_id}/email/routing/rules` |
| Verify destination | POST | `/zones/{zone_id}/email/routing/addresses` |
| List destinations | GET | `/zones/{zone_id}/email/routing/addresses` |

### Create Routing Rule Example

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/email/routing/rules" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": true,
    "name": "Forward sales",
    "matchers": [{"type": "literal", "field": "to", "value": "sales@yourdomain.com"}],
    "actions": [{"type": "forward", "value": ["alice@company.com"]}],
    "priority": 0
  }'
```

Matcher types: `literal` (exact match), `all` (catch-all).
