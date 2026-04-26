## Zone Management

```typescript
// List zones
const zones = await client.zones.list({
  account: { id: 'account-id' },
  status: 'active',
});

// Create zone
const zone = await client.zones.create({
  account: { id: 'account-id' },
  name: 'example.com',
  type: 'full', // or 'partial'
});

// Update zone
await client.zones.edit('zone-id', {
  paused: false,
});

// Delete zone
await client.zones.delete('zone-id');
```

```go
// Go: requires cloudflare.F() wrapper
zone, err := client.Zones.New(ctx, cloudflare.ZoneNewParams{
    Account: cloudflare.F(cloudflare.ZoneNewParamsAccount{
        ID: cloudflare.F("account-id"),
    }),
    Name: cloudflare.F("example.com"),
    Type: cloudflare.F(cloudflare.ZoneNewParamsTypeFull),
})
```

