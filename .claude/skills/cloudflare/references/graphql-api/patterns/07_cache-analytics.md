## Cache Analytics

```graphql
query CacheStatusBreakdown($zoneTag: string!, $start: Time!, $end: Time!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpRequestsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }
        limit: 20
        orderBy: [count_DESC]
      ) {
        count
        dimensions { cacheStatus }
        sum { edgeResponseBytes }
      }
    }
  }
}
```

For cache hit ratio over time, use aliases to query the same dataset twice — once with `cacheStatus: "hit"` filter and once without — then compute the ratio client-side.

