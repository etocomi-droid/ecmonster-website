## TypeScript Types

```typescript
import type { RealtimeKitClient, States, UIConfig, Participant } from '@cloudflare/realtimekit';

// Main interface
interface RealtimeKitClient {
  self: SelfState;          // Local participant (id, userId, name, audioEnabled, videoEnabled, roomJoined, roomState)
  participants: { joined, active, waitlisted, pinned };  // Reactive Maps
  chat: ChatNamespace;      // messages[], sendTextMessage(), sendImageMessage()
  polls: PollsNamespace;    // items[], create(), vote()
  plugins: PluginsNamespace;  // all[], activate(), deactivate()
  ai: AINamespace;          // transcripts[]
  meta: MetaState;          // meetingId, meetingTitle, meetingStartedTimestamp
  join(): Promise<void>;
  leave(): Promise<void>;
}

// Participant (self & remote share same shape)
interface Participant {
  id: string;                      // Peer ID (changes on rejoin)
  userId: string;                  // Persistent participant ID
  name: string;
  audioEnabled: boolean;
  videoEnabled: boolean;
  screenShareEnabled: boolean;
  audioTrack: MediaStreamTrack | null;
  videoTrack: MediaStreamTrack | null;
  screenShareTracks: MediaStreamTrack[];
}
```

