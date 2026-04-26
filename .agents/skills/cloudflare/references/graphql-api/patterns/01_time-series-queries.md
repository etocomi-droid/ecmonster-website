## Time-Series Queries

Use time dimension granularity matching your range (see Best Practices below).

```graphql
query TrafficTimeSeries($zoneTag: string!, $start: Time!, $end: Time!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpRequestsAdaptiveGroups(
        filter: { datetime_gt: $start, datetime_lt: $end }
        limit: 1000
        orderBy: [datetimeFiveMinutes_ASC]  # or datetimeHour_ASC for longer ranges
      ) {
        count
        dimensions { datetimeFiveMinutes }
        sum { edgeResponseBytes }
        ratio { status4xx status5xx }
      }
    }
  }
}
```

