## Debugging Tips

```typescript
// Check devices
const devices = await meeting.self.getAllDevices();
meeting.self.on('deviceListUpdate', ({ added, removed, devices }) => console.log('Devices:', { added, removed, devices }));

// Monitor participants
meeting.participants.joined.on('participantJoined', (p) => console.log(`${p.name} joined:`, { id: p.id, userId: p.userId, audioEnabled: p.audioEnabled, videoEnabled: p.videoEnabled }));

// Check room state
meeting.self.on('roomJoined', () => console.log('Room:', { meetingId: meeting.meta.meetingId, meetingTitle: meeting.meta.meetingTitle, participantCount: meeting.participants.joined.size() + 1, audioEnabled: meeting.self.audioEnabled, videoEnabled: meeting.self.videoEnabled }));

// Log all events
['roomJoined', 'audioUpdate', 'videoUpdate', 'screenShareUpdate', 'deviceUpdate', 'deviceListUpdate'].forEach(event => meeting.self.on(event, (data) => console.log(`[self] ${event}:`, data)));
['participantJoined', 'participantLeft'].forEach(event => meeting.participants.joined.on(event, (data) => console.log(`[participants] ${event}:`, data)));
meeting.chat.on('chatUpdate', (data) => console.log('[chat] chatUpdate:', data));
```

