## Data Sources

**Get Zone:**
```typescript
const zone = cloudflare.getZone({name: "example.com"});
const zoneId = zone.then(z => z.id);
```

**Get Accounts (via API):**
Use Cloudflare API directly or custom dynamic resources.

