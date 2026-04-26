## ICE Restart Pattern

After network change, TURN server maintenance, or credential expiry:

```typescript
pc.addEventListener('iceconnectionstatechange', async () => {
  if (pc.iceConnectionState === 'failed') {
    console.warn('ICE connection failed, restarting...');
    
    // Refresh credentials
    await refreshTURNCredentials(pc);
    
    // Trigger ICE restart
    pc.restartIce();
    const offer = await pc.createOffer({ iceRestart: true });
    await pc.setLocalDescription(offer);
    
    // Send offer to peer via signaling channel...
  }
});
```

