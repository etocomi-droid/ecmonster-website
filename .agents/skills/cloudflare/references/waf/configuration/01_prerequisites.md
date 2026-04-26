## Prerequisites

**API Token**: Create at https://dash.cloudflare.com/profile/api-tokens
- Permission: `Zone.WAF Edit` or `Zone.Firewall Services Edit`
- Zone Resources: Include specific zones or all zones

**Zone ID**: Found in dashboard > Overview > API section (right sidebar)

```bash
# Set environment variables
export CF_API_TOKEN="your_api_token_here"
export ZONE_ID="your_zone_id_here"
```

