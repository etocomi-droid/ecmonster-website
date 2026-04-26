## Aggregation Fields

Aggregated dataset nodes (`*Groups`) return these field categories. Not every node has all — use introspection to check.

### count

Total events in the group. Available on `*Groups` nodes but **not** on raw `*Adaptive` nodes (e.g., `workersInvocationsAdaptive` — use `sum { requests }` instead).

### sum

Cumulative metrics. Fields vary by dataset:

```graphql
# HTTP requests
sum { edgeResponseBytes edgeRequestBytes visits edgeTimeToFirstByteMs originResponseDurationMs }

# Workers invocations
sum { requests errors subrequests cpuTimeUs wallTime duration responseBodySize clientDisconnects requestDuration }
```

### quantiles

Percentile distributions (on datasets like `workersInvocationsAdaptive`). Available percentiles: P25, P50, P75, P90, P95, P99, P999 for `cpuTime`, `wallTime`, `requestDuration`, `duration`, `responseBodySize`.

```graphql
quantiles { cpuTimeP50 cpuTimeP99 wallTimeP50 wallTimeP99 }
```

### ratio, avg, uniq, confidence

```graphql
ratio { status4xx status5xx }      # float64 (0 to 1) -- HTTP datasets only
avg { sampleInterval }              # useful for understanding sampling resolution
uniq { uniques }                    # unique IP count -- rollup datasets (*1hGroups, *1dGroups) only
confidence(level: 0.95) {           # Adaptive datasets only; works on count and sum fields
  count { estimate lower upper sampleSize }
}
```

