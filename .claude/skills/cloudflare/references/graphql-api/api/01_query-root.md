## Query Root

The schema has a single entry point: `Query.viewer`. Mutations are not supported.

```graphql
{
  cost       # uint64 -- query cost (returned in response)
  viewer {
    budget   # uint64 -- remaining budget
    zones(filter: { zoneTag: "..." }) { ... }
    accounts(filter: { accountTag: "..." }) { ... }
  }
}
```

