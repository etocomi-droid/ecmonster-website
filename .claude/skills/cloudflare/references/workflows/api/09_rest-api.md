## REST API

```bash
# Create
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/workflows/{workflow_name}/instances" -H "Authorization: Bearer {token}" -d '{"id":"custom-id","params":{"userId":"user123"}}'

# Status
curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/status" -H "Authorization: Bearer {token}"

# Send Event
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/events" -H "Authorization: Bearer {token}" -d '{"type":"approval","payload":{"approved":true}}'
```

See: [configuration.md](./configuration.md), [patterns.md](./patterns.md)
