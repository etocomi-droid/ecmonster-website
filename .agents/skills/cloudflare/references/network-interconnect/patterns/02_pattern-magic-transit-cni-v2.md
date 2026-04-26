## Pattern: Magic Transit + CNI v2

**Use Case:** DDoS protection, private connectivity, no GRE overhead.

```typescript
// 1. Create interconnect
const ic = await client.networkInterconnects.interconnects.create({
  account_id: id,
  type: 'direct',
  facility: 'EWR1',
  speed: '10G',
  name: 'magic-transit-primary',
});

// 2. Poll until active
const status = await pollUntilActive(id, ic.id);

// 3. Configure Magic Transit tunnel via Dashboard/API
```

**Benefits:** 1500 MTU both ways, simplified routing.

