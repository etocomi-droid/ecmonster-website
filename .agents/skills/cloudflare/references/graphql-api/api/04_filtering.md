## Filtering

### Scope Filters

```graphql
zones(filter: { zoneTag: "ZONE_ID" })           # up to 10 zones
zones(filter: { zoneTag_in: ["Z1", "Z2"] })
accounts(filter: { accountTag: "ACCOUNT_ID" })   # exactly 1 account
```

### Dataset Filters

**Always include a time range filter.** Multiple filters at the same level are implicitly AND-ed.

```graphql
httpRequestsAdaptiveGroups(
  filter: { datetime_gt: "2025-01-01T00:00:00Z", datetime_lt: "2025-01-02T00:00:00Z", clientCountryName: "US" }
  limit: 1000
)
```

### Filter Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| (none) | equals | `clientCountryName: "US"` |
| `_gt` / `_lt` | greater / less than | `datetime_gt: "..."` |
| `_geq` / `_leq` | greater/less or equal | `datetime_geq: "..."` |
| `_neq` | not equal | `cacheStatus_neq: "hit"` |
| `_in` / `_notin` | in / not in list | `clientCountryName_in: ["US", "GB"]` |
| `_like` / `_notlike` | SQL LIKE with `%` | `clientRequestPath_like: "/api/%"` |
| `_has` / `_hasall` / `_hasany` | array contains | `botDetectionIds_has: "abc"` |

> `_notin` and `_notlike` are in the schema but not in official docs. Confirmed via introspection.

### Boolean Operators (AND / OR)

```graphql
# Explicit AND
filter: { AND: [{ datetime_gt: "..." }, { datetime_lt: "..." }, { clientCountryName: "US" }] }

# Explicit OR
filter: { datetime_gt: "...", OR: [{ edgeResponseStatus: 403 }, { edgeResponseStatus: 429 }] }
```

