## Auto-Pagination

All SDKs support automatic pagination for list operations.

```typescript
// TypeScript: for await...of
for await (const zone of client.zones.list()) {
  console.log(zone.id);
}
```

```python
# Python: iterator protocol
for zone in client.zones.list():
    print(zone.id)
```

```go
// Go: ListAutoPaging
iter := client.Zones.ListAutoPaging(ctx, cloudflare.ZoneListParams{})
for iter.Next() {
    zone := iter.Current()
    fmt.Println(zone.ID)
}
```

