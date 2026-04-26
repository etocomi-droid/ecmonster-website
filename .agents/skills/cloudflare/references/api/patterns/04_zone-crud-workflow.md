## Zone CRUD Workflow

```typescript
// Create
const zone = await client.zones.create({
  account: { id: 'account-id' },
  name: 'example.com',
  type: 'full',
});

// Read
const fetched = await client.zones.get({ zone_id: zone.id });

// Update
await client.zones.edit(zone.id, { paused: false });

// Delete
await client.zones.delete(zone.id);
```

