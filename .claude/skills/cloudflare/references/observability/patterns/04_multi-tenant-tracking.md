## Multi-Tenant Tracking

```typescript
env.ANALYTICS.writeDataPoint({
  indexes: [tenantId], // efficient filtering
  blobs: [tenantId, url.pathname, method, status],
  doubles: [1, duration, bytesSize]
});
```

