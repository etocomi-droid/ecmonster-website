## Python SDK

```python
from cloudflare import Cloudflare

client = Cloudflare(api_token=os.environ["CF_TOKEN"])

# List, create, status (same pattern as TypeScript)
client.network_interconnects.interconnects.list(account_id=id)
client.network_interconnects.interconnects.create(account_id=id, account=id, slot_id="slot_abc", type="direct", facility="EWR1", speed="10G")
client.network_interconnects.interconnects.get(account_id=id, icon=icon_id)

# CNI objects and slots
client.network_interconnects.cnis.create(account_id=id, cust_ip="192.0.2.1/31", cf_ip="192.0.2.0/31", bgp_asn=65000)
client.network_interconnects.slots.list(account_id=id, occupied=False)
```

