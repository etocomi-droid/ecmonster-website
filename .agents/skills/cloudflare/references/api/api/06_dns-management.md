## DNS Management

```typescript
// Create DNS record
await client.dns.records.create({
  zone_id: 'zone-id',
  type: 'A',
  name: 'subdomain.example.com',
  content: '192.0.2.1',
  ttl: 1, // auto
  proxied: true, // Orange cloud
});

// List DNS records (with auto-pagination)
for await (const record of client.dns.records.list({
  zone_id: 'zone-id',
  type: 'A',
})) {
  console.log(record.name, record.content);
}

// Update DNS record
await client.dns.records.update({
  zone_id: 'zone-id',
  dns_record_id: 'record-id',
  type: 'A',
  name: 'subdomain.example.com',
  content: '203.0.113.1',
  proxied: true,
});

// Delete DNS record
await client.dns.records.delete({
  zone_id: 'zone-id',
  dns_record_id: 'record-id',
});
```

```python
# Python example
client.dns.records.create(
    zone_id="zone-id",
    type="A",
    name="subdomain.example.com",
    content="192.0.2.1",
    ttl=1,
    proxied=True,
)
```

