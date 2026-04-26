## Python SDK

```python
from cloudflare import Cloudflare

client = Cloudflare(api_token="your-api-token")

# Create
app = client.spectrum.apps.create(
    zone_id="your-zone-id",
    protocol="tcp/22",
    dns={"type": "CNAME", "name": "ssh.example.com"},
    origin_direct=["tcp://192.0.2.1:22"],
    ip_firewall=True,
    tls="off",
)

# List
apps = client.spectrum.apps.list(zone_id="your-zone-id")

# Get
app_details = client.spectrum.apps.get(zone_id="your-zone-id", app_id=app.id)

# Update
client.spectrum.apps.update(zone_id="your-zone-id", app_id=app.id, tls="full")

# Delete
client.spectrum.apps.delete(zone_id="your-zone-id", app_id=app.id)

# Analytics
analytics = client.spectrum.analytics.aggregate(
    zone_id="your-zone-id",
    metrics=["bytesIngress", "bytesEgress"],
    since=datetime.now() - timedelta(hours=1),
)
```

