## cURL

```bash
# List interconnects
curl "https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/cni/interconnects" \
  -H "Authorization: Bearer ${CF_TOKEN}"

# Create interconnect
curl -X POST "https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/cni/interconnects?validate_only=true" \
  -H "Authorization: Bearer ${CF_TOKEN}" -H "Content-Type: application/json" \
  -d '{"account": "id", "slot_id": "slot_abc", "type": "direct", "facility": "EWR1", "speed": "10G"}'

# LOA PDF
curl "https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/cni/interconnects/${ICON_ID}/loa" \
  -H "Authorization: Bearer ${CF_TOKEN}" --output loa.pdf
```

