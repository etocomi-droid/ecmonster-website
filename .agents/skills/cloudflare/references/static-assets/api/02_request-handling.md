## Request Handling

### Path Resolution

```typescript
// All resolve to same asset:
env.ASSETS.fetch("https://example.com/logo.png")
env.ASSETS.fetch("https://ignored.host/logo.png")
env.ASSETS.fetch("/logo.png")
```

Assets are resolved relative to configured `assets.directory`.

### Headers

Request headers that affect response:

| Header | Effect |
|--------|--------|
| `Accept-Encoding` | Controls compression (gzip, brotli) |
| `Range` | Enables partial content (206 responses) |
| `If-None-Match` | Conditional request via ETag |
| `If-Modified-Since` | Conditional request via modification date |

Custom headers pass through but don't affect asset serving.

### Method Support

| Method | Supported | Response |
|--------|-----------|----------|
| `GET` | ✅ Yes | Asset content |
| `HEAD` | ✅ Yes | Headers only, no body |
| `POST`, `PUT`, etc. | ❌ No | 405 Method Not Allowed |

