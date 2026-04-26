## Core Concepts

| Concept | Description |
|---------|-------------|
| **Endpoint** | `POST https://api.cloudflare.com/client/v4/graphql` |
| **Explorer** | [graphql.cloudflare.com](https://graphql.cloudflare.com/) - interactive query builder |
| **Viewer** | Root query object: `viewer { zones(...) { ... } }` or `viewer { accounts(...) { ... } }` |
| **Dataset (Node)** | A queryable table under a zone or account (e.g., `httpRequestsAdaptiveGroups`) |
| **Dimensions** | Fields to group by (time buckets, country, status code, script name, etc.) |
| **Metrics** | Aggregation fields: `count`, `sum { ... }`, `avg { ... }`, `quantiles { ... }`, `ratio { ... }` |
| **Filter** | Input object constraining results by time range, dimensions, etc. |
| **Limit** | Maximum rows returned per dataset node (required, max varies by dataset) |
| **OrderBy** | Enum-based sorting: `[field_ASC]` or `[field_DESC]` |
| **Adaptive Sampling** | Nodes with `Adaptive` in the name use ABR sampling; results are statistically representative |

