## Playback APIs

### Embed Player (iframe)

```html
<iframe
  src="https://customer-<CODE>.cloudflarestream.com/<VIDEO_ID>/iframe?autoplay=true&muted=true"
  style="border: none;" height="720" width="1280"
  allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;"
  allowfullscreen="true"
></iframe>
```

### HLS/DASH Manifest URLs

```typescript
// HLS
const hlsUrl = `https://customer-<CODE>.cloudflarestream.com/${videoId}/manifest/video.m3u8`;

// DASH
const dashUrl = `https://customer-<CODE>.cloudflarestream.com/${videoId}/manifest/video.mpd`;
```

### Thumbnails

```typescript
// At specific time (seconds)
const thumb = `https://customer-<CODE>.cloudflarestream.com/${videoId}/thumbnails/thumbnail.jpg?time=10s`;

// By percentage
const thumbPct = `https://customer-<CODE>.cloudflarestream.com/${videoId}/thumbnails/thumbnail.jpg?time=50%`;

// Animated GIF
const gif = `https://customer-<CODE>.cloudflarestream.com/${videoId}/thumbnails/thumbnail.gif`;
```

