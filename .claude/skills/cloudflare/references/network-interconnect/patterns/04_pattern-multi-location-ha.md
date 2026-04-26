## Pattern: Multi-Location HA

**Use Case:** 99.99%+ uptime.

```typescript
// Primary (NY)
const primary = await client.networkInterconnects.interconnects.create({
  account_id: id,
  type: 'direct',
  facility: 'EWR1',
  speed: '10G',
  name: 'primary-ewr1',
});

// Secondary (NY, different hardware)
const secondary = await client.networkInterconnects.interconnects.create({
  account_id: id,
  type: 'direct',
  facility: 'EWR2',
  speed: '10G',
  name: 'secondary-ewr2',
});

// Tertiary (LA, different geography)
const tertiary = await client.networkInterconnects.interconnects.create({
  account_id: id,
  type: 'partner',
  facility: 'LAX1',
  speed: '10G',
  name: 'tertiary-lax1',
});

// BGP local preferences:
// Primary: 200
// Secondary: 150
// Tertiary: 100
// Internet: Last resort
```

