## WebRTC Flow

```typescript
// 1. Create PeerConnection
const pc = new RTCPeerConnection({
  iceServers: [{urls: 'stun:stun.cloudflare.com:3478'}]
});

// 2. Add tracks
const stream = await navigator.mediaDevices.getUserMedia({video: true, audio: true});
stream.getTracks().forEach(track => pc.addTrack(track, stream));

// 3. Create offer
const offer = await pc.createOffer();
await pc.setLocalDescription(offer);

// 4. Send to backend → Cloudflare API
const response = await fetch('/api/new-session', {
  method: 'POST',
  body: JSON.stringify({sdp: offer.sdp})
});

// 5. Set remote answer
const {sessionDescription} = await response.json();
await pc.setRemoteDescription(sessionDescription);
```

