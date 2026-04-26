## Local Development Limits

```typescript
// ❌ Miniflare/wrangler dev: Limited R2 support
// - No multipart uploads
// - No presigned URLs (requires S3 SDK + network)
// - Memory-backed storage (lost on restart)

// ✅ Use remote bindings for full features
wrangler dev --remote

// OR: Conditional logic
if (env.ENVIRONMENT === 'development') {
  // Fallback for local dev
} else {
  // Full R2 features
}
```

