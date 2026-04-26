## TypeScript SDK

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({ apiToken: process.env.CF_TOKEN });

// List
await client.networkInterconnects.interconnects.list({ account_id: id });

// Create with validation
await client.networkInterconnects.interconnects.create({
  account_id: id,
  account: id,
  slot_id: 'slot_abc',
  type: 'direct',
  facility: 'EWR1',
  speed: '10G',
  name: 'prod-interconnect',
}, {
  query: { validate_only: true }, // Dry-run validation
});

// Create without validation
await client.networkInterconnects.interconnects.create({
  account_id: id,
  account: id,
  slot_id: 'slot_abc',
  type: 'direct',
  facility: 'EWR1',
  speed: '10G',
  name: 'prod-interconnect',
});

// Status
await client.networkInterconnects.interconnects.get(accountId, iconId);

// LOA (use fetch)
const res = await fetch(`https://api.cloudflare.com/client/v4/accounts/${id}/cni/interconnects/${iconId}/loa`, {
  headers: { Authorization: `Bearer ${token}` },
});
await fs.writeFile('loa.pdf', Buffer.from(await res.arrayBuffer()));

// CNI object
await client.networkInterconnects.cnis.create({
  account_id: id,
  account: id,
  cust_ip: '192.0.2.1/31',
  cf_ip: '192.0.2.0/31',
  bgp_asn: 65000,
  vlan: 100,
});

// Slots (filter by facility and speed)
await client.networkInterconnects.slots.list({
  account_id: id,
  occupied: false,
  facility: 'EWR1',
  speed: '10G',
});
```

