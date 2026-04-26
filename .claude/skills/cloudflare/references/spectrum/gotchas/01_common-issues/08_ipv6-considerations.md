### IPv6 Considerations

**Problem:** IPv6 clients can't connect or origin doesn't support IPv6  
**Solution:** Configure `edge_ips.connectivity`

```typescript
const app = await client.spectrum.apps.create({
  // ...
  edge_ips: {
    type: 'dynamic',
    connectivity: 'ipv4',  // Options: 'all', 'ipv4', 'ipv6'
  },
});
```

**Options:**
- `all`: Dual-stack (default, requires origin support both)
- `ipv4`: IPv4 only (use if origin lacks IPv6)
- `ipv6`: IPv6 only (rare)

