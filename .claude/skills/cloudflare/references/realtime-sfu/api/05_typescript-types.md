## TypeScript Types

```typescript
interface TrackMetadata {
  trackName: string;
  location: "local" | "remote";
  sessionId?: string; // For remote tracks
  mid?: string; // WebRTC mid
}
```

