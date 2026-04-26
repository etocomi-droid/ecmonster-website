## Subscribing

```typescript
const res = await fetch(`/api/sessions/${sessionId}/tracks`, {
  method: 'POST',
  body: JSON.stringify({
    tracks: [{location: 'remote', trackName: remoteTrackId, sessionId: remoteSessionId}]
  })
});

const {sessionDescription} = await res.json();
await pc.setRemoteDescription(sessionDescription);

const answer = await pc.createAnswer();
await pc.setLocalDescription(answer);

await fetch(`/api/sessions/${sessionId}/renegotiate`, {
  method: 'PUT',
  body: JSON.stringify({sdp: answer.sdp})
});

pc.ontrack = (event) => {
  const [remoteStream] = event.streams;
  videoElement.srcObject = remoteStream;
};
```
