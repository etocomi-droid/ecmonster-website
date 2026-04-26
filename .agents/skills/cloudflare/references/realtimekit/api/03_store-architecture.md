## Store Architecture

RealtimeKit uses reactive store (event-driven updates, live Maps):

```typescript
// Subscribe to state changes
meeting.self.on('audioUpdate', ({ audioEnabled, audioTrack }) => {});
meeting.participants.joined.on('participantJoined', (p) => {});

// Access current state synchronously
const isAudioOn = meeting.self.audioEnabled;
const count = meeting.participants.joined.size();
```

**Key principles:** State updates emit events after changes. Use `.toArray()` sparingly. Collections are live Maps.

