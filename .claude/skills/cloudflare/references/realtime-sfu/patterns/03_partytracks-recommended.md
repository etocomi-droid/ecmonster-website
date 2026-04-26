## PartyTracks (Recommended)

Observable-based client with automatic device/network handling:

```typescript
import {PartyTracks} from 'partytracks';

// Create client
const pt = new PartyTracks({
  apiUrl: '/api/calls',
  sessionId: 'my-session',
  onTrack: (track, peer) => {
    const video = document.getElementById(`video-${peer.id}`) as HTMLVideoElement;
    video.srcObject = new MediaStream([track]);
  }
});

// Publish camera (push API)
const camera = await pt.getCamera(); // Auto-requests permissions, handles device changes
await pt.publishTrack(camera, {trackName: 'my-camera'});

// Subscribe to remote track (pull API)
await pt.subscribeToTrack({trackName: 'remote-camera', sessionId: 'other-session'});

// React hook example
import {useObservableAsValue} from 'observable-hooks';

function VideoCall() {
  const localTracks = useObservableAsValue(pt.localTracks$);
  const remoteTracks = useObservableAsValue(pt.remoteTracks$);
  
  return <div>{/* Render tracks */}</div>;
}

// Screenshare
const screen = await pt.getScreenshare();
await pt.publishTrack(screen, {trackName: 'my-screen'});

// Handle device changes (automatic)
// PartyTracks detects device changes (e.g., Bluetooth headset) and renegotiates
```

