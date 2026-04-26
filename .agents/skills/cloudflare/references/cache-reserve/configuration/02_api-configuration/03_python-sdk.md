### Python SDK

```bash
pip install cloudflare
```

```python
from cloudflare import Cloudflare

client = Cloudflare(api_token=os.environ.get("CLOUDFLARE_API_TOKEN"))

# Enable Cache Reserve
client.cache.cache_reserve.edit(
    zone_id="abc123",
    value="on"
)

# Get Cache Reserve status
status = client.cache.cache_reserve.get(zone_id="abc123")
print(status.value)  # 'on' or 'off'
```

