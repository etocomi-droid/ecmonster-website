## ICE Restart Required Scenarios

These events require ICE restart (see [patterns.md](./patterns.md#ice-restart-pattern)):

1. **TURN server maintenance** (occasional on Cloudflare's network)
2. **Network topology changes** (anycast routing changes)
3. **Credential refresh** during long sessions (>1 hour)
4. **Connection failure** (iceConnectionState === 'failed')

Implement in all production apps:

```typescript
pc.addEventListener('iceconnectionstatechange', async () => {
  if (pc.iceConnectionState === 'failed' || 
      pc.iceConnectionState === 'disconnected') {
    await refreshTURNCredentials(pc);
    pc.restartIce();
    const offer = await pc.createOffer({ iceRestart: true });
    await pc.setLocalDescription(offer);
    // Send offer to peer via signaling...
  }
});
```

Reference: [RFC 8445 Section 2.4](https://datatracker.ietf.org/doc/html/rfc8445#section-2.4)

