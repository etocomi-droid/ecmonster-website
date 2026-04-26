## SDK-Specific Issues

### Go: Required Field Wrapper

**Problem:** Go SDK requires `cloudflare.F()` wrapper for optional fields.

```go
// ❌ WRONG - Won't compile or send field
client.Zones.New(ctx, cloudflare.ZoneNewParams{
    Name: "example.com",
})

// ✅ CORRECT
client.Zones.New(ctx, cloudflare.ZoneNewParams{
    Name: cloudflare.F("example.com"),
    Account: cloudflare.F(cloudflare.ZoneNewParamsAccount{
        ID: cloudflare.F("account-id"),
    }),
})
```

**Why:** Distinguishes between zero value, null, and omitted fields.

### Python: Async vs Sync Clients

**Problem:** Using sync client in async context or vice versa.

```python
# ❌ WRONG - Can't await sync client
from cloudflare import Cloudflare
client = Cloudflare()
await client.zones.list()  # TypeError

# ✅ CORRECT - Use AsyncCloudflare
from cloudflare import AsyncCloudflare
client = AsyncCloudflare()
await client.zones.list()
```

