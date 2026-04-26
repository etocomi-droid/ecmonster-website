## Direct Upload / Live / Watermark Config

```typescript
// Direct upload
const uploadConfig = {
  maxDurationSeconds: 3600,
  expiry: new Date(Date.now() + 3600000).toISOString(),
  requireSignedURLs: true,
  allowedOrigins: ['https://yourdomain.com'],
  meta: { creator: 'user-123' }
};

// Live input
const liveConfig = {
  recording: { mode: 'automatic', timeoutSeconds: 30 },
  deleteRecordingAfterDays: 30
};

// Watermark
const watermark = {
  name: 'Logo', opacity: 0.7, padding: 20,
  position: 'lowerRight', scale: 0.15
};
```

