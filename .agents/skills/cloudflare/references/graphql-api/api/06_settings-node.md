## Settings Node

Query per-node limits and availability:

```graphql
viewer { zones(filter: { zoneTag: "..." }) { settings {
  httpRequestsAdaptiveGroups { enabled maxDuration maxNumberOfFields maxPageSize notOlderThan }
} } }
```

