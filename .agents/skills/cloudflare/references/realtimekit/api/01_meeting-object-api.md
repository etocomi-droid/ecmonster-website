## Meeting Object API

### `meeting.self` - Local Participant

```typescript
// Properties: id, userId, name, audioEnabled, videoEnabled, screenShareEnabled, audioTrack, videoTrack, screenShareTracks, roomJoined, roomState
// Methods
await meeting.self.enableAudio() / disableAudio() / enableVideo() / disableVideo() / enableScreenShare() / disableScreenShare()
await meeting.self.setName("Name")  // Before join only
await meeting.self.setDevice(device)
const devices = await meeting.self.getAllDevices() / getAudioDevices() / getVideoDevices() / getSpeakerDevices()
// Events: 'roomJoined', 'audioUpdate', 'videoUpdate', 'screenShareUpdate', 'deviceUpdate', 'deviceListUpdate'
meeting.self.on('roomJoined', () => {})
meeting.self.on('audioUpdate', ({ audioEnabled, audioTrack }) => {})
```

### `meeting.participants` - Remote Participants

**Collections**:
```typescript
meeting.participants.joined / active / waitlisted / pinned  // Maps
const participants = meeting.participants.joined.toArray()
const count = meeting.participants.joined.size()
const p = meeting.participants.joined.get('peer-id')
```

**Participant Properties**:
```typescript
participant.id / userId / name
participant.audioEnabled / videoEnabled / screenShareEnabled
participant.audioTrack / videoTrack / screenShareTracks
```

**Events**:
```typescript
meeting.participants.joined.on('participantJoined', (participant) => {})
meeting.participants.joined.on('participantLeft', (participant) => {})
```

### `meeting.meta` - Metadata
```typescript
meeting.meta.meetingId / meetingTitle / meetingStartedTimestamp
```

### `meeting.chat` - Chat
```typescript
meeting.chat.messages  // Array
await meeting.chat.sendTextMessage("Hello") / sendImageMessage(file)
meeting.chat.on('chatUpdate', ({ message, messages }) => {})
```

### `meeting.polls` - Polling
```typescript
meeting.polls.items  // Array
await meeting.polls.create(question, options, anonymous, hideVotes)
await meeting.polls.vote(pollId, optionIndex)
```

### `meeting.plugins` - Collaborative Apps
```typescript
meeting.plugins.all  // Array
await meeting.plugins.activate(pluginId) / deactivate()
```

### `meeting.ai` - AI Features
```typescript
meeting.ai.transcripts  // Live transcriptions (when enabled in Preset)
```

### Core Methods
```typescript
await meeting.join()   // Emits 'roomJoined' on meeting.self
await meeting.leave()
```

