## Analytics API

**Metrics:**
- `bytesIngress` - Bytes received from clients
- `bytesEgress` - Bytes sent to clients
- `count` - Number of connections
- `duration` - Connection duration (seconds)

**Dimensions:**
- `event` - Connection event type
- `appID` - Spectrum application ID
- `coloName` - Datacenter name
- `ipVersion` - IPv4 or IPv6

**Example:**
```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/analytics/aggregate/current?metrics=bytesIngress,bytesEgress,count&dimensions=appID" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

