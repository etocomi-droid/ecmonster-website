## Multi-Dataset Queries

A single request can query multiple datasets, avoiding extra HTTP round-trips:

```graphql
query DashboardOverview($zoneTag: string!, $start: Time!, $end: Time!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpTraffic: httpRequestsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }, limit: 1
      ) { count  sum { edgeResponseBytes }  ratio { status4xx status5xx } }
      firewallEvents: firewallEventsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }, limit: 5, orderBy: [count_DESC]
      ) { count  dimensions { action source } }
      dnsQueries: dnsAnalyticsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }, limit: 1
      ) { count }
    }
  }
}
```

