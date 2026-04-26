## React Stream Player

`npm install @cloudflare/stream-react`

```tsx
import { Stream } from '@cloudflare/stream-react';

export function VideoPlayer({ videoId, token }: { videoId: string; token?: string }) {
  return <Stream controls src={token ? `${videoId}?token=${token}` : videoId} responsive />;
}
```

