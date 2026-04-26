## Validation Function

```typescript
function validateRTCIceServer(obj: unknown): obj is RTCIceServer {
  if (!obj || typeof obj !== 'object') {
    return false;
  }

  const server = obj as Record<string, unknown>;

  if (typeof server.urls !== 'string' && !Array.isArray(server.urls)) {
    return false;
  }

  if (server.username && typeof server.username !== 'string') {
    return false;
  }

  if (server.credential && typeof server.credential !== 'string') {
    return false;
  }

  return true;
}
```

