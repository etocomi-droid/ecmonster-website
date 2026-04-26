## React Hooks (Official)

```typescript
import { useRealtimeKitClient, useRealtimeKitSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  const [meeting, initMeeting] = useRealtimeKitClient();
  const audioEnabled = useRealtimeKitSelector(m => m.self.audioEnabled);
  const participantCount = useRealtimeKitSelector(m => m.participants.joined.size());
  
  useEffect(() => { initMeeting({ authToken: '<token>' }); }, []);
  
  return <div>
    <button onClick={() => meeting?.self.enableAudio()}>{audioEnabled ? 'Mute' : 'Unmute'}</button>
    <span>{participantCount} participants</span>
  </div>;
}
```

**Benefits:** Automatic re-renders, memoized selectors, type-safe

