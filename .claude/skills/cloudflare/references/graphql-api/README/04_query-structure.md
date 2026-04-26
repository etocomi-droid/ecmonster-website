## Query Structure

Every query follows this pattern:

```graphql
{
  viewer {
    # Zone-scoped
    zones(filter: { zoneTag: "ZONE_ID" }) {
      datasetName(
        filter: { datetime_gt: "...", datetime_lt: "..." }
        limit: 1000
        orderBy: [datetimeFiveMinutes_DESC]
      ) {
        count
        dimensions { ... }
        sum { ... }
      }
    }
    # Account-scoped
    accounts(filter: { accountTag: "ACCOUNT_ID" }) {
      datasetName(filter: { ... }, limit: 100) {
        count
        dimensions { ... }
        sum { ... }
      }
    }
  }
}
```

