## Wrangler Setup

```jsonc
{
  "name": "my-calls-app",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01", // Use current date for new projects
  "vars": {
    "CALLS_APP_ID": "your-app-id",
    "MAX_WEBCAM_BITRATE": "1200000",
    "MAX_WEBCAM_FRAMERATE": "24",
    "MAX_WEBCAM_QUALITY_LEVEL": "1080"
  },
  // Set secret: wrangler secret put CALLS_APP_SECRET
  "durable_objects": {
    "bindings": [
      {
        "name": "ROOM",
        "class_name": "Room"
      }
    ]
  }
}
```

