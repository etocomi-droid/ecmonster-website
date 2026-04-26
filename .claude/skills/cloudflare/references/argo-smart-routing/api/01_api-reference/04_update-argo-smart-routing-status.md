### Update Argo Smart Routing Status

**Endpoint:** `PATCH /zones/{zone_id}/argo/smart_routing`

**Description:** Enable or disable Argo Smart Routing for a zone.

**Request Body:**
```json
{
  "value": "on"  // or "off"
}
```

**cURL Example:**
```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/argo/smart_routing" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"value": "on"}'
```

**TypeScript SDK Example:**
```typescript
const result = await client.argo.smartRouting.edit({
  zone_id: 'your-zone-id',
  value: 'on',
});
console.log(`Updated: ${result.value} at ${result.modified_on}`);
```

**Python SDK Example:**
```python
result = client.argo.smart_routing.edit(
    zone_id='your-zone-id',
    value='on'
)
print(f"Updated: {result.value} at {result.modified_on}")
```

