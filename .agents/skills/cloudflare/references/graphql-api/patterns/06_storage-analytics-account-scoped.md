## Storage Analytics (Account-Scoped)

R2, KV, and D1 use `date` (Date type) filters instead of `datetime` (Time type).

```graphql
# R2 operations
r2OperationsAdaptiveGroups(filter: { date_geq: $start, date_leq: $end }, limit: 100, orderBy: [date_DESC]) {
  dimensions { date bucketName actionType }
  sum { requests }
}

# KV operations
kvOperationsAdaptiveGroups(filter: { date_geq: $start, date_leq: $end }, limit: 100, orderBy: [date_DESC]) {
  dimensions { date actionType }
  sum { requests }
}

# D1 analytics
d1AnalyticsAdaptiveGroups(filter: { date_geq: $start, date_leq: $end }, limit: 100, orderBy: [date_DESC]) {
  dimensions { date databaseId }
  sum { readQueries writeQueries rowsRead rowsWritten }
}
```

