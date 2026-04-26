## WebRTC Streaming (WHIP/WHEP)

### Browser to Stream (WHIP)

```typescript
async function startWebRTCBroadcast(liveInputId: string) {
  const pc = new RTCPeerConnection();
  
  // Add local media tracks
  const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
  stream.getTracks().forEach(track => pc.addTrack(track, stream));
  
  // Create offer
  const offer = await pc.createOffer();
  await pc.setLocalDescription(offer);
  
  // Send to Stream via WHIP
  const response = await fetch(
    `https://customer-<CODE>.cloudflarestream.com/${liveInputId}/webRTC/publish`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/sdp' },
      body: offer.sdp
    }
  );
  
  const answer = await response.text();
  await pc.setRemoteDescription({ type: 'answer', sdp: answer });
}
```

### Stream to Browser (WHEP)

```typescript
async function playWebRTCStream(videoId: string) {
  const pc = new RTCPeerConnection();
  
  pc.addTransceiver('video', { direction: 'recvonly' });
  pc.addTransceiver('audio', { direction: 'recvonly' });
  
  const offer = await pc.createOffer();
  await pc.setLocalDescription(offer);
  
  const response = await fetch(
    `https://customer-<CODE>.cloudflarestream.com/${videoId}/webRTC/play`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/sdp' },
      body: offer.sdp
    }
  );
  
  const answer = await response.text();
  await pc.setRemoteDescription({ type: 'answer', sdp: answer });
  
  return pc;
}
```

