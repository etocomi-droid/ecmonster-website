## Publishing

```typescript
const offer = await pc.createOffer();
await pc.setLocalDescription(offer);

const res = await fetch(`/api/sessions/${sessionId}/tracks`, {
  method: 'POST',
  body: JSON.stringify({
    sdp: offer.sdp,
    tracks: [{location: 'local', trackName: 'my-video'}]
  })
});

const {sessionDescription, tracks} = await res.json();
await pc.setRemoteDescription(sessionDescription);
const publishedTrackId = tracks[0].trackName; // Share with others
```

