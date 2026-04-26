## Common Errors

### "Slow initial connect (~1.8s)"

**Cause:** First STUN delayed during consensus forming (normal behavior)
**Solution:** Subsequent connections are faster. CF detects DTLS ClientHello early to compensate.

### "No media flow"

**Cause:** SDP exchange incomplete, connection not established, tracks not added before offer, browser permissions missing
**Solution:** 
1. Verify SDP exchange complete
2. Check `pc.connectionState === 'connected'`
3. Ensure tracks added before creating offer
4. Confirm browser permissions granted
5. Use `chrome://webrtc-internals` for debugging

### "Track not receiving"

**Cause:** Track not published, track ID not shared, session IDs mismatch, `pc.ontrack` not set, renegotiation needed
**Solution:** 
1. Verify track published successfully
2. Confirm track ID shared between peers
3. Check session IDs match
4. Set `pc.ontrack` handler before answer
5. Trigger renegotiation if needed

### "ICE connection failed"

**Cause:** Network changed, firewall blocked UDP, TURN needed, transient network issue
**Solution:**
```typescript
pc.oniceconnectionstatechange = async () => {
  if (pc.iceConnectionState === 'failed') {
    console.warn('ICE failed, attempting restart');
    await pc.restartIce(); // Triggers new ICE gathering
    
    // Create new offer with ICE restart flag
    const offer = await pc.createOffer({iceRestart: true});
    await pc.setLocalDescription(offer);
    
    // Send to backend → Cloudflare API
    await fetch(`/api/sessions/${sessionId}/renegotiate`, {
      method: 'PUT',
      body: JSON.stringify({sdp: offer.sdp})
    });
  }
};
```

### "Track stuck/frozen"

**Cause:** Sender paused track, network congestion, codec mismatch, mobile browser backgrounded
**Solution:**
1. Check `track.enabled` and `track.readyState === 'live'`
2. Verify sender active: `pc.getSenders().find(s => s.track === track)`
3. Check stats for packet loss/jitter (see patterns.md)
4. On mobile: Re-acquire tracks when app foregrounded
5. Test with different codecs if persistent

### "Network change disconnects call"

**Cause:** Mobile switching WiFi↔cellular, laptop changing networks
**Solution:**
```typescript
// Listen for network changes
if ('connection' in navigator) {
  (navigator as any).connection.addEventListener('change', async () => {
    console.log('Network changed');
    await pc.restartIce(); // Use ICE restart pattern above
  });
}

// Or use PartyTracks (handles automatically)
```

