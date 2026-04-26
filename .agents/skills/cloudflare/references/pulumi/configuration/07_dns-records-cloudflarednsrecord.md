## DNS Records (cloudflare.DnsRecord)

```typescript
const zone = cloudflare.getZone({name: "example.com"});
const record = new cloudflare.DnsRecord("www", {
    zoneId: zone.then(z => z.id), name: "www", type: "A",
    content: "192.0.2.1", ttl: 3600, proxied: true,
});
```

