## Audio-Only Mode

```typescript
const meeting = new RealtimeKitClient({
  authToken: '<token>',
  video: false,  // Disable video
  audio: true,
  mediaConfiguration: {
    audio: {
      echoCancellation: true,
      noiseSuppression: true,
      autoGainControl: true
    }
  }
});

// Use audio grid component
import { RtkAudioGrid } from '@cloudflare/realtimekit-react-ui';
<RtkAudioGrid meeting={meeting} />
```

