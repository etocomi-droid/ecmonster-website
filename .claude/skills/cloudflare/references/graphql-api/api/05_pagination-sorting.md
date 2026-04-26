## Pagination & Sorting

No cursor-based pagination. Use `limit`, `orderBy`, and filter-based offsets:

```graphql
# First page
httpRequestsAdaptiveGroups(filter: { datetime_gt: "..." }, limit: 100, orderBy: [datetime_ASC])

# Next page: filter by last seen value from previous page
httpRequestsAdaptiveGroups(filter: { datetime_gt: "2025-01-01T01:35:00Z" }, limit: 100, orderBy: [datetime_ASC])
```

Sort with `orderBy: [field_ASC]` or `[field_DESC]`. Multiple sort fields supported.

