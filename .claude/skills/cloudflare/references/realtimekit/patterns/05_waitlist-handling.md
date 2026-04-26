## Waitlist Handling

```typescript
// Monitor waitlist
meeting.participants.waitlisted.on('participantJoined', (participant) => {
  console.log(`${participant.name} is waiting`);
  // Show admin UI to approve/reject
});

// Approve from waitlist (backend only)
await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${accountId}/realtime/kit/${appId}/meetings/${meetingId}/active-session/waitlist/approve`,
  {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${apiToken}` },
    body: JSON.stringify({ user_ids: [participant.userId] })
  }
);

// Client receives automatic transition when approved
meeting.self.on('roomJoined', () => console.log('Approved and joined'));
```

