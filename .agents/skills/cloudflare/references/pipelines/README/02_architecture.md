## Architecture

```
Data Sources → Streams → Pipelines (SQL) → Sinks → R2
                 ↑          ↓                ↓
            HTTP/Workers  Transform     Iceberg/Parquet
```

| Component | Purpose | Key Feature |
|-----------|---------|-------------|
| Streams | Event ingestion | Structured (validated) or unstructured |
| Pipelines | Transform with SQL | Immutable after creation |
| Sinks | Write to R2 | Exactly-once delivery |

