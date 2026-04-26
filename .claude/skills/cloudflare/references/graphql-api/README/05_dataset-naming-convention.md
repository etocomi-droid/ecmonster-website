## Dataset Naming Convention

Dataset names follow a consistent pattern visible in the schema:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `*Adaptive` | Raw rows with adaptive sampling; some (e.g., `workersInvocationsAdaptive`) also support aggregation fields (`sum`, `quantiles`, `avg`) | `httpRequestsAdaptive`, `workersInvocationsAdaptive` |
| `*AdaptiveGroups` | Aggregated data with adaptive sampling | `httpRequestsAdaptiveGroups` |
| `*1hGroups` | Hourly rollups (pre-aggregated) | `httpRequests1hGroups` |
| `*1dGroups` | Daily rollups (pre-aggregated) | `httpRequests1dGroups` |
| `*1mGroups` | Minutely rollups | `httpRequests1mGroups` |
| `Zone*` prefix | Zone-scoped dataset | `ZoneHttpRequestsAdaptiveGroups` |
| `Account*` prefix | Account-scoped dataset | `AccountWorkersInvocationsAdaptive` |

**Prefer `*AdaptiveGroups` nodes** for most use cases - they support flexible time grouping via dimension fields (`datetimeFiveMinutes`, `datetimeHour`, etc.) and are the most commonly used.

