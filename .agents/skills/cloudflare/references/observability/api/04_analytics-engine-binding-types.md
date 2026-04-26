### Analytics Engine Binding Types

```typescript
interface AnalyticsEngineDataset {
  writeDataPoint(event: AnalyticsEngineDataPoint): void;
}

interface AnalyticsEngineDataPoint {
  // Indexed strings (use for filtering/grouping)
  indexes?: string[];
  
  // Non-indexed strings (metadata, IDs, URLs)
  blobs?: string[];
  
  // Numeric values (counts, durations, amounts)
  doubles?: number[];
}
```

**Field Limits**:
- Max 20 indexes
- Max 20 blobs
- Max 20 doubles
- Max 25 `writeDataPoint` calls per request

