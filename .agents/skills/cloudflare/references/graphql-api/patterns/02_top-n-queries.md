## Top-N Queries

### Top Countries by Request Count

```graphql
query TopCountries($zoneTag: string!, $start: Time!, $end: Time!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpRequestsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }
        limit: 10
        orderBy: [count_DESC]
      ) {
        count
        dimensions { clientCountryName }
      }
    }
  }
}
```

Use `orderBy: [sum_edgeResponseBytes_DESC]` for top paths by bandwidth. Add `edgeResponseStatus_geq: 400` to the filter for top error status codes.

