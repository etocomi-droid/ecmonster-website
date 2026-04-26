## Error Tracking

```typescript
env.ANALYTICS.writeDataPoint({
  blobs: [error.name, request.url, request.method],
  doubles: [1],
  indexes: [error.name]
});
```

