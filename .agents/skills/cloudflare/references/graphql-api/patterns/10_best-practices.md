## Best Practices

**Always include time filters.** Queries without time filters scan all data and are slow/expensive.

**Match time granularity to range:**

| Time Range | Recommended Dimension |
|------------|----------------------|
| < 6 hours | `datetimeMinute` or `datetimeFiveMinutes` |
| 6-48 hours | `datetimeFiveMinutes` or `datetimeFifteenMinutes` |
| 2-14 days | `datetimeHour` |
| 14+ days | `date` |

**Use aliases** for querying the same dataset with different filters in one request.

**Request only needed fields.** Extra dimensions and metrics increase query cost.

