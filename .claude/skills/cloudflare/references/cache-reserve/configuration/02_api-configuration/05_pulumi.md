### Pulumi

```typescript
import * as cloudflare from "@pulumi/cloudflare";

// Enable Cache Reserve
const cacheReserve = new cloudflare.ZoneCacheReserve("example", {
  zoneId: zoneId,
  enabled: true,
});

// Enable Tiered Cache (required)
const tieredCache = new cloudflare.TieredCache("example", {
  zoneId: zoneId,
  cacheType: "smart",
});
```

