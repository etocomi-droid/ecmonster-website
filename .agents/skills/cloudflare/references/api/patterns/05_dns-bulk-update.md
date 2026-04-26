## DNS Bulk Update

```typescript
// Fetch all A records
const records = [];
for await (const record of client.dns.records.list({
  zone_id: 'zone-id',
  type: 'A',
})) {
  records.push(record);
}

// Update all to new IP
await Promise.all(records.map(record =>
  client.dns.records.update({
    zone_id: 'zone-id',
    dns_record_id: record.id,
    type: 'A',
    name: record.name,
    content: '203.0.113.1', // New IP
    proxied: record.proxied,
    ttl: record.ttl,
  })
));
```

