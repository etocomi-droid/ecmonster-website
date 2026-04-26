## List All with Auto-Pagination

**Problem:** API returns paginated results. Default page size is 20.

**Solution:** Use SDK auto-pagination to iterate all results.

```typescript
// TypeScript
for await (const zone of client.zones.list()) {
  console.log(zone.name);
}
```

```python
# Python
for zone in client.zones.list():
    print(zone.name)
```

```go
// Go
iter := client.Zones.ListAutoPaging(ctx, cloudflare.ZoneListParams{})
for iter.Next() {
    fmt.Println(iter.Current().Name)
}
```

