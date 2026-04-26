## DNS Analytics

```graphql
query DNSQueryVolume($zoneTag: string!, $start: Time!, $end: Time!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      dnsAnalyticsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }
        limit: 500
        orderBy: [datetimeFiveMinutes_ASC]
      ) {
        count
        dimensions { datetimeFiveMinutes }
      }
    }
  }
}
```

