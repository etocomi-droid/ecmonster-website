## Filter and Collect Results

```typescript
// Find all proxied A records
const proxiedRecords = [];
for await (const record of client.dns.records.list({
  zone_id: 'zone-id',
  type: 'A',
})) {
  if (record.proxied) {
    proxiedRecords.push(record);
  }
}
```

