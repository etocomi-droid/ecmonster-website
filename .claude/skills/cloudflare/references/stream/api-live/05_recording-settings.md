## Recording Settings

| Mode | Behavior |
|------|----------|
| `automatic` | Record all live streams |
| `off` | No recording |
| `timeoutSeconds` | Stop recording after N seconds of inactivity |

```typescript
const recordingConfig = {
  mode: 'automatic',
  timeoutSeconds: 30, // Auto-stop 30s after stream ends
  requireSignedURLs: true, // Require token for VOD playback
  allowedOrigins: ['https://yourdomain.com']
};
```

