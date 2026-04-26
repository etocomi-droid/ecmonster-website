### Get Argo Smart Routing Status

**Endpoint:** `GET /zones/{zone_id}/argo/smart_routing`

**Description:** Retrieves current Argo Smart Routing enablement status.

**cURL Example:**
```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/argo/smart_routing" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "result": {
    "id": "smart_routing",
    "value": "on",
    "editable": true,
    "modified_on": "2024-01-11T12:00:00Z"
  },
  "success": true,
  "errors": [],
  "messages": []
}
```

**TypeScript SDK Example:**
```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN
});

const status = await client.argo.smartRouting.get({ zone_id: 'your-zone-id' });
console.log(`Argo status: ${status.value}, editable: ${status.editable}`);
```

**Python SDK Example:**
```python
from cloudflare import Cloudflare

client = Cloudflare(api_token=os.environ.get('CLOUDFLARE_API_TOKEN'))

status = client.argo.smart_routing.get(zone_id='your-zone-id')
print(f"Argo status: {status.value}, editable: {status.editable}")
```

